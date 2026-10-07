#!/usr/bin/env python3
"""Exact combinatorial controls; not an actual native null certificate."""
import json
from fractions import Fraction

flags = ceilings = gain_checks = 0
for r in range(1, 17):
    for initial_parity in (1, -1):
        parities = [initial_parity * (-1)**q for q in range(r)]
        ranks = {p: parities.count(p) for p in (1, -1)}
        for j in range(r + 3):
            dims = {p: sum(q+j < r and parities[q] == p for q in range(r))
                    for p in (1, -1)}
            assert sum(dims.values()) == max(r-j, 0)
            for p in (1, -1):
                if j == 0:
                    bound = ranks[p]
                elif j % 2:
                    m = (j-1)//2
                    bound = max(0, min(ranks[p]-m, ranks[-p]-m))
                else:
                    m = j//2
                    bound = max(0, min(ranks[p]-m, ranks[-p]-m+1))
                assert dims[p] <= bound
                if j:
                    assert dims[p] <= sum(q+j-1 < r and parities[q] == -p
                                          for q in range(r))
                flags += 1
        for p in (1, -1):
            if ranks[p]:
                ceiling = min(2*ranks[p], 2*ranks[-p]+1)
                assert not any(parities[q] == p and q+ceiling < r
                               for q in range(r))
                ceilings += 1
        regular = {p: sum(q+1 < r and parities[q] == p for q in range(r))
                   for p in (1, -1)}
        for n in range(2, 9):
            s = Fraction(1, 4**n)
            for p in (1, -1):
                rough = ranks[p] - regular[p]
                trace = regular[p]*s + rough/s
                assert trace >= 0
                if ranks[p] > ranks[-p]:
                    assert rough >= ranks[p]-ranks[-p]
                    assert trace >= Fraction(ranks[p]-ranks[-p], s)
                gain_checks += 1

# Balanced control: one chosen parity trace vanishes, total diverges.
for n in range(2, 12):
    s = Fraction(1, 4**n)
    assert s > 0 and 1/s > 0
    assert s + 1/s > 1/s
    gain_checks += 1

# Abstract unequal ranks: regular part of the dominant sector is capped.
for rp in range(1, 9):
    for ro in range(rp):
        assert rp - min(rp, ro) == rp-ro > 0
        gain_checks += 1

print(json.dumps({"flag_controls": flags, "ceiling_controls": ceilings,
                  "gain_controls": gain_checks,
                  "status": "exact_controls_pass",
                  "scope": "spline parity counts and abstract gain rates only"},
                 sort_keys=True))
