#!/usr/bin/env python3
"""NF11 independent analytic prime-only degree 0/1 cross-check of low8.

Proves consistency of the separately integrated 8x8 interval block
with closed-form translated-overlap formulas. This is NOT verification
of archimedean, poles, full native112, or original whole-domain sign.
"""
from fractions import Fraction as F
from math import isqrt
import json
from certify_native_prime8_lowblock_nf11_106 import compute,A,POWERS,BASE

def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):
    p=[a*b for a in x for b in y]
    return min(p),max(p)
def logn(n,N=260):
    z=F(n-1,n+1);p=z;s=F(0)
    for k in range(N):
        s+=2*p/F(2*k+1);p*=z*z
    return s,s+2*p/F((2*N+1)*(1-z*z))
def div(x,y):return mul(x,(1/y[1],1/y[0]))
def sqrtint(n):
    g=10**120;v=isqrt(n*g*g)
    return F(v,g),F(v+1,g)
def overlap(x,y):return not (x[1]<y[0] or y[1]<x[0])

Q=compute()
low=(F(0),F(0));odd=(F(0),F(0))
logs={n:logn(n) for n in (2,3,5,7)}
for n in POWERS:
    lg=logs[BASE[n]]
    sq=sqrtint(n)
    c=div(lg,sq)
    # The independent closed forms are exact physical-normalized P0/P1.
    shift=div(logn(n),(2*A,2*A))
    q=shift
    even=(1-q[1],1-q[0])
    q2=mul(q,q);q3=mul(q2,q)
    odd_kernel=add(add((F(1),F(1)),mul(q,(F(-3),F(-3)))),mul(q3,(F(2),F(2))))
    low=add(low,mul(c,even))
    odd=add(odd,mul(c,odd_kernel))
even_expected=(-2*low[1],-2*low[0])
odd_expected=(-2*odd[1],-2*odd[0])
assert overlap(Q[0][0],even_expected)
assert overlap(Q[1][1],odd_expected)
assert max(x[1]-x[0] for row in Q for x in row)<F(1,10**58)
assert all(Q[i][j]==Q[j][i] for i in range(8) for j in range(8))
assert all(Q[i][j]==(0,0) for i in range(8) for j in range(8) if (i+j)%2)
assert Q[0][2][1]<0 and Q[1][3][1]<0 and Q[2][2][0]>0
print(json.dumps(dict(status='PASS',aperture='53/50',matrix='8x8 prime-only',
    independent_closed_form_degree0_overlap=True,
    independent_closed_form_degree1_overlap=True,
    parity_exact=True,symmetry_exact=True,
    full_native112=False,whole_aperture_positive=False),indent=2))
