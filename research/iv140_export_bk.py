"""Lossless, text-readable custody export of the pinned BK archive.

Does not evaluate the BK coercivity inequality or interpret array fields.
No pickle loading, no ZIP extraction. Every payload is hashed and checked
after reconstruction; original ZIP and NPY member bytes are preserved.
"""
import base64
import hashlib
import io
import json
import pathlib
import sys
import zipfile
import numpy as np
from iv139_reconstruct_bk import reconstruct, COMMIT, SHA256, SIZE, require

CHUNK = 180000

def digest(b):
    return hashlib.sha256(b).hexdigest()

def emit(out, stem, payload):
    parts = []
    for i, pos in enumerate(range(0, len(payload), CHUNK)):
        b = payload[pos:pos+CHUNK]
        name = f"{stem}-{i:04d}.b64"
        p = out / name
        p.write_bytes(base64.b64encode(b)+b"\n")
        parts.append({"file":name,"size":len(b),"sha256":digest(b)})
    recovered = b"".join(base64.b64decode((out / p["file"]).read_bytes().strip(),
                        validate=True) for p in parts)
    require(recovered == payload, "text roundtrip "+stem)
    return {"size":len(payload),"sha256":digest(payload),"parts":parts}

def run(repo, out):
    archive, entries = reconstruct(repo)
    out.mkdir(parents=True, exist_ok=False)
    index = {"source_commit":COMMIT,"archive_sha256":SHA256,"archive_size":SIZE,
             "archive":emit(out,"archive",archive),"members":[],"arrays":[]}
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        for i, name in enumerate(entries):
            info = z.getinfo(name)
            if info.is_dir(): continue
            data = z.read(name)
            index["members"].append({"name":name,"size":len(data),"sha256":digest(data)})
            if not name.endswith(".npz"): continue
            with zipfile.ZipFile(io.BytesIO(data)) as nz:
                require(nz.testzip() is None,"NPZ CRC "+name)
                members = nz.namelist()
                require(len(members)==len(set(members)),"duplicate NPZ names "+name)
                for j, member in enumerate(members):
                    if not member.endswith(".npy"): continue
                    raw = nz.read(member)
                    a = np.load(io.BytesIO(raw),allow_pickle=False)
                    rec = {"archive_member":name,"npz_member":member,"shape":list(a.shape),
                           "dtype":a.dtype.str,"npy":emit(out,f"array-{i:04d}-{j:04d}",raw)}
                    # Exact decimal integer entries for human/connector inspection.
                    # Other dtypes retain the original NPY bytes, without conversion.
                    if a.dtype.kind in "iu":
                        flat = a.ravel(order="C")
                        parts = []
                        for k, pos in enumerate(range(0,flat.size,12000)):
                            values = [int(x) for x in flat[pos:pos+12000]]
                            p = out / f"integer-{i:04d}-{j:04d}-{k:04d}.json"
                            p.write_text(json.dumps(values,separators=(",",":"))+"\n",encoding="utf-8")
                            require(json.loads(p.read_text())==values,"integer roundtrip")
                            parts.append({"file":p.name,"offset":pos,"count":len(values),
                                          "sha256":digest(p.read_bytes())})
                        rec["integer_c_order"] = parts
                    index["arrays"].append(rec)
                    print("ARRAY",name,member,a.dtype.str,list(a.shape),flush=True)
    require(index["arrays"],"no NPZ arrays found")
    (out/"index.json").write_text(json.dumps(index,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    files=sorted(p for p in out.iterdir() if p.is_file())
    (out/"SHA256SUMS").write_text("".join(digest(p.read_bytes())+"  "+p.name+"\n" for p in files))
    print("BK BYTE AND TEXT ROUNDTRIP PASS",len(index["members"]),"members",len(index["arrays"]),"arrays",len(files),"files")

if __name__=="__main__":
    run(pathlib.Path(sys.argv[1]),pathlib.Path(sys.argv[2]))
