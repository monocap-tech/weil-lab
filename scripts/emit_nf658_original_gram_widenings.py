#!/usr/bin/env python3
"""NF658: original physical H -> certified 64-digit rational intervals.

Every generated theorem is a candidate until a Lean kernel build accepts it.
The inputs are the actual NF631 archived entries and exact NF657 witness.
"""
import argparse,gzip,hashlib,io,json,zipfile,sys
from pathlib import Path
sys.set_int_max_str_digits(0)
I=list(range(14))+[241]
Q=10**2600; S=10**64
ZIP='e91a83cae117e98608aefa6849dac178e4ddb58dd1dffbfe37304ad248af9ed9'
WIT='f884548b04664516a9b508a1ca8ac41cc52ccf0295a959198bf528e561d1c39b'
sha=lambda b:hashlib.sha256(b).hexdigest()
def source(p):
    assert sha(p.read_bytes())==ZIP
    with zipfile.ZipFile(p) as z:
        raw=z.read('nf631-widened-entries.jsonl.gz')
        m=json.loads(z.read('nf631-widening.json'))
    assert m['schema']=='NF631-reference-widening-v1' and sha(raw)==m['widened_entry_sha256']
    rows={}
    with gzip.GzipFile(fileobj=io.BytesIO(raw)) as f:
        h=json.loads(next(f))
        assert h['scale']=='10^2600' and h['original_entry_sha256']==m['original_entry_sha256']
        for i,line in enumerate(f):
            if i not in I:continue
            d=json.loads(line)
            assert d['row']==i and len(d['H_lower'])==i+1
            for j in I:
                if j<=i:
                    a,b=map(int,d['H_lower'][j]);assert b>=0
                    rows[i,j]=a,b
    assert len(rows)==120
    return rows,m
def matrix(name,vals):
    assert len(vals)==15 and all(len(row)==15 for row in vals)
    return 'def '+name+' : Array (Array ℤ) := #[\n'+',\n'.join(
        '  #['+','.join(f'({v}:ℤ)' for v in row)+']' for row in vals)+'\n]\n\n'
