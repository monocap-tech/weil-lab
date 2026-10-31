#!/usr/bin/env python3
"""EF24 — original signed n5/n7 edge FIR mixed: SOURCE-PINNED outward intervals.

This script uses ONLY stdlib exact integer endpoints (fixed-point radix
10**340) and original SI06 arctan/logarithm series with verified remainder.
The original 107 SI10 centers and 469 Taylor orders remain exact rationals.

The actual original FIR edge polynomial G(t)=prod(1-2cos(theta_j)t+t²)^pj
has a0..a210 from the universal exact Chebyshev-Newton recurrence.
Real/complex interval arithmetic is outward-rounded EVERY operation.
Original q_prime,5 and q_prime,7 are the exact EF23 211/39-term source
edge formulas. No fake high-precision float and no surrogate source.

This only measures ORIGINAL ARITHMETIC mixed M5/M7. Original arch M/E,
whole M and normalized Schur/RH are NOT measured, even when intervals pass.
"""
from fractions import Fraction as F
from math import factorial, isqrt
from decimal import Decimal, localcontext
from pathlib import Path
import json

from validate_rpb108_si06_negative_band import (
    B, ACTIVE, arctan_bounds, ln_bounds, PI as OLD_PI,
    WEIGHTS as OLD_W, SHIFTS as OLD_SHIFTS,
)
from validate_rpb108_ef21_original_even_fixed_bell import (
    H, R, N, authentic_source_replay,
)
from validate_rpb108_ef22_original_even_prime_energy_vanish import (
    exact_original_n2_signed_mixed_lower,
)

ROOT=Path(__file__).resolve().parents[1]
D=340
S=10**D
ZERO=(0,0)
ONE=(S,S)


def floor_ratio(a,b):
    assert b>0
    return a//b


