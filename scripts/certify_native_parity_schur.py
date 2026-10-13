"""Exact rational constants for the actual constant/linear corrected block."""
import json
from certify_native_legendre_small_window import F, I, log_rational, sqrt_rational, certificate
from certify_native_constant_schur import certify as constant_certificate


def certify():
    constant = constant_certificate()
    logtwo = log_rational(F(2))
    r = 2*logtwo-I(1)
    length = 2*logtwo
    c = logtwo/sqrt_rational(F(2))
    polynomials = [I(1),r]
    for n in range(1,65):
        polynomials.append((F(2*n+1)*r*polynomials[n]-n*polynomials[n-1])/I(n+1))
    integrals = [I(1)-r]+[(polynomials[n-1]-polynomials[n+1])/I(2*n+1)
                         for n in range(1,65)]
    prime_tail = c*c*(I(1)-r*r*r)/I(3)
    for n in range(1,64,2):
        coeff = c*((n+1)*integrals[n+1]+n*integrals[n-1]
                   -length*(2*n+1)*integrals[n])/sqrt_rational(F(2*n+1))
        prime_tail = prime_tail-coeff*coeff
    assert prime_tail.hi < F(1,900)
    smooth_squared = F(81,6*64*65)
    assert smooth_squared < F(3,50)**2
    assert F(1,64)+F(1,30)+F(3,50) < F(11,100)
    finite = certificate(F(1,2))
    # Q_01=0 by exact parity, so pivot 1 equals the raw Q_11 entry.
    assert F(finite['pivot_lower_bounds'][1]) > F(9,100)
    linear_lower = F(9,100)-5*F(11,100)**2
    assert linear_lower == F(59,2000) and linear_lower > F(1,40)
    physical_lower = F(3,50)
    assert F(constant['schur_diagonal_lower_bound']) > physical_lower
    assert linear_lower > physical_lower/3
    return dict(status='certified actual corrected constant-linear block only',aperture='1/2',
                low_sources=['1','2x'],physical_gram_diagonal=['1','1/3'],
                complement_moment_count=64,
                linear_prime_tail_squared_enclosure=[str(prime_tail.lo),str(prime_tail.hi)],
                linear_log_tail_norm_bound='1/64',linear_smooth_tail_squared_bound=str(smooth_squared),
                linear_residual_norm_bound='11/100',linear_coupling_upper_bound='121/2000',
                corrected_diagonal_lower_bounds=[constant['schur_diagonal_lower_bound'],str(linear_lower)],
                corrected_mixed_entry='0 (exact reflection parity)',physical_coercivity=str(physical_lower),
                corrected_block_sign_certified=True,full_schur_sign_certified=False,
                whole_domain_positivity=False)


if __name__ == '__main__':
    print(json.dumps(certify(),indent=2))
