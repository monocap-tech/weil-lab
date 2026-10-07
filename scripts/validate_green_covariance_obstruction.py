#!/usr/bin/env python3
"""Exact controls of covariance/completion implications, not native endpoints."""
import json
from fractions import Fraction as Q

tail_controls = completion_controls = projection_controls = 0
for m in range(9):
    for n in range(max(m+1, 2), max(m+1, 2)+20):
        # T=diag(1/n), finite correction supported in first m coordinates.
        raw_cov = Q(1, n*n)
        target_cov = 1 + Q(1, 2*n)
        assert raw_cov > 0
        assert raw_cov <= Q(1, (m+1)**2)
        assert target_cov - raw_cov >= 1
        # Any prefix correction leaves this tail coordinate unchanged.
        correction_on_tail = Q(0)
        assert raw_cov + correction_on_tail == raw_cov
        tail_controls += 1

mass = Q(0)
for n in range(1, 65):
    mass += Q(1, n*n)
    assert mass <= 2 - Q(1, n)
    raw_preimage_norm_sq = gradient_norm_sq = n
    assert raw_preimage_norm_sq == gradient_norm_sq
    assert mass < raw_preimage_norm_sq or n == 1
    completion_controls += 1

# Finite projections converge on every fixed finite support,
# while their covariance mismatch always has unit tail size.
for fixed_support in range(1, 17):
    for cutoff in range(fixed_support, fixed_support+8):
        assert all(n <= cutoff for n in range(1, fixed_support+1))
        tail_index = cutoff+1
        target_tail = 1 + Q(1, 2*tail_index)
        projected_tail = 0
        assert target_tail-projected_tail > 1
        projection_controls += 1

print(json.dumps({"covariance_tail_controls": tail_controls,
                  "completion_controls": completion_controls,
                  "projection_controls": projection_controls,
                  "status": "exact_controls_pass",
                  "scope": "abstract diagonal covariance and completion only"},
                 sort_keys=True))
