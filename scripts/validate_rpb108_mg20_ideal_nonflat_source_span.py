#!/usr/bin/env python3
"""MG20: exact ideal affine source-SPAN versus conservative lower-reference gate.

MG17's 24 truly NONFLAT ORIGINAL real frequency cells have complete
positive affine weight reference moments J0,J1,J2. Earlier MG18/MG19
retain 21 negative LOWER-REFERENCE directions despite strong positive
trace gains. Is there a structural lack of affine source excitation,
or are the negativity certificates mainly interval/error losses?

MG20 constructs, on the SAME 24 real original cells and the SAME
23 exactly dual-boundary-vanishing source functions + true odd sinh
pole, complete rational IDEAL Fourier-affine reference:
 R_p = 2 sum_cells [J0 vv^T + J1(vd^T+dv^T)+J2 dd^T], p=1,2.
It computes exact rational inertia and row-span ranks of the actual
rational center/source derivative vectors, and exact certified
J0*J2-J1²>0 on each cell.

IMPORTANT: R_p is the rational REFERENCE operator, not a rigorous
lower bound for the true original Fourier integral. True source
midpoint, derivative, and multiplier errors are NOT in R_p.
A positive reference must never be promoted to operator positivity.
The actual complete original Ao/Ao² source lower references remain
indefinite, and source470/even/Weil/RH remain OPEN.

This gate identifies a finite-frequency source-excitation bottleneck
separately from the rigorous error-envelope bottleneck.
"""
import argparse
import json
from fractions import Fraction as F
from validate_rpb108_mg17_nonflat_multiplier_scout import scout
from validate_rpb108_mg16_weighted_affine_source_moments import (
    ROOT,N,PHYS,PIVOT,POLE,B,ORDERS,
    original_source_centered_windows,original_full_25_physical_interval_gram,
    protected_inner_cover,boundary_intervals,derivative_intervals_and_D3,
    interval_out,pair_coefficients,positive_gap,
    hyperbolic_interval,original_full_second_derivative_upper,
    original_exact_physical_fourier_midpoint,
    original_midpoint_derivative_intervals,original_third_spatial_moment,
    transformed_affine,abs_cap,moments_reference,
    covariance_matrices,zero
)
from validate_rpb108_sm62_full25_338signed_positive import exact_inertia_general

def exact_rank(rows,n):
    """Fraction row-echelon rank with pivot elimination in source space."""
    pivots={}
    for original in rows:
        x=[F(z) for z in original]
        assert len(x)==n
        for p in sorted(pivots):
            if x[p]:
                t=x[p]
                q=pivots[p]
                for j in range(p,n):
                    x[j]-=t*q[j]
        for p in range(n):
            if x[p]:
                t=x[p]
                for j in range(p,n):
                    x[j]/=t
                pivots[p]=x
                break
        if len(pivots)==n:
            break
    return sorted(pivots)

