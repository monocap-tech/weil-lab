#!/usr/bin/env python3
"""NUMERICAL-ONLY actual original MG07 augmented physical-ray feasibility scout.

Source is the original rational two-source vector
 12001*sin(2*pi*(37/64)*x)+16384*sinh(x/2), x in [-11/10,11/10].
G14 are TRUE SI29 continuous Jensen means/first moments, NOT Simpson proxies.
Pole alignment g_j(x)-g_j(B)/s(B)*s(x) preserves trial span.
Float64 truncated grid/padded FFT (uncontrolled low/high frequency errors),
physical SVD rank cutoffs and sampled digamma: NO ORIGINAL CERTIFICATE.

The scout tests the actual Astar=Ao-2|s><s| and Kminus=(kappa-m)+
on source-dependent full Astar-Galerkin responses in numerically resolved
subspaces of span(J2,G14). Negative direct ratio>certified SM40 theta
and D/G >> necessary MG07 budget are METHOD DISCOVERY only, not
actual operator no-go or RH information. Never assert full 470 sign.
"""
import json,argparse
from pathlib import Path
import numpy as np
from scipy import special,linalg
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import ACTIVE,B
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES
from validate_rpb108_mg07_global_negative_sup import exact_bound

ROOT=Path(__file__).resolve().parents[1]
K=0.001
THETA_SHARP=0.9699135819561749 # DISPLAY ONLY from passed exact SM40 artifact
RAY_COEFF=(12001,16384)
SOURCE_CENTER=F(37,64)

def original_multiplier(xi):
    """Sampled actual original seven-prime-power signed m (NOT interval)."""
    v=np.real(special.digamma(0.25+1j*np.pi*xi))-np.log(np.pi)
    for n,prime in ACTIVE.items():
        v-=2*np.log(prime)/np.sqrt(n)*np.cos(2*np.pi*xi*np.log(n))
    return v

def true_jensen(x,c,r,degree):
    z=2*np.pi*r*x
    theta=2*np.pi*c*x
    if degree==0:
        return np.sin(theta)*np.sinc(z/np.pi)
    # Actual continuous first Legendre moment, not SI25 Simpson nodes.
    # 3*cos(theta)*(sin(z)-z*cos(z))/z^2.
    small=np.abs(z)<1e-3
    out=np.empty_like(z)
    out[small]=z[small]*(1-z[small]**2/10+z[small]**4/280)
    out[~small]=3*(np.sin(z[~small])-z[~small]*np.cos(z[~small]))/z[~small]**2
    return np.cos(theta)*out

