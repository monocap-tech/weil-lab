"""Uniform actual 48-moment complement bounds through aperture 69/100."""
import json
from math import factorial
from certify_native_larger_aperture_complement import integrated_mass
from certify_native_legendre_small_window import F,atan,log_rational,sqrt_rational


def certificate():
    a=F(69,100);k=48;T=F(81,10);Tlog=F(7)
    pi=16*atan(F(1,5))-4*atan(F(1,239))
    assert 2<pi.lo<pi.hi<F(22,7)
    ell3=log_rational(F(3));amp=(ell3/sqrt_rational(F(3))).hi
    assert a<ell3.lo<ell3.hi<2*a
    assert 2*a<log_rational(F(4)).lo
    assert log_rational(F(2)).hi<1 and a/2<log_rational(F(2)).lo
    ell2=log_rational(F(2))
    amp2=(ell2/sqrt_rational(F(2))).hi
    assert a<ell2.lo and ell2.hi<2*a
    # Re psi(1/4+iy) >= psi(1/4); gamma < H_100-log(100) < 1.
    gamma_upper=sum((F(1,n) for n in range(1,101)),F(0))-log_rational(F(100)).lo
    assert gamma_upper<1
    arch_low=-gamma_upper-3*ell2.hi-pi.hi/2-log_rational(pi.hi).hi
    assert arch_low>-8
    # A compressed shift and its adjoint form disjoint two-point fibres
    # when a < shift < 2a; their sum has norm exactly one.
    rho=integrated_mass(a,k,T)
    pole=16*a*(a/2)**(2*k)/factorial(k)**2
    c=log_rational(T).lo-F(1,2)/T
    physical=c-(10+c)*rho-pole-amp2-amp
    assert physical>F(89,100)
    # m0(t)-amp2-amp >= w(t)/10 for t>=7; w <= log(t)+3/t.
    rho_log=integrated_mass(a,k,Tlog)
    highgap=F(9,10)*log_rational(Tlog).lo-F(4,5)/Tlog-amp2-amp
    assert highgap>0
    logarithmic=F(1,10)-(10+amp2+amp+F(3,10))*rho_log-pole
    assert logarithmic>F(9,100)
    return dict(status='uniform actual 48-moment complement coercivity with compressed primes 2 and 3',
                aperture_interval=['1/2','69/100'],physical_degrees=list(range(k)),
                physical_cutoff=str(T),logarithmic_cutoff=str(Tlog),prime_terms_at_upper_aperture=[2,3],
                compressed_prime2_adjacency_norm_upper='1',prime2_amplitude_upper=str(amp2),
                archimedean_global_lower=str(arch_low),archimedean_low_floor_used='-10',
                compressed_prime3_adjacency_norm_upper='1',prime3_amplitude_upper=str(amp),
                physical_low_frequency_mass_upper=str(rho),logarithmic_low_frequency_mass_upper=str(rho_log),pole_absolute_upper=str(pole),
                physical_unrounded_lower=str(physical),physical_lower='89/100',
                logarithmic_high_symbol_gap_lower=str(highgap),
                logarithmic_unrounded_lower=str(logarithmic),logarithmic_lower='9/100',
                complement_inverse_factor='100/89',schur_dimension=48,
                whole_domain_positivity=False,actual_negative_witness=False,
                f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
