#!/usr/bin/env python3
"""Reuse accepted NF648 literal inputs; prepare local Gram proof targets.
All files are untrusted until their kernel builds succeed."""
import gzip, hashlib, json, re, sys, zipfile
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
sha=lambda b:hashlib.sha256(b).hexdigest()
A=Path(sys.argv[1]); O=Path(sys.argv[2]); M=O/'NF648'; H=O/'NF655'
M.mkdir(parents=True,exist_ok=True); H.mkdir(parents=True,exist_ok=True)
ARCH={'Pole':'33b2f19bb0d9d502dce88c92a95d6fa7d18e182474c62741f1abeeb2ff81bab2','Osc':'4616be088fef87ea09500ab21596bf250632988845d2c424f73f0a61decac492','Mixed':'1c06748b94a91ae5cbd72c9935d3583ebaf612eea7df072b7c677274ab0a64af'}
KEYS={'Pole':(F(1),F(0)),'Osc':(F(0),F(37,32)),'Mixed':(F(1,2),F(37,64)),'MixedOpp':(F(-1,2),F(37,64))}
rows={}; files={}; shapes=[]; input_hashes=None; pi_hash=None; bank_hash=None
for group,digest in ARCH.items():
    p=A/f'nf648-{group}.zip'; assert sha(p.read_bytes())==digest
    with zipfile.ZipFile(p) as z:
        m=json.loads(z.read('manifest.json')); assert m['group']==group and m['schema']=='NF648-ten-leaf-local-moment-proposals-v1'
        if input_hashes is None: input_hashes=m['input_sha256']; pi_hash=m['pi_manifest_sha256']; bank_hash=m['bank_manifest_sha256']
        assert (input_hashes,pi_hash,bank_hash)==(m['input_sha256'],m['pi_manifest_sha256'],m['bank_manifest_sha256'])
        shapes+=m['groups']; assert m['prefix_checks']==38*m['leaf_count']
        for f in m['files']:
            n=f['file']; b=z.read(n); assert sha(b)==f['sha256']; assert n not in files
            files[n]=f['sha256']; (M/n).write_bytes(b)
assert len(files)==73 and sum(x['rows'] for x in shapes)==42
for i in range(8):
    n=f'nf621-shard{i}.json.gz'
    with zipfile.ZipFile(A/f'nf621-shard{i}.zip') as z: raw=z.read(n)
    assert sha(raw)==input_hashes[n]
    for t in json.loads(gzip.decompress(raw))['tables']:
        k=F(t['h']),F(t['f'])
        if k in KEYS.values(): assert k not in rows; rows[k]=[tuple(map(int,r)) for r in t['rows']]
assert [len(rows[k]) for k in KEYS.values()]==[1,27,14,14]
coord=r'\((-?\d+):ℚ\)/\(neutralNF616Q:ℚ\)'
for g in ARCH:
    s=(M/(g+'.lean')).read_text().split(f'def nf648{g}Table :',1)[1].split('\n\ntheorem',1)[0]
    assert list(map(int,re.findall(coord,s)))==[v for r in rows[KEYS[g]] for v in r]
# Fourth table: reuse identical four certified leaf modules, reverse only real routes.
s=(M/'Mixed.lean').read_text().replace('nf648Mixed','nf648MixedOpp')
lo=s.index('def nf648MixedOppTable :'); hi=s.index('\n\ntheorem',lo)
scaled=lambda x:f'({x}:ℚ)/(neutralNF616Q:ℚ)'
rowlit=lambda r:'⟨'+','.join(map(scaled,r))+'⟩'
body='def nf648MixedOppTable : NF624KeyTable := ⟨⟨(-1/2:ℚ),(37/64:ℚ)⟩, #[\n    '+',\n    '.join(map(rowlit,rows[KEYS['MixedOpp']]))+'\n  ]⟩'
s=s[:lo]+body+s[hi:]
lo=s.index('theorem nf648MixedOppR0Param'); hi=s.index('theorem nf648MixedOppP0Param')
swap={'(1/2:ℚ)':'(-1/2:ℚ)','(-1/2:ℚ)':'(1/2:ℚ)','Real0001':'Real0003','Real0003':'Real0001'}
s=s[:lo]+re.sub(r'\(-?1/2:ℚ\)|Real000[13]',lambda m:swap[m[0]],s[lo:hi])+s[hi:]
(M/'MixedOpp.lean').write_text(s)
assert list(map(int,re.findall(coord,s.split('def nf648MixedOppTable :',1)[1].split('\n\ntheorem',1)[0])))==[v for r in rows[KEYS['MixedOpp']] for v in r]
# Original widened entries only, linked to all original shard hashes.
p=A/'nf631-widened.zip'; assert sha(p.read_bytes())=='e91a83cae117e98608aefa6849dac178e4ddb58dd1dffbfe37304ad248af9ed9'
ix=list(range(14))+[241]; entries={}
with zipfile.ZipFile(p) as z:
    w=json.loads(z.read('nf631-widening.json')); assert w['input_sha256']==input_hashes
    raw=z.read('nf631-widened-entries.jsonl.gz'); assert sha(raw)==w['widened_entry_sha256']
    import io
    with gzip.GzipFile(fileobj=io.BytesIO(raw)) as f:
        hdr=json.loads(next(f)); assert hdr['scale']=='10^2600' and hdr['original_entry_sha256']==w['original_entry_sha256']
        for i,line in enumerate(f):
            d=json.loads(line); assert d['row']==i and len(d['H_lower'])==i+1
            if i in ix:
                for j in ix:
                    if j<=i: entries[i,j]=tuple(map(int,d['H_lower'][j])); assert entries[i,j][1]>=0
