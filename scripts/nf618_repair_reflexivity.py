import hashlib,json,re,sys
from fractions import Fraction as F
from pathlib import Path
sha=lambda b:hashlib.sha256(b).hexdigest()
pat=re.compile(r'(^theorem \w+(?:Neg)?PhaseIdentity : nf618HybridPhase \(([^\n:]+):ℚ\) = nf618HybridPhase \(([^\n:]+):ℚ\) := by\n)  unfold nf618HybridPhase\n  rw \[neutralNF592Phase_identity, neutralNF592Phase_identity\]\n  rw \[show neutralNF592Reduced [^\n]+\]$',re.M)

def patch(s):
    s,n=pat.subn(lambda m:m[1]+'  rfl' if F(m[2])==F(m[3]) else m[0],s)
    old='    convert en using 1 <;> push_cast\n';new='    convert en using 1 <;> push_cast <;> rfl\n'
    return s.replace(old,new)

def main():
    root=Path(sys.argv[1]);p=root/'manifest.json';m=json.loads(p.read_text());files=m['files'];changed={};finger=lambda:sha('\n'.join(f'{n}:{h}' for n,h in sorted(files.items())).encode())
    original=finger();assert m.get('source_fingerprint',original)==original
    for n,h in files.items():assert sha((root/n).read_bytes())==h,n
    for r in m['tables']:
        n=r['module']+'.lean';q=root/n;s=q.read_text();t=patch(s)
        if s!=t:
            q.write_text(t);changed[n]={'old':files[n],'new':sha(q.read_bytes())};files[n]=changed[n]['new']
    fp=finger();m['source_fingerprint']=fp;m['reflexivity_repair']={'original_source_fingerprint':original,'changed':changed};p.write_text(json.dumps(m,indent=2)+'\n');print('reflexivity repair',len(changed),original,fp)
    if len(sys.argv)>2:assert len(changed)==int(sys.argv[2]) and fp==sys.argv[3]
if __name__=='__main__':main()
