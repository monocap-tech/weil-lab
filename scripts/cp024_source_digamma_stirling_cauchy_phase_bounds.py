#!/usr/bin/env python3
"""CP024 ORIGINAL-SOURCE analytic phase envelopes: exact rational preflight.

This is a FALSIFIABLE calculation of all rational reductions in an
analytic proof using frozen ACTUAL original Zeta Mathlib theorems:
  Complex.Stirling.norm_digamma_sub_log_le',
  Complex.norm_deriv_le_of_forall_mem_sphere_norm_le,
  hasDerivAt_riemannSiegelTheta,
  Complex.im_deriv_digamma_nonpos,
  Real.log_two_lt_d9 and Real.one_sub_inv_le_log_of_pos.

The user's ORIGINAL phase is theta=riemannSiegelTheta, and
w(t)=1/4+i*t/2, 149.5<=t<=150.05353.

PROPOSED MATHEMATICAL ENVELOPES:
    2/5 <= theta'(t) <= 9/5;
    0   <= theta''(t) <= 1/200.

The digamma error H(z)=psi(z)-Log z+(2z)^-1 is holomorphic
on the complex circle |z-w(t)|<=1/8; Re z>=1/8, |z|>=74.
Original Stirling gives |H(z)| <= (17/12)/74^2 < 1/3000.
Original complex Cauchy gives |H'(w)| <= 8/3000=1/375.
Since psi'(w)=1/w+1/(2w^2)+H'(w):
  |psi'(w)| <= 1/74+1/(2*74^2)+1/375 < 1/50,
  theta''(t)=-Im psi'(w)/4, with Im psi'<=0 upstream;
  hence 0<=theta''<=1/200.

At center, source gives |H(w)|<1/5000, so
  |Re psi(w)-log|w|| <= 1/148+1/5000 <1/100.
Also 37/2 <= |w|/pi <=76/3 <32, and
  log 32 =5 log 2 <7/2 via original Mathlib log_two_lt_d9,
  log x>=1-1/x via Real.one_sub_inv_le_log_of_pos.
Thus 3463/7400 <= theta' <=351/200, proving the advertised
coarse 2/5<=theta'<=9/5.

ALL discrete inequalities here are exact Fraction. THIS PROGRAM DOES
NOT kernel-compile the above analytic implications, prove the source
phase envelopes in Lean, certify complex interval balls for original
finite zeta approximant, or establish a zero/Weil/RH theorem.

The earlier original Euler–Maclaurin R0/R1/R2 error caps are also
SOURCE-ONLY uncompiled local Cauchy theorem targets. Conditional on
those caps, improved Hardy-Z remainder error buffers become
  |Z_R'|<=87/(5*10^13)=1.74e-12,
  |Z_R''|<=29787/(200*10^13)=1.48935e-11.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import re
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ORIGINAL_ZETA_COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
ORIGINAL_MATHLIB_REF="v4.35.0"
ZETA_PINS={
 "Zeta/Gamma/DigammaStirling.lean":"9b5a21dfefe6c778411b03fc7e0cf8e8c5bcfac8",
 "Zeta/Gamma/TrigammaDecay.lean":"60b6e9a4645d06988d2ca2d293b141195382d37c",
 "Zeta/Gram/Averaging.lean":"6a30171433903a57736de2ab83b120ef660e08bd",
}
MATHLIB_PINS={
 "Mathlib/Analysis/Complex/Liouville.lean":"70382d63ec267d2704790b1d77692e1f5cd5faed",
 "Mathlib/Analysis/Complex/ExponentialBounds.lean":"bbc13e49781e7f620ffa0b69d693e753d2190cb8",
 "Mathlib/Analysis/Complex/Norm.lean":"0e2b6317a777c4d168a9098fb17ad33323efd4c3",
}
SIGNATURES={
 "Zeta/Gamma/DigammaStirling.lean":["theorem norm_digamma_sub_log_le'"],
 "Zeta/Gamma/TrigammaDecay.lean":["theorem im_deriv_digamma_nonpos",
                                "theorem monotoneOn_re_digamma_quarter_vertical"],
 "Zeta/Gram/Averaging.lean":["theorem hasDerivAt_riemannSiegelTheta",
                             "Real.one_sub_inv_le_log_of_pos"],
 "Mathlib/Analysis/Complex/Liouville.lean":[
    "theorem norm_deriv_le_of_forall_mem_sphere_norm_le"],
 "Mathlib/Analysis/Complex/ExponentialBounds.lean":[
    "theorem log_two_lt_d9"],
 "Mathlib/Analysis/Complex/Norm.lean":["theorem abs_re_le_norm"],
}
A=Q(299,2)
B=Q(15005353,100000)
R=Q(1,8)
WLOW=Q(74)
WHIGH=Q(76)
C0=Q(3,4)
CC=Q(17,12)
H_CENTER_CAP=Q(1,5000)
H_CIRCLE_CAP=Q(1,3000)
DELTA_CAP=Q(1,100)
H_PRIME_CAP=Q(1,375)
PSI_PRIME_CAP=Q(1,50)
P_LO=Q(2,5)
P_HI=Q(9,5)
Q_LO=Q(0)
Q_HI=Q(1,200)
R0=Q(3,10**13)
R1=Q(12,10**13)
R2=Q(96,10**13)
R3=Q(1152,10**13)
E1=Q(87,5*10**13)
E2=Q(29787,200*10**13)
PREVIOUS_E1=Q(18,10**13)
PREVIOUS_E2=Q(159,10**13)

def test_exact():
    assert A==Q("149.5") and B==Q("150.05353")
    assert A>0 and B>A
    # w=1/4+i*t/2; |w|≥t/2≥299/4≥74.
    assert A/2==Q(299,4)>WLOW
    assert Q(1,4)+B/2<WHIGH
    # On the ENTIRE closed complex disk |z-w|≤1/8.
    assert Q(1,4)-R==Q(1,8)>0
    assert A/2-R==Q(597,8)>WLOW
    # Source: C(a) = 1/12 + 3/(2*pi²*a);
    # replacing pi² by rigorous LOWER bound 3².
    assert Q(1,12)+3/(2*Q(9)*Q(1,4))==C0
    assert Q(1,12)+3/(2*Q(9)*Q(1,8))==CC
    assert C0/WLOW**2==Q(3,21904)<H_CENTER_CAP
    assert CC/WLOW**2==Q(17,65712)<H_CIRCLE_CAP
    # Center psi-log real error |(2w)^-1|+|H(w)| <1/100.
    delta=Q(1,2*WLOW)+H_CENTER_CAP
    assert delta==Q(1287,185000)<DELTA_CAP
    # |w|/pi in [74/4, 76/3], and 76/3<32.
    assert WLOW/Q(4)==Q(37,2)>1
    assert WHIGH/Q(3)<32
    # Genuine original log2 theorem: log2<0.6931471808<7/10.
    assert Q("0.6931471808")<Q(7,10)
    assert 5*Q(7,10)==Q(7,2)
    # log x >= 1-1/x, x>=37/2, so theta' lower >=3463/7400.
    lo=(Q(1)-Q(2,37)-DELTA_CAP)/2
    hi=(Q(7,2)+DELTA_CAP)/2
    assert lo==Q(3463,7400)>P_LO
    assert hi==Q(351,200)<P_HI
    # Original Cauchy on 1/8 circle: |H'(w)| <=8/3000.
    assert H_CIRCLE_CAP/R==H_PRIME_CAP
    psi_prime_bound=Q(1,WLOW)+Q(1,2*WLOW**2)+H_PRIME_CAP
    assert psi_prime_bound==Q(66827,4107000)<PSI_PRIME_CAP
    assert PSI_PRIME_CAP/4==Q_HI
    # Original upstream im psi'(w)<=0 gives theta''>=0.
    assert Q_LO==0
    # Improved actual HardyZ phase remainder conditional buffers.
    # Attention: R=1/8 here is DIGAMMA disk, not ζ disk radius 1/4.
    # ζ Cauchy derivative recurrences use 1/4, not R.
    assert R1==R0/Q(1,4)
    assert R2==Q(2)*R0/Q(1,4)**2
    assert R3==Q(6)*R0/Q(1,4)**3
    assert P_HI*R0+R1==E1
    assert (P_HI**2+Q_HI)*R0+2*P_HI*R1+R2==E2
    assert E1<PREVIOUS_E1 and E2<PREVIOUS_E2
    assert E1==Q("0.00000000000174")
    assert E2==Q("0.0000000000148935")
    # Negative controls fail in exact rationals:
    assert C0/WLOW**2>Q(1,10000)
    assert CC/WLOW**2>Q(1,5000)
    assert psi_prime_bound>Q(1,100)
    assert hi>Q(17,10)
    assert E2>Q(1,10**11)
    print("CP024 ORIGINAL STIRLING/CAUCHY PHASE EXACT RATIONAL PREFLIGHT: PASS NOT LEAN")
    print("  source original height interval",A,B,"digamma disk",R)
    print("  original centered Stirling bound <= ",C0/WLOW**2,"<",H_CENTER_CAP)
    print("  whole digamma circle bound <=",CC/WLOW**2,"<",H_CIRCLE_CAP)
    print("  Cauchy |H'| <=",H_PRIME_CAP,"; |psi'| <=",psi_prime_bound,"<",PSI_PRIME_CAP)
    print("  mathematically derived theta' rational envelope",lo,hi)
    print("  source-derivable coarse 2/5<=theta'<=9/5 and 0<=theta''<=1/200")
    print("  conditional Hardy-Z remainder first jet <=",E1,"=",float(E1))
    print("  conditional Hardy-Z remainder second jet <=",E2,"=",float(E2))
    print("  strengthened vs CP023 exactly:",PREVIOUS_E1-E1,PREVIOUS_E2-E2)
    print("  bad-too-tight bounds rejected by exact rational negative controls")
    print("  no original Lean kernel/interval phase envelope/root/Weil certificate implied")

def git_blob_sha(path:Path)->str:
    h=hashlib.sha1(b"blob "+str(path.stat().st_size).encode()+b"\0")
    with path.open("rb") as f:
        for part in iter(lambda:f.read(1<<20),b""):
            h.update(part)
    return h.hexdigest()

def upstream_audit(zeta:Path, mathlib:Path):
    for base,pins in ((zeta,ZETA_PINS),(mathlib,MATHLIB_PINS)):
        for name,sha in pins.items():
            f=base/name
            got=git_blob_sha(f)
            if got!=sha:
                raise ValueError(f"original frozen source Git blob mismatch {name}: {got} != {sha}")
            content=f.read_text("utf-8")
            for theorem in SIGNATURES[name]:
                if theorem not in content:
                    raise ValueError(f"missing actual original source theorem {name}: {theorem}")
    print("CP024 SIX ORIGINAL DIGAMMA/CAUCHY/LOG-BOUND GIT-BLOB AND API CHECKS: 6/6 PASS NOT LEAN")

def local_source_audit():
    base=ROOT/"cp011_zeta_v435"
    first=(base/"CP021GermLeaf.lean").read_text("utf-8")
    last=(base/"CP021BorweinLeaf.lean").read_text("utf-8")
    theta=(base/"CP019ThetaSecond.lean").read_text("utf-8")
    jet=(base/"CP018HardyJet.lean").read_text("utf-8")
    if not all(t in first for t in (
        "original_zeta_EM_derivative_error_identity",
        "Filter.EventuallyEq.iteratedDeriv_eq",
        "riemannZeta_eq_approximant_add_remainder")):
        raise ValueError("Original ζ−EM germ identity source contract missing")
    if not all(t in last for t in (
        "original_Borwein_all_circles",
        "original_complex_cpow_bound",
        "norm_ascPochhammer_eval_le_product")):
        raise ValueError("original Borwein all-circle source contract missing")
    if not all(t in theta for t in (
        "original_riemannSiegelTheta_second_deriv",
        "hasDerivAt_riemannSiegelTheta",
        "deriv Complex.digamma")):
        raise ValueError("original phase second derivative source candidate missing")
    if not all(t in jet for t in (
        "thetaPrimeJet","thetaSecondJet","sourceFirstJet","sourceSecondJet")):
        raise ValueError("actual original phase/ζ complex jet source declarations missing")
    if re.search(r"(?m)^\s*(axiom|sorry|constant)\b",last+"\n"+first):
        raise ValueError("untrusted admission in the isolated original source leaves")
    print("CP024 FOUR PREVIOUS SOURCE JET/LEAF DECLARATION CONTRACTS: 4/4 PASS NOT LEAN")

def receipt(path:Path):
    data={
      "status":"CP024_SOURCE_BASED_STIRLING_CAUCHY_PHASE_BUDGET_PASS_NOT_LEAN",
      "original_zeta_commit":ORIGINAL_ZETA_COMMIT,
      "original_mathlib_ref":ORIGINAL_MATHLIB_REF,
      "original_six_pinned_source_blobs":{**ZETA_PINS,**MATHLIB_PINS},
      "exact_original_height_range":[str(A),str(B)],
      "digamma_Cauchy_radius":"1/8",
      "source_derived_phase_prime_bounds":["2/5","9/5"],
      "source_derived_phase_second_bounds":["0","1/200"],
      "phase_prime_and_second_original_Lean_kernel_accepted":False,
      "previous_original_zeta_remainder_complex_Cauchy_Lean_kernel_accepted":False,
      "conditional_first_HardyZ_remainder_error":str(E1),
      "conditional_second_HardyZ_remainder_error":str(E2),
      "finite_original_zeta_approximant_interval_enclosures":False,
      "original_Zprime_anchor_ge12_div5_certified":False,
      "original_full_interval_Zsecond_curvature_le4_certified":False,
      "original_narrow_root53_numerical_sign":False,
      "original_signed_Weil_to_full_spectral_dictionary":False,
      "global_Weil_positivity_or_RH":False,
    }
    path.write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
    print(data["status"])

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--source-contract",action="store_true")
    p.add_argument("--original-zeta",type=Path)
    p.add_argument("--original-mathlib",type=Path)
    p.add_argument("--receipt",type=Path)
    args=p.parse_args()
    if args.self_test:test_exact()
    if args.source_contract:local_source_audit()
    if bool(args.original_zeta)!=bool(args.original_mathlib):
        p.error("frozen source verification requires original Zeta AND Mathlib roots")
    if args.original_zeta:upstream_audit(args.original_zeta,args.original_mathlib)
    if args.receipt:
        if not (args.self_test and args.source_contract and args.original_zeta):
            raise ValueError("fail closed: receipt requires exact math, local source AND all six original immutable source checks")
        receipt(args.receipt)
    if not (args.self_test or args.source_contract or args.original_zeta):
        p.print_help()

if __name__=="__main__":
    try:main()
    except (OSError,ValueError,UnicodeError,AssertionError) as e:
        raise SystemExit("CP024 SOURCE/EXACT TEST NOT READY: "+str(e))
