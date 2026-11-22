#!/usr/bin/env python3
"""Arithmetic and algebraic checks for UOI037 (NOT a Lean proof)."""
from decimal import Decimal, getcontext
from fractions import Fraction as F
from itertools import product

getcontext().prec=65
D=Decimal

t=D(8).ln()
kappa=D(2).ln()/D(8).sqrt()
delta=F(1,1000)
assert D(1)+D(delta.numerator)/D(delta.denominator)<t/2<D(11)/10-D(delta.numerator)/D(delta.denominator)
assert t/2 < D(6)/5-D(delta.numerator)/D(delta.denominator)
assert D(2).ln() > 2*D(delta.numerator)/D(delta.denominator)
assert D(8).ln()-D(7).ln() > 2*D(delta.numerator)/D(delta.denominator)
assert D(9).ln()-D(8).ln() > 2*D(delta.numerator)/D(delta.denominator)
for n in range(2,13):
    s=D(n).ln()
    assert not (s<=D(2)/1000), n
    assert (abs(s-t)<=D(2)/1000)==(n==8), n

# Exact rational Fourier/Gamma bounds on two microcollars.
length=4*delta
lowband=10*length
assert length==F(1,250)
assert lowband==F(1,25)
gamma=F(11,10)-F(67,10)*lowband
assert gamma==F(104,125)
prior_pole=8*length
assert prior_pole==F(4,125)
assert gamma-prior_pole==F(4,5)

# Formal integration-by-parts coefficient of e^{s x}(eta''-1/4 eta).
for sigma in [F(1,2),-F(1,2)]:
    assert sigma**2-F(1,4)==0

# Pole form on moment image C² is nondegenerate of signature (1,1).
def p(u,v):
    return u[0].conjugate()*v[1]+u[1].conjugate()*v[0]
assert p((1,1),(1,1))==2
assert p((1,-1),(1,-1))==-2
assert p((1,1),(1,-1))==0
assert p((1,1j),(1,1j))==0
assert p((1,1j),(1,0))==(-1j)

# Phi and its shifted copy both have moment vector (0,0), so every phase is pole-neutral.
for beta in [1+0j,-1+0j,1j,(3+4j)/5]:
    J=2.0
    first=beta*J  # correlation at +log 8
    other=beta.conjugate()*J
    full_prime=float(kappa)*(first+other)
    half_shell=float(kappa)/2*(first+other)
    assert abs(full_prime.imag)<1e-12
    assert abs(full_prime.real-2*float(kappa)*J*beta.real)<1e-12
    assert abs(full_prime-2*half_shell)<1e-12
    assert abs(full_prime.real)<=float(kappa)*2*J+1e-12

# Rational strict bound log(2)/sqrt(8) < 1/4.
partial=1+F(7,10)+F(7,10)**2/F(2)+F(7,10)**3/F(6)
assert partial==F(12013,6000)>2
assert F(8)>F(14,5)**2
assert kappa<D(1)/4
margin=D(gamma.numerator)/D(gamma.denominator)-kappa
assert margin>D(291)/500
assert (gamma-F(1,4))==F(291,500)
assert (gamma-prior_pole)==F(4,5)
assert (margin-(D(4)/5-kappa))==D(prior_pole.numerator)/D(prior_pole.denominator)

print('UOI037: sanity checks grouped by geometry, exact gamma/rational arithmetic,')
print('double-moment cancellation, rank-two pole signature, phase and normalization PASS.')
print('log8/2 =',t/2,'; kappa =',kappa)
print('Gamma lower =', gamma, '; general earlier pole penalty =',prior_pole)
print('Pole-neutral W lower coefficient =', margin)
print('Rational conservative coefficient = 291/500 =',D(291)/500)
print('Source-bound analytical checks only; NOT Lean/kernel acceptance.')