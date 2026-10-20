#!/usr/bin/env python3
"""MG26: actual-original contiguous source-frequency moment and mass closure.

For a true contiguous positive band C=[0,T] and its negative-frequency
mirror, calculate exact rational original 24-channel source Fourier
enclosures for H_C, G_C, S_C using MG14-16 whole-cell affine Taylor
and SM43 true seven-prime/digamma multiplier bounds.

For all other REAL frequencies, use the *remaining original physical
source mass* H-H_C instead of a crude whole-Gram majorant:

 LG = L_GC + kappa (Hlo-U_HC)
 UG = U_GC + M_k(Hup-L_HC) + tau_G(k) I
 LS = L_SC + kappa²(Hlo-U_HC)
 US = U_SC + M_k²(Hup-L_HC) + tau_S(k) I.

The high-frequency tau for xi>2^k pays (a-M)_+ and (a²-M²)_+.
These are genuine complete-original-frequency Loewner enclosures,
not evaluated exact G/S, and not a full 470D residual.
Rank-one sinh-pole c=G_o e_p is enclosed with MG24's true matrix
Loewner pole-cross method. MG24 original Fourier/domain assumptions
remain inherited and not independently established here.
"""
import argparse,json,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from validate_rpb108_mg16_weighted_affine_source_moments import (
 ROOT,N,PHYS,POLE,PIVOT,B,CHOSEN_TAUS,
 original_source_centered_windows,
 original_full_25_physical_interval_gram,
 protected_inner_cover,boundary_intervals,derivative_intervals_and_D3,
 interval_out,pair_coefficients,positive_gap,
 hyperbolic_interval,original_full_second_derivative_upper,
 original_exact_physical_fourier_midpoint,
 original_midpoint_derivative_intervals,original_third_spatial_moment,
 transformed_affine,abs_cap,zero,finalize,
 positive_cell_weight_interval
)
from validate_rpb108_mg15_directional_affine_covariance import (
 add_directed_cell,lower_cell_trace
)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import (
 exact_sqrt_ceil,add,scale,diag_shift,matrix_outer,serialize
)
from validate_rpb108_mg25_original24_robust_trial import (
 original_H24_from_physical_source,deserialize
)
from validate_rpb108_mg25_robust_source_aware_residual import (
 Id,sub,plus,mul,gersh_lower,psd
)
from validate_rpb108_mg23_physical_metric_matrix_envelope import (
 KAPPA,KAPPA_STAR,LN
)

KEYS=("mass","one","two")
DIM=24
PREFIX=F(4)
PARTITIONS=(8,16)
CUTS=(12,16)

def trace(A):
    return sum((A[i][i] for i in range(len(A))),F(0))

def sign_test():
    """Exact toy mass-complement regression with a high-frequency multiplier."""
    k=F(1,1000);M=F(3)
    Hc=[[F(1),F(0)],[F(0),F(2)]]
    Hl=[[F(3,2),F(0)],[F(0),F(3,4)]]
    Hh=[[F(1,2),F(0)],[F(0),F(1,4)]]
    H=add(add(Hc,Hl),Hh)
    Gc=scale(F(2),Hc);Sc=scale(F(4),Hc)
    G=add(add(Gc,scale(F(1),Hl)),scale(F(8),Hh))
    S=add(add(Sc,scale(F(1),Hl)),scale(F(64),Hh))
    # Even though high weight 8 exceeds low-band upper M=3,
    # explicit positive tau terms make complete-frequency upper valid.
    tau1=F(8)*F(1,2);tau2=F(64)*F(1,2)
    assert psd(sub(G,add(Gc,scale(k,sub(H,Hc)))))
    assert psd(sub(add(add(Gc,scale(M,sub(H,Hc))),
                            scale(tau1,Id(2))),G))
    assert psd(sub(S,add(Sc,scale(k*k,sub(H,Hc)))))
    assert psd(sub(add(add(Sc,scale(M*M,sub(H,Hc))),
                            scale(tau2,Id(2))),S))
    return True

def original_partition_preparation():
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==PHYS and sources[POLE][0]=="pole"
    clusters,*_=protected_inner_cover()
    b=[interval_out(x) for x in boundary_intervals(sources,clusters)]
    d,_=derivative_intervals_and_D3(sources,clusters)
    free=tuple(i for i in range(PHYS) if i not in (PIVOT,POLE))
    assert len(free)==23 and PIVOT==23
    det,a,c=pair_coefficients(b,d,PIVOT,free)
    assert positive_gap(det)>0
    hyp=(hyperbolic_interval(B/2,"sinh"),
         hyperbolic_interval(B/2,"cosh"))
    Kglobal=original_full_second_derivative_upper(sources)
    Kthird=original_third_spatial_moment(sources)
    return centers,sources,a,c,hyp,Kglobal,Kthird

