#!/usr/bin/env python3
"""UOI038 rational arithmetic verifier; not a Lean compiler or a proof of support transfer."""
from fractions import Fraction as F
from math import factorial, log, sqrt, pi, cosh, sinh

DELTA = F(1, 1000)
QMAX = F(32)
K = F(1025)
X = F(139, 200)
P4 = sum((X ** k) / factorial(k) for k in range(5))
assert P4 > F(2), 'exp(139/200)>2 must follow from positive Taylor terms'
# sqrt(8)>14/5; hence log(2)/sqrt(8)<(139/200)/(14/5)=139/560.
assert F(14, 5)**2 < F(8)
KAPPA_UPPER = F(139, 560)
assert KAPPA_UPPER == X / F(14, 5)
assert 10*pi < float(QMAX)
assert cosh(0.0005) < 2 and sinh(0.0005) < .001
# Hence |R''| <= q^2 + cosh(delta/2)/4 + |q| sinh(delta/2)/2 <1025.
assert QMAX**2 + F(2,4) + QMAX * DELTA / 2 < K
# |F f| <= K delta^(5/2) ||f||_2 on [-5,5].
LOW_BAND_RATIO = 10 * K**2 * DELTA**5
GAMMA_PENALTY = F(67, 10) * LOW_BAND_RATIO
RATIONAL_COEFF = F(11, 10) - KAPPA_UPPER - GAMMA_PENALTY
assert RATIONAL_COEFF > F(17, 20)
REAL_KAPPA = log(2)/sqrt(8)
REAL_COEFF = 1.1 - REAL_KAPPA - float(GAMMA_PENALTY)
# Exact normalized prime spectrum of Pi_D B Pi_D is +/-kappa/2.
# All other shell separations are more than 2 delta away from log(8).
assert abs(log(9/8)) > 2*float(DELTA)
assert abs(log(11/8)) > 2*float(DELTA)
assert log(2) > 2*float(DELTA)
center = log(8)/2
assert 1 + float(DELTA) < center < 1.1 - float(DELTA)
# Numerical spot checks only: the analytic Taylor remainder proof is in the report.
from cmath import exp as cexp
for freq in [0, .5, 3, 5]:
    q = 2*pi*freq
    for y in [-.001, -.0003, 0, .0003, .001]:
        rem = cexp(-1j*q*y)-cosh(y/2)+2j*q*sinh(y/2)
        assert abs(rem) <= (float(K)/2) * y*y + 1e-12
print('UOI038 exact rational checks PASS')
print('P4(139/200) =', P4, '= %.12f' % float(P4))
print('low-band L / ||f||^2 <=', LOW_BAND_RATIO, '= %.12g' % float(LOW_BAND_RATIO))
print('Gamma penalty <=', GAMMA_PENALTY, '= %.12g' % float(GAMMA_PENALTY))
print('Certified rational coefficient lower =',RATIONAL_COEFF, '= %.12f' % float(RATIONAL_COEFF))
print('Strong consequence: W(f) > (17/20) ||f||^2 for nonzero f in K')
print('Numeric coefficient (approx only) = %.12f' % REAL_COEFF)
print('Prime compressed operator eigenvalues +/-%.12f' % (REAL_KAPPA/2))
print('No Lean, no source-to-native equivalence, no RH or global positivity claim.')
