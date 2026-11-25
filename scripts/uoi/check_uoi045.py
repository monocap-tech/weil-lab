#!/usr/bin/env python3
"""UOI045 exact rational third-order interpolation budget; not Lean."""
from fractions import Fraction as Q
from math import cosh, sinh, pi, factorial

C = 32785
D = Q(1,1000)
qcap = Q(32)
assert 10*pi < 32
assert cosh(float(D/2)) < 2
assert sinh(float(D/2)) < float(D)
assert qcap**3 + qcap**2 * D/2 + qcap*2/4 < C
s7 = D**7 / (1-Q(1,8**7))
B3 = Q(5,9)*C*C*s7
penalty = Q(67,10)*B3
G3 = Q(11,10)-penalty
G_old = Q(2195428693,1996093750)
assert G3>G_old
assert G3 > Q(1099999,1000000) # 1.099999 < G3
assert G3 < Q(11,10)
print('Third-order Taylor remainder bound: |R_q(y)| <= (32785/6)|y|^3')
print('sum delta_j^7 <=',s7)
print('Low band / L2 mass <=',B3, '=',float(B3))
print('Gamma penalty <=',penalty,'=',float(penalty))
print('G3 lower =',G3,'=',float(G3))
print('Former G lower =',float(G_old))
print('Improvement =',float(G3-G_old))
print('Ten-stage lower using old B10 bound: >= G3-949/1000 =', float(G3-Q(949,1000)))
print('Exact-rational arithmetic checks PASS; no Lean/CI cert.')
