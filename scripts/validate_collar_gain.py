#!/usr/bin/env python3
"""Rational constant/rate controls only; no actual residual certification."""
from fractions import Fraction as F
from math import factorial
import json

def main():
    lower=sum((F(1,factorial(j)) for j in range(5)),F(0))
    assert lower>F(8,3) and F(16)/lower<6
    assert 4+F(16)/lower<10
    budgets=[{'p':p,'C_p':8*(2*p)**p+2**(p+1)} for p in range(1,13)]
    rate_cases=0
    for power in range(1,13):
        for n in range(4*power,4*power+11):
            # s=4^-n, e=s^(1/2)=2^-n. For fixed power,
            # e*n^power has eventually geometric ratio <=2/3.
            ratio=F((n+1)**power,2*n**power)
            assert ratio<=F(2,3)
            s=F(1,4**n); e=F(1,2**n)
            assert e/(s*s)==8**n
            rate_cases+=1
    print(json.dumps({'status':'rational_controls_pass','e_lower':'65/24',
                      'one_log_constant':10,'finite_p_budgets':budgets,
                      'rough_superlog_rate_cases':rate_cases,
                      'scope':'constant and scalar rate controls; no actual null or Lean certification'},sort_keys=True))

if __name__=='__main__': main()
