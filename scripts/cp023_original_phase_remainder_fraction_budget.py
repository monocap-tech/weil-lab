#!/usr/bin/env python3
"""CP023 strict, exact-rational PHASE-AWARE Zeta remainder error budget.

This is an analytic SOURCE-INTEGRATION planning certificate, NOT a
complex ball interval enclosure, not a new Lean theorem or kernel PASS.

Under the real Hardy-Z original phase derivative envelopes
    |theta'(t)| <= 2,   |theta''(t)| <= 1,
and the TRUE CP019–22 conditional complex Zeta Euler–Maclaurin
Cauchy remainder error budgets on the entire height interval:
    |R| <= 3e-13, |R'| <= 1.2e-12, |R''| <= 9.6e-12,
we get real rotated first- and second-jet errors:

  E_1 = Re( exp(i theta) * i * (theta' R + R') )
  |E_1| <= 2 |R| + |R'| <= 18/10^13 = 1.8e-12

  E_2 = Re( exp(i theta) *
     (-theta'^2 R - 2 theta' R' - R'' + i theta'' R) )
  |E_2| <= (2^2+1)|R| + 2*2|R'| + |R''|
        <= 159/10^13 = 1.59e-11

These bounds follow from |exp(i theta)|=1 and the complex triangle
inequality. The phase-derivative envelopes are UNSUPPLIED ORIGINAL
ANALYTIC NUMERICAL HYPOTHESES. Remainder derivative upper bounds are
not yet NEW Lean-kernel accepted. This script only checks exact
rational arithmetic and phase-jet syntax/provenance. Never assert
HardyZ global curvature, root 53, spectral equality or RH.
"""
from __future__ import annotations
import argparse
import json
import re
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = F("149.5")
END = F("150.05353")
RADIUS = F(1,4)
R0 = F(3,10**13)
R1 = F(12,10**13)
R2 = F(96,10**13)
R3 = F(1152,10**13)
P = F(2)
Q = F(1)
E1 = F(18,10**13)
E2 = F(159,10**13)
DERIV_MARGIN = F(4647,25000)
KERNEL_STATUS = "NO_NEW_ACCEPTED_CP013_CP023_LEAN_KERNEL_PROOF"
REPORT = {
    "status": "CP023_PHASE_REMAINDER_EXACT_BUDGET_PASS_NOT_SOURCE_LEAN",
    "target_interval": [str(START), str(END)],
    "phase_derivative_assumptions_unproved": {
      "abs_theta_prime_uniform": str(P),
      "abs_theta_double_prime_uniform": str(Q),
    },
    "complex_EM_remainder_Cauchy_upper_bounds_Not_Lean_accepted": {
      "R0": str(R0), "R1": str(R1), "R2": str(R2), "R3": str(R3)
    },
    "if_hypotheses_then_first_hardyZ_jet_error": str(E1),
    "if_hypotheses_then_second_hardyZ_jet_error": str(E2),
    "source_Lean_v435_new_kernel_certification": False,
    "source_original_phase_uniform_interval_enclosures": False,
    "finite_original_EM_approximant_derivative_interval_enclosures": False,
    "true_HardyZ_anchor_ge_12_div_5": False,
    "true_HardyZ_second_derivative_abs_le_4_uniform": False,
    "CP010_narrow_refined_root_sign_certificate": False,
    "original_complete_signed_Weil_spectral_identity": False,
    "RH_or_global_Weil_positivity": False,
}

