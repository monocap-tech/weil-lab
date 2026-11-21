#!/usr/bin/env python3
"""CP013 SHA-pinned original RS-only source theorem-lineage audit.

Verifies that a newly generated separate Lean proof reuses EXACTLY all 124
original first-group RS batches + all 69 remaining original RS-only groups,
with every intermediate count/endpoint derived from REAL frozen upstream
source signatures. No new zero/bracket data, source-index proof, original
Weil/spectral equality, or Lean kernel receipt is supplied by this script.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM_COMMIT = "c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
GROUP1_REL = "Zeta/Zeros/Certificates/Groups/Level1/Group0001.lean"
ASSEMBLER_REL = "Zeta/Zeros/Certificates.lean"
SHA = {
    GROUP1_REL: "12263d2f09d5a69c489c29c63940829e2c7211dc",
    ASSEMBLER_REL: "54fce07cbc5bf0913ceccb108cbf73f1227857c0",
}
RS_ONLY = ROOT/"cp011_zeta_v435/CP013RSOnly.lean"
SEAM = ROOT/"cp011_zeta_v435/CP013Seam.lean"
RS_RE = re.compile(
    r"theorem upTo_RS(\d{4}) : BatchSpec (\d+) 1000 1000 (\d+) 1000 :="
)
GROUP_RE = re.compile(
    r"theorem upTo_G(\d{4}) : BatchSpec (\d+) 1000 1000 (\d+) 1000 :="
)
MISSING = "NOT_READY"

def git_sha(path):
    n = path.stat().st_size
    h = hashlib.sha1(b"blob "+str(n).encode("ascii")+b"\0")
    with path.open("rb") as f:
        for p in iter(lambda:f.read(1<<20),b""):
            h.update(p)
    return h.hexdigest()

def declarations(contents, rx):
    rows = [tuple(map(int, m.groups())) for m in rx.finditer(contents)]
    if not rows or len({x[0] for x in rows})!=len(rows):
        raise ValueError("Missing or duplicate original upstream generated source signatures")
    return rows

def verify_original_source(upstream):
    original = {}
    for relative,sha in SHA.items():
        p = upstream / relative
        if git_sha(p)!=sha:
            raise ValueError(f"Upstream source Git blob mismatch {relative}")
        original[relative]=p.read_text("utf-8")
    rs=declarations(original[GROUP1_REL],RS_RE)
    gs=declarations(original[ASSEMBLER_REL],GROUP_RE)
    if len(rs)!=124 or len(gs)!=70:
        raise ValueError("Expected exact 124 initial RS batches and 70 original source groups")
    if any(i!=k or length!=52+200*k for k,(i,length,_) in enumerate(rs,1)):
        raise ValueError("Original first group RS interval-count progression changed")
    if any(i!=k for k,(i,_,_) in enumerate(gs,1)):
        raise ValueError("Original group ordering/indexing changed")
    if gs[0][1]!=rs[-1][1] or gs[0][2]!=rs[-1][2]:
        raise ValueError("Original group one does not equal first 52+124 RS prefix")
    if any(gs[k][1]-gs[k-1][1]!=25000 for k in range(1,69)):
        raise ValueError("An intermediate all-RS group is no longer 25000 intervals")
    if gs[-1][1]-gs[-2][1]!=23150:
        raise ValueError("Original terminal RS group no longer exactly 23150")
    if gs[-1][1]!=1748002 or gs[-1][2]!=1000449286:
        raise ValueError("Original full certified store count/Gram endpoint changed")
    return rs,gs

def exact_export_check(rs,gs):
    lean=RS_ONLY.read_text("utf-8")
    seam=SEAM.read_text("utf-8")
    if re.search(r"(?m)^\s*(sorry|axiom)\b",lean+"\n"+seam):
        raise ValueError("Generated source includes new axioms/sorry")
    if lean.count("theorem upToRS")!=124 or lean.count("theorem upToGroup")!=69:
        raise ValueError("Wrong number of source-linked Lean proof stages")
    prev=None
    for i,n,end in rs:
        name=f"upToRS{i:04d}"
        expected=f"theorem {name} : BatchSpec {n-52} 149500 1000 {end} 1000 :="
        if lean.count(expected)!=1:
            raise ValueError(f"Missing/duplicate source-derived RS-only signature {name}")
        witness=(f"  Zeta.Certificates.RiemannSiegel.Batch{i:04d}.batch"
                 if i==1 else
                 f"  BatchSpec.append {prev} "
                 f"Zeta.Certificates.RiemannSiegel.Batch{i:04d}.batch rfl rfl rfl")
        if lean.count(witness)!=1:
            raise ValueError(f"RS-only source theorem {name} has wrong original proof dependency")
        prev=name
    for i,n,end in gs[1:]:
        name=f"upToGroup{i:04d}"
        expected=f"theorem {name} : BatchSpec {n-52} 149500 1000 {end} 1000 :="
        if lean.count(expected)!=1:
            raise ValueError(f"Missing/duplicate source-derived RS group signature {name}")
        witness=(f"  BatchSpec.append {prev} "
                 f"Zeta.Certificates.Groups.Level1.Group{i:04d}.group rfl rfl rfl")
        if lean.count(witness)!=1:
            raise ValueError(f"Group source theorem {name} has wrong original proof dependency")
        if f"import Zeta.Zeros.Certificates.Groups.Level1.Group{i:04d}" not in lean:
            raise ValueError(f"Missing genuine original group import {i}")
        prev=name
    if lean.count("theorem all_original_RS_only : BatchSpec 1747950 149500 1000 1000449286 1000 :=")!=1:
        raise ValueError("Final reconstructed RS-only theorem differs")
    if f"  {prev}" not in lean:
        raise ValueError("Final theorem does not cite terminal original RS-only group")
    for src in [
        "theorem first52Euler :",
        "BatchSpec 52 1000 1000 149500 1000",
        "theorem allRS :",
        "BatchSpec 1747950 149500 1000 1000449286 1000",
        "theorem allOriginalSplit :",
        "BatchSpec 1748002 1000 1000 1000449286 1000",
        "BatchSpec.append first52Euler allRS rfl rfl rfl",
    ]:
        if src not in seam:
            raise ValueError(f"Missing true source 52/RS 149.500 seam in formal target: {src}")
    # Should be checked by the actual external Lean compiler:
    print("CP013 GENERATED SOURCE DEPENDENCY/CUT-SEAM ARITHMETIC PREFLIGHT: PASS")
    print("ONLY an actual Lean 4.35 compile + standard-axiom receipt upgrades the source proof.")


def synthetic_tests():
    """Independent exact counting identity; NOT evidence of any zero's location."""
    assert 124*200==24800
    assert 69-1==68
    assert 24800+68*25000+23150==1747950
    assert 52+1747950==1748002
    assert 149500==149500
    assert 1000449286>149500
    # Negative controls: missing source group or duplicated Euler prefix gives wrong count.
    assert 24800+67*25000+23150 != 1747950
    assert 124*200+69*25000+23150 != 1747950
    print("CP013 EXACT SOURCE RS-ONLY / EULER SEAM COUNT NEGATIVE CONTROLS: PASS")


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--original-root",type=Path)
    p.add_argument("--receipt",type=Path,default=Path("cp013-original-rs-only-source-lineage.json"))
    a=p.parse_args()
    if a.self_test:
        synthetic_tests()
    if a.original_root:
        try:
            rs,gs=verify_original_source(a.original_root)
            exact_export_check(rs,gs)
            receipt={
                "status":"CP013_ORIGINAL_RS_ONLY_SIGNATURES_AND_149500_SEAM_SOURCE_PASS_NOT_KERNEL",
                "original_upstream_commit":UPSTREAM_COMMIT,
                "original_source_blobs":SHA,
                "original_first_euler_count":52,
                "original_RS_only_count":gs[-1][1]-52,
                "original_total":gs[-1][1],
                "original_seam":"149500/1000",
                "original_last_source_right":f"{gs[-1][2]}/1000",
                "first_group_original_RS_batch_count":len(rs),
                "subsequent_original_group_count":len(gs)-1,
                "actual_new_lean_kernel_receipt":None,
                "actual_N_at_seam_count_proof":None,
                "actual_53rd_source_row_binding":None,
            }
            a.receipt.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
            print(receipt["status"])
        except (ValueError,OSError,UnicodeError,AssertionError) as e:
            raise SystemExit(f"{MISSING}: {e}")
    if not a.self_test and not a.original_root:
        p.print_help()

if __name__=="__main__":
    main()
