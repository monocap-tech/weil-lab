#!/usr/bin/env python3
"""CF018 read-only local validation of logarithmic interval capacity and
sharp arithmetic-discrepancy decoupling. No repository or network access.

Fourier convention: fhat(xi)=int exp(-2*pi*i*x*xi) f(x) dx.
Exact assertions are separated from exploratory numerical quadrature.
"""
from __future__ import annotations
from math import e, exp, log, pi, sqrt, sinh
from scipy.integrate import quad

C = 0.4
A = log(2.0)
KAPPA = log(2.0)/sqrt(2.0)
S_C = KAPPA  # Exactly one active prime power n=2 for c=0.4.
K_LOG = 1.0 - 0.5772156649015329 - log(2*pi)


def sincpi(z: float) -> float:
    if z == 0.0:
        return 1.0
    from math import sin
    return sin(pi*z)/(pi*z)


def rect_log_energy_approx(ell: float, cutoff: int = 256):
    """Finite-range numerical quadrature with a rigorous nonnegative tail
    *upper* bound. Do not interpret as certified interval arithmetic.
    """
    total = 0.0
    for j in range(cutoff):
        value, _ = quad(lambda z: 2.0*log(e + z/ell)*sincpi(z)**2,
                        float(j), float(j+1), epsabs=2e-11, epsrel=1e-10)
        total += value
    # 2/pi² ∫_Z∞ log(e+z/ell) / z² dz, exact antiderivative.
    Z = float(cutoff)
    tail_upper = (2.0/pi**2)*(log(e+Z/ell)/Z
                    + log(1.0 + e*ell/Z)/(e*ell))
    return total, tail_upper


def disc_exact(ell: float) -> float:
    return KAPPA/2 - 8*sqrt(2)/ell*sinh(ell/4)**2


def disc_independent_quad(ell: float) -> float:
    # Autocorrelation symmetric part: (ell - |s-a|)/(2ell) on [a-ell,a+ell].
    cont = quad(lambda s: exp(s/2)*(ell-abs(s-A))/(2*ell),
                A-ell, A+ell, points=[A], epsabs=1e-13, epsrel=1e-12)[0]
    return KAPPA/2-cont


def disc_bound(ell: float) -> float:
    wsmall = log(e+1/(4*ell))
    bracket = (S_C*(sqrt(2)*ell**0.25 + 1/sqrt(log(e+ell**(-0.5))))
               +sqrt(ell*(exp(2*C)-1)))
    return sqrt(2/wsmall)*bracket


def capacity_lower(ell: float) -> float:
    return 0.5*log(e+1/(4*ell))


def capacity_refined(ell: float) -> float:
    L = log(1/ell)
    if L < 2.0:
        return 0.0
    return max(0., L-log(2*L)-1.)


def main():
    assert A < 2*C and 2*C < log(3), 'One-prime window failed.'
    print(f'c={C}, active n=2, κ={KAPPA:.10f}')
    print('ell        D-exact     Elog approx   Elog-L      lower bound     D/Elog    upper A(ell)')
    for ell in (0.05,0.02,0.01,0.005,0.001,0.0001):
        assert ell < min(C, 2*C-A, A)
        dex = disc_exact(ell)
        dquad = disc_independent_quad(ell)
        assert abs(dex-dquad) < 2e-12, (ell,dex,dquad)
        val, upper_tail = rect_log_energy_approx(ell)
        L = log(1/ell)
        # Lower bound is exact; numerical val omits positive tail.
        assert val + 2e-10 >= capacity_lower(ell), (ell,val,capacity_lower(ell))
        assert val + 2e-10 >= capacity_refined(ell), (ell,val,capacity_refined(ell))
        # If ||f||log=||v||log=sqrt(E), the normalized ratio is D/E.
        # Actual E >= val, so abs(D)/E <= abs(D)/val.
        assert abs(dex)/val <= disc_bound(ell) + 1e-10
        print(f'{ell:8.4g}  {dex:10.7f}  {val:12.6f}  {val-L:9.5f}  '
              f'{capacity_lower(ell):12.6f}  {dex/val:9.6f}  {disc_bound(ell):12.6f}')
        print(f'           omitted positive Fourier tail <= {upper_tail:.5f}')
    print(f'Asymptotic Elog(1_[0,ell]/sqrt(ell)) - log(1/ell) '
          f'-> 1 - EulerGamma - log(2pi) = {K_LOG:.8f}')
    print(f'Asymptotic log(1/ell)*D/(||f||log ||v||log) '
          f'-> κ/2 = {KAPPA/2:.10f}')
    print('PASS: exact triangular correlation, logarithmic capacity, '
          'and mixed-discrepancy bound numerically checked.')

if __name__ == '__main__':
    main()