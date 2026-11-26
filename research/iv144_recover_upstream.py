"""Recover selected pinned Canonical Return upstream archives, without execution.
Usage: python research/iv144_recover_upstream.py CHECKOUT OUTPUT [--large]
Verify every Git blob, full ZIP digest and CRC before publishing the ZIP.
No assumption that the selected archives contain every transitive dependency.
"""
import argparse, hashlib, json, pathlib, subprocess, tempfile, zipfile
MANIFEST=pathlib.Path(__file__).with_name("iv144_upstream_manifest.json")
def require(p,s):
    if not p: raise ValueError(s)
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("checkout",type=pathlib.Path)
    p.add_argument("output",type=pathlib.Path)
    p.add_argument("--large",action="store_true")
    a=p.parse_args()
    m=json.loads(MANIFEST.read_text())
    a.output.mkdir(parents=True,exist_ok=True)
    receipts=[]
    for name,r in m["archives"].items():
        if r["bytes"]>10000000 and not a.large: continue
        target=a.output/name
        require(not target.exists(),"existing output "+name)
        with tempfile.NamedTemporaryFile(dir=a.output,delete=False) as f:
            tmp=pathlib.Path(f.name)
            try:
                h=hashlib.sha256(); total=0
                for item in r["parts"]:
                    b=subprocess.check_output(["git","-C",str(a.checkout),"show",
                        m["source_commit"]+":"+item["path"]])
                    require(len(b)==item["bytes"],"part length")
                    require(hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()==item["git_blob"],"blob hash")
                    f.write(b); h.update(b); total+=len(b)
                f.flush()
                require(total==r["bytes"] and h.hexdigest()==r["sha256"],"archive hash "+name)
                with zipfile.ZipFile(tmp) as z:
                    require(z.testzip() is None,"CRC "+name)
                    names=z.namelist()
                    require(len(names)==len(set(names)),"duplicate names")
                    members=[{"name":i.filename,"bytes":i.file_size,"crc":i.CRC} for i in z.infolist()]
                tmp.rename(target)
                receipts.append({"archive":name,"bytes":total,"sha256":h.hexdigest(),"members":members})
                print("CUSTODY PASS",name,total,h.hexdigest(),flush=True)
            finally:
                if tmp.exists(): tmp.unlink()
    (a.output/"receipt.json").write_text(json.dumps(receipts,indent=2)+"\n")
if __name__=="__main__": main()
