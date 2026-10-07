#!/usr/bin/env python3
"""Critical regularity/cusp exponent controls; no actual null assertion."""
from fractions import Fraction as F
import json

def main():
    derivative=fractions=budgets=0
    alpha=F(1,4)
    diff_order=1+2*alpha
    for beta in (F(1,2),F(9,16),F(5,8),F(11,16)):
        assert diff_order-2*beta>0
        assert 2*beta>=1
        budgets+=1
    assert diff_order-2*F(3,4)==0
    assert 2*alpha-1<0
    for n in range(1,129):
        # epsilon=2^(-4n), wholly inside chi=1.
        energy=F(2**(2*n)-2,8)
        assert energy>0
        next_energy=F(2**(2*(n+1))-2,8)
        assert next_energy>4*energy
        derivative+=1
        # t=2^(-4n), beta=5/8: t^(3/2-2beta)=2^(-n).
        assert F(1,2**(6*n))/F(1,2**(5*n))==F(1,2**n)
        assert sum(F(1,2**j) for j in range(1,n+1))<1
        fractions+=1
    # The critical negative derivative weight cannot contain a delta:
    # on [2^n,2^(n+1)] a lower log/(1+xi) budget >= n/4,
    # using log(2)>1/2, interval length 2^n, denominator <=2^(n+2).
    delta=sum(F(n,4) for n in range(1,129))
    assert delta==F(128*129,8)
    print(json.dumps(dict(status="rational_controls_pass",
        exponent_budgets=budgets,truncated_derivative_cases=derivative,
        summable_fractional_cases=fractions,delta_divergence_cases=128,
        scope="cusp exponent and growth controls; no actual critical promotion or F4"),
        sort_keys=True))
if __name__=="__main__": main()
