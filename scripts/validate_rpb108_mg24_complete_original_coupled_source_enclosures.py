#!/usr/bin/env python3
"""MG24: rigorous complete-frequency 24-channel coupled source moment ENCLOSURES.

Combines original MG19 selected-frequency certified Loewner lower moments
(p=1,2) with original MG12/SM41 complete-frequency physical-Gram and
Fourier tail UPPERS, for actual 23 boundary-adapted sources + sinh pole.

The actual full-frequency matrices are enclosed, not evaluated exactly.
Uses a true source pole column b=H e_p and full Ao pole column c=Go e_p:
Gstar=Go-2bb*; Sstar=So-2(cb*+bc*)+4sigma bb*.
Certifies whole-frequency coupled LOEWNER enclosures by exact rational
source interval and row-sum error accounting. No truncated source matrix
may be presented as the actual full-frequency matrix.

Also emits an upper on the genuine 24D strong physical residual of
Y=tF, but no full 470D J or signed 51/56 negative cap.
"""
import argparse,json,sys
from fractions import Fraction as F
from math import isqrt
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

from validate_rpb108_mg19_intersected_weight_source_moments import main_data
from validate_rpb108_mg23_physical_metric_matrix_envelope import (
    ROOT, N, P, interval_frac, maxabs, pair_coefficients,
    original_transformed_gram, pole_crosses, certified_raw_eigen_floor,
    original_full_25_physical_interval_gram,exact_verified_preconditioned_gram,
    protected_inner_cover, geometry, select_sources,
    boundary_intervals, derivative_intervals_and_D3,
    positive_gap, KAPPA_STAR, LN,
    mathematical_global_original_positive_multiplier_majorant
)
from validate_rpb108_mg11_dual_boundary_trace_kernel import interval_out

