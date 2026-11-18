#!/usr/bin/env python3
"""Exact rational replay of two actual original physical moment keys.
No floating-point or externally trusted exponential primitive.
"""
from fractions import Fraction as F
from math import floor, ceil, factorial
Q=10**40
N=48
ZERO=(F(0),F(0)); ONE=(F(1),F(0))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],a[1])
def rnd(a): return (F(floor(a[0]*Q),Q),F(ceil(a[1]*Q)+1,Q))
def exact(q):
    q=F(q)
    return (q,F(0)) if (q*Q).denominator==1 else rnd((q,F(0)))
def mul(a,b):
    m,r=a; n,s=b
    return rnd((m*n,abs(m)*s+abs(n)*r+r*s))
def div(a,d): return rnd((a[0]/d,a[1]/d))
def real(q): return (exact(q),ZERO)
def zadd(a,b): return (add(a[0],b[0]),add(a[1],b[1]))
def zneg(a): return (neg(a[0]),neg(a[1]))
def zmul(a,b): return (add(mul(a[0],b[0]),neg(mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0])))
def small(z):
    s=(ZERO,ZERO); t=(ONE,ZERO)
    for n in range(N):
        s=zadd(s,t); u=zmul(t,z); t=(div(u[0],n+1),div(u[1],n+1))
    return tuple((m,r+F(1,Q)) for m,r in s)
def atan(x):
    b=ZERO
    for n in range(N): b=add(b,exact((-1)**n*x**(2*n+1)/F(2*n+1)))
    return (b[0],b[1]+F(1,Q))
P=add(mul(exact(16),atan(F(1,5))),neg(mul(exact(4),atan(F(1,239)))))
def phase(f):
    u=f*F(11,10); u-=floor(u+F(1,2))
    a=small((ZERO,mul(P,exact(u/2))))
    b=zmul(a,a); return zmul(b,b)
def endpoint(h,f):
    a=small(real(h*F(11,20))); return zmul(zmul(a,a),phase(f))
def norm_upper(a): return sum(abs(m)+r for m,r in a)
CASES=[(F(0),F(37,32),[(27269882293080879354289005834393638,0),(0,7902701562810619635220000592690864)]),(F(1,2),F(37,64),[(-49886081731885688585833176103982357,14043467082935807939230485585476647)])]
def main():
    assert 2*Q<=factorial(N)
    assert all(Q<=p**(2*N+1)*(2*N+1) for p in (5,239))
    cases = CASES + [(F(-1,2),F(37,64),[(-49886081731885688585833176103982357,-14043467082935807939230485585476647)])]
    for h,f,rows in cases:
        z=(exact(h),mul(P,exact(2*f))); pos=endpoint(h,f); negend=endpoint(-h,-f)
        d=max(abs(h),6*abs(f)); R=F(1,10**33); prev=None
        for n,(x,y) in enumerate(rows):
            c=(exact(F(x,10**35)),exact(F(y,10**35)))
            b=zadd(zmul(real(F(11,10)**n),pos),zneg(zmul(real(F(-11,10)**n),negend)))
            r=zadd(b,zneg(zmul(z,c)))
            if n: r=zadd(r,zneg(zmul(real(n),prev)))
            fee=norm_upper(r)+(n*R if n else 0)
            assert fee<=d*R,(h,f,n,fee,d*R)
            print(f'key=({h},{f}) degree={n} residual upper={norm_upper(r)} payment PASS')
            prev=c
    osc = F(27269882293080879354289005834393638,10**35)
    mixed = F(14043467082935807939230485585476647,10**35)
    print("H[0,0] center:", F(11,10)-osc/2, "radius:", R/2)
    print("H[0,241] center:", mixed, "radius:", R)
if __name__=='__main__': main()
