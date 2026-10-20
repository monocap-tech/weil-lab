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
import sys
sys.set_int_max_str_digits(0)
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

PRIMES=(2147483647,2147483629,1000000007,1000000009,998244353,2305843009213693951)

def modular_rank(rows,n,p):
    """Exact reduction of rational source vectors to F_p, with
    a nonzero 24x24 witness when full rank; never infer missing rank
    from a rank-deficient modular reduction.
    """
    assert len(rows)>=n and all(len(row)==n for row in rows)
    A=[]
    for row in rows:
        z=[]
        for x in row:
            x=F(x)
            den=x.denominator%p
            if den==0:
                return None
            z.append((x.numerator%p)*pow(den,-1,p)%p)
        A.append(z)
    basis={}
    ids={}
    for ix,row in enumerate(A):
        x=row[:]
        for pivot in sorted(basis):
            if x[pivot]:
                factor=x[pivot]
                base=basis[pivot]
                for j in range(pivot,n):
                    x[j]=(x[j]-factor*base[j])%p
        for pivot in range(n):
            if x[pivot]:
                inv=pow(x[pivot],-1,p)
                for j in range(pivot,n):
                    x[j]=(x[j]*inv)%p
                basis[pivot]=x
                ids[pivot]=ix
                break
        if len(basis)==n:break
    pivots=sorted(basis)
    witness_ids=[ids[i] for i in pivots]
    return {"prime":p,"rank_lower_bound":len(pivots),
            "independent_row_indices":witness_ids,
            "independent_row_residues":[A[i] for i in witness_ids]}

def certified_modular_rank(rows,n):
    best=None
    for prime in PRIMES:
        got=modular_rank(rows,n,prime)
        if got is None:continue
        if best is None or got["rank_lower_bound"]>best["rank_lower_bound"]:
            best=got
        if got["rank_lower_bound"]==n:break
    assert best is not None, "all modular primes divide a source denominator"
    return best

def strict_positive_dyadic_lower(x):
    """Small exact rational witness, avoiding multi-thousand-digit I/O."""
    x=F(x)
    assert x>0
    k=max(0,x.denominator.bit_length()-x.numerator.bit_length()+2)
    y=F(1,2**k)
    assert 0<y<=x
    return y,k

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
    vals=[];derivatives=[];details=[]
    reference_trace_lower={1:None,2:None}
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
            # A direct, analytic, exact rational source-trace lower:
            # smallest eigen of the 2x2 weight Gram >= det/trace,
            # hence any nonzero (v_i,d_i) contributes positively.
            # This does NOT claim it lower bounds the true source form.
            if reference_trace_lower[p] is None:
                i=next((i for i in range(N) if v[i] or slopes[i]),None)
                if i is not None:
                    reference_trace_lower[p]=2*gramdet*(
                        v[i]**2+slopes[i]**2)/(J[0]+J[2])
            diag["moment_"+str(p)+"_strict_positive_determinant"]=True
            diag["moment_"+str(p)+"_J1"]=str(J[1])
        details.append(diag)
    rank_values=certified_modular_rank(vals,N)
    rank_derivatives=certified_modular_rank(derivatives,N)
    rank_combined=certified_modular_rank(vals+derivatives,N)
    assert rank_combined["rank_lower_bound"]>=rank_values["rank_lower_bound"]
    assert rank_combined["rank_lower_bound"]>=rank_derivatives["rank_lower_bound"]
    assert rank_combined["rank_lower_bound"]==N, (
        "No full 24D modular witness found: inconclusive source-span gate, "
        "not an actual rank-deficiency proof",rank_combined)
    # Each reference-weight 2x2 moment Gram is strictly SPD.
    # Hence R_p=2 sum_j B_j^T J_j^p B_j is SPD exactly when the
    # 48x24 rational affine source frame B has rank 24.
    data={}
    for p in (1,2):
        lower=reference_trace_lower[p]
        assert lower is not None and lower>0
        data["one" if p==1 else "two"]={
            "exact_affine_reference_inertia":{
                "positive":N,"negative":0,"zero":0},
            "certified_positive_affine_reference_trace_lower":str(strict_positive_dyadic_lower(lower)[0]),
            "certified_positive_affine_trace_dyadic_exponent":strict_positive_dyadic_lower(lower)[1],
            "ideal_affine_reference_rank":N,
            "weighted_moment_strict_positive_every_cell":True,
            "ideal_inertia_proved_by_modular_full_rank_and_positive_exact_weight_moments":True
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
        "rational_source_midpoint_rank_lower_bound":rank_values["rank_lower_bound"],
        "rational_source_derivative_rank_lower_bound":rank_derivatives["rank_lower_bound"],
        "rational_source_affine_combined_rank":rank_combined["rank_lower_bound"],
        "modular_source_affine_rank_witness":rank_combined,
        "true_exact_affine_24D_ideal_reference_inertia_by_positive_Gram":True,
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
        "interpretation":"Exact 24D rational affine REFERENCE rank from mod-p nonzero determinant plus analytic positive 2x2 weighted moments. This proves ideal reference SPD, not a lower bound for the true original source operator or an RH result."
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
        "v_rank_floor":d["rational_source_midpoint_rank_lower_bound"],
        "d_rank_floor":d["rational_source_derivative_rank_lower_bound"],
        "combined_rank":d["rational_source_affine_combined_rank"],
        "ideal_moments":d["weighted_ideal_first_second_source_reference"],
        "modular_witness_prime":d["modular_source_affine_rank_witness"]["prime"],
        "complete_actual_odd_even_Weil_RH":"OPEN"
    }),flush=True)

if __name__=="__main__":
    main()
