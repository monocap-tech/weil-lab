import hashlib,json,re
from fractions import Fraction
from pathlib import Path

def sha(b):return hashlib.sha256(b).hexdigest()
def patch_file(s,f):
    if not re.search(r'^def .*Cache : NF617MomentCache := nf618HybridCache .* false$',s,re.M):return s
    f=Fraction(f);signed=-f
    pat=r'^  · change (\w+Value)\.Contains \(nf618HybridPhase \(([^\n]+):ℚ\)\)$'
    m=re.search(pat,s,re.M);assert m and Fraction(m[2])==signed
    return s[:m.start()]+f'  · rw [show (if (false : Bool) = true then ({f}:ℚ) else -({f}:ℚ)) = ({signed}:ℚ) by norm_num]'+s[m.end():]

def main():
    import sys
    root=Path(sys.argv[1]); p=root/'manifest.json';m=json.loads(p.read_text()); files=m['files']; changed={}
    original=sha('\n'.join(f'{n}:{h}' for n,h in sorted(files.items())).encode())
    assert original==m.get('source_fingerprint',original)
    for n,h in files.items():assert sha((root/n).read_bytes())==h,n
    for r in m['tables']:
        n=r['module']+'.lean';q=root/n;s=q.read_text();t=patch_file(s,r['key'][1]);
        if s!=t:
            q.write_text(t);changed[n]={'old':files[n],'new':sha(q.read_bytes())};files[n]=changed[n]['new']
    fingerprint=sha('\n'.join(f'{n}:{h}' for n,h in sorted(files.items())).encode())
    m['source_fingerprint']=fingerprint;m['repair']={'original_source_fingerprint':original,'changed':changed};p.write_text(json.dumps(m,indent=2)+'\n')
    print('bool branch repair',len(changed),original,fingerprint)
    if len(sys.argv)>2: assert len(changed)==int(sys.argv[2]) and fingerprint==sys.argv[3]
if __name__=='__main__':main()
