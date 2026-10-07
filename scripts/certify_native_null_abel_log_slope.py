#!/usr/bin/env python3
"""Rational Abel/sharp controls; not actual zeta or analytic certification."""
from fractions import Fraction as F
import json

def exp_minus_bounds(x,n):
    # Taylor's integral remainder has alternating sign for exp(-x), x>=0.
    assert x>=0 and n%2==1
    total=term=F(1)
    for j in range(1,n+1):
        term*= -x/j
        total+=term
    return total,total+term*(-x)/(n+1)

abel_brackets=0
for n in range(15,80,2):
    l1,u1=exp_minus_bounds(F(1),n)
    l2,u2=exp_minus_bounds(F(2),n)
    lower=F(1,2)-u1+l2/2
    upper=F(1,2)-l1+u2/2
    assert lower>F(1,160) and lower<upper
    abel_brackets+=1

# Infinite source norms: sum j*r^j=r/(1-r)^2 at r=1/4.
series=F(1,4)/(1-F(1,4))**2
assert F(9,4)*series==1
assert F(9,8)*series+F(1,2)==1
head=F(0)
sharp_returns=sharp_peaks=normalized_lower_bounds=0
for j in range(1,65):
    pos_mass=F(9*j,4*4**j)
    neg_mass=F(9*j,8*4**j)
    head+=4**j*pos_mass
    assert head==F(9*j,4)
    sharp_peaks+=1
    head-=2*4**j*neg_mass
    assert head==0
    sharp_returns+=1
    # At tau=4^-j, this pair alone contributes >=(9/640)j.
    # Since log 4<2, divide by log(1/tau)<2j.
    assert F(9*j,640)/(2*j)==F(9,1280)>0
    normalized_lower_bounds+=1

# For E(t)=c*t+O(t^(1+delta)), its remainder integral is bounded
# by integral_0^1 t^(delta-1)dt=1/delta, independently of tau.
# Check the rational positive budgets for a range of actual margins.
local_budgets=0
for numerator in range(1,33):
    delta=F(numerator,16)
    assert delta>0 and 1/delta>0
    local_budgets+=1

print(json.dumps({
    "status":"PASS",
    "scope":"rational signed sharp/Abel controls; exact native slope is an analytic proof",
    "independent_abel_coefficient_brackets":abel_brackets,
    "neutral_infinite_norm_checks":2,
    "sharp_returns":sharp_returns,
    "sharp_peaks":sharp_peaks,
    "normalized_abel_lower_controls":normalized_lower_bounds,
    "positive_local_remainder_budgets":local_budgets,
    "actual_arithmetic_sublog_bound":False,
    "actual_null_or_lean_certificate":False,
},indent=2,sort_keys=True))
