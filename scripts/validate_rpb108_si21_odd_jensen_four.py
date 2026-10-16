#!/usr/bin/env python3
"""SI21 — rigorous rank-four *physical* odd Jensen minorant.

Certified original signed archimedean / seven-prime positivity on four
whole frequency windows. Use exact positive Jensen / variance Loewner
minorants of physically supported Fourier concentrations; compute the full
4x4 Gram and odd-pole overlaps for exact averaged features with rational
Simpson intervals and a rigorously charged fourth-derivative remainder.

The 4x4 positive inverse correction is certified via a *rational variational
dual witness*, avoiding sign errors in matrix adjugates and ever computing
the unrestricted Fourier reciprocal. All accepting decisions use Fraction.
"""
from fractions import Fraction as F

from validate_rpb108_si06_negative_band import PI, B, prime_interval
from validate_rpb108_si13_odd_fourier_reference import arch_lower
from validate_rpb108_si18_odd_rank_two_woodbury import gram, signed_odd_overlap
from validate_rpb108_si12_even_supported_inverse import sinh_bounds

KAPPA = F(1,1000)
CENTERS = (F(3,10), F(19,25), F(6,5), F(33,20))
RADIUS = F(1,50)
DELTAS = (F(27,10), F(5,4), F(17,20), F(7,10))
CELLS = 128


def plus(a,b):
    return (a[0]+b[0],a[1]+b[1])


def times(a,b):
    vals = (a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
    return (min(vals),max(vals))


def scale(q,span):
    return times((q,q),span)


def outward(span, digits=12):
    """Exact outward DECIMAL rational enclosure (no float assumptions).

    Large intermediate Machin/Taylor denominators are removed *after*
    their interval proofs: the rounded interval strictly contains the
    exact source interval and charges <10^-digits at each endpoint.
    """
    d=10**digits
    a,b=span
    aa=a*d
    bb=b*d
    lo=aa.numerator//aa.denominator
    hi=-((-bb.numerator)//bb.denominator)
    return (F(lo,d),F(hi,d))


def midpoint(span):
    return (span[0]+span[1])/2


def certify_original_window(center,delta):
    left=center-RADIUS
    right=center+RADIUS
    smallest=None
    for i in range(CELLS):
        l=left+(right-left)*i/CELLS
        r=left+(right-left)*(i+1)/CELLS
        mid=(l+r)/2
        # Same whole-cell arch monotonicity and original signed prime
        # Lipschitz 69 used throughout SI06–SI19. No sample-only claim.
        lower=arch_lower(l)+prime_interval(mid)[0]-F(69,2)*(r-l)
        assert lower > KAPPA+delta, (
            "original signed positivity failed",center,delta,i,float(lower))
        smallest=lower if smallest is None else min(smallest,lower)
    return smallest


def simpson_terms(center):
    # Average of h_xi over [c-r,c+r] via normalized 1-panel Simpson.
    return ((center-RADIUS,F(1,6)),(center,F(2,3)),
            (center+RADIUS,F(1,6)))


def averaged_q_interval(center):
    total=(F(0),F(0))
    for c,w in simpson_terms(center):
        total=plus(total,scale(w,signed_odd_overlap(c)))
    return total


def averaged_gram_interval(c,d):
    total=(F(0),F(0))
    for x,wx in simpson_terms(c):
        for y,wy in simpson_terms(d):
            total=plus(total,scale(wx*wy,gram(x,y)))
    return total


def solve_exact(matrix, vector):
    """Exact rational Gaussian elimination; midpoint only picks witness."""
    n=len(vector)
    a=[list(matrix[i])+[vector[i]] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]!=0),None)
        assert pivot is not None
        a[j],a[pivot]=a[pivot],a[j]
        factor=a[j][j]
        a[j]=[x/factor for x in a[j]]
        for i in range(n):
            if i==j:
                continue
            scale_i=a[i][j]
            a[i]=[a[i][k]-scale_i*a[j][k] for k in range(n+1)]
    return [a[i][-1] for i in range(n)]


def variational_lower(q,M,z):
    """Rigorous lower bound 2 z^T q-z^T M z for actual interval data."""
    n=len(q)
    lower=F(0)
    for i in range(n):
        t=2*z[i]
        lower += t*(q[i][0] if t>=0 else q[i][1])
    for i in range(n):
        for j in range(n):
            t=z[i]*z[j]
            upper=t*(M[i][j][1] if t>=0 else M[i][j][0])
            lower -= upper
    return lower


