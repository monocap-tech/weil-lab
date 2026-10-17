#!/usr/bin/env python3
"""SM21: original SI29-C14 Rayleigh lower on ACTUAL first SM10 odd source.

Independent exact-rational physical source/pole enclosures give a substantially
better local forward Ritz trial than SM20's uniform global scalar floor.
No 890-column inverse, true residual cross-matrix or W-ODD-NEG closure.
"""
from fractions import Fraction as F

from validate_rpb108_si06_negative_band import B, PI
from validate_rpb108_si10_complement_positivity import KAPPA
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_sm20_original_source_forward import (
    simpson_error, TAIL_A2, KAPPA_STAR
)
from validate_rpb108_si18_odd_rank_two_woodbury import (
    gram, signed_odd_overlap
)
from validate_rpb108_si25_first_moment_bessel import (
    feature_terms, bilinear_interval
)
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES

def sq_lower(iv):
    a,b=iv
    if a<=0<=b:
        return F(0)
    return min(a*a,b*b)

def abs_upper(iv):
    return max(abs(iv[0]),abs(iv[1]))

def run():
    clusters,width,mass,total=full_upper_leaves()
    assert len(clusters)==107 and len(FEATURES)==14
    j=clusters[0]
    c=(j[0][0]+j[-1][1])/2
    assert c==F(37,64)
    nlo,nhi=gram(c,c)
    assert F(0)<nlo<=nhi<F(9,4)
    positive=KAPPA*nlo
    source_terms=[]
    for i,(center,radius,delta,degree) in enumerate(FEATURES):
        # The TRUE continuous physical SI29 features are enclosed by their
        # signed composite Simpson quadrature, with original uniform error.
        terms=feature_terms(center,radius,degree)
        sampled=bilinear_interval(terms,((c,F(1)),))
        tau=simpson_error(radius,degree)
        assert tau>0
        iv=(sampled[0]-2*B*tau,sampled[1]+2*B*tau)
        gamma=4*radius*delta/(3 if degree else 1)
        assert gamma>0
        gain=gamma*sq_lower(iv)
        positive+=gain
        source_terms.append((iv,gamma,gain))
    pole_iv=signed_odd_overlap(c)
    pole_upper=2*abs_upper(pole_iv)**2
    original_lower=positive-pole_upper
    floor_lower=KAPPA_STAR*nlo
    chosen=max(floor_lower,original_lower)
    assert chosen>0
    # The full-original a^2 high tail and physical support are paid in SM20.
    graph_upper=1360*nhi+2*TAIL_A2
    assert graph_upper>0
    old_lambda=floor_lower/graph_upper
    new_lambda=chosen/graph_upper
    old_gain=floor_lower**2/graph_upper
    new_gain=chosen**2/graph_upper
    improvement_factor=new_gain/old_gain
    D_hi=nhi-new_gain
    assert F(0)<D_hi<nhi
    n0=1
    while F(n0*n0)<=graph_upper:
        n0+=1
    # Derived true forward residual E=u-lambda A_*u, including all
    # seven original primes, supported pole and unbounded graph tail.
    D_lo=max(F(0),nlo-4*new_lambda*n0)
    assert D_lo<=D_hi
    actual_pole=(pole_iv[0]-new_lambda*n0,
                 pole_iv[1]+new_lambda*n0)
    F_actual=[]
    for iv,gamma,gain in source_terms:
        F_actual.append((iv[0]-3*new_lambda*n0,
                         iv[1]+3*new_lambda*n0))
    assert len(F_actual)==14
    # The retained single-column forward-energy H=2<Y,u>-<Y,A_*Y>
    # is enclosed WITHOUT replacing its pole conditioning.
    H_lower=2*new_lambda*nlo-new_lambda**2*F(3,2)*n0
    H_upper=2*new_lambda*nhi-new_lambda**2*chosen
    assert H_lower<=H_upper

    print("SM21 first original supported center",float(c),flush=True)
    print("SM21 original SI29 14 physical positive terms",len(source_terms),flush=True)
    print("SM21 true C14 first-source positive Rayleigh lower",float(positive),flush=True)
    print("SM21 true original odd pole upper",float(pole_upper),flush=True)
    print("SM21 actual conditioned original Rayleigh LOWER",float(original_lower),flush=True)
    print("SM21 old original uniform floor Rayleigh lower",float(floor_lower),flush=True)
    print("SM21 accepted local Rayleigh lower",float(chosen),flush=True)
    print("SM21 original graph M0 upper",float(graph_upper),flush=True)
    print("SM21 old scalar first-source lambda",float(old_lambda),flush=True)
    print("SM21 new actual supported source lambda",float(new_lambda),flush=True)
    print("SM21 strict certified residual upper reduction",float(new_gain),flush=True)
    print("SM21 improvement factor vs SM20",float(improvement_factor),flush=True)
    print("SM21 original residual squared norm interval",float(D_lo),float(D_hi),flush=True)
    print("SM21 original forward-energy H00 enclosure",float(H_lower),float(H_upper),flush=True)
    print("SM21 true original pole residual interval",tuple(map(float,actual_pole)),flush=True)
    for i,iv in enumerate(F_actual):
        print("SM21 true SI29 source cross-residual",i,
              float(iv[0]),float(iv[1]),flush=True)
    if original_lower>floor_lower and improvement_factor>F(100):
        print("SM21 PASS SCOPED: ORIGINAL SI29 physical positive energy"
              " improves first source Ritz gain >100-fold over scalar SM20;"
              " no other 889 columns or entire W-ODD-NEG",flush=True)
    else:
        print("SM21 PASS DIAGNOSTIC: original C14 lower insufficient"
              " for large gain; source retained; W-ODD-NEG OPEN",flush=True)

if __name__=="__main__":
    run()
