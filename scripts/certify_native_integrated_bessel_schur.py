"""Rational full-domain sign certificate at a=1/2; no all-window claim."""
import hashlib,json
from pathlib import Path
from fractions import Fraction as F
from math import factorial,prod
from certify_native_legendre_small_window import I,atan,log_rational,sqrt_rational,positive_pivots
from certify_native_legendre_bessel_complement import certificate as prior_complement


def certificate():
    prior_complement()  # retains logarithmic coercivity for the actual lift
    k=20;T=F(9,2)
    pi=16*atan(F(1,5))-4*atan(F(1,239))
    assert pi.hi<F(22,7)
    prime=sqrt_rational(F(2)).hi*log_rational(F(2)).hi
    y=F(22,7)*T
    ratio=y*y/((2*k+1)*(2*k+3))
    assert ratio<1
    # Integrate (2n+1)(pi t)^(2n)/[(2n+1)!!]^2 over [-T,T].
    # The integration cancels 2n+1; bound successive terms geometrically.
    rho=2*T*y**(2*k)/prod(range(1,2*k+2,2))**2/(1-ratio)
    pole=F(8,4**(2*k)*factorial(k)**2)
    high=log_rational(T).lo-F(1,2)/T-prime
    alpha=high-(10+high)*rho-pole
    assert alpha>F(2,5)
    beta=F(5,2);tau=F(1,10**7)
    root=Path(__file__).resolve().parents[1]/'notes/data'
    paths=[root/'RPB108_NATIVE_TWENTY_MATRIX_CERTIFICATE_20261005.json',root/'RPB108_TWENTY_RESIDUAL_GRAM_CERTIFICATE_20261005.json']
    native,gram=[json.loads(p.read_text()) for p in paths]
    assert gram['native_certificate_sha256']==hashlib.sha256(paths[0].read_bytes()).hexdigest()
    source=root/'RPB108_TWENTY_SMOOTH_SOURCE_CERTIFICATE_20261005.json'
    assert gram['source_certificate_sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
    assert native['physical_degrees']==gram['physical_degrees']==list(range(20))
    assert gram['projected_away_degrees']==list(range(20))
    delta=F(gram['actual_gram_operator_error_upper'])
    Q=[[I(*x) for x in row] for row in native['matrix_intervals']]
    R=[[I(*x) for x in row] for row in gram['residual_gram_surrogate']]
    lower=[[Q[i][j]-beta*R[i][j] for j in range(20)] for i in range(20)]
    for i in range(20):lower[i][i]-=beta*delta+tau
    pivots=positive_pivots(lower)
    broken=[row[:] for row in lower];broken[0][0]=I(-1)
    try:positive_pivots(broken)
    except ArithmeticError:pass
    else:raise AssertionError('Negative control accepted')
    # ||r||^2 <= trace(Rtilde)+delta; ||z|| <= beta ||r||.
    lift_norm_squared=beta**2*(sum((R[i][i].hi for i in range(20)),F(0))+delta)
    assert lift_norm_squared<25
    whole=tau/52
    assert 2*whole<F(2,5)
    return dict(status='certified strict actual full-domain positivity at aperture 1/2',
        aperture='1/2',physical_degrees=list(range(20)),fourier_cutoff=str(T),
        pi_upper='22/7',prime_amplitude_upper=str(prime),
        integrated_bessel_tail_ratio=str(ratio),integrated_low_mass_upper=str(rho),
        high_symbol_lower=str(high),pole_absolute_upper=str(pole),
        complement_unrounded_physical_lower=str(alpha),complement_physical_lower='2/5',
        retained_logarithmic_complement_lower='9/100',complement_inverse_factor='5/2',
        actual_gram_operator_error_upper=str(delta),corrected_schur_coercivity_lower=str(tau),
        shifted_pivot_lower_bounds=[str(x.lo) for x in pivots],
        lift_operator_norm_squared_upper=str(lift_norm_squared),lift_operator_norm_upper='5',
        whole_domain_physical_coercivity_lower=str(whole),negative_control_rejected=True,
        input_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        whole_domain_positivity=True,fixed_aperture_weak_kernel_zero=True,
        fixed_aperture_unit_domination=True,all_window_unit_domination=False,
        f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
