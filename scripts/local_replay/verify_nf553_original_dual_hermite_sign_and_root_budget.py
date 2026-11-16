#!/usr/bin/env python3
"""NF553: original NF407 exact 242 odd-jet determinant SIGN and dual Hermite root budget.

This checks the authentic source ordering and source multiplicities. The
sign is derived symbolically for every actual pi>0; no sampled pi,
numerical Gram, or replacement of the genuine sinh pole is used.

This is NOT a substitute for the still-open Lean proof of original
real/complex odd-jet independence and canonical Gram positivity.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
from verify_nf545_original_J242_exp_poly_signature import (
    SOURCE_PATH, NF500_PATH, NF500_SHA, SRC_SHA, LEAN_PATH,
    exact_read, signature_from_original_source, signature_from_lean_text,
)

N = 242


def signed_source_hermite_certificate(nodes, groups):
    assert len(nodes) == N and nodes[-1] == ["pole", None]
    assert len(groups) == 67 and sum(m for _, m in groups) == 241
    assert all(f > 0 and m > 0 for f, m in groups)
    assert all(groups[i][0] < groups[i+1][0] for i in range(len(groups)-1))
    assert [(Fraction(f), k) for f,k in nodes[:241]] == [
        (f,k) for f,m in groups for k in range(m)
    ]

    # A[n,(f,k)] = (-1)^(n+floor(k/2))*(2n+1)_k*(2pi*f)^(2n+1-k).
    # A[n,pole] = 2^(-2n-1).
    # In A's exact original column ordering: 67 increasingly ordered
    # positive t_f=(2pi*f)^2, then the negative genuine pole t_p=-1/4.
    # All oscillator-oscillator Vandermonde factors are positive.
    # Every oscillator-pole difference has negative sign and exponent m_f.
    row_sign_exponent = N*(N-1)//2
    source_even_odd_sign_exponent = sum(
        k//2 for f,m in groups for k in range(m)
    )
    pole_cross_sign_exponent = sum(m for f,m in groups)
    determinant_sign = -1 if (
        row_sign_exponent + source_even_odd_sign_exponent
        + pole_cross_sign_exponent
    ) % 2 else 1
    assert row_sign_exponent == 29161
    assert source_even_odd_sign_exponent == 165
    assert pole_cross_sign_exponent == 241
    assert determinant_sign == -1

    # The monic product H(t)=(t+1/4)*Prod_f (t-4pi²f²)^m_f
    # has degree exactly 242, and all of its 68 real roots are distinct
    # for the actual pi>0. Any degree <=241 p with H|p must be zero.
    return {
      "pass": "NF553-original-J242-dual-Hermite-source-sign-budget",
      "original_frequency_groups_strictly_increasing": True,
      "original_frequency_groups": len(groups),
      "original_oscillator_multiplicity_sum": sum(m for _,m in groups),
      "genuine_sinh_pole_index": 241,
      "real_hermite_nodes_with_pole": len(groups)+1,
      "dual_polynomial_maximum_degree": 241,
      "monic_divisor_degree": sum(m for _,m in groups)+1,
      "exact_row_sign_exponent": row_sign_exponent,
      "exact_original_source_parity_sign_exponent": source_even_odd_sign_exponent,
      "exact_negative_pole_cross_exponent": pole_cross_sign_exponent,
      "symbolic_actual_pi_positive_determinant_sign": determinant_sign,
      "dual_injectivity_paper_proof": (
        "A^T a=0 => H(t)|p(t), deg p<=241, deg H=242 => a=0; "
        "actual original source derivative bridge / root multiplicity Lean OPEN"
      ),
      "original_complex_global_independence_Lean": "OPEN",
      "canonical_original_Gram_strict_positive_Lean": "OPEN",
      "full_source_graph_signed_Weil_and_RH": "OPEN"
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output",type=Path)
    args=ap.parse_args()
    source, sha = exact_read(SOURCE_PATH)
    nf500,nf500sha=exact_read(NF500_PATH)
    assert sha == SRC_SHA, "METHOD STOP: source SHA changed"
    assert nf500["original_source_native_raw_json_sha256"] == NF500_SHA
    assert nf500["original_nf407_sha256"] == sha
    nodes=source["original_selected_generator_node_orders"]
    groups=signature_from_original_source(nodes)
    assert groups == signature_from_lean_text(LEAN_PATH)
    result=signed_source_hermite_certificate(nodes,groups)
    result["original_nf407_source_sha256"] = sha
    result["original_nf500_native_raw_source_sha256"] = NF500_SHA
    result["nf500_custody_json_sha256"] = nf500sha
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("NF553: original 67 oscillator+true pole real Hermite source order PASS")
    print("NF553: exact original 242 odd-jet determinant SIGN = -1 for pi>0 PASS")
    print("NF553: root-multiplicity/source bridge and global independence in Lean OPEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
