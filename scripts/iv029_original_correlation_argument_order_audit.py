#!/usr/bin/env python3
"""IV029: exact ORIGINAL signed correlation argument-order dictionary.

Source authority: ActualZetaCorrelationTransform.lean defines
 neutralWindowCorrelation a first second tau
   = integral second(x) * conj(first(x-tau)) dx.

The independent IV024/IV027 directed graph uses its 'from' cell as
UNSHIFTED at x and its 'to' cell as SHIFTED at x-tau. Therefore the
graph arrow is SOURCE SECOND ARGUMENT -> SOURCE FIRST ARGUMENT.
It is NOT the order of the original Lean function's two arguments.

Rigorously check all 4*4*7*2=224 directed source samples against
the exact-rational active-prime overlap classifier and the signed
adjoint reversal. An independent exact-complex finite step-function
surrogate checks first-slot antilinearity, second-slot linearity,
conjugation and shift reversal, and the reality of diagonal +/- terms.
Step functions are NOT Schwartz. These tests are NONKERNEL and cannot
prove a theorem about the original signed Weil form, a spectral
representation, global Weil positivity, or RH.
"""
import argparse
import json
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path

from iv024_original_prime_interaction_graph import (
    CELLS, active, classify, rigorous_log,
)

OUT = Path("iv029-original-correlation-argument-conjugation-dictionary-NONKERNEL.json")


