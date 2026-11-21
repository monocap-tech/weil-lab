#!/usr/bin/env python3
"""CP010 fail-closed REAL Lean v4.35 dual-source sign certificate audit.

Does not promote numerical mpmath evidence to a kernel pass. Requires:
  * pinned original upstream 1e6 source/Git SHA,
  * real compilations of both genuine original method-specific Lean tactics,
  * exact local source/manifests and original RS source enclosure,
  * actual .olean and standard-only two #print axioms receipts.
Not a proof of all-million-height refined zeros or Weil EF equivalence.
"""
import hashlib
import json
import re
from pathlib import Path

from cp010_dual_method_root53_pilot import (
    DIR, LEAN, EULER, RS, E_MANIFEST, R_MANIFEST, SOURCE_TAG,
    SOURCE_RS_SHA, strict_candidates, source_first_rs
)

OLEAN=DIR/".lake/build/lib/lean/CP010DualMethods.olean"
LOG=DIR/"cp010-direct-axioms.log"
RECEIPT=DIR/"cp010-dual-methods-lean-receipt.json"
SOURCE_REFERENCE=DIR/"source_original_first_rs.txt"
TARGETS=[
    "CP010DualMethods.coarseRiemannSiegelCandidate",
    "CP010DualMethods.narrowEulerMaclaurinCandidate",
]
ALLOWED={"propext","Classical.choice","Quot.sound"}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    assert strict_candidates()
    assert all(x.is_file() for x in
               [OLEAN,LOG,SOURCE_REFERENCE,LEAN,EULER,RS,E_MANIFEST,R_MANIFEST])
    assert DIR.joinpath("lean-toolchain").read_text().strip()=="leanprover/lean4:v4.35.0"
    source_first_rs(SOURCE_REFERENCE)
    source=LEAN.read_text("utf-8")
    log=LOG.read_text("utf-8")
    assert not re.search(r"\bsorry\b",source) and "sorryAx" not in log and "error:" not in log
    reports={}
    for target in TARGETS:
        rx=re.compile(re.escape("'"+target+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
        found=rx.findall(log)
        assert len(found)==1, f"Need exactly one genuine compiled axiom receipt: {target}"
        deps={x.strip() for x in found[0].split(",") if x.strip()}
        assert deps<=ALLOWED, f"Unsafe/missing-standard axiom certificate: {target} {deps-ALLOWED}"
        reports[target]=sorted(deps)
    receipt={
        "status":"CP010_DUAL_METHODS_V435_KERNEL_PASS_ONLY",
        "scope":"One coarse RS plus independent narrow Euler first-RS-row certificates, not same-root ID or full Weil",
        "pinned_upstream_commit":SOURCE_TAG,
        "original_first_RS_git_blob_sha":SOURCE_RS_SHA,
        "source_sha256":sha(LEAN),
        "olean_sha256":sha(OLEAN),
        "first_RS_full_source_sha256":sha(SOURCE_REFERENCE),
        "euler_candidate_store_sha256":sha(EULER),
        "rs_candidate_store_sha256":sha(RS),
        "euler_candidate_manifest_sha256":sha(E_MANIFEST),
        "rs_candidate_manifest_sha256":sha(R_MANIFEST),
        "axioms":reports,
    }
    RECEIPT.write_text(json.dumps(receipt,indent=2)+"\n","utf-8")
    print(receipt["status"])
    print("Actual full source identity and compiled 2-method root count test only; original signed Weil dictionary OPEN")

if __name__=="__main__":
    main()
