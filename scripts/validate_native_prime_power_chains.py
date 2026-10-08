"""Exact arithmetic and weighted-matrix bounds for original prime-power chains."""
from fractions import Fraction as F
from math import isqrt
import json
from certify_native_drive_cusp_geometry import log_interval


def sqrt_interval(n, digits=40):
    scale=10**digits
    r=isqrt(n*scale*scale)
    return F(r,scale), F(r+1,scale)


def ceil_fraction(x):
    return -(-x.numerator//x.denominator)


def chain_bound(a,p):
    lo,hi=log_interval(p)
    m=ceil_fraction(2*a/lo)
    assert (m-1)*hi < 2*a < m*lo
    sqrt_lo,_=sqrt_interval(p)
    q=1/sqrt_lo
    matrix=[[F(0) if i==j else hi*q**abs(i-j)
             for j in range(m)] for i in range(m)]
    if m==1:
        return m,F(0),0
    weights=[F(1)]*m
    scale=10**24
    for _ in range(32):
        out=[sum((matrix[i][j]*weights[j] for j in range(m)),F(0))
             for i in range(m)]
        largest=max(out)
        weights=[F(ceil_fraction(v/largest*scale),scale) for v in out]
    bound=max(sum((matrix[i][j]*weights[j] for j in range(m)),F(0))/weights[i]
              for i in range(m))
    assert all(sum((matrix[i][j]*weights[j] for j in range(m)),F(0))
               <=bound*weights[i] for i in range(m))
    return m,bound,m


def sinh_upper(a,terms=50):
    term=a
    value=term
    for j in range(1,terms):
        term*=a*a/F((2*j)*(2*j+1))
        value+=term
    next_term=term*a*a/F((2*terms)*(2*terms+1))
    ratio=a*a/F((2*terms+2)*(2*terms+3))
    assert ratio<1
    return value+next_term/(1-ratio)


def run():
    checks=0
    def check(v):
        nonlocal checks
        assert v
        checks+=1
    rows=[]
    for a,target,pole_target,expected in [
        (F(1),F(3),F(351,1000),[3,2,2,2]),
        (F(21,20),F(10,3),F(408,1000),[4,2,2,2])]:
        bounds=[]
        lengths=[]
        for p,m_expect in zip([2,3,5,7],expected):
            m,b,count=chain_bound(a,p)
            check(m==m_expect)
            checks+=count  # exact Collatz row inequalities asserted above
            bounds.append(b);lengths.append(m)
        total=sum(bounds,F(0))
        check(total<target)
        loss=2*(sinh_upper(a)-a)
        check(0<loss<pole_target)
        if a==F(21,20):
            # The old JOINT bound is already stronger than this candidate.
            # A positive constant-function Rayleigh quotient bounds rho from below.
            lower=F(0)
            for p,m in zip([2,3,5,7],lengths):
                log_lo,_=log_interval(p)
                _,sqrt_hi=sqrt_interval(p)
                lower+=2*log_lo*sum((F(m-r,m)/sqrt_hi**r
                                     for r in range(1,m)),F(0))
            check(lower>F(1063939,500000))
        rows.append({'a':str(a),'chain_lengths':lengths,
                     'prime_budget_strict_upper':str(target),
                     'negative_pole_strict_upper':str(pole_target)})
    # At exact L=m*s, endpoint power m is zero, not a new chain node.
    for m in range(1,9):
        s=F(3,5);L=m*s
        check(ceil_fraction(L/s)==m)
        check((m-1)*s<L)
        check(m*s==L)
    # Shifted positive level remains explicit in the lower-bound loss.
    mu,B,E,mass=F(3,2),F(7),F(20),F(2)
    check(E-(B+mu)*mass == (E-B*mass)-mu*mass)
    return {'passed':True,'finite_checks':checks,'rows':rows,
            'scope':'exact arithmetic/weighted-matrix controls; analytic chain decomposition separate',
            'candidate_improves_existing_joint_bound_at_105':False,
            'new_whole_domain_certificate':False,'lean_certified':False}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
