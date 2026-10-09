#!/usr/bin/env python3
"""DNE11: exact rational analytic kernel/source-tail checks.

This verifies the Taylor recurrence, native polynomial singular-action
algebra, and the Cauchy bound with integers. It does NOT calculate the
full Weil source Gram, complete high Schur response, or any RH certificate.
"""
from fractions import Fraction as F
from math import factorial,comb
import json

def qcoeffs(N):
    q=[]
    for n in range(N+1):
        z=F(1,2**(n+1)*factorial(n))
        z-=sum((q[n-2*k]/factorial(2*k+1) for k in range(1,n//2+1)),F(0))
        q.append(z)
    return q

def D_derivative_monomial(n,x,a):
    return sum((F(factorial(n),factorial(n-k))*x**(n-k)*
                ((-1)**(k+1)*(x+a)**k-(a-x)**k)/
                (2*k*factorial(k)) for k in range(1,n+1)),F(0))

def D_direct_monomial(n,x,a):
    if n==0:return F(0)
    return sum((x**(n-1-j)*
                 ((2*x**(j+1)-(-a)**(j+1)-a**(j+1))/
                 (2*(j+1))) for j in range(n)),F(0))

def Rpoly_monomial(q,N,n,x,a):
    # Integral over y in [-a,a] of r_N(|x-y|) y**n
    return sum((q[k+1]*comb(n,j)*x**(n-j)*
                (((-1)**j*(x+a)**(k+j+1))+
                  (a-x)**(k+j+1))/(k+j+1)
                for k in range(N) for j in range(n+1)),F(0))

def run():
    checks=0
    def ck(v):
        nonlocal checks
        assert v
        checks+=1
    q=qcoeffs(18)
    ck(q[0]==F(1,2))
    ck(q[1]==F(1,4))
    ck(q[2]==F(-1,48))
    ck(q[3]==F(-1,32))
    for n in range(19):
        lhs=2*sum((q[n-2*k]/factorial(2*k+1)
                   for k in range(n//2+1)),F(0))
        ck(lhs==F(1,2**n*factorial(n)))
    a=F(53,50)
    for n in range(9):
        for x in (-a/2,F(0),a/3,F(3,5)):
            ck(-a<x<a)
            ck(D_derivative_monomial(n,x,a)==D_direct_monomial(n,x,a))
    ck(D_derivative_monomial(1,F(1,3),a)==F(1,3))
    ck(D_derivative_monomial(2,F(1,3),a)==
       (3*F(1,3)**2-a*a)/2)
    # Independent rational primitive for constant monomial p=1.
    N=8
    for x in (-a/2,F(0),a/3,F(3,5)):
        direct=Rpoly_monomial(q,N,0,x,a)
        primitive=sum((q[k+1]*((x+a)**(k+1)+(a-x)**(k+1))/(k+1)
                      for k in range(N)),F(0))
        ck(direct==primitive)
    # Uniform Cauchy analytic radius R=5/2 and max-distance 53/25:
    R=F(5,2);qmax=(2*a)/R
    ck(qmax==F(106,125))
    ck(R>2*a)
    ck(550*106**600*10**40<19*125**600)
    ck(550*106**600*10**41<19*125**600)
    ck(550*106**1000*10**68<19*125**1000)
    ck(2*a<F(3))
    # Uniform pole-exponential polynomialization: degree 64 remainder.
    epsilon_exp=F(2*2**65,3**65*factorial(65))
    ck(epsilon_exp<F(1,10**100))
    ck(4*a*(4*epsilon_exp+epsilon_exp**2)<F(3,10**99))
    # Both analytic errors combined for the complete signed native source.
    eps_arch=F(1,10**41)
    eps_pole=F(1,10**100)
    ck(2*a*eps_arch+4*a*(4*eps_pole+eps_pole**2)<F(3,10**41))
    # A0+2 CJ=-gamma_E-log(2pi), checked by formal coefficient arrays
    # basis order (gamma_E, pi, log2, logpi).
    a0=[F(-1),F(-1,2),F(-3),F(-1)]
    CJ=[F(0),F(1,4),F(1),F(0)]
    ck([a0[k]+2*CJ[k] for k in range(4)]==
       [F(-1),F(0),F(-1),F(-1)])
    assert checks==111, checks
    return dict(stage="DNE11 native source polynomial-log action",
                all_passed=True,exact_rational_assertions=checks,
                q0_to_q3=[str(z) for z in q[:4]],
                analytic_radius="5/2",
                cap="53/50",
                tail_N="600",
                error_bound="delta_600 < 10^-41 (exact rational)",
                full_source_operator_error="<3*10^-41 relative physical L2 (with pole Taylor64)",
                exact_prime_rows_retained=True,
                signed_pole_rows_approximated_degree64_with_paid_error=True,
                full_56_source_gram_interval_evaluated=False,
                original_null_excluded=False,RH_proved=False,
                lean_certified=False)

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
