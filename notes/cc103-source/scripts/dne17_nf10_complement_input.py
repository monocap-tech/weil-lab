#!/usr/bin/env python3
"""NF10: independent exact-rational original prime-8 112-vector complement.
Fixed aperture 53/50; complete six-prime translation operator, depth-6
Bessel high-frequency mass (degrees >=112), archimedean and pole bounds.
The sign of the complete original Weil form on D_a is NOT asserted.
"""
from fractions import Fraction as F
from math import factorial, isqrt
import json

A = F(53,50)
K = 112
POWERS = (2,3,4,5,7,8)
BASE = {n:(2 if n in (4,8) else n) for n in POWERS}

def log_bounds(n,N=220):
    x=F(n-1,n+1);p=x;s=F(0)
    for j in range(N):
        s+=2*p/F(2*j+1);p*=x*x
    return s,s+2*p/(F(2*N+1)*(1-x*x))

def pi_bounds(N=65):
    def at(x):
        s=F(0);p=x
        for j in range(N):
            s+=(-1)**j*p/F(2*j+1);p*=x*x
        e=p/F(2*N+1)
        return s-e,s+e
    u,v=at(F(1,5)),at(F(1,239))
    return 16*u[0]-4*v[1],16*u[1]-4*v[0]

PI=pi_bounds()
LOG={n:log_bounds(n) for n in (2,3,5,7)}
LOG[4]=tuple(2*x for x in LOG[2])
LOG[8]=tuple(3*x for x in LOG[2])
LOG[9]=tuple(2*x for x in LOG[3])
LOG[14]=(LOG[2][0]+LOG[7][0],LOG[2][1]+LOG[7][1])
LOG[15]=(LOG[3][0]+LOG[5][0],LOG[3][1]+LOG[5][1])
LOG[16]=tuple(4*x for x in LOG[2])
assert LOG[8][1]<2*A<LOG[9][0]

def sq_min(l,r):
    return F(0) if l<=0<=r else min(l*l,r*r)
def w_lower(l,r):
    return F(5,8)+F(3,8)*sq_min(l,r)/A**2
def w_upper(l,r):
    return F(5,8)+F(3,8)*max(l*l,r*r)/A**2

def prime_weighted_upper(mesh=6000):
    """Rigorous interval cell covering for Schur weight
       w(x)=5/8+3x^2/(8a^2), x in [-a,a].
       All active shifts counted; cells crossing support cuts use a
       safely enlarged possible-overlap interval, never a missed term.
    """
    amp={}
    for n in POWERS:
        sq=F(isqrt(n*10**36),10**18)
        amp[n]=LOG[BASE[n]][1]/sq
    bound=F(0);worst=0
    for i in range(mesh):
        l=-A+2*A*i/mesh;r=-A+2*A*(i+1)/mesh
        total=F(0)
        for n in POWERS:
            for sign in (1,-1):
                lg=LOG[n]
                y1=l+sign*(lg[0] if sign>0 else lg[1])
                y2=r+sign*(lg[1] if sign>0 else lg[0])
                if y2<=-A or y1>=A:continue
                p=max(-A,y1);q=min(A,y2)
                if p<=q:total+=amp[n]*w_upper(p,q)
        row=total/w_lower(l,r)
        if row>bound:bound=row;worst=i
    assert bound<F(257,100)  # sharper than chosen 13/5
    return bound,worst,mesh

def derivative_coeffs(n,depth=6):
    c=[F(1,2*n+3)]
    for _ in range(depth):
        sq=[F(0)]*(2*len(c)-1)
        for j,x in enumerate(c):
            for k,y in enumerate(c):sq[j+k]+=x*y
        c=[F(1,2*n+3)]+[x/F(2*n+2*j+5) for j,x in enumerate(sq)]
    return c

GRID=10**8
def floor_grid(x):return F((x*GRID).__floor__(),GRID)
def ceil_grid(x):return F((x*GRID).__ceil__(),GRID)
def exp_poly_lower(x,terms=155):
    """Positive truncated exponential series, exact rational lower."""
    acc=F(1);t=F(1)
    for j in range(1,terms):
        t=t*x/j;acc+=t
    return acc

