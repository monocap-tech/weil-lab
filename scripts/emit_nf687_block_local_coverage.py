#!/usr/bin/env python3
"""Compact block-local metadata, derived only from pinned original NF679/NF682 sources.
No new numerical moment values. The complete 68-group proof candidates retain
the exact NF682 partitions and source map, with a block-local reader/index.
"""
import argparse,hashlib,json,re
from pathlib import Path
from fractions import Fraction as F
from emit_nf627_original_moment_bank import filetext,qlit
MOD="WeilDefect.Generated.NF687"
BASE="WeilDefect.Arithmetic.ActualZetaOriginalPhysicalBlockLocalCoverage"
OPT="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def validate(d):
    m=json.loads((d/"manifest.json").read_text())
    for r in m["files"]:
        p=d/r["file"]
        # The retained NF682 ZIP includes only NF679's metadata and manifest.
        if d.name=="NF679" and p.name!="Metadata.lean": continue
        assert sha(p)==r["sha256"],p
    return m
def main():
    p=argparse.ArgumentParser()
    for k in ("metadata","groups","output"):p.add_argument("--"+k,type=Path,required=True)
    a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
    md,gm=validate(a.metadata),validate(a.groups)
    assert (md["keys"],md["moment_rows"])==(7835,37994)
    assert gm["metadata_sha256"]==sha(a.metadata/"Metadata.lean")
    assert gm["metadata_manifest_sha256"]==sha(a.metadata/"manifest.json")
    source=(a.metadata/"Metadata.lean").read_text()
    pat=r"⟨⟨\((-?\d+/\d+):ℚ\),\((-?\d+/\d+):ℚ\)⟩, Array\.replicate (\d+) ⟨0,0,0⟩⟩"
    shapes=[(F(h),F(f),int(n)) for h,f,n in re.findall(pat,source)]
    assert len(shapes)==7835 and sum(n for h,f,n in shapes)==37994
    assert len({(h,f) for h,f,n in shapes})==7835
    assert shapes==sorted(shapes)
    files=[]
    def write(name,imports,body):
        q=a.output/(name+".lean");q.write_text(filetext(imports,OPT+body),encoding="utf8")
        files.append({"file":q.name,"sha256":sha(q)})
    blocks=[]
    for start in range(0,len(shapes),128):
        name=f"Block{start//128:03d}";v="nf687"+name;blocks.append(name)
        vals=",\n  ".join(f"(⟨{qlit(h)},{qlit(f)}⟩,{n})" for h,f,n in shapes[start:start+128])
        write(name,[BASE],f"def {v} : Array NF687Shape := #[\n  {vals}\n]")
    body="def nf687Parts : Array (Unit → Array NF687Shape) := #[\n  "+",\n  ".join("fun _ => nf687"+v for v in blocks)+"\n]\n\n"
    body+="""
def nf687Size : ℕ := 7835

def nf687Read (i : ℕ) : NF687Shape :=
  let p := (nf687Parts[i / 128]?).getD (fun _ => #[])
  ((p ())[i % 128]?).getD (⟨0,0⟩,0)

def nf687Index : NF616Frequency → ℕ :=
  neutralNF687Index nf687Read nf687Size
"""
    write("Compact",[MOD+"."+v for v in blocks],body)
    for i in range(68):
        name=f"Group{i:02d}"
        old=(a.groups/(name+".lean")).read_text()
        imports=[x.split(" ",1)[1] for x in old.splitlines() if x.startswith("import ")]
        assert "WeilDefect.Generated.NF679.Metadata" in imports
        imports=[MOD+".Compact" if x=="WeilDefect.Generated.NF679.Metadata" else x for x in imports]
        body=old.split("namespace WeilDefect\n",1)[1].rsplit("end WeilDefect",1)[0].strip()
        body=body.replace(OPT.strip(),"").lstrip()
        for sym in ("SelectedAt","MixedAt","GroupRow"):
            body=body.replace("neutralNF682"+sym,"neutralNF687"+sym)
        body=body.replace("nf679Meta (neutralNF624Index nf679Meta)","nf687Read nf687Size nf687Index")
        body=body.replace(f"nf682Group{i:02d}",f"nf687Group{i:02d}")
        assert "nf679Meta" not in body
        write(name,imports,body)
    common=["WeilDefect.Generated.NF682.Maps","WeilDefect.Generated.NF682.Partitions"]
    write("Pilot",common+[MOD+".Compact"],"""
theorem nf687PilotAt : neutralNF687SelectedAt nf687Read nf687Size nf687Index nf682Top 0 0=true := by
  decide +kernel

theorem nf687PilotBatch : nf682HPart00.all
    (neutralNF687SelectedAt nf687Read nf687Size nf687Index nf682Top 0)=true := by
  decide +kernel

#print axioms nf687PilotAt
#print axioms nf687PilotBatch
""")
    write("Reference",common+["WeilDefect.Generated.NF679.Metadata"],"""
theorem nf687ReferenceAt : neutralNF682SelectedAt nf679Meta
    (neutralNF624Index nf679Meta) nf682Top 0 0=true := by
  decide +kernel

#print axioms nf687ReferenceAt
""")
    indices=[0,127,128,255,256,4095,4096,7834]
    body=""
    for j,i in enumerate(indices):
        body+=f"theorem nf687ShapeSample{j} : neutralNF627ShapeAt nf679Meta {i}=nf687Read {i} := by\n  decide +kernel\n#print axioms nf687ShapeSample{j}\n\n"
    write("ShapeSamples",[MOD+".Compact","WeilDefect.Generated.NF679.Metadata"],body)
    body="theorem nf687AllRows : ∀ i : Fin 68,\n    neutralNF687GroupRow nf687Read nf687Size nf687Index nf682Top i=true := by\n  intro i\n  fin_cases i\n"
    for i in range(68):body+=f"  · exact nf687Group{i:02d}Check\n"
    body+="""
theorem nf687CoverageOnBank (bank : Array NF624KeyTable)
    (hs : bank.size=nf687Size)
    (hr : ∀ i<nf687Size, neutralNF627ShapeAt bank i=nf687Read i) :
    neutralNF624CoverageCheck bank (neutralNF624Index bank)=true := by
  rw [neutralNF687Index_eq bank nf687Read nf687Size hs hr]
  exact neutralNF682CoverageCheck_of_coverage _ _
    (neutralNF687Coverage_of_groups bank nf687Read nf687Size hs hr
      nf687Index nf682Top nf682Group nf682DomAll nf687AllRows)

#print axioms nf687AllRows
#print axioms nf687CoverageOnBank
"""
    write("AllGroups",[MOD+f".Group{i:02d}" for i in range(68)],body)
    m={"schema":"NF687-block-local-coverage-proposals-v1","keys":len(shapes),
       "rows":sum(n for h,f,n in shapes),"blocks":len(blocks),"block_width":128,
       "metadata_sha256":sha(a.metadata/"Metadata.lean"),"group_manifest_sha256":sha(a.groups/"manifest.json"),
       "group_proposals":68,"pilot_groups":[0,67],"pilot_shape_indices":indices,"files":files,
       "scope":"All group proposals, two-group pilot only, full exact actual numerical bank shape attachment not asserted."}
    (a.output/"manifest.json").write_text(json.dumps(m,indent=2)+"\n")
    print("NF687 original compact metadata: 62 blocks, 7835 keys, 37994 row counts, 68 group candidates; kernel pending")
if __name__=="__main__":main()
