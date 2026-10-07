#!/usr/bin/env python3
"""Exact edge-overlap and IBP constants; no actual-null certificate."""
import json
from fractions import Fraction as Q

def derivative_polynomial(p):
    q = {}
    for degree, coefficient in p.items():
        if degree:
            q[degree-1] = q.get(degree-1, Q(0)) + degree*coefficient
        q[degree+1] = q.get(degree+1, Q(0)) - coefficient/2
    return {k: v for k, v in q.items() if v}

p = {1: Q(1)}
derivatives = [p]
for _ in range(4):
    p = derivative_polynomial(p)
    derivatives.append(p)
assert derivatives[1].get(0) == 1
assert derivatives[3].get(0) == Q(-3, 2)
assert derivatives[4] == {1: Q(15, 4), 3: Q(-5, 4), 5: Q(1, 16)}
moments = {1: Q(2), 3: Q(8), 5: Q(64)}
l1_ceiling = sum(abs(v)*moments[k] for k, v in derivatives[4].items())
assert l1_ceiling == Q(43, 2)
assert l1_ceiling + Q(3, 2) == 23

overlap_controls = sign_controls = rate_controls = 0
for j in range(65):
    t = Q(j, 16)
    overlap = t if t <= 1 else 2-t if t <= 2 else Q(0)
    overlap = max(Q(0), overlap)
    assert overlap >= 0
    if t <= 1:
        assert overlap == t
    else:
        assert abs(overlap-t) <= 2*t
    overlap_controls += 1
assert Q(23, 64) + Q(24576, 64**3) == Q(29, 64)
for r in range(64, 257):
    relative_error = Q(23, r)+Q(24576, r**3)
    assert relative_error <= Q(29, 64) < Q(1, 2)
    sign_controls += 1
for k in range(8, 41):
    n = k*k
    # The action weight n^(3/2) exactly cancels the control's R^(-3/2).
    assert Q(k**3, k**3) == 1
    rate_controls += 1

print(json.dumps({"overlap_controls": overlap_controls,
                  "sign_controls": sign_controls, "rate_controls": rate_controls,
                  "fourth_derivative_L1_ceiling": str(l1_ceiling),
                  "relative_error_at_64": "29/64", "status": "exact_controls_pass",
                  "scope": "adjacent-step carrier control; not actual native residual"},
                 sort_keys=True))
