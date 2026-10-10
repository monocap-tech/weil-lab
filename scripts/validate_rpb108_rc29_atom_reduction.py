"""Exact physical overlaps and RC29 budgets; transcendental matrix not evaluated."""
from fractions import Fraction as F
from math import comb, factorial
import json

B=F(11,10)
R=2*B

def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return c

def legendre(n):
    a,b=[F(1)],[F(0),F(1)]
    if n==0: return a
    for j in range(1,n):
        c=add([F(0)]+[F(2*j+1,j+1)*x for x in b],
              [-F(j,j+1)*x for x in a])
        a,b=b,c
    return b

def overlap_one(i,j):
    p,q=legendre(i),legendre(j)
    out=[F(0)]*(i+j+2)
    for a,pa in enumerate(p):
        for d,qd in enumerate(q):
            for b in range(d+1):
                # x^a (x+r)^d / B^(a+d), then integrate x.
                coeff=pa*qd*comb(d,b)/B**(a+d)
                m=a+d-b+1
                for k in range(m+1):
                    out[b+k]+=coeff*comb(m,k)*B**(m-k)*(-1)**k/m
                out[b]-=coeff*(-B)**m/m
    return out

def overlap(i,j): return add(overlap_one(i,j),overlap_one(j,i))
def value(p,x): return sum((c*x**j for j,c in enumerate(p)),F(0))
def integral(p): return sum((c*R**(j+1)/F(j+1) for j,c in enumerate(p)),F(0))

def controls():
    checks=0
    def check(v):
        nonlocal checks
        assert v, checks+1
        checks+=1
    check(sum((F(7,3)**j/factorial(j) for j in range(13)),F(0))>10)
    delta,T,N=F(1,100000),F(100000),1000
    check(T/delta==10**10)
    # log(T/delta)<70/3<24, h<24/1000.
    h=F(24,N)
    err=h*h/4
    upper=3*delta+4*B/T+err
    check(err==F(9,62500))
    check(upper==F(109,500000))
    check(upper<F(1,4000))
    check(210000//N==210)
    rows=[]
    for i in range(8):
        for j in range(i,8):
            p=overlap(i,j)
            check(p==overlap(j,i))
            check(value(p,R)==0)
            check(value(p,0)==(4*B/F(2*i+1) if i==j else 0))
            check(integral(p)==(R*R if i==j==0 else 0))
            if (i+j)%2: check(all(x==0 for x in p))
            rows.append(dict(i=i,j=j,coefficients=[str(x) for x in p]))
    check(overlap(0,0)==[4*B,F(-2)])
    # Rational recurrence control for denominator t^2+c^2*r^2:
    # r^p=(r^(p-2)/c^2)*(t^2+c^2*r^2)-t^2*r^(p-2)/c^2.
    for p in range(2,17):
        for r in [F(0),F(1,3),R]:
            t,c=F(7,5),F(22,7)
            check(r**p/(t*t+c*c*r*r)==r**(p-2)/(c*c)-
                  t*t*r**(p-2)/(c*c*(t*t+c*c*r*r)))
    return dict(milestone='RC29',status='PASS',exact_rational_checks=checks,
                atoms=N,quadrature_error_upper=str(err),
                whole_error_upper=str(upper),overlap_rows=rows,
                complete_metric_evaluated=False,Riesz_solve=False,
                aperture_extended=False)

if __name__=='__main__': print(json.dumps(controls(),indent=2))
