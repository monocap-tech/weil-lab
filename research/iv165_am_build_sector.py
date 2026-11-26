#!/usr/bin/env python3
"""Serially compile one generated sector; preserve source and all object
companions. Recheck the named proof declarations in the build output."""
import argparse,hashlib,json,re,subprocess,time
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--sector',type=int,choices=range(8),required=True)
p.add_argument('--out',type=Path,required=True)
a=p.parse_args()
root=Path('WeilDefect/Arithmetic/IV160Bank')
a.out.mkdir(parents=True,exist_ok=True)
plan=json.loads((root/f'RowSector{a.sector:02}.json').read_text())
lo,hi=plan['block_interval']
assert (lo,hi)==((32,128) if a.sector==0 else (128*a.sector,128*(a.sector+1)))
expected=[f'Row{b:04}' for b in range(lo,hi,2)]+[f'RowGroup{b:04}' for b in range(lo,hi,8)]+[f'RowSector{a.sector:02}']
assert plan['modules']==expected
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
records=[]
for stem in expected:
    src=root/(stem+'.lean')
    source=src.read_text()
    assert not re.search(r'\b(?:sorry|admit|sorryAx|native_decide|axiom)\b',source)
    names=re.findall(r'^#print axioms (\w+)$',source,re.M)
    assert len(names)==(2 if re.fullmatch(r'Row\d{4}',stem) else 1)
    start=time.monotonic()
    r=subprocess.run(['/usr/bin/time','-v','timeout','300','lake','build','WeilDefect.Arithmetic.IV160Bank.'+stem],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    log=a.out/(stem+'.log'); log.write_text(r.stdout)
    build=Path('.lake/build/lib/lean')/root
    objs=sorted(build.glob(stem+'.olean*'))
    ok=r.returncode==0 and (build/(stem+'.olean')).is_file()
    for n in names:
        empty=r.stdout.count(f"'WeilDefect.{n}' does not depend on any axioms")
        deps=re.findall(r"'WeilDefect\."+re.escape(n)+r"' depends on axioms: \[([^\]]*)\]",r.stdout)
        ok=ok and empty+len(deps)==1 and (not deps or set(deps[0].replace(' ','').split(','))<={'propext','Classical.choice','Quot.sound'})
        if len(names)==2: ok=ok and empty==1
    record={'module':stem,'names':names,'source_sha256':digest(src),'log_sha256':digest(log),'objects':{q.name:digest(q) for q in objs},'seconds':time.monotonic()-start,'pass':bool(ok)}
    records.append(record)
    (a.out/'manifest.json').write_text(json.dumps({'plan':plan,'records':records},indent=2))
    print(stem,'PASS' if ok else 'FAIL',flush=True)
    if not ok: raise SystemExit(1)
    (a.out/src.name).write_bytes(src.read_bytes())
    for q in objs: (a.out/q.name).write_bytes(q.read_bytes())
