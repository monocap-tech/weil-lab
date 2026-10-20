#!/usr/bin/env python3
"""MG17B: original weighted-versus-constant SAME-NONFLAT-CELL source moments.

Replays MG17's RIGOROUS true-nonconstant original multiplier panel
selection. Holds fixed the genuine MG11/12 23 double-boundary-vanishing
supported physical sources and true sinh pole.

On exactly each new nonflat cell, evaluate two INDEPENDENT true-source
complete 24x24 Loewner certificates:
 (a) SM43 true original multiplier interval [l,u] and MG15
     sourcewise affine Young bound, optimized over the same 7 tau;
 (b) MG16 exact true-original SM43A J0/J1/J2 signed-positive reference
     plus both full-source affine Young and true multiplier-error fees,
     optimized over same tau.
No mixing regions or comparing this new spectrum to old MG15
spectrum as if it were on the same operator-window.
The two moments are Ao and Ao squared, NOT pole-corrected Astar².
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_mg17_nonflat_multiplier_scout import scout
from validate_rpb108_mg16_weighted_affine_source_moments import (
 ROOT,PHYS,N,POLE,PIVOT,B,ORDERS,CHOSEN_TAUS,
 moments_reference,covariance_matrices,true_cell_add,
 weighted_lower_trace,original_source_centered_windows,
 original_full_25_physical_interval_gram,
 protected_inner_cover,boundary_intervals,derivative_intervals_and_D3,
 interval_out,pair_coefficients,positive_gap,
 hyperbolic_interval,original_full_second_derivative_upper,
 original_exact_physical_fourier_midpoint,
 original_midpoint_derivative_intervals,original_third_spatial_moment,
 transformed_affine,abs_cap,zero,finalize,exact_inertia_general,
 positive_cell_weight_interval
)
from validate_rpb108_mg15_directional_affine_covariance import (
 add_directed_cell,lower_cell_trace
)
def main_data():
    sites=scout()
    selected=sites["selected_nonflat_original_cells"]
    assert len(selected)>=8 and sites["selected_cell_count"]==len(selected)
    centers,sources,_=original_source_centered_windows()
    G,physical,_=original_full_25_physical_interval_gram()
    assert physical==sources and len(sources)==PHYS
    clusters,*_=protected_inner_cover()
    b=[interval_out(x) for x in boundary_intervals(sources,clusters)]
    dtrace,_=derivative_intervals_and_D3(sources,clusters)
    free=tuple(i for i in range(PHYS) if i not in (PIVOT,POLE))
    det,a,c=pair_coefficients(b,dtrace,PIVOT,free)
    assert positive_gap(det)>0 and len(free)==23
    hyp=(hyperbolic_interval(B/2,"sinh"),
         hyperbolic_interval(B/2,"cosh"))
    Kglobal=original_full_second_derivative_upper(sources)
    Kthird=original_third_spatial_moment(sources)

    families=("constant","weighted")
    mats={family:{order:(zero(),zero()) for order in ORDERS}
          for family in families}
    counts={f:{o:{str(t):0 for t in CHOSEN_TAUS} for o in ORDERS}
            for f in families}
    diagnostics=[]
    for site in selected:
        left,right=F(site["left"]),F(site["right"])
        assert left<right
        mid=(left+right)/2;half=(right-left)/2;width=right-left
        lo,hi,info=positive_cell_weight_interval(left,right)
        assert lo>F(1,1000)
        vals=original_exact_physical_fourier_midpoint(
            mid,centers,sources,hyp)
        deriv,second=original_midpoint_derivative_intervals(
            mid,centers,sources,hyp)
        K=[min(glob,abs_cap(local)+third*half)
           if local is not None else glob
           for glob,local,third in zip(Kglobal,second,Kthird)]
        v,d,r=transformed_affine(vals,deriv,K,a,c,half)
        reference,meta=moments_reference(left,right,centers,sources)
        assert meta["type"]=="signed_positive_part_affine"
        assert reference[1][0][1]!=0
        q=[abs(v[i])+half*abs(d[i])+r[i] for i in range(N)]
        desc={"left":str(left),"right":str(right),
              "original_multiplier_lower":str(lo),
              "original_multiplier_upper":str(hi),
              "J1_nonzero":True}
        for order in ORDERS:
            power=1 if order=="one" else 2
            low,up=(lo,hi) if power==1 else (lo**2,hi**2)
            J,eta=reference[power]
            C=covariance_matrices(v,d,J)
            baseline=max(
                ((lower_cell_trace((low,up),width,v,d,r,t),t)
                 for t in CHOSEN_TAUS),key=lambda x:x[0])
            weighted=max(
                ((weighted_lower_trace(C,J[0],eta,width,q,r,t),t)
                 for t in CHOSEN_TAUS),key=lambda x:x[0])
            add_directed_cell(
                mats,"constant",order,(low,up),width,v,d,r,baseline[1])
            true_cell_add(
                mats,"weighted",order,C,J[0],eta,width,q,r,weighted[1])
            counts["constant"][order][str(baseline[1])]+=1
            counts["weighted"][order][str(weighted[1])]+=1
            desc[order+"_constant_selected_tau"]=str(baseline[1])
            desc[order+"_weighted_selected_tau"]=str(weighted[1])
            desc[order+"_weighted_lower_reference_trace_minus_constant"]=str(
                weighted[0]-baseline[0])
        diagnostics.append(desc)
    output={}
    for family in families:
        output[family]={}
        for order in ORDERS:
            L,U,el,eu=finalize(mats[family][order])
            inertia=exact_inertia_general(L)
            assert sum(inertia)==N
            output[family][order]={
                "lower":[[str(z) for z in row] for row in L],
                "upper":[[str(z) for z in row] for row in U],
                "lower_trace":str(sum((L[i][i] for i in range(N)),F(0))),
                "upper_trace":str(sum((U[i][i] for i in range(N)),F(0))),
                "lower_exact_inertia":dict(zip(
                    ("positive","negative","zero"),inertia)),
                "whole_matrix_outward_fees":[str(el),str(eu)]
            }
    comp={}
    for order in ORDERS:
        old=output["constant"][order];new=output["weighted"][order]
        comp[order]={
           "weighted_lower_trace_minus_same_cell_constant":str(
               F(new["lower_trace"])-F(old["lower_trace"])),
           "weighted_upper_trace_reduction_same_cell":str(
               F(old["upper_trace"])-F(new["upper_trace"])),
           "same_cell_constant_lower_inertia":old["lower_exact_inertia"],
           "same_cell_weighted_lower_inertia":new["lower_exact_inertia"],
           "negative_lower_reference_directions_recovered":(
               old["lower_exact_inertia"]["negative"]-
               new["lower_exact_inertia"]["negative"])
        }
    return {
        "status":"SCOPED_ACTUAL_NONFLAT_ORIGINAL_WEIGHTED_VS_CONSTANT_SOURCE_MOMENTS",
        "canonical_W_ODD_NEG":"OPEN",
        "nonflat_original_multiplier_sites_replayed":True,
        "true_source_count":PHYS,
        "true_boundary_adapted_source_count":23,
        "original_pole_included":True,
        "all_24_coupled_source_channels_retained":True,
        "same_new_nonflat_cell_family_used_for_both_comparisons":True,
        "selected_new_nonflat_cells":len(selected),
        "original_true_nonflat_multiplier_certified_each_cell":True,
        "SM43A_true_signed_affine_J1_nonzero_each_cell":True,
        "true_original_weight_mismatch_paid":True,
        "source_Taylor_error_paid_in_both_comparisons":True,
        "tau_selection_counts":counts,
        "per_cell_diagnostics":diagnostics,
        "actual_original_coupled_source_matrices":output,
        "same_cell_method_comparison":comp,
        "source_moments_cover_complete_low_band":False,
        "original_Astar_squared_pole_correction_certified":False,
        "original_strong_Galerkin_residual_certified":False,
        "original_full470_odd_operator_certified":False,
        "even_Weil_CC27_RH":"OPEN",
        "independent_original_Fourier_domain_premises_audit":"OPEN",
        "decision":"Interpret exact same-cell spectral reference comparison, not original operator inertia. No whole-operator theorem promotion."
    }
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/mg17_original_nonflat_coupled_two_moments.json")
    args=p.parse_args()
    d=main_data()
    file=ROOT/args.output
    file.parent.mkdir(parents=True,exist_ok=True)
    file.write_text(json.dumps(d,indent=2)+"\n")
    print("MG17 original same-nonflat-cell source moments:",json.dumps({
        "cells":d["selected_new_nonflat_cells"],
        "comparison":d["same_cell_method_comparison"],
        "full_odd_even_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":
    main()
