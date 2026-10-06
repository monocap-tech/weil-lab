"""Actual 84-moment complement with a proved spherical-Bessel tail damping."""
import hashlib,json
from pathlib import Path
from math import factorial
from certify_native_legendre_small_window import F,I,atan,log_rational
from certify_native_larger_aperture_complement import integrated_mass
from certify_native_prime5_complement84_082 import certificate as original_certificate


def damped_mass(a,k,T,q,N):
    if k<1 or N<1 or not 0<q<1:raise ValueError('Invalid tail split')
    pi=16*atan(F(1,5))-4*atan(F(1,239))
    if (2*a*pi.hi*T)**2>=k*(k+1):raise ValueError('Outside proved positive Bessel region')
    z=(2*a*pi.lo*q*T)**2/F(2*(k+N-1)+3)
    # exp(z) >= its finite positive Taylor sum; reciprocal is an upper bound.
    exponential_lower=sum((z**j/factorial(j) for j in range(61)),F(0))
    attenuation=I(1/exponential_lower).hi
    low=integrated_mass(a,k,q*T)
    undamped=integrated_mass(a,k,T)
    tail=integrated_mass(a,k+N,T)
    bound=low+attenuation*undamped+tail
    return bound,dict(split_low_mass_upper=str(low),undamped_full_mass_upper=str(undamped),
        finite_band_attenuation_upper=str(attenuation),tail_mass_upper=str(tail),
        damping_exponent_lower=str(z),exponential_lower_terms=61,
        proved_positive_region_upper_argument_squared=str((2*a*pi.hi*T)**2))


def certificate():
    old=I.grid;I.grid=10**80
    try:
        result=original_certificate();a=F(41,50);k=84;T=F(67,5);q=F(87,100);N=16
        rho,detail=damped_mass(a,k,T,q,N)
        loss=F(result['joint_prime24_operator_upper'])+F(result['joint_prime35_operator_upper'])
        high=log_rational(T).lo-F(7,216)/T**2
        physical=high-(F(27,5)+high)*rho-F(result['pole_absolute_upper'])-loss
        assert physical>F(3,5) and rho<F(2,1000)
        for args in [(a,0,T,q,N),(a,k,F(20),q,N),(a,k,T,F(1),N),(a,k,T,q,0)]:
            try:damped_mass(*args)
            except ValueError:pass
            else:raise AssertionError('Invalid damping domain accepted')
        root=Path(__file__).resolve().parents[1]/'notes/data'
        result.pop('aperture_interval')
        result.update(status='certified fixed-aperture actual damped 84-moment complement',aperture='41/50',
            physical_cutoff=str(T),physical_low_frequency_mass_upper=str(rho),
            physical_unrounded_lower=str(physical),physical_lower='3/5',complement_inverse_factor='5/3',
            damping_frequency_split=str(q),damped_degree_count=N,damped_degrees=list(range(k,k+N)),
            damping_details=detail,invalid_damping_domain_controls_rejected=4,
            prior_complement_sha256=hashlib.sha256((root/'RPB108_PRIME5_COMPLEMENT84_082_CERTIFICATE_20261006.json').read_bytes()).hexdigest(),
            physical_lower_display=float(physical),physical_low_mass_display=float(rho),
            whole_domain_positivity=False,whole_domain_positivity_frontier='81/100')
        return result
    finally:I.grid=old


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
