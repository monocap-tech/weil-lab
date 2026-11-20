#!/usr/bin/env python3
"""NF710: exact 242-row global vector certification inventory and aggregation plan.

NF709 emits actual source-specific Lean vector gates; this script builds a
total, disjoint 16-row schedule and proof modules for terminal assembly.
No generated theorem is claimed accepted until the corresponding Lean audit.
"""
import argparse, hashlib, json, subprocess
from pathlib import Path
from emit_nf630_original_literal_payments import filetext

N, WIDTH = 242, 16
PREFIX = "WeilDefect.Generated.NF710Vectors"
OPT = "set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row_theorem(i):
    return f"nf709Row{i:03d}Vector"


def emit_shard(start, end):
    size = end-start
    tag = f"Shard{start:03d}"
    th = f"nf710Vector{tag}"
    body = f"""theorem {th} (j : Fin {size}) :
    nf703OriginalCache.vectorGate nf702OriginalInputs
      (⟨{start} + j.val, by omega⟩ : Fin 242) = true := by
  fin_cases j
"""
    for i in range(start, end):
        body += f"  · exact {row_theorem(i)}\n"
    body += f"\n#print axioms {th}\n"
    return tag, th, body


def main():
    p = argparse.ArgumentParser()
    for key in ("inputs","cache","vectors","input_audit","cache_audit","vector_audit","output"):
        p.add_argument("--"+key.replace("_","-"),type=Path,required=True)
    a = p.parse_args()
    base=Path("WeilDefect/Generated/NF709")
    call=["python", "scripts/emit_nf709_original_global_vector_attachments.py"]
    for k in ("inputs","cache","vectors","input_audit","cache_audit","vector_audit"):
        call += ["--"+k.replace("_","-"),str(getattr(a,k))]
    call += ["--output",str(base),"--first","0","--count","242"]
    subprocess.run(call,check=True)
    source=json.loads((base/"manifest.json").read_text())
    assert source["schema"]=="NF709-global-original-vector-attachments-v1"
    assert source["rows"]==list(range(N)) and source["first"]==0 and source["count"]==N
    assert len(source["files"])==N+1 and len(source["theorems"])==6+14*N
    assert len(set(source["theorems"]))==len(source["theorems"])
    for entry in source["files"]:
        assert sha(base/entry["file"])==entry["sha256"]
    a.output.mkdir(parents=True,exist_ok=True)
    files=[]
    shards=[]
    for start in range(0,N,WIDTH):
        end=min(N,start+WIDTH)
        name, theorem, body=emit_shard(start,end)
        imports=[f"WeilDefect.Generated.NF709.Row{i:03d}" for i in range(start,end)]
        path=a.output/(name+".lean")
        path.write_text(filetext(imports,OPT+body))
        files.append({"file":path.name,"sha256":sha(path)})
        shards.append({"start":start,"end":end,"module":name,"theorem":theorem,
                       "rows":list(range(start,end))})
    assert len(shards)==16 and shards[-1]["rows"]==[240,241]
    assert [i for sh in shards for i in sh["rows"]]==list(range(N))
    names=[row_theorem(i) for i in range(N)]
    assert set(names)<=set(source["theorems"])
    body="""theorem nf710EveryOriginalVector (i : Fin 242) :
    nf703OriginalCache.vectorGate nf702OriginalInputs i = true := by
  fin_cases i
"""
    for i in range(N):
        body+=f"  · exact {row_theorem(i)}\n"
    body+="""

theorem nf710OriginalVectorCheck :
    (List.finRange 242).all
      (nf703OriginalCache.vectorGate nf702OriginalInputs) = true := by
  apply List.all_eq_true.mpr
  intro i _
  exact nf710EveryOriginalVector i

#print axioms nf710EveryOriginalVector
#print axioms nf710OriginalVectorCheck
"""
    f=a.output/"All.lean"
    f.write_text(filetext([PREFIX+"."+s["module"] for s in shards],OPT+body))
    files.append({"file":f.name,"sha256":sha(f)})
    result={
        "schema":"NF710-global-original-vector-aggregation-v1",
        "rows":N,"width":WIDTH,"shards":shards,
        "local_source_manifest_sha256":sha(base/"manifest.json"),
        "source_manifests":source["source_manifests"],
        "accepted_prior_audits":source["accepted_audits"],
        "global_vector_gates":N,
        "source_declarations":len(source["theorems"]),
        "shard_theorems":[s["theorem"] for s in shards],
        "terminal_theorems":["nf710EveryOriginalVector","nf710OriginalVectorCheck"],
        "files":files,
        "scope":"Exhaustive Lean proof candidates; cannot mark original vector check true until all NF709 row gates and NF710 aggregate audit compile. HD/A and payment validity separate."
    }
    (a.output/"manifest.json").write_text(json.dumps(result,indent=2)+"\n")
    print(f"NF710 242-row disjoint vector schedule PASS: {len(shards)} shards, "
          f"{len(source['theorems'])} pending NF709 declarations, "
          f"{len(shards)+2} aggregate theorem candidates; kernel pending")


if __name__=="__main__":
    main()
