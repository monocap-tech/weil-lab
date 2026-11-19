#!/usr/bin/env python3
"""NF682: retain original NF679 metadata, generate maximum-degree group proof proposals.

The 67 oscillator blocks and actual pole are only a proposed compression.
Lean checks every source index's same-key and degree-domination relation.
Every grouped coverage request is still the exact NF624 lookup predicate.
"""
import argparse,hashlib,json,re
from pathlib import Path
from emit_nf627_original_moment_bank import filetext
MOD="WeilDefect.Generated.NF682"
BASE="WeilDefect.Arithmetic.ActualZetaOriginalPhysicalFrequencyBlockCoverage"
META="WeilDefect.Generated.NF679.Metadata"
OPT="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser()
    for k in ("root","metadata","output"):
        p.add_argument("--"+k,type=Path,required=True)
    a=p.parse_args()
    m=json.loads((a.metadata/"manifest.json").read_text())
    assert (m["keys"],m["moment_rows"],m["source_rows"])==(7835,37994,242)
    md=next(x for x in m["files"] if x["file"]=="Metadata.lean")
    assert sha(a.metadata/"Metadata.lean")==md["sha256"]
    source=a.root/"WeilDefect/Arithmetic/ActualZetaOriginalJ242ExponentialSignature.lean"
    groups=re.findall(r"\(\((\d+(?:/\d+)?)\s*:\s*ℚ\),\s*(\d+)\)",source.read_text())
    assert len(groups)==67 and sum(int(n) for _,n in groups)==241
    assert all(int(n)>0 for _,n in groups)
    tops=[]; mapping=[]; end=0
    for i,(_,n) in enumerate(groups):
        n=int(n);end+=n;tops.append(end-1);mapping.extend([i]*n)
    tops.append(241);mapping.append(67)
    assert len(tops)==68 and len(mapping)==242
    a.output.mkdir(parents=True,exist_ok=True)
    files=[]
    def write(name,imports,body):
        q=a.output/(name+".lean")
        q.write_text(filetext(imports,OPT+body),encoding="utf8")
        files.append({"file":q.name,"sha256":sha(q)})
    vec=lambda xs: "#["+", ".join(map(str,xs))+"]"
    body=f"""def nf682TopData : Array (Fin 242) := {vec(tops)}
def nf682GroupData : Array (Fin 68) := {vec(mapping)}
def nf682Top (i : Fin 68) : Fin 242 := nf682TopData[i.val]!
def nf682Group (i : Fin 242) : Fin 68 := nf682GroupData[i.val]!

theorem nf682DomGate :
    (List.finRange 242).all (neutralNF682DomRow nf682Top nf682Group) = true := by
  decide +kernel

theorem nf682DomAll (i : Fin 242) :
    neutralNF682DomRow nf682Top nf682Group i = true :=
  (List.all_eq_true.mp nf682DomGate) i (by simp)

#print axioms nf682DomGate
#print axioms nf682DomAll
"""
    # Maps deliberately does not import the large bank metadata.
    write("Maps",[BASE],body)
    body=""
    partitions={}
    for lbl,n in (("H",68),("V",33)):
        names=[]
        for start in range(0,n,8):
            name=f"nf682{lbl}Part{start//8:02d}";names.append(name)
            body+=f"def {name} : List (Fin {n}) := ["+", ".join(map(str,range(start,min(start+8,n))))+"]\n"
        parts=f"nf682{lbl}Parts"
        body+=f"def {parts} : List (List (Fin {n})) := ["+", ".join(names)+"]\n"
        body+=f"theorem nf682{lbl}Partition : {parts}.flatten = List.finRange {n} := by\n  decide +kernel\n\n"
        partitions[lbl]=names
    write("Partitions",[BASE],body)
    for i in range(68):
        z=f"nf682Group{i:02d}"
        body=""
        checks=[]
        for lbl,func in (("H","neutralNF682SelectedAt"),("V","neutralNF682MixedAt")):
            names=partitions[lbl]
            proofnames=[]
            pred=f"({func} nf679Meta (neutralNF624Index nf679Meta) nf682Top ({i}:Fin 68))"
            for j,block in enumerate(names):
                name=f"{z}{lbl}{j:02d}"
                body+=f"theorem {name} : {block}.all {pred} = true := by\n  decide +kernel\n\n"
                proofnames.append(name);checks.append(name)
            n=68 if lbl=="H" else 33
            body+=f"theorem {z}{lbl}All : (List.finRange {n}).all {pred} = true := by\n"
            body+=f"  rw [← nf682{lbl}Partition]\n"
            body+=f"  simp only [nf682{lbl}Parts, List.flatten_cons, List.flatten_nil, List.all_append, List.all_nil, "+", ".join(proofnames)+", Bool.and_self]\n\n"
            checks.append(f"{z}{lbl}All")
        body+=f"""theorem {z}Check :
    neutralNF682GroupRow nf679Meta (neutralNF624Index nf679Meta) nf682Top ({i}:Fin 68) = true := by
  simp only [neutralNF682GroupRow, {z}HAll, {z}VAll, Bool.and_self]

"""
        checks.append(f"{z}Check")
        body+="\n".join("#print axioms "+name for name in checks)
        write(f"Group{i:02d}",[MOD+".Maps",MOD+".Partitions",META],body)
    body="theorem nf682AllGroups : ∀ i : Fin 68,\n    neutralNF682GroupRow nf679Meta (neutralNF624Index nf679Meta) nf682Top i = true := by\n  intro i\n  fin_cases i\n"
    for i in range(68):
        body+=f"  · exact nf682Group{i:02d}Check\n"
    body+="""
theorem nf682MetadataCoverage :
    neutralNF624CoverageCheck nf679Meta (neutralNF624Index nf679Meta) = true :=
  neutralNF682CoverageCheck_of_coverage _ _
    (neutralNF682Coverage_of_groups _ _ nf682Top nf682Group nf682DomAll nf682AllGroups)

#print axioms nf682AllGroups
#print axioms nf682MetadataCoverage
"""
    write("AllGroups",[MOD+f".Group{i:02d}" for i in range(68)],body)
    report={"schema":"NF682-original-frequency-block-proposals-v1",
            "metadata_sha256":md["sha256"],"metadata_manifest_sha256":sha(a.metadata/"manifest.json"),
            "source_signature_sha256":sha(source),"groups":68,"original_sources":242,
            "original_lookup_requests":362032,
            "group_selected_requests":68*68*4,"group_mixed_requests":68*33*4,
            "domination_requests":242*2,"lookup_batch_max":32,"files":files,
            "scope":"Original metadata coverage candidates; analytic moment validity and numeric-bank shape independent."}
    (a.output/"manifest.json").write_text(json.dumps(report,indent=2)+"\n")
    print("NF682 original group proposals: 27472 lookup requests, 484 source domination relations; kernel pending")
if __name__=="__main__": main()
