#!/usr/bin/env python3
"""MG14 — original 24-channel AFFINE two-moment coupled source test.

Scope: EXACT ORIGINAL SOURCE, but only 24 disjoint real-frequency cells
from MG13, conditional on the same original Fourier/form-domain premises.

Original physical h_i=f_i-a_i*s-c_i*f_23 (23 exact dual-endpoint
vanishing sources) plus actual pole s, all original source crosses.

At each cell midpoint, exact original physical Fourier Taylor data:
   T(xi)=v+d*(xi-mid)+e(xi), |e_i(xi)|<=radius_i
where v,d are rationals and radius_i rigorously includes original
value/derivative intervals and genuine second-derivative Taylor fees.

The exactly integrated affine PSD reference is
   C=vv^T+(width^2/12)*dd^T.
For ||e||<=E and ||v+d*t||<=||v||+width/2*||d||,
the complete pointwise operator error is bounded by
   delta=2*E*(||v||+width/2*||d||)+E^2.
With true original 0<l<=a_o(xi)<=u on ENTIRE real cell:
  2*w*l*(C-delta I) <= 2 int_cell a_o*T*T^T
                    <= 2*w*u*(C+delta I);
and similarly l^2,u^2 for the A_o^2 source moment.

Compare with an independent faithful replay of MG13 midpoint
lower/upper matrices on the very SAME frequency panels. A third
policy selects the greater cellwise lower TRACE for each moment.
Selection never assumes Loewner dominance, and every selected
whole-matrix enclosure is independently valid.

No entire low band, Astar^2, Galerkin residual, 470D inverse,
canonical odd/even, Weil, CC27 or RH theorem is inferred.
"""
import argparse
import json
from fractions import Fraction as F

from validate_rpb108_mg13_true_coupled_lowband_moments import (
    ROOT, N, PHYS, POLE, PIVOT, I, B,
    original_source_centered_windows,
    original_full_25_physical_interval_gram,
    protected_inner_cover, boundary_intervals,
    derivative_intervals_and_D3, interval_out, pair_coefficients,
    positive_gap, panel_windows, hyperbolic_interval,
    original_physical_source_lipschitz,
    original_full_second_derivative_upper,
    local_source_first_derivative_at_midpoint,
    original_exact_physical_fourier_midpoint,
    positive_cell_weight_interval, transformed_frequency,
    sqrt_upper, up, down, zero, sym, add_rank_one,
    compact_lower, compact_upper
)
from validate_rpb108_sm46_affine_physical_fourier_source import (
    original_midpoint_derivative_intervals,
    original_third_spatial_moment
)
from validate_rpb108_sm62_full25_338signed_positive import exact_inertia_general

POLICIES = ("midpoint", "affine", "adaptive")
ORDERS = ("one", "two")

def abs_cap(x):
    return max(abs(x.l), abs(x.h))

def centered_interval(x):
    """Rational reference point and outward radius for the true interval."""
    iv = interval_out(x)
    v = down(iv.mid())
    r = up(max(abs(iv.l-v), abs(iv.h-v)))
    assert v-r <= x.l and x.h <= v+r
    return v,r

def transformed_affine(vals, derivatives, K2, a, c, half):
    assert len(vals)==len(derivatives)==len(K2)==PHYS
    phys_val = [I(x-r,x+r) for x,r in vals]
    midpoint=[]; slope=[]; radius=[]
    for i in range(PHYS):
        if i==PIVOT or i==POLE:
            continue
        value=phys_val[i]-a[i]*phys_val[POLE]-c[i]*phys_val[PIVOT]
        deriv=derivatives[i]-a[i]*derivatives[POLE]-c[i]*derivatives[PIVOT]
        K=K2[i]+abs_cap(a[i])*K2[POLE]+abs_cap(c[i])*K2[PIVOT]
        v,vr=centered_interval(value)
        d,dr=centered_interval(deriv)
        e=up(vr+dr*half+K*half*half/2)
        midpoint.append(v);slope.append(d);radius.append(e)
    v,vr=centered_interval(phys_val[POLE])
    d,dr=centered_interval(derivatives[POLE])
    midpoint.append(v);slope.append(d)
    radius.append(up(vr+dr*half+K2[POLE]*half*half/2))
    assert len(midpoint)==len(slope)==len(radius)==N
    assert all(z>=0 for z in radius)
    return midpoint,slope,radius

