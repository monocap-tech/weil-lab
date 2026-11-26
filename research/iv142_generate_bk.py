"""Generate a Lean data module from the exact, pinned IV140 export.
Verifies every exported file, the original ZIP, original NPY payloads,
and the exact C-order integer arrays against independent NPZ decoding.
No object arrays, pickle, eigensolver, or floating-point conversion.
"""
import base64, hashlib, io, json, math, pathlib, sys, zipfile
import numpy as np

ROOT=pathlib.Path("custody/iv140-bk")
OUT=pathlib.Path("iv142/out")
LEAN=pathlib.Path("WeilDefect/Arithmetic/ActualZetaIV142BKData.lean")
ARCHIVE="805fa6a91f0bdb9dbfffde06a9c8a774df744c0ef7b1df74690447e0454669ac"
MOD=1000000007
def require(x,msg):
    if not x: raise ValueError(msg)
def sha(b): return hashlib.sha256(b).hexdigest()
def raw(rec):
    data=b"".join(base64.b64decode((ROOT/p["file"]).read_bytes().strip(),validate=True)
        for p in rec["parts"])
    require(len(data)==rec["size"] and sha(data)==rec["sha256"],"payload identity")
    return data
def rolling(v):
    h=0
    for x in v: h=(h*257+x)%MOD
    return h
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    idx=json.loads((ROOT/"index.json").read_text())
    require(idx["source_commit"]=="ea81fd040e51bf0ffbe8fdab3b5c6282cf293a0f","source commit")
    require(idx["archive_sha256"]==ARCHIVE,"archive pin")
    archive=raw(idx["archive"])
    require(len(archive)==2992441 and sha(archive)==ARCHIVE,"ZIP pin")
    bank={}
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        require(z.testzip() is None,"ZIP CRC")
        for item in idx["members"]:
            b=z.read(item["name"])
            require(len(b)==item["size"] and sha(b)==item["sha256"],"member identity")
        for p,m,n,parity in (("even",5081,121,0),("odd",5143,119,1)):
            for filename,field,label,shape in (
                ("exceptional","E",p+"E",(m,n)),
                ("physical_dictionary","indices",p+"Mode",(m,)),
                ("physical_dictionary","weights",p+"Weight",(m,)),
                ("exceptional","scale",p+"Scale",()),
                ("exceptional","parity",p+"Parity",()),
                ("physical_dictionary","weight_scale",p+"WeightScale",()),
                ("physical_dictionary","parity",p+"DictParity",())):
                name=f"{p}/{filename}.npz"
                recs=[r for r in idx["arrays"] if r["archive_member"]==name and r["npz_member"]==field+".npy"]
                require(len(recs)==1,"unique field "+label)
                r=recs[0]
                with zipfile.ZipFile(io.BytesIO(z.read(name))) as nz:
                    original=nz.read(field+".npy")
                require(raw(r["npy"])==original,"NPY identity "+label)
                a=np.load(io.BytesIO(original),allow_pickle=False)
                require(a.shape==shape and list(a.shape)==r["shape"] and a.dtype.str==r["dtype"]
                        and a.dtype.kind in "iu","shape/dtype "+label)
                v=[]
                for c in r["integer_c_order"]:
                    b=(ROOT/c["file"]).read_bytes()
                    require(sha(b)==c["sha256"] and len(v)==c["offset"],"chunk identity")
                    vals=json.loads(b)
                    require(len(vals)==c["count"] and all(type(x) is int for x in vals),"chunk integers")
                    v.extend(vals)
                require(v==[int(x) for x in a.ravel(order="C")],"integer replay "+label)
                bank[label]=v
            require(bank[p+"Scale"]==[2**23] and bank[p+"WeightScale"]==[10**8],"scale")
            require(bank[p+"Parity"]==bank[p+"DictParity"]==[parity],"parity")
            modes=bank[p+"Mode"]
            require(len(set(modes))==m and all(j>=0 and j%2==parity for j in modes),"mode IDs")
            require((modes[-1]==0 and modes.count(0)==1) if p=="even" else 0 not in modes,"constant")
            require(all(w>0 for w in bank[p+"Weight"]),"deficit weights")
        for member in ("even/bk_basis.py","odd/bk_basis.py","physical_gram.py","bk_check.py",
                       "even/basis.log","odd/basis.log","even/physical.log","odd/physical.log"):
            (OUT/("BK-"+member.replace("/","-"))).write_bytes(z.read(member))
    lines=["import Mathlib","namespace WeilDefect.BKData",
           "def decode (s : String) : Array Int := (s.split ',').toList.toArray.map (fun x => x.toString.toInt!)",
           "def decodeAll (ss : Array String) : Array Int := ss.foldl (fun a s => a ++ decode s) #[]",
           "def checksum (a : Array Int) : Int := a.foldl (fun h x => (h*257+x)%1000000007) 0"]
    expected=[]
    for name in ("evenE","oddE","evenMode","oddMode","evenWeight","oddWeight"):
        v=bank[name]
        chunks=[",".join(map(str,v[i:i+2048])) for i in range(0,len(v),2048)]
        # Decimal-only string literals; source readback is deterministic.
        lines.append("def "+name+" : Array Int := decodeAll #["+ ",\n".join(json.dumps(c) for c in chunks)+"]")
        lines.append('#eval IO.println ("BKDATA '+name+' " ++ toString '+name+'.size ++ " " ++ toString (checksum '+name+'))')
        expected.append(f"BKDATA {name} {len(v)} {rolling(v)}")
    lines.append("end WeilDefect.BKData")
    LEAN.write_text("\n".join(lines)+"\n")
    (OUT/"data-expected.txt").write_text("\n".join(expected)+"\n")
    (OUT/"data-source.sha256").write_text(sha(LEAN.read_bytes())+"  "+str(LEAN)+"\n")
    (OUT/"data-summary.json").write_text(json.dumps({k:{"count":len(v),"min":min(v),"max":max(v),"checksum":rolling(v)} for k,v in bank.items()},indent=2)+"\n")
    print("BK EXACT INTEGER REPLAY PASS",len(bank["evenE"])+len(bank["oddE"]))
if __name__=="__main__": main()
