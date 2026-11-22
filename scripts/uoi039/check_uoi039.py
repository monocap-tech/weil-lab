#!/usr/bin/env python3
"""UOI039 exact rational budget and sample-geometry checks.

No symbolic/Lean kernel proof, no statement of general Weil positivity/RH.
"""
from fractions import Fraction as Q
from math import factorial, log, pi, sqrt

# Strict rational certificates: exp(139/200)>2 by its positive Taylor lower sum;
# sqrt(8)>707/250 by squaring.
x = Q(139, 200)
p4 = sum(x**k / factorial(k) for k in range(5))
assert p4 > 2
assert Q(707, 250)**2 < 8
r_upper = Q(250, 707)
prime_upper = 2*x*r_upper/(1-r_upper)
assert prime_upper == Q(695, 914)

# Delta_m = 1/(1000*8**(m-2)), with m*delta_m <= 1/500.
# The all-m proof uses m <= 2*8**(m-2) by induction.
# 2*delta_m / 8**(-(m-1)) = 16/1000 < 8/9,
# giving a rigorous uniform log-separation from every other integer.
assert Q(16, 1000) < Q(8, 9)
assert 2*Q(1, 1000) < Q(1, 10)

band_upper = Q(20, 500)*Q(32, 1000)**2
gamma_penalty = Q(67, 10)*band_upper
margin = Q(11, 10)-prime_upper-gamma_penalty
assert band_upper == Q(16, 390625)
assert gamma_penalty == Q(536, 1953125)
assert margin == Q(302880048, 892578125)
assert margin > Q(1, 3)

# The optional three-ordinary-moment filter is smaller but remains infinite-dimensional.
third_moment_band = Q(20, 500)*Q(32, 1000)**6/Q(6)**2
assert third_moment_band < band_upper

k1 = log(2)/sqrt(8)
k2 = log(2)/8
true_prime_bound = 2*log(2)/(sqrt(8)-1)
assert true_prime_bound < float(prime_upper)
assert 10*pi < 32

# A_3 finite-dimensional (prime operator tensor the identity on each collar).
# The 8-8-64 triangle makes the third spectral moment nonzero.
trace_cube = 6*k1*k1*k2
determinant = 2*k1*k1*k2
lambdas = [-k2, (k2+sqrt(k2*k2+8*k1*k1))/2, (k2-sqrt(k2*k2+8*k1*k1))/2]
assert trace_cube > 0 and determinant > 0
assert abs(sum(l**3 for l in lambdas)-trace_cube) < 1e-12
assert abs(sum(lambdas)) < 1e-12

# Sample checks of the general support geometry, NOT substitutes for its induction proof.
t = log(8)
for m in range(2, 13):
    delta = 1/(1000*8**(m-2))
    assert m*delta <= 1/500
    centers = [(j+0.5)*t for j in range(m)]
    assert centers[0]-delta > 1
    assert (centers[-1]+delta) > 0
    for d in range(1, m):
        assert 2*delta < log(1+8**(-d))
    # Finite Toeplitz row-sums, bounded uniformly by the geometric series.
    for j in range(m):
        row = sum(log(2)*8**(-abs(j-k)/2) for k in range(m) if j != k)
        assert row < true_prime_bound

print('UOI039 rational and finite consistency checks PASS')
print('Strict certified rational prime norm upper:', prime_upper, '≈', float(prime_upper))
print('Strict certified rational gamma penalty upper:', gamma_penalty, '≈', float(gamma_penalty))
print('Universal lower ratio:', margin, '≈', float(margin), '>1/3')
print('True (non-rational) geometric prime norm cap ≈', true_prime_bound)
print('m=3 prime spectrum ≈', lambdas)
print('m=3 trace(A^3) =', trace_cube, '>0 (not chiral)')
print('Theorem is analytic only; no UOI039 Lean compilation or acceptance.')