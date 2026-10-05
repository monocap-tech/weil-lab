"""Exact integer polynomial products and antiderivative-Horner correlations."""
from math import lcm,comb
from fractions import Fraction as F


def mul(p,q):
    dp=lcm(*(x.denominator for x in p));dq=lcm(*(x.denominator for x in q))
    pp=[int(x*dp) for x in p];qq=[int(x*dq) for x in q]
    out=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(pp):
        if x:
            for j,y in enumerate(qq):
                if y:out[i+j]+=x*y
    return [F(x,dp*dq) for x in out]


def correlation(p,q):
    """Integral from y-1 to 1 of p(x)q(x-y) dx, as a polynomial in y."""
    dp=lcm(*(x.denominator for x in p));dq=lcm(*(x.denominator for x in q))
    pp=[int(x*dp) for x in p];qq=[int(x*dq) for x in q]
    size=len(p)+len(q);den=lcm(*range(1,size))
    primitive=[[0]*size for _ in range(size)]
    for i,x in enumerate(pp):
        if x:
            for j,y in enumerate(qq):
                if y:
                    for k in range(j+1):
                        m=i+j-k+1
                        primitive[m][k]+=x*y*comb(j,k)*(-1)**k*(den//m)
    upper=[sum(row[k] for row in primitive) for k in range(size)]
    lower=[0]*size
    # Evaluate the x-antiderivative at x=y-1 using polynomial Horner.
    for row in reversed(primitive):
        assert lower[-1]==0  # The total-degree bound prevents truncation.
        lower=[row[k]-lower[k]+(lower[k-1] if k else 0) for k in range(size)]
    return [F(x-y,dp*dq*den) for x,y in zip(upper,lower)]
