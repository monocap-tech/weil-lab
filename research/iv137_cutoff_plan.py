"""Exact integer cutoff planning for IV127's leakage inequality.

M is an input upper bound, NOT a computed arithmetic certificate.
Uses pi<4 and log(2)>1/2, so T=2^m and log(e+T)>m/2.
"""
import argparse
from fractions import Fraction as Q
from math import isqrt

def ceil(q):
    return -(-q.numerator // q.denominator)

def plan(M, eta=Q(1), eps=Q(1, 4), a=Q(11, 10)):
    M, eta, eps, a = map(Q, (M, eta, eps, a))
    if M < 0 or eta <= 0 or not 0 < eps < 1 or a <= 0:
        raise ValueError("require M>=0, eta>0, 0<eps<1, a>0")
    m = max(1, ceil(2*(M+eta)/(1-eps)))
    T = 1 << m
    # 16*pi^2*a*(2a)^2*T^3/3 < 1024*a^3*T^3/3
    K = Q(1024,3)*a**3*T**3/eps
    N = max(1, isqrt(ceil(K)))
    if N*N < K:
        N += 1
    assert N*N >= K
    assert (1-eps)*Q(m,2)-M >= eta
    assert N == 1 or (N-1)**2 < K
    return m,T,N

if __name__ == "__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("M",type=Q)
    p.add_argument("--eta",type=Q,default=Q(1))
    p.add_argument("--eps",type=Q,default=Q(1,4))
    x=p.parse_args()
    m,T,N=plan(x.M,x.eta,x.eps)
    print("CONDITIONAL on supplied certified total budget",x.M)
    print("m =",m,"T =",T,"N =",N)
