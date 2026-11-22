#!/usr/bin/env python3
"""Exact arithmetic sanity checks for UOI043's constants and inequalities.

This script verifies rational constants only; it is NOT a Lean proof of the
Gamma prime spectral theorem, of compactness, or of RH.
"""
from fractions import Fraction as Q
from math import log, sqrt

B = Q(4096, 199609375)
G = Q(11, 10) - Q(67, 10)*B
assert G == Q(2195428693, 1996093750)
Lupper = Q(695, 914)
M0 = G - Lupper
assert M0 == Q(154834167288, 456107421875)
assert M0 > Q(1, 3)
assert 2*log(2)/(sqrt(8)-1) < float(Lupper)
assert G > Q(109986, 100000)

# The sum of physical measure of all infinitely many geometric collars.
measure = 2*Q(1,1000)/(1-Q(1,8))
assert measure == Q(2,875)

# q_6 / Gamma equivalence, if Gamma >= G*L2 on the test domain.
q6_over_gamma_max = 1 + Q(6)/G
assert q6_over_gamma_max > 1

# Recompute the constants displayed in UOI040 for the off-ladder baseline.
alpha = M0/(M0+Q(6)+Lupper)
assert 0 < alpha < 1

print("UOI043 rational arithmetic checks PASS")
print("G lower-bound:",G,float(G))
print("8-ladder upper-bound:",Lupper,float(Lupper))
print("ladder-subtracted baseline margin:",M0,float(M0))
print("union support volume:",measure,float(measure))
print("Gamma-to-q6 equivalence factor:",q6_over_gamma_max,float(q6_over_gamma_max))
print("Baseline-to-q6 lower comparison:",alpha,float(alpha))
print("finite-band HS squared coefficient: 4R/875")
