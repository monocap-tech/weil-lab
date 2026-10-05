"""Uniform actual 36-moment complement bounds through aperture 11/20."""
import json
from math import factorial
from certify_native_larger_aperture_complement import integrated_mass
from certify_native_legendre_small_window import F,atan,log_rational,sqrt_rational


def certificate():
    a=F(14,25);k=36;T=F(15,2);Tlog=F(7)
    pi=16*atan(F(1,5))-4*atan(F(1,239))
    assert pi.hi<F(22,7)
    ell3=log_rational(F(3));amp=(ell3/sqrt_rational(F(3))).hi
    assert a<ell3.lo<ell3.hi<2*a
    assert 2*a<log_rational(F(4)).lo
    assert log_rational(F(2)).hi<1 and a/2<log_rational(F(2)).lo
    S=sqrt_rational(F(2)).hi*log_rational(F(2)).hi
    assert S<1
    rho=integrated_mass(a,k,T)
    pole=16*a*(a/2)**(2*k)/factorial(k)**2
    c=log_rational(T).lo-F(1,2)/T-S
    physical=c-(10+c)*rho-pole-amp
    assert physical>F(31,100)
    # m2(t)-amp >= w(t)/10 for t>=7; w <= log(t)+3/t.
    rho_log=integrated_mass(a,k,Tlog)
    highgap=F(9,10)*log_rational(Tlog).lo-F(4,5)/Tlog-S-amp
    assert highgap>0
    logarithmic=F(1,10)-(10+amp+F(3,10))*rho_log-pole
    assert logarithmic>F(9,100)
    return dict(status='uniform actual 36-moment complement coercivity with compressed prime 3',
                aperture_interval=['1/2','14/25'],physical_degrees=list(range(k)),
                physical_cutoff=str(T),logarithmic_cutoff=str(Tlog),prime_terms_at_upper_aperture=[2,3],
                compressed_prime3_adjacency_norm_upper='1',prime3_amplitude_upper=str(amp),
                physical_low_frequency_mass_upper=str(rho),logarithmic_low_frequency_mass_upper=str(rho_log),pole_absolute_upper=str(pole),
                physical_unrounded_lower=str(physical),physical_lower='31/100',
                logarithmic_high_symbol_gap_lower=str(highgap),
                logarithmic_unrounded_lower=str(logarithmic),logarithmic_lower='9/100',
                complement_inverse_factor='100/31',schur_dimension=36,
                whole_domain_positivity=False,actual_negative_witness=False,
                f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
