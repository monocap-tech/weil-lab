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
    z=x*x/F(2*n+3)
    upper=1/sum((z**m/factorial(m) for m in range(61)),F(0))
    assert hi*hi<upper
    too_strong=1/sum(((2*z)**m/factorial(m) for m in range(101)),F(0))
    assert lo*lo>too_strong
    return dict(degree=n,argument=str(x),normalized_squared_upper=str(hi*hi),
        damping_upper=str(upper),too_strong_damping_rejected=True,ode_coefficient_identity_checks=K+1)


def certificate(repeat_path):
    root=Path(__file__).resolve().parents[1]/'notes/data'
    path=root/'RPB108_PRIME5_INTEGRATED_SCHUR84_085_CERTIFICATE_20261006.json'
    raw=path.read_bytes();assert raw==Path(repeat_path).read_bytes();c=json.loads(raw)
    cp=root/'RPB108_PRIME5_INTEGRATED_COMPLEMENT84_085_CERTIFICATE_20261006.json'
    complement=json.loads(cp.read_bytes())
    assert c['complement_certificate_sha256']==hashlib.sha256(cp.read_bytes()).hexdigest()
    assert F(complement['physical_unrounded_lower'])>F(complement['physical_lower'])==F(13,20)
    detail=complement['integrated_damping_details']
    assert detail['degrees']==list(range(84,132))
    assert sum(map(F,detail['individual_integrated_term_upper']),F(0))+F(detail['infinite_undamped_tail_upper'])==F(complement['physical_low_frequency_mass_upper'])
    names={'gram':'RPB108_PRIME5_GRAM84_085_CERTIFICATE_20261006.json',
        'source':'RPB108_PRIME5_SOURCE84_085_CERTIFICATE_20261006.json',
        'native':'RPB108_PRIME5_MATRIX84_085_COMPACT80_20261006.json'}
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
    assert beta==F(20,13) and tau>0 and len(c['shifted_pivot_lower_bounds'])==84
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
    mu=tau*F(13,20)/(tau+F(13,20)*(1+L*L));kappa=mu/(10*(mu+23))
    assert mu==F(c['whole_domain_physical_coercivity_lower']) and kappa==F(c['logarithmic_coercivity_lower'])
    determinant=(tau-mu*(1+L*L))*(F(13,20)-mu)-(mu*L)**2
    assert determinant==F(c['exact_conversion_determinant'])==mu*mu>0
    checks=[series_control(n,F(x)) for n in (84,131) for x in (60,75)]
    return dict(certificate_reproduced_byte_for_byte=True,certificate_sha256=hashlib.sha256(raw).hexdigest(),
        all_four_input_hashes_verified=True,all_84_corrected_pivots_rechecked_at_80_digits=True,
        negative_diagonal_control_rejected=True,full_domain_and_logarithmic_conversions_verified=True,
        independent_bessel_series_controls=checks,whole_domain_positivity=True,
        global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)


if __name__=='__main__':
    import sys
    print(json.dumps(certificate(sys.argv[1]),indent=2))
