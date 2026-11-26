#!/usr/bin/env python3
"""Generate bounded independent Lean proof modules and audit every named receipt.
No replacement data; each declaration reduces the original predicate."""
import argparse,json,re,subprocess,time
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--kind',choices=['sym','row'],required=True)
p.add_argument('--start',type=int,default=0)
p.add_argument('--stop',type=int,required=True)
p.add_argument('--out',type=Path,required=True)
a=p.parse_args()
a.out.mkdir(parents=True,exist_ok=True)
assert 0<=a.start<a.stop<=(128 if a.kind=='sym' else 1024)
records=[]
for k in range(a.start,a.stop,2):
    ids=list(range(k,min(k+2,a.stop)))
    names=[f'neutralIV159{a.kind.capitalize()}_{b:04}' for b in ids]
    pred='neutralIV157SymBlock' if a.kind=='sym' else 'neutralIV159RowBlock'
    imp='ActualZetaIV157AMSymmetryPilot' if a.kind=='sym' else 'ActualZetaIV159AMRowReceiver'
    source='import WeilDefect.Arithmetic.'+imp+'\nnamespace WeilDefect\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'
    for b,n in zip(ids,names):
        source+=f'theorem {n} : {pred} {b} = true := by decide\n#print axioms {n}\n'
    source+='end WeilDefect\n'
    stem=f'IV159{a.kind.capitalize()}{k:04}'
    path=a.out/(stem+'.lean')
    path.write_text(source)
    start=time.monotonic()
    r=subprocess.run(['/usr/bin/time','-v','timeout','240','lake','env','lean',str(path)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (a.out/(stem+'.log')).write_text(r.stdout)
    ok=r.returncode==0 and all(r.stdout.count("'WeilDefect."+n+"' does not depend on any axioms")==1 for n in names)
    records.append({'blocks':ids,'names':names,'seconds':time.monotonic()-start,'returncode':r.returncode,'pass':ok})
    (a.out/'manifest.json').write_text(json.dumps(records,indent=2))
    print(stem,'PASS' if ok else 'FAIL',round(records[-1]['seconds'],2),flush=True)
    if not ok: raise SystemExit(1)