def lean(imports,body):
    return ''.join('import '+m+'\n' for m in imports)+'''
namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 0

'''+body+'\nend WeilDefect\n'
def main():
    p=argparse.ArgumentParser()
    for x in ('archive','witness','output'):p.add_argument('--'+x,type=Path,required=True)
    a=p.parse_args()
    wraw=a.witness.read_bytes()
    witness_sha=sha(wraw)
    w=json.loads(wraw)
    assert w['schema']=='NF657-original-15-source-compact-congruence-v1'
    assert w['indices']==I and w['S']=='10^64' and w['Q']=='10^2600'
    rows,m=source(a.archive)
    assert w['widened_entry_sha256']==m['widened_entry_sha256']
    assert w['original_entry_sha256']==m['original_entry_sha256']
    C=[[int(v) for v in row] for row in w['H_center_scaled']]
    E=[[int(v) for v in row] for row in w['H_radius_scaled']]
    K=[[int(v) for v in row] for row in w['K_scaled']]
    d=list(map(int,w['dominance_margin_scaled_numerator']))
    kn=int(w['K_norm_sq_scaled_numerator'])
    assert len(d)==15 and min(d)>0 and min(d)*10**60>S*kn
    assert w['source_archive_sha256']==ZIP
    assert all(K[i][j]==(S if i==j else 0) for i in range(15) for j in range(i,15))
    assert sum(x*x for row in K for x in row)==kn
    for i in range(15):
        margin=0
        for j in range(15):
            center=sum(K[i][p]*K[j][q]*C[p][q] for p in range(15) for q in range(15))
            radius=sum(abs(K[i][p]*K[j][q])*E[p][q] for p in range(15) for q in range(15))
            margin += center-radius if i==j else -(abs(center)+radius)
        assert margin==d[i]
    assert all(C[i][j]==C[j][i] and E[i][j]==E[j][i]>=0
               for i in range(15) for j in range(15))
    a.output.mkdir(parents=True,exist_ok=True);files=[]
    def write(name,imports,body):
        path=a.output/(name+'.lean')
        path.write_text(lean(imports,body))
        files.append({'file':path.name,'sha256':sha(path.read_bytes())})
    body=matrix('nf658Kints',K)+matrix('nf658Centers',C)+matrix('nf658Radii',E)
    body+='def nf658Margins : Array ℤ := #['+','.join(f'({v}:ℤ)' for v in d)+']\n'
    body+=f'def nf658MinMargin : ℤ := {min(d)}\n'
    body+=f'def nf658Ksq : ℤ := {kn}\n'
    body+='''theorem nf658MarginPos : ∀ i : Fin 15,
    0 < nf658Margins[i.val]! := by
  decide +kernel
theorem nf658MinMarginLe : ∀ i : Fin 15,
    nf658MinMargin ≤ nf658Margins[i.val]! := by
  decide +kernel
theorem nf658CoercivityIntegerGate :
    nf658MinMargin * (10^60:ℤ) > (10^64:ℤ) * nf658Ksq := by
  decide +kernel
#print axioms nf658CoercivityIntegerGate
'''
    write('WitnessData',['WeilDefect.Arithmetic.ActualZetaOriginalPhysicalLocalGramBlock'],body)
    checked=0
    for i in I:
        imports=['WeilDefect.Generated.NF658.WitnessData',
                 f'WeilDefect.Generated.NF655.BaseRow{i:03d}']
        if i==241:imports.append('WeilDefect.Generated.NF655.CrossRow241')
        body=''
        for j in I:
            if j>i:continue
            mid,rad=rows[i,j]
            c,e=C[I.index(i)][I.index(j)],E[I.index(i)][I.index(j)]
            assert (c-e)*Q<=(mid-rad)*S and (mid+rad)*S<=(c+e)*Q
            name=f'nf658H{i:03d}_{j:03d}'
            old=f'nf655H{i:03d}_{j:03d}Ball'
            new=name+'Ball'
            cond=f'|{old}.mid - {new}.mid| + {old}.rad ≤ {new}.rad'
            body+=f'def {new} : NF591Ball := ⟨({c}:ℚ)/(10^64:ℚ),({e}:ℚ)/(10^64:ℚ)⟩\n'
            body+=f'theorem {name}Gate : decide ({cond}) = true := by\n  decide +kernel\n'
            body+=f'theorem {name}Widen : {old}.Widens {new} := by\n  change {cond}\n  exact of_decide_eq_true {name}Gate\n'
            body+=f'theorem {name}Contains : {new}.Contains (neutralNF606PhysicalH {i} {j}) :=\n  NF591Ball.contains_widen nf655H{i:03d}_{j:03d}Contains {name}Widen\n'
            body+=f'#print axioms {name}Contains\n\n'
            checked+=1
        write(f'Row{i:03d}',imports,body)
    assert checked==120
    write('Complete',[f'WeilDefect.Generated.NF658.Row{i:03d}' for i in I],
          '-- All 120 actual original H entry interval transfers.\n'+
          '#print axioms nf658H000_000Contains\n#print axioms nf658H241_241Contains')
    report={'schema':'NF658-original-physical-gram-64-digit-attachment-v1',
            'archive_sha256':ZIP,'entry_sha256':m['widened_entry_sha256'],
            'compact_witness_sha256':witness_sha,'original_entry_intervals':checked,
            'exact_scaled_widenings':'PASS','positive_margins':15,
            'coercivity_integer_gate':'PASS','files':files,
            'scope':'actual exact source preflight, candidate Lean proof modules only'}
    (a.output/'manifest.json').write_text(json.dumps(report,indent=2)+'\n')
    print('NF658 original 120 source widenings PASS; 17 Lean proof modules emitted')
if __name__=='__main__':main()
