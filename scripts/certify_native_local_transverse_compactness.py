#!/usr/bin/env python3
"""Exact rare-cluster controls; locations are not actual zeta zeros."""
from fractions import Fraction as F
from math import factorial
import json

terms=12
log2_lower=2*sum((F(1,3)**(2*m+1)/(2*m+1) for m in range(terms)),F(0))
log2_upper=log2_lower+2*F(1,3)**(2*terms+1)/((2*terms+1)*(1-F(1,9)))
assert F(2,3)<log2_lower<log2_upper<F(3,4)
n=8
exp1_upper=sum((F(1,factorial(k)) for k in range(n+1)),F(0))
exp1_upper+=F(1,factorial(n+1))/(1-F(1,n+2))
assert exp1_upper<3
B=F(3,8);cumulative=F(0)
for j in range(1,33):
    copies=2**j
    cumulative+=copies*B**2
    local_lower=copies*B**2/(F(3,4)*(copies+1))
    assert local_lower>=F(1,8)
    assert cumulative<=2*copies*B**2
print(json.dumps({"kind":"artificial cluster controls, not actual divisor data",
 "log2_bracket":"2/3 < log 2 < 3/4","exp1_upper_below_3":True,
 "cluster_blocks_checked":32,"normalized_local_mass_lower":"1/8",
 "full_actual_negative_compactness_certified":False,
 "critical_source_bound_certified":False},indent=2,sort_keys=True))
