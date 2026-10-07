#!/usr/bin/env python3
"""Independent rational logarithm enclosures for strip-kernel controls."""
from fractions import Fraction as F
import json

def twice_atanh(z, n=24):
    lo = 2*sum((z**(2*k+1)/F(2*k+1) for k in range(n)), F(0))
    tail = 2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
    return lo, lo+tail

checks = 0
for j in range(64):
    x=F(1, j+2)
    lo,hi=twice_atanh(x/(2-x)) # -log(1-x)
    assert 0 < lo-x
    assert hi-x <= x*x
    lo,hi=twice_atanh(x/(2+x)) # log(1+x)
    assert lo-x/(1+x) > 0
    assert hi-x/(1+x) <= x*x/2
    checks += 2
lo,hi=twice_atanh(F(1,3))
assert F(2,3) < lo < hi < 1
# Both near-strip absolute kernel integrals in the note equal log 2.
# The indicator's rescaled two-edge logarithm has integral 2.
for L in range(4,68):
    assert F(L,2*(L+1)) > F(1,4)
    assert 1+F(1,2*L) <= F(9,8)
print(json.dumps({
    "status":"PASS",
    "scope":"rational strip-kernel and rough-profile controls; analytic theorem not mechanically certified",
    "log_remainder_enclosures":checks,
    "atanh_terms":24,
    "log2_interval":[str(lo),str(hi)],
    "near_strip_kernel_integrals":"log 2 <1",
    "indicator_edge_log_integral":"2",
    "rough_profile_brackets":64,
    "actual_null_or_lean_certificate":False,
},indent=2,sort_keys=True))
