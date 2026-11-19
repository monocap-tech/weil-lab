#!/usr/bin/env python3
"""Generate exact NF621 metadata and all original source-row coverage gates.

This does not certify the numerical moment bank; dummy moment values
are never used as enclosures. The row proposals preserve all original
selected and critical source pair lookups, including the pole.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from tempfile import TemporaryDirectory
from emit_nf627_original_moment_bank import keylit,metadata_body,filetext
from verify_nf622_physical_entry_reassembly import read_shards
sys.set_int_max_str_digits(0)
MODULE="WeilDefect.Generated.NF679"
BASE="WeilDefect.Arithmetic.ActualZetaOriginalPhysicalCoverageRows"
OPTIONS="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
N=242

def emit(data,hashes,out):
    out.mkdir(parents=True,exist_ok=True)
    files=[]
    def write(name,imports,body):
        p=out/(name+".lean")
        p.write_text(filetext(imports,body),encoding="utf8")
        files.append({"file":p.name,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
    shapes=["⟨"+keylit(k)+f", Array.replicate {len(rows)} ⟨0,0,0⟩⟩" for k,rows in sorted(data.items())]
    body=metadata_body(shapes)
    # Keep the retained NF627 shape construction, but isolate names.
    body=body.replace("nf627Meta","nf679Meta")
    write("Metadata",[BASE],body)
    for i in range(N):
        name=f"nf679CoverageRow{i:03d}"
        write(f"Row{i:03d}",[MODULE+".Metadata"],OPTIONS+
            f"theorem {name} :\n"
            f"    neutralNF679CoverageRow nf679Meta (neutralNF624Index nf679Meta) ({i} : Fin 242) = true := by\n"
            "  decide +kernel\n\n"+f"#print axioms {name}")
    body=OPTIONS+"theorem nf679AllCoverageRows : ∀ i : Fin 242,\n    neutralNF679CoverageRow nf679Meta (neutralNF624Index nf679Meta) i = true := by\n  intro i\n  fin_cases i\n"
    for i in range(N):
        body+=f"  · exact nf679CoverageRow{i:03d}\n"
    body+="\ntheorem nf679MetadataCoverage :\n    neutralNF624CoverageCheck nf679Meta (neutralNF624Index nf679Meta) = true :=\n  neutralNF679Coverage_of_rows nf679Meta (neutralNF624Index nf679Meta) nf679AllCoverageRows\n\n#print axioms nf679AllCoverageRows\n#print axioms nf679MetadataCoverage"
    write("AllRows",[MODULE+f".Row{i:03d}" for i in range(N)],body)
    m={"schema":"NF679-original-metadata-row-proposals-v1","input_sha256":hashes,
       "keys":len(data),"moment_rows":sum(map(len,data.values())),
       "source_rows":N,"selected_pair_lookups":N*N*4,"mixed_pair_lookups":N*4*33*4,
       "files":files,
       "scope":"Actual original frequency/degree metadata only; no analytic moment validity, bank shape binding or numerical inequalities asserted."}
    (out/"manifest.json").write_text(json.dumps(m,indent=2)+"\n")
    return m

def self_test():
    from fractions import Fraction as F
    with TemporaryDirectory() as d:
        out=Path(d)
        m=emit({(F(0),F(1)):[(7,8,9)],(F(1),F(0)):[(1,2,3),(4,5,6)]},{},out)
        assert (m["keys"],m["moment_rows"],len(m["files"]))==(2,3,N+2)
        assert "nf679MetaPart000" in (out/"Metadata.lean").read_text()
        assert "nf627Meta" not in (out/"Metadata.lean").read_text()
        assert "(241 : Fin 242)" in (out/"Row241.lean").read_text()
        assert "nf679CoverageRow241" in (out/"AllRows.lean").read_text()
        for row in m["files"]:
            assert hashlib.sha256((out/row["file"]).read_bytes()).hexdigest()==row["sha256"]
    print("NF679 synthetic serialization PASS; no source coverage proof claimed")

def main():
    p=argparse.ArgumentParser()
    for k in ("root","shards","coverage","output"):
        p.add_argument("--"+k,type=Path)
    p.add_argument("--self-test",action="store_true")
    a=p.parse_args()
    if a.self_test:
        self_test()
        return
    assert all((a.root,a.shards,a.coverage,a.output))
    data=read_shards(a.root,a.shards)
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in a.shards.rglob("nf621-shard*.json.gz")}
    coverage=json.loads(a.coverage.read_text())
    assert len(hashes)==8
    assert hashes=={s["file"]:s["sha256"] for s in coverage["shards"]}
    assert len(data)==coverage["nonzero_keys"]==7835
    assert sum(map(len,data.values()))==coverage["nonzero_rows"]==37994
    m=emit(data,hashes,a.output)
    print("NF679 emitted",m["source_rows"],"literal original source coverage proposals,",
          m["keys"],"keys,",m["moment_rows"],"moment rows; Lean pending")

if __name__=="__main__":
    main()
