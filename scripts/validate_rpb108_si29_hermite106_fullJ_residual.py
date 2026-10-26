#!/usr/bin/env python3
"""NF: true 14 SI29 features have tiny L2 residual against full J470.

Frequency Hermite interpolation of sin(2*pi*eta*x) using the first
15 TRUE original SI10 cluster centers, with orders p_j totaling 106,
produces physical approximants in the ORIGINAL J470 source span.
The classical confluent Hermite remainder is bounded for every real x:
 (2*pi_up*B)^N/N! * product_j max(|c+r-c_j|,|c-r-c_j|)^p_j.
For genuine Jensen first moments multiply by E|3u| = 3/2.

Consequence: ||(I-P_J)F14||_HS < 1.6e-21; this controls F14*R0 for
the complete original 470D Galerkin strong residual, NOT Ritz movement.
The actual Astar-weighted Schur T is still UNKNOWN.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

from validate_rpb108_si06_negative_band import B, PI, TWOC
from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES
from validate_rpb108_mg07_global_negative_sup import exact_bound
from validate_rpb108_sm17_compact_spectral_gate import KAPPA_STAR
from validate_rpb108_mg07_two_source_original_physical_pole_input import (
    CENTER, RAYS
)

ROOT=Path(__file__).resolve().parents[1]
PI_UP=F(22,7)
EXPECTED_CLUSTERS=(
 (F(37,64),15),(F(211,128),11),(F(45,16),11),
 (F(117,32),6),(F(141,32),8),(F(45,8),6),
 (F(25,4),5),(F(929,128),6),(F(523,64),5),
 (F(1113,128),5),(F(295,32),5),(F(641,64),6),
 (F(1511,128),6),(F(1651,128),5),(F(1845,128),6))
EXPECTED_FEATURES=(
 (F(3,10),F(1,50),0),(F(19,25),F(1,50),0),
 (F(6,5),F(1,50),0),(F(33,20),F(1,50),0),
 (F(1,4),F(3,100),0),(F(7,20),F(3,100),0),
 (F(1,4),F(3,100),1),(F(7,20),F(3,100),1),
 (F(221,100),F(1,50),0),(F(21,10),F(1,50),0),
 (F(58,25),F(1,50),0),(F(18,25),F(1,50),0),
 (F(14,5),F(1,50),0),(F(17,5),F(1,50),0))

def hyp_upper(x,odd,kmax=12):
    lo=sum((x**(2*k+int(odd))/factorial(2*k+int(odd))
            for k in range(kmax)),F(0))
    p=2*kmax+int(odd)
    first=x**p/factorial(p)
    ratio=x*x/F((p+1)*(p+2))
    assert ratio<1
    return lo+first/(1-ratio)

def verify():
    assert B==F(11,10) and PI[0]>3 and PI[1]<PI_UP
    assert F(0)<TWOC<F(8)
    assert KAPPA_STAR==F(33621,10**9)
    H=F(exact_bound()['original_negative_norm_upper'])
    assert H<F(13)
    clusters,_,_,_,_=protected_inner_cover()
    assert len(clusters)==107
    first=tuple(((a+b)/2,taylor_order(b-a,9)[0])
                for a,b,_ in clusters[:15])
    assert first==EXPECTED_CLUSTERS
    assert 1+sum(taylor_order(b-a,9)[0] for a,b,_ in clusters)==470
    assert len(FEATURES)==14
    actual=tuple((c,r,dg) for c,r,_delta,dg in FEATURES)
    assert actual==EXPECTED_FEATURES
    N=sum(p for _,p in first)
    assert N==106

    # Exact rational, independent of any Gram inversion or floating SVD.
    errors=[]
    for c,r,degree in actual:
        product=F(1)
        for cj,p in first:
            distance=max(abs(c+r-cj),abs(c-r-cj))
            product*=distance**p
        variation=F(3,2) if degree else F(1)
        eps=variation*(2*PI_UP*B)**N*product/factorial(N)
        errors.append(eps)
    assert max(errors)<F(1,10**21)
    trace=2*B*sum((e*e for e in errors),F(0))
    trace_ceiling=F(1,4*10**41)
    hs_ceiling=F(8,5*10**21)
    assert trace<trace_ceiling and trace<hs_ceiling**2

    # Frequency-Hermite interpolation commutes with physical d/dx.
    # For h(eta,x)=sin(2*pi*eta*x), the Nth eta derivative of
    # d_x h=2*pi*eta*cos(2*pi*eta*x) is bounded by
    # 2*pi_up*[15*(2*pi_up*|x|)^N+N*(2*pi_up*|x|)^(N-1)]
    # on the convex hull of all first-15 nodes and SI29 bands (<15).
    # Hence the true physical derivative of each interpolation error
    # is at most Cx*eps_i, Cx=2*pi_up*15+N/B<191.
    assert max(c for c,_ in first)<F(15)
    assert max(c+r for c,r,d in actual)<F(15)
    Cx=2*PI_UP*15+F(N,B)
    assert Cx<F(191)
    # Zero-extension variation <=(2+2B*191)*eps_i.
    # Whole-original Ao form <= 36*2B*eps_i²+V_i²:
    # low |xi|<=1 uses Ao<=36, high |xi|>=1 uses SM41
    # Ao<=17+ln|xi| and |hat e|<=V/(2pi|xi|)<V/(6|xi|);
    # 2*integral_1^infty (17+ln xi)/xi² dxi=36.
    Vconst=2+2*B*F(191)
    assert Vconst<F(423)
    Atr=(36*2*B+Vconst*Vconst)*sum((e*e for e in errors),F(0))
    weighted_upper=F(2,10**37)
    assert Atr<weighted_upper
    # The Astar-Galerkin feature Schur T is the MINIMAL Astar
    # energy of F-G with G in J470. Since Astar<=Ao and
    # frequency-Hermite interpolants belong to J470,
    # 0<T<=Atr*I_14 <2e-37 I. Thus lambda_min(T)<1e-25
    # AUTOMATICALLY: the earlier conditional threshold is too
    # weak to distinguish viable augmentation from failure.
    # For full P_J and original R0: J*R0=0,
    # ||F*R0|| <= ||(I-P_J)F||_HS ||R0||.
    # For f=Jx and forcing y=H_phys^-1 A_J x:
    # R0 y=-(I-P_J)Astar f=-(I-P_J)Ao f, since s in J.

    # Original whole-real Ao= max(kappa,m)(D). On |xi|<=1:
    # psi(1/4)-ln(pi)<0; 0th digamma summand <=4,
    # others <=16 sum_{k>=1} k^-3 <24, seven-prime bound <8,
    # hence a_o<=36. On |xi|>=1 inherited SM41: a_o<=17+ln|xi|.
    # Zero extension integration by parts gives
    # |hat f(xi)|<=V/(2*pi*|xi|)<V/(6*|xi|).
    # ∫_1∞ (17+ln xi)^2 xi^-2 dxi = 325; both tails 650.
    # Therefore ||Ao f||²<= 36²*2B*amp²+(325/18)*V²,
    # amp=a+3b/5 and V=2amp+2B(2pi_up a c+3b/5).
    assert hyp_upper(B/2,True)<F(3,5)
    assert hyp_upper(B/2,False)<F(6,5)
    assert CENTER==F(37,64)
    expected=((12001,16384,1400000),(3013,4096,350000))
    assert tuple((a,b,m) for (a,b,_),(_,_,m) in zip(RAYS,expected))==expected
    ray_data=[]
    for a,b,M in expected:
        amp=F(a)+F(3,5)*b
        V=2*amp+2*B*(a*2*PI_UP*CENTER+F(3,5)*b)
        Ao_norm2=36**2*2*B*amp*amp+F(325,18)*V*V
        assert Ao_norm2<M*M
        bound=hs_ceiling*M
        ray_data.append({'a':a,'b':b,'Ao_norm_upper':M,
                         'actual_14D_FstarR0_vector_upper':str(bound),
                         'display_upper':float(bound),
                         'exact_Ao_norm_squared_majorant':str(Ao_norm2)})
    assert F(ray_data[0]['actual_14D_FstarR0_vector_upper'])==F(224,10**17)
    assert F(ray_data[1]['actual_14D_FstarR0_vector_upper'])==F(56,10**17)

    # NECESSARY degeneracy gate for any SI29 rescue of the canonical
    # theta=.97 direct-ray cap-only criterion:
    # if T=W*Astar W >= 1e-25 I, positive energy gain
    # E=r*T^-1 r < (2.24e-15)^2 /1e-25 =5.0176e-5.
    # ||D||²<=E/kappa_star<25/16, ||f||²<33000².
    # Even for ideal cap Kminus, ||Kminus||<13:
    # possible cap-only margin improvement
    # <=theta E + 2*13*33000*(5/4) <1,072,501,
    # below CANONICAL full source-only deficit >1,286,120.
    tiny_T=F(1,10**25)
    r=F(ray_data[0]['actual_14D_FstarR0_vector_upper'])
    E=r*r/tiny_T
    amp=F(expected[0][0])+F(3,5)*expected[0][1]
    assert E<F(1,1000) and E/KAPPA_STAR<F(25,16)
    assert 2*B*amp*amp<33000**2
    max_improvement=E+2*13*33000*F(5,4)
    assert max_improvement<F(1286120)
    result={
        'status':'CONDITIONAL_EXACT_TRUE_SI29_HERMITE106_FULL_J470_PROJECTION',
        'original_source_count':470,'Hermite_original_generator_count':N,
        'true_continuous_SI29_feature_count':14,
        'exact_feature_uniform_pointwise_errors':[str(x) for x in errors],
        'max_uniform_feature_pointwise_error_upper':str(F(1,10**21)),
        'full_J470_projected_SI29_14D_physical_Schur_trace_upper':str(trace_ceiling),
        'full_J470_projected_SI29_14D_physical_Schur_trace_actual_bound':str(trace),
        'full_J470_projected_feature_HS_norm_upper':str(hs_ceiling),
        'true_SI29_Astar_weighted_Schur_14D_operator_upper':str(weighted_upper),
        'true_SI29_Astar_weighted_Schur_14D_exact_trace_majorant':str(Atr),
        'weighted_Schur_less_than_1e_25_automatic':True,
        'small_weighted_Schur_eigenvalue_is_NOT_SI29_success_or_failure':True,
        'original_full_Galerkin_feature_coupling_operator_bound':
           '||Fstar R0|| <= (8/5)*10^-21 ||R0||',
        'original_exact_stopping_rays':ray_data,
        'necessary_weighted_Schur_min_eigenvalue_for_cap_only_rescue':
           '< '+str(tiny_T),
        'assuming_weighted_Schur_at_least_1e_25_upper_A_energy_gain':str(E),
        'assuming_weighted_Schur_at_least_1e_25_upper_cap_margin_gain':str(max_improvement),
        'inherited_exact_MG07_direct_stop_deficit':'>1286120',
        'actual_original_weighted_Schur_T':'OPEN',
        'actual_SI29_augmented_ritz_move':'OPEN',
        'actual_original_complete_signed_operator':'OPEN',
        'even_CC27_Weil_RH':'OPEN',
        'source_hypotheses':'Original SI06/SI10 source realization and SM41 multiplier tail.'
    }
    return result

if __name__=='__main__':
    z=verify()
    path=ROOT/'artifacts/si29_true14_hermite106_fullJ_projection.json'
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(z,indent=2)+'\n')
    print('NF SI29 TRUE14 HERMITE106 FULL-J RESIDUAL PASS',
          float(F(z['full_J470_projected_SI29_14D_physical_Schur_trace_actual_bound'])),
          [x['display_upper'] for x in z['original_exact_stopping_rays']],
          flush=True)
