"""Upper ceiling of the existing 36-moment scalar cutoff majorant at a=14/25.

This limits that proof family, not the true native complement coercivity.
"""
import json,hashlib
from pathlib import Path
from certify_native_legendre_small_window import F,log_rational,sqrt_rational
from certify_native_larger_aperture_complement import integrated_mass


def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    op=root/'RPB108_PRIME3_GRAM36_056_OBSTRUCTION_CERTIFICATE_20261005.json'
    obstruction=json.loads(op.read_text())
    a=F(14,25);T0=F(763,100)
    S=sqrt_rational(F(2))*log_rational(F(2))
    A=log_rational(F(3))/sqrt_rational(F(3))
    logarithm=log_rational(T0)
    c0_lower=logarithm.lo-F(1,2)/T0-S.hi
    symbol_upper=logarithm.hi-F(1,2)/T0-S.lo-A.lo
    rho0=integrated_mass(a,36,T0)
    gap=730*rho0-(1+F(1,2)/T0)
    required=1/F(obstruction['necessary_uniform_inverse_upper'])
    assert c0_lower>0 and gap>0
    assert symbol_upper<F(353,1000)<required
    return dict(aperture='14/25',moment_dimension=36,cutoff_split=str(T0),
                scalar_family='c(T)-(10+c(T))*rho(T)-pole-A, c(T)=log(T)-1/(2T)-S',
                admissible_conditions=['T>0','geometric ratio<1','10+c(T)>=0'],
                rho_at_split=str(rho0),symbol_lower_at_split=str(c0_lower),
                derivative_negativity_gap=str(gap),symbol_minus_prime3_upper_at_split=str(symbol_upper),
                uniform_scalar_family_ceiling_upper='353/1000',
                necessary_physical_coercivity_lower=str(required),cutoff_only_repair_excluded=True,
                obstruction_certificate_sha256=hashlib.sha256(op.read_bytes()).hexdigest(),
                actual_complement_ceiling_proved=False,actual_negative_witness=False,
                whole_domain_positivity=False,global_endpoint_excluded=False,
                f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
