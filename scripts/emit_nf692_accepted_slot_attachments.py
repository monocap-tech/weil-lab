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
MOD="WeilDefect.Generated.NF692"
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
    hashes={x["file"]:x["sha256"] for x in bm["files"]}
    assert [x["index"] for x in bm["slots"]]==list(range(7835))
    for name in ("NF632","NF684","NF685","NF686","NF689","NF687"):
        d=a.generated/name
        for f in load(d/"manifest.json")["files"]:
            assert sha(d/f["file"])==f["sha256"],(name,f["file"])
    files=[];records=[];seen=set();chunks={}
    def write(name,imports,body):
        path=a.output/(name+".lean")
        path.write_text(filetext(imports,OPT+body),encoding="utf8")
        files.append({"file":path.name,"sha256":sha(path)})
    grouped={}
    for stage,audits in ((684,["684"]),(685,["685"]),(686,["686"]),(689,["689-0","689-1"])):
        d=a.generated/f"NF{stage}";m=load(d/"manifest.json")
        assert m["input_sha256"]==bm["input_sha256"]
        expected={x.get("module",x.get("group")):x for x in m.get("groups",m.get("tables",[]))}
        for audit in audits:
            paths=list((a.audits/audit).rglob("*.json"))
            paths=[q for q in paths if "audit" in q.name]
            assert len(paths)==1,(audit,paths)
            receipt=load(paths[0]);assert receipt["manifest_sha256"]==sha(d/"manifest.json")
            rows=receipt["tables"]
            if stage==689:assert receipt["family"]==int(audit[-1])
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
                assert slot["rows"]==rec["rows"]
                if chunk not in chunks:
                    path=bank/(chunk+".lean")
                    assert sha(path)==hashes[path.name]
                    chunks[chunk]=re.findall(r"#\[\n    (.*?)\n  \]",path.read_text(),re.S)
                    assert len(chunks[chunk])==min(16,7835-16*int(chunk[-3:]))
                match=re.search(r"def "+prior+r"Table : NF624KeyTable := ⟨"+re.escape(keylit(k))+r", #\[\n    (.*?)\n  \]⟩",src.read_text(),re.S)
                assert match and match[1]==chunks[chunk][offset],(stage,name,i)
                assert len(match[1].split(",\n    "))==slot["rows"]
                label=f"Slot{i:05d}";z="nf692"+label
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
                record=dict(index=i,key=rec["key"],rows=rec["rows"],stage=stage,receipt=name,chunk=chunk,offset=offset,module=label,shard=audit)
                records.append(record);grouped.setdefault(audit,[]).append(record)
    assert len(records)==271 and sum(r["rows"] for r in records)==2124
    assert {k:(len(v),sum(r["rows"] for r in v)) for k,v in grouped.items()}=={"684":(5,79),"685":(87,522),"686":(108,909),"689-0":(35,308),"689-1":(36,306)}
    # Group the concrete proposals into bounded modules. These import the FULL
    # bank and are deliberately not built in the local-slot workflow.
    for aidx,(shard,rs) in enumerate(grouped.items()):
        for start in range(0,len(rs),8):
            batch=rs[start:start+8];body=""
            for r in batch:
                i=r["index"];z="nf692"+r["module"]
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
    out={"schema":"NF692-accepted-moment-slot-attachments-v1","bank_manifest_sha256":sha(bank/"manifest.json"),
         "tables":len(records),"rows":sum(r["rows"] for r in records),"records":records,"files":files,
         "scope":"Local exact key, degree, whole row-array equality and analytic transport. Concrete full-bank projections emitted but not built in this workflow."}
    (a.output/"manifest.json").write_text(json.dumps(out,indent=2)+"\n")
    print("NF692 271 accepted tables / 2124 rows reconciled exactly to original payload slots; local and concrete Lean proposals generated")
if __name__=="__main__":main()
