"""Fresh complement, support geometry and constructor ceilings beyond 9/10."""
import json
from math import factorial
from certify_native_legendre_small_window import F,I,log_rational,bernoulli
from certify_native_prime5_complement84_092 import certificate as baseline
from certify_native_iterated_damped_mass import integrated_iterated_mass
from certify_native_translation_panel_order import translation_panels


def certificate(a):
    parameters={F(91,100):(F(69,5),F(317,500),39),F(23,25):(F(137,10),F(623,1000),40)}
    if a not in parameters:raise ValueError('Unsupported iterated preflight aperture')
    T,c,ceiling=parameters[a];old=I.grid;I.grid=10**80
    try:
        result=baseline(a);rho,detail=integrated_iterated_mass(a,84,T,depth=3)
        high=log_rational(T).lo-F(7,216)/T**2
        loss=F(result['joint_prime24_operator_upper'])+F(result['joint_prime35_operator_upper'])
        lower=high-(F(27,5)+high)*rho-loss-F(result['pole_absolute_upper']);assert lower>c
        d=2*a;L=4*a
        assert log_rational(F(ceiling)).lo>L and log_rational(F(5)).hi<L
        B=bernoulli(202)
        coefficients=[abs(B[2*k]*(2*d)**(2*k)/factorial(2*k)) for k in range(1,101)]
        assert all(y<x for x,y in zip(coefficients,coefficients[1:]))
        assert all((B[2*k]>0)==(k%2==1) for k in range(1,101))
        assert (1+d+d*d/3)/2<F(9,4) and d/2<1 and d<3
        panels=translation_panels(a)
        assert panels['labels']==['0','1-log(5)/(2a)','1-log(4)/(2a)','log(2)/(2a)',
            '1-log(3)/(2a)','log(3)/(2a)','1-log(2)/(2a)','log(4)/(2a)','log(5)/(2a)','1']
        result.pop('damping_details')
        result.update(status='certified fresh iterated complement and geometry; matched sign pending',
            physical_cutoff=str(T),physical_low_frequency_mass_upper=str(rho),
            physical_unrounded_lower=str(lower),physical_lower=str(c),complement_inverse_factor=str(1/c),
            iterated_damping_details=detail,physical_lower_display=float(lower),physical_low_mass_display=float(rho),
            native_exp_ceiling=ceiling,native_kernel_ceiling=str(5*L/4),source_kernel_ceiling='9/4',
            source_alternating_kernel_controls_passed=True,panel_endpoints=panels['labels'],
            whole_domain_positivity_frontier='9/10',matching_native_source_gram_sign_pending=True)
        return result
    finally:I.grid=old


if __name__=='__main__':print(json.dumps({str(a):certificate(a) for a in (F(91,100),F(23,25))},indent=2))
