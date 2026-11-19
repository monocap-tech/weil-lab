#!/usr/bin/env python3
"""Attach accepted original moment declarations to exact local payload slots.

Full-bank projections are separate, generated as concrete proof candidates.
Every source is authenticated by archive digests in the workflow and exact
manifest hashes here; the kernel must still prove the actual row equality.
"""
import argparse,hashlib,json,re,sys
from pathlib import Path
from fractions import Fraction as F
from emit_nf627_original_moment_bank import filetext,keylit
sys.set_int_max_str_digits(0)
MOD="WeilDefect.Generated.NF705"
CORE="WeilDefect.Arithmetic.ActualZetaOriginalPhysicalShapedBank"
OPT="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def main():
    p=argparse.ArgumentParser()
    for k in ("generated","audits","output"):p.add_argument("--"+k,type=Path,required=True)
    a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
    bank=a.generated/"NF690";bm=load(bank/"manifest.json")
    assert (bm["keys"],bm["rows"],bm["chunks"])==(7835,37994,490)
    slots={tuple(map(F,x["key"])):x for x in bm["slots"]}
    assert len(slots)==7835
    prior_manifest=load(a.generated/"NF692"/"manifest.json")
    assert prior_manifest["bank_manifest_sha256"]==sha(bank/"manifest.json")
    assert (prior_manifest["tables"],prior_manifest["rows"])==(271,2124)
    prior_slots={r["index"] for r in prior_manifest["records"]}
    assert len(prior_slots)==271
    pm696=load(a.generated/"NF696"/"manifest.json")
    assert pm696["bank_manifest_sha256"]==sha(bank/"manifest.json")
    assert pm696["nf692_manifest_sha256"]==sha(a.generated/"NF692"/"manifest.json")
    assert (pm696["tables"],pm696["rows"])==(127,548)
    assert prior_slots.isdisjoint(r["index"] for r in pm696["records"])
    prior_slots.update(r["index"] for r in pm696["records"])
    assert len(prior_slots)==398
    pm701=load(a.generated/"NF701"/"manifest.json")
    assert pm701["bank_manifest_sha256"]==sha(bank/"manifest.json")
    assert (pm701["tables"],pm701["rows"])==(548,2608)
    for n in (692,696): assert pm701[f"nf{n}_manifest_sha256"]==sha(a.generated/f"NF{n}"/"manifest.json")
    assert prior_slots.isdisjoint(r["index"] for r in pm701["records"])
    prior_slots.update(r["index"] for r in pm701["records"])
    assert len(prior_slots)==946
    hashes={x["file"]:x["sha256"] for x in bm["files"]}
    assert [x["index"] for x in bm["slots"]]==list(range(7835))
    for name in ("NF632","NF698","NF687"):
        d=a.generated/name
        for f in load(d/"manifest.json")["files"]:
            assert sha(d/f["file"])==f["sha256"],(name,f["file"])
    files=[];records=[];seen=set();chunks={}
    def write(name,imports,body):
        path=a.output/(name+".lean")
        path.write_text(filetext(imports,OPT+body),encoding="utf8")
        files.append({"file":path.name,"sha256":sha(path)})
    grouped={}
    for stage,audits in ((698,[str(i) for i in range(6)]),):
        d=a.generated/f"NF{stage}";m=load(d/"manifest.json")
        assert m["input_sha256"]==bm["input_sha256"]
        expected={x.get("module",x.get("group")):x for x in m.get("groups",m.get("tables",[]))}
        for audit in audits:
            paths=list((a.audits/audit).rglob("*.json"))
            paths=[q for q in paths if "audit" in q.name]
            assert len(paths)==1,(audit,paths)
            receipt=load(paths[0]);assert receipt["manifest_sha256"]==sha(d/"manifest.json")
            rows=receipt["tables"]
            assert stage==698 and receipt["pair"]==int(audit)
            assert receipt["full_plan_sha256"]==m["full_plan_sha256"]
            assert len(m["selected_families"])==24 and len(expected)==930
            assert {r["group"] for r in rows}=={r["group"] for r in m["groups"] if r["family"]//2==int(audit)}
            for rec in rows:
                name=rec.get("module",rec.get("group"))
                assert name in expected
                exp=expected[name]
                assert all(rec[k]==v for k,v in exp.items())
                src=d/(name+".lean")
                assert sha(src)==rec.get("source_sha256",rec.get("sha256"))
                prior=f"nf{stage}{name}"
                assert rec["theorem"]==prior+"Moment"
                assert set(rec["axioms"])<={"propext","Classical.choice","Quot.sound"}
                k=tuple(map(F,rec["key"]));assert k not in seen;seen.add(k)
                slot=slots[k];i=slot["index"];chunk=slot["chunk"];offset=slot["offset"]
                assert i not in prior_slots,("overlap with NF692/NF696/NF701",i)
                assert slot["rows"]==rec["rows"]
                if chunk not in chunks:
                    path=bank/(chunk+".lean")
                    assert sha(path)==hashes[path.name]
                    chunks[chunk]=re.findall(r"#\[\n    (.*?)\n  \]",path.read_text(),re.S)
                    assert len(chunks[chunk])==min(16,7835-16*int(chunk[-3:]))
                match=re.search(r"def "+prior+r"Table : NF624KeyTable := ⟨"+re.escape(keylit(k))+r", #\[\n    (.*?)\n  \]⟩",src.read_text(),re.S)
                assert match and match[1]==chunks[chunk][offset],(stage,name,i)
                assert len(match[1].split(",\n    "))==slot["rows"]
                label=f"Slot{i:05d}";z="nf705"+label
                body=f"""def {z}Rows : Array NF617MomentRow :=
  (nf690{chunk}[{offset}]?).getD #[]

theorem {z}Key : (nf687Read {i}).1 = {prior}Table.key := by
  decide +kernel

theorem {z}Length : (nf687Read {i}).2 = {prior}Table.rows.size := by
  decide +kernel

theorem {z}RowsEq : {z}Rows = {prior}Table.rows := by
  rfl

theorem {z}Sound (payload : ℕ → Array NF617MomentRow)
    (hp : payload {i} = {z}Rows) :
    neutralNF690TableSound (neutralNF690Table nf687Read payload {i}) := by
  have ht := neutralNF690Table_eq nf687Read payload {i} {prior}Table
    {z}Key (hp.trans {z}RowsEq) {z}Length
  rw [ht]
  exact {prior}Moment

#print axioms {z}Key
#print axioms {z}Length
#print axioms {z}RowsEq
#print axioms {z}Sound
"""
                write(label,["WeilDefect.Generated.NF687.Compact","WeilDefect.Generated.NF690."+chunk,f"WeilDefect.Generated.NF{stage}."+name],body)
                record=dict(index=i,key=rec["key"],rows=rec["rows"],stage=stage,receipt=name,chunk=chunk,offset=offset,module=label,shard=str(rec["family"]//2))
                records.append(record);grouped.setdefault(record["shard"],[]).append(record)
    assert len(records)==475 and sum(r["rows"] for r in records)==2209
    assert [(len(grouped[str(i)]),sum(r['rows'] for r in grouped[str(i)])) for i in range(6)]==[(80,382),(81,374),(78,370),(77,365),(77,363),(82,355)]
    assert set(grouped)==set(map(str,range(6)))
    # Group the concrete proposals into bounded modules. These import the FULL
    # bank and are deliberately not built in the local-slot workflow.
    for aidx,(shard,rs) in enumerate(grouped.items()):
        for start in range(0,len(rs),8):
            batch=rs[start:start+8];body=""
            for r in batch:
                i=r["index"];z="nf705"+r["module"]
                body+=f"""theorem {z}PayloadEq : nf690Payload {i} = {z}Rows := by
  rfl

theorem {z}Concrete :
    neutralNF690TableSound (neutralNF624BankRead nf690OriginalBank {i}) := by
  rw [show nf690OriginalBank = neutralNF690Bank nf687Read nf687Size nf690Payload from rfl]
  rw [neutralNF690Bank_read nf687Read nf687Size nf690Payload {i} (by decide +kernel)]
  exact {z}Sound nf690Payload {z}PayloadEq

#print axioms {z}PayloadEq
#print axioms {z}Concrete

"""
            write(f"Concrete{aidx}{start//8:02d}",["WeilDefect.Generated.NF690.Bank"]+[MOD+"."+r["module"] for r in batch],body)
    out={"schema":"NF705-accepted-moment-slot-attachments-v1","bank_manifest_sha256":sha(bank/"manifest.json"),
         "tables":len(records),"rows":sum(r["rows"] for r in records),"records":records,"files":files,
         "nf692_manifest_sha256":sha(a.generated/"NF692"/"manifest.json"),
         "nf696_manifest_sha256":sha(a.generated/"NF696"/"manifest.json"),
         "nf701_manifest_sha256":sha(a.generated/"NF701"/"manifest.json"),
         "scope":"Exact local and concrete proof candidates against the incumbent original bank."}
    (a.output/"manifest.json").write_text(json.dumps(out,indent=2)+"\n")
    print("NF705 475 accepted tables / 2209 rows reconciled exactly to original payload slots; local and concrete Lean proposals generated")
if __name__=="__main__":main()
