#!/usr/bin/env python3
"""NF23: rational outward complete original physical source Gram on e0/e1.

No quadrature. Original 13 translation cells, exact endpoint log primitives,
NF22 degree-320 regular polynomial and paid physical L2 remainder. Hyperbolic
pole factors use rational Taylor polynomials with explicit uniform remainder.
This two-mode Gram is not the 58-column Gram or a whole-domain sign.
"""
from fractions import Fraction as F
from math import comb, factorial
from functools import lru_cache
import json
import certify_native_arch_source_square_nf22_106 as arch
import certify_native_source_square_prime_pole_nf21_106 as pp

A=arch.A
I=pp.I

def lift(v):return I(v.lo,v.hi)

def constants():
    pi=16*arch.atan_r(F(1,5))-4*arch.atan_r(F(1,239))
    pi=lift(pi)
    lnpi=I(arch.log_r(pi.l).lo,arch.log_r(pi.h).hi)
    b=arch.bernoulli(42)
    gamma=I(sum((F(1,k) for k in range(1,101)),F(0))-F(1,200))-lift(arch.log_r(F(100)))
    for k in range(1,21):gamma+=b[2*k]/F(2*k*100**(2*k))
    err=abs(b[42])/F(42*100**42)
    gamma+=I(-err,err)
    return -gamma-pp.log(2)-lnpi

def log_i(t):
    assert t.l>0
    return I(pp.log(t.l).l,pp.log(t.h).h)

def add(p,q):
    r=dict(p)
    for k,v in q.items():r[k]=r.get(k,F(0))+v
    return r

def mul(p,q):
    r={}
    for i,x in p.items():
        for j,y in q.items():r[i+j]=r.get(i+j,F(0))+x*y
    return r

def polynomial_integral(p,L,U):
    ans=I(0)
    # Grid rounding bounds every endpoint and coefficient operation.
    for n,v in p.items():ans+=v*(U**(n+1)-L**(n+1))/F(n+1)
    return ans

def log_primitive(n,x,sign):
    # t=a+sign*x; x=sign*(t-a), dx=sign*dt.
    t=I(A)+sign*x
    if t.l==t.h==0:return I(0) # continuous t^k log(t) limit
    lt=log_i(t)
    ans=I(0)
    for k in range(n+1):
        ans+=F(sign**(n+1)*comb(n,k))*(-A)**(n-k)*t**(k+1)/F(k+1)*(lt-F(1,k+1))
    return ans

def log_integral(n,L,U):
    return sum((log_primitive(n,U,s)-log_primitive(n,L,s) for s in (-1,1)),I(0))

def arch_pair_cell(p,parity,L,U,c):
    regular=arch.P if parity==0 else arch.odd_regular
    factor={0:F(1)} if parity==0 else {1:F(1)}
    weighted=mul(p,factor)
    val=polynomial_integral(mul(p,regular),L,U)+c*polynomial_integral(weighted,L,U)
    for n,v in weighted.items():val-=v*log_integral(n,L,U)/2
    return val

