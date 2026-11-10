#!/usr/bin/env python3
"""NF493 INDEPENDENT exact-Fraction original genuine U-log-squared energy.

From 400 native outward original NF407 source U(B-d) 4096bit coefficient
balls, compute first genuine nonnegative component in the FULL original
NF491 physical J8 bulk positive square:
   E_Ulog = 1/4 ∫_0^(1/500) U(B-d)^2 log(B/d)^2 dd.
This is one *component*, not the whole (p+z)^2; cross components MUST
be calculated from SAME source before an NF404 acceptance claim.

No floating input, no guessed mesh, no original coefficient changes.
All original dyadic source input errors, 400-jet Cauchy tail and
improper log550 atanh interval are charged rigorously. An independent
direct polynomial/log moment contraction is also tested.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,sys,argparse,math
from verify_nf488_original_J8_terminal_four_moment_source_gate_exact import Iv,log550
from verify_nf492_original_J8_all_orders_log_peel_400jet_exact import positive_square_polynomial_exact_controls
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);DELTA=F(1,500);R=F(1,25)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def maxabs(x):
    return max(abs(x.lo),abs(x.hi))
def ov(a,b):
    return a.lo<=b.hi and b.lo<=a.hi
def log_weight(j,h):
    """Exact positive log^2 moment on d=delta*t, t∈[0,1]."""
    q=F(j+1)
    return (h**2+(F(2)/q)*h+F(2,q*q))/q
def fractional_polynomial_energy(coeff,h):
    """Entire genuine original U_SOURCE polynomial, signed Q-correlation."""
    n=len(coeff)
    moment=[log_weight(j,h) for j in range(2*n-1)]
    out=Iv(0)
    for j in range(n):
        for k in range(j,n):
            out+=coeff[j]*coeff[k]*moment[j+k]*(2 if j!=k else 1)
    return DELTA*out/4
def diagnostic_algebra_controls():
    """Independent EXACT pure rational toy source, direct power vs convolution."""
    tests=[
      [F(-1,11),F(1,13),F(-5,17)],
      [F(0),F(0),F(3,41),F(-2,71)],
      [F(-11,97),F(-1,101)],
      [F(1,10**7),F(-3,10**9),F(5,10**11),F(-7,10**13)],
      [F(-2),F(1),F(-2),F(1),F(-2)],
      [F(0),F(0),F(0),F(0),F(0),F(1,1009)],
      [F(1,83)],
      [F(0),F(0),F(13,89),F(17,97),F(-19,101),F(-23,103)]
    ]
    h=F(7,3)
    for u in tests:
        direct=F(0)
        for i,a in enumerate(u):
            for j,b in enumerate(u):
                direct+=a*b*log_weight(i+j,h)
        poly=[F(0)]*(len(u)*2-1)
        for i,a in enumerate(u):
            for j,b in enumerate(u):poly[i+j]+=a*b
        via=sum((c*log_weight(i,h) for i,c in enumerate(poly)),F(0))
        assert direct==via
        # A separate exact rational endpoint-suppressed weighted
        # value at δ from full complete source polynomial.
        assert sum(u,F(0))**2==sum(poly,F(0))
    return len(tests)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--native",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    nat,nsha=read(args.native)
    source,ssh=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,ksha=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    jet,jsha=read("notes/data/provisional/NF411_original_source_boundary_jet.json")
    curv,csha=read("notes/data/provisional/NF413_original_full_246_source_curvature_native.json")
    prior,nf492sha=read("notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    assert ssh==nat["original_nf407_source_sha256"]==SRC
    assert ksha==nat["original_nf406_seams_sha256"]==SEAM
    assert jet["nf407_source_sha256"]==curv["original_nf407_full_native_source_sha256"]==prior["source_SHA256"]==SRC
    assert nat["pass"]=="NF493-original-source-400-log-jets"
    assert nat["original_native_precision_bits"]==4096
    assert nat["original_selected_generators"]==242 and nat["original_critical_generators"]==4
    assert nat["original_grouped_source_modes"]==273 and nat["original_critical_sine_frequencies"]==32
    assert nat["original_full_odd_sinh_pole_preserved"]
    assert nat["original_source_400_taylor_direct_overlap"]
    assert nat["original_real_original_U_dyadic_coefficient_ball_first_400"] and len(nat["original_real_original_U_dyadic_coefficient_ball_first_400"])==400
    assert nat["original_source_input_complete_complex_sup_fee"]=="1e-450"
    assert nat["original_source_input_added_each_taylor_jet"]=="1e-450*25**n"
    assert F(nat["original_source_native_dyadic_midpoint_radii_sum_exact"])<F(1,10**700)
    assert nat["original_J8_terminal_delta"]=="1/500"
    assert nat["original_analytic_fixed_branch_Cauchy_radius"]=="1/25"
    assert nat["original_real_terminal_ratio"]=="1/20"
    assert nat["original_source_log_u_taylor_degree"]=="399"
    assert nat["original_true_log_source_coefficient"]=="U(B-d)/2"
    assert not nat["original_400_H_analytic_coefficients_numerically_computed"]
    assert not nat["original_complete_original_Ew_bulk_numerically_certified"]
    assert nat["original_full_J8_D8_signed_UPPER"]==nat["NF404"]==nat["W_ODD_NEG"]==nat["RH"]=="OPEN"
    intervals=[Iv(*map(F,pair)) for pair in nat["original_real_original_U_dyadic_coefficient_ball_first_400"]]
    v=Iv(*map(F,jet["original_original_source_value_at_B_arb"].replace("[","").replace("]","").split(" +/- "))) if False else None
    from verify_nf488_original_J8_terminal_four_moment_source_gate_exact import arb_ball
    v=arb_ball(jet["original_original_source_value_at_B_arb"])
    u0=intervals[0]
    assert ov(u0,v)
    assert u0.hi<0
    d1=arb_ball(jet["original_original_source_derivative_at_B_arb"])
    assert ov(-intervals[1],d1)
    assert intervals[1].lo>0
    assert -F(1,1000)<2*intervals[2].lo<2*intervals[2].hi<0
    source_B_delta=Iv(*map(F,nat["original_source_4096bit_U_at_B_minus_delta_outward"]))
    assert source_B_delta.lo>0
    assert source_B_delta.width()<F(1,10**40)
    coeff=[]
    d_power=F(1)
    for i,c in enumerate(intervals):
        coeff.append(c*d_power)   # normalized t=d/delta
        d_power*=DELTA
    nativepoint=sum(coeff,Iv(0))
    tail=F(nat["original_source_400_taylor_analytic_Cauchy_abs_tail"])
    assert tail<F(1,10**119)
    assert ov(nativepoint+Iv(-tail,tail),source_B_delta)
    assert nativepoint.lo>0
    # Degree cutoff is selected ONLY from all 400 complete same-source
    # normalized original coefficient intervals, not guessed frequency
    # falloff nor a falsely uniform original source derivative bound.
    abscoeff=list(map(maxabs,coeff))
    total_abs=sum(abscoeff,F(0))
    assert total_abs<F(10)**20, "METHOD STOP: actual source polynomial abs envelope too loose"
    tails=[F(0)]*401
    for n in range(399,-1,-1):
        tails[n]=tails[n+1]+abscoeff[n]
    cutoff=next((k for k in range(1,401) if tails[k]<F(1,10**75)),400)
    neglected=tails[cutoff]
    assert neglected<=total_abs
    h=log550()
    assert F(6)<h.lo<=h.hi<F(7)
    assert h.width()<F(1,10**90)
    moment2=DELTA*log_weight(0,h)
    assert moment2.hi<65*DELTA
    print("NF493 source-exact 400 physical U coefficients, chosen independent signed source cutoff",cutoff,flush=True)
    print("NF493 original source 400 abs normalized envelope, neglected 400-jet component tail",float(total_abs),float(neglected),flush=True)
    # Independent exact rational original source polynomial-square log
    # contraction after joint original 246-generator source summation.
    partial=fractional_polynomial_energy(coeff[:cutoff],h)
    scalar_error=(2*total_abs*(neglected+tail)+(neglected+tail)**2)*moment2.hi/F(4)
    true=partial+Iv(-scalar_error,scalar_error)
    assert true.lo>0,"METHOD STOP: actual original pure log square not certified positive"
    assert true.width()<F(1,10**26),"METHOD STOP: first genuine source square component too loose"
    assert true.hi<F(1,100),"original genuine physical source log-square magnitude unreasonable"
    assert diagnostic_algebra_controls()==8
    assert positive_square_polynomial_exact_controls()>30
    result={
      "pass":"NF493",
      "standing":"SOURCE-EXACT ORIGINAL all 400 original U(B-d) 4096-bit original 246-generator joint coefficients and FIRST ACTUAL pure original full-J8 physical logarithmic-square component, not whole w=p+z or Ew_bulk",
      "original_nf407_source_sha256":SRC,
      "original_nf406_seams_sha256":SEAM,
      "original_native_source_json_sha256":nsha,
      "original_nf411_endpoint_native_source_sha256":jsha,
      "original_nf413_full_source_curvature_sha256":csha,
      "original_original_nf450_complete_zB_source_sha256":nf492sha,
      "original_true_source_4096bit_400_jet_coefficients_verified":400,
      "original_true_log_source_coefficient":"U(B-d)/2",
      "original_source_first_log_uB_interval":u0.raw(),
      "original_source_true_U_at_B_minus_delta_interval":source_B_delta.raw(),
      "original_source_U400_at_B_minus_delta_interval":nativepoint.raw(),
      "original_source_uniform_400_coeff_analytic_remainder":str(tail),
      "original_actual_normalized_400_coeff_l1_envelope":str(total_abs),
      "original_exact_integrated_log_square_selected_jet_count":cutoff,
      "original_source_remaining_normalized_400_jet_l1_tail":str(neglected),
      "original_source_actual_original_uniform_U_polynomial_plus_analytic_tail_error":str(neglected+tail),
      "original_true_improper_original_0_to_1over500_log_square_moment_upper":str(moment2.hi),
      "original_true_Ulog_square_numeric_interval_outward":true.raw(),
      "original_true_Ulog_square_numeric_interval_decimal":true.decimal(45),
      "original_true_Ulog_square_interval_width_decimal":true.width().__str__(),
      "original_true_full_physical_square_one_source_loglog_component":"E_log = (1/4)int_0^(1/500) U(B-d)^2 log(B/d)^2 dd",
      "independent_exact_signed_source_polynomial_log_controls":8,
      "independent_NF492_positive_square_algebra_controls":True,
      "original_full_400_analytic_H_source_jets_numerical":"OPEN",
      "original_complete_true_positive_Ew_bulk":"OPEN",
      "original_J8_signed_D8_upper":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF494 evaluate actual original source-correlated H_400 analytic coefficients and both H² and H·U logarithmic cross terms; add this accepted pure U² L² source component without breaking source covariance"
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(result,indent=2)+"\n")
    print("NF493 original genuine one pure U(B-d)^2/4*log(B/d)^2 source component EXACT Fraction ACCEPT",*true.decimal(45),flush=True)
    print("NF493 true full source physical Ew_T/Ew_bulk uncomputed; original D8 upper/NF404/RH OPEN",flush=True)
if __name__=="__main__":main()
