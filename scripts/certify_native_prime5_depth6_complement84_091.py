"""Fresh sixth finite-iteration complement at the fixed actual 91/100 aperture."""
import json
from certify_native_legendre_small_window import F,I,log_rational
from certify_native_prime5_iterated_complement84_091 import certificate as baseline
from certify_native_iterated_damped_mass_depth6 import integrated_iterated_mass

def certificate():
    old=I.grid;I.grid=10**80
    try:
        r=baseline();a=F(91,100);T=F(277,20)
        rho,detail=integrated_iterated_mass(a,84,T,depth=6)
        high=log_rational(T).lo-F(7,216)/T**2
        loss=F(r['joint_prime24_operator_upper'])+F(r['joint_prime35_operator_upper'])
        lower=high-(F(27,5)+high)*rho-loss-F(r['pole_absolute_upper'])
        c=F((lower*10**6).__floor__(),10**6);assert c>0 and lower>=c
        r.update(physical_cutoff=str(T),physical_low_frequency_mass_upper=str(rho),
            physical_unrounded_lower=str(lower),physical_lower=str(c),complement_inverse_factor=str(1/c),
            physical_lower_display=float(lower),physical_low_mass_display=float(rho),
            iterated_damping_details=detail,status='certified depth-six fixed-aperture complement; complete corrected sign pending')
        return r
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
