#!/usr/bin/env python3
"""NF494 independent exact-Fraction original J8 TOTAL PHYSICAL positive square.

Consumes actual source-native 4096-bit 400 original NF407 full-compact
H(d) and full U(B-d) coefficient intervals. No image-only shadows, no
pointwise mesh, no independent absolute giant mode norms.

Ew_T = int_0^(1/500) [H(d)+v*C8+U(B-d)/2*log(B/d)]² dd
is evaluated from ONE jointly source-contracted original-source
polynomial×log square. Accepted NF492 real analytic Cauchy tail
<1e-96, native source input, all 400 finite coefficients, and true
improper log550 source exact atanh are all paid.

Independently audit genuine NF493 source U400 coefficient artifact,
NF492 independently original physical H(1/500) point, NF491 original
positive square bulk gates and last collar, NF483 principal and NF482
first n9-irrational panel. This may certify a full J8 scalar if and
ONLY if the original full numeric error interval passes its gates.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json,sys
from verify_nf488_original_J8_terminal_four_moment_source_gate_exact import Iv,arb_ball,log550
from verify_nf492_original_J8_all_orders_log_peel_400jet_exact import positive_square_polynomial_exact_controls
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10)
DELTA=F(1,500)
ETA=F(1,10**15)
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
P=(2,3,4,5,7,8,9)
def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def overlap(a,b):return a.lo<=b.hi and b.lo<=a.hi
def maxabs(a):return max(abs(a.lo),abs(a.hi))
def index_weights(h,N):
    """All proper logarithmic moments for t=d/delta ∈[0,1]."""
    k0=[];k1=[];k2=[]
    for j in range(2*N-1):
        n=F(j+1)
        k0.append(Iv(1)/n)
        k1.append(h/n+Iv(1)/n**2)
        k2.append(h**2/n+2*h/n**2+Iv(2)/n**3)
    return k0,k1,k2
def contract_full_same_source_square(a,c,h):
    n=len(a)
    assert len(c)==n
    k0,k1,k2=index_weights(h,n)
    energy0=Iv(0);energy1=Iv(0);energy2=Iv(0)
    for i in range(n):
        for j in range(i,n):
            factor=(2 if i!=j else 1)
            energy0+=factor*a[i]*a[j]*k0[i+j]
            energy2+=factor*c[i]*c[j]*k2[i+j]
        for j in range(n):
            energy1+=2*a[i]*c[j]*k1[i+j]
    return DELTA*(energy0+energy1+energy2),(
           DELTA*energy0,DELTA*energy1,DELTA*energy2)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--native",required=True)
    ap.add_argument("--nf493-native",required=True)
    ap.add_argument("--nf492-point",required=True)
    ap.add_argument("--nf491",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    curr,nsha=read(args.native)
    prev,psha=read(args.nf493_native)
    oldh,hsha=read(args.nf492_point)
    nf491,gsha=read(args.nf491)
    jet,jsha=read("notes/data/provisional/NF411_original_source_boundary_jet.json")
    nf450,zsha=read("notes/data/provisional/NF450_original_B_complete_Laplace_native_sign_custody_index.json")
    nf482,ash=read("notes/data/provisional/NF482_original_first_J8_irrational_n9_source_signed_custody.json")
    nf483,bsh=read("notes/data/provisional/NF483_original_J8_principal_gram_and_endpoint_stop_custody.json")
    source,ssh=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,seamsha=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    assert curr["pass"]=="NF494-native"
    assert prev["pass"]=="NF493-original-source-400-log-jets"
    assert oldh["pass"]=="NF492-original-source-exact-full-log-physical-crosscheck"
    assert nf491["pass"]=="NF491"
    assert "original_nf406_seam_sha256" in nf491 and "original_nf406_support_sha256" not in nf491, "NF495 exact immutable NF491 schema gate"
    assert ssh==curr["original_nf407_source_sha256"]==prev["original_nf407_source_sha256"]==nf491["original_nf407_source_sha256"]==SRC
    assert seamsha==curr["original_nf406_seams_sha256"]==prev["original_nf406_seams_sha256"]==nf491["original_nf406_seam_sha256"]==SEAM
    assert jet["nf407_source_sha256"]==nf450["source_SHA256"]==nf482["original_nf407_source_sha256"]==SRC
    assert nf483["source_ci_completed_exact"]["conclusion"]=="SUCCESS"
    assert nf482["source_exact_archive"]["conclusion"]=="SUCCESS"
    assert nf491["source_exact_ci"]["conclusion"]=="SUCCESS"
    assert curr["native_precision_bits"]==prev["original_native_precision_bits"]==4096
    assert curr["original_source_original_246_generators_273_modes"] and curr["original_source_true_sinh_zero_rate_pole"]
    assert curr["original_critical_sine_frequencies"]==32
    assert curr["original_source_400_jet_order"]==400 and curr["original_fixed_source_K_tail_index_count"]==1000
    assert curr["original_source_analytic_Cauchy_radius"]==prev["original_analytic_fixed_branch_Cauchy_radius"]=="1/25"
    assert curr["original_true_terminal_delta"]==prev["original_J8_terminal_delta"]=="1/500"
    assert curr["original_source_each_coeff_holomorphic_numeric_input_overcharge"]=="1e-300*25**n"
    assert curr["original_full_J8_Ew_integrated"]==False and curr["NF404"]=="OPEN"
    assert len(curr["original_H_400_native_outward"])==len(curr["original_U_400_native_outward"])==400
    H=[Iv(*map(F,pair)) for pair in curr["original_H_400_native_outward"]]
    U=[Iv(*map(F,pair)) for pair in curr["original_U_400_native_outward"]]
    Up=[Iv(*map(F,pair)) for pair in prev["original_real_original_U_dyadic_coefficient_ball_first_400"]]
    for j,(a,b) in enumerate(zip(U,Up)):
        assert overlap(a,b),("METHOD STOP original U400 source != independently accepted NF493",j)
    v=U[0]
    assert overlap(v,arb_ball(jet["original_original_source_value_at_B_arb"]))
    assert overlap(-U[1],arb_ball(jet["original_original_source_derivative_at_B_arb"]))
    assert v.hi<0 and U[1].lo>0
    c8=Iv(0);seen=[]
    for row in jet["all_seven_original_prime_seam_derivative_identities"]:
        n=row["prime_power"]
        assert n in P and n not in seen
        lo,hi=map(F,row["c_n_positive_outward"])
        c8+=Iv(lo,hi)
        seen.append(n)
    assert seen==list(P) and F(3)<c8.lo<=c8.hi<F(7)
    assert overlap(H[0],Iv(*map(F,nf450["complete_z_B_outward_24_decimal"])))
    assert H[0].hi<0
    refH=Iv(*map(F,oldh["original_source_complete_analytic_H_delta_outward"]))
    delta_pow=F(1)
    Hdelta=Iv(0);Udelta=Iv(0)
    a=[];c=[]
    for j in range(400):
        if j==0:
            a.append(H[j]+v*c8)
        else:
            a.append(H[j]*delta_pow)
        c.append(U[j]*delta_pow/2)
        Hdelta+=H[j]*delta_pow
        Udelta+=U[j]*delta_pow
        delta_pow*=DELTA
    EH=F(curr["original_original_H400_analytic_tail"])
    EU=F(curr["original_original_U400_analytic_tail"])
    assert EH<F(1,10**99) and EU<F(1,10**119)
    assert overlap(Hdelta+Iv(-EH,EH),refH),(
        "METHOD STOP original complete H400 at physical x=549/500 disagrees with independent NF492 source")
    assert Udelta.lo>0
    srcU=Iv(*map(F,curr["original_source_U_at_B_minus_delta_400_native_outward"]))
    assert overlap(Udelta,srcU)
    assert positive_square_polynomial_exact_controls()>30
    h=log550()
    assert F(6)<h.lo<=h.hi<7 and h.width()<F(1,10**90)
    # Exact source-specific coefficient cutoff, NOT assumed frequency
    # decay or independently bounding the huge old matched images.
    ma=sum((maxabs(x) for x in a),F(0))
    mc=sum((maxabs(x) for x in c),F(0))
    assert ma+mc<F(10)**30
    tailsA=[F(0)]*401;tailsC=[F(0)]*401
    for j in range(399,-1,-1):
        tailsA[j]=tailsA[j+1]+maxabs(a[j])
        tailsC[j]=tailsC[j+1]+maxabs(c[j])
    K=next((j for j in range(1,401) if
            tailsA[j]<F(1,10**70) and tailsC[j]<F(1,10**70)),400)
    erra=tailsA[K]+EH
    errc=tailsC[K]+EU/2
    assert erra>0 and errc>0
    assert erra+errc<F(1,10**50), "METHOD STOP source native H high-degree tail not adequately controlled"
    # Actual original physical |w|<25007+0.5*log(B/d); original NF492
    # exact improper log moments I1<8δ, I2<65δ.
    # Account real H/U truncated polynomial error inside the SQUARE,
    # rather than falsely treating divergent log as uniformly bounded.
    truncerr=DELTA*(50014*erra+8*erra+
        (50014*8+65)*errc+erra**2+16*erra*errc+65*errc**2)
    assert truncerr<F(1,10**45)
    print("NF494 exact source joint original H/U 400 jets; original normalized cutoff",K,
          "l1 H+vC",float(ma),"l1 U/2",float(mc),flush=True)
    EwFinite,parts=contract_full_same_source_square(a[:K],c[:K],h)
    EwT=EwFinite+Iv(-truncerr,truncerr)
    assert EwT.lo>0,"METHOD STOP: whole original physical square interval not positive"
    assert EwT.width()<F(1,10**26),"METHOD STOP: full true original physical positive square too wide for NF404"
    EwLast=Iv(*map(F,nf491["genuine_original_last_1e15_Ew_strict_bracket_approx"]))
    assert F(0)<EwLast.lo<=EwLast.hi<F(1,10**33)
    EwBulk=EwT-EwLast
    assert EwBulk.lo>0
    forced=F("9.542089396822990418379e-23")
    sufficient=F("9.54374468603209522225e-23")
    failure=F("9.68201636850086745946e-23")
    # Strictly conservative rounding: the printed original NF491 lower is\n    # 9.542089396822990418379790...e-23, so round DOWN not UP.\n    assert forced<F(nf491["original_source_inferred_EwBulk_strict_lower_approx"])
    assert sufficient<F(nf491["original_NF404_sufficient_EwBulk_upper_approx"])
    assert failure>F(nf491["original_NF404_certain_failure_EwBulk_lower_approx"])
    # This source-inferred original strict lower is a mandatory crosscheck:
    # a contradictory actually measured source bulk interval is a STOP.
    assert EwBulk.hi>forced, "METHOD STOP: actual compact square contradicts accepted NF491 source-inferred lower"
    D_A=Iv(*map(F,nf482["original_J8_first_exact_fraction_source_signed_D_coarse"]))
    EpT=Iv(*map(F,nf483["source_accepted_original_J8_terminal_principal_exact_outward_decimal"]))
    assert D_A.lo>0 and EpT.lo>0
    original_D8=D_A+2*(EwT-EpT)
    D8cap=F("1.629122471432905958157e-22")
    D8fail=F("1.656776807914060395598e-22")
    nf404_sufficient=(EwBulk.hi<=sufficient and original_D8.hi<=D8cap)
    nf404_certain_failure=(EwBulk.lo>failure and original_D8.lo>D8fail)
    decision=("NF404_SOURCE_SCALAR_SUFFICIENT_PASS" if nf404_sufficient else
              "NF404_SOURCE_SCALAR_CERTAIN_FAIL" if nf404_certain_failure else
              "NF404_SOURCE_SCALAR_UNDECIDED")
    out={
      "pass":"NF494",
      "standing":"COMPLETE ACTUAL original source entire J8 terminal 400-H/400-U physical joint positive square numerical SOURCE-certified if all CI passes; NF404 source scalar decision separate from RH",
      "original_nf407_source_sha256":SRC,
      "original_nf406_seams_sha256":SEAM,
      "original_nf494_native_source_json_sha256":nsha,
      "original_nf493_prior_full_U400_native_source_sha256":psha,
      "original_nf492_true_physical_H_delta_source_sha256":hsha,
      "original_nf491_true_positive_bulk_gate_receipt_sha256":gsha,
      "original_nf411_source_sha256":jsha,
      "original_nf450_true_zB_source_sha256":zsha,
      "original_nf482_first_original_n9_signed_sha256":ash,
      "original_nf483_terminal_true_principal_sha256":bsh,
      "original_full_source_400_H_and_400_U_native_exact_interval_coefficients":True,
      "original_native_full_U400_prior_source_each_index_overlaps":True,
      "original_original_endpoint_H0_matches_NF450":True,
      "original_original_400_Hdelta_matches_independent_NF492":True,
      "true_original_J8_terminal_delta":"1/500",
      "original_full_numeric_Hplus_vC8_normalized_l1_envelope":str(ma),
      "original_full_numeric_U_over2_normalized_l1_envelope":str(mc),
      "original_true_same_source_joint_normalized_coeff_retained_count":K,
      "original_full_H400_remaining_source_normalized_l1":str(tailsA[K]),
      "original_full_U400_remaining_source_normalized_l1":str(tailsC[K]),
      "original_complete_H400_original_source_Cauchy_tail":str(EH),
      "original_complete_U400_original_source_Cauchy_tail":str(EU),
      "original_joint_whole_square_finite_400_jet_cutoff_error":str(truncerr),
      "original_complete_J8_true_improper_whole_terminal_positive_square_EwT_outward":EwT.raw(),
      "original_complete_J8_true_improper_whole_terminal_positive_square_EwT_decimal":EwT.decimal(50),
      "original_original_full_terminal_Hplus_vC8_square_component":parts[0].raw(),
      "original_original_full_terminal_cross_HUlog_signed_component":parts[1].raw(),
      "original_original_full_terminal_Ulog_square_component":parts[2].raw(),
      "original_true_original_last_Ew_physical_from_NF491":EwLast.raw(),
      "original_complete_J8_true_BULK_positive_square_EwBulk_outward":EwBulk.raw(),
      "original_complete_J8_true_BULK_positive_square_EwBulk_decimal":EwBulk.decimal(50),
      "original_NF491_bulk_source_forced_lower":str(forced),
      "original_NF404_sufficient_original_bulk_square_upper":str(sufficient),
      "original_NF404_source_scalar_certain_failure_bulk_square_lower":str(failure),
      "original_true_full_J8_first_irrational_D_A_from_NF482":D_A.raw(),
      "original_true_full_J8_principal_EpT_from_NF483":EpT.raw(),
      "original_true_full_J8_signed_D8_outward":original_D8.raw(),
      "original_true_full_J8_signed_D8_decimal":original_D8.decimal(50),
      "NF404_original_selected_source_scalar_decision":decision,
      "original_full_J8_D8_signed_upper_numerically_integrated":True,
      "NF404":"SOURCE SCALAR ONLY — "+decision,
      "W_ODD_NEG":"OPEN",
      "even_whole_operator_domain":"OPEN",
      "RH":"OPEN",
      "next_bold":"NF495 independently replay accepted original raw full physical H400 native all 400 signed square coefficients and original W-ODD-NEG exterior/operator-domain, no RH claim"
    }
    p=Path(args.output);p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2)+"\n")
    print("NF494 true original J8 complete signed source total EwT",*EwT.decimal(40),flush=True)
    print("NF494 true original J8 NF491 actual bulk source EwBulk",*EwBulk.decimal(40),flush=True)
    print("NF494 original source full signed D8",*original_D8.decimal(40),flush=True)
    print("NF494 NF404 selected original SOURCE scalar decision",decision,flush=True)
    print("NF494 W_ODD_NEG / even-whole operator/domain / RH OPEN",flush=True)
if __name__=="__main__":main()