def full_original_reference():
    sites=scout()
    assert sites["selected_cell_count"]==24
    centers,sources,_=original_source_centered_windows()
    H,physical,_=original_full_25_physical_interval_gram()
    assert physical==sources and len(H)==PHYS
    clusters,*_=protected_inner_cover()
    b=[interval_out(x) for x in boundary_intervals(sources,clusters)]
    bd,_=derivative_intervals_and_D3(sources,clusters)
    free=tuple(i for i in range(PHYS) if i not in (PIVOT,POLE))
    det,a,c=pair_coefficients(b,bd,PIVOT,free)
    assert positive_gap(det)>0 and len(free)==23
    hyp=(hyperbolic_interval(B/2,"sinh"),
         hyperbolic_interval(B/2,"cosh"))
    k2=original_full_second_derivative_upper(sources)
    k3=original_third_spatial_moment(sources)
    R={p:zero() for p in (1,2)}
    vals=[];derivatives=[];details=[]
    for site in sites["selected_nonflat_original_cells"]:
        left,right=F(site["left"]),F(site["right"])
        width=right-left;half=width/2;mid=(left+right)/2
        old=original_exact_physical_fourier_midpoint(
            mid,centers,sources,hyp)
        d,second=original_midpoint_derivative_intervals(
            mid,centers,sources,hyp)
        curv=[min(k2[i],abs_cap(second[i])+k3[i]*half)
              if second[i] is not None else k2[i]
              for i in range(PHYS)]
        v,slopes,radii=transformed_affine(old,d,curv,a,c,half)
        assert len(v)==len(slopes)==N and all(z>=0 for z in radii)
        reference,meta=moments_reference(left,right,centers,sources)
        assert meta["type"]=="signed_positive_part_affine"
        vals.append(v);derivatives.append(slopes)
        diag={"left":str(left),"right":str(right),
              "source_midpoint_sq":str(sum(t*t for t in v)),
              "source_affine_derivative_sq":str(sum(t*t for t in slopes)),
              "source_error_radius_sq":str(sum(t*t for t in radii))}
        for p in (1,2):
            J,eta=reference[p]
            assert J[0]>0 and J[2]>0
            gramdet=J[0]*J[2]-J[1]*J[1]
            # A genuinely positive weight on a full nonzero-width
            # interval gives strictly positive 2x2 moment Gram.
            assert gramdet>0
            cell=covariance_matrices(v,slopes,J)
            for i in range(N):
                for j in range(N):
                    R[p][i][j]+=2*cell[i][j]
            diag["moment_"+str(p)+"_strict_positive_determinant"]=True
            diag["moment_"+str(p)+"_J1"]=str(J[1])
        details.append(diag)
    rank_values=exact_rank(vals,N)
    rank_derivatives=exact_rank(derivatives,N)
    rank_combined=exact_rank(vals+derivatives,N)
    assert rank_combined>=rank_values and rank_combined>=rank_derivatives
    data={}
    for p in (1,2):
        A=R[p]
        assert all(A[i][j]==A[j][i] for i in range(N) for j in range(N))
        inertia=exact_inertia_general(A)
        assert sum(inertia)==N and inertia[1]==0
        # The ideal weighted affine reference is positive semidefinite
        # by construction, independent of source/multiplier uncertainty.
        assert inertia[0]==len(rank_combined), (
            "ideal rational weighted affine moment rank mismatch",p,inertia,rank_combined)
        data["one" if p==1 else "two"]={
            "exact_affine_reference_inertia":dict(zip(
                ("positive","negative","zero"),inertia)),
            "exact_positive_affine_reference_trace":str(
                sum(A[i][i] for i in range(N))),
            "ideal_affine_reference_rank":inertia[0],
            "weighted_moment_strict_positive_every_cell":True
        }
    return {
        "status":"EXACT_IDEAL_NONFLAT_ORIGINAL_SOURCE_REFERENCE_SPAN_GATE",
        "canonical_W_ODD_NEG":"OPEN",
        "original_physical_source_catalog_25":True,
        "double_boundary_adapted_sources":23,
        "original_odd_sinh_pole_channel":True,
        "original_source_channels":N,
        "true_original_nonflat_frequency_cells_verified":24,
        "same_true_original_nonflat_cells_as_MG17_MG18_MG19":True,
        "rational_source_midpoint_only_rank":len(rank_values),
        "rational_source_derivative_only_rank":len(rank_derivatives),
        "rational_source_affine_combined_rank":len(rank_combined),
        "weighted_ideal_first_second_source_reference":data,
        "all_24_original_affine_cells_positive_moment_Gram":True,
        "all_576_mixed_source_entries_preserved_in_affine_reference":True,
        "all_source_and_multiplier_remainder_omitted_from_ideal_reference":True,
        "original_true_24_channel_lower_reference_inertia_still_unsolved_by_ideal_rank":True,
        "complete_original_low_band_certified":False,
        "genuine_Astar_squared_source_moment_certified":False,
        "actual_strong_Galerkin_residual_certified":False,
        "original_470D_odd_operator_complete":"OPEN",
        "even_Weil_CC27_RH":"OPEN",
        "original_Fourier_form_domain_audit":"OPEN",
        "cell_source_diagnostics":details,
        "interpretation":"Exact positive rank of rational affine SOURCE REFERENCE, not a lower certificate for actual original source operator. Compare with MG19 LOWER reference 3+/21- as an error-envelope geometry audit."
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/mg20_ideal_original_nonflat_source_span.json")
    args=p.parse_args()
    d=full_original_reference()
    output=ROOT/args.output
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(d,indent=2)+"\n")
    print("MG20 ideal original nonflat affine source span:",json.dumps({
        "v_rank":d["rational_source_midpoint_only_rank"],
        "d_rank":d["rational_source_derivative_only_rank"],
        "combined_rank":d["rational_source_affine_combined_rank"],
        "ideal_moments":d["weighted_ideal_first_second_source_reference"],
        "complete_actual_odd_even_Weil_RH":"OPEN"
    }),flush=True)

if __name__=="__main__":
    main()
