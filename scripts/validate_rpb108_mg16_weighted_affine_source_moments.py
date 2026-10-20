#!/usr/bin/env python3
"""MG16: TRUE original SM46 weighted affine J0/J1/J2 two-moment gate.

Only SAME 24 real-frequency cells and SAME original 24 channels as
passing MG15: MG11's 23 actual double-boundary-vanishing physical
source functions plus true sinh pole.

On every cell SM43A supplies a positive rational reference weight
w_ref(xi)=constant or max(kappa, certified affine signed interpolant),
and a rigorous pointwise |w_true-w_ref|<=eps_w. We integrate both
w_ref and w_ref^2 TIMES the complete affine source covariance
(v+d*(xi-mid))(v+d*(xi-mid))^T with exact rational moments J0,J1,J2.

MG15's actual source-coordinate Taylor errors |e_i|<=r_i imply
ee^T<=D_r=(sum r_i)diag(r_i). With 0<tau<1:
 (1-tau)C_w-(1/tau-1)J0 D_r <= int w_ref TT^T
 <= (1+tau)C_w+(1+1/tau)J0 D_r.
For |w_true^p-w_ref^p|<=eta_p (p=1,2), each original true
T_i has |T_i|<=q_i=|v_i|+h|d_i|/2+r_i.
TT^T<=D_q=(sum q_i)diag(q_i); consequently multiplier mismatch
costs at most width*eta_p*D_q in FULL Loewner order.
Multiply all by 2 for the two original Fourier-frequency signs.

This pays multiplier mismatch, source correlation, true pole and all
24x24 crosses. It is an independently certified 24-cell SOURCE-MOMENT
enclosure, not an original full low band or Astar squared residual.

Compare complete 24x24 results against independently rebuilt,
verified MG15 original scalar/source-weighted matrices and exact
rational lower-reference inertias; no automatic spectral promotion.
"""
import argparse,json
from fractions import Fraction as F
from math import comb
from validate_rpb108_mg15_directional_affine_covariance import (
 ROOT,N,PHYS,POLE,PIVOT,B,ORDERS,TAUS,LABELS,
 full_measured_run,
 original_source_centered_windows,
 original_full_25_physical_interval_gram,
 protected_inner_cover,boundary_intervals,derivative_intervals_and_D3,
 interval_out,pair_coefficients,positive_gap,panel_windows,
 hyperbolic_interval,original_full_second_derivative_upper,
 original_exact_physical_fourier_midpoint,
 original_midpoint_derivative_intervals,original_third_spatial_moment,
 transformed_affine,abs_cap,zero,sym,add_rank_one,finalize
)
from validate_rpb108_sm43_positive_affine_error import affine_cell_error
from validate_rpb108_sm46_affine_physical_fourier_source import (
 positive_reference_moments,arch_lower_at,arch_upper_at,prime_interval,
 KAPPA
)
from validate_rpb108_sm43_positive_cell_envelope import (
 positive_cell_weight_interval
)
from validate_rpb108_sm62_full25_338signed_positive import exact_inertia_general
from validate_rpb108_si06_negative_band import PI

POLICIES=("weighted_best",)
CHOSEN_TAUS=TAUS

def poly_integral(n,p,a,b,lo,hi):
    """Integral (t-1/2)^n (a+b*t)^p over a rational interval."""
    assert 0<=n<=2 and p in (1,2)
    z=F(0)
    for i in range(n+1):
        for j in range(p+1):
            m=i+j+1
            z+=(F(comb(n,i)*comb(p,j))*(-F(1,2))**(n-i)*
                 a**(p-j)*b**j*(hi**m-lo**m)/m)
    return z

