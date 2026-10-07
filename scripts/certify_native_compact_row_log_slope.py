#!/usr/bin/env python3
"""Rational physical-profile and geometric-scale controls; not actual null certification."""
from fractions import Fraction as F
import json

q=2**16
B=F(3,8)
u=F(9,128)
Pmax=F(9,128); Nmax=F(1,128); Nmin=F(3,2048)
assert 1/(1-u*u)<F(9,8)
assert u/(1-u*u)<F(1,8)
assert 64*F(9,8)+4*B*F(9,8)+B*B*F(9,8)/16<100
Delta_min=F(1,16)**2-Nmax**2
assert Delta_min==F(63,16384)>0
assert F(400,255)<2 and F(100,255)<1
assert 2*B**2*F(17,16)==F(153,512)<1

squared_budgets=fourier_margins=0
for j in range(1,65):
    H=q**j; sqrtH=2**(8*j); c=F(1,sqrtH); error=F(2,H**2)
    budget=F(1,H**2*sqrtH)
    assert 2*(Pmax+Nmax)*c*error+2*error**2<budget
    assert 2*Pmax*c*error+error**2<budget
    assert 2*Nmax*c*error+error**2<budget
    assert Nmin*c-error>0
    assert Delta_min/H-budget>0
    squared_budgets+=3
    assert c/32-error>c/64
    fourier_margins+=1

def exp_minus_bounds(x,n=63):
    total=term=F(1)
    for j in range(1,n+1):
        term*= -x/j
        total+=term
    return total,total+term*(-x)/(n+1)

abel_blocks=finite_geometric_agreements=0
for m in range(1,13):
    for r in (F(1),F(1,2),F(1,4)):
        tau=r/q**m
        low_lower=low_upper=F(0)
        for j in range(1,m+1):
            x=tau*q**j
            lo,hi=exp_minus_bounds(x)
            kl=(1-hi)/x; ku=(1-lo)/x
            assert 1-x/2<=kl<=ku<=1
            low_lower+=kl; low_upper+=ku
        deficit_bound=tau*sum((F(q**j,2) for j in range(1,m+1)),F(0))
        assert deficit_bound==tau*F(q*(q**m-1),2*(q-1))
        assert F(m)-low_lower<=deficit_bound<=F(q,2*(q-1))
        tail_upper=F(1,r*(q-1))
        assert low_upper+tail_upper-m<=F(q,q-1)
        abel_blocks+=1; finite_geometric_agreements+=1

error_series=F(1,2**24-1)
assert sum((F(1,2**(24*j)) for j in range(1,65)),F(0))<error_series
assert 2*Delta_min/16==F(63,131072)>0
assert 2*Nmin**2/16==F(9,33554432)>0

print(json.dumps({
    "status":"PASS",
    "scope":"rational profile/interference/Abel-scale controls; analytic limits in companion note",
    "squared_interference_budgets":squared_budgets,
    "physical_fourier_lower_margins":fourier_margins,
    "independent_abel_block_brackets":abel_blocks,
    "finite_geometric_agreements":finite_geometric_agreements,
    "all_occupied_bins_good_margin":"153/512 < 1",
    "signed_artificial_log_slope_lower":"63/131072",
    "negative_artificial_log_slope_lower":"9/33554432",
    "artificial_divisor_locations":True,
    "actual_arithmetic_or_lean_certificate":False,
},indent=2,sort_keys=True))
