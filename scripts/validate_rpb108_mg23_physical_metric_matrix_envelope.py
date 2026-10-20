#!/usr/bin/env python3
"""MG23: complete-original-frequency PHYSICAL-METRIC coupled Loewner envelope.

This is a genuine 23D source-frame strong-action / one-step residual
certificate, conditional on the inherited original Fourier/form/domain
lemmas. It is NOT the missing exact source moment Gstar or Sstar and
NOT the full 470-source residual, inverse, or signed negative cap.

MG12 already proves S_o <= M_k^2 H + tau_k I, for the TRUE physical
H=F*F. MG22 loses correlation by replacing H with tr(H) I, then
dividing by a conservative raw eigenfloor ell. MG23 retains H.

For b=F*s, sigma=||s||^2, Astar=Ao-2|s><s|:
Sstar <= (1+eta)(M^2 H+tau I)+4(1+1/eta)sigma bb*.
This is a complete-frequency symbolic MATRIX Loewner inequality,
not an entrywise or truncated-frequency estimate. By physical Cauchy,
bb* <= sigma H, so a valid full-frame scalar relative envelope is
Kstar(eta)=(1+eta)(M^2+tau/ell)+4(1+1/eta)sigma^2.
On true ker(b*) (dimension 22), Astar Fz=Ao Fz and
K0=M^2+tau/ell. The old MG22 bounds remain as fallback.

The finite frame is not invariant under I-t Astar. NEVER iterate
these one-step bounds into a Neumann inverse.
"""
import argparse
import json
from fractions import Fraction as F
from validate_rpb108_mg12_double_trace_gram_lowband import (
    ROOT, N, P, CUTOFFS, interval_frac, maxabs, pair_coefficients,
    original_transformed_gram, pole_crosses, certified_raw_eigen_floor,
    original_full_25_physical_interval_gram,
    exact_verified_preconditioned_gram,
    protected_inner_cover, geometry, select_sources,
    boundary_intervals, derivative_intervals_and_D3,
    positive_gap, derivative_remainder_tail, up,
    KAPPA, KAPPA_STAR, LN
)
from validate_rpb108_mg11_dual_boundary_trace_kernel import interval_out
from validate_rpb108_mg22_pole_aware_complete_frequency_residual import (
    pole_rank_certificate, source_scalar_trial_case
)
from validate_rpb108_sm41_original_positive_log_tail import (
    mathematical_global_original_positive_multiplier_majorant
)

ETA_CANDIDATES = (
    F(1,1024), F(1,256), F(1,64), F(1,16), F(1,4),
    F(1), F(4), F(16), F(64), F(256), F(1024)
)

