#!/usr/bin/env python3
"""Bind the NF648 three local moment proofs to all 120 physical Gram
entries at actual source indices 0..13 and 241, using retained NF631 radii.
No full-bank truth, no substitute source, no global positivity claim.
Generate NF648 proof proposals first with --group omitted.
"""
import argparse,gzip,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from emit_nf627_original_moment_bank import filetext, scaled
from verify_nf620_physical_key_tables import canonical
from verify_nf622_physical_entry_reassembly import read_shards,selected
from verify_nf631_reference_entry_widening import reference_entry
BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalLocalGramBlock'
MODULE='WeilDefect.Generated.NF649'
MOM='WeilDefect.Generated.NF648'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
INDICES=list(range(14))+[241]
KEYS=[(F(1),F(0)),(F(0),F(37,32)),(F(1,2),F(37,64))]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser()
    for k in ('root','shards','moments','entries','summary','output'): ap.add_argument('--'+k,type=Path,required=True)
    a=ap.parse_args(); a.output.mkdir(parents=True,exist_ok=True)
    m=json.loads((a.moments/'manifest.json').read_text())
    assert m['schema']=='NF648-ten-leaf-local-moment-proposals-v1'
    assert m['group'] is None and m['rows']==42 and m['leaf_count']==10
    for x in m['files']: assert sha(a.moments/x['file'])==x['sha256']
    summary=json.loads(a.summary.read_text())
    hashes={p.name:sha(p) for p in a.shards.rglob('nf621-shard*.json.gz')}
    assert len(hashes)==8 and hashes==m['input_sha256']==summary['input_sha256']
    assert summary['schema']=='NF631-reference-widening-v1'
    assert sha(a.entries)==summary['widened_entry_sha256']
    full=read_shards(a.root,a.shards)
    data={k:full[k] for k in KEYS}
    assert [len(data[k]) for k in KEYS]==[1,27,14]
    S=selected(a.root)
    assert len(S)==242
    assert all({(h,abs(f),n) for h,f,n,c,d in S[i]}=={(F(0),F(37,64),i)} for i in range(14))
    assert {(h,f,n) for h,f,n,c,d in S[241]}=={(F(1,2),F(0),0),(F(-1,2),F(0),0)}
    retained={}
    with gzip.open(a.entries,'rt') as fh:
        head=json.loads(next(fh))
        assert head['schema']=='NF622-original-physical-entry-balls-v1' and head['scale']=='10^2600'
        assert head['original_entry_sha256']==summary['original_entry_sha256']
        for i,line in enumerate(fh):
            q=json.loads(line); assert q['row']==i and len(q['H_lower'])==i+1
            if i in INDICES:
                for j in INDICES:
                    if j<=i: retained[i,j]=tuple(map(int,q['H_lower'][j]))
    assert len(retained)==120
    files=[]
    def write(name,imports,body):
        p=a.output/(name+'.lean')
        p.write_text(filetext(imports,OPT+body))
        files.append({'file':p.name,'sha256':sha(p)})
    body='''def nf649Bank : Array NF624KeyTable :=
  #[nf648PoleTable,nf648OscTable,nf648MixedTable]

def nf649Index (k : NF616Frequency) : ℕ :=
  if k.h=1 ∧ k.f=0 then 0
  else if k.h=0 ∧ k.f=37/32 then 1
  else if k.h=1/2 ∧ k.f=37/64 then 2
  else 3

theorem nf649BankSound : ∀ i < nf649Bank.size,
    ∀ n < (neutralNF624BankRead nf649Bank i).rows.size,
    ‖neutralNF620J (neutralNF624BankRead nf649Bank i).key.value n -
      (neutralNF617MomentRead (neutralNF624BankRead nf649Bank i).rows n).value‖ ≤
      (neutralNF617MomentRead (neutralNF624BankRead nf649Bank i).rows n).rad := by
  intro i hi n hn
  have hs : nf649Bank.size=3 := by rfl
  rw [hs] at hi
  have hh : i=0 ∨ i=1 ∨ i=2 := by omega
  rcases hh with rfl | rfl | rfl
  · exact nf648PoleMoment n hn
  · exact nf648OscMoment n hn
  · exact nf648MixedMoment n hn

#print axioms nf649BankSound
'''
    write('Bank',[BASE]+[MOM+'.'+g for g in ('Pole','Osc','Mixed')],body)
    pair_count=zero_count=0; keys=set(); zero_degrees=set()
    for i in INDICES:
        body=''
        for j in INDICES:
            if j>i: continue
            for h,f,n,c,d in S[i]:
                for u,g,l,e,v in S[j]:
                    k=canonical(h+u,f+g); degree=n+l; pair_count+=1
                    if k==(0,0):
                        zero_count+=1; zero_degrees.add(degree)
                    else:
                        assert k in data and degree<len(data[k])
                        keys.add(k)
            x,r=retained[i,j]
            y,s=reference_entry(data,S[i],S[j])
            assert r>=0 and s>=0 and abs(x-y)+s<=r
            assert abs(x-y)+s>0
            v=f'nf649H{i:03d}_{j:03d}'
            body+=f'def {v}Ball : NF591Ball := ⟨{scaled(x)},{scaled(r)}⟩\n'
            body+=f'theorem {v}Route : neutralNF649HCheck nf649Bank nf649Index {i} {j}=true := by\n  decide +kernel\n'
            body+=f'theorem {v}Widen : neutralNF649WidenH nf649Bank nf649Index {i} {j} {v}Ball=true := by\n  decide +kernel\n'
            body+=f'theorem {v}Contains : {v}Ball.Contains (neutralNF606PhysicalH {i} {j}) :=\n  neutralNF649H_of_local nf649Bank nf649Index nf649BankSound {i} {j} _ {v}Route {v}Widen\n\n'
        write(f'Row{i:03d}',[MODULE+'.Bank'],body)
    assert pair_count==480 and len(keys)==3
    write('Complete',[MODULE+f'.Row{i:03d}' for i in INDICES],
          '#print axioms nf649H000_000Contains\n#print axioms nf649H013_013Contains\n#print axioms nf649H241_000Contains\n#print axioms nf649H241_241Contains')
    result={'schema':'NF649-original-local-gram-block-v1','indices':INDICES,'lower_entries':120,
        'source_pairs':pair_count,'zero_pairs':zero_count,'zero_degrees':sorted(zero_degrees),
        'input_sha256':hashes,'entry_sha256':sha(a.entries),'moment_manifest_sha256':sha(a.moments/'manifest.json'),
        'files':files,'scope':'untrusted local proof proposals, pending kernel truth and NF648 prerequisites'}
    (a.output/'manifest.json').write_text(json.dumps(result,indent=2)+'\n')
    print('NF649 exact retained 120-entry widening comparisons and',pair_count,'source pair routes PASS; kernel proposals emitted')
if __name__=='__main__': main()
