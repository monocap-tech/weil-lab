"""Independent polynomial recurrence, source conventions and complete mass audit."""
import json,hashlib
from pathlib import Path
from math import factorial,prod
from certify_native_legendre_small_window import F,I,atan


def polynomial(n,depth):
    p={1:F(1,2*n+3)}
    for _ in range(depth):
        square={}
        for i,a in p.items():
            for j,b in p.items():square[i+j]=square.get(i+j,F(0))+a*b
        p={1:F(1,2*n+3),**{d+1:v/F(2*n+3+d) for d,v in square.items()}}
    return {d+1:2*v/F(d+1) for d,v in p.items()}


def series_control(n,x):
    coefficients=[F(1)]
    for m in range(1,162):
        coefficients.append(-coefficients[-1]/F(2*m*(2*n+2*m+1)))
        assert 2*m*(2*n+2*m+1)*coefficients[m]+coefficients[m-1]==0
    terms=[v*x**(2*m) for m,v in enumerate(coefficients)]
    assert x*x<n*(n+1) and abs(terms[-1])<abs(terms[-2])
    hi=sum(terms[:-1],F(0));lo=hi+terms[-1];assert 0<lo<=hi
    exponent=sum((v*x**d for d,v in polynomial(n,6).items()),F(0))
    upper=1/sum((exponent**j/F(factorial(j)) for j in range(101)),F(0))
    assert hi*hi<upper
    excessive=1/sum(((2*exponent)**j/F(factorial(j)) for j in range(141)),F(0))
    assert lo*lo>excessive
    return dict(degree=n,argument=str(x),iteration_depth=6,
        independent_series_damping_verified=True,excessive_exponent_rejected=True,
        differential_equation_coefficient_identities=161)


def certificate(path,repeat):
    raw=Path(path).read_bytes();assert raw==Path(repeat).read_bytes();data={'23/25':json.loads(raw)}
    old=I.grid;I.grid=10**100
    try:pi=16*atan(F(1,5))-4*atan(F(1,239))
    finally:I.grid=old
    from certify_native_iterated_damped_mass_depth6 import derivative_coefficients,integrated_iterated_mass
    for n in (1,84,131):
        for depth in range(7):
            p=polynomial(n,depth)
            assert p=={2*j+2:v/F(j+1) for j,v in enumerate(derivative_coefficients(n,depth))}
        assert polynomial(n,1)=={2:F(1,2*n+3),4:F(1,2*(2*n+3)**2*(2*n+5))}
    reports=[]
    for aperture,c in data.items():
        a=F(aperture);T=F(c['physical_cutoff']);d=c['iterated_damping_details']
        assert d['iteration_depth']==6 and d['degrees']==list(range(84,132))
        U=F(d['positive_region_argument_squared_upper']);assert U>=(2*a*T*pi.hi)**2 and U<84*85
        Ylo=2*a*T*pi.lo
        for index,n in enumerate(range(84,132)):
            H=polynomial(n,6)
            exact_rate=F(2*n+1)-sum((power*v*U**(power//2) for power,v in H.items()),F(0))
            rate=F(d['integrated_rate_lower'][index])
            assert 0<rate==F((exact_rate*10**80).__floor__(),10**80)
            exponent=F(d['squared_damping_exponent_lower'][index])
            assert 0<exponent<=sum((v*Ylo**power for power,v in H.items()),F(0))
            term=F(1);den=term
            for j in range(1,101):term*=exponent/j;den+=term
            D=prod(range(1,2*n+2,2))
            bound=4*a*T*(2*n+1)*U**n/(rate*D*D*den)
            assert F(d['individual_integrated_term_upper'][index])>=bound
        upperY=2*a*F(22,7)*T;D=prod(range(1,266,2));ratio=upperY*upperY/F(265*267)
        assert 0<ratio<1
        tail=F(d['infinite_undamped_tail_upper']);assert tail>=4*a*T*upperY**264/(D*D*(1-ratio))
        rho=F(c['physical_low_frequency_mass_upper'])
        assert rho==sum(map(F,d['individual_integrated_term_upper']),F(0))+tail
        from certify_native_legendre_small_window import log_rational
        saved=I.grid;I.grid=10**100
        try:high=log_rational(T).lo-F(7,216)/T**2
        finally:I.grid=saved
        loss=F(c['joint_prime24_operator_upper'])+F(c['joint_prime35_operator_upper'])
        fresh_lower=high-(F(27,5)+high)*rho-loss-F(c['pole_absolute_upper'])
        assert fresh_lower>=F(c['physical_unrounded_lower'])>F(c['physical_lower'])
        assert F(c['complement_inverse_factor'])*F(c['physical_lower'])==1
        assert c['whole_domain_positivity'] is False and c['matching_native_source_gram_sign_pending'] is True
        reports.append(dict(aperture=aperture,all_48_degree_bounds_verified=True,complete_infinite_tail_verified=True,
            all_positive_region_and_rate_checks_passed=True,complement_only_scope_verified=True))
    controls=[(F(91,100),0,F(69,5),48,3),(F(91,100),84,F(20),48,3),
              (F(91,100),84,F(69,5),0,3),(F(91,100),84,F(69,5),48,7)]
    for args in controls:
        try:integrated_iterated_mass(*args)
        except ValueError:pass
        else:raise AssertionError('Invalid iteration domain accepted')
    checks=[series_control(n,F(x)) for n in (84,131) for x in (75,80)]
    return dict(preflight_sha256=hashlib.sha256(raw).hexdigest(),preflight_reproduced_byte_for_byte=True,
        independent_polynomial_recurrence_checks=21,quartic_specialization_checks=3,
        aperture_checks=reports,independent_bessel_series_controls=checks,
        invalid_iteration_domain_controls_rejected=len(controls),whole_domain_positivity_frontier='91/100',
        new_aperture_whole_domain_positivity=False,global_endpoint_excluded=False,f4_entry_closed=False,
        full_transport_closed=False,lean_formalized=False)


if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
