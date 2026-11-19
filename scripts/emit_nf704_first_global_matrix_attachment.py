#!/usr/bin/env python3
"""Attach accepted NF681 original dot receipts to NF702/NF703 data.
Run only after the complete original scaled-input and cache artifacts exist.
The emitted Lean statements, not the JSON audit, establish projections.
"""
import argparse
import hashlib
import json
from pathlib import Path
from emit_nf630_original_literal_payments import filetext
N=242
MOD="WeilDefect.Generated.NF704Frontier"
OPT="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(d):
    p=d/"manifest.json"
    m=json.loads(p.read_text())
    for x in m["files"]: assert sha(d/x["file"])==x["sha256"],x["file"]
    return m
def main():
    p=argparse.ArgumentParser()
    for k in ("inputs","cache","frontier","input_audit","cache_audit","frontier_audit","output"):
        p.add_argument("--"+k.replace("_","-"),type=Path,required=True)
    p.add_argument("--count",type=int,default=8)
    a=p.parse_args()
    assert 0<a.count<=N
    s,c,f=map(load,(a.inputs,a.cache,a.frontier))
    assert s["rows"]==c["rows"]==N
    assert s["entries_sha256"]==c["entry_sha256"]==f["entry_sha256"]
    for k in ("historical_sha256","payment_sha256"):
        assert s[k]==c[k]==f[k]
    assert c["cache_sha256"]==f["cache_sha256"]
    assert s["source_frame_sha256"]==f["frame_sha256"]
    assert c["frontier_manifest_sha256"]==sha(a.frontier/"manifest.json")
    for d,p0,names,field in (
        (a.inputs,a.input_audit,{"nf702InputH_symm","nf702OriginalW"},"axioms"),
        (a.cache,a.cache_audit,{"nf703HDRow0Projection","nf703HDCol0Projection","nf703ACol0Projection","nf703CacheA_symm"},"axioms"),
        (a.frontier,a.frontier_audit,{f"nf681Col{i:03d}{suf}" for i in range(N) for suf in ("HD","A")},"theorems")):
        audit=json.loads(p0.read_text())
        assert audit["manifest_sha256"]==sha(d/"manifest.json")
        assert names<=set(audit[field])
        assert all(set(v)<={"propext","Classical.choice","Quot.sound"} for v in audit[field].values())
    a.output.mkdir(parents=True,exist_ok=True)
    files=[];names=[]
    def write(name,imports,body,th):
        path=a.output/(name+".lean")
        path.write_text(filetext(imports,OPT+body))
        files.append({"file":path.name,"sha256":sha(path)})
        names.extend(th)
    common="""theorem nf704HRow0Gate :
    (List.finRange 242).all (fun k : Fin 242 =>
      decide (nf681HRow0 k = nf702OriginalInputs.H 0 k)) = true := by
  decide +kernel

theorem nf704HRow0Projection : nf681HRow0 = nf702OriginalInputs.H 0 :=
  funext (fun k => of_decide_eq_true ((List.all_eq_true.mp nf704HRow0Gate) k (by simp)))

theorem nf704HDCol0Projection : nf681HDCol0 = fun k => nf703OriginalCache.HD k 0 :=
  funext nf703HDCol0Projection

#print axioms nf704HRow0Gate
#print axioms nf704HRow0Projection
#print axioms nf704HDCol0Projection
"""
    write("Common",["WeilDefect.Generated.NF702Inputs.Data","WeilDefect.Generated.NF703Cache.Frontier"],common,
          ["nf704HRow0Gate","nf704HRow0Projection","nf704HDCol0Projection"])
    for i in range(a.count):
        j=f"{i:03d}";z=f"nf704Col{j}";d=f"nf681Col{j}"
        body=f"""theorem {z}DGate :
    (List.finRange 242).all (fun k : Fin 242 =>
      decide ({d} k = nf702OriginalInputs.D k ({i}:Fin 242))) = true := by
  decide +kernel

theorem {z}DProjection : {d} = fun k => nf702OriginalInputs.D k ({i}:Fin 242) :=
  funext (fun k => of_decide_eq_true ((List.all_eq_true.mp {z}DGate) k (by simp)))

theorem {z}HD :
    nf703OriginalCache.HDGate nf702OriginalInputs 0 ({i}:Fin 242) = true :=
  neutralNF681HDGate_of_projection nf702OriginalInputs nf703OriginalCache
    0 ({i}:Fin 242) nf681HRow0 {d} (nf681HDRow0 ({i}:Fin 242))
    nf704HRow0Projection {z}DProjection
    (nf703HDRow0Projection ({i}:Fin 242)) {d}HD

theorem {z}A :
    nf703OriginalCache.AGate nf702OriginalInputs ({i}:Fin 242) 0 = true :=
  neutralNF681AGate_of_projection nf702OriginalInputs nf703OriginalCache
    ({i}:Fin 242) 0 {d} nf681HDCol0 (nf681ACol0 ({i}:Fin 242))
    {z}DProjection nf704HDCol0Projection
    (nf703ACol0Projection ({i}:Fin 242)) {d}A

"""
        th=[z+suf for suf in ("DGate","DProjection","HD","A")]
        body+="\n".join("#print axioms "+n for n in th)+"\n"
        write("Col"+j,[MOD+".Common","WeilDefect.Generated.NF681.Col"+j],body,th)
    manifest={"schema":"NF704-global-matrix-projection-proposals-v1","columns":a.count,
              "global_gate_targets":2*a.count,"audit_theorems":names,"files":files,
              "input_manifest_sha256":sha(a.inputs/"manifest.json"),
              "cache_manifest_sha256":sha(a.cache/"manifest.json"),
              "frontier_manifest_sha256":sha(a.frontier/"manifest.json"),
              "scope":"Source-bound proposals only. Kernel must prove operand and result projection gates."}
    (a.output/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    print(f"NF704 {2*a.count} actual global matrix gate proposals; kernel pending")
if __name__=="__main__": main()
