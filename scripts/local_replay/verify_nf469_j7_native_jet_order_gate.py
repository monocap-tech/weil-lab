#!/usr/bin/env python3
"""Exact rational Cauchy tail gate, not source-native numerical integration."""
from fractions import Fraction as F
import json
B=F(11,10);left=F(26,25);right=F(53,50)
dmax=B-left;dmin=B-right;t0=F(1,8);R=F(1,5)
assert dmin==F(1,25) and dmax==F(3,50)
assert 2*dmax==F(3,25)<t0
smax=dmax+t0/2
assert smax==F(49,400)
ratio=smax/R
assert ratio==F(49,80)
# Compare exact integer powers without floating point or arbitrary precision transcendental routines.
# E_N = 10^800 * (49/80)^N / (1-49/80).
def tail_lt(N, power):  # E_N < 10^(-power)
    return 10**(800+power)*49**N*80 < 31*80**N
assert not tail_lt(1150,0)
assert tail_lt(4000,40)
print(json.dumps({"pass":"NF469","panel":["26/25","53/50"],"t0":"1/8","R":"1/5","M_U":"10^800",
"max_local_displacement":"49/400","Cauchy_ratio":"49/80",
"1150_jet_bound_below_one":False,"4000_jet_bound_below_1e-40":True,
"source_native_J7_integral_computed":False,"standing":"source-independent jet tail gate only"},indent=2))
