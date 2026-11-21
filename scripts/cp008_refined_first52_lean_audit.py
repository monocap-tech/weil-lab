#!/usr/bin/env python3
"""CP008 strict direct Zeta v4.35 Lean batch/source/olean axiom audit.

Acceptance ONLY after actual `lake build CP008First52` and real
`lake env lean CP008First52.lean`. Checks THIS refined data store's bytes.
External prebuilt Zeta dependency has its own immutable release trust boundary;
passing here never imports or proves the original Weil-Lab v4.34 dictionary.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT/"cp008_zeta_v435"
SOURCE=PROJECT/"CP008First52.lean"
OLEAN=PROJECT/".lake/build/lib/lean/CP008First52.olean"
STORE=PROJECT/"python/out/euler_maclaurin/zeros/zeros_00001.txt"
MANIFEST=STORE.parent/"manifest.json"
LOG=PROJECT/"cp008-direct-lean-axioms.log"
RECEIPT=PROJECT/"cp008-refined-first52-kernel-audit.json"
TARGET="CP008First52.refinedCandidateBatch"
AXIOMS={"propext","Classical.choice","Quot.sound"}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    assert all(f.is_file() for f in (SOURCE,OLEAN,STORE,MANIFEST,LOG)), "Missing actual compiled .olean, source, data or axiom log"
    assert PROJECT.joinpath("lean-toolchain").read_text().strip()=="leanprover/lean4:v4.35.0"
    source=SOURCE.read_text(encoding="utf-8")
    log=LOG.read_text(encoding="utf-8")
    assert "theorem refinedCandidateBatch" in source and "build_batch 0 52" in source
    assert not re.search(r"\bsorry\b",source), "Source uses sorry"
    assert "sorryAx" not in log and "error:" not in log, "Kernel failed or nonstandard sorryAx found"
    regex=re.compile(re.escape("'"+TARGET+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
    found=regex.findall(log)
    assert len(found)==1, f"Require exactly one actual Lean axiom declaration for {TARGET}, saw {len(found)}"
    axioms={s.strip() for s in found[0].split(",") if s.strip()}
    assert axioms<=AXIOMS, f"Unsafe/nonstandard Lean axioms: {axioms-AXIOMS}"
    rows=STORE.read_text().splitlines()
    assert len(rows)==52 and rows[0].startswith("1, 14.13472, 14.13473, ")
    assert rows[-1].startswith("52, 147.42276, 147.42277, ")
    receipt={
        "status":"CP008_REFINED_FIRST52_ZETA_V435_KERNEL_PASS",
        "scope":"52 new individual Euler-Maclaurin sign-change brackets, not full 1.748m count, Weil RH or spectral compatibility",
        "original_upstream_tag":"v1-1e6",
        "source_commit":"c06b4e13d9c847e50a32c3d738271cbad62ae9f3",
        "runtime_toolchain":"leanprover/lean4:v4.35.0",
        "data_sha256":sha(STORE),
        "manifest_sha256":sha(MANIFEST),
        "source_sha256":sha(SOURCE),
        "olean_sha256":sha(OLEAN),
        "axioms":sorted(axioms),
    }
    RECEIPT.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print(receipt["status"])

if __name__=="__main__":
    main()
