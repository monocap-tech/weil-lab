#!/usr/bin/env python3
"""NF697: bind a reusable compiled bank to the exact source and toolchain."""
import hashlib
import json
import platform
import subprocess
from pathlib import Path

def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            h.update(block)
    return h.hexdigest()

def main():
    root=Path("WeilDefect/Generated")
    names={Path(p.decode()) for p in subprocess.check_output(["git","ls-files","-z"]).split(b"\0")
           if p and (p.endswith(b".lean") or p in {b"lean-toolchain",b"lakefile.toml",b"lakefile.lean"})}
    names.add(Path("lake-manifest.json"))
    # All restored sources in the accepted bank build, not just their manifest.
    for d in ("NF679","NF682","NF687","NF690","NF691"):
        names.update(p for p in (root/d).rglob("*") if p.is_file())
    files={str(p):sha(p) for p in sorted(names)}
    env={"lean":subprocess.check_output(["lean","--version"],text=True).strip(),
         "lake":subprocess.check_output(["lake","--version"],text=True).strip(),
         "machine":platform.machine(),"os":platform.system(),
         "mathlib":subprocess.check_output(["git","-C",".lake/packages/mathlib","rev-parse","HEAD"],text=True).strip()}
    body={"schema":"NF697-compiled-bank-binding-v1","environment":env,"files":files}
    raw=json.dumps(body,sort_keys=True,separators=(",",":")).encode()
    body["fingerprint"]=hashlib.sha256(raw).hexdigest()
    Path("nf697-bank-binding.json").write_text(json.dumps(body,indent=2,sort_keys=True)+"\n")
    print("NF697 exact source/environment fingerprint",body["fingerprint"],"files",len(files))

if __name__=="__main__":
    main()
