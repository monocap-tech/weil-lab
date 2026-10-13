"""Rational constants for the analytic actual a=1/2 complement theorem."""
from fractions import Fraction as F
from math import factorial
import json
from certify_native_legendre_small_window import log_rational


def certificate():
    k = 64
    # Only prime 2 occurs, and S=sqrt(2)*log(2)<(10/7)*(7/10)=1.
    assert log_rational(F(2)).hi < F(7,10)
    assert log_rational(F(3)).lo > 1
    assert F(100,49) > 2
    rho2 = F(8*3**32*16**(2*k),factorial(k)**2)
    pole = F(8,4**(2*k)*factorial(k)**2)
    physical_loss = F(245,24)*rho2+pole
    logarithmic_loss = F(51,5)*rho2+pole
    assert physical_loss < F(1,120)
    assert logarithmic_loss < F(1,100)
    return dict(status='certified constants for actual complement coercivity',
                aperture='1/2',physical_orthogonality_degrees=[0,k-1],
                fourier_cutoff=4,low_frequency_squared_norm_bound=str(rho2),
                pole_absolute_bound=str(pole),physical_loss_bound=str(physical_loss),
                logarithmic_loss_bound=str(logarithmic_loss),
                physical_coercivity='1/5',logarithmic_coercivity='9/100',
                low_frequency_squared_norm_display=float(rho2),
                schur_dimension=k,schur_sign_certified=False,
                whole_domain_positivity=False)


if __name__ == '__main__':
    print(json.dumps(certificate(),indent=2))
