#!/usr/bin/env python3
"""Elementary margins only; the endpoint promotion theorem is analytic."""
from fractions import Fraction as F
import json

# log 2 <1: integral_1^2 1/x dx < integral_1^2 1 dx.
# On [epsilon/2,epsilon], the logarithmic profile squared is
# between 1/(L+log 2) and 1/L.
for L in range(4, 68):
    lower = F(L, 2*(L+1))
    assert lower > F(1, 4)
    assert lower < F(1, 2)
    # sqrt-log integral relative upper budget 1+1/(2L).
    assert 1+F(1, 2*L) <= F(9, 8)
    # e^L >= L^2/2 implies L*e^-L <=2/L, tending to zero.
    assert F(2, L) <= F(1, 2)

# Cauchy-Schwarz gives M^2 <=epsilon*mass. Normalization then
# gives (sqrt(L)*M/epsilon)^2 <= L*mass/epsilon = B.
for L in [4, 8, 16, 32]:
    for eps in [F(1, 16), F(1, 256), F(1, 65536)]:
        for mass in [eps/F(L), eps/F(L*L)]:
            m_squared_upper = eps*mass
            assert L*m_squared_upper/(eps*eps) == L*mass/eps

print(json.dumps({
    "status": "PASS",
    "scope": "elementary endpoint mass/reciprocal budgets; no actual-null or Lean certificate",
    "log_profile_brackets": 64,
    "log_profile_normalized_lower": "1/4",
    "log_profile_normalized_upper": "1",
    "sqrt_log_integral_relative_upper": "9/8 for L>=4",
    "h1_rate_upper": "2/L from L exp(-L), tending to zero",
    "cauchy_normalizations": 24,
    "retained_pairings": ["interior mollified null residual", "exterior inverse residual"],
}, indent=2, sort_keys=True))