assert len(entries)==120
BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalLocalGramBlock'; mod='WeilDefect.Generated.NF655'; mom='WeilDefect.Generated.NF648'
def write(name,imports,body):
    data=''.join('import '+i+'\n' for i in imports)+'\nnamespace WeilDefect\n\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'+body+'\n\nend WeilDefect\n'
    (H/(name+'.lean')).write_text(data)
def bank(label,gs):
    v='nf655'+label; n=len(gs)
    b=f'def {v}Bank : Array NF624KeyTable := #['+', '.join('nf648'+g+'Table' for g in gs)+']\n\n'
    b+=f'def {v}Index (k : NF616Frequency) : ℕ :=\n'
    for i,g in enumerate(gs):
        h,f=KEYS[g]; b+=f'  '+('' if i==0 else 'else ')+f'if k.h = ({h.numerator}/{h.denominator}:ℚ) ∧ k.f = ({f.numerator}/{f.denominator}:ℚ) then {i}\n'
    b+=f'  else {n}\n\n'
    b+=f'''theorem {v}Sound : ∀ i < {v}Bank.size, ∀ n < (neutralNF624BankRead {v}Bank i).rows.size,
    ‖neutralNF620J (neutralNF624BankRead {v}Bank i).key.value n - (neutralNF617MomentRead (neutralNF624BankRead {v}Bank i).rows n).value‖ ≤
      (neutralNF617MomentRead (neutralNF624BankRead {v}Bank i).rows n).rad := by
  intro i hi n hn
  have hs : {v}Bank.size = {n} := by rfl
  rw [hs] at hi
  have hh : '''+' ∨ '.join(f'i={i}' for i in range(n))+' := by omega\n  rcases hh with '+' | '.join('rfl' for _ in gs)+'\n'+''.join(f'  · exact nf648{g}Moment n hn\n' for g in gs)
    write(label+'Bank',[BASE]+[mom+'.'+g for g in gs],b)
bank('Base',['Pole','Osc']); bank('Full',list(KEYS))
# Two independent groups: Base has no dependence on the opposite-sign table.
report={}; allnames=[]
for label,which in [('Base',[(i,j) for i,j in entries if i<14 or i==j==241]),('Cross',[(i,j) for i,j in entries if i==241 and j<14])]:
    bname='Base' if label=='Base' else 'Full'; v='nf655'+bname; names=[]
    for i in sorted(set(i for i,j in which)):
        body=''
        for k,j in which:
            if k!=i:continue
            m,r=entries[i,j]; t=f'nf655H{i:03d}_{j:03d}'
            body+=f'def {t}Ball : NF591Ball := ⟨{scaled(m)},{scaled(r)}⟩\n'
            body+=f'theorem {t}Route : neutralNF649HCheck {v}Bank {v}Index {i} {j}=true := by\n  decide +kernel\n'
            body+=f'theorem {t}Widen : neutralNF649WidenH {v}Bank {v}Index {i} {j} {t}Ball=true := by\n  decide +kernel\n'
            body+=f'theorem {t}Contains : {t}Ball.Contains (neutralNF606PhysicalH {i} {j}) :=\n  neutralNF649H_of_local {v}Bank {v}Index {v}Sound {i} {j} _ {t}Route {t}Widen\n#print axioms {t}Contains\n\n'
        name=f'{label}Row{i:03d}'; write(name,[mod+'.'+bname+'Bank'],body); names.append(name)
    write(label,[mod+'.'+n for n in names],f'-- {len(which)} actual physical entry containment targets')
    report[label]=len(which); allnames+=names
assert report=={'Base':106,'Cross':14}
write('Complete',[mod+'.Base',mod+'.Cross'],'-- All 120 actual physical entry containment targets.')
# Independent byte-level verification of every emitted ball against NF631.
seen={}
for n in allnames:
    for i,j,m,r in re.findall(r'def nf655H(\d{3})_(\d{3})Ball : NF591Ball := ⟨'+coord+','+coord+'⟩',(H/(n+'.lean')).read_text()):
        key=int(i),int(j); assert key not in seen; seen[key]=int(m),int(r)
assert seen==entries
report={'schema':'NF655-certified-moment-gram-preflight-v1','accepted_archives':ARCH,'accepted_modules':len(files),'accepted_rows':42,'new_moment_rows':14,'new_endpoint_prefixes':0,'base_entries':106,'cross_entries':14,'entry_literal_matches':len(seen),'new_modules':1+len(list(H.glob('*.lean'))),'input_sha256':input_hashes,'files':{str(p.relative_to(O)):sha(p.read_bytes()) for p in sorted(O.rglob('*.lean'))},'scope':'retained bytes and emitted proof targets, not new kernel acceptance'}
(O/'nf655-report.json').write_text(json.dumps(report,indent=2)+'\n'); print({k:v for k,v in report.items() if k not in ('files','input_sha256','accepted_archives')})