def exact_affine_error(v,d,e,half):
    v2=sum((x*x for x in v),F(0))
    d2=sum((x*x for x in d),F(0))
    e2=sum((x*x for x in e),F(0))
    V=sqrt_upper(v2)+half*sqrt_upper(d2)
    E=sqrt_upper(e2)
    delta=up(2*V*E+e2)
    assert delta>=0
    # A Taylor linearization error is for the WHOLE affine vector,
    # not independently payable diagonal-only source entries.
    return delta,v2,d2,e2

def toy_exact_affine_integral():
    """Independently verify the t-even cross cancellation."""
    v=[F(2),F(-3),F(5)]
    d=[F(7),F(11),F(-1)]
    half=F(1,8); width=2*half
    for i in range(3):
        for j in range(3):
            # Integrate (v_i+t*d_i)*(v_j+t*d_j) exactly on [-half,half].
            full=(width*v[i]*v[j]
                  +width**3*d[i]*d[j]/12)
            direct=(width*v[i]*v[j]
                    +(v[i]*d[j]+d[i]*v[j])*(half**2-(-half)**2)/2
                    +(d[i]*d[j])*(half**3-(-half)**3)/3)
            assert full==direct
    return True

def add_policy_cell(out,order,policy,v,d,delta,width,l,u):
    assert 0<=delta and 0<l<=u and width>0
    lo,hi=out[policy][order]
    fac=2*width
    add_rank_one(lo,v,fac*l)
    add_rank_one(hi,v,fac*u)
    if d is not None:
        q=width*width/12
        add_rank_one(lo,d,fac*l*q)
        add_rank_one(hi,d,fac*u*q)
    for i in range(N):
        lo[i][i]-=fac*l*delta
        hi[i][i]+=fac*u*delta

def finalize(matrix):
    lo,hi=matrix
    sym(lo);sym(hi)
    l,ell=compact_lower(lo)
    u,ue=compact_upper(hi)
    assert len(l)==len(u)==N
    assert all(u[i][i]>=l[i][i] for i in range(N))
    return l,u,ell,ue

