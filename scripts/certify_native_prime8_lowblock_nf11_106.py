#!/usr/bin/env python3
"""NF11 exact interval native six-prime Legendre 8x8 block at 53/50.
Complete prime-shift contribution only, not the full signed Weil form.
High degrees require an optimized producer, not this symbolic algorithm.
"""
from fractions import Fraction as F
from math import comb, isqrt
import json

A=F(53,50); POWERS=(2,3,4,5,7,8)
BASE={n:2 if n in (4,8) else n for n in POWERS}
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[1],-x[0]
def mul(x,y):
    p=(x[0]*y[0],x[0]*y[1],x[1]*y[0],x[1]*y[1])
    return min(p),max(p)
def scale(x,y):return mul(x,(F(y),F(y)))
def log_interval(n,N=250):
    z=F(n-1,n+1);t=z;s=F(0)
    for k in range(N):
        s+=2*t/F(2*k+1);t*=z*z
    return s,s+2*t/F((2*N+1)*(1-z*z))
def sqrtint(n):
    d=10**120;k=isqrt(n*d*d);return F(k,d),F(k+1,d)
def div(x,y):return mul(x,(1/y[1],1/y[0]))
def poly(n):return [(-1)**(n-k)*comb(n,k)*comb(n+k,k) for k in range(n+1)]
def canon_pair(i,j,q):
    P,Q=poly(i),poly(j)
    powers=[(F(1),F(1))]
    for k in range(j):powers.append(mul(powers[-1],q))
    shift=[(F(0),F(0)) for _ in range(j+1)]
    for r in range(j+1):
        for k in range(r,j+1):
            shift[r]=add(shift[r],scale(powers[k-r],Q[k]*comb(k,r)))
    prod=[(F(0),F(0)) for _ in range(i+j+1)]
    for k,c in enumerate(P):
        for r,v in enumerate(shift):prod[k+r]=add(prod[k+r],scale(v,c))
    x=(1-q[1],1-q[0]);val=(F(0),F(0));p=(F(1),F(1))
    for t,v in enumerate(prod):
        p=mul(p,x);val=add(val,scale(mul(v,p),F(1,t+1)))
    return val
def compute(size=8):
    if size!=8:raise ValueError("NF11 audited configuration is 8x8; higher modes require optimized engine")
    logs={n:log_interval(n) for n in (2,3,5,7)}
    logs[4]=scale(logs[2],2);logs[8]=scale(logs[2],3)
    shift={n:div(logs[n],(2*A,2*A)) for n in POWERS}
    coeff={n:div(logs[BASE[n]],sqrtint(n)) for n in POWERS}
    Q=[[(F(0),F(0)) for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(i,size):
            if (i+j)%2:continue
            v=(F(0),F(0))
            for n in POWERS:
                val=add(canon_pair(i,j,shift[n]),canon_pair(j,i,shift[n]))
                v=add(v,mul(coeff[n],val))
            Q[i][j]=Q[j][i]=neg(mul(v,sqrtint((2*i+1)*(2*j+1))))
    return Q
def round_out(q):
    d=10**40
    return [str((q[0]*d).__floor__()),str((q[1]*d).__ceil__())]
def certificate():
    Q=compute()
    assert all(Q[i][j]==Q[j][i] for i in range(8) for j in range(8))
    assert all(Q[i][j]==(0,0) for i in range(8) for j in range(8) if (i+j)%2)
    assert max(v[1]-v[0] for row in Q for v in row)<F(1,10**58)
    assert F(-1988,1000)<Q[0][0][0] and Q[0][0][1]<F(-1987,1000)
    assert F(1453,1000)<Q[1][1][0] and Q[1][1][1]<F(1454,1000)
    return dict(aperture="53/50",physical_basis="sqrt((2i+1)/(2a)) P_i(x/a)",
       source="full original 2,3,4,5,7,8 prime-power shift part, both orientations",
       matrix_size=8,grid_denominator=str(10**40),
       lower_triangle=[[round_out(Q[i][j]) for j in range(i+1)] for i in range(8)],
       max_entry_interval_width=str(max(v[1]-v[0] for row in Q for v in row)),
       reflection_cross_zero=True,full_native_matrix=False,
       archimedean_included=False,poles_included=False,
       whole_aperture_positive=False,lean_certified=False)
if __name__=="__main__":print(json.dumps(certificate(),indent=2))
