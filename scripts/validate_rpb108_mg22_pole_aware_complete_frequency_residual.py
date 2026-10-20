#!/usr/bin/env python3
"""MG22: first ORIGINAL complete-frequency pole-aware scalar Galerkin trial gate.

Uses genuine original 25 physically supported odd SI10 sources,
MG11's 23D exact double-boundary kernel, SM42 exact 25D physical
Gram, and original entire-frequency SM41/MG11 Fourier bounds.

For h_z in true 23D physical frame F, inherited SI29 shows
<Astar h,h> >= kappa_star*||h||^2. MG12 proves whole-original
||Astar h||² <= Smax||z||² and H23>=ell I, hence
||Astar h||² <= Kstar||h||² where Kstar=Smax/ell.

THE COMPLETE strong residual of the actual trial Y=t F is
R(z)=Fz-t Astar Fz (NO truncation of residual Fourier frequencies).
For t=alpha/K, using alpha=κ_star and the above full action:
||R(z)||² <=(1-alpha²/K)||Fz||².
This is a rigorous but quantitatively very weak ORIGINAL 23D
source-frame upper, not a global inverse contraction.

On the exact physical pole-orthogonal subspace ker g,
g_i=<s,h_i>, dimension 22 if g !=0, Astar h=Ao h and
Ao>=κ, so a strictly BETTER original whole-frequency upper uses
Smax0=M² trace(H23)+tauA (no pole and no Young factor):
||R0(z)||² <= (1-κ²/K0)||Fz||², K0=Smax0/ell.
This is a method gate that exposes the rank-one pole loss.

*** IT DOES NOT CERTIFY A RESOLVENT ***
The residual R(z) generally LEAVES the finite 23D frame. One
CANNOT iterate the finite-frame bound to claim Neumann convergence
on the full infinite-dimensional Hilbert space. Neither bound is
a source470 actual inverse or a signed odd negative-cap certificate.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_mg12_double_trace_gram_lowband import (
    ROOT,N,P,CUTOFFS,interval_frac,maxabs,pair_coefficients,
    original_transformed_gram,pole_crosses,certified_raw_eigen_floor,
    full_rational_source_norm_bounds,
    original_full_25_physical_interval_gram,
    exact_verified_preconditioned_gram,
    protected_inner_cover,geometry,select_sources,
    boundary_intervals,derivative_intervals_and_D3,
    positive_gap,derivative_remainder_tail,up,down,
    I,KAPPA,KAPPA_STAR,LN
)
from validate_rpb108_mg11_dual_boundary_trace_kernel import interval_out
from validate_rpb108_sm41_original_positive_log_tail import (
    mathematical_global_original_positive_multiplier_majorant
)

def rational_unit(x):
    x=F(x)
    assert x>0
    k=max(0,x.denominator.bit_length()-x.numerator.bit_length()+2)
    small=F(1,2**k)
    assert 0<small<=x
    return str(small)

def pole_rank_certificate(g):
    witnesses=[]
    for i,z in enumerate(g):
        if z.l>0:witnesses.append({"index":i,"gap_from_zero":z.l})
        if z.h<0:witnesses.append({"index":i,"gap_from_zero":-z.h})
    return max(witnesses,key=lambda x:x["gap_from_zero"]) if witnesses else None

def source_scalar_trial_case(physical_trace_upper,ell,g,pole_norm,tail,k):
    assert ell>0 and physical_trace_upper>=ell
    M=F(17)+k*F(347,500)
    assert LN[2][1]<F(347,500)
    pole_cov=up(pole_norm.h*sum((maxabs(z)**2 for z in g),F(0)))
    positive_action_scalar=up(M*M*physical_trace_upper+tail)
    full_action_scalar=up(2*positive_action_scalar+8*pole_cov)
    assert positive_action_scalar>0 and full_action_scalar>positive_action_scalar
    K0=up(positive_action_scalar/ell)
    Ks=up(full_action_scalar/ell)
    assert 0<KAPPA_STAR<KAPPA
    assert K0>=KAPPA*KAPPA and Ks>=KAPPA_STAR*KAPPA_STAR
    # MG11's generic down() rounds to 1e-12, but the true
    # squared contraction gaps may be far SMALLER. Exact Fraction
    # preserves a positive rational lower instead of rounding to zero.
    # K0 and Ks have already been rounded UP rigorously.
    delta0=KAPPA*KAPPA/K0
    deltas=KAPPA_STAR*KAPPA_STAR/Ks
    assert 0<delta0<1 and 0<deltas<1
    # The optimum scalar coefficients are kept exactly rational.
    # Even slight rounding would spoil their optimal bound.
    t0=KAPPA/K0
    ts=KAPPA_STAR/Ks
    assert 0<t0 and 0<ts
    full_residual_sq=F(1)-deltas
    null_residual_sq=F(1)-delta0
    assert 0<full_residual_sq<1 and 0<null_residual_sq<1
    return {
        "original_cutoff_k":k,
        "original_cutoff_lambda":str(2**k),
        "actual_pole_free_strong_source_coeff_upper":str(positive_action_scalar),
        "actual_pole_corrected_strong_source_coeff_upper":str(full_action_scalar),
        "original_true_physical_Gram_eigen_floor":str(ell),
        "original_global_reference_energy_alpha":str(KAPPA_STAR),
        "original_pole_null_energy_alpha":str(KAPPA),
        "full_Astar_strong_relative_upper_Kstar":str(Ks),
        "pole_null_Ao_strong_relative_upper_K0":str(K0),
        "full_actual_scalar_trial_coefficient_t":str(ts),
        "pole_null_actual_scalar_trial_coefficient_t":str(t0),
        "full_certified_relative_residual_squared_upper":str(full_residual_sq),
        "pole_null_certified_relative_residual_squared_upper":str(null_residual_sq),
        "full_residual_squared_gap_from_one_lower":str(deltas),
        "pole_null_residual_squared_gap_from_one_lower":str(delta0),
        "pole_null_to_full_gap_ratio_lower":str(down(delta0/deltas)),
        "every_frequency_included_in_strong_upper":True,
        "scalar_trial_not_full_resolvent_or_iterable":True
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",default="artifacts/mg22_full_frequency_pole_aware_scalar_residual.json")
    opts=parser.parse_args()
    ledger=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in ledger["obligations"] if o["id"]=="W-ODD-NEG")
    assert odd["status"]==ledger["objective"]["status"]=="open"
    assert ledger["active_obligation"]=="W-ODD-NEG"
    assert ledger["governance"]["no_automatic_promotion"]
    assert all(x in odd["evidence"] for x in ("SM41","SM42","SI29"))
    assert mathematical_global_original_positive_multiplier_majorant()
    clusters,_,_,_,_=protected_inner_cover()
    assert len(clusters)==107
    infos,*_=geometry()
    sources=select_sources(infos)
    assert len(sources)==N and sources[P][0]=="pole"
    raw,physical,_=original_full_25_physical_interval_gram()
    assert physical==sources
    H=[[interval_frac(x) for x in row] for row in raw]
    b=[interval_out(x) for x in boundary_intervals(sources,clusters)]
    d,D3=derivative_intervals_and_D3(sources,clusters)
    candidates=[]
    for q in range(N-1):
        gap=positive_gap(b[P]*d[q]-b[q]*d[P])
        if gap>0:candidates.append((gap,q))
    assert candidates
    _,pivot=max(candidates,key=lambda p:(p[0],-p[1]))
    assert pivot==23
    free=tuple(i for i in range(N) if i not in (pivot,P))
    assert len(free)==23
    delta,a,c=pair_coefficients(b,d,pivot,free)
    assert positive_gap(delta)>0
    H23=original_transformed_gram(H,free,pivot,a,c)
    gramcert=exact_verified_preconditioned_gram(H23)
    assert gramcert["certified_entire_original_25x25_physical_gram_SPD"]
    ell,_=certified_raw_eigen_floor(H23,gramcert)
    g=pole_crosses(H,free,pivot,a,c)
    assert len(g)==23
    witness=pole_rank_certificate(g)
    assert witness is not None,(
       "No physical pole overlap was interval-separated from zero; "
       "cannot certify a 22D pole-null hyperplane")
    Dcorr=[up(D3[i]+maxabs(a[i])*D3[P]+maxabs(c[i])*D3[pivot])
           for i in free]
    Dcorr2=up(sum((x*x for x in Dcorr),F(0)))
    trace=up(sum((H23[i][i].h for i in range(23)),F(0)))
    assert Dcorr2>0 and trace>ell
    cases=[]
    for k in CUTOFFS:
        tail=up(derivative_remainder_tail(k,Dcorr2))
        cases.append(source_scalar_trial_case(trace,ell,g,H[P][P],tail,k))
    # Best a priori bound over original certified dyadic cutoffs:
    bestfull=max(cases,key=lambda x:F(x["full_residual_squared_gap_from_one_lower"]))
    bestnull=max(cases,key=lambda x:F(x["pole_null_residual_squared_gap_from_one_lower"]))
    result={
        "status":"ORIGINAL_COMPLETE_FREQUENCY_SCALAR_SOURCE_RESIDUAL_METHOD_GATE",
        "canonical_W_ODD_NEG":"OPEN",
        "original_SI10_physical_source_count":25,
        "original_true_boundary_adapted_source_dimension":23,
        "original_pole_source_index":24,
        "original_boundary_nonpole_pivot":23,
        "complete_original_physical_Gram_recomputed_exact_intervals":True,
        "strict_original_H23_positive_interval_Gershgorin":True,
        "original_physical_Gram_coefficient_eigen_floor":str(ell),
        "original_pole_nonzero_overlap_interval_witness":{
           "source_index":witness["index"],
           "gap_from_zero_positive_dyadic_lower":rational_unit(witness["gap_from_zero"])},
        "original_exact_pole_null_hyperplane_dimension":22,
        "original_23D_actual_true_Astar_scalar_trial_residual":True,
        "original_22D_pole_null_actual_true_Ao_scalar_trial_residual":True,
        "original_source_global_kappa_star":str(KAPPA_STAR),
        "original_positive_multiplier_floor_kappa":str(KAPPA),
        "original_full_frequency_tail_and_low_band_paid":True,
        "dyadic_case_bounds":cases,
        "best_complete_frame_trial":{
             "cutoff_power":bestfull["original_cutoff_k"],
             "relative_residual_squared_upper":bestfull[
                 "full_certified_relative_residual_squared_upper"],
             "strict_gap_from_one":bestfull[
                 "full_residual_squared_gap_from_one_lower"]},
        "best_pole_null_trial":{
             "cutoff_power":bestnull["original_cutoff_k"],
             "relative_residual_squared_upper":bestnull[
                 "pole_null_certified_relative_residual_squared_upper"],
             "strict_gap_from_one":bestnull[
                 "pole_null_residual_squared_gap_from_one_lower"]},
        "actual_470_source_J_and_Y_strong_residual_certified":False,
        "finite_source_residual_stays_in_F_subspace":False,
        "repeated_finite_frame_residual_bound_proves_Neumann_convergence":False,
        "actual_source23_full_Gstar_Sstar_fine_matrices_computed":False,
        "full_original_signed_negative_cap_51over56_accepted":False,
        "complete_even_Weil_CC27_RH":"OPEN",
        "independent_full_original_Fourier_and_domain_audit":"OPEN",
        "decision":"Pole-null 22D is a genuine original source subspace and loses no rank-one pole action, but even the optimized full-frequency scalar residual envelope is too conservative for a practical 470D original inverse. No iterative claim: the residual leaves the finite frame. Next work needs coupled source-frequency matrices and complete pole-corrected original response."
    }
    out=ROOT/opts.output
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n")
    print("MG22 original complete-frequency pole-aware scalar source residual:",json.dumps({
        "true_source23":23,"true_pole_null_dimension":22,
        "best_full_cutoff":bestfull["original_cutoff_k"],
        "best_full_gap":float(F(bestfull["full_residual_squared_gap_from_one_lower"])),
        "best_pole_null_cutoff":bestnull["original_cutoff_k"],
        "best_pole_null_gap":float(F(bestnull["pole_null_residual_squared_gap_from_one_lower"])),
        "actual_470_signed_odd_even_Weil_RH":"OPEN"
    }),flush=True)

if __name__=="__main__":
    main()
