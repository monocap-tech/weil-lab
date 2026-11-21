#!/usr/bin/env python3
"""PI021 ANALYTIC-ONLY exact meromorphic-residue sanity checks.

PI021's new infinite-spectrum theorem is a CLASSICAL PROOF, not proved by
this finite regression. This script uses Fraction for exact arithmetic
to check the crucial residue-isolation step in finite examples:
    F(s) = sum_j t_j/(s-i*z_j), |Im z_j| <= 1/4.
At s=i*z_k+epsilon, epsilon*F(s) -> t_k.
The pole residue is exactly the spectral coefficient, and a purported
entire Laplace transform cannot contain a nonzero one.

The regression does NOT read zeta zeros, prove zero counting, establish
Masullo's trace, compile Lean, invoke GitHub Actions or assert RH.
"""
from fractions import Fraction as Q

C = tuple[Q, Q]  # exact Gaussian rational (real, imaginary)


def add(a:C,b:C)->C: return a[0]+b[0], a[1]+b[1]
def sub(a:C,b:C)->C: return a[0]-b[0], a[1]-b[1]
def mul(a:C,b:C)->C: return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]
def inv(a:C)->C:
    d=a[0]*a[0]+a[1]*a[1]
    if d == 0: raise ZeroDivisionError("Actual meromorphic pole")
    return a[0]/d, -a[1]/d
def div(a:C,b:C)->C: return mul(a,inv(b))
def sqnorm(a:C)->Q: return a[0]*a[0]+a[1]*a[1]


def pole(n:int)->C:
    # z_n=n+i/4; i*z_n=-1/4+i*n; imaginary parts of z_n bounded.
    assert n!=0
    return -Q(1,4),Q(n)


def weight(n:int)->Q:
    assert n!=0
    return Q(1,(1+abs(n))**6)


def meromorphic_sum(s:C, indices:range)->C:
    out: C=(Q(0),Q(0))
    for n in indices:
        if n:
            out=add(out,div((weight(n),Q(0)),sub(s,pole(n))))
    return out


def main()->None:
    indices=range(-8,9)
    checks=0
    for k in (-5,-3,-1,1,2,4,6):
        for denom in (20,80,320):
            eps=Q(1,denom)
            s=add(pole(k),(eps,Q(0)))
            observed=mul((eps,Q(0)),meromorphic_sum(s,indices))
            difference=sub(observed,(weight(k),Q(0)))
            # Exact triangle estimate from all OTHER pole distances:
            # |epsilon*sum t_n/(epsilon+i(k-n))|
            # <= epsilon*sum t_n/|k-n| for n!=k.
            bound=eps*sum(
                (weight(n)/abs(k-n)
                 for n in indices if n and n!=k),Q(0))
            assert sqnorm(difference) <= bound*bound
            checks+=1

    # At their actual pole, the terms in the meromorphic series have
    # nonzero residues, with noncentral, real-frequency separation.
    for n in indices:
        if n:
            assert weight(n)>0
            assert pole(n)!=pole(-n)

    # A discrete infinite real-frequency series can vanish on a BOUNDED
    # open interval (smooth periodic Fourier series with local support).
    # That counterexample is proved in the PI021 memo; no finite sample
    # test could certify an interval vanishing identically.
    print("PI021 EXACT GAUSSIAN-RATIONAL LAPLACE-POLE REGRESSION: PASS")
    print(f"{checks} finite-meromorphic residue-isolation bounds")
    print("Nonzero residues obstruct entire continuation if a spectral")
    print("exponential sum vanishes on the FULL right half-line a>A.")
    print("NO zeta-zero data, spectral trace, infinite-series proof, Lean, RH.")


if __name__=="__main__":
    main()
