"""Exact rational constants certifying one actual Schur diagonal at a=1/2.

Analytic tail identities and smooth derivative bounds are proved in the note.
No floating value is used in the certificate.
"""
import json
from certify_native_legendre_small_window import F, I, log_rational, sqrt_rational, certificate


def certify():
    count = 64
    logtwo = log_rational(F(2))
    r = 2*logtwo-I(1)
    c = logtwo/sqrt_rational(F(2))
    assert 0 < r.lo < r.hi < 1
    polynomials = [I(1),r]
    for n in range(1,count):
        polynomials.append((F(2*n+1)*r*polynomials[n]-n*polynomials[n-1])/I(n+1))
    coefficients = [c*(I(1)-r)]
    for n in range(1,count):
        coefficients.append(I(0) if n%2 else
                            c*(polynomials[n-1]-polynomials[n+1])/sqrt_rational(F(2*n+1)))
    prime_tail = c*c*(I(1)-r)
    for x in coefficients:
        prime_tail = prime_tail-x*x
    assert prime_tail.hi < F(1,800) < F(1,28)**2
    log_tail_squared = F(1,count**2)
    smooth_tail_squared = F(3,2*count*(count+1))
    assert smooth_tail_squared < F(1,50)**2
    residual_norm = F(1,64)+F(1,28)+F(1,50)
    assert residual_norm < F(9,125)
    finite = certificate(F(1,2))
    actual_q00_lower = F(finite['pivot_lower_bounds'][0])
    assert actual_q00_lower > F(11,125)
    coupling_bound = 5*F(9,125)**2
    schur_lower = F(11,125)-coupling_bound
    assert schur_lower == F(194,3125) and schur_lower > F(3,50)
    return dict(status='certified one actual Schur diagonal only',aperture='1/2',
                source='constant 1 on [-1/2,1/2]',complement_moment_count=count,
                prime_tail_squared_enclosure=[str(prime_tail.lo),str(prime_tail.hi)],
                endpoint_log_tail_squared_bound=str(log_tail_squared),
                smooth_tail_squared_bound=str(smooth_tail_squared),
                residual_norm_upper_bound='9/125',coupling_upper_bound=str(coupling_bound),
                raw_q00_lower_bound='11/125',schur_diagonal_lower_bound=str(schur_lower),
                scalar_schur_sign_certified=True,full_schur_sign_certified=False,
                whole_domain_positivity=False)


if __name__ == '__main__':
    print(json.dumps(certify(),indent=2))
