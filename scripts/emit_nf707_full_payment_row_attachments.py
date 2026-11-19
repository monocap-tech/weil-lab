#!/usr/bin/env python3
"""NF707 attach accepted NF698/NF701 original physical rows to NF702 full payment.
Strict source and receipt reconciliation; only Lean establishes the projection.
"""
import argparse,hashlib,json
from pathlib import Path
from emit_nf627_original_moment_bank import filetext
MOD="WeilDefect.Generated.NF707"
OPT="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
ALLOWED={"propext","Classical.choice","Quot.sound"}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return json.loads(p.read_text())
def one(root,name):
    a=list(root.rglob(name));assert len(a)==1,(name,a)
    return a[0]
def main():
    p=argparse.ArgumentParser()
    for k in ("input","row698","row701","output"):
        p.add_argument("--"+k,type=Path,required=True)
    a=p.parse_args()
    source=one(a.input,"nf702-input-complete-audit.json")
    audit=read(source)
    d=one(a.input,"manifest.json").parent
    m=read(d/"manifest.json")
    assert d.name=="NF702Inputs" and m["rows"]==242
    assert audit["manifest_sha256"]==sha(d/"manifest.json")
    assert all(audit[k]==v for k,v in m.items())
    names={"nf702InputH_symm","nf702OriginalW"}|{n for r in m["projection_rows"] for n in r["theorems"]}
    assert len(names)==50 and set(audit["axioms"])==names
    assert all(set(v)<=ALLOWED for v in audit["axioms"].values())
    assert [r["row"] for r in m["projection_rows"]]==list(range(8))
    for r in m["files"]: assert sha(d/r["file"])==r["sha256"]
    a.output.mkdir(parents=True,exist_ok=True)
    records=[];files=[];sources={}
    for n,root,lo,hi in ((698,a.row698,8,24),(701,a.row701,24,48)):
        stem=f"nf{n}Physical";stage=f"NF{n}Physical"
        receipt=one(root,stem+"-complete-audit.json")
        rm=one(root,"manifest.json")
        ra,rr=read(receipt),read(rm)
        assert rm.parent.name==stage
        assert all(ra[k]==v for k,v in rr.items())
        assert rr["widened_digest"]==m["entries_sha256"]
        assert [r["row"] for r in rr["rows"]]==list(range(lo,hi))
        assert rr["nf631_archive_sha256"]=="e91a83cae117e98608aefa6849dac178e4ddb58dd1dffbfe37304ad248af9ed9"
        assert ra["nf691_accepted_zip_sha256"]=="c0d513078ecb64e1d6ff718fa0163f0e4af229034a11172eaea7d05d17398844"
        expected={"nf691OriginalLookup_eq","nf691OriginalCoverage"}|{v for r in rr["rows"] for v in r["theorems"]}
        assert set(ra["axioms"])==expected and len(expected)==2+3*(hi-lo)
        assert all(set(v)<=ALLOWED for v in ra["axioms"].values())
        sources[stage]={"manifest_sha256":sha(rm),"audit_sha256":sha(receipt)}
        for r in rr["rows"]:
            i=r["row"];j=f"{i:03d}"
            assert (r["H"],r["V"],r["symmetry"])==(i+1,4,242)
            assert sha(rm.parent/r["file"])==r["sha256"]
            v=stem+"Row"+j;z="nf707Attach"+j;src=v+"Payment"
            assert set(r["theorems"])=={v+x for x in ("Fast","ActualBank","PaymentTransport")}
            body=f"""theorem {z}HRowGate :
    (List.finRange 242).all (fun j =>
      decide ({src}.H0 ({i}:Fin 242) j =
        nf702OriginalInputs.payment.H0 ({i}:Fin 242) j)) = true := by
  decide +kernel

theorem {z}HColGate :
    (List.finRange 242).all (fun j =>
      decide ({src}.H0 j ({i}:Fin 242) =
        nf702OriginalInputs.payment.H0 j ({i}:Fin 242))) = true := by
  decide +kernel

theorem {z}VGate :
    (List.finRange 4).all (fun j =>
      decide ({src}.V0 ({i}:Fin 242) j =
        nf702OriginalInputs.payment.V0 ({i}:Fin 242) j)) = true := by
  decide +kernel

theorem {z}EH : {src}.eH = nf702OriginalInputs.payment.eH := by
  decide +kernel

theorem {z}EV : {src}.eV = nf702OriginalInputs.payment.eV := by
  decide +kernel

theorem {z}ActualPayment :
    neutralNF674OriginalRowCheck
      (neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))
      nf702OriginalInputs.payment ({i}:Fin 242) = true := by
  apply {v}PaymentTransport
  · intro j
    exact of_decide_eq_true ((List.all_eq_true.mp {z}HRowGate) j (by simp))
  · intro j
    exact of_decide_eq_true ((List.all_eq_true.mp {z}HColGate) j (by simp))
  · intro j
    exact of_decide_eq_true ((List.all_eq_true.mp {z}VGate) j (by simp))
  · exact {z}EH
  · exact {z}EV

"""
            th=[z+x for x in ("HRowGate","HColGate","VGate","EH","EV","ActualPayment")]
            body+="\n".join("#print axioms "+t for t in th)+"\n"
            name="Attach"+j;path=a.output/(name+".lean")
            path.write_text(filetext(["WeilDefect.Generated.NF702Inputs.Data",f"WeilDefect.Generated.{stage}.Row{j}"],OPT+body))
            files.append({"file":path.name,"sha256":sha(path)})
            records.append({"row":i,"module":name,"source_stage":stage,"theorems":th})
    assert [r["row"] for r in records]==list(range(8,48))
    assert len({n for r in records for n in r["theorems"]})==240
    manifest={"schema":"NF707-full-original-payment-row-attachments-v1","records":records,"files":files,
              "input_manifest_sha256":sha(d/"manifest.json"),"input_audit_sha256":sha(source),"sources":sources,
              "scope":"40 exact original full-payment row candidates; per-row checker only, analytical bank validity still separate."}
    (a.output/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    print("NF707 40 original payment projection candidates / 240 declarations emitted; Lean pending")
if __name__=="__main__": main()