def run(n,pad,rtol):
    Bf=float(B);dx=2*Bf/n;x=-Bf+dx*np.arange(n)
    pole=np.sinh(x/2)
    sine=np.sin(2*np.pi*float(SOURCE_CENTER)*x)
    J=np.column_stack((sine,pole))
    src=J@np.array(RAY_COEFF,dtype=float)
    src/=np.sqrt(dx*np.dot(src,src))
    G=[]
    for c,r,delta,degree in FEATURES:
        c,r=float(c),float(r)
        g=true_jensen(x,c,r,degree)
        gB=true_jensen(np.array([Bf]),c,r,degree)[0]
        G.append(g-gB/np.sinh(Bf/2)*pole)
    V=np.column_stack((J,*G))
    U,singular,_=linalg.svd(V*np.sqrt(dx),full_matrices=False,lapack_driver='gesvd')
    rank=max(2,int(np.count_nonzero(singular>rtol*singular[0])))
    P=U[:,:rank]/np.sqrt(dx)
    N=n*pad
    freq=np.fft.fftfreq(N,d=dx)
    m=original_multiplier(freq)
    a=np.maximum(K,m)
    neg=np.maximum(K-m,0)
    f=np.fft.fft(P,n=N,axis=0)
    def apply(weight):
        return np.fft.ifft(f*weight[:,None],axis=0)[:n].real
    Ao=apply(a)
    Aaction=Ao-2*np.outer(pole,pole@P*dx)
    A=(P.T@Aaction)*dx
    A=(A+A.T)/2
    if linalg.eigvalsh(A)[0]<=0:
        raise ValueError("Numerical positive trial stiffness not SPD")
    L=P.T@src*dx
    q=linalg.solve(A,L,assume_a='pos')
    z=P@q
    positive=float(q@A@q)
    negative=float(dx*(z@(apply(neg)@q)))
    R=src-Aaction@q
    D=float(dx*(R@R))
    H=float(F(exact_bound()["original_negative_norm_upper"]))
    ks=float(F(33621,10**9))
    c=H/(ks*K)
    relN=negative/positive
    relD=D/positive
    return dict(nphysical=n,pad=pad,rtol=rtol,
                effective_rank=rank,nominal_trial_columns=16,
                smallest_retained_L2_singular=float(singular[rank-1]),
                largest_L2_singular=float(singular[0]),
                source_rational_sine_center=str(SOURCE_CENTER),
                source_rational_coefficients=list(RAY_COEFF),
                Astar_trial_energy=positive,
                sampled_DIRECT_Knegative_over_Astar=relN,
                sampled_squared_strong_residual_over_G=relD,
                displayed_SM40_conditional_theta=THETA_SHARP,
                direct_gap_above_theta=relN-THETA_SHARP,
                MG07_residual_coefficient=c,
                residual_budget_theta_over_c=THETA_SHARP/c,
                D_over_necessary_residual_only_budget=relD/(THETA_SHARP/c),
                raywise_best_possible_YOUNG_direct_lower_display=(
                    np.sqrt(max(relN,0))+np.sqrt(max(c*relD,0)))**2,
                all_Fourier_approximations_uncontrolled=True,
                full_14D_trial_unresolved_due_to_SVD_cutoff=True,
                original_certified_method_obstruction=False)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--quick',action='store_true')
    p.add_argument('--output',default='artifacts/mg07_augmented_true_si29_ray_NONCERTIFYING.json')
    a=p.parse_args()
    assert len(FEATURES)==14 and sum(deg==1 for *_,deg in FEATURES)==2
    grids=[(2048,4),(4096,4),(4096,8)]
    cuts=[1e-5,1e-8] if a.quick else [1e-5,1e-8,1e-11]
    results=[run(n,pad,cut) for n,pad in grids for cut in cuts]
    assert len(results)>0
    result=dict(status='NONCERTIFYING_ORIGINAL_MG07_AUGMENTED_TWO_SOURCE_SCOUT',
       provenance='actual_original_470_source_subset_plus_TRUE_continuous_SI29',
       actual_470dimensional_full_inverse_computed=False,
       complete_484D_trial_not_numerically_resolved=True,
       source_count=470,original_source_support=2,SI29_features_true=14,
       direct_negative_is_not_upper_cap=True,
       certified_theta_loaded_from_passing_SM40_artifact_as_display_not_reproved=True,
       all_tests=[dict(**r) for r in results],
       sampled_direct_ratio_min=min(r['sampled_DIRECT_Knegative_over_Astar'] for r in results),
       sampled_direct_ratio_max=max(r['sampled_DIRECT_Knegative_over_Astar'] for r in results),
       sampled_residual_ratio_min=min(r['sampled_squared_strong_residual_over_G'] for r in results),
       sampled_residual_ratio_max=max(r['sampled_squared_strong_residual_over_G'] for r in results),
       claim_genuine_original_470_source_G_N_loewner=False,
       odd_even_Weil_CC27_RH='OPEN')
    path=ROOT/a.output;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('NUMERICAL ONLY augmented two-source scan:',
          result['sampled_direct_ratio_min'],
          result['sampled_direct_ratio_max'],
          result['sampled_residual_ratio_min'],
          result['sampled_residual_ratio_max'],flush=True)
    print('NONCERTIFYING: ORIGINAL W-ODD-NEG / RH OPEN',flush=True)

if __name__=='__main__': main()
