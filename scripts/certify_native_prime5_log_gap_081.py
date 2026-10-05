"""Quantified logarithmic stability from the certified physical 0.81 seed."""
import hashlib,json
from math import factorial
from pathlib import Path
from certify_native_legendre_small_window import F,I,log_rational,sqrt_rational


def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    gp=root/'RPB108_PRIME5_GRAM84_081_CERTIFICATE_20261005.json'
    vp=root/'RPB108_PRIME5_84_SCHUR_081_VALIDATION_20261005.json'
    cp=root/'RPB108_PRIME5_COMPLEMENT84_081_CERTIFICATE_20261005.json'
    g=json.loads(gp.read_text());v=json.loads(vp.read_text());c=json.loads(cp.read_text())
    assert v['certificate_sha256']==hashlib.sha256(gp.read_bytes()).hexdigest()
    assert v['certificate_reproduced_byte_for_byte'] and v['whole_domain_positivity']
    assert g['whole_domain_positivity'] and g['corrected_schur_sign_certified']
    assert g['aperture']=='81/100' and g['native_source_pairing_count']==7056
    mu=F(g['whole_domain_physical_coercivity_lower'])
    assert mu==F(1,202*10**29)
    assert F(c['archimedean_global_lower'])>-F(27,5)
    assert c['archimedean_high_lower']=='log(abs(t))-7/(216t^2), abs(t)>=1'
    previous=I.grid;I.grid=10**200
    try:
        log4=log_rational(F(4)).hi;assert log4<2
        prime=2*sum((log_rational(F(n if n!=4 else 2)).hi/sqrt_rational(F(n)).lo for n in (2,3,4,5)),F(0))
        assert prime<5
    finally:I.grid=previous
    e_upper=sum((F(1,factorial(k)) for k in range(21)),F(0))+F(1,factorial(21))/(1-F(1,22))
    assert e_upper<3
    # For |xi|<=1, w<=log(4)<2. For |xi|>=1, w<=log|xi|+log(4).
    low_difference_lower=-F(27,5)-F(1,5)
    high_difference_lower=-F(7,216)-F(1,5)
    assert min(low_difference_lower,high_difference_lower)>-6
    # Absolute pole <=4a exp(a)||h||^2 <=4e||h||^2 <12||h||^2 for a<=1.
    C=F(6+5+12);alpha=F(1,10)
    kappa=alpha*mu/(mu+C)
    physical_blend=C/(mu+C);garding_blend=mu/(mu+C)
    assert physical_blend+garding_blend==1
    assert physical_blend*mu-garding_blend*C==0 and garding_blend*alpha==kappa
    # A scalar control saturates both input inequalities. Doubling kappa fails.
    test_mass=F(1);test_energy=(mu+C)/alpha;test_q=mu
    assert test_q==mu*test_mass==alpha*test_energy-C*test_mass
    assert test_q-2*kappa*test_energy<0
    return dict(status='certified actual logarithmic seed gap and perturbation budget',aperture='81/100',
        canonical_log_weight='log(exp(1)+abs(xi))',physical_coercivity_lower=str(mu),
        archimedean_garding_log_coefficient=str(alpha),archimedean_garding_mass_loss='6',
        independent_prime_absolute_operator_upper=str(prime),prime_loss_ceiling='5',
        exponential_one_upper=str(e_upper),absolute_pole_loss_ceiling='12',
        total_garding_mass_loss=str(C),logarithmic_coercivity_lower=str(kappa),
        fixed_carrier_perturbation_radius=str(kappa/2),inverse_log_riesz_norm_upper=str(1/kappa),
        physical_blend_weight=str(physical_blend),garding_blend_weight=str(garding_blend),
        doubled_gap_arithmetic_control_rejected=True,control_is_actual_negative_witness=False,
        schur_certificate_sha256=hashlib.sha256(gp.read_bytes()).hexdigest(),
        schur_validation_sha256=hashlib.sha256(vp.read_bytes()).hexdigest(),
        complement_certificate_sha256=hashlib.sha256(cp.read_bytes()).hexdigest(),
        fixed_carrier_local_positive_neighborhood_exists=True,numerical_aperture_extension_certified=False,
        finite_first_endpoint_strictly_above='81/100',global_endpoint_excluded=False,
        retained_witness_transport_closed=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
