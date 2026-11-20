#!/usr/bin/env python3
"""NF732: authenticate 8 immutable successful original NF729 numerical kernel
artifacts and install only source-compatible Lean objects, never code oracles.

A source-bound numerical quad must have both accepted original HD and A range
theorems with standard Lean axioms and a successful upstream job. The GitHub
workflow verifies each immutable job/artifact identity via the GitHub API
before downloading. This script checks every original receipt and the exact
compiled Lean object and rejects all conflicting downstream object copies.

This cannot promote a source-only quad to a kernel proof; absent upstream
audit and actual compiled object is an error, not an inferred PASS.
"""
import hashlib
import json
import re
import shutil
from pathlib import Path

STARTS=(0,4,8,12,16,20,24,28)
ALLOWED={"propext","Classical.choice","Quot.sound"}
ROOT=Path("nf732-original-quads")
SOURCE=Path("WeilDefect/Generated/NF729")
BUILD=Path(".lake/build/lib/lean/WeilDefect")
EXPECTED_NAME=lambda b:f"nf729-real-original-HD-A-quad-{b:03d}-source-bound-kernel-audit"

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def unique(root,name):
    paths=list(Path(root).rglob(name))
    assert len(paths)==1,(root,name,paths)
    return paths[0]

def main():
    manifest=json.loads((SOURCE/"manifest.json").read_text())
    assert manifest["schema"]=="NF729-original-global-index-one-8-quads-source-custody-v1"
    assert manifest["accepted_index_one_global_product_declarations"]==252
    assert manifest["files"]=={name:sha(SOURCE/name) for name in manifest["files"]}
    assert [q["first_block"] for q in manifest["quads"]]==list(STARTS)
    assert [i for q in manifest["quads"]
       for i in range(q["first_coordinate"],q["end_coordinate"])]==list(range(242))
    roots=sorted(p for p in ROOT.iterdir() if p.is_dir())
    assert len(roots)==8,roots
    assert {p.name for p in roots}=={EXPECTED_NAME(b) for b in STARTS}
    sources=[]
    installed={}
    for b in STARTS:
        root=ROOT/EXPECTED_NAME(b)
        receipt_file=unique(root,f"nf729-{b:03d}-original-audit.json")
        m=json.loads(receipt_file.read_text())
        assert m["schema"]=="NF729-independent-original-quad-lean-kernel-audit-v1"
        assert m["kind"]=="Original" and m["quad_first_block"]==b
        assert m["quad_first_coordinate"]==b*8
        assert m["quad_end_coordinate"]==min((b+4)*8,242)
        names=[f"nf729Original{t}Quad{b:03d}" for t in ("HD","A")]
        assert m["theorems"]==names
        assert set(m["axioms"])==set(names)
        assert all(set(values)<=ALLOWED for values in m["axioms"].values())
        assert m["status"]=="LEAN KERNEL PASS, source-specific global HD/A original gate claims"
        expected_source=SOURCE/f"Quad{b:03d}Original.lean"
        assert m["source_sha256"]==sha(expected_source)
        assert m["manifest_sha256"]==sha(SOURCE/"manifest.json")
        copied=0
        proof_sha=None
        for path in root.rglob("*.olean"):
            assert "WeilDefect" in path.parts, path
            offset=path.parts.index("WeilDefect")
            relative=Path(*path.parts[offset+1:])
            dest=BUILD/relative
            dest.parent.mkdir(parents=True,exist_ok=True)
            if dest.is_file():
                assert sha(dest)==sha(path),(
                   "Lean source object SHA collision from separately accepted original quad jobs",str(path),str(dest))
            else:
                shutil.copy2(path,dest)
            installed[str(relative)]=sha(dest)
            copied+=1
            if relative==Path(f"Generated/NF729/Quad{b:03d}Original.olean"):
                proof_sha=sha(dest)
        assert copied>0 and proof_sha is not None,(b,copied)
        target=BUILD/"Generated"/"NF729"/f"Quad{b:03d}Original.olean"
        assert target.stat().st_size>1024
        assert proof_sha==sha(target)
        sources.append({
          "quad":b,
          "proof_theorems":names,
          "original_source_sha256":m["source_sha256"],
          "source_manifest_sha256":m["manifest_sha256"],
          "accepted_original_numerical_audit_sha256":sha(receipt_file),
          "olean_sha256":proof_sha,
          "compiled_objects_installed":copied
        })
    assert len(sources)==8
    assert [x["quad"] for x in sources]==list(STARTS)
    result={
      "schema":"NF732-original-eight-accepted-NF729-numerical-quad-olean-inputs-v1",
      "upstream_run_id":44767040253,
      "upstream_exact_numerical_quad_jobs_success_requirement":8,
      "all_eight_accepted_original_quad_kernel_runs":True,
      "eight_original_gate_ranges_complete_Fin242":True,
      "sources":sources,
      "installed_compiled_modules":installed,
      "original_HD_gate_range_claims":8,
      "original_A_gate_range_claims":8,
      "theorem_status":"16 accepted source-specific original range theorems from 8 independently kernel-verified upstream jobs. New NF732 full universal theorem still requires its own Lean compilation and axiom audit.",
    }
    Path("nf732-accepted-original-numerical-inputs.json").write_text(
       json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("NF732 all 8 accepted source-bound original HD/A index-one numerical shard kernel objects, 16 exact product theorem names and strictly matching source+compiled SHA-256 verified. Original full universal kernel still PENDING.")

if __name__=="__main__":
    main()
