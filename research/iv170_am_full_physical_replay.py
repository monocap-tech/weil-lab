#!/usr/bin/env python3
"""Fresh full-bank source replay, not a proof import from CI archives.
Run only in a pinned Lean/Mathlib checkout with adequate runner budget.
Stops at first error; never treats an evidence manifest as a proof."""
import argparse,subprocess,re,hashlib,json
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--out',type=Path,required=True)
p.add_argument('--generate-only',action='store_true')
a=p.parse_args()
out=a.out.resolve(); out.mkdir(parents=True,exist_ok=True)
def run(*args): subprocess.run(list(args),check=True)
run('python','research/iv160_am_importable_bank.py','--kind','sym','--assemble')
run('python','research/iv160_am_importable_bank.py','--kind','row','--stop','32','--assemble')
for k in range(8): run('python','research/iv165_am_sector_sources.py','--sector',str(k))
run('python','research/iv165_am_sector_sources.py','--assemble')
root=Path('WeilDefect/Arithmetic/IV160Bank')
expected=sorted([*root.glob('Sym*.lean'),*root.glob('Row*.lean')])
assert len(expected)==731, len(expected)
assert len(set(p.name for p in expected))==731
leaves=[p for p in expected if re.fullmatch(r'(Sym|Row)\d{4}',p.stem)]
assert len(leaves)==576
for kind,N in [('Sym',128),('Row',1024)]:
    ids=[]
    for q in leaves:
        if q.stem.startswith(kind):
            ids.extend(int(x) for x in re.findall(r'^theorem neutralIV159'+kind+r'_(\d{4})\b',q.read_text(),re.M))
    assert sorted(ids)==list(range(N))
for q in expected:
    assert not re.search(r'\b(?:sorry|admit|sorryAx|native_decide|axiom)\b',q.read_text()),q
(out/'source-manifest.json').write_text(json.dumps({str(q):hashlib.sha256(q.read_bytes()).hexdigest() for q in expected},indent=2))
if a.generate_only: raise SystemExit(0)
run('lake','build','WeilDefect.Arithmetic.ActualZetaIV159AMRowReceiver','WeilDefect.Arithmetic.ActualZetaIV156AMPhysicalForm')
run('python','research/iv161_am_build_bank.py','--kind','sym','--stop','128','--out',str(out/'sym'))
run('python','research/iv161_am_build_bank.py','--kind','row','--stop','32','--out',str(out/'prefix'))
for k in range(8):
    run('python','research/iv165_am_build_sector.py','--sector',str(k),'--out',str(out/f'sector{k}'))
for module,names in [
    ('IV160Bank.RowBank',['neutralIV160RowBank']),
    ('ActualZetaIV170AMPhysicalTerminal',['neutralIV170FullRows','neutralIV170PhysicalTerminal'])]:
    full='WeilDefect.Arithmetic.'+module
    r=subprocess.run(['lake','build',full],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (out/(module.replace('.','_')+'.log')).write_text(r.stdout)
    assert r.returncode==0,r.stdout
    for n in names:
        empty=r.stdout.count(f"'WeilDefect.{n}' does not depend on any axioms")
        dep=re.findall(r"'WeilDefect\."+re.escape(n)+r"' depends on axioms: \[([^\]]*)\]",r.stdout)
        assert empty+len(dep)==1 and (not dep or set(dep[0].replace(' ','').split(','))<={'propext','Classical.choice','Quot.sound'}),n
    path=Path('.lake/build/lib/lean')/Path(*full.split('.'))
    assert path.with_suffix('.olean').is_file()
    for q in path.parent.glob(path.name+'.olean*'):
        (out/q.name).write_bytes(q.read_bytes())
print('Fresh physical terminal replay PASS')
