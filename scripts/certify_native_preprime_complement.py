"""Uniform actual complement bounds for 1/2 <= a <= 27/50.

No larger-aperture full-domain Schur sign or Lean claim.
"""
import json
from fractions import Fraction as F
from math import factorial, prod
from certify_native_legendre_small_window import atan, log_rational, sqrt_rational


def integrated_mass(a, k, cutoff):
    y = 2*a*F(22, 7)*cutoff
    ratio = y*y/F((2*k+1)*(2*k+3))
    if ratio >= 1:
        raise ValueError('Geometric majorant requires ratio < 1')
    return 4*a*cutoff*y**(2*k)/prod(range(1, 2*k+2, 2))**2/(1-ratio)


def certificate():
    a = F(27, 50)
    k = 20
    cutoff = F(43, 10)
    pi = 16*atan(F(1, 5))-4*atan(F(1, 239))
    assert pi.hi < F(22, 7)
    # Prime powers contribute when log(n) < 2a. Only n=2 is active.
    assert log_rational(F(2)).hi < 1
    assert 2*a < log_rational(F(3)).lo
    prime = sqrt_rational(F(2)).hi*log_rational(F(2)).hi
    assert prime < 1
    # Each exponential pole moment <= sqrt(2a)*2*(a/2)^k/k! ||f||_2.
    assert a/2 < log_rational(F(2)).lo
    pole = 16*a*(a/2)**(2*k)/factorial(k)**2
    rho = integrated_mass(a, k, cutoff)
    high = log_rational(cutoff).lo-F(1, 2)/cutoff-prime
    physical = high-(10+high)*rho-pole
    assert physical > F(1, 3)
    # Retain the established high-band m >= w/10 at cutoff 4.
    assert log_rational(F(2)).lo > F(2, 3)
    rho_log = integrated_mass(a, k, F(4))
    logarithmic = F(1, 10)-F(51, 5)*rho_log-pole
    assert logarithmic > F(9, 100)
    try:
        integrated_mass(a, k, F(100))
    except ValueError:
        pass
    else:
        raise AssertionError('Invalid geometric ratio accepted')
    return dict(
        status='uniform actual complement coercivity only',
        aperture_interval=['1/2', str(a)], physical_degrees=list(range(k)),
        prime_powers=[2], physical_cutoff=str(cutoff),
        integrated_physical_low_mass_upper=str(rho),
        physical_high_symbol_lower=str(high), pole_absolute_upper=str(pole),
        unrounded_physical_lower=str(physical), physical_lower='1/3',
        logarithmic_cutoff='4', integrated_logarithmic_low_mass_upper=str(rho_log),
        unrounded_logarithmic_lower=str(logarithmic), logarithmic_lower='9/100',
        complement_inverse_factor='3', invalid_ratio_control_rejected=True,
        larger_aperture_matrix_certified=False,
        larger_aperture_residual_gram_certified=False,
        larger_aperture_whole_domain_positivity=False,
        global_endpoint_excluded=False, f4_entry_closed=False,
        full_transport_closed=False, lean_formalized=False)


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
