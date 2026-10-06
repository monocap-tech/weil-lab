"""Independent Bessel-series controls and widened stored Schur sign checks."""
import hashlib,json
from pathlib import Path
from math import factorial
from certify_native_legendre_small_window import F,I,positive_pivots


def series_control(n,x,K=160):
    coefficients=[F(1)]
    for m in range(1,K+2):
        coefficients.append(-coefficients[-1]/(2*m*(2*n+2*m+1)))
        assert 2*m*(2*m+2*n+1)*coefficients[m]+coefficients[m-1]==0
    terms=[c*x**(2*m) for m,c in enumerate(coefficients)]
    assert x*x<n*(n+1) and abs(terms[-1])<abs(terms[-2])
    partial=sum(terms[:-1],F(0));lo=partial+terms[-1];hi=partial
    assert 0<lo<=hi
    A=F(1,2*n+3);B=A*A/F(2*n+5)
    assert (2*n+3)*A==1 and (2*n+5)*B==A*A
    assert 2*A*B>0 and B*B>0
    z=x*x/F(2*n+3)+x**4/F(2*(2*n+3)**2*(2*n+5))
    upper=1/sum((z**m/factorial(m) for m in range(81)),F(0))
    assert hi*hi<upper
    too_strong=1/sum(((2*z)**m/factorial(m) for m in range(101)),F(0))
    assert lo*lo>too_strong
    return dict(degree=n,argument=str(x),normalized_squared_upper=str(hi*hi),
        damping_upper=str(upper),too_strong_damping_rejected=True,ode_coefficient_identity_checks=K+1)



def integrated_exponential_control(n,z,w,K=180):
    # Integrate the even Taylor polynomial in z*s^2+w*s^4 exactly.
    from math import comb
    assert z>0 and w>0 and K%2==0
    zp=[z**m for m in range(K+2)];wp=[w**m for m in range(K+2)]
    terms=[F((-1)**m,factorial(m))*sum((comb(m,j)*zp[m-j]*wp[j]/F(2*n+2*m+2*j+1)
            for j in range(m+1)),F(0)) for m in range(K+2)]
    upper=sum(terms[:-1],F(0));lower=upper+terms[-1]
    assert 0<lower<=upper and abs(terms[-1])<abs(terms[-2])
    rate=F(2*n+1)-2*z-4*w;assert rate>0
    attenuation_upper=1/sum(((z+w)**m/factorial(m) for m in range(81)),F(0))
    majorant=attenuation_upper/rate
    assert upper<majorant
    old=I.grid;I.grid=10**80
    try:
        reported_lower=I(lower).lo;reported_upper=I(upper).hi;reported_majorant=I(majorant).lo
        assert 0<reported_lower<=reported_upper<reported_majorant
        return dict(degree=n,integrated_taylor_pairs=K//2,positive_integral_lower=str(reported_lower),
            independent_integral_upper=str(reported_upper),power_majorant_lower=str(reported_majorant),
            report_interval_grid_digits=80,integrated_power_majorant_verified=True)
    finally:I.grid=old