def exact_test():
    assert START == F(299,2) and END - START == F(55353,100000)
    assert RADIUS == F(1,4)
    # Cauchy derivatives, from the original M=6 N=256 circle radius 1/4.
    assert R1 == R0/RADIUS
    assert R2 == F(2)*R0/RADIUS**2
    assert R3 == F(6)*R0/RADIUS**3
    assert P*R0 + R1 == E1
    assert (P*P+Q)*R0 + 2*P*R1 + R2 == E2
    assert E1 == F("0.0000000000018")
    assert E2 == F("0.0000000000159")
    assert DERIV_MARGIN > E1
    assert F(4) - E2 > F("3.99999999998")
    # Reject unsupported stronger derivative-error conclusions.
    assert E1 > F(1,10**12)
    assert E2 > F(1,10**11)
    # If phase'<=3 instead of 2, the advertised E1 budget is invalid.
    assert 3*R0+R1>E1
    assert (3*3+Q)*R0+2*3*R1+R2>E2
    print("CP023 EXACT PHASE/COMPLEX-EM-REMAINDER JET BUDGET: PASS NOT LEAN")
    print("  original phase envelopes |theta-prime|<=2, |theta-second|<=1: UNPROVED")
    print("  original complex ζ remainder Cauchy bounds: not yet local Lean kernel")
    print(f"  first real phase-remainder derivative error <= {E1} = {float(E1):.5g}")
    print(f"  second real phase-remainder curvature error <= {E2} = {float(E2):.5g}")
    print("  false-tight-error and weakened-phase-assumption controls: PASS")

def source_contract():
    base=ROOT/"cp011_zeta_v435"
    jet=(base/"CP018HardyJet.lean").read_text("utf-8")
    rem=(base/"CP021BorweinLeaf.lean").read_text("utf-8")
    germ=(base/"CP021GermLeaf.lean").read_text("utf-8")
    explicit=[
        "noncomputable def sourceFirstJet",
        "noncomputable def sourceSecondJet",
        "deriv (deriv riemannZeta)",
        "thetaPrimeJet",
        "thetaSecondJet",
    ]
    for x in explicit:
        if x not in jet:raise ValueError("missing frozen original phase/zeta source jet token: "+x)
    if not all(x in rem for x in (
        "original_Borwein_all_circles","original_bernoulli_fourteen",
        "norm_ascPochhammer_eval_le_product",
        "have ht_nonneg : (0 : ℝ) ≤ t := by",
        "abs_of_nonneg ht_nonneg")):
        raise ValueError("CP022 repaired original complex-circle leaf missing")
    if "abs_of_nonneg ht.1" in rem:
        raise ValueError("regression: invalid lower-bound proof in CP021 Borwein leaf")
    if not all(x in germ for x in (
        "riemannZeta_eq_approximant_add_remainder",
        "Filter.EventuallyEq.iteratedDeriv_eq",
        "original_zeta_EM_derivative_error_identity")):
        raise ValueError("source-germ leaf changed away from actual original identity")
    if re.search(r"(?m)^\s*(sorry|axiom|opaque|constant)\b", rem+"\n"+germ):
        raise ValueError("new leaf uses untrusted axiom/constant or sorry")
    print("CP023 ORIGINAL HARDY-Z PHASE-JET / ZETA LEAF SOURCE CONTRACT: PASS NOT LEAN")

def optional_screen():
    """Numerical only; NEVER interval-certificate or theorem proof."""
    import mpmath as mp
    mp.mp.dps=35
    samples=("149.5","149.75","150.05353")
    for s in samples:
        t=mp.mpf(s); w=mp.mpf(1)/4+1j*t/2
        p=(mp.re(mp.digamma(w))-mp.log(mp.pi))/2
        q=-mp.im(mp.polygamma(1,w))/4
        print("CP023 NONRIGOROUS phase sample",
              s,"theta'≈",mp.nstr(p,20),"theta''≈",mp.nstr(q,20),
              "NOT uniform/rigorous")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--self-test",action="store_true")
    ap.add_argument("--source-contract",action="store_true")
    ap.add_argument("--numeric-screen",action="store_true")
    ap.add_argument("--receipt",type=Path)
    args=ap.parse_args()
    if args.self_test:exact_test()
    if args.source_contract:source_contract()
    if args.numeric_screen:optional_screen()
    if args.receipt:
        args.receipt.write_text(json.dumps(REPORT,indent=2)+"\n",encoding="utf-8")
    if not (args.self_test or args.source_contract or args.numeric_screen):
        ap.print_help()

if __name__=="__main__":
    try:main()
    except (ValueError,OSError) as err:
        raise SystemExit("CP023 NOT_READY: "+str(err))
