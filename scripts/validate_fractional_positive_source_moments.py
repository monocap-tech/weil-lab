#!/usr/bin/env python3
"""Fractional source observation budgets and moment-threshold controls."""
from fractions import Fraction as F
from itertools import product
import json

def main():
    perturbations=moments=logs=errors=0
    for x,y in product((F(-3),F(-1),F(0),F(2),F(5)),repeat=2):
        assert (x+y)**2<=2*x*x+2*y*y
        assert x*x<=2*(x+y)**2+2*y*y
        perturbations+=1
    # t0=1/16; exact rational values of t0^(2-2s).
    for s,power in ((F(1,4),F(1,64)),(F(1,2),F(1,16)),(F(3,4),F(1,4))):
        denominator=2-2*s
        assert denominator>0 and power/denominator>0
        errors+=1
    assert 2-2*F(1)==0  # integral argument cannot be reused at s=1.
    for m,n in product((2,4,8),range(1,129)):
        base=sum(F(1,2)**(m*j) for j in range(1,n+1))
        subcritical=sum(F(1,2)**j for j in range(1,n+1))
        critical=sum(F(1) for j in range(1,n+1))
        assert base<F(1,2**m-1) and subcritical<1
        assert critical==n
        # theta_j^(2s)*p_j^2 with 2s=(m-1)/m:
        for j in (1,n):
            assert F(2**((m-1)*j))*F(1,2**(m*j))==F(1,2**j)
            assert F(2**(m*j))*F(1,2**(m*j))==1
        moments+=1
    for k,j in product((1,2,4),range(8,136)):
        if j>=2*k:
            ratio=F(j+1,j)**k/F(4)
            assert ratio<F(1,2)
            logs+=1
    print(json.dumps(dict(status="rational_controls_pass",
        perturbation_cases=perturbations,integrable_error_cases=errors,
        fractional_moment_cases=moments,logarithmic_tail_ratio_cases=logs,
        scope="algebra/rate controls; no actual critical or order-two source estimate"),
        sort_keys=True))
if __name__=="__main__": main()
