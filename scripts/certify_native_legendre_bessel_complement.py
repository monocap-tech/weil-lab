"""Actual a=1/2 coercive complement after physical degrees 0..19."""
from fractions import Fraction as F
from math import factorial,prod
import json
from certify_native_legendre_small_window import atan,log_rational


def certificate():
    k=20
    pi=16*atan(F(1,5))-4*atan(F(1,239))
    assert pi.hi<F(13,4)
    assert log_rational(F(2)).hi<F(7,10)
    assert log_rational(F(2)).lo>F(2,3)
    assert F(100,49)>2
    assert log_rational(F(3)).lo>1
    # |j_n(y)| <= |y|^n/(2n+1)!! by its real Poisson integral.
    ratio=F(169,(2*k+1)*(2*k+3))
    first=F((2*k+1)*13**(2*k),prod(range(1,2*k+2,2))**2)
    rho2=8*first/(1-ratio)
    pole=F(8,4**(2*k)*factorial(k)**2)
    physical=F(5,24)-F(245,24)*rho2-pole
    logarithmic=F(1,10)-F(51,5)*rho2-pole
    assert physical>F(1,5)
    assert logarithmic>F(9,100)
    return dict(status='certified actual degree-20 complement coercivity',
                aperture='1/2',physical_orthogonality_degrees=[0,k-1],
                fourier_cutoff=4,plane_wave_argument_bound=13,
                bessel_squared_tail_ratio_upper=str(ratio),
                low_frequency_squared_norm_upper=str(rho2),
                low_frequency_squared_norm_display=float(rho2),
                pole_absolute_bound=str(pole),
                physical_coercivity_unrounded_lower=str(physical),
                logarithmic_coercivity_unrounded_lower=str(logarithmic),
                physical_coercivity='1/5',logarithmic_coercivity='9/100',
                schur_dimension=20,whole_domain_positivity=False)


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
