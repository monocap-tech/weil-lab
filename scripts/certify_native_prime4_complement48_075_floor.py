"""Uniform actual 48-moment complement bounds through aperture 3/4."""
import json
from math import factorial
from certify_native_larger_aperture_complement import integrated_mass
from certify_native_legendre_small_window import F,atan,log_rational,sqrt_rational


def certificate():
    a=F(3,4);k=48;T=F(15,2);Tlog=F(7)
    pi=16*atan(F(1,5))-4*atan(F(1,239))
    assert 3<pi.lo<pi.hi<F(22,7)
    ell3=log_rational(F(3));amp=(ell3/sqrt_rational(F(3))).hi
    assert a<ell3.lo<ell3.hi<2*a
    assert log_rational(F(4)).hi<2*a<log_rational(F(5)).lo
    assert log_rational(F(2)).hi<1 and a/2<log_rational(F(2)).lo
    ell2=log_rational(F(2))
    amp2=(ell2/sqrt_rational(F(2))).hi
    assert ell2.hi<a and 2*a<3*ell2.lo
    amp4=ell2.hi/2
    joint=(amp4+sqrt_rational(amp4*amp4+8*amp2*amp2).hi)/2
    assert joint>amp2
    amp2=joint
    # Re psi(1/4+iy) >= psi(1/4); gamma < H_100-log(100) < 1.
    gamma_upper=sum((F(1,n) for n in range(1,101)),F(0))-log_rational(F(100)).lo
    assert gamma_upper<1
    arch_low=-gamma_upper-3*ell2.hi-pi.hi/2-log_rational(pi.hi).hi
    assert arch_low>-F(27,5)
    # On three-point prime-2 fibres, prime 4 closes the triangle.
    # Perron eigenvalue of [[0,A2,A4],[A2,0,A2],[A4,A2,0]] is joint.
    rho=integrated_mass(a,k,T)
    pole=16*a*(a/2)**(2*k)/factorial(k)**2
    c=log_rational(T).lo-F(7,216)/T**2
    physical=c-(F(27,5)+c)*rho-pole-amp2-amp
    assert physical>F(12,25)
    # m0(t)-amp2-amp >= w(t)/10 for t>=7; w <= log(t)+3/t.
    rho_log=integrated_mass(a,k,Tlog)
    highgap=F(9,10)*log_rational(Tlog).lo-F(3,10)/Tlog-F(7,216)/Tlog**2-amp2-amp
    assert highgap>0
    logarithmic=F(1,10)-(F(27,5)+amp2+amp+F(3,10))*rho_log-pole
    assert logarithmic>F(9,100)
    return dict(status='uniform actual 48-moment complement coercivity with joint compressed prime powers 2 and 4',
                aperture_interval=['1/2','3/4'],physical_degrees=list(range(k)),
                archimedean_high_lower='log(t)-7/(216t^2)',archimedean_high_valid_for='abs(t)>=1',
                quarter_line_euler_maclaurin_order=2,periodic_B2_absolute_upper='1/6',
                physical_cutoff=str(T),logarithmic_cutoff=str(Tlog),prime_terms_at_upper_aperture=[2,3,4],
                compressed_prime2_adjacency_norm_upper='sqrt(2)',prime4_amplitude_upper=str(amp4),
                joint_prime24_operator_upper=str(joint),joint_prime24_formula='(A4+sqrt(A4^2+8A2^2))/2',
                archimedean_global_lower=str(arch_low),archimedean_low_floor_used='-27/5',
                compressed_prime3_adjacency_norm_upper='1',prime3_amplitude_upper=str(amp),
                physical_low_frequency_mass_upper=str(rho),logarithmic_low_frequency_mass_upper=str(rho_log),pole_absolute_upper=str(pole),
                physical_unrounded_lower=str(physical),physical_lower='12/25',
                logarithmic_high_symbol_gap_lower=str(highgap),
                logarithmic_unrounded_lower=str(logarithmic),logarithmic_lower='9/100',
                complement_inverse_factor='25/12',schur_dimension=48,
                whole_domain_positivity=False,actual_negative_witness=False,
                f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
