"""Check an inconclusive complement lower bound after prime-3 activation."""
import json
from math import factorial
from certify_native_larger_aperture_complement import integrated_mass
from certify_native_legendre_small_window import F,log_rational,sqrt_rational


def certificate():
    a=F(11,20);T=F(43,10)
    S=sqrt_rational(F(2)).hi*log_rational(F(2)).hi
    rho=integrated_mass(a,20,T);pole=16*a*(a/2)**40/factorial(20)**2
    c=log_rational(T).lo-F(1,2)/T-S
    baseline=c-(10+c)*rho-pole
    amp=log_rational(F(3))/sqrt_rational(F(3))
    combined=baseline-amp.hi
    assert combined<0
    assert log_rational(F(3)).lo>a and log_rational(F(3)).hi<2*a
    return dict(status='inconclusive twenty-moment physical complement bound after prime-3 activation',
                aperture=str(a),cutoff=str(T),prime2_only_physical_lower=str(baseline),
                compressed_prime3_amplitude_interval=[str(amp.lo),str(amp.hi)],
                combined_physical_lower=str(combined),
                overlap_width_interval=[str(2*a-log_rational(F(3)).hi),str(2*a-log_rational(F(3)).lo)],
                compressed_prime3_adjacency_norm='1',complement_coercivity_certified=False,
                actual_negative_witness=False,whole_domain_positivity=False,
                f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