def moments_reference(left,right,centers,sources):
    width=right-left
    assert width>0
    _,meta=affine_cell_error(left,right,centers,sources)
    choice=meta["reference_choice"]
    if choice=="original_constant_cell":
        low,hi,_=positive_cell_weight_interval(left,right)
        ref=(low+hi)/2
        eps=(hi-low)/2
        assert ref>=KAPPA and eps>=0
        return {
         p:([width**(n+1)*ref**p*(F(1,12) if n==2 else
                 F(1) if n==0 else F(0)) for n in range(3)],
            eps if p==1 else eps*(2*ref+eps))
         for p in (1,2)},{
           "type":choice,"reference_max":ref,
           "original_weight_error":eps}
    assert choice=="signed_positive_part_affine"
    mla=arch_lower_at(left)+prime_interval(left)[0]
    mua=arch_upper_at(left)+prime_interval(left)[1]
    mlb=arch_lower_at(right)+prime_interval(right)[0]
    mub=arch_upper_at(right)+prime_interval(right)[1]
    va=(mla+mua)/2;vb=(mlb+mub)/2
    slope=vb-va
    pieces=[]
    if va>=KAPPA and vb>=KAPPA:
        pieces=[(F(0),F(1),va,slope)]
    elif va<=KAPPA and vb<=KAPPA:
        pieces=[(F(0),F(1),KAPPA,F(0))]
    else:
        assert slope!=0
        t=(KAPPA-va)/slope
        assert 0<t<1
        if va<KAPPA:
            pieces=[(F(0),t,KAPPA,F(0)),(t,F(1),va,slope)]
        else:
            pieces=[(F(0),t,va,slope),(t,F(1),KAPPA,F(0))]
    refmax=max(KAPPA,va,vb)
    eps=(meta["signed_original_endpoint_interval_max_width"]/2+
         meta["exact_curvature_error"])
    assert eps>=0
    result={}
    for p in (1,2):
        m=[width**(n+1)*sum(
             (poly_integral(n,p,a,b,lo,hi) for lo,hi,a,b in pieces),F(0))
           for n in range(3)]
        eta=eps if p==1 else eps*(2*refmax+eps)
        result[p]=(m,eta)
    J,_=positive_reference_moments(left,right,meta),meta
    assert result[1][0]==J
    assert result[1][0][0]>0 and result[2][0][0]>0
    return result,{"type":choice,"reference_max":refmax,
                   "original_weight_error":eps}

def add_sym_cross(A,v,d,coef):
    for i in range(N):
        for j in range(i,N):
            A[i][j]+=coef*(v[i]*d[j]+d[i]*v[j])

def covariance_matrices(v,d,J):
    """Exact weighted correlated affine vv,vd+dv,dd; PSD reference."""
    j0,j1,j2=J
    A=zero()
    add_rank_one(A,v,j0)
    add_sym_cross(A,v,d,j1)
    add_rank_one(A,d,j2)
    return sym(A)

def true_cell_add(matrices,policy,order,C,J0,eta,width,q,r,tau):
    assert width>0
    lo,hi=matrices[policy][order]
    S=sum(r,F(0));Q=sum(q,F(0))
    for i in range(N):
        for j in range(i,N):
            lo[i][j]+=2*(1-tau)*C[i][j]
            hi[i][j]+=2*(1+tau)*C[i][j]
    for i in range(N):
        lo[i][i]-=2*((1/tau-1)*J0*S*r[i]+width*eta*Q*q[i])
        hi[i][i]+=2*((1+1/tau)*J0*S*r[i]+width*eta*Q*q[i])

def weighted_lower_trace(C,J0,eta,width,q,r,tau):
    return 2*((1-tau)*sum((C[i][i] for i in range(N)),F(0))
      -(1/tau-1)*J0*sum(r,F(0))**2
      -width*eta*sum(q,F(0))**2)

