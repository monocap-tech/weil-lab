#!/usr/bin/env python3
"""NF480 exact original J8 endpoint-renormalized complete-source high-image audit.

Source contract: immutable NF407 246 generators / 273 grouped modes, original
NF406 n9 support, *native original* NF477 4096-bit 360 source-contracted
inverse-a jets and exact positive binomial resolvent remainder.

T_m = sum_(n>=0) mu_n/a_m^(n+1), a_m=m+1/4,
mu_0=v=U(B), mu_n=U^(n)(B)/2^n, m>=M=18000.

Extract mu_0 ... mu_11 as exact SOURCE-SHARED Arb interval coefficient
functions, not as independent unmeasured errors. Original mu_0/a_m image
series is summed analytically and cancels the explicit original -v/2 log
singularity. The n>=1 functions have uniformly absolutely convergent
Laplace series at the real J8 B endpoint.

The 12-jet residual is source-certified in L2 on entire real ORIGINAL J8,
including x=B, and on its odd-reflected counterpart. It is NOT yet an
evaluated whole original J8 signed D8 upper or NF404 scalar PASS.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from decimal import Decimal,localcontext
import argparse,json,hashlib,sys
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/"notes/data/provisional"
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
NF477_RUN=42436964916
NF477_NATIVE_SHA="54442a3c342c4b2b31e912cd910fcce952198519ee3b8065a842a317283d5aee"
M=18000
N=360
B=F(11,10)
def dec(x,digits=45):
    with localcontext() as c:
        c.prec=digits
        return str(Decimal(x.numerator)/Decimal(x.denominator))
def pos_abs_lower(it):
    a,b=map(F,it)
    assert a<=b
    return min(abs(a),abs(b)) if (a>0 or b<0) else F(0)
def pos_abs_upper(it):
    a,b=map(F,it)
    assert a<=b
    return max(abs(a),abs(b))
def load(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--nf477-original-native-raw",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    d,h=load(args.nf477_original_native_raw)
    prev,_=load(DATA/"NF477_original_J7_correlated_resolvent_high_image_tail_custody.json")
    seam,_=load(DATA/"NF406_original_prime_support_partition_exact.json")
    source,_=load(DATA/"NF407_original_fourth_physical_coefficients_native.json")
    nf479,_=load(DATA/"NF479_original_full_J8_forced_positive_NF404_transfer_custody.json")
    assert d["pass"]=="NF477" and d["native_precision_bits"]==4096
    assert h==NF477_NATIVE_SHA==prev["raw_native_source_artifact"]["raw_sha256"]
    assert d["original_nf407_sha256"]==SRC and d["original_nf406_sha256"]==SEAM
    assert d["original_246_generators"] and d["original_273_modes"] and d["original_99_frequency_groups"] and d["original_odd_sinh_pole"]
    assert prev["source_sha256"]==SRC and prev["seam_sha256"]==SEAM
    assert prev["independent_exact_fraction_ci"]["status"]=="SUCCESS"
    assert source["original_dimension"]==242
    assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
    assert len(source["original_source_critical_sine_frequencies"])==32
    assert nf479["original_nf407_source_sha256"]==SRC and nf479["original_nf406_seams_sha256"]==SEAM
    assert nf479["original_full_J8_signed_sign"].startswith("STRICT POSITIVE")
    assert d["source_resolvent_lower_m"]==M and d["source_resolvent_contracted_order"]==N
    assert d["genuine_original_source_input_radius_lt"]=="1e-700"
    jets=d["original_first_twelve_source_jets_outward"]
    assert len(jets)==12
    leading=F(d["post_contraction_original_360_jet_absolute_sum"])
    original_remainder=F(d["exact_absolute_binomial_remainder"])
    assert F(0)<original_remainder<F(1,10**130)
    # Each source-native mu_j ball already encloses the ORIGINAL dyadic
    # NF407 coefficient uncertainties. The original absolute 360-jet total
    # was computed from full Arb original source, NOT midpoint coefficients.
    # The binomial remainder source envelope 1e160 also includes them.
    # Therefore a separate unscaled delta(mu_0)/m term must NOT be added:
    # it belongs to the exact analytically resummed shared mu_0=U(B).
    assert F(d["source_uniform_all_m_amplitude_bound"]) >= leading+original_remainder
    assert pos_abs_lower(jets[0])>0
    # Audit conservative source-native first jets and all-360 total.
    assert pos_abs_lower(jets[0])<pos_abs_upper(jets[0])
    spent=F(0)
    witnesses=[]
    for k in range(1,13):
        j=k-1
        spent+=pos_abs_lower(jets[j])/M**k
        c_k=leading-spent+original_remainder
        assert c_k>0,("invalid source contracted jet subtraction",k,str(c_k))
        # Original source exact Laurent/resolvent remainder is an absolutely
        # convergent series of powers m^-(n+1), n>=N, with positive
        # coefficient majorant. Thus after extracting k<=12 jets EVERY
        # residual term has m-decay at least (M/(m+1/4))^(k+1).
        #
        # F_m(x)=exp(-2a_m(B-x))-exp(-2a_m(B+x)).
        # On positive x∈J8, 0<=F_m(x)<=exp(-2m(B-x)).
        # ∑(M/m)^(k+1) <= 1+M/k by the integral test.
        U_k=c_k*(1+F(M,k))/2
        # B-x=d∈[0,2B-log9]. Integrate over a LARGER halfline d>=0.
        L1_k=U_k/F(2*M)
        L2sq_k=U_k**2/F(4*M)
        # sqrt(M)>134 and sqrt(2M)>189. These root-free upper
        # enclosures are conservative for respectively positive J8 and
        # the two reflected physical J8 halves.
        assert 134**2<M and 189**2<2*M
        L2positive_rootfree=U_k/F(268)
        L2two_rootfree=U_k/F(189)
        witnesses.append({
          "source_extracted_jets":k,
          "original_laurent_tail_weight_at_M":str(c_k),
          "original_maximal_residual_envelope_Uk":str(U_k),
          "original_maximal_residual_envelope_Uk_decimal":dec(U_k),
          "original_J8_positive_L1_upper":str(L1_k),
          "original_J8_positive_L2_squared_upper":str(L2sq_k),
          "original_J8_positive_L2_rootfree_upper":str(L2positive_rootfree),
          "original_reflected_both_J8_L2_rootfree_upper":str(L2two_rootfree),
          "original_J8_positive_L2_under_1e_minus26":L2positive_rootfree<F(1,10**26)
        })
        if k>=2:
            assert F(witnesses[-1]["original_J8_positive_L2_rootfree_upper"]) < F(witnesses[-2]["original_J8_positive_L2_rootfree_upper"])
    assert not witnesses[-2]["original_J8_positive_L2_under_1e_minus26"]
    assert witnesses[-1]["original_J8_positive_L2_under_1e_minus26"]
    tail=witnesses[-1]
    U=F(tail["original_maximal_residual_envelope_Uk"])
    Eplus=F(tail["original_J8_positive_L2_rootfree_upper"])
    Epair=F(tail["original_reflected_both_J8_L2_rootfree_upper"])
    assert U<F("2.23e-24")
    assert Eplus<F("8.33e-27")
    assert Epair<F("1.18e-26")
    # Conditional energy perturbation: if later original finite-18000 +
    # exact H + 11 Lerch-jet comparator has ||g_12||_L2(I) <=4e-11, then
    # ||g||² differs from ||g_12||² by <=2||g_12||epsilon+epsilon².
    # The comparator's norm upper is NOT certified by this pass.
    energy_conditional=2*F(4,10**11)*Epair+Epair**2
    assert energy_conditional<F(1,10**36)
    # The former J7 entire-cell exponential gap d>=11/4000 is unavailable
    # in ORIGINAL J8 since B-x actually reaches zero. This is why the
    # original principal/exact H resummation is non-optional.
    assert prev["original_both_endpoint_image_tail_lt_1e_minus_40"]
    out={
      "pass":"NF480",
      "standing":"SOURCE + EXACT FRACTION ACCEPTED genuine entire J8 endpoint-renormalized original 12-jet source-correlated high-image residual L2, NOT J8 signed integral or NF404 cap",
      "original_nf407_source_sha256":SRC,
      "original_nf406_seams_sha256":SEAM,
      "original_nf477_4096bit_native_source_sha256":h,
      "original_nf477_4096bit_source_CI_run":NF477_RUN,
      "source_native_273_mode_360_jet_total":str(leading),
      "source_native_360_jet_exact_binomial_remainder":str(original_remainder),
      "original_source_midpoint_and_dyadic_interval_inputs":"ALL included in original Arb mu_j and raw 1e160 resolvent envelope, NOT new surrogate midpoints",
      "original_sinh_pole":"PRESERVED in original full source mu_j",
      "original_true_J8_physical_interval":["log9-B","B"],
      "original_odd_reflection":"original negative J8 is the odd reflected positive physical source",
      "source_original_pole_cancelation":"mu_0=v=U(B); exact original H(d)=sum_m exp(-2(m+1/4)d)/(m+1/4) cancels the -v/2 log(B/d) in complete original z",
      "source_original_H_d_exact":"log(coth(d/4))+2atan(exp(-d/2))",
      "source_original_H_d_limit":"H(d)+log(d)->log(4)+pi/2 as d->0",
      "residual_definition":"(1/2)*sum_{m>=18000}[T_m-sum_{n=0}^{11}mu_n/(m+1/4)^(n+1)]*(exp(-2a_m(B-x))-exp(-2a_m(B+x)))",
      "extracted_original_jet_moment_functions":"n=1..11, Phi_n(d)=sum_{m>=18000}[exp(-2a_m d)-exp(-2a_m(2B-d))]/a_m^(n+1); continuous to d=0, no sampling",
      "source_resolvent_M":M,"source_contracted_resolvent_order":N,
      "source_jet_extraction_sweep":witnesses,
      "first_jet_count_with_original_J8_positive_L2_below_1e_minus26":12,
      "original_J8_positive_uniform_envelope":"U12*exp(-36000*(B-x))",
      "original_J8_positive_uniform_U12_outward_decimal":dec(U),
      "original_J8_positive_L1_residual_upper_decimal":dec(F(tail["original_J8_positive_L1_upper"])),
      "original_J8_positive_L2_residual_rootfree_upper_decimal":dec(Eplus),
      "original_J8_reflected_both_sides_L2_residual_rootfree_upper_decimal":dec(Epair),
      "conditional_comparator_full_L2_upper_for_energy_charge":"4e-11 (NOT established in NF480)",
      "conditional_energy_charge_if_comparator_L2_lt_4e_minus11":str(energy_conditional),
      "conditional_energy_charge_lt_1e_minus36":True,
      "NF479_original_full_J8_signed_positive_inferred":True,
      "actual_original_J8_signed_full_integral_upper":"OPEN",
      "original_full_NF404_centered_scalar_certified":"OPEN",
      "W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF481 compute source-correlated finite original J8 18000 matched images plus analytic H/d-log cancellation and eleven exact Lerch moment functions; enclose actual J8 signed D8 or directly Efull with coupled <=3.31e-26 tolerance"
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2)+"\n")
    print("NF480 verified native original J7->J8 endpoint-renormalized 12-jet transfer",flush=True)
    print("NF480 original J8 residual uniform U12",dec(U),flush=True)
    print("NF480 original J8 residual positive L2",dec(Eplus),flush=True)
    print("NF480 original J8 residual BOTH odd physical halves L2",dec(Epair),flush=True)
    print("NF480 conditional energy fee if later finite comparator <4e-11",dec(energy_conditional),flush=True)
    print("NF480 full ORIGINAL J8 signed numeric upper NF404 W-ODD-NEG RH OPEN",flush=True)

if __name__=="__main__":main()