def certificate(repeat_path):
    root=Path(__file__).resolve().parents[1]/'notes/data'
    path=root/'RPB108_PRIME5_QUARTIC_SCHUR84_090_CERTIFICATE_20261006.json'
    raw=path.read_bytes();assert raw==Path(repeat_path).read_bytes();c=json.loads(raw)
    cp=root/'RPB108_PRIME5_QUARTIC_COMPLEMENT84_090_CERTIFICATE_20261006.json'
    complement=json.loads(cp.read_bytes())
    assert c['complement_certificate_sha256']==hashlib.sha256(cp.read_bytes()).hexdigest()
    assert F(complement['physical_unrounded_lower'])>F(complement['physical_lower'])==F(627,1000)
    detail=complement['quartic_damping_details']
    assert detail['degrees']==list(range(84,132))
    assert sum(map(F,detail['individual_integrated_term_upper']),F(0))+F(detail['infinite_undamped_tail_upper'])==F(complement['physical_low_frequency_mass_upper'])
    names={'gram':'RPB108_PRIME5_GRAM84_090_CERTIFICATE_20261006.json',
        'source':'RPB108_PRIME5_SOURCE84_090_CERTIFICATE_20261006.json',
        'native':'RPB108_PRIME5_MATRIX84_090_COMPACT80_20261006.json'}
    data={}
    for key,name in names.items():
        value=(root/name).read_bytes();assert hashlib.sha256(value).hexdigest()==c['input_sha256'][key]
        data[key]=json.loads(value)
    g=data['gram'];R=[[(F(lo),F(hi)) for lo,hi in row] for row in g['residual_gram_surrogate']]
    assert len(R)==84 and all(len(row)==84 for row in R)
    assert all(R[i][j]==R[j][i] and R[i][j][0]<=R[i][j][1] for i in range(84) for j in range(84))
    trace=sum((R[i][i][1] for i in range(84)),F(0));M=F(g['surrogate_residual_map_norm_upper'])
    assert M*M>=trace
    eta=F(data['source']['source_map_error_upper']);delta=eta*(2*M+eta)
    assert delta==F(c['actual_gram_operator_error_upper'])
    native=data['native'];triangle=native['lower_triangle_row_major'];assert len(triangle)==3570
    Q=[[None]*84 for _ in range(84)];index=0
    for i in range(84):
        for j in range(i+1):
            Q[i][j]=Q[j][i]=tuple(F(int(x),10**80) for x in triangle[index]);index+=1
    beta=F(c['complement_inverse_factor']);tau=F(c['corrected_coercivity_lower_bound'])
    assert beta==F(1000,627) and tau>0 and len(c['shifted_pivot_lower_bounds'])==84
    assert min(map(F,c['shifted_pivot_lower_bounds']))>0
    old=I.grid;I.grid=10**80
    try:
        lower=[[I(*Q[i][j])-beta*I(*R[i][j]) for j in range(84)] for i in range(84)]
        for i in range(84):lower[i][i]-=beta*delta+tau
        fresh=positive_pivots(lower);assert len(fresh)==84 and min(p.lo for p in fresh)>0
        broken=[row[:] for row in lower];broken[0][0]=I(-1)
        try:positive_pivots(broken)
        except ArithmeticError:pass
        else:raise AssertionError('Negative diagonal accepted')
    finally:I.grid=old
    L=c['lift_operator_norm_integer_upper'];lift2=beta*beta*(trace+delta)
    assert lift2==F(c['lift_norm_squared_upper']) and L*L>lift2
    mu=tau*F(627,1000)/(tau+F(627,1000)*(1+L*L));kappa=mu/(10*(mu+23))
    assert mu==F(c['whole_domain_physical_coercivity_lower']) and kappa==F(c['logarithmic_coercivity_lower'])
    determinant=(tau-mu*(1+L*L))*(F(627,1000)-mu)-(mu*L)**2
    assert determinant==F(c['exact_conversion_determinant'])==mu*mu>0
    checks=[series_control(n,F(x)) for n in (84,131) for x in (75,80)]
    from certify_native_legendre_small_window import atan
    old=I.grid;I.grid=10**100
    try:pi=16*atan(F(1,5))-4*atan(F(1,239))
    finally:I.grid=old
    a=F(9,10);T=F(69,5);Y=2*a*T*pi.lo
    from math import prod
    U=F(detail['positive_region_argument_squared_upper'])
    assert U>=(2*a*T*pi.hi)**2 and U<84*85
    assert len(detail['integrated_rate_lower'])==len(detail['squared_damping_exponent_lower'])==48
    degree_checks=0
    for index,n in enumerate(range(84,132)):
        z=U/F(2*n+3);w=U*U/F(2*(2*n+3)**2*(2*n+5))
        rate=F(detail['integrated_rate_lower'][index]);assert rate==2*n+1-2*z-4*w and rate>0
        e=F(detail['squared_damping_exponent_lower'][index])
        assert 0<e<=Y*Y/F(2*n+3)+Y**4/F(2*(2*n+3)**2*(2*n+5))
        # Independently accumulate the positive exponential sum by recurrence.
        term=F(1);denominator=term
        for j in range(1,81):term*=e/j;denominator+=term
        D=prod(range(1,2*n+2,2))
        bound=4*a*T*(2*n+1)*U**n/(rate*D*D*denominator)
        assert F(detail['individual_integrated_term_upper'][index])>=bound
        degree_checks+=1
    # The remaining undamped infinite tail has an exact geometric majorant.
    upperY=2*a*F(22,7)*T;D=prod(range(1,266,2))
    first=4*a*T*upperY**264/(D*D)
    ratio=upperY*upperY/F(265*267);assert 0<ratio<1
    assert F(detail['infinite_undamped_tail_upper'])>=first/(1-ratio)
    # Modest rational control arguments avoid importing the constructor's moments.
    integral_checks=[integrated_exponential_control(84,F(35),F(4)),
                     integrated_exponential_control(131,F(23),F(11,10))]

    return dict(certificate_reproduced_byte_for_byte=True,certificate_sha256=hashlib.sha256(raw).hexdigest(),
        all_four_input_hashes_verified=True,all_84_corrected_pivots_rechecked_at_80_digits=True,
        negative_diagonal_control_rejected=True,full_domain_and_logarithmic_conversions_verified=True,
        independent_bessel_series_controls=checks,independent_integrated_exponential_controls=integral_checks,whole_domain_positivity=True,
        all_48_quartic_degree_bounds_rechecked=degree_checks==48,complete_infinite_tail_rechecked=True,
        global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)


if __name__=='__main__':
    import sys
    print(json.dumps(certificate(sys.argv[1]),indent=2))
