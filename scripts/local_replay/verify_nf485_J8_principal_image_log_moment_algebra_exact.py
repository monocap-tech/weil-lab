#!/usr/bin/env python3
"""NF485: pure-exact rational controls for the ORIGINAL J8 terminal
principal x same-source finite-image analytic log moment identity.

These are ALGEBRAIC controls, not substitutes for original NF407 source
data. Original 18k native source and full physical mixed D8 remain OPEN.
"""
from fractions import Fraction as F
from math import factorial
DELTA=F(1,500)

def kernels(lam,order):
    """Finite formal exponential J,K moments, log(B/d)=h+log(delta/d)."""
    a=-lam*DELTA
    J=sum((a**k/F(factorial(k)*(k+1)) for k in range(order)),F(0))*DELTA
    K=sum((a**k/F(factorial(k)*(k+1)**2) for k in range(order)),F(0))*DELTA
    return J,K

def direct_polynomial(coeff_left,coeff_right,v,c,order):
    """Integrate 4 p I, treating h=log(B/delta) as a FORMAL variable."""
    ans0=F(0)
    ansh=F(0)
    for k in range(order):
        coef=sum((d*(-(2*m+F(1,2)))**k-b*((2*m+F(1,2)))**k
                  for m,(d,b) in enumerate(zip(coeff_left,coeff_right))),F(0))
        coef/=2*factorial(k)
        moment=DELTA**(k+1)/F(k+1)
        ans0+=4*v*coef*moment*(c+F(1,2*(k+1)))
        ansh+=2*v*coef*moment
    return ans0,ansh

def exponential_kernels(coeff_left,coeff_right,v,c,order):
    """Independent grouped analytic J,K formula, exact over Q."""
    ans0=F(0)
    ansh=F(0)
    for m,(d,b) in enumerate(zip(coeff_left,coeff_right)):
        lam=2*m+F(1,2)
        jp,kp=kernels(lam,order)
        jn,kn=kernels(-lam,order)
        j=d*jp-b*jn
        k=d*kp-b*kn
        ans0+=2*v*(c*j+k/F(2))
        ansh+=v*j
    return ans0,ansh

def main():
    tests=[
      ([F(1)],[F(0)]),
      ([F(-7,13)],[F(3,4)]),
      ([F(0),F(1)],[F(-1),F(0)]),
      ([F(3,7),F(-5,11),F(7,13)],[F(-2,5),F(1,19),F(0)]),
      ([F(0)]*4,[F(0)]*4),
      ([F((-1)**m,2*m+3) for m in range(7)],[F((-1)**(m+1),3*m+7) for m in range(7)]),
      ([F(1),F(-1),F(1),F(-1)],[F(-1),F(1),F(-1),F(1)]),
      ([F(-1,10**20)],[F(1,10**25)]),
      ([F(10**25),-F(10**25)],[F(7),F(-11)]),
      ([F(0),F(0),F(0),F(1)],[F(0),F(0),F(0),F(-1)]),
      ([F(5,9),F(0),F(-2,17),F(0),F(11,19)],[F(0),F(1,7),F(0),F(-9,23),F(0)]),
      ([F((-1)**m*(m+1),2*m+1) for m in range(9)],
       [F((-1)**m*(m+2),3*m+4) for m in range(9)]),
    ]
    count=0
    for left,right in tests:
        assert len(left)==len(right)
        for order in (1,2,4,9,16):
            for v,c in ((F(-17,31),F(11,4)),(F(5,37),F(0))):
                direct=direct_polynomial(left,right,v,c,order)
                grouped=exponential_kernels(left,right,v,c,order)
                assert direct==grouped,(left,right,order,direct,grouped)
                count+=1
    print("NF485 pure-exact rational log-moment identity controls PASS:",count)
    print("No authentic NF407 physical J8 signed D8 numerical value is claimed.")
if __name__=="__main__":main()
