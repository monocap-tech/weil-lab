#!/usr/bin/env python3
"""NF22: exact rational Cauchy/Taylor certificate for the original
archimedean physical source on the first two Legendre modes at a=53/50.
The analytic logarithms are preserved, not approximated by bounded
polynomials at support endpoints. No complete source-square or P2 claim.
"""
from fractions import Fraction as F
from math import factorial
import json

A=F(53,50)
DEGREE=320
R=F(5,2)

def kernel_coefficients(N=DEGREE):
    # h(z)=z*exp(z/2)/(2*sinh z) and
    # (2*sinh(z)/z)*h(z)=exp(z/2).
    h=[]
    for n in range(N+1):
        v=F(1,2**n*factorial(n))
        for k in range(1,n//2+1):
            v-=F(2,factorial(2*k+1))*h[n-2*k]
        h.append(v/2)
    return h

def certify():
    coeff=kernel_coefficients()
    assert coeff[:8]==[
        F(1,2),F(1,4),F(-1,48),F(-1,32),
        F(7,11520),F(5,1536),F(-31,1935360),F(-61,184320)]
    ratio=2*A/R
    assert ratio==F(106,125) and ratio<1
    # On |z|=R=5/2, |sinh z|>1/2:
    # if |Re z|>=1/2, sinh|Re z|>1/2;
    # otherwise sqrt(6)<|Im z|<=5/2 and |sin(Im z)|>1/2.
    # Also |exp(z/2)|<=exp(5/4)<4, so |h(z)|<10.
    # Cauchy coefficients |h_k|<=10/R^k.
    remainder=F(4)*ratio**DEGREE/(1-ratio)
    assert remainder<F(1,10**20)
    # r(z)=j(z)-1/(2z), where j(z)=exp(-z/2)/(1-exp(-2z)).
    # r_N(z)=sum_{k=1}^N h_k z^(k-1).
    # g_N(t)=gamma0-sum h_k t^k/k,
    # F_N(t)=t/2+sum h_k t^(k+1)/(k+1);
    # gamma0=log 2+pi/4 and F(t)=int_0^t s*j(s)ds.
    # The true source is:
    # arch(e0)=U(x)/sqrt(2a),
    # arch(e1)=sqrt(3/(2a))/a*[xU(x)+F(a+x)-F(a-x)].
    # U(x)=-EulerGamma-log(2pi)-log(a^2-x^2)/2
    #      -sum_{k>=1}h_k[(a-x)^k+(a+x)^k]/k.
    # The rational polynomial U_N and F_N are uniform:
    # ||arch(e0)-arch_N(e0)||_L2 <=4*a*remainder,
    # ||arch(e1)-arch_N(e1)||_L2 <=8*a*sqrt(3)*remainder
    #                                  <14*a*remainder.
    even_error=4*A*remainder
    odd_error=14*A*remainder
    assert even_error<F(1,10**19) and odd_error<F(1,10**19)
    return dict(milestone="NF22",aperture=str(A),N=DEGREE,
        analytic_Cauchy_radius=str(R),relative_radius=str(ratio),
        first_h_coefficients=[str(v) for v in coeff[:8]],
        rigorous_regular_kernel_sup_error_less_than="1/10^20",
        exact_regular_kernel_error=str(remainder),
        rigorous_arch_e0_source_L2_error_less_than="1/10^19",
        rigorous_arch_e1_source_L2_error_less_than="1/10^19",
        arch_endpoint_log_retained_exactly=True,
        complete_original_source_square=False,full_P2_certified=False)

if __name__=="__main__":print(json.dumps(certify(),indent=2))
