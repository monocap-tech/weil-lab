#!/usr/bin/env python3
"""Source-scoped native preflight. Run with manifest and fresh research checkout.
Git transport is read-only; no workflow dispatch or remote writes."""
import json, pathlib, re, subprocess, sys, hashlib, shutil
p=pathlib.Path
m=json.loads(p(sys.argv[1]).read_text())
root=p(sys.argv[2]).resolve()
out=p(sys.argv[3]).resolve()
out.mkdir(parents=True, exist_ok=True)
def git(*args, raw=False):
    b=subprocess.check_output(['git','-C',str(root),*args])
    return b if raw else b.decode().strip()
def blob(b):
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
assert git('rev-parse','HEAD')==m['research']['ref']
assert git('rev-parse','HEAD^{tree}')==m['research']['tree']
assert (root/'lean-toolchain').read_text().strip()==m['research']['toolchain']
for name,sha in m['research']['base_pins'].items():
    assert blob((root/name).read_bytes())==sha, name
files=m['files']
assert len(files)==m['counts']['files']==72
assert len(set(x['ref'] for x in files))==m['counts']['refs']==36
assert len(set(x['dest'] for x in files))==len(files)
assert sum(x['dest'].startswith('WeilDefect/Generated/F08/') for x in files)==39
assert all(not (root/x['dest']).exists() for x in files)
# Fetch immutable refs only, not mutable branch names. Preserve original blob bytes.
for ref in dict.fromkeys(x['ref'] for x in files):
    subprocess.run(['git','-C',str(root),'fetch','--no-tags','--depth=1','origin',ref],check=True)
    assert git('rev-parse',ref+'^{commit}')==ref
for x in files:
    b=git('show',x['ref']+':'+x['path'],raw=True)
    assert blob(b)==x['sha'], x
    dst=root/x['dest']
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_bytes(b)
    assert blob(dst.read_bytes())==x['sha']
    print(x['sha'],x['dest'])
# Traverse all project imports reachable from the target, plus every overlay file.
# Mathlib and other package imports are handled by the pinned Lake toolchain.
pending=[x['dest'] for x in files]
seen=set()
while pending:
    name=pending.pop()
    if name in seen: continue
    seen.add(name)
    f=root/name
    assert f.is_file(),name
    for imp in re.findall(r'^\s*import\s+(WeilDefect\.[\w.]+)',f.read_text(),re.M):
        dep=imp.replace('.','/')+'.lean'
        assert (root/dep).is_file(), (name,dep)
        pending.append(dep)
target=(root/m['target']).read_text()
names=re.findall(r'^#print axioms (\w+)\s*$',target,re.M)
assert names==m['audit'] and len(set(names))==10
assert not re.search(r'\b(sorry|admit|axiom)\b',target)
mod=m['target'].removesuffix('.lean').replace('/','.')
(out/'audit.lean').write_text('import '+mod+'\n'+'\n'.join('#print axioms WeilDefect.'+n for n in names)+'\n')
(out/'expected_names.json').write_text(json.dumps(names,indent=2)+'\n')
(out/'reachable_project_sources.json').write_text(json.dumps(sorted(seen),indent=2)+'\n')
shutil.copyfile(sys.argv[1],out/'source_manifest.json')
print('PRECHECK PASS: 72 exact overlays; 10 strict targets; project source graph',len(seen))
