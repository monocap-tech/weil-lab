#!/usr/bin/env python3
"""W-ODD-NEG: original SM40 cap-only ray SCOUT, never a proof.

Build same-original-source sampled AJ and best certified SM40 890-column CJ, prefer minimum
physical source support for a rational candidate violating theta AJ-CJ.
All FFT, quadrature, high-frequency and float errors are UNCONTROLLED.
"""
import argparse,json,math
from itertools import combinations
from pathlib import Path
import numpy as np
from scipy import linalg
from sm36_original_odd_numerical_pilot import (
    geometry,select_sources,physical_columns,fourier_form,
    all_source_negative_cap)
from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_sm34_positive_energy_dual_schur import CLEAN_THRESHOLD
from validate_rpb108_sm40_endpoint_curvature_negative_cap import (
    refined_original_endpoint_curvature
)

ROOT=Path(__file__).resolve().parents[1]
THETA=float(CLEAN_THRESHOLD)

def descriptors(infos,sources):
    clusters,*_=protected_inner_cover()
    assert len(clusters)==107
    result=[]
    for typ,j,k in sources:
        if typ=="pole":
            result.append(dict(kind="original_supported_sinh_pole",
                               cluster_index=None,degree=None,
                               exact_center=None))
        else:
            a,b,_=clusters[j]
            center=(a+b)/2
            assert abs(float(center)-infos[j][0])<1e-10
            result.append(dict(kind="original_polynomial_sine" if k%2==0
                               else "original_polynomial_cosine",
                               cluster_index=int(j),degree=int(k),
                               exact_center=str(center)))
    return result

def matrices(n,pad,infos,sources,cap,orders,mass,total):
    x,dx,v=physical_columns(n,infos,sources)
    H=(v.T@v)*dx
    H=(H+H.T)/2
    Ao,Kdirect,_,info=fourier_form(v,dx,pad)
    b=(v.T@np.sinh(x/2))*dx
    A=Ao-2*np.outer(b,b)
    A=(A+A.T)/2
    C,ci=all_source_negative_cap(
        v,x,dx,cap,orders,np.eye(len(sources)),H,mass,total)
    C=(C+C.T)/2
    assert ci["columns"]==890 and ci["blocks"]==107
    ev=linalg.eigvalsh(A,H)
    assert ev[0]>0
    return A,C,Kdirect,dict(nphysical=n,pad=pad,
            nyquist=float(info["nyquist"]),
            frequency_step=float(info["freq_step"]),
            condition_H=float(np.linalg.cond(H)),
            min_A_over_H=float(ev[0]),eta=float(ci["eta"]))

def integer_ray(x,dim):
    x=np.asarray(x,dtype=float)
    x=x/max(float(np.max(np.abs(x))),1e-30)
    ints=np.rint(16384*x).astype(np.int64)
    assert ints.size==dim and np.any(ints)
    g=math.gcd(*[abs(int(z)) for z in ints if z])
    ints//=g
    if ints[np.nonzero(ints)[0][0]]<0:ints=-ints
    return tuple(int(z) for z in ints)

def ray_ratio(A,C,K,v):
    x=np.asarray(v,dtype=float)
    d=float(x@A@x)
    assert d>0
    return dict(cap_A=float(x@C@x/d),
                direct_negative_A=float(x@K@x/d),
                theta_minus_cap_ratio=float(THETA-x@C@x/d))

