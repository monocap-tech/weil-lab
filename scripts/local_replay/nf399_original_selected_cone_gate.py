#!/usr/bin/env python3
"""NF399: exact source-pinned necessary cone/norm gate for original J242.

No new signed kernel evaluation. This checks a selected-space METHOD obstruction
under the inherited original strong Fourier/operator-domain realization.
"""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

NATIVE = "notes/data/provisional/NF398_original_j387_selected_signed_native.json"
DECISION = "notes/data/provisional/NF398_original_j387_exact_candidate_decision.json"
RECEIPT = "notes/data/provisional/NF398_native_execution_status.json"
SOURCE_ZIP_SHA256 = "f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0"
LOWER = Fraction(3153944, 10000000)  # 0.3153944, strict


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def interval(v):
    assert isinstance(v, list) and len(v) == 2
    lo, hi = map(Fraction, v)
    assert lo <= hi
    return lo, hi


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--native", default=NATIVE)
    p.add_argument("--decision", default=DECISION)
    p.add_argument("--receipt", default=RECEIPT)
    p.add_argument("--output", default=None)
    a = p.parse_args()
    n, sha = load(a.native)
    d, _ = load(a.decision)
    r, _ = load(a.receipt)

    assert r["pass"] == "NF398"
    assert r["native_job_result"] == "success"
    assert r["original_native_signed_selected_accepted"] is True
    assert r["j387_method_verdict"] == "STOP"
    assert r["native_sha256"] == sha
    assert d["original_native_report_sha256"] == sha
    assert d["original_archive_sha256"] == SOURCE_ZIP_SHA256
    assert n["original_signed_archive_zip_sha256"] == SOURCE_ZIP_SHA256
    assert n["original_selected_frame_sha_pass"] is True
    assert n["original_householder_two_vector_isometry_check_pass"] is True
    assert n["original_archived_householder_count"] == 4
    assert n["pole_restored_for_selected_test"] is True
    assert n["original_pole_overlap_source_projection_identity_verified"] is True
    assert d["physical_pole_independent_overlap_intersection_pass"] is True
    assert d["full_odd_pole_restoration_interval_intersection_pass"] is True
    assert d["original_moment_discrepancy_interval_identity_pass"] is True
    assert d["recomputed_nf391_nf392_source_native_exact_verdict"] == "STOP"
    assert d["actual_fixed_j387_stop_certified"] is True
    assert r["W_ODD_NEG"] == d["W_ODD_NEG"] == n["W_ODD_NEG"] == "OPEN"
    assert r["RH"] == d["RH"] == n["RH"] == "OPEN"

    A_lo, A_hi = interval(n["original_multiplier_m_u4_j387_interval"])
    h2_lo, h2_hi = interval(n["original_j387_physical_norm_squared_interval"])
    assert A_lo <= A_hi < 0
    assert 0 < h2_lo <= h2_hi
    abs_A_lower = -A_hi
    H = Fraction(n["original_NF375_fourth_highband_action_norm_upper"])
    tau = Fraction(n["original_NF375_fourth_lowband_future_target"])
    assert H > 0 and tau == Fraction(7, 25000000000000)

    # For original t_L, h=j387 and original A=<m(D)u4,h>, highband e:
    # |<t_L,h>-A| <= H ||h||.
    #
    # If <j,h> >= 0, then <t_L-j,h> <= A_hi+H||h|| < 0,
    # hence ||t_L-j|| >= |A|/||h||-H > LOWER.
    cone_strict = abs_A_lower**2 > (LOWER + H)**2 * h2_hi
    assert cone_strict

    # If ||t_L-j||<=tau, then
    # |A| <= (||j||+H+tau)||h||. Therefore ||j||>LOWER.
    universal_norm_strict = abs_A_lower**2 > (LOWER + H + tau)**2 * h2_hi
    assert universal_norm_strict

    # The same close-approximation assumption forces <j,h><0.
    negative_projection_required = abs_A_lower**2 > (H + tau)**2 * h2_hi
    assert negative_projection_required

    report = {
        "pass": "NF399",
        "source_native_sha256": sha,
        "source_original_signed_archive_zip_sha256": SOURCE_ZIP_SHA256,
        "original_selected_dimension": 242,
        "original_source_probe": "frozen NF387 j387, no new signed cells",
        "cutoff": str(n["original_NF375_fourth_cutoff"]),
        "candidate_norm_strict_lower": str(LOWER),
        "exact_cone_lower_squared_pass": cone_strict,
        "exact_universal_norm_squared_pass": universal_norm_strict,
        "exact_negative_projection_required_pass": negative_projection_required,
        "excluded_candidates": "ALL j in J242 with <j,j387> >= 0; residual > 0.3153944",
        "necessary_for_lowband_error_le_tau": "||j|| > 0.3153944 AND <j,j387> < 0",
        "full_lowband_upper_established": False,
        "all_J242_candidates_excluded": False,
        "operator_domain_independently_audited": False,
        "W_ODD_NEG": "OPEN",
        "RH": "OPEN",
    }
    payload = json.dumps(report, indent=2) + "\n"
    if a.output:
        Path(a.output).parent.mkdir(parents=True, exist_ok=True)
        Path(a.output).write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
