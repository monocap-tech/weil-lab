"""Independent triangular exact-rational quadratic audit of the Schur witness."""
import gzip,hashlib,json
from fractions import Fraction as F
from pathlib import Path

def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    name='RPB108_PRIME7_SCHUR96_098_STRONGER_OBSTRUCTION_20261007.json'
    raw=(root/name).read_bytes();w=json.loads(raw)
    def read(name):
        p=root/name
        return p.read_bytes() if p.exists() else gzip.decompress(p.with_suffix('.json.gz').read_bytes())
    names={'gram':'RPB108_PRIME7_GRAM96_098_CERTIFICATE_20261007.json',
        'native':'RPB108_PRIME7_MATRIX96_098_COMPACT80_20261007.json',
        'source':'RPB108_PRIME7_SOURCE96_098_CERTIFICATE_20261007.json'}
    inputs={k:read(p) for k,p in names.items()}
    assert {k:hashlib.sha256(v).hexdigest() for k,v in inputs.items()}==w['input_sha256']
    g,n,s=(json.loads(inputs[k]) for k in ('gram','native','source'))
    v=list(map(F,w['rational_vector']));assert len(v)==96
    norm=sum(x*x for x in v);assert str(norm)==w['vector_norm_squared']
    qlo=qhi=rlo=rhi=F(0);index=0
    for i in range(96):
        for j in range(i+1):
            a,b=(F(int(x),10**80) for x in n['lower_triangle_row_major'][index]);index+=1
            x,y=map(F,g['residual_gram_surrogate'][i][j])
            assert g['residual_gram_surrogate'][i][j]==g['residual_gram_surrogate'][j][i]
            t=v[i]*v[j]*(1 if i==j else 2)
            qlo+=min(t*a,t*b);qhi+=max(t*a,t*b)
            rlo+=min(t*x,t*y);rhi+=max(t*x,t*y)
    assert list(map(str,(qlo,qhi)))==w['native_quadratic_enclosure']
    assert list(map(str,(rlo,rhi)))==w['residual_quadratic_enclosure']
    eta=F(s['source_map_error_upper']);M=F(g['surrogate_residual_map_norm_upper'])
    delta=2*eta*M+eta*eta;assert str(delta)==w['actual_gram_operator_error_upper']
    beta=F(100,93);upper=qhi-beta*rlo+beta*delta*norm
    assert str(upper)==w['actual_schur_quadratic_upper'] and upper<-F(9,10**30)
    needed=(rlo-delta*norm)/qhi;assert qlo>0 and needed>F(93317,100000)
    assert str(needed)==w['necessary_complement_lower']
    cp=read('RPB108_PRIME7_96_PREFLIGHT_098_CERTIFICATE_20261007.json')
    assert hashlib.sha256(cp).hexdigest()==w['complement_sha256']
    assert needed>F(json.loads(cp)['physical_unrounded_lower'])
    assert upper+norm>0
    return dict(aperture='49/50',witness_sha256=hashlib.sha256(raw).hexdigest(),
        triangular_terms_independently_checked=index,rational_quadratic_enclosures_match=True,
        source_error_perturbation_included=True,actual_schur_upper_display=float(upper),
        necessary_complement_lower_display=float(needed),unrounded_complement_insufficient=True,
        positive_shift_control_rejected=True,actual_negative_weil_form_claimed=False,
        whole_domain_positivity_at_098=False,whole_domain_frontier='973/1000',f4_entry_closed=False)

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
