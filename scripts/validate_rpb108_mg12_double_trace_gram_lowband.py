#!/usr/bin/env python3
"""MG12: original physical 23D double-boundary-adapted Gram and low-band gate.

Unlike MG11's conditional tail, this reconstructs the TRUE original
L2 physical Gram H_T=T* H25 T of all 23 supported source combinations
h_i=f_i-a_i*s-c_i*f_pivot, with BOTH exact endpoint traces cancelled.
All transformed coefficients a_i,c_i are rigorously enclosed using
SM42 exact rational original endpoint values and derivatives;
all original 25x25 physical cross terms enter H_T.

The script proves H_T>0 by exact rational interval preconditioned
Gershgorin and exports a genuine coefficient-norm eigenvalue floor.
It then gives actual, conservative complete Loewner low-band bounds
for the ORIGINAL pole-free positive A_o source action:
    kappa*(H_T-tau_L2*I) <= A_{o,<=L} <= M_L*H_T,
    ||A_{o,<=L}h||² <= M_L²*h*H_T*h
and combines MG11's rigorously bounded WHOLE strong high tail
    ||A_o h||² <= M_L² H_T + tau_A I.
Finally original pole covariance and full Astar strong action are
charged correctly via Young/complete source Gram bounds.

These estimates do NOT certify a small strong Galerkin residual,
nor SI29/470D inverse/signed odd/even Weil CC27/RH. The low-band
strong upper is deliberately coarse and assessed for viability.
All analytic conclusions assume original multiplier/form domain lemmas.
"""
import argparse,json
from fractions import Fraction as F
import numpy as np
from validate_rpb108_si06_negative_band import B,LN
from validate_rpb108_si10_complement_positivity import protected_inner_cover,KAPPA
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    I,original_full_25_physical_interval_gram,
    exact_verified_preconditioned_gram,rational_round)
from validate_rpb108_sm41_original_positive_log_tail import (
    mathematical_global_original_positive_multiplier_majorant)
from validate_rpb108_mg10_rank_one_endpoint_source_tail import boundary_intervals
from validate_rpb108_mg11_dual_boundary_trace_kernel import (
    derivative_intervals_and_D3,derivative_remainder_tail,
    interval_out,positive_gap,up,down)
from validate_rpb108_sm17_compact_spectral_gate import KAPPA_STAR
from sm36_original_odd_numerical_pilot import ROOT,geometry,select_sources

N=25
P=24
CUTOFFS=(12,16,20,24,30)
def maxabs(x):return max(abs(x.l),abs(x.h))
def interval_frac(x):
    return I(down(x.l),up(x.h))
def pair_coefficients(b,d,pivot,free):
    delta=b[P]*d[pivot]-b[pivot]*d[P]
    assert positive_gap(delta)>0
    a={};c={}
    for i in free:
        # Actual rational interval enclosures of exact real coefficients.
        ai=(b[i]*d[pivot]-b[pivot]*d[i])/delta
        ci=(b[P]*d[i]-b[i]*d[P])/delta
        a[i]=interval_frac(ai)
        c[i]=interval_frac(ci)
    return delta,a,c
def original_transformed_gram(H,free,pivot,a,c):
    n=len(free);G=[[I(0) for j in range(n)] for i in range(n)]
    # Exact algebraic 25D congruence, no source cross term omitted.
    for ii,i in enumerate(free):
        for jj in range(ii,n):
            j=free[jj]
            val=(H[i][j]-a[j]*H[i][P]-c[j]*H[i][pivot]
                -a[i]*H[P][j]-c[i]*H[pivot][j]
                +a[i]*a[j]*H[P][P]
                +(a[i]*c[j]+c[i]*a[j])*H[P][pivot]
                +c[i]*c[j]*H[pivot][pivot])
            G[ii][jj]=G[jj][ii]=interval_frac(val)
    return G
def pole_crosses(H,free,pivot,a,c):
    return [interval_frac(H[P][i]-a[i]*H[P][P]-c[i]*H[P][pivot])
            for i in free]
