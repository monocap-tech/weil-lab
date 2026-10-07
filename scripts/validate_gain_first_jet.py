#!/usr/bin/env python3
"""Rational rate controls, with log base four; not actual response data."""
from fractions import Fraction as F
import json

def main():
    cases=0; previous=None
    for n in range(2,25):
        s=F(1,4**n); L=F(n)
        gains=(s,F(1,8**n),s*L,s/L)
        ratios=tuple(g/(s*s) for g in gains)
        assert ratios==(4**n,2**n,n*4**n,F(4**n,n))
        for g in gains:
            M=L*g
            assert g<=10*M/L and M>0
            cases+=1
        if previous:
            old_g,old_ratios=previous
            assert all(a<b for a,b in zip(gains,old_g))
            assert all(a>b for a,b in zip(ratios,old_ratios))
        previous=gains,ratios
        if n%2==0:
            increment=F(1,8**(n//2))
            assert increment*increment==gains[1]
            assert increment/s==2**(n//2)
    print(json.dumps({'status':'rational_controls_pass','rate_cases':cases,
                      'log_base':4,'scope':'first-derivative/rate controls only; no actual arithmetic endpoint bound'},sort_keys=True))

if __name__=='__main__': main()