def exact_weighted_regression():
    # Reference integral of (1+t)^2 * [v+d*t]^2, with nonzero
    # off-diagonal mixed source components.
    left=F(-1,3);right=F(2,3)
    for p in (1,2):
        J=[poly_integral(n,p,F(1),F(1),left,right)
           for n in range(3)]
        assert J[0]>0 and J[2]>0
        v=[F(2),F(-3)]; d=[F(4),F(5)]
        C=[[J[0]*v[i]*v[j]+J[1]*(v[i]*d[j]+d[i]*v[j])
             +J[2]*d[i]*d[j] for j in range(2)] for i in range(2)]
        assert C[0][1]==C[1][0]
        # Polynomial evaluation at 4 points gives an independent
        # exact interpolation proof for degree<=4.
        def poly_eval(t,i,j):
            return (1+t)**p*(v[i]+d[i]*t)*(v[j]+d[j]*t)
        nodes=[F(-2),F(-1),F(0),F(1),F(2)]
        for i,j in ((0,0),(0,1),(1,1)):
            vals=[poly_eval(t,i,j) for t in nodes]
            assert any(vals)
            # Explicit full polynomial expansion via binomial.
            total=F(0)
            for m in range(p+1):
                coeff=F(comb(p,m))
                terms=((0,v[i]*v[j]),
                       (1,v[i]*d[j]+v[j]*d[i]),
                       (2,d[i]*d[j]))
                for n,x in terms:
                    degree=n+m
                    total+=coeff*x*(right**(degree+1)-
                                    left**(degree+1))/(degree+1)
            assert total==C[i][j]
    return True

