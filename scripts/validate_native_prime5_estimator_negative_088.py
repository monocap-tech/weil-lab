"""Independent stored-vector audit: negative sufficient estimator, positive native energy."""
import hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I


def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    gp=root/'RPB108_PRIME5_GRAM84_088_CERTIFICATE_20261006.json'
    np=root/'RPB108_PRIME5_MATRIX84_088_COMPACT80_20261006.json'
    sp=root/'RPB108_PRIME5_SOURCE84_088_CERTIFICATE_20261006.json'
    g=json.loads(gp.read_bytes());native=json.loads(np.read_bytes())
    assert hashlib.sha256(np.read_bytes()).hexdigest()==g['native_certificate_sha256']
    assert hashlib.sha256(sp.read_bytes()).hexdigest()==g['source_certificate_sha256']
    assert g['aperture']==native['aperture']=='22/25'
    assert g['corrected_schur_sign_certified'] is False and g['actual_negative_witness'] is False
    v=list(map(F,g['estimator_negative_vector']));assert len(v)==84
    triangle=native['lower_triangle_row_major'];assert len(triangle)==3570
    R=g['residual_gram_surrogate'];assert len(R)==84 and all(len(row)==84 for row in R)
    assert all(R[i][j]==R[j][i] for i in range(84) for j in range(84))
    old=I.grid;I.grid=10**100
    try:
        q=I(0);residual=I(0);index=0
        for i in range(84):
            for j in range(i+1):
                weight=v[i]*v[j]*(1 if i==j else 2)
                q+=I(*(F(int(x),10**80) for x in triangle[index]))*weight;index+=1
                residual+=I(*(F(x) for x in R[i][j]))*weight
        norm=sum((x*x for x in v),F(0));assert norm>0 and q.lo>0
        delta=F(g['actual_gram_operator_error_upper']);beta=F(g['complement_inverse_factor'])
        assert beta==F(5,3)
        upper=(q-beta*residual).hi+beta*delta*norm
        assert upper<0
        required=(residual+I(-delta,delta)*norm)/q
        assert required.lo>F(3,5) and required.hi<F(619,1000)
        return dict(aperture='22/25',gram_sha256=hashlib.sha256(gp.read_bytes()).hexdigest(),
            independent_negative_estimator_verified=True,same_vector_native_energy_positive=True,
            native_rayleigh_interval=[str(q.lo/norm),str(q.hi/norm)],
            estimator_rayleigh_upper=str(upper/norm),required_complement_interval=[str(required.lo),str(required.hi)],
            actual_negative_full_form_witness=False,baseline_estimator_whole_domain_positivity=False,
            global_endpoint_excluded=False,f4_entry_closed=False,lean_formalized=False)
    finally:I.grid=old


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