def new_case(k, ell, tail, sigma, old):
    assert ell>0 and tail>=0 and sigma>0
    M=F(17)+k*F(347,500)
    assert LN[2][1]<F(347,500)
    # MG12's true COMPLETE-frequency 23D Loewner inequality:
    # S_o <= M^2 H + tail I, not M^2 trace(H) I+tail I.
    K0=up(M*M+tail/ell)
    old0=F(old["pole_null_Ao_strong_relative_upper_K0"])
    assert 0<K0<old0
    # Rank-one structure is kept in the matrix assertion; for a
    # scalar trial ONLY, bb* <= sigma H by ambient physical Cauchy.
    full_candidates=[
        (up((1+eta)*K0+4*(1+1/eta)*sigma*sigma),eta)
        for eta in ETA_CANDIDATES
    ]
    newfull, eta=min(full_candidates,key=lambda p:(p[0],p[1]))
    oldfull=F(old["full_Astar_strong_relative_upper_Kstar"])
    Kfull=min(oldfull,newfull)
    assert Kfull>0 and K0>0
    # KEEP EXACT Fraction! Both genuine positive gaps can be <1e-12.
    delta0=KAPPA*KAPPA/K0
    deltafull=KAPPA_STAR*KAPPA_STAR/Kfull
    assert 0<delta0<1 and 0<deltafull<1
    assert delta0>F(old["pole_null_residual_squared_gap_from_one_lower"])
    assert deltafull>=F(old["full_residual_squared_gap_from_one_lower"])
    return {
        "original_cutoff_k": k,
        "every_original_frequency_paid": True,
        "original_low_multiplier_M": str(M),
        "complete_original_strong_high_tail_tau": str(tail),
        "complete_true_pole_free_matrix_bound":
            "S_o <= M^2 H23 + tau I23",
        "complete_true_pole_corrected_matrix_bound":
            "Sstar <= (1+eta)(M^2 H23+tau I23)+4(1+1/eta)sigma b b^T",
        "physical_source_rank_one_cauchy_bound":
            "b b^T <= sigma H23",
        "chosen_Young_eta": str(eta),
        "new_pole_null_relative_K0": str(K0),
        "new_rank_one_full_relative_Kstar": str(newfull),
        "accepted_full_relative_Kstar_with_MG22_fallback": str(Kfull),
        "mg22_old_pole_null_K0": str(old0),
        "mg22_old_full_Kstar": str(oldfull),
        "new_pole_null_trial_t0": str(KAPPA/K0),
        "new_full_trial_tstar": str(KAPPA_STAR/Kfull),
        "pole_null_strict_residual_squared_gap": str(delta0),
        "full_strict_residual_squared_gap": str(deltafull),
        "pole_null_residual_squared_upper": str(1-delta0),
        "full_residual_squared_upper": str(1-deltafull),
        "pole_null_gain_vs_MG22": str(delta0/F(old[
            "pole_null_residual_squared_gap_from_one_lower"])),
        "full_gain_vs_MG22": str(deltafull/F(old[
            "full_residual_squared_gap_from_one_lower"])),
        "not_iterable_as_finite_frame_contraction": True
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",default=
        "artifacts/mg23_original_physical_metric_matrix_envelope.json")
    args=parser.parse_args()
    ledger=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in ledger["obligations"] if o["id"]=="W-ODD-NEG")
    assert odd["status"]==ledger["objective"]["status"]=="open"
    assert ledger["active_obligation"]=="W-ODD-NEG"
    assert ledger["governance"]["no_automatic_promotion"]
    assert all(e in odd["evidence"] for e in ("SM41","SM42","SI29"))
    assert mathematical_global_original_positive_multiplier_majorant()

    clusters,_,_,_,_=protected_inner_cover()
    assert len(clusters)==107
    infos,*_=geometry()
    sources=select_sources(infos)
    assert len(sources)==N and sources[P][0]=="pole"
    raw,physical,_=original_full_25_physical_interval_gram()
    assert physical==sources
    H25=[[interval_frac(x) for x in row] for row in raw]
    b=[interval_out(x) for x in boundary_intervals(sources,clusters)]
    d,D3=derivative_intervals_and_D3(sources,clusters)
    pivots=[]
    for q in range(N-1):
        gap=positive_gap(b[P]*d[q]-b[q]*d[P])
        if gap>0:pivots.append((gap,q))
    assert pivots
    _,pivot=max(pivots,key=lambda p:(p[0],-p[1]))
    assert pivot==23
    free=tuple(i for i in range(N) if i not in (pivot,P))
    assert len(free)==23
    det,a,c=pair_coefficients(b,d,pivot,free)
    assert positive_gap(det)>0
    H23=original_transformed_gram(H25,free,pivot,a,c)
    cert=exact_verified_preconditioned_gram(H23)
    assert cert["certified_entire_original_25x25_physical_gram_SPD"]
    ell,_=certified_raw_eigen_floor(H23,cert)
    assert ell>0
    g=pole_crosses(H25,free,pivot,a,c)
    witness=pole_rank_certificate(g)
    assert witness is not None and len(g)==23
    sigma=H25[P][P].h
    assert sigma>0
    deriv=[up(D3[i]+maxabs(a[i])*D3[P]+maxabs(c[i])*D3[pivot])
           for i in free]
    Dcorr2=up(sum((x*x for x in deriv),F(0)))
    trace=up(sum((H23[i][i].h for i in range(23)),F(0)))
    assert trace>ell and Dcorr2>0
    cases=[]
    for k in CUTOFFS:
        tau=up(derivative_remainder_tail(k,Dcorr2))
        old=source_scalar_trial_case(trace,ell,g,H25[P][P],tau,k)
        cases.append(new_case(k,ell,tau,sigma,old))
    best0=max(cases,key=lambda r:F(r["pole_null_strict_residual_squared_gap"]))
    bestfull=max(cases,key=lambda r:F(r["full_strict_residual_squared_gap"]))
    out={
        "status":"ORIGINAL_COMPLETE_FREQUENCY_PHYSICAL_METRIC_MATRIX_METHOD_GATE",
        "canonical_W_ODD_NEG":"OPEN",
        "full_original_physical_25D_Gram_interval_recomputed":True,
        "true_double_boundary_source_frame_dimension":23,
        "true_pole_null_dimension":22,
        "true_pole_overlap_nonzero_interval_witness":True,
        "H23_strict_positive_verified":True,
        "H23_coeff_eigen_floor":str(ell),
        "original_pole_sigma_upper":str(sigma),
        "original_positive_Ao_energy_floor":str(KAPPA),
        "original_pole_corrected_Astar_energy_floor":str(KAPPA_STAR),
        "complete_frequency_matrix_Loewner_envelope_theorem_used":True,
        "matrix_envelope_uses_exact_true_H_and_b_symbolically":True,
        "actual_coupled_original_Gstar_computed":False,
        "actual_coupled_original_Sstar_computed":False,
        "MG07_full_470D_source_J_and_Y_residual_certified":False,
        "finite_frame_residual_invariant":False,
        "global_Neumann_inverse_certified":False,
        "original_signed_51over56_cap_certified":False,
        "even_Weil_CC27_RH":"OPEN",
        "independent_Fourier_form_domain_audit":"OPEN",
        "dyadic_cases":cases,
        "best_null_case_k":best0["original_cutoff_k"],
        "best_full_case_k":bestfull["original_cutoff_k"],
        "best_null_strict_gap":best0["pole_null_strict_residual_squared_gap"],
        "best_full_strict_gap":bestfull["full_strict_residual_squared_gap"],
        "decision":"Retain full H23 and rank-one bb^T structure, rather than MG22 trace scalarization. This is a valid complete-original-frequency 23D matrix UPPER ENVELOPE but not the actual Gstar/Sstar; a mixed-frequency pole-corrected 470-source residual remains the open acceptance gate."
    }
    dst=ROOT/args.output
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(out,indent=2)+"\n")
    print("MG23 physical-metric complete-frequency envelope:",
        json.dumps({
          "best_null_cutoff":out["best_null_case_k"],
          "best_full_cutoff":out["best_full_case_k"],
          "best_null_gap":float(F(out["best_null_strict_gap"])),
          "best_full_gap":float(F(out["best_full_strict_gap"])),
          "470D_original_signed_odd_even_Weil_RH":"OPEN"
        }),flush=True)

if __name__=="__main__":
    main()