DIM=24
CUTS=(12,16,20)
SQRT_SCALE=10**15
def zeros(n=DIM): return [[F(0) for _ in range(n)] for _ in range(n)]
def exact_sqrt_ceil(x):
    x=F(x);assert x>=0
    t=x.numerator*SQRT_SCALE**2
    # q is the smallest integer >= sqrt(t/x.denominator)
    q=isqrt(t//x.denominator)
    if q*q*x.denominator<t:q+=1
    assert F(q,SQRT_SCALE)**2>=x
    return F(q,SQRT_SCALE)
def centers_and_diag_error(H):
    n=len(H)
    mid=[[(z.l+z.h)/2 for z in row] for row in H]
    rad=[[(z.h-z.l)/2 for z in row] for row in H]
    err=max(sum(row,F(0)) for row in rad)
    assert err>=0
    for i in range(n):
        for j in range(n):
            assert mid[i][j]==mid[j][i] and rad[i][j]==rad[j][i]
            assert rad[i][j]>=0
    return mid,rad,err
def matrix_outer(v,w):
    return [[x*y for y in w] for x in v]
def add(A,B):
    return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def scale(k,A):
    return [[k*x for x in row] for row in A]
def diag_shift(A,t):
    B=[list(row) for row in A]
    for i in range(len(B)):B[i][i]+=t
    return B
def lower_and_upper(mg19,order):
    c=mg19["actual_original_coupled_source_matrices"]["relative"][order]
    return ([[F(x) for x in row] for row in c["lower"]],
            [[F(x) for x in row] for row in c["upper"]])
def serialize(A):return [[str(x) for x in row] for row in A]

def build_pole_brackets(Hmid,Hrad,Herr,Lgo,Lso,k,tail_form,tail_sq,ell,
                        b0,eb,sigma0,esigma):
    """All comparisons are in the SAME real 24-channel physical basis."""
    M=F(17)+k*F(347,500)
    assert LN[2][1]<F(347,500) and ell>0
    UG=diag_shift(scale(M,Hmid),M*Herr+tail_form)
    US=diag_shift(scale(M*M,Hmid),M*M*Herr+tail_sq)
    # Lgo <= Go <= UG, hence D=UG-Lgo >=0 and
    # c=(Go)e_p lies in the D-induced Loewner column interval.
    D=add(UG,scale(-1,Lgo))
    assert all(D[i][i]>=0 for i in range(DIM))
    cp=DIM-1
    c0=[(Lgo[i][cp]+UG[i][cp])/2 for i in range(DIM)]
    ec=[exact_sqrt_ceil(D[i][i]*D[cp][cp])/2 for i in range(DIM)]
    assert all(v>=0 for v in ec)
    BB=matrix_outer(b0,b0)
    Berr=[[abs(b0[i])*eb[j]+abs(b0[j])*eb[i]+eb[i]*eb[j]
            for j in range(DIM)] for i in range(DIM)]
    ebrow=max(sum(row,F(0)) for row in Berr)
    # The cross term is formed with the ACTUAL pole response column.
    T=zeros();Terr=zeros()
    for i in range(DIM):
        for j in range(DIM):
            T[i][j]=(-2*(c0[i]*b0[j]+b0[i]*c0[j])
                      +4*sigma0*BB[i][j])
            ecross=(abs(c0[i])*eb[j]+abs(b0[j])*ec[i]+ec[i]*eb[j]
                   +abs(c0[j])*eb[i]+abs(b0[i])*ec[j]+ec[j]*eb[i])
            Terr[i][j]=2*ecross+4*(
                abs(sigma0)*Berr[i][j]
                +esigma*(abs(BB[i][j])+Berr[i][j]))
            assert Terr[i][j]>=0
    terr=max(sum(row,F(0)) for row in Terr)
    LG=diag_shift(add(Lgo,scale(-2,BB)),-2*ebrow)
    UGstar=diag_shift(add(UG,scale(-2,BB)),2*ebrow)
    LS=diag_shift(add(Lso,T),-terr)
    USstar=diag_shift(add(US,T),terr)
    # Global full-source 24D fallback K, t, positive gap.
    # This relies on SI29 only within its independently audited domain.
    eta=F(1,16)
    K0=M*M+tail_sq/ell
    Kstar=(1+eta)*K0+4*(1+1/eta)*(sigma0+esigma)**2
    t=KAPPA_STAR/Kstar
    gap=KAPPA_STAR*KAPPA_STAR/Kstar
    assert 0<gap<1 and 0<t
    # R*R <= H_upper -2t Gstar_lower +t² Sstar_upper
    Rupper=diag_shift(add(add(Hmid,scale(-2*t,LG)),
                          scale(t*t,USstar)),Herr)
    strict=False
    # Gershgorin sufficient, never falsely promote if uncertain.
    Hlower=diag_shift(Hmid,-Herr)
    margin=add(diag_shift(scale(1-gap,Hlower),F(0)),scale(-1,Rupper))
    margin_gersh=min(margin[i][i]-
                      sum((abs(margin[i][j]) for j in range(DIM)
                           if j!=i),F(0)) for i in range(DIM))
    strict=margin_gersh>0
    return {
      "cutoff_k":k,
      "all_original_frequencies_covered_by_selected_L_and_whole_U":True,
      "actual_Go_and_So_values_computed":False,
      "MG19_selected_Go_lower":serialize(Lgo),
      "MG19_selected_So_lower":serialize(Lso),
      "complete_original_Go_upper":serialize(UG),
      "complete_original_So_upper":serialize(US),
      "complete_Gstar_lower":serialize(LG),
      "complete_Gstar_upper":serialize(UGstar),
      "complete_Sstar_lower":serialize(LS),
      "complete_Sstar_upper":serialize(USstar),
      "pole_response_c_mid":[str(v) for v in c0],
      "pole_response_c_radius":[str(v) for v in ec],
      "pole_mixed_exact_interval_correction_center":serialize(T),
      "pole_mixed_correction_row_error":str(terr),
      "pole_gram_outer_row_error":str(ebrow),
      "complete_original_form_tail_rational":str(tail_form),
      "complete_original_strong_tail_rational":str(tail_sq),
      "original_global_lowband_majorant_M":str(M),
      "scalar_full24_Kstar_fallback":str(Kstar),
      "scalar_trial_t":str(t),
      "fallback_one_step_squared_residual_gap":str(gap),
      "complete_Gstar_Sstar_residual_matrix_upper":serialize(Rupper),
      "matrix_residual_strict_margin_gershgorin":str(margin_gersh),
      "strict_matrix_residual_contraction_passed":strict,
      "not_a_full470_residual":True
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default=
        "artifacts/mg24_full_original_coupled_24source_matrix_enclosures.json")
    p.add_argument("--verified-mg19-json",default=None,
        help="Accepted full exact-rational MG19 Actions artifact; otherwise replay full MG19")
    opts=p.parse_args()
    led=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in led["obligations"] if o["id"]=="W-ODD-NEG")
    assert led["active_obligation"]=="W-ODD-NEG"
    assert odd["status"]==led["objective"]["status"]=="open"
    assert led["governance"]["no_automatic_promotion"]
    assert mathematical_global_original_positive_multiplier_majorant()
    if opts.verified_mg19_json:
        # Archived immutable MG19 GitHub Actions 39363425186 PASSED both
        # original calculation-bearing and independent exact Fraction CI.
        # This JSON is retrieved by the workflow by exact run ID and name;
        # independently enforce the mathematical scope and source identity.
        selected=json.loads((ROOT/opts.verified_mg19_json).read_text())
        assert selected["status"]==(
            "SCOPED_NONFLAT_ORIGINAL_INTERSECTED_RELATIVE_WEIGHT_FULL_SOURCE_MOMENTS")
        assert selected["MG19_all_independent_relative_weight_factors_intersected"]
        assert selected["selected_new_nonflat_cells"]==24
        assert selected["same_new_nonflat_cell_family_used_for_both_comparisons"]
        assert selected["all_24_coupled_source_channels_retained"]
        assert not selected["source_moments_cover_complete_low_band"]
    else:
        selected=main_data()
    assert selected["canonical_W_ODD_NEG"]=="OPEN"
    # MG19 counts the FULL original physical catalog (25), whereas its
    # adapted coupled moment matrices have 23 boundary sources + pole =24.
    assert selected["true_source_count"]==25
    assert selected["true_boundary_adapted_source_count"]==23
    assert selected["original_pole_included"]
    assert not selected["source_moments_cover_complete_low_band"]
    assert selected["MG17_absolute_same_cell_exact_replay_matched"]

    clusters,_,_,_,_=protected_inner_cover()
    infos,*_=geometry()
    sources=select_sources(infos)
    assert len(sources)==25 and sources[P][0]=="pole"
    raw,physical,_=original_full_25_physical_interval_gram()
    assert sources==physical
    H25=[[interval_frac(x) for x in row] for row in raw]
    bv=[interval_out(x) for x in boundary_intervals(sources,clusters)]
    dv,_=derivative_intervals_and_D3(sources,clusters)
    pivots=[]
    for q in range(24):
        gap=positive_gap(bv[P]*dv[q]-bv[q]*dv[P])
        if gap>0:pivots.append((gap,q))
    _,pivot=max(pivots,key=lambda pair:(pair[0],-pair[1]))
    assert pivot==23
    free=tuple(i for i in range(25) if i not in (P,pivot))
    assert len(free)==23
    delta,a,c=pair_coefficients(bv,dv,pivot,free)
    assert positive_gap(delta)>0
    H23=original_transformed_gram(H25,free,pivot,a,c)
    g=pole_crosses(H25,free,pivot,a,c)
    assert len(g)==23
    H24=[[None for _ in range(DIM)] for _ in range(DIM)]
    for i in range(23):
        for j in range(23):H24[i][j]=H23[i][j]
        H24[i][23]=H24[23][i]=g[i]
    H24[23][23]=H25[P][P]
    cert=exact_verified_preconditioned_gram(H24)
    assert cert["certified_entire_original_25x25_physical_gram_SPD"]
    ell,_=certified_raw_eigen_floor(H24,cert)
    assert ell>0
    Hmid,Hrad,Herr=centers_and_diag_error(H24)
    b0=[Hmid[i][23] for i in range(DIM)]
    eb=[Hrad[i][23] for i in range(DIM)]
    sigma0=b0[23];esigma=eb[23]
    assert sigma0>esigma>=0
    # SM41 original 1/xi physical source Fourier tails; 23D double
    # boundary transform is charged by triangle, so no missing terms.
    pole_u=F(2,5)
    raw_u={i:(F(1,2) if sources[i][2]==0 else F(7,10))
            for i in range(24)}
    u=[raw_u[i]+maxabs(a[i])*pole_u+maxabs(c[i])*raw_u[pivot]
       for i in free]+[pole_u]
    sq_energy=sum((x*x for x in u),F(0))
    assert len(u)==DIM and sq_energy>0
    Lgo,_=lower_and_upper(selected,"one")
    Lso,_=lower_and_upper(selected,"two")
    assert len(Lgo)==len(Lso)==DIM
    cases=[]
    for k in CUTS:
        M=F(17)+k*F(347,500)
        Lambda=F(2**k)
        tailG=2*sq_energy*(M+1)/Lambda
        tailS=2*sq_energy*(M*M+2*M+2)/Lambda
        cases.append(build_pole_brackets(
            Hmid,Hrad,Herr,Lgo,Lso,k,tailG,tailS,ell,
            b0,eb,sigma0,esigma))
    best=max(cases,key=lambda z:F(z["fallback_one_step_squared_residual_gap"]))
    out={
      "status":"ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES",
      "canonical_W_ODD_NEG":"OPEN",
      "original_physical_SI10_source_count":25,
      "original_23D_double_boundary_source_frame":True,
      "physical_23D_plus_genuine_pole_channel_dimension":24,
      "original_24D_physical_Gram_verified_positive":True,
      "original_24D_Gram_ell":str(ell),
      "physical_Gram_Loewner_row_error":str(Herr),
      "original_pole_b_center":[str(x) for x in b0],
      "original_pole_b_radii":[str(x) for x in eb],
      "pole_sigma_center":str(sigma0),
      "pole_sigma_radius":str(esigma),
      "true_original_source_pole_response_c_enclosed":True,
      "true_complete_original_pole_Gstar_Sstar_Loewner_bracket":True,
      "actual_full_original_Gstar_Sstar_matrices_evaluated_exactly":False,
      "selected_MG19_original_source_lower_replayed":True,
      "unselected_lowband_paid_by_global_multiplier_majorant":True,
      "whole_real_highband_paid_by_SM41_source_tails":True,
      "MG07_actual_full470_source_residual_certified":False,
      "signed_original_negative_cap_51over56":False,
      "even_Weil_CC27_RH":"OPEN",
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "finite_frame_invariant_under_residual":False,
      "cases":cases,
      "best_scalar_fallback_cutoff":best["cutoff_k"],
      "best_scalar_fallback_gap":best["fallback_one_step_squared_residual_gap"],
      "decision":"Rigorous complete-frequency original coupled 24D Gstar and Sstar matrix Loewner ENCLOSURES, including c=Go e_p and pole mixed term. NOT exact evaluated full-frequency matrices, not sharp 24D contraction from matrix brackets unless strict margin passes, and no original 470D signed gate."
    }
    dst=ROOT/opts.output
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(out,indent=2)+"\n")
    print("MG24 complete-frequency coupled enclosure:",json.dumps({
      "dimension":24,
      "MG19_selected_cells":selected["selected_new_nonflat_cells"],
      "best_scalar_k":out["best_scalar_fallback_cutoff"],
      "best_scalar_gap":float(F(out["best_scalar_fallback_gap"])),
      "strict_matrix_residual_cases":[
        x["cutoff_k"] for x in cases if x["strict_matrix_residual_contraction_passed"]],
      "signed_negative_cap_51over56":"OPEN"}),flush=True)

if __name__=="__main__":main()
