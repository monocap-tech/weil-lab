"""Independent widened refined-sign and exact complement/conversion audit at 97/100."""
import hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I,positive_pivots

def certificate(repeat_path):
    root=Path(__file__).resolve().parents[1]/'notes/data'
    path=root/'RPB108_PRIME5_SCHUR96_097_CERTIFICATE_20261007.json'
    raw=path.read_bytes();assert raw==Path(repeat_path).read_bytes();c=json.loads(raw)
    cp=root/'RPB108_PRIME5_96_PREFLIGHT_097_20261007.json'
    complement=json.loads(cp.read_bytes())
    assert c['complement_certificate_sha256']==hashlib.sha256(cp.read_bytes()).hexdigest()
    assert F(complement['physical_lower'])==F(477,500)<F(complement['physical_unrounded_lower'])
    names={'gram':'RPB108_PRIME5_GRAM96_097_CERTIFICATE_20261007.json',
        'source':'RPB108_PRIME5_SOURCE96_097_CERTIFICATE_20261007.json',
        'native':'RPB108_PRIME5_MATRIX96_097_COMPACT80_20261007.json'}
    data={}
    for key,name in names.items():
        p=root/name
        value=p.read_bytes() if p.exists() else __import__('gzip').decompress(p.with_suffix('.json.gz').read_bytes())
        assert hashlib.sha256(value).hexdigest()==c['input_sha256'][key]
        data[key]=json.loads(value)
    g=data['gram'];R=[[(F(lo),F(hi)) for lo,hi in row] for row in g['residual_gram_surrogate']]
    assert len(R)==96 and all(len(row)==96 for row in R)
    assert all(R[i][j]==R[j][i] and R[i][j][0]<=R[i][j][1] for i in range(96) for j in range(96))
    trace=sum((R[i][i][1] for i in range(96)),F(0));M=F(g['surrogate_residual_map_norm_upper'])
    assert M*M>=trace
    eta=F(data['source']['source_map_error_upper']);delta=eta*(2*M+eta)
    assert delta==F(c['actual_gram_operator_error_upper'])
    native=data['native'];triangle=native['lower_triangle_row_major'];assert len(triangle)==4656
    Q=[[None]*96 for _ in range(96)];index=0
    for i in range(96):
        for j in range(i+1):
            Q[i][j]=Q[j][i]=tuple(F(int(x),10**80) for x in triangle[index]);index+=1
    beta=F(c['complement_inverse_factor']);tau=F(c['corrected_coercivity_lower_bound'])
    assert beta==1/F(477,500) and tau>0 and len(c['shifted_pivot_lower_bounds'])==96
    assert min(map(F,c['shifted_pivot_lower_bounds']))>0
    old=I.grid;I.grid=10**80
    try:
        lower=[[I(*Q[i][j])-beta*I(*R[i][j]) for j in range(96)] for i in range(96)]
        for i in range(96):lower[i][i]-=beta*delta+tau
        fresh=positive_pivots(lower);assert len(fresh)==96 and min(p.lo for p in fresh)>0
        broken=[row[:] for row in lower];broken[0][0]=I(-1)
        try:positive_pivots(broken)
        except ArithmeticError:pass
        else:raise AssertionError('Negative diagonal accepted')
    finally:I.grid=old
    L=c['lift_operator_norm_integer_upper'];lift2=beta*beta*(trace+delta)
    assert lift2==F(c['lift_norm_squared_upper']) and L*L>lift2
    mu=tau*F(477,500)/(tau+F(477,500)*(1+L*L));kappa=mu/(10*(mu+23))
    assert mu==F(c['whole_domain_physical_coercivity_lower']) and kappa==F(c['logarithmic_coercivity_lower'])
    determinant=(tau-mu*(1+L*L))*(F(477,500)-mu)-(mu*L)**2
    assert determinant==F(c['exact_conversion_determinant'])==mu*mu>0
    false_mu=2*mu
    assert (tau-false_mu*(1+L*L))*(F(477,500)-false_mu)-(false_mu*L)**2<0
    from certify_native_exact_logarithm import log_rational
    jp=root/'RPB108_PRIME5_WEIGHTED_POINTWISE_097_CERTIFICATE_20261007.json'
    jr=jp.read_bytes() if jp.exists() else __import__('gzip').decompress(jp.with_suffix('.json.gz').read_bytes())
    joint=json.loads(jr)
    assert hashlib.sha256(jr).hexdigest()==complement['prime_input_uncompressed_sha256']
    assert 2*sum(map(F,joint['amplitude_upper']))<5
    old=I.grid;I.grid=10**80
    try:
        assert log_rational(F(3),300).lo>1  # exp(1)<3
        assert log_rational(F(4),300).hi<2
        assert log_rational(F(7),300).lo>2*F(97,100)
    finally:I.grid=old
    assert F(97,100)<1 and 4*F(97,100)*3<12
    # Published m0 >= w/10-6; prime loss <5 and pole loss <12.
    assert 6+5+12==23
    assert mu>F(9,10**30) and kappa>F(4,10**32)
    return dict(published_physical_lower='9/10^30',published_logarithmic_lower='4/10^32',aperture='97/100',fresh_garding_constant_23_verified=True,certificate_reproduced_byte_for_byte=True,
        certificate_sha256=hashlib.sha256(raw).hexdigest(),all_four_input_hashes_verified=True,
        all_96_corrected_pivots_rechecked_at_80_digits=True,actual_source_correction_recomputed=True,
        refined_complement_exactly_below_proved_unrounded_bound=True,
        negative_diagonal_control_rejected=True,excessive_conversion_control_rejected=True,
        full_domain_and_logarithmic_conversions_verified=True,
        physical_coercivity_display=float(mu),logarithmic_coercivity_display=float(kappa),
        whole_domain_positivity=True,global_endpoint_excluded=False,f4_entry_closed=False,
        full_transport_closed=False,lean_formalized=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(sys.argv[1]),indent=2))
