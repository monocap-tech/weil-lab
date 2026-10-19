#!/usr/bin/env python3
"""MG13: first TRUE original coupled low-frequency A_o and A_o^2 matrices.

A 24-channel original physical source frame consists of MG12's 23
double-boundary-vanishing h_i=f_i-a_i*s-c_i*f_23 plus the actual sinh
pole s. For each selected real-frequency panel, exact SM43 original
seven-prime/digamma a_o intervals, SM44 exact physical Fourier source
midpoint intervals and SM45/46 analytic derivative bounds yield a
complete coupled Loewner bracket for:
  M1(Omega)=2 int_Omega a_o(xi) T(xi) T(xi)^t dxi,
  M2(Omega)=2 int_Omega a_o(xi)^2 T(xi) T(xi)^t dxi.
All 24*24 matrix crosses, including h_i/s pole, are preserved.

The source Fourier midpoint is the true interval of the ORIGINAL
supported source combination, not a sampled FFT or unverified
midpoint-coefficient transform. An exact full-operator covariance
error is paid by ±(2||v|| ||e||+||e||²) I on every cell.
A complete rational row-sum fee protects export rounding.

Selected panels cover only three original frequency intervals, NOT
the entire [0,Lambda] band. Thus M1/M2 are scoped direct coupled
SOURCE-frequency MOMENTS; the complete Galerkin strong residual,
Astar^2, 470D inverse, whole odd/even, Weil, CC27 and RH remain OPEN.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B
from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    I,hyperbolic_interval,original_full_25_physical_interval_gram)
from validate_rpb108_sm43_positive_cell_envelope import (
    positive_cell_weight_interval,original_source_centered_windows)
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    original_exact_physical_fourier_midpoint,
    original_physical_source_lipschitz,
    original_full_second_derivative_upper,sqrt_upper)
from validate_rpb108_sm44_physical_fourier_cell_gram import (
    local_source_first_derivative_at_midpoint)
from validate_rpb108_mg10_rank_one_endpoint_source_tail import boundary_intervals
from validate_rpb108_mg11_dual_boundary_trace_kernel import (
    derivative_intervals_and_D3,positive_gap,interval_out,up,down)
from validate_rpb108_mg12_double_trace_gram_lowband import pair_coefficients
from sm36_original_odd_numerical_pilot import ROOT,geometry,select_sources

PHYS=25
POLE=24
PIVOT=23
N=24
FEE_DEN=10**10
def compact_lower(A):
    n=len(A)
    q=[[F((A[i][j]*FEE_DEN).numerator//
           (A[i][j]*FEE_DEN).denominator,FEE_DEN)
        for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i):
            assert A[i][j]==A[j][i]
            assert q[i][j]==q[j][i]
    rad=max(sum((abs(A[i][j]-q[i][j]) for j in range(n)),F(0))
            for i in range(n))
    rad=up(rad)
    return [[q[i][j]-(rad if i==j else 0) for j in range(n)]
            for i in range(n)],rad
def compact_upper(A):
    q,fee=compact_lower(A)
    # compact_lower gives q-fee I, so recover q+fee I exactly.
    return [[q[i][j]+(2*fee if i==j else 0)
             for j in range(len(A))] for i in range(len(A))],fee
def zero():
    return [[F(0) for _ in range(N)] for _ in range(N)]
def add_rank_one(A,v,coeff):
    for i in range(N):
        for j in range(i,N):
            A[i][j]+=coeff*v[i]*v[j]
def sym(A):
    for i in range(N):
        for j in range(i):
            A[i][j]=A[j][i]
    return A
def panel_windows(centers,sources):
    selected=[]
    for typ,j,k in sources:
        if typ=="cluster" and j not in selected:
            selected.append(j)
    assert len(selected)==16
    spans=[(F(0),F(1,8),"origin_low"),
           (centers[selected[0]]-F(1,16),
            centers[selected[0]]+F(1,16),"cluster_A"),
           (centers[selected[1]]-F(1,16),
            centers[selected[1]]+F(1,16),"cluster_B")]
    spans.sort()
    assert all(F(0)<=a<b<=4096 for a,b,_ in spans)
    assert all(spans[i][1]<spans[i+1][0] for i in range(len(spans)-1))
    panels=[]
    for a,b,name in spans:
        for k in range(8):
            lo=a+(b-a)*F(k,8)
            hi=a+(b-a)*F(k+1,8)
            panels.append((lo,hi,name))
    assert len(panels)==24
    return panels,spans

def transformed_frequency(vmid,rad,deriv,coeff_a,coeff_c,half):
    old=[I(vmid[i]-rad[i],vmid[i]+rad[i]) for i in range(PHYS)]
    vec=[];err=[]
    for i in range(PHYS):
        if i==PIVOT or i==POLE:continue
        ai=coeff_a[i];ci=coeff_c[i]
        ti=interval_out(old[i]-ai*old[POLE]-ci*old[PIVOT])
        v=down(ti.mid())
        e=up(max(abs(ti.l-v),abs(ti.h-v))+
             (deriv[i]+max(abs(ai.l),abs(ai.h))*deriv[POLE]
              +max(abs(ci.l),abs(ci.h))*deriv[PIVOT])*half)
        vec.append(v);err.append(e)
    # Preserve true original sinh physical pole as channel #23:
    pole=old[POLE]
    vp=down(pole.mid())
    ep=up(max(abs(pole.l-vp),abs(pole.h-vp))+
          deriv[POLE]*half)
    vec.append(vp);err.append(ep)
    assert len(vec)==len(err)==24
    assert all(e>=0 for e in err)
    return vec,err

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/mg13_true_coupled_original_lowband_moments.json")
    args=p.parse_args()
    ledger=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in ledger["obligations"] if x["id"]=="W-ODD-NEG")
    assert ledger["active_obligation"]=="W-ODD-NEG"
    assert odd["status"]==ledger["objective"]["status"]=="open"
    assert ledger["governance"]["no_automatic_promotion"]
    assert all(x in odd["evidence"] for x in ("SM41","SM42","SI29"))
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==PHYS and sources[POLE][0]=="pole"
    gram,phys,_=original_full_25_physical_interval_gram()
    assert phys==sources and len(gram)==PHYS
    clusters,_,_,_,_=protected_inner_cover()
    b=[interval_out(x) for x in boundary_intervals(sources,clusters)]
    d,_=derivative_intervals_and_D3(sources,clusters)
    delta,a,c=pair_coefficients(b,d,PIVOT,
                                 tuple(i for i in range(PHYS)
                                       if i not in (PIVOT,POLE)))
    assert positive_gap(delta)>0
    panels,spans=panel_windows(centers,sources)
    hyp=(hyperbolic_interval(B/2,"sinh"),
         hyperbolic_interval(B/2,"cosh"))
    globalD=original_physical_source_lipschitz(sources)
    K2=original_full_second_derivative_upper(sources)
    L1=zero();U1=zero();L2=zero();U2=zero()
    er1l=er1u=er2l=er2u=F(0)
    weights=[];cellstats=[];near_kink=0
    for l,r,label in panels:
        mid=(l+r)/2;half=(r-l)/2
        wlo,whi,meta=positive_cell_weight_interval(l,r)
        wlo=down(wlo);whi=up(whi)
        assert F(0)<wlo<=whi
        near_kink+=bool(meta["cell_contains_possible_m_equals_kappa"])
        vals=original_exact_physical_fourier_midpoint(mid,centers,sources,hyp)
        derivatives=local_source_first_derivative_at_midpoint(
            mid,centers,sources,hyp)
        cellD=[min(globalD[i],derivatives[i]+K2[i]*half)
               for i in range(PHYS)]
        v,e=transformed_frequency(
            [val for val,_ in vals],[rad for _,rad in vals],
            cellD,a,c,half)
        v2=sum((x*x for x in v),F(0))
        e2=sum((x*x for x in e),F(0))
        delta_cov=up(2*sqrt_upper(v2*e2)+e2)
        assert delta_cov>=0
        h=2*(r-l) # whole-real positive and negative frequencies
        w1l=h*wlo;w1u=h*whi
        w2l=h*wlo*wlo;w2u=h*whi*whi
        add_rank_one(L1,v,w1l);add_rank_one(U1,v,w1u)
        add_rank_one(L2,v,w2l);add_rank_one(U2,v,w2u)
        er1l+=w1l*delta_cov;er1u+=w1u*delta_cov
        er2l+=w2l*delta_cov;er2u+=w2u*delta_cov
        weights.append((wlo,whi))
        cellstats.append({
            "region":label,
            "cell_left":str(l),"cell_right":str(r),
            "certified_original_multiplier_lower":str(wlo),
            "certified_original_multiplier_upper":str(whi),
            "complete_transformed_source_mean_sq":str(up(v2)),
            "complete_source_mean_error_sq":str(up(e2)),
            "whole_matrix_rankone_covariance_error":str(delta_cov)
        })
    for A in (L1,U1,L2,U2):sym(A)
    for A,err,sign in ((L1,er1l,-1),(U1,er1u,1),
                        (L2,er2l,-1),(U2,er2u,1)):
        for i in range(N):A[i][i]+=sign*up(err)
    L1,lf1=compact_lower(L1);U1,uf1=compact_upper(U1)
    L2,lf2=compact_lower(L2);U2,uf2=compact_upper(U2)
    # Exact whole-source ordering: both valid Loewner brackets must
    # give nonnegative *diagonal* gap on all channels. A numerical
    # operator spectral certificate is intentionally not inferred.
    for i in range(N):
        assert U1[i][i]>=L1[i][i] and U2[i][i]>=L2[i][i]
    data={
      "status":"CERTIFIED_CONDITIONAL_SELECTED_LOW_FREQUENCY_ORIGINAL_COUPLED_TWO_MOMENTS",
      "canonical_W_ODD_NEG":"OPEN",
      "original_true_odd_supported_source_count":PHYS,
      "boundary_adapted_sources":23,
      "physical_odd_sinh_pole_explicit_channel":True,
      "coupled_Fourier_channels_with_pole":N,
      "original_MG11_endpoint_pivots":[PIVOT,POLE],
      "original_complete_25D_physical_Gram_recomputed":True,
      "actual_true_original_signed_digamma_prime_multiplier_enclosed":True,
      "all_original_24x24_mixed_Fourier_source_terms_covered":True,
      "both_true_original_moments_certified_on_selected_panels":True,
      "strong_moment_is_Ao_squared_not_Astar_squared":True,
      "original_Astar_squared_full_pole_cross_terms_still_open":True,
      "original_three_test_frequency_regions":[
           {"left":str(l),"right":str(r),"label":label}
           for l,r,label in spans],
      "actual_original_disjoint_signed_frequency_cells":len(panels),
      "original_nonsmooth_multiplier_kink_possible_cells":near_kink,
      "all_true_original_frequency_cell_diagnostics":cellstats,
      "certified_moment_one_lower": [[str(x) for x in row] for row in L1],
      "certified_moment_one_upper": [[str(x) for x in row] for row in U1],
      "certified_moment_two_lower": [[str(x) for x in row] for row in L2],
      "certified_moment_two_upper": [[str(x) for x in row] for row in U2],
      "whole_matrix_original_Ao_first_lower_fee":str(up(er1l)+lf1),
      "whole_matrix_original_Ao_first_upper_fee":str(up(er1u)+uf1),
      "whole_matrix_original_Ao_second_lower_fee":str(up(er2l)+lf2),
      "whole_matrix_original_Ao_second_upper_fee":str(up(er2u)+uf2),
      "first_original_physical_moment_lower_trace":str(
          sum((L1[i][i] for i in range(N)),F(0))),
      "first_original_physical_moment_upper_trace":str(
          sum((U1[i][i] for i in range(N)),F(0))),
      "second_original_physical_moment_lower_trace":str(
          sum((L2[i][i] for i in range(N)),F(0))),
      "second_original_physical_moment_upper_trace":str(
          sum((U2[i][i] for i in range(N)),F(0))),
      "full_0_to_2pow12_low_band_covered":False,
      "original_complete_23D_Astar_and_Astar_squared_certified":False,
      "original_23D_strong_Galerkin_residual_certified":False,
      "original_470_source_resolvent_certified":False,
      "original_odd_even_Weil_CC27_RH":"OPEN",
      "independent_original_Fourier_form_domain_audit":"OPEN",
      "interpretation":"First exact original SI10-derived coupled 24x24 Fourier two-moment brackets on three selected physical low-frequency regions, preserving 23 boundary-adapted functions and sinh pole. Strictly local panel source matrices, not global Astar or 470D resolvent, with an explicit feasibility diagnostic for covariance overpricing."
    }
    dest=ROOT/args.output;dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(data,indent=2)+"\n")
    print("MG13 true original coupled 24D Fourier moments:",json.dumps({
        "cells":len(panels),
        "first_moment_lower_trace":float(F(data["first_original_physical_moment_lower_trace"])),
        "first_moment_upper_trace":float(F(data["first_original_physical_moment_upper_trace"])),
        "second_moment_lower_trace":float(F(data["second_original_physical_moment_lower_trace"])),
        "second_moment_upper_trace":float(F(data["second_original_physical_moment_upper_trace"])),
        "complete_23D_Galerkin_and_470D_odd_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":main()
