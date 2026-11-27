#!/usr/bin/env python3
"""Read-only static preflight. Run in Weil-Lab clone with all pinned commits present.
No checkout, build, dispatch or ref changes. Does not certify Lean proofs."""
import json, pathlib, subprocess, re
m=json.loads(pathlib.Path(__file__).with_name("corrected_source_manifest.json").read_text())
def git(*args): return subprocess.check_output(["git",*args])
def show(ref,path): return git("show",ref+":"+path)
r=m["research"]
assert git("rev-parse",r["ref"]+"^{tree}").decode().strip()==r["tree"]
assert show(r["ref"],"lean-toolchain").decode().strip()==r["toolchain"]
refs=list(dict.fromkeys(f["ref"] for f in m["files"]))
assert len(refs)==13 and len(m["files"])==35
paths=set(git("ls-tree","-r","--name-only",r["ref"]).decode().splitlines())
overlay={}
for f in m["files"]:
    dst="WeilDefect/Arithmetic/"+pathlib.Path(f["path"]).name
    assert dst not in paths and dst not in overlay
    data=show(f["ref"],f["path"])
    assert git("rev-parse",f["ref"]+":"+f["path"]).decode().strip()==f["sha"]
    overlay[dst]=data.decode()
names=[]; modules=[]
for dst,s in overlay.items():
    for imp in re.findall(r"^import (WeilDefect\.[\w.]+)",s,re.M):
        p=imp.replace(".","/")+".lean"
        assert p in overlay or p in paths,(dst,imp)
    if any("ActualZetaIV106"+p in dst for p in m["targetPrefix"]):
        modules.append(dst)
        names+=re.findall(r"^#print axioms (\w+)\s*$",s,re.M)
assert len(modules)==11 and len(names)==len(set(names))==m["expectedAudit"]==45
print(json.dumps({"status":"static preflight PASS; no native audit","sources":35,"refs":13,"modules":modules,"names":names},indent=2))
