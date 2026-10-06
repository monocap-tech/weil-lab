"""Independent stored corrected sign, actual error and same-domain conversion audit."""
import hashlib,json,sys
from pathlib import Path
from certify_native_legendre_small_window import F,I,positive_pivots

def certificate(path,repeat):
    raw=Path(path).read_bytes();assert raw==Path(repeat).read_bytes();g=json.loads(raw)
    assert g['aperture']=='91/100' and g['corrected_schur_sign_certified'] is True
    root=Path(__file__).resolve().parents[1]/'notes/data'
    np=root/'RPB108_PRIME5_MATRIX84_091_COMPACT80_20261006.json'
    sp=root/'RPB108_PRIME5_SOURCE84_091_CERTIFICATE_20261006.json'
    cp=root/'RPB108_PRIME5_ITERATED_COMPLEMENT84_091_CERTIFICATE_20261006.json'
    native=json.loads(np.read_bytes());source=json.loads(sp.read_bytes());complement=json.loads(cp.read_bytes())
    assert hashlib.sha256(np.read_bytes()).hexdigest()==g['native_certificate_sha256']
    assert hashlib.sha256(sp.read_bytes()).hexdigest()==g['source_certificate_sha256']
    assert native['aperture']==source['aperture']==complement['aperture']=='91/100'
    c=F(317,500);beta=F(500,317)
    assert F(complement['physical_lower'])==c<F(complement['physical_unrounded_lower'])
    assert F(g['logarithmic_complement_lower'])==F(complement['logarithmic_lower'])==F(9,100)
    assert F(g['complement_inverse_factor'])==F(complement['complement_inverse_factor'])==beta
    assert g['panel_count']==9 and g['native_source_pairing_count']==7056
    assert g['projected_away_degrees']==g['physical_degrees']==list(range(84))
    assert g['all_mixed_terms_retained'] is True
    R=[[(F(lo),F(hi)) for lo,hi in row] for row in g['residual_gram_surrogate']]
    assert len(R)==84 and all(len(row)==84 for row in R)
    assert all(R[i][j]==R[j][i] and R[i][j][0]<=R[i][j][1] for i in range(84) for j in range(84))
    trace=sum((R[i][i][1] for i in range(84)),F(0));M=F(g['surrogate_residual_map_norm_upper'])
    assert M>=0 and M*M>=trace
    eta=F(source['source_map_error_upper']);delta=eta*(2*M+eta)
    assert delta==F(g['actual_gram_operator_error_upper'])
    triangle=native['lower_triangle_row_major'];assert len(triangle)==3570
    Q=[[None]*84 for _ in range(84)];index=0
    for i in range(84):
        for j in range(i+1):
            Q[i][j]=Q[j][i]=tuple(F(int(x),10**80) for x in triangle[index]);index+=1
    tau=F(g['corrected_coercivity_lower_bound']);assert tau>0
    assert len(g['shifted_pivot_lower_bounds'])==84 and min(map(F,g['shifted_pivot_lower_bounds']))>0
    old=I.grid;I.grid=10**100
    try:
        lower=[[I(*Q[i][j])-beta*I(*R[i][j]) for j in range(84)] for i in range(84)]
        for i in range(84):lower[i][i]-=beta*delta+tau
        pivots=positive_pivots(lower);assert len(pivots)==84 and min(p.lo for p in pivots)>0
        broken=[row[:] for row in lower];broken[0][0]=I(-1)
        try:positive_pivots(broken)
        except ArithmeticError:pass
        else:raise AssertionError('Negative diagonal accepted')
    finally:I.grid=old
    J=g['lift_operator_norm_integer_upper'];lift2=beta**2*(trace+delta)
    assert type(J) is int and J>0 and J*J>lift2==F(g['lift_norm_squared_upper'])
    mu=tau*c/(tau+c*(1+J*J));kappa=mu/(10*(mu+23))
    assert mu==F(g['whole_domain_physical_coercivity_lower'])>0
    assert kappa==F(g['logarithmic_coercivity_lower'])>0
    def determinant(x):return (tau-x*(1+J*J))*(c-x)-(x*J)**2
    assert determinant(mu)==mu*mu>0 and determinant(2*mu)<0
    return dict(aperture='91/100',certificate_sha256=hashlib.sha256(raw).hexdigest(),
        repeated_complete_outputs_identical=True,native_and_source_hashes_verified=True,
        complement_sha256=hashlib.sha256(cp.read_bytes()).hexdigest(),
        actual_error_and_residual_trace_recomputed=True,corrected_pivots_rechecked_at_100_digits=84,
        negative_diagonal_control_rejected=True,excessive_conversion_control_rejected=True,
        whole_domain_physical_coercivity_lower=str(mu),logarithmic_coercivity_lower=str(kappa),
        physical_coercivity_display=float(mu),logarithmic_coercivity_display=float(kappa),
        exact_conversion_determinant=str(mu*mu),whole_domain_positivity=True,
        global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)

if __name__=='__main__':print(json.dumps(certificate(sys.argv[1],sys.argv[2]),indent=2))
