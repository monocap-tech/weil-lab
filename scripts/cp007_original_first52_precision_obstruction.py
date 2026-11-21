#!/usr/bin/env python3
"""CP007: SOURCE-DATA-BACKED zero-interval precision obstruction, exact arithmetic.

The 52 published Euler–Maclaurin zero store rows are preserved BYTE-FOR-BYTE
from smmercuri/zeta commit c06b4e13d9c847e50a32c3d738271cbad62ae9f3,
Git blob SHA-1 6958515f7dd1be86ebe823ff6fd67ec110ec90f7.
This tests the adequacy of CP006's CURRENT conservative error BOUND,
not actual spectral incompatibility and not the Lean theorem's validity.
"""
from __future__ import annotations
import argparse
import hashlib
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

from cp005_formal_zero_roster_adapter import E_tail, E_QUAD_ALLOWANCE, EPS_MAX, RADII
from cp006_dyadic_zero_bracket_budget import (
    localization, dyadic_band, uniform_localization,
)

SOURCE_COMMIT = "c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
SOURCE_BLOB = "6958515f7dd1be86ebe823ff6fd67ec110ec90f7"
SOURCE_ROWS = Path(__file__).resolve().parents[1] / "data/cp007_original_euler_maclaurin_first52.txt"
N_EULER = 52
N_RIEMANN_SIEGEL = 1_747_950
N_TOTAL = 1_748_002


def gitblob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def parse_original52(path=SOURCE_ROWS):
    raw=path.read_bytes()
    assert gitblob(raw)==SOURCE_BLOB, "Original euler_maclaurin first-52 source blob does not match"
    lines=raw.decode("ascii").splitlines()
    assert len(lines)==N_EULER, "Wrong original Euler–Maclaurin batch count"
    out=[]
    prior=None
    for i,line in enumerate(lines,1):
        fields=[s.strip() for s in line.split(",")]
        assert len(fields)==7, f"Original 7-column record missing at row {i}"
        assert int(fields[0])==i, f"Source local zero index out of order at row {i}"
        lo,hi=F(fields[1]),F(fields[2])
        assert 0<lo<hi
        if prior is not None:
            assert lo==prior, f"Original published widened brackets must tile, row {i}"
        # The four method-specific precision/cutoff fields are integral.
        assert all(int(s)>0 for s in fields[3:])
        out.append((lo,hi))
        prior=hi
    assert out[0]==(F(1),F(17846,1000))
    assert out[-1][1]==F(149500,1000)
    assert N_EULER+N_RIEMANN_SIEGEL==N_TOTAL
    return out


def bin_sums(brackets):
    result=defaultdict(lambda:F(0))
    for lo,hi in brackets:
        result[dyadic_band(lo)]+=(hi-lo)/2
    return dict(result)


def assess(brackets):
    # Every band contribution is nonnegative; the first-row bound is a
    # RIGOROUS LOWER BOUND ON THE COMPUTED CP006 BUDGET for all roots.
    b_first=bin_sums(brackets[:1])
    b_all=bin_sums(brackets)
    stats={}
    for r in RADII:
        lower_single=localization(r,b_first)
        lower_fiftytwo=localization(r,b_all)
        assert lower_single>EPS_MAX
        assert lower_fiftytwo>=lower_single
        # Additional rigorous allowable halfwidth for FIRST bracket in isolation:
        # all other localization contributions set to zero (optimistically).
        per_half=localization(r,{0:F(1)})
        residual=EPS_MAX-E_tail(r)-E_QUAD_ALLOWANCE
        assert residual>0
        maximal_first_halfwidth=residual/per_half
        assert maximal_first_halfwidth<F(1,100)
        stats[str(r)]={
            "first_bracket_localization":lower_single,
            "first_52_localization":lower_fiftytwo,
            "first_bracket_halfwidth":F(8423,1000),
            "max_first_halfwidth_if_all_other_rows_exact_and_quad_budget_proved":maximal_first_halfwidth,
            "absolute_total_budget":EPS_MAX,
            "first_bracket_exceeds_total_target":lower_single>EPS_MAX,
        }
    return stats


def self_test():
    a=parse_original52()
    stats=assess(a)
    assert dyadic_band(F(1))==0
    assert len(bin_sums(a))>1
    # Negative control: point-like synthetic precision greatly reduces its
    # first-row contribution. It is NOT a certified zero bracket!
    fake=[(F(14),F(14)+F(1,10**9))]
    for r in RADII:
        assert localization(r,bin_sums(fake))<EPS_MAX
    print(f"CP007 SOURCE SNAPSHOT: exact Git blob {SOURCE_BLOB}; {len(a)} authentic widened source brackets")
    print(f"Original first bracket: [{a[0][0]}, {a[0][1]}], half-width={F(8423,1000)}")
    for r,s in stats.items():
        print(f"r={r}: first-row CP006 budget bound {float(s['first_bracket_localization']):.9f}; "
              f"first-52 bound {float(s['first_52_localization']):.9f}; "
              f"absolute maximum allowed 0.002")
        print(f"  optimistic first-row half-width ceiling < "
              f"{float(s['max_first_halfwidth_if_all_other_rows_exact_and_quad_budget_proved']):.9f}")
    print("CP007 ORIGINAL STORE PRECISION OBSTRUCTION: EXACT FRACTION PASS")
    print("This falsifies use of the raw widened store with the CURRENT conservative "
          "CP006 error certificate, NOT CP-C1 or RH.")
    print("Real upstream kernel receipt and per-row proof-to-store lineage still OPEN.")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--source-store",type=Path,default=SOURCE_ROWS)
    args=p.parse_args()
    if args.source_store!=SOURCE_ROWS:
        a=parse_original52(args.source_store)
        assess(a)
        print("EXTERNAL_FIRST52_SOURCE_STORE_BUDGET_EXCEEDED; no Lean pass")
    else:
        self_test()