@dataclass(frozen=True)
class ComplexQ:
    re: Q
    im: Q

    def __add__(self, other):
        return ComplexQ(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexQ(self.re * other.re - self.im * other.im,
                        self.re * other.im + self.im * other.re)

    def conj(self):
        return ComplexQ(self.re, -self.im)

    def real_scale(self, r):
        return ComplexQ(self.re * r, self.im * r)

    def is_real(self):
        return self.im == 0


ZERO = ComplexQ(Q(0), Q(0))
ONE = ComplexQ(Q(1), Q(0))


def source_sample(first, second, n, sign):
    """Lean first/second is OPPOSITE the arrow from/to in IV024."""
    return classify(second, first, n, sign)[0]


def intersect_len(left1, right1, left2, right2):
    return max(Q(0), min(right1, right2) - max(left1, left2))


def exact_overlap(first_index, second_index, tau):
    first = CELLS[first_index]
    second = CELLS[second_index]
    # Source integrand second(x)*conj(first(x-tau)).
    return intersect_len(second.left, second.right,
                         first.left + tau, first.right + tau)


def correlation(first, second, tau):
    """Exact integral of a FINITE STEP surrogate, NOT a Schwartz test.

    Each source input is a map (cell index -> rational complex value).
    In the authentic functional it is second(x)*conj(first(x-tau)).
    """
    acc = ZERO
    for i, u in first.items():
        for j, v in second.items():
            acc = acc + (v * u.conj()).real_scale(exact_overlap(i, j, tau))
    return acc


def scale_wave(f, z):
    return {i: z * v for i, v in f.items()}


def preflight():
    assert active() == (2, 3, 4, 5, 7, 8, 9)
    expected = {
        ("old_left", "old_right", 9, 1),
        ("old_right", "old_left", 9, -1),
    }
    source_edges = set()
    tests = 0
    for first in CELLS:
        for second in CELLS:
            for n in active():
                for sign in (-1, 1):
                    verdict = source_sample(first, second, n, sign)
                    reflected = source_sample(second, first, n, -sign)
                    assert verdict == reflected, (first.label, second.label, n, sign)
                    tests += 1
                    if verdict == "OVERLAP":
                        source_edges.add((first.label, second.label, n, sign))
                    else:
                        assert verdict == "CLEAR", (first.label, second.label, n, sign)
    assert source_edges == expected, (
        "Wrong original Lean first/second source argument interpretation",
        sorted(source_edges),
    )

    # WRONG no-swap dictionary must be rejected on a genuine n9 edge.
    assert classify(CELLS[0], CELLS[1], 9, 1)[0] == "CLEAR"
    assert source_sample(CELLS[0], CELLS[1], 9, 1) == "OVERLAP"
    assert source_sample(CELLS[1], CELLS[0], 9, -1) == "OVERLAP"
    assert source_sample(CELLS[0], CELLS[1], 9, -1) == "CLEAR"

    # Rigorous exact-Fraction real log9 bracket, BOTH endpoints.
    loglo, loghi = rigorous_log(9)
    for tau in (loglo, loghi):
        assert exact_overlap(0, 1, tau) > 0
        assert exact_overlap(1, 0, -tau) > 0
        assert exact_overlap(0, 1, -tau) == 0
        assert exact_overlap(1, 0, tau) == 0

    # Finite piecewise-constant exact-complex surrogate. This tests
    # the algebraic input convention, NOT Schwartz continuity or Lean.
    f = {
        0: ComplexQ(Q(1), Q(1)),
        1: ComplexQ(Q(2), Q(-3)),
        2: ComplexQ(Q(1), Q(2)),
    }
    g = {
        0: ComplexQ(Q(3), Q(-2)),
        1: ComplexQ(Q(-1), Q(2)),
        3: ComplexQ(Q(2), Q(1)),
    }
    alpha = ComplexQ(Q(2), Q(3))
    beta = ComplexQ(Q(-1), Q(2))
    tau = Q(2197, 1000)
    assert abs(tau - Q(2198, 1000)) < Q(2, 1000)
    for shift in (tau, -tau, Q(0), Q(1, 2), Q(7, 10)):
        sample = correlation(f, g, shift)
        reflected = correlation(g, f, -shift)
        assert sample == reflected.conj(), ("adjoint shift failed", str(shift))
        scaled = correlation(scale_wave(f, alpha), scale_wave(g, beta), shift)
        assert scaled == alpha.conj() * beta * sample, (
            "first-antilinear/second-linear convention failed", str(shift),
        )
        diag_two_signs = correlation(f, f, shift) + correlation(f, f, -shift)
        assert diag_two_signs.is_real(), ("two-sign diagonal nonreal", str(shift))

    l = {0: ComplexQ(Q(1), Q(1))}
    r = {1: ComplexQ(Q(2), Q(-1))}
    c_plus = correlation(l, r, tau)
    c_minus = correlation(l, r, -tau)
    assert c_plus != ZERO and c_minus == ZERO
    assert c_plus != correlation(r, l, tau)  # false same-sign input swap
    assert c_plus == correlation(r, l, -tau).conj()

    receipt = {
        "schema": "IV029-original-source-signed-correlation-input-order-v1",
        "literal_Lean_definition": (
            "neutralWindowCorrelation a first second tau = "
            "integral second(x)*conj(first(x-tau)) dx"
        ),
        "graph_from_is_SOURCE_second_argument": True,
        "graph_to_is_SOURCE_first_argument": True,
        "source_argument_order_is_NOT_graph_arrow_order": True,
        "original_source_signed_possible_n9_entries": [
            {"first": "old_left", "second": "old_right",
             "sign": 1, "prime_power": 9},
            {"first": "old_right", "second": "old_left",
             "sign": -1, "prime_power": 9},
        ],
        "original_graph_from_to_signed_possible_n9_entries": [
            {"from": "old_right", "to": "old_left",
             "sign": 1, "prime_power": 9},
            {"from": "old_left", "to": "old_right",
             "sign": -1, "prime_power": 9},
        ],
        "all_directed_source_pair_prime_power_samples": tests,
        "conjugation_and_shift_adjoint_verified_in_exact_step_surrogate": True,
        "first_argument_antilinear_second_linear_in_exact_step_surrogate": True,
        "diagonal_two_signed_samples_real_in_exact_step_surrogate": True,
        "naive_no_swap_and_same_sign_negative_controls_rejected": True,
        "rigorous_log9_bracket_both_endpoints_preserve_overlap_orientation": True,
        "step_surrogate_is_not_Schwartz": True,
        "graph_edges_are_only_possible_prime_interactions_not_pairing_values": True,
        "genuine_original_sesquilinear_dictionary_Lean_certified": False,
        "independent_spectral_operator_or_preservation_map_constructed": False,
        "global_Weil_positivity": False,
        "RH": False,
    }
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print("IV029 SOURCE-DICTIONARY EXACT NONKERNEL PASS:",
          tests, "directed source pair prime-power samples;",
          "source argument reversal, complex conjugation and signed adjoint;",
          "no Lean compiler or spectral claim.")
    return receipt


if __name__ == "__main__":
    argparse.ArgumentParser().parse_args()
    preflight()
