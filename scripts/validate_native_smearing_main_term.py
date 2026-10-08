"""Exact exponential-moment algebra, not PNT or actual spectral certification."""
from fractions import Fraction as F
from math import factorial
import json

def run():
    checks=0
    def check(x):
        nonlocal checks
        assert x
        checks+=1
    for delta in [F(1,64),F(1,128),F(1,1024)]:
        # alpha=sum delta^(2j)/(2^(2j)*(2j+1)!).
        terms=[delta**(2*j)/F(2**(2*j)*factorial(2*j+1)) for j in range(8)]
        ratio=delta*delta/24
        lower=1+delta*delta/24
        upper=1+ratio/(1-ratio)
        check(1<lower<=sum(terms)<upper)
        for j in range(7):
            check(terms[j+1]<=ratio*terms[j])
        for J in [F(1),F(3,7)]:
            check(2*(1-lower)*J<0)
            alpha=sum(terms)
            unmatched=2*(1-alpha)*J
            pole_adjustment=2*(alpha-1)*J
            check(unmatched+pole_adjustment==0)
            prime_error,pole_budget=F(1,100),F(11)
            check(prime_error+(alpha-1)*pole_budget>prime_error)
    return {'passed':True,'finite_checks':checks,
        'scope':'finite moment/sign/error algebra only; PNT limit is analytic'}

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