def ceil_ratio(a,b):
    assert b>0
    return -((-a)//b)


class I:
    __slots__=("lo","hi")
    def __init__(self,lo,hi=None):
        self.lo=int(lo)
        self.hi=int(lo if hi is None else hi)
        assert self.lo<=self.hi
    @classmethod
    def rational(cls,x):
        x=F(x)
        return cls(floor_ratio(x.numerator*S,x.denominator),
                   ceil_ratio(x.numerator*S,x.denominator))
    @classmethod
    def rational_bounds(cls,lo,hi):
        lo,hi=F(lo),F(hi)
        assert lo<=hi
        return cls(floor_ratio(lo.numerator*S,lo.denominator),
                   ceil_ratio(hi.numerator*S,hi.denominator))
    def __add__(a,b):
        b=as_i(b)
        return I(a.lo+b.lo,a.hi+b.hi)
    __radd__=__add__
    def __neg__(a):
        return I(-a.hi,-a.lo)
    def __sub__(a,b):
        return a+(-as_i(b))
    def __rsub__(a,b):
        return as_i(b)+(-a)
    def __mul__(a,b):
        b=as_i(b)
        vals=[x*y for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
        return I(min(vals)//S,ceil_ratio(max(vals),S))
    __rmul__=__mul__
    def __truediv__(a,b):
        b=as_i(b)
        assert b.lo>0 or b.hi<0, "division by uncertain zero"
        vals=[(x*S,y) for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
        bounds=[]
        for x,y in vals:
            if y<0:x,y=-x,-y
            bounds.append((floor_ratio(x,y),ceil_ratio(x,y)))
        return I(min(x for x,_ in bounds),max(y for _,y in bounds))
    def scaled(self):
        with localcontext() as ctx:
            ctx.prec=20
            x=Decimal(self.lo).scaleb(-D)
            y=Decimal(self.hi).scaleb(-D)
            return f"[{x:.10e},{y:.10e}]"
    def sign(self):
        return "+" if self.lo>0 else "-" if self.hi<0 else "UNDETERMINED"
    def abs_upper(self):
        return max(abs(self.lo),abs(self.hi))
    def width(self):
        return self.hi-self.lo
    def excludes_zero(self):
        return self.lo>0 or self.hi<0


def as_i(x):
    return x if isinstance(x,I) else I.rational(x)


def exact_source_pi():
    # 310 original Machin-arctan terms; SI06 initially uses 50.
    # This is a mathematically identical source constant at MUCH
    # tighter certified precision, never a new pi assumption.
    a=arctan_bounds(F(1,5),terms=310)
    b=arctan_bounds(F(1,239),terms=310)
    lo,hi=16*a[0]-4*b[1],16*a[1]-4*b[0]
    assert OLD_PI[0]<=lo<hi<=OLD_PI[1]
    assert hi-lo<F(1,10**420)
    return I.rational_bounds(lo,hi)


PI=exact_source_pi()
TAYLOR=150
# Original cos and sin on [-pi,pi] from Taylor through degrees 300,301.
# Remainder <=(22/7)^302/302! and <=(22/7)^303/303!,
# since EVERY derivative sin/cos is bounded by one on R.
COS_REM=I.rational_bounds(
    -F(22,7)**(2*TAYLOR+2)/factorial(2*TAYLOR+2),
    F(22,7)**(2*TAYLOR+2)/factorial(2*TAYLOR+2))
SIN_REM=I.rational_bounds(
    -F(22,7)**(2*TAYLOR+3)/factorial(2*TAYLOR+3),
    F(22,7)**(2*TAYLOR+3)/factorial(2*TAYLOR+3))
assert COS_REM.abs_upper()<S//10**335 and SIN_REM.abs_upper()<S//10**335


def trig_pi(q):
    q=as_i(q)
    # Choose common exact period-2 reduction from interval midpoint.
    period=((q.lo+q.hi)//2+S)//(2*S)
    q=q-2*period
    assert -S<=q.lo<=q.hi<=S
    t=PI*q
    t2=t*t
    ct=I(S)
    st=t
    cterm=I(S)
    sterm=t
    for k in range(1,TAYLOR+1):
        cterm=-(cterm*t2)/((2*k-1)*(2*k))
        sterm=-(sterm*t2)/((2*k)*(2*k+1))
        ct=ct+cterm
        st=st+sterm
    return ct+COS_REM,st+SIN_REM


def cadd(x,y):
    return (x[0]+y[0],x[1]+y[1])


def cmul(x,y):
    return (x[0]*y[0]-x[1]*y[1],
            x[0]*y[1]+x[1]*y[0])


def tighter_source_log(n,terms):
    lo,hi=ln_bounds(n,terms=terms)
    old=OLD_SHIFTS[n]
    assert old[0]<=lo<hi<=old[1]
    return I.rational_bounds(lo,hi)


def source_sqrt(n):
    root=isqrt(n*S*S)
    return I(root,root+1)


def recurrence_211_native():
    centers,orders=authentic_source_replay()
    assert len(centers)==107 and sum(orders)==469
    moments=[I(0) for _ in range(211)]
    for cj,pj in zip(centers,orders):
        assert 0<cj*H<F(1,2)
        u,_=trig_pi(2*H*cj)
        t0=I(S)
        t1=u
        for m in range(1,211):
            moments[m]=moments[m]+pj*t1
            t0,t1=t1,2*u*t1-t0
    coefficients=[I(S)]
    for l in range(1,211):
        total=I(0)
        for m in range(1,l+1):
            total=total+moments[m]*coefficients[l-m]
        coefficients.append((-2*total)/l)
    assert coefficients[0].lo==coefficients[0].hi==S
    # Independent direct-product source-check for ALL FIRST 39
    # coefficients. Both intervals must overlap at each position.
    direct=[I(S)]+[I(0) for _ in range(38)]
    for cj,pj in zip(centers,orders):
        u,_=trig_pi(2*H*cj)
        for _ in range(pj):
            nextv=[I(0) for _ in range(39)]
            for k in range(39):
                nextv[k]=nextv[k]+direct[k]
                if k>=1:nextv[k]=nextv[k]-2*u*direct[k-1]
                if k>=2:nextv[k]=nextv[k]+direct[k-2]
            direct=nextv
    for k in range(39):
        assert max(direct[k].lo,coefficients[k].lo)<=min(
            direct[k].hi,coefficients[k].hi),("coefficient crosscheck",k)
    return coefficients


def original_bell_hat_at_c0():
    c0=F(37,64)
    q=2*R*c0
    _,ss=trig_pi(q)
    q_i=I.rational(q)
    product=I(S)
    for k in (1,2,3):
        product=product*(q_i*q_i-k*k)
    hat=(-F(45,2)*R*ss)/(PI*q_i*product)
    assert hat.lo>0,hat.scaled()
    mass=F(5,8)*R
    assert hat.hi < I.rational(mass).hi
    return hat


def original_edge_interval(n,coeff,hat):
    assert n in (5,7)
    c0=F(37,64)
    ln2=tighter_source_log(2,terms=400)
    if n==5:
        ln=tighter_source_log(5,terms=1100)
    else:
        ln=tighter_source_log(7,terms=1600)
    root=source_sqrt(n)
    weight=ln/root
    # Authentic EF23 original source edge phases.
    if n==5:
        phase=2*c0*(ln-B+ln2)
        K=210
        chirality=-1
        sign=1
    else:
        phase=2*c0*(ln-B+ln2-2*N*H)
        K=38
        chirality=1
        sign=-1
    phasecos,phasesin=trig_pi(phase)
    zcos,zsin=trig_pi(2*c0*H)
    z=(zcos,chirality*zsin)
    zpow=(I(S),I(0))
    total=(I(0),I(0))
    for l in range(K+1):
        total=cadd(total,(coeff[l]*zpow[0],coeff[l]*zpow[1]))
        zpow=cmul(zpow,z)
    real=cmul((phasecos,phasesin),total)[0]
    value=sign*weight*hat*real
    return value,real,weight


def run():
    m=json.loads((ROOT/"research/obligations.json").read_text())
    o={x["id"]:x for x in m["obligations"]}
    assert m["active_obligation"]=="W-EVEN-FORM"
    assert all(o[k]["status"]=="open" for k in (
        "W-EVEN-FORM","W-ODD-NEG","W-WHOLE-FORM"))
    assert "EF24" in o["W-EVEN-FORM"]["evidence"]
    coeff=recurrence_211_native()
    hat=original_bell_hat_at_c0()
    n2lo,n2hi,_=exact_original_n2_signed_mixed_lower()
    v5,raw5,w5=original_edge_interval(5,coeff,hat)
    v7,raw7,w7=original_edge_interval(7,coeff,hat)
    n2=I.rational_bounds(n2lo,n2hi)
    total=n2+v5+v7
    print("EF24 true native SI10 107-center 469-order SOURCE",
          "outward integer fixed-point digits",D,"Taylor order",TAYLOR,
          flush=True)
    print("EF24 original source pi interval",PI.scaled(),
          "width 10^-",D,"scaled integer units",PI.width(),flush=True)
    print("EF24 ORIGINAL FIR a38",coeff[38].scaled(),
          "a210",coeff[210].scaled(),flush=True)
    print("EF24 original even C5 bell transform at true c0:",
          hat.scaled(),flush=True)
    print("EF24 original signed n5 REAL edge",raw5.scaled(),
          "weight",w5.scaled(),"M5",v5.scaled(),
          "SIGN",v5.sign(),flush=True)
    print("EF24 original signed n7 REAL edge",raw7.scaled(),
          "weight",w7.scaled(),"M7",v7.scaled(),
          "SIGN",v7.sign(),flush=True)
    print("EF24 original n2 retained",n2.scaled(),
          "TOTAL arithmetic mixed ORIGINAL n2+n5+n7:",
          total.scaled(),"SIGN",total.sign(),flush=True)
    if not v5.excludes_zero() or not v7.excludes_zero():
        print("EF24 SCOPED PRECISION STOP: rigorous signed source"
              " interval includes zero, DO NOT claim numerical n5/n7"
              " sign. Increase original source precision ONLY after"
              " establishing a useful normalized Schur target.",flush=True)
    else:
        print("EF24 SCOPED VERIFIED ORIGINAL SIGNED ARITHMETIC:"
              " BOTH n5/n7 intervals exclude zero; full prime mixed"
              " interval calculated. This does NOT settle total M"
              " because the true ORIGINAL arch M is uncomputed.",
              flush=True)
    print("EF24 OPEN: actual original ARCH M, ARCH E upper,"
          " normalized |M|²/E, finite corrected 469D even Schur,"
          " odd/whole Weil, source analytic audit, RH.",flush=True)


if __name__=="__main__":
    run()