def rate_lower():
    """Coefficients decrease monotonically with n by their positive
    convolution/denominator recursion. Therefore the smallest rate
    across n>=112 and T<=16 is bounded below using n=112 and T=16.
    """
    c=derivative_coeffs(K)
    y=ceil_grid(2*A*PI[1]*16)
    p=y*y;s=F(0)
    for v in c:
        s+=v*p;p*=y*y
    lower=2*K+1-2*s
    assert lower>80
    return lower

def integrated_mass_upper(T,rate=75):
    """Inherit the depth-6 positive-region Bessel/Legendre integrated
    mass inequality, but compute a conservative upper with rational
    outward-rounded first 48 terms and an undamped geometric tail.
    """
    T=F(T)
    lo=floor_grid(2*A*PI[0]*T)
    hi=ceil_grid(2*A*PI[1]*T)
    assert hi*hi<K*(K+1)
    double_factorial=1
    for z in range(1,2*K+2,2):double_factorial*=z
    total=F(0)
    for n in range(K,K+48):
        c=derivative_coeffs(n)
        p=lo*lo;exponent=F(0)
        for j in range(12):
            exponent+=c[j]*p/F(j+1)
            p*=lo*lo
        exponent=F((exponent*1000).__floor__(),1000)
        assert exponent>0
        attenuation=1/exp_poly_lower(exponent)
        term=4*A*T*(2*n+1)*hi**(2*n)*attenuation/(rate*double_factorial**2)
        # Upward exact 1e-18 rounding of every term.
        term=F((term*10**18).__ceil__(),10**18)
        total+=term
        double_factorial*=2*n+3
    n=K+48
    y=2*A*F(22,7)*T
    ratio=y*y/F((2*n+1)*(2*n+3))
    assert ratio<1
    tail=4*A*T*y**(2*n)/(double_factorial**2*(1-ratio))
    total+=F((tail*10**18).__ceil__(),10**18)
    return total

def certificate():
    prime,worst,mesh=prime_weighted_upper()
    rate=rate_lower()
    masses={T:integrated_mass_upper(T) for T in (14,15,16)}
    assert masses[14]<masses[15]<masses[16]
    def high(T):
        return LOG[T][0]-F(7,216)/T**2,LOG[T][1]-F(7,216)/T**2
    h14,h15,h16=(high(T) for T in (14,15,16))
    arch=h16[0]-(h14[1]+F(27,5))*masses[14]-(h15[1]-h14[0])*masses[15]-(h16[1]-h15[0])*masses[16]
    pole=16*A*(A/2)**(2*K)/factorial(K)**2
    remainder=arch-F(13,5)-pole
    assert arch>F(277,100)
    assert remainder>F(17,100)
    return dict(
      stage="NF10 fresh physical complement at aperture 53/50",
      aperture=str(A),physical_retained_degrees=list(range(112)),
      full_prime_powers=list(POWERS),both_translation_orientations=True,
      prime_schur_weight="5/8+3*x^2/(8*a^2)",
      prime_cell_cover=mesh,maximum_cell_index=worst,
      prime_interval_upper=str(F((prime*10**12).__ceil__(),10**12)),
      certified_joint_prime_norm_upper="13/5",
      depth6_rate_lower=str(F((rate*10**6).__floor__(),10**6)),
      depth6_conservative_rate_lower=75,
      cutoffs=[14,15,16],
      masses_upper={str(t):str(masses[t]) for t in masses},
      archimedean_lower=str(F((arch*10**12).__floor__(),10**12)),
      pole_upper=str(F((pole*10**120).__ceil__(),10**120)),
      raw_complement_lower=str(F((remainder*10**12).__floor__(),10**12)),
      certified_physical_complement_lower="17/100",
      source="full original prime-power shifts + inherited high-frequency arch and pole inequality",
      whole_native_112_built=False,source_gram_built=False,
      whole_domain_positive=False,global_RH=False,lean_certified=False)

if __name__=="__main__":
    print(json.dumps(certificate(),indent=2))
