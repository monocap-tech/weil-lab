"""Actual complement at 9/10 using integrated degree-by-degree damping."""
import json
from certify_native_legendre_small_window import F,I,log_rational
from certify_native_prime5_complement84_090 import certificate as previous_certificate
from certify_native_integrated_damped_mass import integrated_damped_mass


def certificate():
    old=I.grid;I.grid=10**80
    try:
        result=previous_certificate();a=F(9,10);T=F(66,5);rho,detail=integrated_damped_mass(a,84,T)
        high=log_rational(T).lo-F(7,216)/T**2
        loss=F(result['joint_prime24_operator_upper'])+F(result['joint_prime35_operator_upper'])
        lower=high-(F(27,5)+high)*rho-loss-F(result['pole_absolute_upper'])
        assert lower>F(149,250) and rho<F(1,500)
        for args in [(a,0,T,48),(a,84,F(20),48),(a,84,T,0)]:
            try:integrated_damped_mass(*args)
            except ValueError:pass
            else:raise AssertionError('Invalid integrated damping accepted')
        result.pop('damping_details')
        result.update(status='certified actual 84-moment complement at 9/10 with integrated damping',
            physical_cutoff=str(T),physical_low_frequency_mass_upper=str(rho),
            physical_unrounded_lower=str(lower),physical_lower='149/250',complement_inverse_factor='250/149',
            integrated_damping_details=detail,invalid_integrated_damping_controls_rejected=3,
            physical_lower_display=float(lower),physical_low_mass_display=float(rho))
        return result
    finally:I.grid=old


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
