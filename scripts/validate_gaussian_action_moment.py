#!/usr/bin/env python3
"""Rational overlap/rate controls; not an actual Gaussian action estimate."""
import json
from fractions import Fraction as Q
from math import factorial

# The Gaussian floor e^(-1/2)>1/2 used in the lower overlap.
partial = sum((Q(1, 2)**j / factorial(j) for j in range(9)), Q(0))
first_omitted = Q(1, 2)**9 / factorial(9)
tail_ceiling = first_omitted / (1-Q(1, 20))
assert partial + tail_ceiling < 2

cone_checks = split_checks = rate_checks = 0
for k in range(4, 25):
    x = k*k
    cone = [n for n in range(x-k, x+k+1) if abs(n-x) <= Q(k, 2)]
    assert len(cone) >= Q(k, 2)
    for n in cone:
        assert n >= Q(x, 2)
        assert Q((x-n)**2, n) <= Q(1, 2)
        # n^(3/2) >= x^(3/2)/4, after squaring.
        assert n**3 >= Q(x**3, 16)
        cone_checks += 1
    # count * Gaussian floor * coefficient floor >= x^2/16.
    assert Q(k, 2)*Q(1, 2)*Q(x*k, 4) == Q(x*x, 16)

for x in (4, 9, 16, 25, 36, 49):
    for n in range(2, 4*x+1):
        exponent = Q((x-n)**2, n)
        if n < Q(x, 2):
            assert exponent >= Q(x, 2)
        elif n > 2*x:
            assert exponent >= Q(n, 4)
        else:
            assert exponent >= Q((x-n)**2, 2*x)
        split_checks += 1
for x in (-1, -2, -9, -16):
    for n in range(2, 17):
        assert Q((x-n)**2, n) >= n+2*abs(x)
        split_checks += 1

mass = Q(0)
for j in range(1, 33):
    mass += Q(1, j*j)
    assert mass <= 2-Q(1, j)
    n = j*j
    assert Q(j**3, j**5) == Q(1, n)
    rate_checks += 1
# Condensed baseline harmonic blocks diverge, while extra log power sums.
for k in range(1, 9):
    harmonic_block = sum((Q(1, j) for j in range(2**k, 2**(k+1))), Q(0))
    assert harmonic_block >= Q(1, 2)
    rate_checks += 1

print(json.dumps({"cone_controls": cone_checks, "split_controls": split_checks,
                  "rate_controls": rate_checks, "status": "exact_controls_pass",
                  "scope": "Gaussian overlap inequalities and polynomial rate algebra"},
                 sort_keys=True))
