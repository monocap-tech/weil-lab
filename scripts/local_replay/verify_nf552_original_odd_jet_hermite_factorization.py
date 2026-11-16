#!/usr/bin/env python3
"""NF552: full ORIGINAL 242 x 242 odd-jet audit by a 68-node Hermite reduction.

No floating-point Gram, numerical evaluation of pi, guessed source order,
or substitute pole. The exact source is SHA-pinned by NF545/NF551.

For the oscillator omega=2*pi*f:
  (d/dx)^(2n+1) j_(f,k)(0)
    = (-1)^(n+floor(k/2)) (2n+1)_k omega^(2n+1-k).
For the genuine sinh(x/2) pole the odd derivative is 2^(-2n-1).

A row-sign change (-1)^n and the change t=omega^2 turn this matrix
into a block-triangular column change of a 68-node confluent Vandermonde:
67 distinct t_f=4*pi^2*f^2 > 0 of multiplicity m_f, plus the pole
t_p=-1/4 of multiplicity 1. The determinant product is stated in the
accompanying note; the generic confluent-Vandermonde identity and
source-specific derivative bridge are STILL TO BE COMPILED IN LEAN.

A full 242 x 242 modular determinant at the exact specialization pi=1
is compared against the predicted algebraic product. This is a stringent
independent audit of the genuine source order and parity, NOT an
inference from specializing pi=1 to the transcendental actual pi.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from math import factorial
import json
from pathlib import Path

from verify_nf545_original_J242_exp_poly_signature import (
    SOURCE_PATH, NF500_PATH, NF500_SHA, SRC_SHA, LEAN_PATH,
    exact_read, signature_from_original_source, signature_from_lean_text,
)

# Large known Mersenne prime. Fractions are reduced mod p with inverses.
P = 2**61 - 1
N = 242


def residue(q: Fraction) -> int:
    assert q.denominator % P, "denominator divisible by audit prime"
    return (q.numerator % P) * pow(q.denominator, -1, P) % P


def determinant_mod_p(matrix: list[list[int]]) -> int:
    n = len(matrix)
    assert n == N and all(len(row) == n for row in matrix)
    a = [row[:] for row in matrix]
    det = 1
    for k in range(n):
        pivot_row = next((i for i in range(k, n) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            det = -det % P
        pivot = a[k][k]
        det = (det * pivot) % P
        inv = pow(pivot, -1, P)
        row_k = a[k]
        for i in range(k + 1, n):
            row_i = a[i]
            entry = row_i[k]
            if entry == 0:
                continue
            multiplier = entry * inv % P
            row_i[k] = 0
            for j in range(k + 1, n):
                row_i[j] = (row_i[j] - multiplier * row_k[j]) % P
    return det


def full_original_odd_jet_modular(nodes, groups):
    assert len(nodes) == N
    assert nodes[N - 1] == ["pole", None]
    assert len(groups) == 67 and sum(m for _, m in groups) == 241
    assert len({f for f, _ in groups}) == 67
    assert all(f > 0 and m > 0 for f, m in groups)
    expected = [(f, k) for f, m in groups for k in range(m)]
    assert [(Fraction(f), k) for f, k in nodes[:-1]] == expected

    # Specialization pi=1 is a modular TEST only; not the original pi.
    omegas = {f: residue(2 * f) for f, _ in groups}
    p_half = residue(Fraction(1, 2))
    fact = [1] * (2 * N)
    for k in range(1, 2 * N):
        fact[k] = fact[k - 1] * k % P
    invfact = [1] * (2 * N)
    invfact[-1] = pow(fact[-1], -1, P)
    for k in range(2 * N - 1, 0, -1):
        invfact[k - 1] = invfact[k] * k % P

    matrix = []
    for n in range(N):
        odd_order = 2 * n + 1
        row = []
        for f, k in expected:
            if k > odd_order:
                row.append(0)
            else:
                falling = fact[odd_order] * invfact[odd_order - k] % P
                value = falling * pow(omegas[f], odd_order - k, P) % P
                row.append((-value if (n + k // 2) % 2 else value) % P)
        row.append(pow(p_half, odd_order, P))  # actual sinh(x/2)
        matrix.append(row)
    return matrix, omegas


def predicted_confluent_product(groups, omegas):
    # Actual formula, with omega_f=2*pi*f and t_f=omega_f^2,
    # is valid for any nonzero omega_f and distinct square nodes.
    # We evaluate it modulo P at pi=1 only to audit the 242 rows.
    total = N
    det = P - 1 if (total * (total - 1) // 2) % 2 else 1
    det = det * residue(Fraction(1, 2)) % P  # pole column
    for f, m in groups:
        w = omegas[f]
        assert w != 0
        for k in range(m):
            diag = w * pow(2 * w % P, k, P) % P
            if (k // 2) % 2:
                diag = -diag % P
            det = det * diag % P
    nodes = [(omegas[f] ** 2 % P, m) for f, m in groups]
    nodes.append((residue(Fraction(-1, 4)), 1))
    assert len({node for node, _ in nodes}) == 68
    for _, m in nodes:
        for k in range(m):
            det = det * (factorial(k) % P) % P
    for a, (t_a, m_a) in enumerate(nodes):
        for t_b, m_b in nodes[a + 1:]:
            det = det * pow((t_b - t_a) % P, m_a * m_b, P) % P
    assert det != 0
    return det


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    source, src_sha = exact_read(SOURCE_PATH)
    nf500, nf500_sha = exact_read(NF500_PATH)
    assert src_sha == SRC_SHA, "METHOD STOP: original NF407 SHA mismatch"
    assert nf500["original_source_native_raw_json_sha256"] == NF500_SHA
    assert nf500["original_nf407_sha256"] == src_sha

    nodes = source["original_selected_generator_node_orders"]
    groups = signature_from_original_source(nodes)
    assert groups == signature_from_lean_text(LEAN_PATH), (
        "METHOD STOP: original frequency/order signature differs from Lean"
    )
    matrix, omegas = full_original_odd_jet_modular(nodes, groups)
    computed = determinant_mod_p(matrix)
    predicted = predicted_confluent_product(groups, omegas)
    assert computed != 0, "METHOD STOP: full odd-jet matrix lost modular rank"
    assert computed == predicted, (
        "METHOD STOP: original full odd-jet det differs from Hermite factorization"
    )
    result = {
        "pass": "NF552-exact-original-odd-jet-68-node-confluent-structural-audit",
        "original_nf407_sha256": src_sha,
        "original_nf500_native_raw_source_sha256": NF500_SHA,
        "nf500_custody_json_sha256": nf500_sha,
        "original_oscillators": 241,
        "true_sinh_pole_index": 241,
        "full_original_odd_jet_matrix": [N, N],
        "odd_derivative_orders": "1,3,...,483",
        "distinct_positive_frequency_nodes": 67,
        "distinct_squared_frequency_and_pole_nodes": 68,
        "total_hermite_multiplicity": 242,
        "audit_prime": P,
        "modular_specialization": "pi=1, solely a modular algebraic cross-check",
        "full_specialized_matrix_det_mod_prime": computed,
        "hermite_product_det_mod_prime": predicted,
        "original_pi_det_nonzero": (
            "MATHEMATICAL FACTOR PROOF ON PAPER; source-specific Lean bridge OPEN"
        ),
        "global_source_independence_Lean": "OPEN",
        "canonical_original_Gram_strict_positive_Lean": "OPEN",
        "source_graph_signed_Weil_and_RH": "OPEN",
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("NF552 PASS: SHA-pinned exact original 242x242 odd-jet modular rank")
    print("NF552 PASS: full modular determinant equals 68-node Hermite product")
    print("NF552: actual-pi determinant bridge, unconditional Lean Gram, RH OPEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
