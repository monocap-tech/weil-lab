#!/usr/bin/env python3
"""NF498 actual original J8 source-log carrier: rank-one capture & eligibility.

Exact original source arithmetic, no fitted vector: candidate odd
physical L2 endpoint log carrier
  ell(x)=sgn(x) 1_{B-delta<|x|<B} U(|x|)/2 log(B/(B-|x|)).
The full genuine terminal physical response w=p+z has source-accepted
quadratic parts E0, Ecross, Elog from NF495. The one-direction best
L2 capture and residual (restricted to the TWO TRUE terminal collars)
are computed exactly through the 2x2 Gram Schur complement:
  projection=(Elog+Ecross/2)^2/Elog
  remaining=EwT-projection=E0-Ecross^2/(4Elog).

The original NF493 independently certified Elog is cross-checked AFTER
paying the NF495 H400/U400 cutoff/analytic source errors; the raw finite
polynomial Elog source intervals can differ from NF493 due to different
truncations and must NOT be asserted to overlap without their source
remainder charges.

This is NOT the capture of Q_J w by Q_J ell; the original 242D
projections/cross moments remain unmeasured. ell is L2 but not H1, has
a jump at the inner collar, and is not in the original 242 entire
generator source carrier. Thus it is a concrete Hilbert-space
diagnostic, NOT yet an admissible source or source-selected vector.

Rigorous source asymptotics:
  q=Q_J w,  q(B-d)/log(B/d)->v/2,  d*q'(B-d)->v/2 !=0.
Therefore q and ell lie in L2 but not H1 or L-infinity; no finite
extension by bounded entire original-style generators can capture q
EXACTLY. No quantitative NF404 no-go for other smooth approximations
or new projectors follows.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib,sys
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
B=F(11,10);DELTA=F(1,500)

@dataclass(frozen=True)
class I:
    lo:F
    hi:F
    def __post_init__(self):
        assert self.lo<=self.hi
    @staticmethod
    def frompair(p):return I(F(p[0]),F(p[1]))
    @staticmethod
    def scalar(x):
        x=F(x);return I(x,x)
    def __add__(self,o):
        if not isinstance(o,I):o=I.scalar(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+(-o if isinstance(o,I) else -F(o))
    def __mul__(self,o):
        if not isinstance(o,I):o=I.scalar(o)
        xs=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(xs),max(xs))
    __rmul__=__mul__
    def __truediv__(self,o):
        if not isinstance(o,I):o=I.scalar(o)
        assert o.lo>0 or o.hi<0
        return self*I(F(1)/o.hi,F(1)/o.lo)
    def sq(self):
        if self.lo>=0:return I(self.lo**2,self.hi**2)
        if self.hi<=0:return I(self.hi**2,self.lo**2)
        return I(F(0),max(self.lo**2,self.hi**2))
    def pad(self,e):
        e=F(e);assert e>=0
        return I(self.lo-e,self.hi+e)
    def intersect(self,o):return self.lo<=o.hi and o.lo<=self.hi
    def raw(self):return [str(self.lo),str(self.hi)]
    def decimal(self,n=44):
        from decimal import Decimal,localcontext
        with localcontext() as ctx:
            ctx.prec=n+10
            vals=[Decimal(t.numerator)/Decimal(t.denominator) for t in (self.lo,self.hi)]
            return [format(+v,f".{n-1}E") for v in vals]

def load(p):
    b=Path(p).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()

def positive_gram_controls():
    # The first term is a direct regular source vector A, the second
    # is the logarithmic carrier C, and full response is A+C.
    cases=[
       ((F(1),F(2)),(F(2),F(-1))),
       ((F(3),F(-1)),(F(-1),F(0))),
       ((F(-3),F(4)),(F(2),F(-5))),
       ((F(0),F(0)),(F(1),F(1))),
       ((F(13,37),F(-29,41)),(F(31,43),F(7,47))),
       ((F(-1,10**15),F(1,10**12)),(F(1,10**8),F(-1,10**10))),
       ((F(2),F(3)),(F(4),F(6))),
       ((F(-5),F(4)),(F(-10),F(8)))
    ]
    for a,c in cases:
        e0=sum((x*x for x in a),F(0))
        el=sum((x*x for x in c),F(0))
        cross=2*sum((x*y for x,y in zip(a,c)),F(0))
        whole=e0+cross+el
        assert el>0
        captured=(el+cross/2)**2/el
        resid=whole-captured
        assert resid==e0-cross**2/(4*el)>=0
        assert captured>=0
        assert captured+resid==whole
    return len(cases)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--nf495-raw",required=True)
    ap.add_argument("--nf493-raw",required=True)
    ap.add_argument("--nf496-raw",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()

    nf495,sha495=load(args.nf495_raw)
    nf493,sha493=load(args.nf493_raw)
    nf496,sha496=load(args.nf496_raw)
    original,sha407=load("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,sha406=load("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    nf411,sha411=load("notes/data/provisional/NF411_original_source_boundary_jet.json")
    nf404,sha404=load("notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
    assert sha407==SRC and sha406==SEAM
    assert nf495["pass"]=="NF494" and nf493["pass"]=="NF493" and nf496["pass"]=="NF496"
    assert nf495["original_nf407_source_sha256"]==nf493["original_nf407_source_sha256"]==SRC
    assert nf495["original_nf406_seams_sha256"]==nf493["original_nf406_seams_sha256"]==SEAM
    assert nf496["original_nf407_immutable_source_SHA256"]==SRC
    assert nf496["original_nf406_immutable_seam_SHA256"]==SEAM
    assert nf495["original_full_J8_D8_signed_upper_numerically_integrated"]
    assert nf495["NF404_original_selected_source_scalar_decision"]=="NF404_SOURCE_SCALAR_CERTAIN_FAIL"
    assert nf496["original_NF404_selected_sufficient_complement_gate"]=="CERTIFIED FAIL"
    assert nf493["original_true_source_4096bit_400_jet_coefficients_verified"]==400
    assert nf493["original_true_log_source_coefficient"]=="U(B-d)/2"
    assert nf411["nf407_source_sha256"]==SRC
    assert nf404["original_dimension"]==242 and nf404["original_selected_pole_index"]==241
    assert nf404["fixed_dyadic_pole_coefficient"]=="6677356497477490213/4611686018427387904"
    basis=original["original_selected_generator_node_orders"]
    assert len(basis)==242 and basis[241]==["pole",None]
    assert all((f=="pole" and k is None) or
               (f!="pole" and F(0)<F(f)<883 and isinstance(k,int) and 0<=k<=13)
               for f,k in basis)
    assert len(original["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(original["original_source_critical_sine_frequencies"])==32
    assert original["original_dimension"]==242

    # Exact original full true signed physical source endpoint, unchanged:
    s=nf411["original_original_source_value_at_B_arb"]
    assert s.startswith("[") and s.endswith("]")
    mid,rad=s[1:-1].split(" +/- ")
    v=I(F(mid)-F(rad),F(mid)+F(rad))
    assert F("-1.17e-11")<v.lo<v.hi<F("-1.16e-11")
    assert v.hi<0
    assert F("1.16e-11")<(-v).lo<(-v).hi<F("1.17e-11")
    assert nf411["source_derivative_nonzero_certified"]
    endpoint_log_coeff=v/2
    collar_asymptotic_norm_coefficient=v.sq()/2
    assert endpoint_log_coeff.hi<0 and collar_asymptotic_norm_coefficient.lo>0
    assert positive_gram_controls()==8

    # *Every* source subcomponent from original NF495 native 400 H/U:
    E0=I.frompair(nf495["original_original_full_terminal_Hplus_vC8_square_component"])
    Ex=I.frompair(nf495["original_original_full_terminal_cross_HUlog_signed_component"])
    El=I.frompair(nf495["original_original_full_terminal_Ulog_square_component"])
    Ew=I.frompair(nf495["original_complete_J8_true_improper_whole_terminal_positive_square_EwT_outward"])
    assert E0.lo>0 and Ex.hi<0 and El.lo>0 and Ew.lo>0
    assert nf495["true_original_J8_terminal_delta"]=="1/500"
    assert nf495["original_true_same_source_joint_normalized_coeff_retained_count"]==102
    # The NF495 returned component intervals refer to its finite
    # polynomial; rigorous original 400-jet Cauchy and a posteriori
    # finite cutoff errors must be allocated to EACH component.
    ma=F(nf495["original_full_numeric_Hplus_vC8_normalized_l1_envelope"])
    mc=F(nf495["original_full_numeric_U_over2_normalized_l1_envelope"])
    ta=F(nf495["original_full_H400_remaining_source_normalized_l1"])
    tc=F(nf495["original_full_U400_remaining_source_normalized_l1"])
    EH=F(nf495["original_complete_H400_original_source_Cauchy_tail"])
    EU=F(nf495["original_complete_U400_original_source_Cauchy_tail"])
    original_joint_fee=F(nf495["original_joint_whole_square_finite_400_jet_cutoff_error"])
    ea=ta+EH;ec=tc+EU/2
    assert 0<ea<F(1,10**60) and 0<ec<F(1,10**60)
    assert 0<ma+mc<F(1,10**5)
    e0fee=DELTA*(2*ma*ea+ea**2)
    exfee=16*DELTA*(ma*ec+mc*ea+ea*ec)
    elfee=65*DELTA*(2*mc*ec+ec**2)
    assert e0fee+exfee+elfee<original_joint_fee
    # Pay EACH physical original source-polynomial remainder before
    # comparing with the DIFFERENT NF493 source-contracted cutoff.
    E0=E0.pad(e0fee);Ex=Ex.pad(exfee);El=El.pad(elfee)
    Ei=I.frompair(nf493["original_true_Ulog_square_numeric_interval_outward"])
    assert El.intersect(Ei),(
       "METHOD STOP: source NF495 and independent NF493 real Elog nonoverlap AFTER analytic cutoff charge")
    assert (E0+Ex+El).intersect(Ew)
    assert E0.lo>0 and Ex.hi<0 and El.lo>0

    # ORIGINAL physical L2 diagnostic log carrier on BOTH true
    # terminal collars (odd extension), NOT projector orthogonalized:
    # ||ell||^2 =2 Elog;
    # <w,ell> = 2*(Elog+Ex/2)
    # projection of w onto span(ell) on BOTH collars is
    # 2*(Elog+Ex/2)^2/Elog, while whole w two-collar norm²=2Ew.
    inner=El+Ex/2
    assert inner.hi<0
    opt_scalar=inner/El
    captured=inner.sq()/El
    remainder=Ew-captured
    # Independent exact Schur identity and PSD Gram check.
    schur=E0-Ex.sq()/(4*El)
    assert remainder.intersect(schur)
    assert schur.lo>0 and remainder.lo>0
    assert (E0*El-Ex.sq()/4).lo>0
    fraction=captured/Ew
    residual_fraction=remainder/Ew
    assert F("-0.432545")<opt_scalar.lo<=opt_scalar.hi<F("-0.432543")
    assert F("5.9853e-23")<captured.lo<=captured.hi<F("5.9854e-23")
    assert F("1.15866e-22")<remainder.lo<=remainder.hi<F("1.15867e-22")
    assert F("0.34061")<fraction.lo<=fraction.hi<F("0.34063")
    assert F("0.65937")<residual_fraction.lo<=residual_fraction.hi<F("0.65939")

    q_lower=F(nf496["original_J242_perpendicular_squared_norm_STRICT_lower"])
    gamma2=F(nf496["original_NF403_NF404_exact_gamma_squared_budget"])
    assert q_lower==F("1.57806e-22") and gamma2<F("5.13e-26")
    # Pure log carrier terminal scalar capture is NOT equal to
    # projection of full q=Q_Jw onto e=Q_J ell. No mathematical
    # comparison to the NF496 gamma threshold is made.
    assert (2*El).lo>0 and (2*inner).hi<0

    result={
      "pass":"NF498",
      "standing":"SOURCE-EXACT genuine ORIGINAL full 246-source terminal Hilbert endpoint-log carrier rank-one physical L2 pilot and intrinsic H1/domain eligibility STOP; Q_J carrier projector coupling UNMEASURED; no new RH theorem",
      "original_nf407_source_sha256":SRC,
      "original_nf406_seams_sha256":SEAM,
      "original_nf411_4096bit_endpoint_custody_sha256":sha411,
      "original_nf404_selected_242_analytic_generator_custody_sha256":sha404,
      "original_nf495_complete_true_physical_J8_raw_source_sha256":sha495,
      "original_nf493_independent_Ulog_square_raw_source_sha256":sha493,
      "original_nf496_entire_J242_complement_raw_source_sha256":sha496,
      "original_source_selected_dimension":242,
      "original_selected_authentic_odd_sinh_pole_index":241,
      "original_true_J8_terminal_delta":"1/500",
      "original_complete_true_source_U_B_outward":v.raw(),
      "original_Q_J_w_endpoint_log_leading_coefficient_v_over2_outward":endpoint_log_coeff.raw(),
      "original_Q_J_w_endpoint_q_over_log_limit_equals_v_over2":True,
      "original_Q_J_w_endpoint_d_times_q_prime_limit_equals_v_over2":True,
      "original_Q_J_w_is_L2_but_unbounded_and_not_H1":True,
      "original_any_finite_entire_selected_source_enlargement_captures_q_exactly":False,
      "original_odd_log_carrier_definition":"ell(x)=sgn(x)*1_{B-1/500<abs(x)<B}*U(abs(x))/2*log(B/(B-abs(x)))",
      "original_odd_log_carrier_true_L2_but_not_H1":True,
      "original_odd_log_carrier_full_two_collar_norm_squared_outward":(2*El).raw(),
      "original_odd_log_carrier_full_two_collar_inner_with_w_outward":(2*inner).raw(),
      "original_log_only_one_collar_true_Elog_outward":El.raw(),
      "original_source_400_source_Elog_independent_NF493_overlap_after_fees":True,
      "original_true_full_J8_terminal_Ew_outward":Ew.raw(),
      "original_one_collar_E0_true_source_component":E0.raw(),
      "original_one_collar_cross_true_source_component":Ex.raw(),
      "original_each_component_analytic_and_cutoff_errors":[str(e0fee),str(exfee),str(elfee)],
      "original_raw_nf495_whole_square_source_cutoff_error":str(original_joint_fee),
      "original_optimal_scalar_on_raw_log_carrier_full_two_collar_outward":opt_scalar.raw(),
      "original_optimal_scalar_on_raw_log_carrier_decimal":opt_scalar.decimal(40),
      "original_terminal_one_collar_optimal_raw_log_carrier_captured_power_outward":captured.raw(),
      "original_terminal_one_collar_optimal_raw_log_carrier_captured_power_decimal":captured.decimal(44),
      "original_terminal_one_collar_raw_log_carrier_orthogonal_residual_power_outward":remainder.raw(),
      "original_terminal_one_collar_raw_log_carrier_orthogonal_residual_power_decimal":remainder.decimal(44),
      "original_terminal_raw_log_carrier_one_rank_capture_fraction_outward":fraction.raw(),
      "original_terminal_raw_log_carrier_one_rank_capture_fraction_decimal":fraction.decimal(40),
      "original_terminal_raw_log_carrier_one_rank_residual_fraction_outward":residual_fraction.raw(),
      "original_true_l2_gram_Schur_residual_source_positive":True,
      "original_true_selected_Q_J_log_template_source_coupling_computed":False,
      "original_new_endpoint_log_template_is_admissible_Weil_test_source":"NOT_ESTABLISHED",
      "original_new_endpoint_log_template_belongs_to_smooth_test_source_class":False,
      "original_new_endpoint_log_template_Weil_operator_domain_verified":False,
      "original_NF496_same_original_J242_gamma_residual_requirement_remains":True,
      "original_any_smooth_new_source_outside_current_242_generator_family_ruled_out":False,
      "NF404_original_fixed_selected_sufficient_certificate":"CERTIFIED FAIL",
      "W_ODD_NEG":"OPEN","whole_Weil_operator_domain":"OPEN","RH":"OPEN",
      "next_bold":"NF499 construct source-eligible smooth log-carrier regularization and certify full original J242-orthogonal moment <q,Qell>, ||Qell||²; only then compare genuine Q-capture to 99.96749% threshold"
    }
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2)+"\n")
    print("NF498 ACTUAL original J8 log-only explicit carrier optimal scalar",*opt_scalar.decimal(30),flush=True)
    print("NF498 genuine original two-collar rank-one terminal capture %",*[float(x*100) for x in (fraction.lo,fraction.hi)],flush=True)
    print("NF498 genuine one-collar residual after optimal raw log-carrier",*[float(x) for x in (remainder.lo,remainder.hi)],flush=True)
    print("NF498 source log-carrier and q are L2, NOT H1; true Q_J candidate coupling NOT computed, RH OPEN",flush=True)

if __name__=="__main__":
    main()