def continuous_cell_prefix(m,prepared):
    centers,sources,a,c,hyp,Kglobal,Kthird=prepared
    assert m in PARTITIONS and PREFIX/m>0
    mats={key:(zero(),zero()) for key in KEYS}
    # The SAME certified original source vector is used for all three
    # moments. [0,PREFIX] is tiled with NO gaps or overlap.
    intervals=[]
    counts={key:{str(t):0 for t in CHOSEN_TAUS} for key in KEYS}
    for j in range(m):
        left=PREFIX*F(j,m);right=PREFIX*F(j+1,m)
        width=right-left;half=width/2;mid=(left+right)/2
        lo,hi,_=positive_cell_weight_interval(left,right)
        assert 0<KAPPA<=lo<=hi
        vals=original_exact_physical_fourier_midpoint(
            mid,centers,sources,hyp)
        deriv,second=original_midpoint_derivative_intervals(
            mid,centers,sources,hyp)
        K=[min(global_bound,abs_cap(local)+third*half)
           if local is not None else global_bound
           for global_bound,local,third in
           zip(Kglobal,second,Kthird)]
        v,d,r=transformed_affine(vals,deriv,K,a,c,half)
        assert len(v)==len(d)==len(r)==DIM
        intervals.append((left,right))
        for key in KEYS:
            wlo,whi=((F(1),F(1)) if key=="mass"
                      else (lo,hi) if key=="one"
                      else (lo*lo,hi*hi))
            tau=max(CHOSEN_TAUS,key=lambda t:
                (lower_cell_trace((wlo,whi),width,v,d,r,t),-t))
            add_directed_cell({key:mats},key,key,(wlo,whi),
                              width,v,d,r,tau)
            counts[key][str(tau)]+=1
    assert intervals[0][0]==0 and intervals[-1][1]==PREFIX
    assert all(intervals[i][1]==intervals[i+1][0]
               for i in range(m-1))
    out={}
    for key in KEYS:
        low,up,el,eu=finalize(mats[key])
        out[key]={
          "lower_matrix":low,"upper_matrix":up,
          "lower_trace":trace(low),"upper_trace":trace(up),
          "rounding_lower":el,"rounding_upper":eu}
        assert trace(up)>=trace(low)
    return {"cell_count":m,"coverage_left":F(0),
            "coverage_right":PREFIX,"full_24D":out,
            "selection_counts":counts}

def pole_correct(LG,UG,LS,US,b0,eb,sigma,esigma):
    """Same actual rank-one pole mixed response as verified MG24."""
    D=sub(UG,LG)
    assert all(D[i][i]>=0 for i in range(DIM))
    c0=[(LG[i][23]+UG[i][23])/2 for i in range(DIM)]
    ec=[exact_sqrt_ceil(D[i][i]*D[23][23])/2 for i in range(DIM)]
    BB=matrix_outer(b0,b0)
    errBB=[[abs(b0[i])*eb[j]+abs(b0[j])*eb[i]+eb[i]*eb[j]
            for j in range(DIM)] for i in range(DIM)]
    eBB=max(sum(row,F(0)) for row in errBB)
    center=[[(-2*(c0[i]*b0[j]+b0[i]*c0[j])
               +4*sigma*BB[i][j]) for j in range(DIM)] for i in range(DIM)]
    errors=[]
    for i in range(DIM):
        row=[]
        for j in range(DIM):
            ecross=(abs(c0[i])*eb[j]+abs(b0[j])*ec[i]+ec[i]*eb[j]
                   +abs(c0[j])*eb[i]+abs(b0[i])*ec[j]+ec[j]*eb[i])
            row.append(2*ecross+4*(
                abs(sigma)*errBB[i][j]+
                esigma*(abs(BB[i][j])+errBB[i][j])))
        errors.append(row)
    eT=max(sum(row,F(0)) for row in errors)
    Lstar=diag_shift(add(LG,scale(-2,BB)),-2*eBB)
    Ustar=diag_shift(add(UG,scale(-2,BB)),2*eBB)
    LSstar=diag_shift(add(LS,center),-eT)
    USstar=diag_shift(add(US,center),eT)
    return Lstar,Ustar,LSstar,USstar,{
      "true_original_pole_response_center":[str(x) for x in c0],
      "true_original_pole_response_radii":[str(x) for x in ec],
      "mixed_pole_correction_error_row":str(eT),
      "pole_Gram_outer_error_row":str(eBB),
      "true_Sstar_cross_terms_paid":True}

