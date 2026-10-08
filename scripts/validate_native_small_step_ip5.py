#!/usr/bin/env python3
"""RPB108 IP5: rank-one compact contact exact rational controls; NOT zeta/Lean."""
from fractions import Fraction as F
checks = 0
for j in range(5, 18):
    s = F(1) - F(1, 2**j)
    h = F(1, 16)
    t = s + h
    delta = 1 - s
    eps_squared = s*h
    relative = h/delta
    assert s < 1 < t; checks += 1
    assert eps_squared <= h and eps_squared > 0; checks += 1
    assert relative == F(2**j, 16) and relative > 1; checks += 1
    assert t - 1 == h - delta; checks += 1
s=F(63, 64); t=F(33, 32); d=1-s
assert t-s == F(3, 64); checks += 1
assert s*(t-s) == F(189, 4096); checks += 1
assert (t-s)/d == 3; checks += 1
assert 1-t == F(-1, 32); checks += 1
# Exact rank-one off-diagonal projection norm squared = s*(t-s).
for B in [F(3,2), F(2), F(5,2)]:
    for s in [F(1,4), F(1,2), F(63,64)]:
        for h in [F(1,32), F(1,16)]:
            if s+h <= B:
                assert s*h <= B*h; checks += 1
print(f"RPB108 IP5 exact rational controls: {checks} passed")
