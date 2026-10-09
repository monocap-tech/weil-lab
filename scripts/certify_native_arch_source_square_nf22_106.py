#!/usr/bin/env python3
"""NF22: rigorously enclose physical ARCHIMEDEAN source squares on e0/e1.

The exact original endpoint singularity -1/2 log(a²-x²) is integrated
analytically using rational log-moment identities. The analytic remainder
is approximated by a degree-320 rational polynomial with its full Cauchy
L2 error paid. This is NOT the full arch+prime+pole source-square Gram.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb,factorial
import json
from certify_native_arch_source_uniform_nf22_106 import A,DEGREE,kernel_coefficients

N=DEGREE
h=kernel_coefficients(N)

# Exact even regular polynomial P and odd integrated-kernel difference V.
P={}
V={}
for j in range(0,N+1,2):
    P[j]=-2*sum((h[k]*F(comb(k,j),k)*A**(k-j)
               for k in range(max(1,j),N+1)),F(0))
for j in range(1,N+2,2):
    V[j]=(F(1) if j==1 else F(0))+2*sum(
        (h[k]*F(comb(k+1,j),k+1)*A**(k+1-j)
         for k in range(max(1,j-1),N+1)),F(0))
odd_regular={j:V.get(j,F(0))+P.get(j-1,F(0))
             for j in range(1,N+2,2)}

@lru_cache(None)
def mass_moment(n):
    assert n>=0 and n%2==0
    return 2*A**(n+1)/F(n+1)

@lru_cache(None)
def odd_harmonic(m):
    return sum((F(1,2*k-1) for k in range(1,m+2)),F(0))

def dot(p,q):
    return sum((x*y*mass_moment(i+j) for i,x in p.items()
                for j,y in q.items() if x and y),F(0))
def integral(p):
    return sum((x*mass_moment(i) for i,x in p.items() if i%2==0),F(0))
def harmonic_weighted(p):
    return sum((x*mass_moment(i)*odd_harmonic(i//2)
                for i,x in p.items() if i%2==0),F(0))

class I:
    def __init__(self,lo,hi=None):
        if isinstance(lo,I):self.lo,self.hi=lo.lo,lo.hi;return
        self.lo=F(lo);self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,v):
        v=I(v);return I(self.lo+v.lo,self.hi+v.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,v):return self+-I(v)
    def __rsub__(self,v):return I(v)+-self
    def __mul__(self,v):
        v=I(v)
        q=[x*y for x in (self.lo,self.hi) for y in (v.lo,v.hi)]
        return I(min(q),max(q))
    __rmul__=__mul__
    def __truediv__(self,v):
        v=I(v);assert v.lo>0 or v.hi<0
        return self*I(1/v.hi,1/v.lo)
    def __pow__(self,k):
        assert k==2
        if self.lo<=0<=self.hi:return I(0,max(self.lo**2,self.hi**2))
        return I(min(self.lo**2,self.hi**2),max(self.lo**2,self.hi**2))

def log_unit(q,terms=250):
    assert q>0
    z=(q-1)/(q+1);p=z;s=F(0)
    for k in range(terms):
        s+=2*p/F(2*k+1)
        p*=z*z
    e=2*abs(p)/(F(2*terms+1)*(1-z*z))
    return I(s-e,s+e)

def log_r(q,terms=250):
    assert q>0
    k=0
    while q>=2:q/=2;k+=1
    while q<1:q*=2;k-=1
    return log_unit(q,terms)+k*log_unit(F(2),terms)

def atan_r(q,terms=200):
    assert abs(q)<1
    s=F(0);p=q
    for k in range(terms):
        s+=(-1)**k*p/F(2*k+1)
        p*=q*q
    e=abs(p)/F(2*terms+1)
    return I(s-e,s+e)

def bernoulli(n):
    b=[F(1)]
    for m in range(1,n+1):
        b.append(-sum((F(comb(m+1,k))*b[k]
                       for k in range(m)),F(0))/F(m+1))
    return b

def bounds():
    pi=16*atan_r(F(1,5))-4*atan_r(F(1,239))
    # Round the pi interval outward before taking log to keep denominators
    # manageable. This is a SAFE enlargement, not a precision substitution.
    grid=10**90
    l=F((pi.lo*grid).__floor__(),grid)
    u=F((pi.hi*grid).__ceil__(),grid)
    lnpi=I(log_r(l,260).lo,log_r(u,260).hi)
    ln2=log_r(F(2),330)
    Z=ln2+log_r(A,330) # Z=log(2a)
    B=bernoulli(42)
    gamma=I(sum((F(1,k) for k in range(1,101)),F(0))-F(1,200))-log_r(F(100),330)
    for k in range(1,21):
        gamma+=B[2*k]/F(2*k*100**(2*k))
    e=abs(B[42])/F(42*100**42)
    gamma+=I(-e,e)
    c=-gamma-ln2-lnpi # c=-EulerGamma-log(2pi)

    I0=mass_moment(0);I2=mass_moment(2)
    Ip=integral(P);Ipp=dot(P,P);Iph=harmonic_weighted(P)
    xq={j+1:v for j,v in odd_regular.items()}
    Ixq=integral(xq);Ixqh=harmonic_weighted(xq)
    Iq2=dot(odd_regular,odd_regular)

    # Exact moments:
    # integral x^(2m) L = M_m*2[Z-Hodd(m)]
    # integral x^(2m) L^2 =
    # M_m*(4[Z-Hodd(m)]^2 -pi^2/3+4 Hodd2(m)).
    # Here L=log(a²-x²).
    E0=(I0*c**2+2*c*Ip+Ipp-2*c*(Z-1)*I0-2*Z*Ip+2*Iph+
        I0*((Z-1)**2-pi**2/12+1))/(2*A)
    E1=F(3)/(2*A**3)*(Iq2+2*c*Ixq+c**2*I2-2*Z*Ixq+2*Ixqh-
        2*c*(Z-F(4,3))*I2+
        I2*((Z-F(4,3))**2-pi**2/12+F(10,9)))

    rho=F(106,125);eps=4*rho**N/(1-rho)
    assert eps<F(1,10**20)
    err0=4*A*eps;err1=14*A*eps
    # Exact square difference: | ||f||²-||f_N||² |
    # <= error * (||f||+||f_N||); both <4+error.
    assert 0<E0.lo<=E0.hi<16 and 0<E1.lo<=E1.hi<16
    S0=I(E0.lo-err0*(8+err0),E0.hi+err0*(8+err0))
    S1=I(E1.lo-err1*(8+err1),E1.hi+err1*(8+err1))
    g=10**12
    def rounded(t):
        return [str(F((t.lo*g).__floor__(),g)),
                str(F((t.hi*g).__ceil__(),g))]
    assert F(708214407559,10**11)<S0.lo
    assert S0.hi<F(7082144075591,10**12)
    assert F(1083143528165,10**12)<S1.lo
    assert S1.hi<F(1083143528166,10**12)
    return dict(milestone="NF22",aperture="53/50",degree=N,
        original_arch_source_e0_square_strict=rounded(S0),
        original_arch_source_e1_square_strict=rounded(S1),
        analytic_Cauchy_remainder_sup_less_than="1e-20",
        original_endpoint_logs_integrated_exactly=True,
        archimedean_only=True,complete_Weil_source_square=False,
        all_arch_prime_pole_crosses=False,
        complete_residual_P2=False,whole_aperture_positive=False)

if __name__=="__main__":print(json.dumps(bounds(),indent=2))