def source_panel_run():
    ledger=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in ledger["obligations"] if x["id"]=="W-ODD-NEG")
    assert ledger["active_obligation"]=="W-ODD-NEG"
    assert odd["status"]==ledger["objective"]["status"]=="open"
    assert ledger["governance"]["no_automatic_promotion"]
    assert all(x in odd["evidence"] for x in ("SM41","SM42","SI29"))
    assert toy_exact_affine_integral()

    centers,sources,_=original_source_centered_windows()
    assert len(sources)==PHYS and sources[POLE][0]=="pole"
    Gram,physical,_=original_full_25_physical_interval_gram()
    assert physical==sources and len(Gram)==PHYS
    clusters,*_=protected_inner_cover()
    b=[interval_out(x) for x in boundary_intervals(sources,clusters)]
    deriv_trace,_=derivative_intervals_and_D3(sources,clusters)
    free=tuple(i for i in range(PHYS) if i not in (PIVOT,POLE))
    assert len(free)==23
    determinant,a,c=pair_coefficients(b,deriv_trace,PIVOT,free)
    assert positive_gap(determinant)>0
    panels,spans=panel_windows(centers,sources)
    hyp=(hyperbolic_interval(B/2,"sinh"),
         hyperbolic_interval(B/2,"cosh"))
    lips=original_physical_source_lipschitz(sources)
    Kglobal=original_full_second_derivative_upper(sources)
    Kthird=original_third_spatial_moment(sources)
    assert len(Kthird)==PHYS

    out={policy:{order:(zero(),zero()) for order in ORDERS}
         for policy in POLICIES}
    count={order:{"midpoint":0,"affine":0} for order in ORDERS}
    diagnostics=[]
    for left,right,name in panels:
        width=right-left
        half=width/2
        mid=(left+right)/2
        low,high,meta=positive_cell_weight_interval(left,right)
        low=down(low);high=up(high)
        assert F(0)<low<=high
        old=original_exact_physical_fourier_midpoint(mid,centers,sources,hyp)
        local=local_source_first_derivative_at_midpoint(mid,centers,sources,hyp)
        cell_d=[min(lips[i],local[i]+Kglobal[i]*half)
                for i in range(PHYS)]
        vold,eold=transformed_frequency(
            [v for v,r in old],[r for v,r in old],
            cell_d,a,c,half)
        base_delta=up(2*sqrt_upper(sum((z*z for z in vold),F(0))*
                                    sum((z*z for z in eold),F(0)))+
                      sum((z*z for z in eold),F(0)))
        original_d,second=original_midpoint_derivative_intervals(
            mid,centers,sources,hyp)
        K=[]
        for global_bound,local_second,third in zip(Kglobal,second,Kthird):
            local_bound=(abs_cap(local_second)+third*half
                         if local_second is not None else global_bound)
            K.append(min(global_bound,local_bound))
        v,d,e=transformed_affine(old,original_d,K,a,c,half)
        aff_delta,v2,d2,e2=exact_affine_error(v,d,e,half)

        for order in ORDERS:
            wl,wu=(low,high) if order=="one" else (low*low,high*high)
            add_policy_cell(out,order,"midpoint",vold,None,base_delta,
                            width,wl,wu)
            add_policy_cell(out,order,"affine",v,d,aff_delta,
                            width,wl,wu)
            # Cellwise selection maximizes full-source LOWER TRACE,
            # not an invalid assumption of componentwise Loewner order.
            base_trace=2*width*wl*(sum((x*x for x in vold),F(0))
                                   -N*base_delta)
            aff_trace=2*width*wl*(v2+width*width*d2/12
                                  -N*aff_delta)
            use="affine" if aff_trace>base_trace else "midpoint"
            count[order][use]+=1
            add_policy_cell(out,order,"adaptive",
                            v if use=="affine" else vold,
                            d if use=="affine" else None,
                            aff_delta if use=="affine" else base_delta,
                            width,wl,wu)
        diagnostics.append({
            "region":name,"left":str(left),"right":str(right),
            "original_multiplier_lower":str(low),
            "original_multiplier_upper":str(high),
            "midpoint_complete_covariance_error":str(base_delta),
            "affine_complete_covariance_error":str(aff_delta),
            "affine_derivative_reference_norm_sq":str(up(d2)),
            "affine_remainder_norm_sq":str(up(e2)),
            "first_moment_trace_gain_before_rounding":str(
                2*width*low*(v2+width*width*d2/12
                              -N*aff_delta
                              -sum((x*x for x in vold),F(0))
                              +N*base_delta))
        })
    assert len(diagnostics)==24
    assert sum(count["one"].values())==24
    assert sum(count["two"].values())==24

    policies={}
    for policy in POLICIES:
        rows={}
        for order in ORDERS:
            L,U,erlo,erhi=finalize(out[policy][order])
            tlo=sum((L[i][i] for i in range(N)),F(0))
            thi=sum((U[i][i] for i in range(N)),F(0))
            lo_inertia=exact_inertia_general(L)
            hi_inertia=exact_inertia_general(U)
            assert sum(lo_inertia)==sum(hi_inertia)==N
            rows[order]={
                "lower_trace":str(tlo),
                "upper_trace":str(thi),
                "lower_reference_exact_inertia":{
                    "positive":lo_inertia[0],"negative":lo_inertia[1],
                    "zero":lo_inertia[2]},
                "upper_reference_exact_inertia":{
                    "positive":hi_inertia[0],"negative":hi_inertia[1],
                    "zero":hi_inertia[2]},
                "complete_24x24_lower":[[str(x) for x in r] for r in L],
                "complete_24x24_upper":[[str(x) for x in r] for r in U],
                "whole_matrix_outward_lower_rounding":str(erlo),
                "whole_matrix_outward_upper_rounding":str(erhi)
            }
        policies[policy]=rows
    # Faithfully replay the same MG13 midpoint selection and matrix
    # export (both have identical SM43 multiplier / 24 panels).
    baseline=policies["midpoint"]
    ref={"one":("-0.003790888628","0.006270752428"),
         "two":("-0.000003827808","0.000006305924")}
    for order,(lo,hi) in ref.items():
        got=baseline[order]
        assert abs(F(got["lower_trace"])-F(lo))<F(1,10**9)
        assert abs(F(got["upper_trace"])-F(hi))<F(1,10**9)

    gain={}
    for order in ORDERS:
        bb=baseline[order]
        aa=policies["affine"][order]
        zz=policies["adaptive"][order]
        gain[order]={
            "affine_lower_trace_gain_over_baseline":str(
                F(aa["lower_trace"])-F(bb["lower_trace"])),
            "adaptive_lower_trace_gain_over_baseline":str(
                F(zz["lower_trace"])-F(bb["lower_trace"])),
            "affine_upper_trace_reduction_over_baseline":str(
                F(bb["upper_trace"])-F(aa["upper_trace"])),
            "affine_selected_cells":count[order]["affine"],
            "midpoint_selected_cells":count[order]["midpoint"],
            "affine_lower_reference_trace_positive":F(aa["lower_trace"])>0,
            "adaptive_lower_reference_trace_positive":F(zz["lower_trace"])>0,
            "affine_lower_reference_PSD_certified":
                aa["lower_reference_exact_inertia"]["negative"]==0
                and aa["lower_reference_exact_inertia"]["zero"]==0,
            "adaptive_lower_reference_PSD_certified":
                zz["lower_reference_exact_inertia"]["negative"]==0
                and zz["lower_reference_exact_inertia"]["zero"]==0
        }
    interpretation=(
        "DIRECTIONAL_AFFINE_SOURCE_MOMENT_METHOD_IMPROVEMENT"
        if any(F(gain[k]["adaptive_lower_trace_gain_over_baseline"])>
               F(1,10**9) for k in ORDERS)
        else "NO_MATERIAL_LOWER_TRACE_GAIN_FROM_AFFINE_ON_TEST_PANELS"
    )
    return {
        "status":"SCOPED_EXACT_ORIGINAL_24CHANNEL_AFFINE_FIRST_SECOND_SOURCE_MOMENTS",
        "canonical_W_ODD_NEG":"OPEN",
        "MG13_final_head_passing_actions_run":39344652841,
        "physical_original_source_count":25,
        "boundary_adapted_source_count":23,
        "original_odd_sinh_pole_included_as_channel":True,
        "total_coupled_source_channels":N,
        "source_panel_cell_count":len(diagnostics),
        "source_frequency_panel_regions":[{"a":str(x),"b":str(y),"name":n}
                                         for x,y,n in spans],
        "same_original_true_a_o_multiplier_and_pole_as_MG13":True,
        "genuine_original_Fourier_affine_midpoint_derivative_intervals":True,
        "all_576_mixed_source_covariances_preserved":True,
        "second_moment_is_Ao_squared_not_Astar_squared":True,
        "rational_complete_source_affine_Taylor_error_paid":True,
        "source_cell_Fourier_diagnostics":diagnostics,
        "policies":policies,
        "adaptive_selection_counts":count,
        "certified_method_comparison":gain,
        "exact_24D_lower_reference_spectral_classification_completed":True,
        "no_negative_lower_reference_direction_claimed_as_actual_negative":True,
        "interpretation":interpretation,
        "complete_low_band_zero_to_cutoff_certified":False,
        "genuine_original_Astar_squared_pole_response_certified":False,
        "genuine_original_23D_strong_Galerkin_residual_certified":False,
        "original_full470_resolvent_and_infinite_odd_remainder":"OPEN",
        "even_Weil_CC27_RH":"OPEN",
        "independent_original_Fourier_form_domain_audit":"OPEN",
        "decision":"Accept original selected-panel matrices only; require full-band coupled integration, physical Gram and pole correction, and actual strong residual before any complete operator promotion."
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",default="artifacts/mg14_original_affine_coupled_moments.json")
    args=parser.parse_args()
    result=source_panel_run()
    file=ROOT/args.output
    file.parent.mkdir(parents=True,exist_ok=True)
    file.write_text(json.dumps(result,indent=2)+"\n")
    print("MG14 original true coupled affine two moments:",json.dumps({
        "source_channels":N,"panels":result["source_panel_cell_count"],
        "choice_counts":result["adaptive_selection_counts"],
        "gains":result["certified_method_comparison"],
        "method":result["interpretation"],
        "complete_original_odd_even_Weil_RH":"OPEN"
    }),flush=True)

if __name__=="__main__":
    main()
