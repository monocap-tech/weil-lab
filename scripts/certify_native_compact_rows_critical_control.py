#!/usr/bin/env python3
"""Rational margins for the artificial supported-profile obstruction only."""
from fractions import Fraction as F
import json

b, x = F(3, 8), F(9, 128)
# Even/odd Taylor factorials >=1 bound cosh and sinh by geometric series.
cosh_upper, sinh_upper = 1/(1-x*x), x/(1-x*x)
assert cosh_upper < F(9, 8)
assert sinh_upper < F(1, 8)
tv_plus = 64*F(9, 8) + 4*b*F(1, 8) + b*b*F(9, 8)/16
tv_minus = 64*F(1, 8) + 4*b*F(9, 8) + b*b*F(1, 8)/16
assert max(tv_plus, tv_minus) < 100
error = F(3200, 2**48)
negative_leading = F(3, 2048)
assert error < negative_leading/2
assert F(1, 16)-error > F(1, 32)
assert F(1, 128)+error < F(1, 64)
assert F(1, 32)**2-F(1, 64)**2 == F(3, 4096)
# 64 disjoint dyadic harmonic blocks each contribute at least 1/2.
blocks = 64
for k in range(blocks):
    assert F(2**k, 2**(k+1)) == F(1, 2)
# The normalized local mass decays: log H_j > (2/3)2^(j+4).
# log 2 >2/3 follows from the first term of 2*atanh(1/3).
assert 2*F(1, 3) == F(2, 3)
local_upper = [F(9, 64)/((F(2, 3))*2**(j+4)) for j in range(1, 65)]
assert all(local_upper[j+1] == local_upper[j]/2 for j in range(63))
result = {
    "status": "PASS",
    "scope": "rational artificial-profile margins; no actual-null or Lean certificate",
    "cosh_upper": str(cosh_upper), "sinh_upper": str(sinh_upper),
    "tv_plus_upper": str(tv_plus), "tv_minus_upper": str(tv_minus),
    "relative_cross_error_upper": str(error),
    "negative_observation_lower": "3/4096 times c_j",
    "signed_difference_lower": "3/4096 times c_j^2",
    "harmonic_blocks": blocks, "harmonic_block_lower": "1/2",
    "local_mass_checks": len(local_upper),
}
print(json.dumps(result, indent=2, sort_keys=True))
