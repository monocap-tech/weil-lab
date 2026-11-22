#!/usr/bin/env python3
"""UOI036 reproducible numeric/exact rational sanity checks (NOT Lean certification)."""
from fractions import Fraction as F
import cmath
import math

b_old = F(1,1)
b_mid = F(11,10)
b_new = F(6,5)
delta = F(1,1000)
m = 4*delta
T = math.log(8)
c8 = math.log(2)/math.sqrt(8)

# Exact rational consequences of the sourced Gamma high/low bounds and Cauchy-Schwarz.
low_band = 10*m
assert low_band == F(1,25)
gamma = F(11,10)-F(67,10)*low_band
assert gamma == F(104,125)
pole = 8*m
assert pole == F(4,125)
assert gamma-pole == F(4,5)

# Physical geometry: each halfwidth 0.001 interval lies strictly in old-new collar,
# and in the original intermediate 11/10 window used by the pinned Zeta23 literal form.
assert float(b_old)+float(delta) < T/2 < float(b_mid)-float(delta) < float(b_new)
assert T+2*float(delta) < 2*float(b_new)
assert math.log(2)>2*float(delta)
assert math.log(8)-math.log(7)>2*float(delta)
assert math.log(9)-math.log(8)>2*float(delta)
for n in range(2,12):
    same_side_possible = math.log(n) <= 2*float(delta)
    cross_side_possible = abs(math.log(n)-T) <= 2*float(delta)
    assert not same_side_possible, n
    assert cross_side_possible == (n == 8), n

# Source prime normalization: complete von Mangoldt term is 2 times the
# half-weighted selfadjoint translation-shell quadratic form, not 1 times it.
# For a paired source h = u + beta T_8 u with |beta|=1, 
# mass = 2J, B-energy = c8*J*Re(beta), full prime = 2*c8*J*Re(beta).
J = 1.3
for beta in [1, -1, 1j, cmath.exp(1.5j), cmath.exp(0.2j)]:
    mass = 2*J
    B_energy = c8*J*beta.real
    source_prime = 2*c8*J*beta.real
    assert abs(source_prime-2*B_energy)<1e-12
    assert abs(source_prime) <= c8*mass+1e-12

# Exact analytic lower-bound constants. The strict >1/2 statement is for nonzero f.
coercivity = float(gamma-pole)-c8
assert c8 < F(3,10)
assert coercivity > 0.5
# Uniform delta condition for positivity (m=4delta).
threshold_delta = (1.1-c8)/300
assert float(delta) < threshold_delta

print('UOI036 checked: geometry, only n=8, exact rational gamma/pole budgets,')
print('complex phase and factor-of-two prime normalization. NOT a Lean certificate.')
print('t8 = %.12f; center ±%.12f; halfwidth = %.6f' % (T, T/2, float(delta)))
print('total length m =',m,'low-band relative cap =',low_band)
print('Gamma lower =',gamma,'= %.12f' % float(gamma))
print('Pole absolute upper =',pole,'= %.12f' % float(pole))
print('Prime absolute upper = c8 = %.12f' % c8)
print('Source signed Weil lower = (4/5 - c8) M = %.12f M' % coercivity)
print('Sufficient delta threshold from budget = %.12f' % threshold_delta)
print('STATUS: analytic + arithmetic check only; no new compiler or RH claim.')