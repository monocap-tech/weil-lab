#!/usr/bin/env python3
"""Read-only verification of the original E18 evidence ZIPs; not a proof replay."""
import hashlib,json,pathlib,zipfile
root=pathlib.Path(__file__).resolve().parent
m=json.loads((root/"archive_manifest.json").read_text())
for a in m["archives"]:
    p=root/a["file"]
    b=p.read_bytes()
    assert len(b)==a["bytes"],p
    assert hashlib.sha256(b).hexdigest()==a["sha256"],p
    assert hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()==a["git_blob"],p
    with zipfile.ZipFile(p) as z:
        assert z.testzip() is None,p
        assert len(z.infolist())==a["members"],p
        if "e18x" not in p.name:
            tag=p.name.split("-")[1]
            assert z.read(f"iv106-{tag}/out/axioms.log")== (root.parent/f"{tag}_axioms.log").read_bytes()
        print(p.name, "SHA256, Git blob, ZIP CRC, inventory PASS",a["standing"])
