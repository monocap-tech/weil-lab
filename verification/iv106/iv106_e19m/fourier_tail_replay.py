"""E19M rational tail reserves, not an interval Gram certificate.

For g = indicator of a cell, |hat g(xi)| <= 1/(pi |xi|).
Thus integral over |xi|>T of |hat g|^2/w <= 2/(pi^2*T*w(T)).
For a physical trial f with weak derivative Df in L2,
Plancherel gives integral xi^2 |hat f|^2 = ||Df||^2/(4*pi^2).
The raw adjoint-column tail is <= ||Df||^2/(4*pi^2*T^2*w(T)).
The weighted trial tail is <= w(T)*||Df||^2/(4*pi^2*T^2):
w(x)/x^2 decreases for x>0 since x*w'(x)<=1 and 2*w(x)>=2.
The derivative mass is from E19A; native attachment is pending.
All bounds are squared L2 norms. Use Cauchy-Schwarz for mixed tails.
These estimates do not yet cover the actual IV105C response columns.
"""
from fractions import Fraction as F
from math import factorial

D2=F(27926390440838204641,16514364829462500)
assert D2<1692
for T,l,u in [(1000,6,7),(10000,8,10),(100000,10,12)]:
    # e<3, pi>3; e^l <= 3^l <= T; exp(u)>T+3>e+T.
    assert 3**l<=T
    assert sum(F(u**n,factorial(n)) for n in range(31))>T+3
    indicator=F(2,9*T*l)
    raw_trial=F(1692,36*T*T*l)
    weighted_trial=F(1692*u,36*T*T)
    print(T,l,u,indicator,raw_trial,weighted_trial)

# Arbitrary exterior physical g gives a raw adjoint column whose
# supported projection is zero. It is safe to subtract it both when
# approximating Riesz representatives and when bounding full residuals.
# The closure of these exterior adjoint columns is the entire supported
# carrier orthogonal complement, by the kernel-range annihilator identity.
# Finite exterior banks may approximate the projection, but no numerical
# enclosure of that approximation is produced by this replay.
