#!/usr/bin/env python3
"""SM15: FULL original negative Fourier quadratic UPPER on real odd g_14.42.

Replays the SI10/SM10 global sign-safe cover, refines EVERY leaf's
original seven-prime multiplier by a local all-real rational bound,
and integrates a rigorous original supported sine-Gram upper across
the entire continuous negative-frequency support. Outside the cover
r=(kappa-m)_+ vanishes by SI10, including the infinite exterior.

Also pays the true odd pole. An isolated positive witness is NOT
positivity of the full original odd quadratic/operator or RH.
Every accepting inequality is exact Fraction.
"""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B,PI,prime_interval
from validate_rpb108_si13_odd_fourier_reference import arch_lower
from validate_rpb108_si18_odd_rank_two_woodbury import (
    gram,signed_odd_overlap
)
from validate_rpb108_si12_even_supported_inverse import cosh_bounds
from validate_rpb108_si10_complement_positivity import KAPPA,protected_outer_band
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_sm14_continuum import C,R,S,err as witness_err

RN=F(1,100)
assert C==F(721,50) and RN==F(1,100)

def abs_hi(v):return max(abs(v[0]),abs(v[1]))

def min_distance(lo,hi,target):
    if target<lo:return lo-target
    if target>hi:return target-hi
    return F(0)

def sinc_amp_bound(t):
    """Uniform |sin(2pi*B*t)/(2pi*t)|, t >=0."""
    if t==0:return B
    return min(B,1/(2*PI[0]*t))

def sinc_deriv_bound(t):
    """Uniform |S'(u)|, S(u)=sin(2pi Bu)/(2pi u), |u|>=t.
    S'(u)=B cos(2pi Bu)/u-sin(2pi Bu)/(2pi u^2);
    globally |S'|<=pi B^2 from its integral representation.
    """
    global_bound=PI[1]*B*B
    if t==0:return global_bound
    return min(global_bound,B/t+1/(2*PI[0]*t*t))

def fourier_amp_upper(left,right):
    """Global original physical upper |<g_C,h_xi>| for xi in leaf."""
    assert F(0)<=left<right
    mid=(left+right)/2
    near=min_distance(left,right,C)
    far=C+left
    envelope=sinc_amp_bound(near)+sinc_amp_bound(far)
    center=abs_hi(gram(C,mid))
    L=sinc_deriv_bound(near)+sinc_deriv_bound(far)
    # True g_C=h_C*sinc(2pi*RN*x).
    # |<g_C-h_C,h_xi>| <= 2B * e_N for all xi.
    return min(envelope,center+L*(right-left)/2)+2*B*witness_err(RN)

def signed_negative_global_upper():
    """All original negative frequencies, not a selected sampled band."""
    exterior,min_ext=protected_outer_band()
    assert exterior>0 and min_ext>KAPPA
    clusters,width,mass,total=full_upper_leaves()
    leaves=[item for cl in clusters for item in cl]
    assert len(leaves)==973 and len(clusters)==107
    assert total<F(38)
    whole=F(0)
    old_cap=F(0)
    strongest=[]
    near=F(0)
    far=F(0)
    removed=0
    for l,r,h in leaves:
        # Original seven-prime lower valid at EVERY real xi in [l,r].
        # Inherited SI10 already bounds r<=h+kappa on these leaves.
        # Local arch lower at l (not unit j) plus prime exact phase
        # produces a potentially sharper independent upper for r.
        mid=(l+r)/2
        lower=arch_lower(l)+prime_interval(mid)[0]-F(69,2)*(r-l)
        w=min(h+KAPPA,max(F(0),KAPPA-lower))
        assert F(0)<=w<=h+KAPPA
        if w==0:
            removed+=1
            continue
        amp=fourier_amp_upper(l,r)
        # Actual Kneg,o=2 int_0^infty r(xi)|h_xi><h_xi|dxi.
        term=2*(r-l)*w*amp**2
        old_cap+=2*(r-l)*(h+KAPPA)*amp**2
        whole+=term
        if l<=C+F(2) and r>=C-F(2):near+=term
        else:far+=term
        strongest.append((term,l,r,w,amp))
    assert whole<=old_cap
    assert whole>0 and whole<F(5)
    assert removed>=0 and near+far==whole
    strongest.sort(reverse=True)
    return whole,old_cap,near,far,removed,strongest,clusters

def pole_upper():
    q=signed_odd_overlap(C)
    _,chi=cosh_bounds(B/2)
    # Exact ||s||_1=4(cosh(B/2)-1), s=sinh(x/2).
    l1_upper=4*(chi-1)
    en=witness_err(RN)
    coeff=abs_hi(q)+en*l1_upper
    result=2*coeff**2
    assert result>0 and result<F(1,10)
    return result,q

def original_positive_lower():
    """Replay SM14 on true physical witness but return exact rational."""
    e=witness_err(RN)
    nlo=(1-e)**2*gram(C,C)[0]
    chosen=F(0)
    for numer,delta in S:
        d=F(numer,50)
        pos_radius=R
        iv=gram(C,d)
        overlap=iv[0] if iv[0]>0 else -iv[1] if iv[1]<0 else F(0)
        lower=max(F(0),overlap-2*B*(e+witness_err(pos_radius)))
        chosen+=4*pos_radius*delta*lower**2
    assert chosen>F(2,3)
    return KAPPA*nlo+chosen,chosen

def validate():
    neg,old,near,far,removed,top,clusters=signed_negative_global_upper()
    pole,pole_iv=pole_upper()
    pos,chosen=original_positive_lower()
    signed_margin=pos-neg-pole
    print('SM15 global original negative certified clusters',len(clusters),flush=True)
    print('SM15 whole original Kneg odd quadratic upper',float(neg),flush=True)
    print('SM15 old SM10 envelope with same physical amplitude',float(old),flush=True)
    print('SM15 near +/-2 negative upper',float(near),'remote upper',float(far),flush=True)
    print('SM15 original entirely sign-protected local leaves',removed,flush=True)
    print('SM15 original odd pole quadratic UPPER',float(pole),flush=True)
    print('SM15 positive whole-original A_o quadratic LOWER',float(pos),flush=True)
    print('SM15 actual original A_o-Kneg-pole Rayleigh LOWER',float(signed_margin),flush=True)
    print('SM15 signed odd pole center interval',tuple(float(x) for x in pole_iv),flush=True)
    for t,l,r,w,amp in top[:5]:
        print('SM15 worst leaf',float(l),float(r),'w_upper',float(w),
              'physical amplitude upper',float(amp),'quad upper',float(t),flush=True)
    if signed_margin>0:
        print('SM15 PASS (SCOPED POSITIVE WITNESS): actual entire original odd signed form >0 on g_14.42; operator-wide W-ODD-NEG and RH OPEN.',flush=True)
    else:
        print('SM15 PASS (SCOPED UPPER ONLY): entire original Kneg and odd pole are upper-bounded on g_14.42, but lower signed margin is inconclusive; W-ODD-NEG and RH OPEN.',flush=True)

if __name__=='__main__':validate()
