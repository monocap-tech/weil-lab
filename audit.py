import json,re,sys,hashlib
from pathlib import Path
p=Path(sys.argv[1]);raw=(p/'manifest.json').read_bytes();m=json.loads(raw);targets=set(m['theorems'])
assert len(m['tables'])==114 and sum(t['rows'] for t in m['tables'])==594
assert len(targets)==len(m['theorems'])==1270
assert len(m['files'])==164
assert all(hashlib.sha256((p/n).read_bytes()).hexdigest()==h for n,h in m['files'].items())
s=(p/'batch27-axioms.log').read_text();found={}
for n,ax in re.findall(r"'WeilDefect\.(\w+)' depends on axioms: \[([^\]]*)\]",s):
    if n in targets:
        assert n not in found
        found[n]=[x.strip() for x in ax.split(',') if x.strip()]
for n in re.findall(r"'WeilDefect\.(\w+)' does not depend on any axioms",s):
    if n in targets:
        assert n not in found
        found[n]=[]
assert set(found)==targets,(len(found),len(targets),sorted(targets-set(found)))
assert all(set(x)<={'propext','Classical.choice','Quot.sound'} for x in found.values())
assert all(t['concrete'] in found for t in m['tables'])
(p/'batch27-audit.json').write_text(json.dumps({'scope':'native evidence only; independent admission pending','manifest_sha256':hashlib.sha256(raw).hexdigest(),'tables':114,'rows':594,'theorems':found},indent=2)+'\n')
print('Strict Batch27 native audit PASS',len(found), '114 tables 594 rows')
