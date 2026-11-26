#!/usr/bin/env python3
"""Build generated importable modules serially and preserve proof objects.
No log or external numerical assertion is used as a theorem."""
import argparse,hashlib,json,re,subprocess,time
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--kind',choices=['sym','row'],required=True)
p.add_argument('--stop',type=int,required=True)
p.add_argument('--out',type=Path,required=True)
a=p.parse_args()
a.out.mkdir(parents=True,exist_ok=True)
assert a.stop%8==0 and 0<a.stop<=(128 if a.kind=='sym' else 1024)
root=Path('WeilDefect/Arithmetic/IV160Bank')
kind=a.kind.capitalize()
ns='WeilDefect.Arithmetic.IV160Bank.'
full=128 if a.kind=='sym' else 1024
bank=kind+'Bank' if a.stop==full else f'{kind}Prefix{a.stop:04}'
names=[f'{kind}{b:04}' for b in range(0,a.stop,2)]
groups=[f'{kind}Group{b:04}' for b in range(0,a.stop,8)]
manifest=[]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
for stem in names+groups+[bank]:
    src=root/(stem+'.lean')
    expected=re.findall(r'^#print axioms (\w+)$',src.read_text(),re.M)
    start=time.monotonic()
    r=subprocess.run(['/usr/bin/time','-v','timeout','300','lake','build',ns+stem],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    log=a.out/(stem+'.log')
    log.write_text(r.stdout)
    olean=Path('.lake/build/lib/lean')/root/(stem+'.olean')
    ok=r.returncode==0 and olean.is_file()
    for n in expected:
        no=re.findall(r"'WeilDefect\."+re.escape(n)+r"' does not depend on any axioms",r.stdout)
        deps=re.findall(r"'WeilDefect\."+re.escape(n)+r"' depends on axioms: \[([^\]]*)\]",r.stdout)
        ok=ok and len(no)+len(deps)==1 and (not deps or set(deps[0].replace(' ','').split(','))<={'propext','Classical.choice','Quot.sound'})
        if stem in names: ok=ok and len(no)==1
    manifest.append({'module':ns+stem,'source_sha256':sha(src),'olean_sha256':sha(olean) if olean.is_file() else None,'log_sha256':sha(log),'seconds':time.monotonic()-start,'expected':expected,'pass':ok})
    (a.out/'manifest.json').write_text(json.dumps(manifest,indent=2))
    print(stem,'PASS' if ok else 'FAIL',flush=True)
    if not ok: raise SystemExit(1)
    # Preserve each checked source and actual import object, not just logs.
    (a.out/(stem+'.lean')).write_bytes(src.read_bytes())
    (a.out/(stem+'.olean')).write_bytes(olean.read_bytes())
