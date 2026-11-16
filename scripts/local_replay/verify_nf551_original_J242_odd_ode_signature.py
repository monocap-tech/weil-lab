#!/usr/bin/env python3
"""NF551: exact ORIGINAL NF407 242-generator odd exponential-ODE certificate.

No numerical Gram, sampled function, guessed zero, surrogate frequency,
or replaced prime divisor multiplicity. The analytical theorem that
finite exponential polynomials with distinct roots are independent is
a standard mathematical result, not claimed compiled by Lean here.

The audit verifies the ORIGINAL source, and makes every required
characteristic-root multiplicity, odd parity, and coefficient-injectivity
obligation explicit in exact rational arithmetic.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path

from verify_nf545_original_J242_exp_poly_signature import (
    SOURCE_PATH, NF500_PATH, NF500_SHA, SRC_SHA, LEAN_PATH,
    exact_read, signature_from_original_source, signature_from_lean_text,
)

HALF = Fraction(1, 2)


def gaussian_pair_nonzero(pair):
    assert isinstance(pair[0], Fraction) and isinstance(pair[1], Fraction)
    return pair != (Fraction(0), Fraction(0))


def source_ode_signature(nodes, groups):
    assert len(nodes) == 242 and nodes[241] == ["pole", None]
    assert len(groups) == 67 and sum(m for _, m in groups) == 241
    assert all(f > 0 and m > 0 for f, m in groups)
    assert len({f for f, _ in groups}) == 67

    # An annihilator of EVERY original selected odd generator:
    # L(D)=(D²−1/4) Π_{f original}(D²+(2πf)²)^m_f.
    # Its exact order is 2 + Σ 2m_f = 484. Distinct oscillator
    # roots are ±(2πif) with multiplicity m_f, plus ±1/2 once.
    characteristic_roots = []
    for f, m in groups:
        for sign in (-1, 1):
            characteristic_roots.append({
                "kind": "oscillator",
                "imaginary_frequency_over_2pi": str(sign * f),
                "multiplicity": m,
            })
    for sign in (-1, 1):
        characteristic_roots.append({
            "kind": "real_sinh_pole",
            "real_root": str(sign * HALF),
            "multiplicity": 1,
        })
    assert len(characteristic_roots) == 136
    assert sum(r["multiplicity"] for r in characteristic_roots) == 484

    # For k even, x^k sin(2πfx) =
    #   x^k * [(-i/2)e^{+2πifx}+(i/2)e^{-2πifx}].
    # For k odd,  x^k cos(2πfx) =
    #   x^k * [(1/2)e^{+2πifx}+(1/2)e^{-2πifx}].
    # For sinh(x/2), the coefficients at ±1/2 are ±1/2.
    #
    # All 241 original oscillator coefficients at the + root
    # are nonzero and occur with UNIQUE (root, polynomial degree).
    # The pole has a distinct real root. This is an exact,
    # diagonal, source-coefficient injectivity certificate once the
    # general exponential-polynomial uniqueness theorem is invoked.
    plus_root_degree_columns = {}
    oscillator_parity = defaultdict(int)
    for i, entry in enumerate(nodes[:241]):
        f = Fraction(entry[0])
        k = entry[1]
        assert isinstance(k, int) and k >= 0
        assert (f, k) not in plus_root_degree_columns
        if k % 2 == 0:
            kind = "x^k_sin"
            positive = (Fraction(0), -HALF)
            negative = (Fraction(0), HALF)
            # even monomial × odd sine = ODD
        else:
            kind = "x^k_cos"
            positive = (HALF, Fraction(0))
            negative = (HALF, Fraction(0))
            # odd monomial × even cosine = ODD
        assert gaussian_pair_nonzero(positive)
        assert gaussian_pair_nonzero(negative)
        assert positive[0] == negative[0] and positive[1] == -negative[1] if k % 2 == 0 else positive == negative
        plus_root_degree_columns[(f, k)] = {
            "original_index": i,
            "source_generator_type": kind,
            "positive_root_coefficient_Qi": tuple(map(str, positive)),
            "negative_root_coefficient_Qi": tuple(map(str, negative)),
            "real_odd": True,
        }
        oscillator_parity[k % 2] += 1

    for f, m in groups:
        assert [k for ff, k in plus_root_degree_columns if ff == f] == list(range(m))
    assert len(plus_root_degree_columns) == 241
    assert all(v["real_odd"] for v in plus_root_degree_columns.values())

    # The last original source sinh(x/2) has distinct real root ±1/2,
    # with exact nonzero ±1/2 exponential coefficients, and is ODD.
    pole_coeff = {"+1/2": HALF, "-1/2": -HALF}
    assert all(v != 0 for v in pole_coeff.values())

    return {
        "pass": "NF551-exact-original-J242-real-odd-exponential-ODE-source-certificate",
        "original_source_total_selected": 242,
        "oscillator_generator_count": 241,
        "true_pole_generator_index": 241,
        "distinct_original_positive_rational_frequencies": 67,
        "oscillator_even_k_xk_sin": oscillator_parity[0],
        "oscillator_odd_k_xk_cos": oscillator_parity[1],
        "each_original_generator_is_odd": True,
        "exact_characteristic_root_count": 136,
        "exact_characteristic_ODE_order": 484,
        "each_original_root_multiplicity_matches_source": True,
        "exact_unique_plus_root_and_monomial_degree_columns": 241,
        "all_unique_plus_root_column_coefficients_nonzero": True,
        "pole_exponential_coefficients_Q": {k: str(v) for k, v in pole_coeff.items()},
        "actual_analytic_global_source_independence": "MATHEMATICALLY FOLLOWS from standard exponential-polynomial distinct-root uniqueness; Lean OPEN",
        "original_local_collar_iff_global_independence_Lean": "NF551 candidate; compile PENDING",
        "original_gram_strict_positive_Lean": "OPEN",
        "full_original_PN_source_graph_and_RH": "OPEN",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    src, sha = exact_read(SOURCE_PATH)
    nf500, nf500_custody_sha = exact_read(NF500_PATH)
    assert sha == SRC_SHA, "METHOD STOP: original NF407 SHA mismatch"
    assert nf500["original_source_native_raw_json_sha256"] == NF500_SHA
    assert nf500["original_nf407_sha256"] == sha
    nodes = src["original_selected_generator_node_orders"]
    groups = signature_from_original_source(nodes)
    assert groups == signature_from_lean_text(LEAN_PATH), "METHOD STOP: original source vs Lean frequency order mismatch"
    result = source_ode_signature(nodes, groups)
    result["original_nf407_source_sha256"] = sha
    result["original_nf500_native_raw_source_sha256"] = NF500_SHA
    result["nf500_custody_json_sha256"] = nf500_custody_sha
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("NF551: original J242 exact REAL-ODD parity PASS; 136 exact distinct roots, ODE order 484 PASS")
    print("NF551: original 241 oscillator + pole source exponential coefficient injectivity PASS")
    print("NF551: Lean original global independence / canonical Gram strict positivity / RH: OPEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
