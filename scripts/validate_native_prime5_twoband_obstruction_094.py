"""Independent exact rational quadratic audit; no floating-point search or interval class."""
import hashlib,json
from fractions import Fraction as F
from pathlib import Path

def certificate(path,repeat):
    raw=Path(path).read_bytes();assert raw==Path(repeat).read_bytes();p=json.loads(raw)
    root=Path(__file__).resolve().parents[1]/'notes/data'
    names={'gram':'RPB108_PRIME5_GRAM84_094_CERTIFICATE_20261007.json','native':'RPB108_PRIME5_MATRIX84_094_COMPACT80_20261007.json','source':'RPB108_PRIME5_SOURCE84_094_CERTIFICATE_20261007.json'}
    data={}
    for k,n in names.items():
        path=root/n
        b=path.read_bytes() if path.exists() else __import__('gzip').decompress(path.with_suffix('.json.gz').read_bytes())
        assert hashlib.sha256(b).hexdigest()==p['input_sha256'][k];data[k]=json.loads(b)
    g=data['gram'];native=data['native'];assert g['aperture']==native['aperture']==p['aperture']=='47/50'
    assert g['all_mixed_terms_retained'] and g['full_source_gram_certified'] and g['native_source_pairing_count']==7056
    v=list(map(F,p['rational_vector']));assert len(v)==84 and max(map(abs,v))==1
    Q=[[None]*84 for _ in range(84)];k=0
    for i in range(84):
        for j in range(i+1):Q[i][j]=Q[j][i]=tuple(F(int(x),10**80) for x in native['lower_triangle_row_major'][k]);k+=1
    R=[[tuple(map(F,x)) for x in row] for row in g['residual_gram_surrogate']]
    assert all(R[i][j]==R[j][i] and R[i][j][0]<=R[i][j][1] for i in range(84) for j in range(84))
    def exact_energy(matrix):
        lo=hi=F(0)
        for i in range(84):
            for j in range(84):
                w=v[i]*v[j];a,b=matrix[i][j]
                lo+=w*(a if w>=0 else b);hi+=w*(b if w>=0 else a)
        return lo,hi
    qlo,qhi=exact_energy(Q);rlo,rhi=exact_energy(R);norm=sum((x*x for x in v),F(0));assert qlo>0 and norm==F(p['vector_norm_squared'])
    M=F(g['surrogate_residual_map_norm_upper']);assert M*M>=sum((R[i][i][1] for i in range(84)),F(0))
    eta=F(data['source']['source_map_error_upper']);delta=eta*(2*M+eta);assert delta==F(g['actual_gram_operator_error_upper'])==F(p['actual_gram_operator_error_upper'])
    cp=root/'RPB108_PRIME5_POWER4_COMPLEMENT84_094_CERTIFICATE_20261007.json';cb=cp.read_bytes();assert hashlib.sha256(cb).hexdigest()==p['complement_certificate_sha256'];c=F(json.loads(cb)['physical_lower']);assert c==F(77,100)
    upper=qhi-rlo/c+delta*norm/c;assert upper<0 and upper<=F(p['estimator_quadratic_upper'])
    required=(rlo-delta*norm)/qhi;assert required>c and required>=F(p['required_scalar_complement_lower_bound'])
    assert qlo>=F(p['same_vector_native_quadratic_lower'])
    assert Q[0][0][1]-R[0][0][0]/c+delta/c>0
    assert p['actual_full_form_negative_witness'] is False and p['whole_domain_positivity'] is False
    return dict(aperture='47/50',obstruction_sha256=hashlib.sha256(raw).hexdigest(),obstruction_reproduced_byte_for_byte=True,
        exact_rational_quadratic_terms_checked=14112,exact_estimator_upper=str(upper),exact_estimator_rayleigh_upper_display=float(upper/norm),
        exact_required_scalar_complement_lower=str(required),exact_required_scalar_complement_lower_display=float(required),
        native_same_vector_strictly_positive=True,gram_error_budget_recomputed=True,nonnegative_coordinate_control_rejected_as_negative=True,
        negative_scalar_estimator_verified=True,actual_full_form_negative_witness=False,whole_domain_positivity=False,
        f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