def candidate(inds,A,C):
    vals,vecs=linalg.eigh(C[np.ix_(inds,inds)],
                          A[np.ix_(inds,inds)])
    vec=np.zeros(A.shape[0],dtype=float)
    vec[list(inds)]=vecs[:,-1]
    z=integer_ray(vec,len(vec))
    return z,ray_ratio(A,C,np.zeros_like(C),z)["cap_A"]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--quick",action="store_true")
    p.add_argument("--output",default="artifacts/w_odd_neg_cap_ray_scout.json")
    args=p.parse_args()
    infos,old_cap,old_orders,mass,_,old_total=geometry()
    sm39_cap,cap,orders,cap_stats=refined_original_endpoint_curvature()
    assert len(old_cap)==len(sm39_cap)==len(cap)==107
    assert orders==old_orders and sum(orders)==890
    assert cap_stats['all_original_signed_subcells']==3892
    assert cap_stats['original_exact_SPD_pivots']==890
    assert cap_stats['new_SM40_signed_envelope_mass']<cap_stats['old_SM39_signed_envelope_mass']
    assert cap_stats['new_SM40_full_Taylor_eta']<cap_stats['old_SM39_full_Taylor_eta']
    total=float(cap_stats['new_SM40_signed_envelope_mass'])
    sources=select_sources(infos)
    descriptions=descriptors(infos,sources)
    dim=len(sources)
    grids=[(4096,4),(8192,4)] if args.quick else [
           (4096,4),(8192,4),(8192,8)]
    runs=[matrices(n,pad,infos,sources,cap,orders,mass,total)
          for n,pad in grids]
    A,C,_,_=runs[-1]
    summaries=[]
    chosen=None
    for k in (1,2,3):
        best=None
        for inds in combinations(range(dim),k):
            z,high=candidate(inds,A,C)
            grid_ratios=[ray_ratio(a,c,d,z)["cap_A"] for a,c,d,_ in runs]
            score=min(grid_ratios)
            if best is None or score>best["lowest_grid_cap_A"]:
                best=dict(support_count=k,source_indices=list(inds),
                          rational_nonzero_coefficients=[
                              [int(i),str(z[i])] for i in inds if z[i]],
                          highest_resolution_cap_A=high,
                          lowest_grid_cap_A=score,
                          grid_cap_A=grid_ratios)
        summaries.append(best)
        print("SMALL SUPPORT",k,"best min cap/A",
              best["lowest_grid_cap_A"],"indices",
              best["source_indices"],flush=True)
        if chosen is None and best["lowest_grid_cap_A"]>THETA+0.1:
            chosen=[0]*dim
            for i,z in best["rational_nonzero_coefficients"]:
                chosen[i]=int(z)
            break
    # A direct-negative (not upper-cap) obstruction to theta is stronger:
    # even an EXACT replacement of the SM40 cap by the true Kneg could
    # not pass theta*AJ-Kneg>=0 on this fixed Ritz space. Explore only.
    Klast=runs[-1][2]
    direct_summaries=[]
    chosen_direct=None
    for k in (1,2,3):
        best=None
        for inds in combinations(range(dim),k):
            z,high=candidate(inds,A,Klast)
            grid_ratios=[ray_ratio(a,c,d,z)["direct_negative_A"]
                         for a,c,d,_ in runs]
            score=min(grid_ratios)
            if best is None or score>best["lowest_grid_direct_A"]:
                best=dict(support_count=k,source_indices=list(inds),
                          rational_nonzero_coefficients=[
                              [int(i),str(z[i])] for i in inds if z[i]],
                          highest_resolution_direct_A=high,
                          lowest_grid_direct_A=score,
                          grid_direct_A=grid_ratios)
        direct_summaries.append(best)
        print("DIRECT SUPPORT",k,"best min direct/A",
              best["lowest_grid_direct_A"],"indices",
              best["source_indices"],flush=True)
        if chosen_direct is None and best["lowest_grid_direct_A"]>THETA+0.02:
            chosen_direct=[0]*dim
            for i,z in best["rational_nonzero_coefficients"]:
                chosen_direct[i]=int(z)
            break
    direct_eigs,direct_vecs=linalg.eigh(Klast,A)
    direct_full=integer_ray(direct_vecs[:,-1],dim)
    eig,vecs=linalg.eigh(C,A)
    full=integer_ray(vecs[:,-1],dim)
    if chosen is None:chosen=list(full)
    cap_chosen=list(chosen)
    # Prefer the stronger sampled DIRECT obstruction candidate when
    # it is supported by all sampled grids; this still proves NOTHING.
    selected_reason="SM40_CAP_ONLY_NUMERICAL_CANDIDATE"
    if chosen_direct is not None:
        chosen=list(chosen_direct)
        selected_reason="TRUE_KNEG_DIRECT_NUMERICAL_CANDIDATE"
    replays=[dict(grid=m,ray=ray_ratio(a,c,d,chosen))
             for a,c,d,m in runs]
    result=dict(status="NUMERICAL_DISCOVERY_ONLY_NOT_PROOF",
                canonical_obligation="W-ODD-NEG OPEN",
                original_total_sources=470,original_cap_columns=890,
                chosen_original_complete_negative_cap='SM40_ENDPOINT_CURVATURE',
                chosen_SM40_subcells=3892,
                SM40_entire_cap_mass=str(cap_stats['new_SM40_signed_envelope_mass']),
                SM40_exact_890_pivots=cap_stats['original_exact_SPD_pivots'],
                theta=str(CLEAN_THRESHOLD),pilot_dim=dim,
                physical_sources=descriptions,
                minimum_support_search=summaries,
                minimum_support_DIRECT_negative_search=direct_summaries,
                selected_candidate_reason=selected_reason,
                sampled_full_pilot_direct_negative_generalized_max=float(direct_eigs[-1]),
                rationalized_direct_full_grid_ratios=[
                    ray_ratio(a,c,d,direct_full)["direct_negative_A"]
                    for a,c,d,_ in runs],
                cap_candidate_even_if_direct_preferred=[
                    dict(source=descriptions[i],coefficient=str(z))
                    for i,z in enumerate(cap_chosen) if z],
                sampled_full_pilot_generalized_max=float(eig[-1]),
                sampled_rationalized_full_pilot_ratios=[
                    ray_ratio(a,c,d,full)["cap_A"] for a,c,d,_ in runs],
                selected_original_physical_ray=[
                    dict(source=descriptions[i],coefficient=str(z))
                    for i,z in enumerate(chosen) if z],
                selected_independent_grid_replays=replays,
                complete_frequency_Astar_bound_certified=False,
                full_890_cap_energy_lower_certified=False,
                rigorous_original_ray_witness_certified=False,
                sampled_DIRECT_Knegative_not_full_operator_certificate=True,
                all_470_original_full_operator_sign_unproved=True,
                signed_odd_even_Weil_CC27_RH="OPEN")
    target=ROOT/args.output
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(result,indent=2)+"\n")
    print("RATIONAL_RAY_CANDIDATE",json.dumps(dict(
        sources=result["selected_original_physical_ray"],
        grid_checks=replays),sort_keys=True),flush=True)
    print("SM40 SELECTED: exact cap ref rebuilt; candidate ray only",flush=True)
    print("NOT A CERTIFICATE: full original odd theorem OPEN",flush=True)

if __name__=="__main__":
    main()