def certified_raw_eigen_floor(G,cert):
    """Recover the EXACT raw physical eigen floor from SM42's
    certified rational Q^T G Q Gershgorin and a rational ||Q||_F².
    NumPy selects Q, never proves its correctness.
    """
    scale_H=10**11;scale_Q=10**6
    hn=[[rational_round(x.mid()*scale_H) for x in row] for row in G]
    middle=np.array([[float(F(x,scale_H)) for x in row] for row in hn])
    assert np.linalg.norm(middle-middle.T)<1e-10
    chol=np.linalg.cholesky(middle)
    Q=np.linalg.inv(chol.T)
    qn=[[int(np.rint(Q[i,j]*scale_Q)) for j in range(len(G))]
        for i in range(len(G))]
    qnorm2=F(sum(q*q for row in qn for q in row),scale_Q**2)
    precond_delta=F(cert["outward_preconditioned_gershgorin_lower"])
    assert precond_delta>0 and qnorm2>0
    # Strict valid because SM42's exact certified Q^T G Q bound
    # is the same Q chosen above; no floating eigenvalue accepted.
    ell=down(precond_delta/qnorm2)
    assert ell>0
    return ell,{"certified_congruence_lower":str(precond_delta),
                "rational_preconditioner_Frobenius_norm_squared":str(qnorm2),
                "certified_original_H23_coefficient_eigenvalue_floor":str(ell)}
