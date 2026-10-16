#!/usr/bin/env python3
"""SI25: rigorous 8-feature original physically supported Jensen/Bessel inverse.

Six actual supported Jensen frequency averages from SI24, plus the first
orthogonal Legendre frequency moment on each SI23 outer positive band.
All full 8x8 physical Gram / original signed overlaps are enclosed by
rational analytic trigonometric intervals and rigorously paid
composite-Simpson errors. Only a one-pole inverse *upper* is certified.
The original signed multiplier, support carrier and kappa floor remain.
"""
from fractions import Fraction as F
from functools import lru_cache
from validate_rpb108_si24_jensen_six_inverse import (
    CENTERS as SIX_CENTERS, RADII as SIX_RADII,
    DELTAS as SIX_DELTAS, simpson_terms,
)
from validate_rpb108_si21_odd_jensen_four import (
    KAPPA, B, PI, certify_original_window, outward, plus, scale,
    midpoint, solve_exact, variational_lower,
)
from validate_rpb108_si13_odd_fourier_reference import certify_window
from validate_rpb108_si18_odd_rank_two_woodbury import (
    gram, signed_odd_overlap,
)
from validate_rpb108_si12_even_supported_inverse import sinh_bounds

N = 8  # Eight composite Simpson panels, nine exact rational frequency nodes
MOMENT_IDS = (4,5)  # Only SI23 outer bands at centers 1/4 and 7/20
# (c, radius, delta, degree) : degree 0 = true mean,
# degree 1 = 3 E[u h_{c+ru}] (first Legendre moment, rational normalized).
FEATURES = (tuple((c,r,d,0) for c,r,d in
                  zip(SIX_CENTERS,SIX_RADII,SIX_DELTAS)) +
            tuple((SIX_CENTERS[i],SIX_RADII[i],SIX_DELTAS[i],1)
                  for i in MOMENT_IDS))

def moment_terms(c,r):
    """Rational composite-Simpson enclosure of 3 E[u h(c+ru)].

    E is normalized (1/2)int_{-1}^1; true moment j1=3 E[u h].
    With step 2/N, Simpson weight simplifies to coef*u/N.
    These signed weights select an approximation, NOT a PSD operator.
    """
    assert N>0 and N%2==0
    for i in range(N+1):
        u=F(-1)+F(2*i,N)
        coef=1 if i in (0,N) else (4 if i%2 else 2)
        yield c+r*u, F(coef,N)*u

def feature_terms(c,r,degree):
    if degree==0:
        return simpson_terms(c,r)
    assert degree==1
    return tuple(moment_terms(c,r))

@lru_cache(maxsize=None)
def bounded_q(xi):
    return outward(signed_odd_overlap(xi),15)

@lru_cache(maxsize=None)
def bounded_gram(xi,eta):
    # Both signs of the true physical analytic Gram are retained.
    if xi>eta:
        xi,eta=eta,xi
    return outward(gram(xi,eta),15)

def linear_interval(terms):
    acc=(F(0),F(0))
    for xi,w in terms:
        acc=plus(acc,outward(scale(w,bounded_q(xi)),15))
    return acc

def bilinear_interval(terms1,terms2):
    acc=(F(0),F(0))
    for xi,wi in terms1:
        for eta,wj in terms2:
            acc=plus(acc,outward(scale(wi*wj,bounded_gram(xi,eta)),15))
    return acc

def square_lo(interval):
    a,b=interval
    if a<=0<=b:
        return F(0)
    return min(a*a,b*b)