def full_arch_pair(p,parity,c):
    regular=arch.P if parity==0 else arch.odd_regular
    weighted=p if parity==0 else {n+1:v for n,v in p.items()}
    # Parity is exact; all monomials in these integrands are even.
    val=I(0)
    for n,v in mul(p,regular).items():
        assert n%2==0
        val+=v*arch.mass_moment(n)
    Z=pp.log(2*A)
    for n,v in weighted.items():
        assert n%2==0
        M=arch.mass_moment(n)
        val+=v*M*(c-Z+arch.odd_harmonic(n//2))
    return val

def enlarge(v,e):return v+I(-e,e)

def display(v,digits=12):
    g=10**digits
    def decimal(k):
        sign='-' if k<0 else ''
        k=abs(k)
        return f'{sign}{k//g}.{k%g:0{digits}d}'
    return [decimal((v.l*g).__floor__()),decimal((v.h*g).__ceil__())]

def certify():
    c=constants()
    powers=(2,3,4,5,7,8)
    logs={n:pp.log(n) for n in powers}
    weights={n:(logs[2] if n in (4,8) else logs[n])/pp.sqrt(F(n)) for n in powers}
    shifts=[(s*logs[n],weights[n]) for n in powers for s in (1,-1)]
    cuts=[I(-A),I(A)]
    for t,w in shifts:cuts.append(I(A)-t if t.l>0 else I(-A)-t)
    cuts.sort(key=lambda t:t.l)
    assert len(cuts)==14
    assert all(l.h<u.l for l,u in zip(cuts,cuts[1:]))
    prime=[I(0),I(0)];ledger=[]
    for L,U in zip(cuts,cuts[1:]):
        x=(L.h+U.l)/2
        selected=[]
        for t,w in shifts:
            inside=(-A<(I(x)+t).l and (I(x)+t).h<A)
            outside=((I(x)+t).h<-A or (I(x)+t).l>A)
            assert inside or outside
            if inside:selected.append((t,w))
        b0=sum((w for t,w in selected),I(0))
        b1=sum((w*t for t,w in selected),I(0))
        v0=-arch_pair_cell({0:b0},0,L,U,c)/A
        v1=-3*arch_pair_cell({0:b1,1:b0},1,L,U,c)/A**3
        prime[0]+=v0;prime[1]+=v1
        ledger.append(dict(left=L.asstr(),right=U.asstr(),active_orientations=len(selected),twice_arch_prime_even=v0.asstr(),twice_arch_prime_odd=v1.asstr()))
    # cosh/sinh(x/2) Taylor polynomials: retain powers 0..40.
    # On |x|<=a, exp(|x|/2)<2, hence each omitted parity tail
    # is bounded by the full exponential remainder 2*(a/2)^41/41!.
    cosh={k:F(1,2**k*factorial(k)) for k in range(0,41,2)}
    sinh={k:F(1,2**k*factorial(k)) for k in range(1,41,2)}
    rem=2*(A/2)**41/F(factorial(41))
    sh=pp.sinh(I(A)/2);ch=pp.cosh(I(A)/2)
    pole0=8*sh/A*full_arch_pair(cosh,0,c)
    pole1=-6/A**3*(4*A*ch-8*sh)*full_arch_pair(sinh,1,c)
    # ||arch_N e_j||<4 (NF22); polynomial hyperbolic error paid
    # by Cauchy-Schwarz on the physical interval. Conservative rational
    # bounds C0<1, C1<2, sqrt(2a)<2, sh<1, |4a ch-8sh|<16.
    pole0=enlarge(pole0,128*rem)
    pole1=enlarge(pole1,1024*rem)
    eps=4*F(106,125)**arch.N/(1-F(106,125))
    delta=[4*A*eps,14*A*eps]
    # NF21 physical source norms: prime<3 and pole<5 in both parities.
    for j in (0,1):prime[j]=enlarge(prime[j],6*delta[j])
    pole=[enlarge(pole0,10*delta[0]),enlarge(pole1,10*delta[1])]
    sectors=pp.certificate()
    for j in (0,1):
        assert F(sectors[f'prime_only_source_square_gram_{j}{j}'][1])<9
        assert F(sectors[f'pole_only_source_square_gram_{j}{j}'][1])<25
    squares=[I(F('7.082144075590'),F('7.082144075591')),
             I(F('1.083143528165'),F('1.083143528166'))]
    full=[]
    for j in (0,1):
        base=I(*map(F,sectors[f'prime_plus_pole_source_square_gram_{j}{j}']))
        s=squares[j]+base+prime[j]+pole[j]
        assert s.l>0 and s.h-s.l<F(2,10**12)
        assert prime[j].h-prime[j].l<F(1,10**15)
        assert pole[j].h-pole[j].l<F(1,10**15)
        full.append(s)
    return dict(milestone='NF23',aperture='53/50',translation_cells=13,
        twice_arch_prime=[v.asstr() for v in prime],twice_arch_pole=[v.asstr() for v in pole],
        twice_arch_prime_outward_1e12=[display(v) for v in prime],
        twice_arch_pole_outward_1e12=[display(v) for v in pole],
        complete_source_square_gram_diagonal=[v.asstr() for v in full],
        complete_source_square_outward_1e12=[display(v) for v in full],
        complete_source_square_gram_offdiagonal=['0','0'],
        arch_degree=arch.N,pole_taylor_degree=40,pole_uniform_remainder=str(rem),
        arch_L2_errors=[str(v) for v in delta],cell_ledger=ledger,
        complete_low2_source_square_certified=True,full_58_column_source_gram=False,
        compensated_residual_P2=False,whole_aperture_positive=False,RH=False,Lean=False)

if __name__=='__main__':print(json.dumps(certify(),indent=2))