def validate():
    signed_minima=[certify_original_window(c,d)
                   for c,d in zip(CENTERS,DELTAS)]
    assert all(signed_minima[i]>KAPPA+DELTAS[i]
               for i in range(3))
    assert CENTERS[0]+RADIUS<CENTERS[1]-RADIUS
    assert CENTERS[1]+RADIUS<CENTERS[2]-RADIUS
    assert CENTERS[2]+RADIUS<CENTERS[3]-RADIUS

    # For the TRUE frequency-averaged supported odd sine features
    # g_c(x)=sin(2*pi*c*x)*sinc(2*pi*r*x), Jensen gives EXACTLY:
    # T_[c-r,c+r],odd >= 4r |g_c><g_c|.
    # The positive remainder is operator-PSD, so kappa is NOT eroded.
    gamma=[4*RADIUS*d for d in DELTAS]
    assert all(g>0 for g in gamma)

    # Rigorous normalized one-panel Simpson 4th derivative remainder:
    # sup_|x|<=B |g_c(x)-sum_{t=c-r,c,c+r} w_t sin(2*pi*t*x)|
    # <= ((2r)^4/2880)*(2*pi*B)^4=(4*pi*r*B)^4/2880.
    # Frequency derivative fourth = (2*pi*x)^4*sin(2*pi*xi*x).
    tau=(4*PI[1]*RADIUS*B)**4/F(2880)
    assert F(0)<tau<F(3,10**6)
    # ||s||<1/2, sqrt(2B)<3/2; q error <3tau/4.
    # All true/Simpson sine averages are convex averages of |h|<=1,
    # hence norms <=sqrt(2B), Gram error <=4B*tau.
    qerr=F(3,4)*tau
    gerr=4*B*tau
    slo,shi=sinh_bounds(B)
    assert shi-B<F(1,4)
    assert 2*B<F(9,4)
    assert qerr<F(3,10**6) and gerr<F(14,10**6)

    q=[]
    G=[]
    for c in CENTERS:
        a,b=averaged_q_interval(c)
        q.append(outward((a-qerr,b+qerr)))
    for i,c in enumerate(CENTERS):
        row=[]
        for j,d in enumerate(CENTERS):
            a,b=averaged_gram_interval(c,d)
            row.append(outward((a-gerr,b+gerr)))
        G.append(row)

    # The original sign topology must stay: q(+,-,+);
    # the full 4x4 Gram, including all cross-terms, is paid.
    assert q[0][0]>0 and q[1][1]<0 and q[2][0]>0
    assert G[0][1][1]<0 and G[0][2][0]>0 and G[1][2][1]<0

    n=4
    M=[[(a/KAPPA + ((1/gamma[i]) if i==j else 0),
         b/KAPPA + ((1/gamma[i]) if i==j else 0))
        for j,(a,b) in enumerate(G[i])] for i in range(n)]

    # M=Gamma^-1+G/kappa >0 since it is the exact physical Gram.
    # For every real z, q^T M^-1 q >= 2z^T q-z^T M z.
    # Exact midpoint solve selects a good RATIONAL witness, but the final
    # bound charges full outward original q and M interval uncertainty.
    qmid=[midpoint(x) for x in q]
    Mmid=[[midpoint(x) for x in row] for row in M]
    z=solve_exact(Mmid,qmid)
    correction=variational_lower(q,M,z)
    assert correction>0
    S_up=F(235648,10**6)
    assert shi-B<S_up
    supported_response_ub=2*(S_up/KAPPA-correction/KAPPA**2)
    assert F(0)<supported_response_ub<F(4)  # SI21 rational improvement: original odd response <4
    assert supported_response_ub<F(5)  # SI20 remains independently certified

    print("SI21 PASS: original signed Jensen rank-four supported inverse certificate")
    print("Four all-frequency signed-window strict minima:",
          *(float(x) for x in signed_minima))
    print("centers:",*(float(x) for x in CENTERS),"r:",float(RADIUS))
    print("original positive margins delta:",*(float(x) for x in DELTAS))
    print("exact positive scalar floor, no Taylor penalty:",float(KAPPA))
    print("whole supported Simpson remainder:",float(tau))
    print("q error / complete physical Gram error:",float(qerr),float(gerr))
    print("certified q outward intervals:",[(float(a),float(b)) for a,b in q])
    print("certified full Gram outward intervals:",
          [[(float(a),float(b)) for a,b in row] for row in G])
    print("rational signed variational witness:",
          [float(x) for x in z])
    print("certified original odd inverse UPPER:",float(supported_response_ub))
    print("SI20 UPPER <5; SI21 UPPER <4 at same original operator")
    print("No full original A^-1 s, original residual Gram, complete BS, Stage I or RH")


if __name__ == "__main__":
    validate()
