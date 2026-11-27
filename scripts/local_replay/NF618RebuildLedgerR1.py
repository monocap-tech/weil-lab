#!/usr/bin/env python3
"""Regenerate Batch24 R1 from pinned parent and admitted batch records.
This checks ledger semantics, not raw producer archive custody.
"""
import hashlib, json
from collections import Counter
from pathlib import Path
from NF618RebuildLedger import advance
P = Path(__file__).resolve().parents[2] / "notes/provisional"
def need(ok, msg):
    if not ok: raise ValueError(msg)
def read(n, digest):
    b=(P/n).read_bytes()
    need(hashlib.sha256(b).hexdigest()==digest, "digest: "+n)
    return b
def census(l):
    s=l["slots"]
    need(len(s)==7835 and all(t["index"]==i and type(t["rows"]) is int and t["rows"]>0 for i,t in enumerate(s)), "slot universe")
    c=[t for t in s if t["certified_group"] is not None]
    r=[t for t in s if t["certified_group"] is None]
    v=[len(c),sum(t["rows"] for t in c),len(r),sum(t["rows"] for t in r)]
    need(v==[l[k] for k in ("certified_tables","certified_rows","residual_tables","residual_rows")], "slot census")
    counts=Counter(t["certified_group"] for t in c)
    rows=Counter()
    for t in c: rows[t["certified_group"]]+=t["rows"]
    need(len(l["groups"])==len(counts) and len({g["group"] for g in l["groups"]})==len(counts), "group universe")
    need(all((counts[g["group"]],rows[g["group"]])==(g["tables"],g["rows"]) for g in l["groups"]), "group census")
    return v
def main():
    need(__debug__, "do not run with -O: imported verifier uses assertions")
    parent=read("NF618CertifiedSlotLedgerBatch20.json","6a396e811890b8d1df7d9fc23855a34cf0ec465a3092b795b2647ca9b949adfd")
    report=json.loads(read("NF618Batch21-24Admission.json","c962aa9e3f895cce259e3320a95ec80e8a4660d3df803d487fcae339eaa23c1e"))
    l=json.loads(parent); census(l)
    need([a["batch"] for a in report]==[21,22,23,24], "batch order")
    idxraw=(P/"NF618DeploymentIndex.json").read_bytes()
    def blob(raw): return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
    need(blob(idxraw)=="7104217aa045d5e9f7008745fb83c5c5452f23af","deployment index")
    idx=json.loads(idxraw)
    for a in report:
        b=a["batch"]; raw=(P/f"NF618Batch{b:02}Plan.json").read_bytes()
        need(blob(raw)==idx["batches"][b][1], "plan identity")
        p=json.loads(raw)
        ids=sorted(i for g in p["groups"] for i,_ in g["slots"])
        need(ids==a["slots"]==[s["index"] for s in l["slots"] if s["scheduled_batch"]==b], "slot schedule")
        need(p["reflexive_fingerprint"]==a["source_fingerprint"] and p["modules"]==a["source_modules"] and p["rows"]==a["rows"] and p["audit_targets"]==a["audit_targets"] and a["source_audit_gate"]=="PASS", "plan binding")
    out=advance(parent,report); n=json.loads(out)
    need(census(n)==[6097,29336,1738,8658],"terminal census")
    changed=[i for i,(a,b) in enumerate(zip(l["slots"],n["slots"])) if a!=b]
    need(len(changed)==448 and set(changed)=={i for a in report for i in a["slots"]}, "exact changed slots")
    need(all({k:v for k,v in l["slots"][i].items() if k!="certified_group"}=={k:v for k,v in n["slots"][i].items() if k!="certified_group"} for i in changed), "immutable slot fields")
    need(hashlib.sha256(out).hexdigest()=="7910b438110d0ecb1a2ab8caf14646d0ac62440c4893dc80bbcce077bf51ddcf", "R1 digest")
    path=P/"NF618CertifiedSlotLedgerBatch24R1.json"
    if path.exists(): need(path.read_bytes()==out, "stored R1 bytes")
    else: path.write_bytes(out)
    print(json.dumps({"functional_regeneration":"PASS","sha256":hashlib.sha256(out).hexdigest(),"new_slots":448,"certified_tables":6097,"certified_rows":29336,"residual_tables":1738,"residual_rows":8658,"scope":"ledger replay only; evidence custody hold remains"},indent=2))
if __name__=="__main__":
    main()