def whole_brackets(part,case,Hmid,Herr,b0,eb,sigma,esigma):
    C=part["full_24D"]
    Hlo=diag_shift(Hmid,-Herr); Hup=diag_shift(Hmid,Herr)
    HClo=C["mass"]["lower_matrix"];HCup=C["mass"]["upper_matrix"]
    Glo=C["one"]["lower_matrix"];Gup=C["one"]["upper_matrix"]
    Slo=C["two"]["lower_matrix"];Sup=C["two"]["upper_matrix"]
    k=F(case["cutoff_k"]);M=F(case["original_global_lowband_majorant_M"])
    assert M==F(17)+k*F(347,500)
    assert LN[2][1]<F(347,500)
    tau1=F(case["complete_original_form_tail_rational"])
    tau2=F(case["complete_original_strong_tail_rational"])
    assert 0<tau1<tau2 and PREFIX<F(2)**int(k)
    # Positive complement H-H_C, with outward physical Gram brackets.
    remlo=sub(Hlo,HCup);remup=sub(Hup,HClo)
    LG=add(Glo,scale(KAPPA,remlo))
    UG=diag_shift(add(Gup,scale(M,remup)),tau1)
    LS=add(Slo,scale(KAPPA*KAPPA,remlo))
    US=diag_shift(add(Sup,scale(M*M,remup)),tau2)
    assert all(UG[i][i]>=LG[i][i] and US[i][i]>=LS[i][i]
               for i in range(DIM))
    Lstar,Ustar,LSstar,USstar,pole=pole_correct(
        LG,UG,LS,US,b0,eb,sigma,esigma)
    # Compare to original MG24 (selected-cell lower + coarse whole upper)
    oldLG=deserialize(case["complete_Gstar_lower"])
    oldUG=deserialize(case["complete_Gstar_upper"])
    oldLS=deserialize(case["complete_Sstar_lower"])
    oldUS=deserialize(case["complete_Sstar_upper"])
    wg=trace(sub(Ustar,Lstar))
    ws=trace(sub(USstar,LSstar))
    oldwg=trace(sub(oldUG,oldLG))
    oldws=trace(sub(oldUS,oldLS))
    assert wg>=0 and ws>=0 and oldwg>=0 and oldws>=0
    # Strict source residual test is separate and may fail.
    t=F(case["scalar_trial_t"])
    residual=add(diag_shift(add(Hmid,scale(-2*t,Lstar)),Herr),
                 scale(t*t,USstar))
    margin=gersh_lower(sub(Hlo,residual))
    return {
      "cutoff_k":int(k),
      "physical_contiguous_prefix":str(PREFIX),
      "measured_positive_frequency_fraction":str(PREFIX/F(2)**int(k)),
      "full_original_frequencies_accounted_for":True,
      "mass_complement_used_not_whole_Gram_duplicate":True,
      "new_Gstar_bracket_width_trace":str(wg),
      "old_MG24_Gstar_bracket_width_trace":str(oldwg),
      "Gstar_width_ratio_new_to_MG24":str(wg/oldwg) if oldwg>0 else None,
      "new_Sstar_bracket_width_trace":str(ws),
      "old_MG24_Sstar_bracket_width_trace":str(oldws),
      "Sstar_width_ratio_new_to_MG24":str(ws/oldws) if oldws>0 else None,
      "new_weak_scalar_residual_Gershgorin_margin":str(margin),
      "new_strict_matrix_scalar_residual_certified":margin>0,
      "MG24_scalar_trial_used_unchanged":str(t),
      "whole_Go_lower":serialize(LG),
      "whole_Go_upper":serialize(UG),
      "whole_So_lower":serialize(LS),
      "whole_So_upper":serialize(US),
      "whole_Gstar_lower":serialize(Lstar),
      "whole_Gstar_upper":serialize(Ustar),
      "whole_Sstar_lower":serialize(LSstar),
      "whole_Sstar_upper":serialize(USstar),
      "pole_certificate":pole
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--verified-mg24-json",required=True)
    p.add_argument("--output",default=
        "artifacts/mg26_contiguous_original_24D_mass_closure.json")
    arg=p.parse_args()
    assert sign_test()
    led=json.loads((ROOT/"research/obligations.json").read_text())
    assert led["active_obligation"]=="W-ODD-NEG"
    assert led["objective"]["status"]=="open"
    assert led["governance"]["no_automatic_promotion"]
    old=json.loads((ROOT/arg.verified_mg24_json).read_text())
    assert old["status"]==(
        "ORIGINAL_COMPLETE_FREQUENCY_24CHANNEL_COUPLED_SOURCE_MATRIX_ENCLOSURES")
    assert old["true_complete_original_pole_Gstar_Sstar_Loewner_bracket"]
    assert old["original_physical_SI10_source_count"]==25
    assert old["physical_23D_plus_genuine_pole_channel_dimension"]==24
    assert old["canonical_W_ODD_NEG"]=="OPEN"
    assert not old["signed_original_negative_cap_51over56"]
    Hmid,Hrad,Herr=original_H24_from_physical_source()
    assert Herr==F(old["physical_Gram_Loewner_row_error"])
    b0=[Hmid[i][23] for i in range(DIM)]
    eb=[Hrad[i][23] for i in range(DIM)]
    sigma=b0[23];esigma=eb[23]
    assert sigma>esigma>=0
    assert [str(x) for x in b0]==old["original_pole_b_center"]
    prepared=original_partition_preparation()
    runs=[]
    for m in PARTITIONS:
        subband=continuous_cell_prefix(m,prepared)
        scenarios=[whole_brackets(subband,c,Hmid,Herr,b0,eb,sigma,esigma)
                   for c in old["cases"] if c["cutoff_k"] in CUTS]
        assert len(scenarios)==len(CUTS)
        part_out={
          "cell_count":m,
          "actual_original_contiguous_positive_band":[str(F(0)),str(PREFIX)],
          "true_coverage_no_gaps_or_overlaps":True,
          "number_physical_generators":25,
          "number_coupled_transformed_sources":DIM,
          "all_576_source_cross_terms_paid":True,
          "complete_unweighted_source_mass_bracket":True,
          "complete_two_original_weighted_source_moment_brackets":True,
          "weighted_Young_tau_choice_counts":subband["selection_counts"],
          "prefix_moments":{
             key:{
                 "lower":serialize(subband["full_24D"][key]["lower_matrix"]),
                 "upper":serialize(subband["full_24D"][key]["upper_matrix"]),
                 "lower_trace":str(subband["full_24D"][key]["lower_trace"]),
                 "upper_trace":str(subband["full_24D"][key]["upper_trace"])
             } for key in KEYS},
          "complete_original_frequency_scenarios":scenarios
        }
        runs.append(part_out)
    out={
      "status":"ORIGINAL_CONTIGUOUS_PREFIX_COUPLED_MASS_CLOSURE_24D",
      "canonical_W_ODD_NEG":"OPEN",
      "verified_MG24_run_id":39378465438,
      "original_24D_physical_Gram_reconstructed":True,
      "true_contiguous_prefix_rational_cell_integrals":True,
      "measured_prefix_positive_frequency_upper":str(PREFIX),
      "not_entire_low_band_numerically_integrated":True,
      "remaining_all_frequencies_certified_with_original_physical_mass":True,
      "all_original_prime7_arch_multiplier_cell_bounds":True,
      "true_original_pole_mixed_response_paid":True,
      "source_24D_is_not_invariant_for_resolvent":True,
      "original_470D_strong_residual_certified":False,
      "original_signed_negative_51over56_cap_certified":False,
      "independent_Fourier_form_domain_audit":"OPEN",
      "even_Weil_CC27_RH":"OPEN",
      "partitions":runs,
      "decision":"Actual original contiguous prefix source mass and two weighted coupled moments, rigorously bounded; complete-frequency complement closed with H-Hprefix and SM41 high tails. Compare numerical width to MG24; no automatic positive contraction or 470D signed proof."
    }
    dst=ROOT/arg.output;dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(out,indent=2)+"\n")
    print("MG26 original prefix mass-closure:",json.dumps({
      "cells":[m["cell_count"] for m in runs],
      "width_ratios":{
        str(p["cell_count"]):{
          str(c["cutoff_k"]):{
            "G":float(F(c["Gstar_width_ratio_new_to_MG24"])),
            "S":float(F(c["Sstar_width_ratio_new_to_MG24"]))}
          for c in p["complete_original_frequency_scenarios"]}
        for p in runs},
      "strict_source_residual_any":any(
          c["new_strict_matrix_scalar_residual_certified"]
          for p in runs for c in p["complete_original_frequency_scenarios"]),
      "signed_470_even_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
