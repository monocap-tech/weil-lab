#!/usr/bin/env python3
"""Exact localization algebra and budget controls, not a global arithmetic bound."""
from fractions import Fraction as F
from math import factorial
import json

def norm2(z): return z.real*z.real+z.imag*z.imag

def main():
    # Rational complex arithmetic represented by Python complex integer inputs,
    # but use explicit real/imag pairs to avoid floating point.
    vals=((F(1),F(0)),(F(-1),F(0)),(F(0),F(1)),(F(1),F(1)),(F(2),F(-1)))
    corrs=((F(0),F(1)),(F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(1),F(0)))
    pairs=poles=0
    for c,s in corrs:
        assert c*c+s*s==1
        for u in vals:
            for v in vals:
                uv=u[0]*v[0]+u[1]*v[1]
                original=sum((u[i]-v[i])**2 for i in range(2))
                localized=sum((u[i]-c*v[i])**2+(s*v[i])**2 for i in range(2))
                assert localized-original==2*(1-c)*uv
                assert -2*c*uv-(-2*uv)==2*(1-c)*uv
                assert 2*c*uv-2*uv==-2*(1-c)*uv
                pairs+=1
    for A in (F(1),F(2),F(3)):
        for selfcost in (F(0),A,2*A):
            for L in range(2,10):
                # cosh L>=1+L^2/2; separated opposite bumps.
                floor=2*A*(1+F(L*L,2))-selfcost
                assert floor>=A*L*L>0
                poles+=1
    # e<3 from the series and a geometric majorant on the tail after k=10.
    e_upper=sum(F(1,factorial(k)) for k in range(11))+F(1,factorial(11))*F(12,11)
    assert e_upper<3
    margin=F(3,10**29)
    assert 4/e_upper>F(4,3)>margin
    print(json.dumps(dict(status="rational_controls_pass",
        correlation_pair_cases=pairs, separated_pole_budget_cases=poles,
        archimedean_tail_budget_rejection=True,
        scope="algebra/budget controls only; combined defect bound unproved"),
        sort_keys=True))
if __name__=="__main__":
    main()
