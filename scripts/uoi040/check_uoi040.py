#!/usr/bin/env python3
"""UOI040: exact rational nested-Gamma/conditional margin checks,
plus high-precision example of elementary log(8)/log(3) approximation.
This is not Lean certification or a proof of uniform arithmetic leakage.
"""
from fractions import Fraction as F
from math import factorial

# Sum_{j>=0} delta_j^3 = 1/(1000^3) * 512/511.
sum_delta_cubed = F(1, 1000**3) * F(512, 511)
B = 20480 * sum_delta_cubed
assert B == F(4096, 199609375)
gamma_penalty = F(67, 10) * B
assert gamma_penalty == F(137216, 998046875)
G = F(11, 10) - gamma_penalty
assert G == F(2195428693, 1996093750)

# Reuse *strict* UOI039 rational upper bound on full 8-power prime sum.
x = F(139, 200)
assert sum(x**k / factorial(k) for k in range(5)) > 2
assert F(707, 250)**2 < 8
C8 = 2*x/(F(707, 250) - 1)
assert C8 == F(695, 914)
M0 = G - C8
assert M0 == F(154834167288, 456107421875)
slack_one_third = M0 - F(1, 3)
assert slack_one_third == F(8395079989, 1368322265625)
assert M0 > F(1, 3) > 0

# Nested collars: fixed widths delta_j, not recomputed as m grows.
prev = set()
for m in range(2, 22):
    present = set(range(m))
    assert prev.issubset(present)
    prev = present
    assert sum(F(1, 1000*8**j)**3 for j in present) <= sum_delta_cubed

# Earliest explicit non-ladder prime edge in the nested model: 4099 near 8**4.
# Trial division by every d <= floor(sqrt(4099)) = 64 is a deterministic
# primality certificate (no statistical/probabilistic primality test).
assert all(4099 % d for d in range(2, 65))
assert 64**2 < 4099 < 65**2
assert F(3, 4096) < F(1, 1000)

# Numerical *infinite-family illustration only*.
# Irrationality + Dirichlet prove infinitely many 3-power resonances.
import mpmath as mp
mp.mp.dps = 90
D, K = 1054, 1995
err = D*mp.log(8) - K*mp.log(3)
assert mp.mpf('0') < abs(err) < mp.mpf('0.00025')

print('UOI040 exact nested-Gamma and conditional margin arithmetic PASS')
print('Band B:', B, float(B))
print('Gamma lower G:', G, float(G))
print('Original 8-ladder upper C8:', C8, float(C8))
print('Pre-leakage margin M0:', M0, float(M0))
print('To preserve >=1/3, required leakage <=', slack_one_third, float(slack_one_third))
print('FIRST explicit off-ladder prime interaction at m=5: prime 4099 near 8**4=4096')
print('Illustrative remote resonance |1054 log8 - 1995 log3|:', mp.nstr(abs(err), 30))
print('WARNING: No bound on off-ladder leakage ell_m has been proved.')
print('NO Lean, zero-side, global Weil positivity, or RH certification.')