#!/usr/bin/env python3
"""Exact scalar verification; analytic/source hypotheses are not audited here."""
from fractions import Fraction as F
c=F(5003,5000)
P0=F(471031,125000)
D=F(20,3)
log2=F(693147181,10**9)
log3=F(1098612289,10**9)
log5=F(1609437913,10**9)
low=F(2,3)+F(11,7)+3*log2+log3+F(1,21)+F(7,6)
high=log2+log5+F(25,8)
assert low<D and high<D
lam=c/(c+P0+D)
assert lam==F(375225,4288318)
assert (1-lam)*(c+P0)-lam*D-P0==0
assert 1/lam==F(4288318,375225)<F(23,2)<21
print('low Gamma shift bound:',low)
print('high Gamma shift bound:',high)
print('inverse scalar reserve:',1/lam)
print('exact fractional reduction versus 21:',1-1/(21*lam))
print('PASS: exact scalar inequalities and convex decomposition')
