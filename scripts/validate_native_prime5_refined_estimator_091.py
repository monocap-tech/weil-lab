"""Independent stored-vector audit: negative sufficient estimator, positive native energy."""
import hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I


def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    gp=root/'RPB108_PRIME5_GRAM84_091_CERTIFICATE_20261006.json'
    np=root/'RPB108_PRIME5_MATRIX84_091_COMPACT80_20261006.json'
    sp=root/'RPB108_PRIME5_SOURCE84_091_CERTIFICATE_20261006.json'
    cp=root/'RPB108_PRIME5_ITERATED_COMPLEMENT84_091_CERTIFICATE_20261006.json'
    g=json.loads(gp.read_bytes());assert gp.read_bytes()==Path(__import__('sys').argv[1]).read_bytes();native=json.loads(np.read_bytes())
    source=json.loads(sp.read_bytes());complement=json.loads(cp.read_bytes())
    assert hashlib.sha256(np.read_bytes()).hexdigest()==g['native_certificate_sha256']
    assert hashlib.sha256(sp.read_bytes()).hexdigest()==g['source_certificate_sha256']
    assert g['aperture']==native['aperture']=='91/100'
    assert g['corrected_schur_sign_certified'] is False and g['actual_negative_witness'] is False
    v=None
    triangle=native['lower_triangle_row_major'];assert len(triangle)==3570
    R=g['residual_gram_surrogate'];assert len(R)==84 and all(len(row)==84 for row in R)
    assert all(R[i][j]==R[j][i] for i in range(84) for j in range(84))
    assert g['native_source_pairing_count']==7056 and g['all_mixed_terms_retained'] is True
    assert g['projected_away_degrees']==list(range(84))
    trace=sum((F(R[i][i][1]) for i in range(84)),F(0))
    M=F(g['surrogate_residual_map_norm_upper']);assert M>=0 and M*M>=trace
    eta=F(source['source_map_error_upper'])
    assert eta*(2*M+eta)==F(g['actual_gram_operator_error_upper'])
    assert complement['aperture']=='91/100' and F(complement['physical_lower'])==F(317,500)
    raw_complement=F(complement['physical_unrounded_lower']);assert raw_complement>F(317,500)
    old=I.grid;I.grid=10**160
    try:
        c=F(634884730051433,10**15);assert F(317,500)<c<raw_complement
        beta=1/c
        from certify_native_prime5_gram84_091 import negative_candidate
        matrix=[[None]*84 for _ in range(84)];index=0
        for i in range(84):
            for j in range(i+1):
                native_entry=I(*(F(int(x),10**80) for x in triangle[index]));index+=1
                matrix[i][j]=matrix[j][i]=native_entry-beta*I(*(F(x) for x in R[i][j]))
        v=negative_candidate(matrix);assert v is not None and len(v)==84
        q=I(0);residual=I(0);index=0
        for i in range(84):
            for j in range(i+1):
                weight=v[i]*v[j]*(1 if i==j else 2)
                q+=I(*(F(int(x),10**80) for x in triangle[index]))*weight;index+=1
                residual+=I(*(F(x) for x in R[i][j]))*weight
        norm=sum((x*x for x in v),F(0));assert norm>0 and q.lo>0
        delta=F(g['actual_gram_operator_error_upper'])
        upper=(q-beta*residual).hi+beta*delta*norm
        assert upper<0
        required=(residual+I(-delta,delta)*norm)/q
        assert required.lo>raw_complement
        return dict(aperture='91/100',gram_sha256=hashlib.sha256(gp.read_bytes()).hexdigest(),
            independent_negative_estimator_verified=True,same_vector_native_energy_positive=True,
            tested_complement_lower=str(c),tested_inverse=str(beta),
            exact_negative_vector=[str(x) for x in v],
            tighter_rounding_alone_insufficient_for_audited_direction=True,
            native_rayleigh_interval=[str(q.lo/norm),str(q.hi/norm)],
            estimator_rayleigh_upper=str(upper/norm),required_complement_interval=[str(required.lo),str(required.hi)],
            required_complement_lower_display=float(required.lo),
            integrated_complement_unrounded_lower_display=float(raw_complement),
            direction_exceeds_current_certified_complement_lower=required.lo>raw_complement,
            complement_sha256=hashlib.sha256(cp.read_bytes()).hexdigest(),
            actual_source_error_correction_recomputed=True,all_84_projection_coordinates_verified=True,
            actual_negative_full_form_witness=False,baseline_estimator_whole_domain_positivity=False,
            global_endpoint_excluded=False,f4_entry_closed=False,lean_formalized=False)
    finally:I.grid=old


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
