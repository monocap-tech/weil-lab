#!/usr/bin/env python3
"""NF499 first ACTUAL original J242 SELECTED pole mixed source moment.

For the explicit source-original genuine terminal logarithmic carrier
ell_U(x)=sgn(x)*1_{B-delta<|x|<B}U(|x|)/2 log(B/(B-|x|)),
and the authentic original J242 selected pole s(x)=sinh(x/2) (index
241), compute the exact physical whole-two-collar selected moment
 <s,ell_U> = int_0^delta U(B-d)sinh((B-d)/2)log(B/d) dd
using independently accepted ORIGINAL NF493 400 full U source-4096bit
outward coefficient balls; one real native original source, no new fit.

Direct rational atanh log550, rational sinh and cosh Taylor positive
remainders, actual 110 retained original U jets and paid remaining
290 exact source coefficients plus accepted U400 Cauchy, plus separate
sinh Taylor remainder and genuine improper log integral.

Then the explicit NF499 smooth phi_epsilon=chi_epsilon ell_U,
epsilon=1e-50 from the independently verified NF499 smoothing result
has |<s,phi>-<s,ell>|<1e-29. This certifies the first original true
nonzero selected J242 overlap, and hence
 ||P_J phi||² >= |<s,phi>|²/||s||² > 2.63e-24.
It does NOT compute remaining 241 selected cross moments or
the true Q_Jw/Q_Jphi projected rank-one capture, or prove source/
operator-domain eligibility.

NF404 ORIGINAL physical pole norm ||s||²=sinh(B)-B is independently
recomputed by exact rational Taylor and checked against its original
source-exact interval. No math source or original selected J is changed.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json,math,sys
from decimal import Decimal,localcontext
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);DELTA=F(1,500);K=110;J=20;NS=100;NL=130
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
class Iv:
    __slots__=("lo","hi")
    def __init__(self,lo,hi=None):
        self.lo=F(lo);self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,o):
        if not isinstance(o,Iv):o=Iv(o)
        return Iv(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return Iv(-self.hi,-self.lo)
    def __sub__(self,o):return self+(-o if isinstance(o,Iv) else -F(o))
    def __mul__(self,o):
        if not isinstance(o,Iv):o=Iv(o)
        z=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return Iv(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,o):
        if not isinstance(o,Iv):o=Iv(o)
        assert o.lo>0 or o.hi<0
        return self*Iv(F(1)/o.hi,F(1)/o.lo)
    def maxabs(self):return max(abs(self.lo),abs(self.hi))
    def pad(self,x):
        x=F(x);assert x>=0
        return Iv(self.lo-x,self.hi+x)
    def contains_overlap(self,o):return self.lo<=o.hi and o.lo<=self.hi
    def raw(self):return [str(self.lo),str(self.hi)]
    def decimals(self,significant=48):
        with localcontext() as ctx:
            ctx.prec=significant+10
            return [format(+(Decimal(v.numerator)/Decimal(v.denominator)),f".{significant-1}E") for v in (self.lo,self.hi)]
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def logpositive(z,N):
    assert F(0)<z<F(1)
    p=z;lo=F(0)
    for n in range(N):
        lo+=2*p/(2*n+1)
        p*=z*z
    return Iv(lo,lo+2*p/(2*N+1)/(1-z*z))
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--nf493-native",required=True)
    ap.add_argument("--nf499-smooth",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    original,sha407=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,sha406=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    nf404,sha404=read("notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
    nf493,sha493=read(args.nf493_native)
    smooth,shasmooth=read(args.nf499_smooth)
    assert sha407==SRC and sha406==SEAM
    assert nf493["pass"]=="NF493-original-source-400-log-jets"
    assert nf493["original_nf407_source_sha256"]==SRC
    assert nf493["original_nf406_seams_sha256"]==SEAM
    assert smooth["pass"]=="NF499"
    assert smooth["original_nf407_source_sha256"]==SRC
    assert smooth["original_nf406_seams_sha256"]==SEAM
    assert nf404["pass"]=="NF404" and nf404["original_dimension"]==242
    assert nf404["original_selected_pole_index"]==241
    assert original["original_selected_generator_node_orders"][241]==["pole",None]
    assert nf404["original_pole_squared_norm_exact_analytic_identity"]=="sinh(11/10)-11/10"
    assert len(original["original_selected_generator_node_orders"])==242
    assert len(original["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(original["original_source_critical_sine_frequencies"])==32
    assert nf493["original_source_log_u_taylor_degree"]=="399"
    assert len(nf493["original_real_original_U_dyadic_coefficient_ball_first_400"])==400
    assert smooth["smooth_collar_C_c_infinity_original_physical"]
    assert smooth["two_collar_smoothing_L2_error_strict_upper"]=="1/100000000000000000000000000000"
    assert F(smooth["source_full_true_U_terminal_uniform_strict_upper"])==F(2,10**7)
    assert F(smooth["smooth_phi_original_full_two_collar_capture_fraction_lower_exact"])>F("0.3402")
    u=[Iv(*map(F,p))*DELTA**n
       for n,p in enumerate(nf493["original_real_original_U_dyadic_coefficient_ball_first_400"])]
    source_tail=sum((x.maxabs() for x in u[K:]),F(0))
    analytic_tail=F(nf493["original_source_400_taylor_analytic_Cauchy_abs_tail"])
    source_tail+=analytic_tail
    assert source_tail<F(2,10**79)
    assert 0<analytic_tail<F(1,10**119)
    # Full EXACT rational original log550; log550=9log2+log(275/256).
    h=9*logpositive(F(1,3),NL)+logpositive(F(19,531),NL)
    assert F("6.3")<h.lo<=h.hi<F("6.4")
    x=B/2
    # Independent exact rational original genuine odd-pole sinh/cosh
    # values and analytic remainder; successive ratios <1/2.
    sinhl=sum((x**(2*n+1)/math.factorial(2*n+1) for n in range(NS)),F(0))
    coshl=sum((x**(2*n)/math.factorial(2*n) for n in range(NS)),F(0))
    sinh=Iv(sinhl,sinhl+2*x**(2*NS+1)/math.factorial(2*NS+1))
    cosh=Iv(coshl,coshl+2*x**(2*NS)/math.factorial(2*NS))
    assert F(0)<sinh.lo<sinh.hi<F(1)
    assert F(1)<cosh.lo<cosh.hi<F(2)
    source_pole_coeff=[
       (sinh if n%2==0 else cosh)*((-DELTA/2)**n/math.factorial(n))
       for n in range(J)]
    # Normalized d=delta*t log moment:
    # int_0^1 t^n log(B/(delta*t))dt=h/(n+1)+1/(n+1)^2
    moments=[h/F(n+1)+Iv(F(1,(n+1)**2)) for n in range(K+J-1)]
    m=Iv(0)
    for i in range(K):
        local=Iv(0)
        for j in range(J):
            local+=source_pole_coeff[j]*moments[i+j]
        m+=u[i]*local
    m=m*DELTA
    # S(d)=sinh((B-d)/2), 20-jet source-independent Taylor remainder
    # <=3*(delta/2)^20/20!, since |sinh|,|cosh|<=exp(B/2)<3.
    srem=3*(DELTA/2)**J/math.factorial(J)
    assert F(0)<srem<F(1,10**75)
    # |U|<2e-7 on full original genuine real terminal, exact
    # int_0^delta log(B/d)dd =delta*(log550+1)<8delta.
    moment_err=8*DELTA*(source_tail+F(2,10**7)*srem)
    m=m.pad(moment_err)
    assert F("7.88476182953535359929e-13")<m.lo<=m.hi<F("7.88476182953535359931e-13")
    # Source accepted ORIGINAL selected pole norm in full physical I:
    # ||sinh(x/2)||²= sinh(B)-B, source exact bracket in NF404.
    sinhn=sum((B**(2*n+1)/math.factorial(2*n+1) for n in range(NS)),F(0))
    pole_norm=Iv(sinhn-B,sinhn-B+2*B**(2*NS+1)/math.factorial(2*NS+1))
    original_norm=Iv(F(nf404["original_pole_squared_norm_lower_exact"]),
                     F(nf404["original_pole_squared_norm_upper_exact"]))
    assert pole_norm.contains_overlap(original_norm)
    assert F(".235")<pole_norm.lo<=pole_norm.hi<F(".237")
    assert pole_norm.hi<F(1)
    # Exact source-certified Cc-infinity phi from NF499 is eta-close
    # to ell_U in actual two-collar L2 and ||s||<1.
    eta=F(smooth["two_collar_smoothing_L2_error_strict_upper"])
    assert eta==F(1,10**29)
    mphi=m.pad(eta)
    assert mphi.lo>0
    projected_pole_power=Iv(mphi.lo**2/pole_norm.hi,
                            mphi.hi**2/pole_norm.lo)
    assert F("2.63e-24")<projected_pole_power.lo<=projected_pole_power.hi<F("2.65e-24")
    cap_c=F("2.53e-11")
    pole_fraction_min=projected_pole_power.lo/cap_c**2
    assert pole_fraction_min>F("0.0041")
    # Pythagoras: because s∈original J242, P_Jphi has at least
    # the positive one-dimensional s projection, but we have NOT
    # computed the other 241 source mixed moments.
    output={
      "pass":"NF499-pole",
      "standing":"SOURCE-EXACT first true original selected J242 pole mixed moment of explicit original 246-source smooth Ccinfty J8 log carrier; nonzero original selected overlap and selected projection lower. Remaining 241 selected moments, actual Q_J capture, source multiplier-domain RH OPEN",
      "original_nf407_source_sha256":SRC,
      "original_nf406_seams_sha256":SEAM,
      "original_nf404_full_selected_pole_custody_sha256":sha404,
      "original_nf493_true_400_native_source_json_sha256":sha493,
      "original_nf499_smooth_source_exact_json_sha256":shasmooth,
      "original_selected_J242_index_for_true_sinh_pole":241,
      "original_selected_true_pole_function":"s(x)=sinh(x/2)",
      "original_true_odd_two_collar_pole_log_moment_formula":"<s,ell>=int_0^(1/500) U(B-d)*sinh((B-d)/2)*log(B/d) dd",
      "original_true_source_400_U_coefficients_audited":400,
      "original_TRUE_source_native_retained_U_coefficients":K,
      "original_remaining_290_native_jet_plus_infinite_original_source_tail_exact":str(source_tail),
      "original_exact_rational_log550_atanh_terms_each":NL,
      "original_true_sinh_and_cosh_positive_Taylor_terms_each":NS,
      "original_true_pole_sinh_B_minus_d_over2_Taylor_terms":J,
      "original_source_sinh_Taylor_remainder":str(srem),
      "original_joint_source_pole_log_moment_total_error_fee":str(moment_err),
      "original_true_raw_log_carrier_selected_pole_moment_outward":m.raw(),
      "original_true_raw_log_carrier_selected_pole_moment_decimal":m.decimals(),
      "original_true_smooth_log_carrier_selected_pole_moment_outward":mphi.raw(),
      "original_true_smooth_log_carrier_selected_pole_moment_decimal":mphi.decimals(),
      "original_source_verified_selected_pole_norm_squared_outward":pole_norm.raw(),
      "original_source_verified_smooth_phi_pole_ray_projection_power_outward":projected_pole_power.raw(),
      "original_source_verified_smooth_phi_pole_ray_projection_power_decimal":projected_pole_power.decimals(),
      "original_source_verified_smooth_phi_J242_full_selected_projection_squared_norm_strictly_gt":"2.63e-24",
      "original_source_verified_smooth_phi_pole_selected_capture_fraction_of_phi_squared_norm_strict_gt":"0.0041",
      "original_smooth_phi_is_perpendicular_to_original_J242":False,
      "original_remaining_241_selected_mixed_moments_computed":False,
      "original_true_Q_J_w_against_Q_J_phi_capture_computed":False,
      "original_test_function_source_to_Weil_multiplier_image_eligible_verified":False,
      "W_ODD_NEG":"OPEN","whole_Weil_operator_domain":"OPEN","RH":"OPEN",
      "next_bold":"NF500 compute all remaining 241 original J242 selected mixed moments of this smooth physical phi and source response w, invert authentic selected Gram with 4096bit correlation and certify actual Q_J phi projector capture; independently check Weil source/domain image"
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(output,indent=2)+"\n")
    print("NF499 original true selected J242 pole raw source <s,ell> in",*m.decimals(34),flush=True)
    print("NF499 new smooth phi selected J242 pole mixed moment POSITIVE, pole-ray projection power in",*projected_pole_power.decimals(34),flush=True)
    print("NF499 full source 242D projection includes >2.63e-24 selected pole power, NOT Q_J full capture; W_ODD_NEG/RH OPEN",flush=True)

if __name__=="__main__":
    main()