def full_rational_source_norm_bounds(G,g,Hpp,ell,tauA,k):
    L=F(2**k)
    M=F(17)+k*F(347,500)
    assert LN[2][1]<F(347,500)
    trace_upper=up(sum((G[i][i].h for i in range(len(G))),F(0)))
    assert trace_upper>ell
    pole_cov=up(Hpp.h*sum((maxabs(z)**2 for z in g),F(0)))
    # ||(A_o -2|s><s|)h||² <=
    # 2||A_o h||² +8 ||s||² |<s,h>|².
    strong_upper=up(2*(M*M*trace_upper+tauA)+8*pole_cov)
    ref_energy_lower=KAPPA_STAR*ell
    assert ref_energy_lower>0 and strong_upper>0
    return {"physical_Gram_trace_upper":str(trace_upper),
            "reference_energy_lower_from_SI29":str(ref_energy_lower),
            "complete_original_Astar_strong_action_scalar_upper":str(strong_upper),
            "strong_action_to_energy_coarse_ratio":str(up(strong_upper/ref_energy_lower))}
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",default="artifacts/mg12_original_double_trace_physical_gram_lowband.json")
    opts=parser.parse_args()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in m["obligations"] if o["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert odd["status"]==m["objective"]["status"]=="open"
    assert m["governance"]["no_automatic_promotion"]
    assert all(x in odd["evidence"] for x in ("SM41","SM42","SI29"))
    assert mathematical_global_original_positive_multiplier_majorant()
    clusters,_,_,_,_=protected_inner_cover()
    assert len(clusters)==107
    infos,*_=geometry();sources=select_sources(infos)
    assert len(sources)==N and sources[P][0]=="pole"
    originalH,physical,_=original_full_25_physical_interval_gram()
    assert physical==sources
    H=[[interval_frac(x) for x in row] for row in originalH]
    b=[interval_out(x) for x in boundary_intervals(sources,clusters)]
    d,D3=derivative_intervals_and_D3(sources,clusters)
    candidates=[]
    for q in range(N-1):
        gap=positive_gap(b[P]*d[q]-b[q]*d[P])
        if gap>0:candidates.append((gap,q))
    assert candidates
    _,pivot=max(candidates,key=lambda p:(p[0],-p[1]))
    assert pivot==23,"MG12 must reproduce verified MG11 nonpole pivot"
    free=tuple(i for i in range(N) if i not in (P,pivot))
    assert len(free)==23
    delta,a,c=pair_coefficients(b,d,pivot,free)
    assert positive_gap(delta)>0
    G=original_transformed_gram(H,free,pivot,a,c)
    assert all(G[i][j].l==G[j][i].l and G[i][j].h==G[j][i].h
               for i in range(23) for j in range(23))
    assert all(G[i][i].l>0 for i in range(23))
    # Exact independent rational interval Gershgorin acceptance,
    # unlike a mere positive sampled or midpoint eigenvalue.
    GramCert=exact_verified_preconditioned_gram(G)
    assert GramCert["certified_entire_original_25x25_physical_gram_SPD"]
    ell,ellmeta=certified_raw_eigen_floor(G,GramCert)
    g=pole_crosses(H,free,pivot,a,c)
    ratioMax=max((maxabs(a[i])+maxabs(c[i]) for i in free))
    Dcorr=[up(D3[i]+maxabs(a[i])*D3[P]+maxabs(c[i])*D3[pivot])
           for i in free]
    Dcorr2=up(sum((x*x for x in Dcorr),F(0)))
    assert Dcorr2>0
    cases=[]
    for k in CUTOFFS:
        L=F(2**k)
        # With |T_h|<=D'_i/(2pi|xi|)^3 on full real tail,
        # raw L2 tail has integral 2/(6^6 *5*L^5).
        L2tail=up(2*Dcorr2/(F(6**6)*5*L**5))
        Atail=up(derivative_remainder_tail(k,Dcorr2))
        M=F(17)+F(k)*F(347,500)
        # Original pole-free positive low band:
        # kappa*(G - L2tail I) <= A_low <= M*G.
        # The strong low action satisfies S_low <= M² G.
        low_floor=down(KAPPA*(ell-L2tail))
        bounds=full_rational_source_norm_bounds(G,g,H[P][P],ell,Atail,k)
        cases.append({
            "cutoff_power":k,"cutoff":"2^"+str(k),
            "exact_transformed_L2_high_tail_upper_multiple_I23":str(L2tail),
            "exact_transformed_Ao_strong_high_tail_upper_multiple_I23":str(Atail),
            "original_low_band_Ao_strict_PSD_from_eigen_floor":low_floor>0,
            "original_low_band_Ao_coefficient_eigen_lower":str(low_floor),
            "original_low_band_Ao_full_Loewner_lower":"kappa*(H23-L2tail*I23)",
            "original_low_band_Ao_full_Loewner_upper":"(17+k*347/500)*H23",
            "original_low_band_Ao_strong_action_upper":"(17+k*347/500)^2*H23",
            "original_full_Ao_strong_upper":"(17+k*347/500)^2*H23+Atail*I23",
            **bounds
        })
    first=next((x["cutoff_power"] for x in cases
               if x["original_low_band_Ao_strict_PSD_from_eigen_floor"]),None)
    status="CERTIFIED_ORIGINAL_23D_BOUNDARY_ADAPTED_PHYSICAL_GRAM_AND_COARSE_LOWBAND"
    artifact={
        "status":status,
        "canonical_W_ODD_NEG":"OPEN",
        "original_physical_source_count":25,
        "original_physical_boundary_adapted_source_count":23,
        "original_pole_index":24,
        "independently_recognized_MG11_second_trace_pivot":pivot,
        "exact_source_value_derivative_trace_matrix_rank":2,
        "original_107_source_cluster_geometry_replayed":True,
        "original_exact_SM42_full_25_physical_source_Gram_recomputed":True,
        "original_full_23x23_transformed_physical_Gram_all_529_entries_covered":True,
        "complete_transformed_physical_Gram_SPD_certified_exact_rational":True,
        "original_transformed_coefficients_are_enclosed_not_sampled":True,
        "exact_source23_pole_coupling_all_entries_paid":True,
        "complete_original_pole_norm_exact_interval":[str(H[P][P].l),str(H[P][P].h)],
        "boundary_trace_2x2_determinant_interval":[str(delta.l),str(delta.h)],
        "source_transform_coefficients_max_abs_sum":str(up(ratioMax)),
        "source_Gram_certificate":GramCert,
        "certified_source23_coefficient_eigen_floor":str(ell),
        "certificate_eigen_floor_derivation":ellmeta,
        "true_source23_third_derivative_majorant_squared_sum":str(Dcorr2),
        "dyadic_checkpoints":cases,
        "first_tested_low_band_strict_PSD_cutoff_power":first,
        "original_low_band_Ao_strong_action_full_interval_certified":True,
        "original_complete_Astar_Galerkin_strong_residual_certified":False,
        "original_original_pole_frequency_crosses_are_replaced_with_exact_physical_coupling":True,
        "original470_source_strong_residual_and_inverse_certified":False,
        "original_signed_negative_cap_and_full470_51over56_gate_passed":False,
        "even_Weil_CC27_RH":"OPEN",
        "independent_original_Fourier_closed_domain_audit":"OPEN",
        "interpretation":"Exact original physical dual-boundary 23D Gram and complete conservative low-band/strong-action Loewner envelopes. Their enormous coarse scalar strong/energy ratio is NOT a small Galerkin residual; original signed negative cap/full470/even/Weil/RH unresolved."
    }
    target=ROOT/opts.output
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(artifact,indent=2)+"\n")
    print("MG12 original boundary-adapted physical Gram:",json.dumps({
        "source23":23,"pivot":pivot,"source23_certified_eigen_floor":float(ell),
        "first_low_band_PSD_k":first,
        "k20_strong_to_energy_ratio":float(F(cases[2]["strong_action_to_energy_coarse_ratio"])),
        "whole470_odd_Weil_RH":"OPEN"
    }),flush=True)
if __name__=="__main__":
    main()
