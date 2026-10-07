#!/usr/bin/env python3
"""Rational controls of cutoff and signed relative-flux budgets, not Fourier limits."""
from fractions import Fraction as F
from itertools import product
import json

def main():
    budgets=signs=limits=0
    # low mass defect/t^2=a; high mass defect/t^2=b; high weight >=L.
    for a,b,L,W,B,M,P in product((F(0),F(1),F(3)),(F(1),F(4)),
        (F(2),F(5)),(F(1),F(2)),(F(0),F(3)),(F(0),F(2)),(F(-4),F(0),F(4))):
        high_weight=L*W
        H=a+high_weight*b
        mass=a+b
        assert mass<=a+H/L
        bound=(B+M)*(1/L+a/H)+abs(P)/(4*H)
        # Every extreme sign of bounded multiplier, mass and pole correction.
        for sb,sm,sp in product((-1,1),repeat=3):
            bounded=sb*B*mass
            shifted=sm*M*mass
            pole=sp*abs(P)/4
            flux=-H-bounded+shifted+pole
            remainder=abs(flux/(-H)-1)
            assert remainder<=bound
            signs+=1
        budgets+=1
    # A rational budget sequence with increasing cutoff weight and H.
    # It verifies the remainder budget tends small, not an actual cosine integral.
    previous=None
    for n in range(2,130):
        L=F(n); H=F(n**3+1); low=F(1); B=F(3); M=F(2); pole=F(4)
        mass=low+F(n*n)
        assert mass<=low+H/L
        bound=(B+M)*(1/L+low/H)+pole/(4*H)
        assert mass/H<=1/L+low/H
        if previous is not None: assert bound<previous
        previous=bound
        if n>=64: assert bound<F(1,10)
        # A positive bounded correction cannot neutralize the leading term.
        if n>=16:
            assert B*mass/H+pole/(4*H)<F(1,2)
        limits+=1
    print(json.dumps(dict(status="rational_controls_pass",cutoff_budgets=budgets,
        signed_remainders=signs,vanishing_budget_cases=limits,
        scope="inequality controls only; analytic limits and actual endpoint bound unproved"),
        sort_keys=True))

if __name__=="__main__": main()
