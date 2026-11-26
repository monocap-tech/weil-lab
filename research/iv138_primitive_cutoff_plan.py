"""Compare conservative IV127 leakage and proposed primitive leakage.

The primitive bound is a mathematical planning assumption, not yet native Lean.
M is hypothetical or independently certified; no arithmetic enclosure is computed.
"""
from fractions import Fraction as Q
from math import isqrt
def ceil(q): return -(-q.numerator//q.denominator)
def rootceil(q):
    n=isqrt(ceil(q))
    return n+(n*n<q)
def plan(M,eta=Q(1),eps=Q(1,4),a=Q(11,10)):
    M,eta,eps,a=map(Q,(M,eta,eps,a))
    assert M>=0 and eta>0 and 0<eps<1 and a>0
    m=max(1,ceil(2*(M+eta)/(1-eps)))
    T=1<<m
    old=Q(1024,3)*a**3*T**3/eps
    new=16*a*a*T*T/eps
    N0,N1=rootceil(old),rootceil(new)
    assert N0*N0>=old and N1*N1>=new
    assert (N0-1)**2<old and (N1-1)**2<new
    assert (1-eps)*Q(m,2)-M>=eta
    return T,N0,N1
if __name__=="__main__":
    for M in (3,5,10,20):
        print(M,*plan(M))
