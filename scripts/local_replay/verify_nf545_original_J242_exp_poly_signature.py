#!/usr/bin/env python3
"""NF545 exact ORIGINAL NF407 J242 exponential-polynomial independence signature audit.

Not a numerical Gram surrogate. This checks the authentic selected generator
nodes against the source-pinned Lean table and exact characteristic-root
separation conditions. The general uniqueness/analyticity/Gram argument is
given in NF545 note and is not asserted Lean-certified by this Python audit.
"""
from __future__ import annotations

import argparse
from collections import OrderedDict
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re

SRC_SHA = "0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
NF500_SHA = "7e261d540c8b658bced4b44d1bf998c23ef7f975fc07daa0f30ae6438dcffb05"
SOURCE_PATH = Path("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
NF500_PATH = Path("notes/data/provisional/NF500_original_all_242_selected_smooth_log_moment_native_custody.json")
NF404_PATH = Path("notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
LEAN_PATH = Path("WeilDefect/Arithmetic/ActualZetaOriginalJ242ExponentialSignature.lean")


def exact_read(path):
    raw = path.read_bytes()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


def signature_from_original_source(nodes):
    assert len(nodes) == 242, "Not original 242 nodes"
    assert nodes[-1] == ["pole", None], "Original sinh pole must be node 241"
    groups: OrderedDict[Fraction, list[int]] = OrderedDict()
    for i, entry in enumerate(nodes[:-1]):
        assert len(entry) == 2
        f, k = entry
        f = Fraction(f)
        assert 0 < f and f.denominator <= 128, ("original rational frequency", i, f)
        assert isinstance(k, int) and k >= 0, ("original order", i, k)
        groups.setdefault(f, []).append(k)
    assert len(groups) == 67, "Mismatched original distinct-frequency count"
    assert sum(map(len, groups.values())) == 241
    for f, orders in groups.items():
        assert orders == list(range(len(orders))), ("noncontiguous source order", f, orders)
    # Original selected j_{f,k}: k even = x^k sin(2π f x);
    # k odd = x^k cos(2π f x); pole = sinh(x/2).
    # Each f contributes ±i2πf; the pole contributes ±1/2.
    # The following symbolic labels are algebraically distinct because
    # π>0, all f>0, and all original rationals f are distinct.
    roots = {("oscillator", sign, f) for f in groups for sign in (-1, 1)}
    roots |= {("pole", -1, Fraction(1, 2)), ("pole", 1, Fraction(1, 2))}
    assert len(roots) == 2 * len(groups) + 2 == 136
    return [(f, len(orders)) for f, orders in groups.items()]


def signature_from_lean_text(path):
    text = path.read_text()
    anchor = "def nf545OriginalSelectedFrequencyGroups : List (ℚ × ℕ) := ["
    assert text.count(anchor) == 1, "Expected one source-pinned Lean frequency table"
    body = text.split(anchor, 1)[1].split("]", 1)[0]
    entries = re.findall(r"\(\(\s*([^()]+?)\s*:\s*ℚ\s*\),\s*(\d+)\s*\)", body)
    assert len(entries) == 67, ("Malformed Lean frequency table", len(entries))
    return [(Fraction(f.strip()), int(k)) for f, k in entries]


def source_geometry_and_graph_tail_checks():
    B = Fraction(11, 10)
    delta = Fraction(1, 500)
    center = B - delta / 2
    radius = delta / 4
    # Positive smooth-correction bump lives strictly inside the ORIGINAL E.
    assert B - delta < center - radius < center + radius < B
    # Its reflection lies strictly inside the negative collar.
    assert -B < -center - radius < -center + radius < -B + delta
    assert center == Fraction(1099, 1000)
    assert radius == Fraction(1, 2000)
    # Exact dyadic divisor-square tail formula:
    # sum_{n>=N} (n+2)/8^n = (56*N+120)/(49*8^N).
    def tail(n):
        return Fraction(56*n+120, 49*8**n)
    for n in range(120):
        assert tail(n) - tail(n+1) == Fraction(n+2, 8**n)
        assert tail(n) > 0
    return {"original_B": str(B), "original_delta": str(delta),
            "chi_bump_center": str(center), "chi_bump_radius": str(radius),
            "dyadic_squared_sample_tail_formula": "(56*N+120)/(49*8^N)",
            "dyadic_tail_recurrence_exact_N0_119": True}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    source, source_sha = exact_read(SOURCE_PATH)
    nf500, nf500_sha = exact_read(NF500_PATH)
    nf404, _ = exact_read(NF404_PATH)
    assert source_sha == SRC_SHA, "METHOD STOP: NF407 original source SHA mismatch"
    assert nf500["original_source_native_raw_json_sha256"] == NF500_SHA, (
        "METHOD STOP: NF500 original SOURCE-NATIVE RAW output digest mismatch"
    )
    assert nf500["pass"] == "NF500"
    assert nf500["original_nf407_sha256"] == source_sha
    assert nf500["original_source_generators_selected"] == 242
    assert nf404["pass"] == "NF404" and nf404["original_selected_pole_index"] == 241
    nodes = source["original_selected_generator_node_orders"]
    sig = signature_from_original_source(nodes)
    assert sig == signature_from_lean_text(LEAN_PATH), (
        "METHOD STOP: Lean signature does not reproduce exact original NF407 node order"
    )
    assert sig[0] == (Fraction(37,64), 14)
    assert sig[-1] == (Fraction(113013,128), 2)
    # Real positive and negative complex characteristic roots never coincide
    # with real pole roots ±1/2, since π>0.
    assert all(f > 0 for f, _ in sig)
    assert len({f for f, _ in sig}) == 67
    geometry = source_geometry_and_graph_tail_checks()
    result = {
       "pass": "NF545-exact-original-J242-characteristic-root-source-signature",
       "original_nf407_source_sha256": source_sha,
       "nf500_custody_json_sha256": nf500_sha,
       "original_nf500_native_raw_source_sha256": NF500_SHA,
       "selected_original_oscillator_frequency_groups": len(sig),
       "selected_original_oscillator_monomial_directions": sum(m for _,m in sig),
       "selected_original_sinh_pole_index": 241,
       "original_total_selected_directions": 242,
       "distinct_exponential_characteristic_root_labels": 136,
       "all_original_frequency_rationals_positive": True,
       "all_monomial_orders_contiguous_from_zero": True,
       "all_source_frequency_groups_match_Lean_table_exactly": True,
       "original_analytic_independence_mathematical_argument": "exponential-polynomial differential-operator annihilators, see NF545 note",
       "actual_selected_moment_functions_in_Lean": "OPEN",
       "actual_source_weighted_Gram_strict_positive_in_Lean": "OPEN",
       "original_actual_two_source_graph_Lean_admission": "OPEN",
       "NF527_full_weil_coercivity_Lean": "OPEN",
       "RH": "OPEN",
       **geometry,
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("NF545: ORIGINAL NF407 J242 signature, 67 distinct positive rationals,",
          "241 oscillator modes + true sinh pole, exact Lean-table identity PASS")
    print("NF545 source-specific weighted Gram nondegeneracy analytically implied by",
          "exponential-polynomial uniqueness; Lean theorem NOT YET compiled.")
    print("NF545 original all-divisor graph/source and global RH: OPEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
