#!/usr/bin/env python3
"""Exact controls for the Abel sharp-height interface; no actual zeta data."""
from fractions import Fraction as F
from math import factorial
import json

scale = F(9, 4)
positive_total = scale * F(1, 4) / (1 - F(1, 4))**2
negative_total = positive_total / 2 + F(1, 2)
assert positive_total == negative_total == 1
signed_height = F(0)
spikes = []
for j in range(1, 65):
    theta = 4**j
    positive = scale * j / theta
    negative = positive / 2
    signed_height += theta * positive
    assert signed_height == scale * j
    spikes.append(str(signed_height))
    signed_height -= 2 * theta * negative
    assert signed_height == 0
# A rational ceiling proves exp(2)<8; lower exp(1/4)>=5/4.
n = 12
exp2_upper = sum((F(2)**k / factorial(k) for k in range(n + 1)), F(0))
exp2_upper += (F(2)**(n + 1) / factorial(n + 1)) / (1 - F(2, n + 2))
assert exp2_upper < 8
assert F(1, 4) * F(1, 8) * (1 - F(4, 5)) == F(1, 160)
assert scale * F(1, 160) == F(9, 640)
# Reject omitting the zero-ordinate normalization and treating a return to zero
# as a uniform bound: the half-negative mass and growing peaks are necessary.
assert positive_total != positive_total / 2
assert spikes[-1] == "144"
print(json.dumps({
    "kind": "abstract coefficient controls, not actual divisor or Lean proof",
    "positive_norm_squared": "1", "negative_norm_squared": "1",
    "paired_sharp_returns_checked": 64, "largest_sharp_peak": spikes[-1],
    "uniform_Abel_block_lower_coefficient": "9/640",
    "exp2_rational_ceiling_below_8": True,
    "actual_contact_bound_certified": False
}, indent=2, sort_keys=True))
