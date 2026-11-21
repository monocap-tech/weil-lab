#!/usr/bin/env python3
"""CP011 source-pinned ORIGINAL RS slot 53 -> refined candidates custody.

This script verifies genuine 7.34MB original RS store Git blob if supplied
and proves only exact-rational source containment (not Hardy Z signs).
Separate Lean source-to-original-roster proof requires actual external
v4.35 kernel/axiom receipts; no source string or raw Git SHA substitutes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

from cp007_original_first52_precision_obstruction import parse_original52
from cp010_dual_method_root53_pilot import (
    SOURCE_TAG, SOURCE_RS_SHA, COARSE, NARROW, RS, EULER,
    strict_candidates
)

HERE=Path(__file__).resolve().parent
PIN=HERE/"cp007_upstream_store_source_manifest.json"
OUT_DEFAULT=Path("cp011-root53-source-identity-receipt.json")
GLOBAL_ZERO_INDEX=53
EULER_COUNT=52
RS_LOCAL_INDEX=1
SOURCE_RS_BATCH_SHA="12848f56d0b62df858dcb89b708a858f4f7b28fb"
SOURCE_RS_BATCH_DECLARATION="theorem batch : BatchSpec 200 149500 1000 474603 1000 := by build_batch_rs 0 200"


def gitblob_sha(path):
    size=path.stat().st_size
    sha=hashlib.sha1(b"blob "+str(size).encode()+b"\0")
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            sha.update(block)
    return sha.hexdigest()


def finite_count_abstract_model():
    # Mathematical negative controls clarify why mere sign changes do not
    # establish a slot identity without the full multiplicity count.
    intervals=((F(0),F(2)),(F(2),F(4)),(F(4),F(6)))
    assigned_roots=(F(1),F(3),F(5))
    def containing_slot(t):
        return [k for k,(a,b) in enumerate(intervals) if a<t<b]
    assert [containing_slot(x) for x in assigned_roots]==[[0],[1],[2]]
    assert len(assigned_roots)==len(intervals)==3
    assert containing_slot(F(1))==[0] # refined point in the same slot
    # Extra positive zero => violates N(g)=3, not a slot uniqueness proof.
    assert len(assigned_roots+(F(3,2),))>len(intervals)
    # Multiplicity 2 at a known zero also exceeds the original count.
    assert len(assigned_roots+(F(3),))>len(intervals)
    # Endpoint witness cannot count as inside either open slot.
    assert containing_slot(F(2))==[]
    # Without strict non-overlap, two original slots may share a root.
    overlapping=((F(0),F(3)),(F(2),F(4)))
    assert sum(a<F(5,2)<b for a,b in overlapping)==2
    print("CP011 finite abstract-count/source-slot uniqueness necessary-hypotheses tests: PASS")
    print("Synthetic model is NOT a Lean proof or a new zeta zero result.")


def read_original_rs_first(original_shard):
    if gitblob_sha(original_shard)!=SOURCE_RS_SHA:
        raise ValueError("Original 7.34MB first RS shard's immutable source Git SHA does not match")
    with original_shard.open("r",encoding="ascii") as f:
        line=f.readline().strip()
    f=[x.strip() for x in line.split(",")]
    if len(f)!=3 or f[0]!="1":
        raise ValueError("RS original local row must start at root index 1")
    a,b=F(f[1]),F(f[2])
    if not (a==F(299,2) and a<b):
        raise ValueError("Original RS first row must start exactly after genuine 52 Euler rows at 149.5")
    return a,b


def real_slot_source_custody(original_shard,original_batch,report):
    if gitblob_sha(original_batch)!=SOURCE_RS_BATCH_SHA:
        raise ValueError("Original RS first 200-root kernel batch source Git SHA mismatch")
    if SOURCE_RS_BATCH_DECLARATION not in original_batch.read_text("utf-8"):
        raise ValueError("Actual first RS batch Lean source theorem not found")
    assert strict_candidates(), "CP010 genuine candidate stores do not match"
    pin=json.loads(PIN.read_text(encoding="utf-8"))
    assert pin["pinned_commit"]==SOURCE_TAG
    assert pin["euler_maclaurin"]["rows"]==EULER_COUNT
    assert pin["riemann_siegel"]["rows"]==1_747_950
    assert pin["riemann_siegel"]["files"][0][1]==SOURCE_RS_SHA
    assert len(parse_original52())==EULER_COUNT
    original=read_original_rs_first(original_shard)
    if not (original[0] < COARSE[0] < NARROW[0] < NARROW[1] < COARSE[1] < original[1]):
        raise ValueError("ORIGINAL first RS row does not strictly enclose BOTH proposed candidates")
    if not (COARSE[0]<NARROW[0]<NARROW[1]<COARSE[1]):
        raise ValueError("Candidate Euler and RS brackets not nested")
    payload={
        "status":"EXACT_SOURCE_SLOT_CONTAINMENT_ONLY_NOT_LEAN",
        "original_upstream":SOURCE_TAG,
        "original_first_rs_shard_git_blob":SOURCE_RS_SHA,
        "original_original_first200_RS_lean_git_blob":SOURCE_RS_BATCH_SHA,
        "global_positive_zero_index":GLOBAL_ZERO_INDEX,
        "rs_local_row_index":RS_LOCAL_INDEX,
        "euler_preceding_rows":EULER_COUNT,
        "original_first_rs_interval":[str(original[0]),str(original[1])],
        "proposed_coarse_rs_interval":[str(x) for x in COARSE],
        "proposed_narrow_euler_interval":[str(x) for x in NARROW],
        "trust":"Source SHA and rational nesting only; neither refined candidate has an accepted original Lean Hardy Z kernel certificate",
        "remaining_gate":"Actual upstream Zeta v4.35 compiled CP011 canonical-roster theorem and original source row + actual CP010 root-existence receipts",
    }
    report.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print("CP011 ORIGINAL FIRST RS SOURCE INTERVAL FOUND:",str(original))
    print("CP011 EXACT SOURCE SLOT CONTAINMENT PASS — NOT A NEW LEAN OR SPECTRAL CERTIFICATE")


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--original-rs-shard",type=Path)
    p.add_argument("--original-rs-batch",type=Path)
    p.add_argument("--receipt",type=Path,default=OUT_DEFAULT)
    args=p.parse_args()
    if args.self_test:
        finite_count_abstract_model()
    if bool(args.original_rs_shard)!=bool(args.original_rs_batch):
        raise SystemExit("NOT_READY: original first RS SHA-verified source shard AND compiled-source batch required together")
    if args.original_rs_shard:
        try:
            real_slot_source_custody(args.original_rs_shard,args.original_rs_batch,args.receipt)
        except (OSError,ValueError,AssertionError,IndexError,KeyError) as e:
            raise SystemExit("NOT_READY: "+str(e))
    if not args.self_test and args.original_rs_shard is None:
        p.print_help()


if __name__=="__main__":
    main()