def run():
    assert exact_weighted_regression()
    previous=full_measured_run()
    assert previous["same_24_frequency_cells_as_MG14"]
    assert previous["exact_MG14_full_24x24_baseline_replayed"]
    centers,sources,_=original_source_centered_windows()
    gram,physical,_=original_full_25_physical_interval_gram()
    assert physical==sources and len(sources)==PHYS
    clusters,*_=protected_inner_cover()
    b=[interval_out(x) for x in boundary_intervals(sources,clusters)]
    bd,_=derivative_intervals_and_D3(sources,clusters)
    free=tuple(i for i in range(PHYS) if i not in (PIVOT,POLE))
    determinant,a,c=pair_coefficients(b,bd,PIVOT,free)
    assert positive_gap(determinant)>0
    panels,spans=panel_windows(centers,sources)
    hyp=(hyperbolic_interval(B/2,"sinh"),
         hyperbolic_interval(B/2,"cosh"))
    kg=original_full_second_derivative_upper(sources)
    k3=original_third_spatial_moment(sources)
    choices=tuple("tau_"+str(t.numerator)+"_"+str(t.denominator)
                  for t in CHOSEN_TAUS)
    names=choices+POLICIES
    matrices={name:{order:(zero(),zero()) for order in ORDERS}
              for name in names}
    selected={order:{name:0 for name in choices} for order in ORDERS}
    diagnostics=[]
    for left,right,region in panels:
        width=right-left
        mid=(left+right)/2
        half=width/2
        vals=original_exact_physical_fourier_midpoint(
            mid,centers,sources,hyp)
        derivatives,second=original_midpoint_derivative_intervals(
            mid,centers,sources,hyp)
        K=[]
        for full,sp,third in zip(kg,second,k3):
            K.append(min(full,abs_cap(sp)+third*half)
                     if sp is not None else full)
        v,d,r=transformed_affine(vals,derivatives,K,a,c,half)
        q=[abs(v[i])+half*abs(d[i])+r[i] for i in range(N)]
        assert all(x>=0 for x in q)
        results,meta=moments_reference(left,right,centers,sources)
        diag={"cell_left":str(left),"cell_right":str(right),
              "region":region,"reference_kind":meta["type"],
              "multiplier_mismatch":str(meta["original_weight_error"])}
        for order in ORDERS:
            exponent=1 if order=="one" else 2
            J,eta=results[exponent]
            C=covariance_matrices(v,d,J)
            scored=[(weighted_lower_trace(C,J[0],eta,width,q,r,t),name,t)
                    for name,t in zip(choices,CHOSEN_TAUS)]
            _,best_name,best_tau=max(scored,key=lambda x:(x[0],-CHOSEN_TAUS.index(x[2])))
            selected[order][best_name]+=1
            for name,t in zip(choices,CHOSEN_TAUS):
                true_cell_add(matrices,name,order,C,J[0],eta,width,q,r,t)
            true_cell_add(matrices,"weighted_best",order,C,J[0],eta,
                          width,q,r,best_tau)
            diag[order+"_weighted_J"]=[str(z) for z in J]
            diag[order+"_squared_radii"] = str(sum((x*x for x in r),F(0)))
            diag[order+"_multiplier_fee_trace"]=str(
                2*width*eta*sum(q,F(0))**2)
            diag[order+"_best_tau"]=str(best_tau)
        diagnostics.append(diag)
    assert len(diagnostics)==24
    result={}
    for name in names:
        result[name]={}
        for order in ORDERS:
            L,U,lf,uf=finalize(matrices[name][order])
            inertia=exact_inertia_general(L)
            assert sum(inertia)==N
            result[name][order]={
                "complete_24x24_lower":[[str(x) for x in row] for row in L],
                "complete_24x24_upper":[[str(x) for x in row] for row in U],
                "lower_trace":str(sum((L[i][i] for i in range(N)),F(0))),
                "upper_trace":str(sum((U[i][i] for i in range(N)),F(0))),
                "lower_exact_inertia":dict(zip(
                    ("positive","negative","zero"),inertia)),
                "whole_matrix_lower_export_fee":str(lf),
                "whole_matrix_upper_export_fee":str(uf)
            }
    baseline=previous["candidate_matrices"]["adaptive"]
    gain={}
    for order in ORDERS:
        best=result["weighted_best"][order]
        old=baseline[order]
        gain[order]={
            "MG15_lower_reference_exact_inertia":old["lower_exact_inertia"],
            "MG16_weighted_lower_reference_exact_inertia":best["lower_exact_inertia"],
            "MG15_lower_trace":old["lower_trace"],
            "MG16_weighted_lower_trace":best["lower_trace"],
            "lower_trace_gain_over_MG15":str(F(best["lower_trace"])-F(old["lower_trace"])),
            "upper_trace_reduction_over_MG15":str(F(old["upper_trace"])-F(best["upper_trace"])),
            "negative_lower_reference_directions_recovered":
                old["lower_exact_inertia"]["negative"]-best["lower_exact_inertia"]["negative"],
            "MG16_weighted_reference_strict_PSD":(
                best["lower_exact_inertia"]["negative"]==0 and
                best["lower_exact_inertia"]["zero"]==0)
        }
    return {
        "status":"SCOPED_TRUE_ORIGINAL_WEIGHTED_SOURCE_AFFINE_FIRST_SECOND_MOMENTS",
        "canonical_W_ODD_NEG":"OPEN",
        "source25_original_physical_and_true_pole":True,
        "boundary_adapted_source_count":23,
        "coupled_source_channels":N,
        "selected_original_real_frequency_cells":24,
        "same_original_24_cells_as_MG15":True,
        "original_107_cluster_physical_sources_replayed":True,
        "original_true_SM43A_multiplier_reference_J012":True,
        "original_reference_squared_weight_J012_exact":True,
        "complete_original_source_pole_mixed_matrices":True,
        "exact_reference_covariance_vv_vd_dd":True,
        "sourcewise_diagonal_error_and_true_multiplier_gap_paid":True,
        "full_MG15_independent_exact_matrix_and_inertia_replay":True,
        "whole_frequency_zero_to_cutoff_covered":False,
        "original_Astar_squared_pole_action_completed":False,
        "original_true_23D_Galerkin_strong_residual_certified":False,
        "actual_470_source_resolvent_and_infinite_odd_remainder":"OPEN",
        "even_Weil_CC27_RH":"OPEN",
        "independent_original_Fourier_closed_domain_premises_audit":"OPEN",
        "tau_candidates":[str(t) for t in CHOSEN_TAUS],
        "selected_tau_counts":selected,
        "cell_diagnostics":diagnostics,
        "complete_candidate_matrices":result,
        "comparison_to_MG15":gain,
        "decision":"Evaluate exact lower inertia vs MG15. If 21 weak lower directions persist, investigate correlated Fourier remainder Gram and full-band geometry rather than assume true negative operator modes."
    }
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/mg16_original_weighted_source_moments.json")
    args=p.parse_args()
    data=run()
    target=ROOT/args.output
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(data,indent=2)+"\n")
    print("MG16 original weighted genuine coupled moments:",json.dumps({
        "source_channels":N,
        "cells":data["selected_original_real_frequency_cells"],
        "results":data["comparison_to_MG15"],
        "selected":data["selected_tau_counts"],
        "complete_odd_even_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":
    main()
