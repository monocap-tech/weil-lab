#!/usr/bin/env python3
"""CP019 exact Fraction original Euler–Maclaurin Borwein/Cauchy budget.
SOURCE/EXACT ARITHMETIC ONLY — never claim a new Lean kernel or real
Hardy-Z derivative enclosure from a Python source check.

The original M=6,N=256 source complex remainder norm and circle geometry
give a fully rational majorant C < 3/10**13 on all radius-1/4 circles
about 1/2+it, t in [149.5,150.05353].  Original Cauchy yields
derivative residual caps k! C/(1/4)**k, k=0,1,2,3.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as F
from math import comb, factorial, prod
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ZETA_COMMIT="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
ZETA_PINS={
 "Zeta/Gram/Averaging.lean":"6a30171433903a57736de2ab83b120ef660e08bd",
 "Zeta/Gamma/TrigammaDecay.lean":"60b6e9a4645d06988d2ca2d293b141195382d37c",
 "Zeta/EulerMaclaurin/Continuation.lean":"1bb01e946fa7e344497eaf7694fbecff0a714d09",
 "Zeta/EulerMaclaurin/ErrorBound.lean":"01184af0dbfd1369e14725e02e990b016bedfe6f",
 "Zeta/Zeros/HardyZ.lean":"9975442b0c14011c35f4624197d0bf26169c7665",
}
MATHLIB_PINS={
 "Mathlib/Analysis/Complex/Liouville.lean":"70382d63ec267d2704790b1d77692e1f5cd5faed",
 "Mathlib/Analysis/Complex/RealDeriv.lean":"d7223234773ef2f7caec59a941211806412083fa",
}
A=F(299,2)
B=F(15005353,100000)
R=F(1,4)
M=6
N=256
CAP=F(3,10**13)
EXPECTED=F(181596617021805363,633825300114114700748351602688)
REQUIRED={
 "CP019OriginalFirstJet.lean":(
   "original_theta_deriv_eq_digamma",
   "original_hardyZ_hasDerivAt_first_source_jet",
   "original_hardyZ_deriv_eq_first_source_jet"),
 "CP019ThetaSecond.lean":(
   "hasDerivAt_re_digamma_quarter_vertical",
   "original_riemannSiegelTheta_second_deriv",
   "original_phase_second_jet_matches_source"),
 "CP019CauchyRemainder.lean":(
   "sphere_re_quarter_le",
   "original_source_zeta_remainder_bound_on_circle",
   "exact_rational_Borwein_majorant",
   "original_zeta_EM_remainder_cauchy_budget",
   "third_derivative_original_zeta_EM_remainder_budget",
   "hholomorphic","hBorweinOnCircle"),
}
SIGS={
 "Zeta/Gram/Averaging.lean":["theorem hasDerivAt_riemannSiegelTheta"],
 "Zeta/Gamma/TrigammaDecay.lean":[
   "theorem monotoneOn_re_digamma_quarter_vertical",
   "HasDerivAt (fun t : ℝ ↦ (Complex.digamma"],
 "Zeta/EulerMaclaurin/Continuation.lean":[
   "theorem differentiableOn_eulerMaclaurinRemainderIoi_cpow",
   "theorem analyticOnNhd_zetaEMExpansion",
   "noncomputable abbrev zetaRemainder",
   "theorem riemannZeta_eq_approximant_add_remainder"],
 "Zeta/EulerMaclaurin/ErrorBound.lean":[
   "noncomputable abbrev zetaRemainderBound",
   "theorem norm_zetaRemainder_le"],
 "Zeta/Zeros/HardyZ.lean":[
   "noncomputable def Zeta.hardyZ",
   "theorem abs_hardyZRemainderEM_le"],
 "Mathlib/Analysis/Complex/Liouville.lean":[
   "theorem norm_iteratedDeriv_le_of_forall_mem_sphere_norm_le"],
 "Mathlib/Analysis/Complex/RealDeriv.lean":[
   "theorem HasDerivAt.ofReal_comp",
   "theorem HasDerivAt.comp_ofReal"],
}

def bernoulli(n:int)->F:
    b=[F(1)]
    for k in range(1,n+1):
        b.append(-sum(F(comb(k+1,j))*b[j] for j in range(k))/F(k+1))
    return b[n]

def exact_budget():
    assert A==F("149.5") and B==F("150.05353")
    assert B-A==F(55353,100000)
    # Re(z)>=1/2-R=1/4 and |z|<=|1/2+it|+R<=1/2+B+R<151.
    assert F(1,2)-R==F(1,4)>0
    assert F(1,2)+B+R<151
    # Original Borwein prefactor |z+13|/(Re z+13) <=164/(13+1/4).
    assert F(164,1)/F(53,4)==F(656,53)
    assert bernoulli(1)==-F(1,2)
    assert bernoulli(12)==-F(691,2730)
    assert bernoulli(14)==F(7,6)
    # Original ascPochhammer_13(s) product j=0..12 norm <= product(151+j).
    envelope=F(656,53)*F(7,6*factorial(14))*F(prod(range(151,164)),N**13)
    assert envelope==EXPECTED
    assert envelope<CAP
    print("CP019 EXACT ORIGINAL BORWEIN UNIFORM COMPLEX CIRCLE ENVELOPE: PASS")
    print("  M=6 N=256 complex radius=1/4; original Re(z)>=1/4 |z|<151")
    print("  exact original B14=7/6 via recurrence; K<=656/53")
    print("  exact Borwein rational envelope:",envelope)
    print("  strict rational cap:",CAP)
    for k in range(4):
        residual=factorial(k)*CAP/R**k
        assert factorial(k)*envelope/R**k<residual
        print(f"  Cauchy order {k} source upper {residual} (display {float(residual):.15e})")
    assert factorial(3)*CAP/R**3==F(1152,10**13)
    assert envelope>F(1,10**13)
    assert factorial(3)*CAP/R**3>F(1,10**10)
    print("CP019 TOO-STRONG-CAP NEGATIVE CONTROLS: PASS")
    print("Actual Cauchy circle source-to-Lean hypotheses remain OPEN; no kernel pass.")

def gitblob(p:Path)->str:
    n=p.stat().st_size
    h=hashlib.sha1(b"blob "+str(n).encode()+b"\0")
    with p.open("rb") as stream:
        for part in iter(lambda:stream.read(1<<20),b""):
            h.update(part)
    return h.hexdigest()

def source_gate(zeta,mathlib,receipt):
    actual={}
    for base,pins in [(zeta,ZETA_PINS),(mathlib,MATHLIB_PINS)]:
        for name,sha in pins.items():
            p=base/name
            if gitblob(p)!=sha:
                raise ValueError("Original source git blob mismatch: "+name)
            actual[name]=p.read_text("utf-8")
    for name,strings in SIGS.items():
        for s in strings:
            if s not in actual[name]:
                raise ValueError("Original source declaration drift: "+name+" : "+s)
    for name,strings in REQUIRED.items():
        src=(ROOT/"cp011_zeta_v435"/name).read_text("utf-8")
        for s in strings:
            if s not in src:
                raise ValueError("Local CP019 source missing prerequisite: "+name+" : "+s)
        if "sorry" in src.split("@[expose] public section")[-1]:
            raise ValueError("CP019 source proof section has sorry: "+name)
    receipt.write_text(json.dumps({
      "status":"CP019_SEVEN_PINNED_SOURCES_AND_EXACT_CAUCHY_BUDGET_PASS_NOT_KERNEL",
      "original_zeta_commit":ZETA_COMMIT,
      "original_mathlib_rev":"v4.35.0",
      "original_source_sha":{**ZETA_PINS,**MATHLIB_PINS},
      "exact_M":M,"exact_N":N,"exact_complex_radius":str(R),
      "source_height_window":[str(A),str(B)],
      "original_Borwein_upper_rational":str(EXPECTED),
      "strict_complex_remainder_cap":str(CAP),
      "conditional_complex_derivative_caps":[
        str(factorial(k)*CAP/R**k) for k in range(4)],
      "new_HardyZ_first_deriv_Lean_accepted":False,
      "new_theta_second_deriv_Lean_accepted":False,
      "source_remainder_ball_holomorphy_Lean_accepted":False,
      "original_Borwein_circle_majorant_Lean_accepted":False,
      "Cauchy_derivative_remainder_Lean_accepted":False,
      "actual_HardyZ_uniform_curvature_proved":False,
      "actual_narrow_root53_exists_Lean_accepted":False,
      "original_signed_Weil_spectral_dictionary":False,
    },indent=2)+"\n","utf-8")
    print("CP019_SEVEN_PINNED_SOURCES_AND_EXACT_CAUCHY_BUDGET_PASS_NOT_KERNEL")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--zeta",type=Path)
    p.add_argument("--mathlib",type=Path)
    p.add_argument("--receipt",type=Path,default=Path("cp019-source-cauchy-budget.json"))
    args=p.parse_args()
    if args.self_test: exact_budget()
    if bool(args.zeta)!=bool(args.mathlib):
        p.error("Original source audit requires both Zeta and Mathlib")
    if args.zeta:
        try: source_gate(args.zeta,args.mathlib,args.receipt)
        except (OSError,ValueError,UnicodeError) as e:
            raise SystemExit("NOT_READY: "+str(e))
    if not (args.self_test or args.zeta): p.print_help()

if __name__=="__main__": main()