def certify():
    assert len(FEATURES)==8
    assert MOMENT_IDS==(4,5)
    assert (FEATURES[6][0],FEATURES[7][0])==(F(1,4),F(7,20))
    assert all(c==SIX_CENTERS[i] and r==SIX_RADII[i]
               for i,(c,r,d,degree) in enumerate(FEATURES[:6]))
    assert all(d==1 for _,_,_,d in FEATURES[6:])

    # All positive-frequency windows are genuinely original signed
    # m(xi)>kappa+delta, not a numerical sample.
    original_minima=[certify_original_window(c,d)
                     for c,d in zip(SIX_CENTERS[:4],SIX_DELTAS[:4])]
    assert all(x>KAPPA+d for x,d in zip(original_minima,SIX_DELTAS[:4]))
    continuous_min=certify_window()  # SI13 whole +/-[0.22,0.38]
    assert continuous_min>KAPPA+SIX_DELTAS[4]

    windows=sorted((c-r,c+r) for c,r,d in zip(SIX_CENTERS,SIX_RADII,SIX_DELTAS))
    assert windows==[(F(22,100),F(28,100)),(F(28,100),F(32,100)),
                     (F(32,100),F(38,100)),(F(74,100),F(78,100)),
                     (F(118,100),F(122,100)),(F(163,100),F(167,100))]
    assert all(windows[i][1]<=windows[i+1][0] for i in range(5))

    # On J=[c-r,c+r], u=(xi-c)/r, normalized E=1/2 int_-1^1.
    # Parseval/Bessel for orthonormal polynomials 1, sqrt(3)u:
    #    T_J=2int_J |h_xi><h_xi|dxi
    #      >=4r |E[h]><E[h]| + (4r/3)|3E[u h]><3E[u h]|.
    # All inequalities are LOEWNER PSD on the ORIGINAL supported odd H.
    # Six rank-0 means + two rank-1 moments from distinct outer bands.
    gamma=[4*r*d/(3 if degree else 1) for c,r,d,degree in FEATURES]
    assert all(g>0 for g in gamma)

    beta=lambda r:2*PI[1]*r*B
    tau=[]
    for c,r,d,degree in FEATURES:
        if degree==0:
            # normalized ordinary Simpson (single panel, nodes c-r,c,c+r)
            err=beta(r)**4/F(180)
        else:
            # 1/2 integral of f(u)=3u*sin(2pi(c+ru)x).
            # |f''''(u)|<=3*(4 beta^3+beta^4).
            # composite Simpson has normalized integral error
            # <= sup|f''''|/180 * (2/N)^4.
            b=beta(r)
            err=3*(4*b**3+b**4)/F(180)*(F(2,N)**4)
        assert err>0
        tau.append(err)
    assert max(tau)<F(11,10**6)
    assert tau[6]<F(3,10**6) and tau[7]<F(3,10**6)

    # Actual |g_degree0|<=1, |g_degree1|<=3/2 since
    # |3 E[u h]|<=3 E[|u|]=3/2.
    # A uniform conservative product bound, incl. quadrature:
    # |<g_i,g_j>-<tilde_i,tilde_j>| <=4B (tau_i+tau_j).
    # Norm ||s||<1/2 and sqrt(2B)<3/2 yield source error <3tau/4.
    q=[]
    terms=[]
    for i,(c,r,d,degree) in enumerate(FEATURES):
        t=feature_terms(c,r,degree)
        terms.append(t)
        lo,hi=linear_interval(t)
        eps=F(3,4)*tau[i]
        q.append(outward((lo-eps,hi+eps),12))
    assert q[0][0]>0 and q[1][1]<0 and q[2][0]>0
    assert q[3][1]<0 and q[4][0]>0 and q[5][0]>0
    assert q[6][0]>0 and q[7][1]<0

    H=[]
    for i in range(8):
        row=[]
        for j in range(8):
            lo,hi=bilinear_interval(terms[i],terms[j])
            err=4*B*(tau[i]+tau[j])
            row.append(outward((lo-err,hi+err),12))
        H.append(row)
    assert all(H[i][j]==H[j][i] for i in range(8) for j in range(8))

    # M=Gamma^-1+H/kappa PSD with strictly positive diagonal Gamma^-1
    # because H is the true physical Gram, not its rounded midpoint.
    M=[[(lo/KAPPA+(1/gamma[i] if i==j else 0),
         hi/KAPPA+(1/gamma[i] if i==j else 0))
        for j,(lo,hi) in enumerate(H[i])] for i in range(8)]
    z=solve_exact([[midpoint(t) for t in row] for row in M],
                  [midpoint(t) for t in q])
    correction=variational_lower(q,M,z)
    assert correction>0
    _,shi=sinh_bounds(B)
    S_up=F(235648,1000000)
    assert shi-B<S_up
    upper=2*(S_up/KAPPA-correction/KAPPA**2)
    assert F(0)<upper<F(13,6), ("SI25 8-feature inverse gate failed",float(upper))
    assert upper<F(217,100)  # SI24 exact rational display 2.169634

    Slo= sinh_bounds(B)[0]-B
    C8s_lo=KAPPA*Slo+sum((g*square_lo(qi)
                          for g,qi in zip(gamma,q)),F(0))
    surplus=C8s_lo-2*(shi-B)**2
    assert surplus>F(47,1000)
    ratio=2*(shi-B)**2/C8s_lo
    assert ratio<F(7,10)  # single physical test vector, not BS supremum

    print("SI25 PASS: certified first orthogonal moment rank-eight inverse comparison")
    print("SI13 original signed full continuous margin:",float(continuous_min))
    print("4 retained SI21 original signed margins:",*[float(x) for x in original_minima])
    print("Bessel degree-0/degree-1 feature counts: 6 2")
    print("moment Simpson panels:",N)
    print("two exact first-moment uniform quadrature errors:",float(tau[6]),float(tau[7]))
    print("original signed 8-feature overlaps:",[(float(a),float(b)) for a,b in q])
    print("original signed FULL 8x8 physical Gram:",
          [[(float(a),float(b)) for a,b in row] for row in H])
    print("rational positive inverse dual witness:",[float(t) for t in z])
    print("certified original odd inverse UPPER:",float(upper))
    print("C8 single-s original pole surplus strict LOWER:",float(surplus))
    print("C8 single-s Rayleigh quotient UPPER (not full BS norm):",float(ratio))
    print("NO original inverse pole threshold <=1; NO complete SI11 BS, Stage I, F4, Lean, RH")

if __name__=="__main__":
    certify()
