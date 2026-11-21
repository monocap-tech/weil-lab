#!/usr/bin/env python3
"""CP031 independent exact rational outward crosscheck, NOT LEAN.

Reconstruct published original M=6,N=256 finite Euler–Maclaurin
expression independently of CP025. Exact fixed-point interval integer
operations, rational log/atan/Taylor bounds and rational B_{2k}
coefficients. Original source membership and source identity still need
separate Lean verification; this is NOT the pinned CP025 engine.

Float used ONLY to select an integer 2*pi phase reduction multiple;
the resulting trig domain is checked with integer inequalities.
"""
from fractions import Fraction as Q
from math import factorial, isqrt
import argparse
import json
from pathlib import Path

S=10**55
CELL=10**9

class I:
    __slots__=('l','h')
    def __init__(self,l,h=None):
        self.l=int(l);self.h=int(l if h is None else h)
        if self.l>self.h:raise ValueError('empty interval')
    @staticmethod
    def q(q):
        q=Q(q); return I(q.numerator*S//q.denominator,
                          -(-q.numerator*S//q.denominator))
    @staticmethod
    def cv(x):return x if isinstance(x,I) else I.q(x)
    def __add__(a,b):
        b=I.cv(b);return I(a.l+b.l,a.h+b.h)
    __radd__=__add__
    def __neg__(a):return I(-a.h,-a.l)
    def __sub__(a,b):return a+(-I.cv(b))
    def __rsub__(a,b):return I.cv(b)-a
    def __mul__(a,b):
        b=I.cv(b);p=(a.l*b.l,a.l*b.h,a.h*b.l,a.h*b.h)
        return I(min(p)//S,-(-max(p)//S))
    __rmul__=__mul__
    def inv(a):
        if a.l<=0<=a.h:raise ZeroDivisionError
        return I(S*S//a.h,-(-S*S//a.l))
    def __truediv__(a,b):return a*I.cv(b).inv()
    def __rtruediv__(a,b):return I.cv(b)/a
    def lo(a):return Q(a.l,S)
    def hi(a):return Q(a.h,S)

class C:
    __slots__=('r','i')
    def __init__(self,r=0,i=0):self.r=I.cv(r);self.i=I.cv(i)
    @staticmethod
    def cv(x):return x if isinstance(x,C) else C(x)
    def __add__(a,b):
        b=C.cv(b);return C(a.r+b.r,a.i+b.i)
    __radd__=__add__
    def __neg__(a):return C(-a.r,-a.i)
    def __sub__(a,b):return a+(-C.cv(b))
    def __rsub__(a,b):return C.cv(b)-a
    def __mul__(a,b):
        b=C.cv(b);return C(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r)
    __rmul__=__mul__
    def inv(a):
        d=a.r*a.r+a.i*a.i
        return C(a.r/d,-a.i/d)
    def __truediv__(a,b):return a*C.cv(b).inv()
    def __rtruediv__(a,b):return C.cv(b)/a

def atan_inv(n,steps=52):
    x=Q(1,n);v=Q(0)
    for k in range(steps):v+=(-1)**k*x**(2*k+1)/(2*k+1)
    e=x**(2*steps+1)/(2*steps+1)
    return I(I.q(v-e).l,I.q(v+e).h)

PI=16*atan_inv(5)-4*atan_inv(239)

def log2(steps=78):
    y=Q(1,3);v=I.q(0)
    for k in range(steps):v+=I.q(2*y**(2*k+1)/(2*k+1))
    e=2*y**(2*steps+1)/((2*steps+1)*(1-y*y))
    return I(v.l,v.h+I.q(e).h)

LOG2=log2()
LOGCACHE={}

def lnq(x,steps=78):
    x=Q(x)
    if x<=0:raise ValueError('log nonpositive')
    if x==1:return I.q(0)
    if x in LOGCACHE:return LOGCACHE[x]
    k=0;u=x
    while u>=2:u/=2;k+=1
    while u<1:u*=2;k-=1
    y=(u-1)/(u+1);v=I.q(0)
    for j in range(steps):v+=I.q(2*y**(2*j+1)/(2*j+1))
    e=2*y**(2*steps+1)/((2*steps+1)*(1-y*y))
    v=I(v.l,v.h+I.q(e).h)+k*LOG2
    LOGCACHE[x]=v
    return v

def lni(v):
    v=I.cv(v)
    if v.l<=0:raise ValueError('log nonpositive interval')
    low,high=lnq(Q(v.l,S)),lnq(Q(v.h,S))
    return I(low.l,high.h)

def invsqrt(n):
    p=isqrt(S*S//n)
    return I(p,p if p*p*n==S*S else p+1)

def sincos(x,m=42):
    x=I.cv(x)
    if max(abs(x.l),abs(x.h))>4*S:raise ValueError('trig domain not reduced')
    xx=x*x;si=I.q(0);co=I.q(0)
    ts=x;tc=I.q(1)
    for j in range(m):
        si+=ts;co+=tc
        ts=-(ts*xx)/((2*j+2)*(2*j+3))
        tc=-(tc*xx)/((2*j+1)*(2*j+2))
    se=I.q(Q(4**(2*m+1),factorial(2*m+1)))
    ce=I.q(Q(4**(2*m),factorial(2*m)))
    return si+I(-se.h,se.h),co+I(-ce.h,ce.h)

def trig(x):
    x=I.cv(x)
    k=round(float(x.lo()/(2*PI.lo())))
    return sincos(x-2*k*PI)

def atan_small(x,m=20):
    x=Q(x)
    if not 0<=x<=Q(1,100):raise ValueError('atan domain')
    v=Q(0)
    for j in range(m):v+=(-1)**j*x**(2*j+1)/(2*j+1)
    e=x**(2*m+1)/(2*m+1)
    return I(I.q(v-e).l,I.q(v+e).h)

LOGPI=lni(PI)
LOG256=lnq(256)
BERNOULLI=[Q(1,6),-Q(1,30),Q(1,42),-Q(1,30),Q(5,66),-Q(691,2730)]

def original_A(t):
    t=Q(t);s=C(Q(1,2),t);a=C()
    for n in range(1,256):
        ln=lnq(n);si,co=trig(t*ln)
        a+=C(co*invsqrt(n),-si*invsqrt(n))
    si,co=trig(t*LOG256)
    base=C(co*Q(1,16),-si*Q(1,16))
    a+=base*256/(s-1)+base/2
    p=C(1)
    for j in range(11):
        p=p*(s+j)
        if j%2==0:
            k=(j+2)//2
            q=BERNOULLI[k-1]/factorial(2*k)/256**(2*k-1)
            a+=p*base*q
    return a

def source_theta_stirling2(t):
    t=Q(t);w=C(Q(1,4),t/2)
    lnabs=lnq(t/2)+lni(1+I.q(Q(1,4*t*t)))/2
    inv=w.inv()
    return (I.q(t/2)*(lnabs-LOGPI-I.q(1))-PI/8
            +atan_small(Q(1,2*t))/4+inv.i/12-(w*w*w).inv().i/360)

def outward(v):return [v.l*CELL//S,-(-v.h*CELL//S)]
def replay():
    rows={}
    for side,t in [('left',Q(15005352,100000)),('right',Q(15005353,100000))]:
        a=original_A(t); theta=source_theta_stirling2(t)
        si,co=trig(theta);finite=(C(co,si)*a).r
        re,im,rot=map(outward,[a.r,a.i,finite])
        for pair in [re,im]:
            if max(map(abs,pair))>CELL//10000:
                raise ValueError(side+' genuine component cap fails')
        if side=='left' and not rot[1] <= -200:
            raise ValueError('left rotated finite cap fails')
        if side=='right' and not rot[0] >= 1000:
            raise ValueError('right rotated finite cap fails')
        rows[side]={'t':str(t),'real_pair':re,
                    'imag_pair':im,'rotated_pair':rot}
        print(side,re,im,rot,'EXTERNAL NOT LEAN')
    return rows

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--receipt',type=Path)
    args=p.parse_args()
    rows=replay()
    data={'status':'CP031_INDEPENDENT_RECONSTRUCTED_1e9_SIX_SCALAR_CELLS_NOT_LEAN',
          'scale':CELL, 'fixed_scale':S, 'rows':rows,
          'pinned_CP025_engine_executed':False,
          'formal_original_source_membership_verified':False,
          'six_original_scalar_Lean_proofs':False,
          'CP027_Borwein_Lean_accepted':False,
          'unconditional_original_zeta_narrow_root_Lean_accepted':False,
          'original_rank53_Lean_accepted':False,
          'global_signed_Weil_positivity_or_RH':False}
    if args.receipt:
        args.receipt.write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
    print(data['status'])

if __name__=='__main__':main()
