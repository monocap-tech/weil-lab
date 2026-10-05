"""Certified limitation of uniform complement inverse factors on one actual Gram direction."""
import json,hashlib
from pathlib import Path
from certify_native_legendre_small_window import F,I

def certificate():
    old=I.grid;I.grid=10**200
    try:
        root=Path(__file__).resolve().parents[1]/'notes/data'
        gp=root/'RPB108_PRIME3_GRAM36_CERTIFICATE_20261005.json'
        r=json.loads(gp.read_text())
        n=json.loads((root/'RPB108_PRIME3_MATRIX36_CERTIFICATE_20261005.json').read_text())
        c=json.loads((root/'RPB108_PRIME3_COMPLEMENT36_CERTIFICATE_20261005.json').read_text())
        v=list(map(F,r['estimator_negative_vector']));norm=sum(x*x for x in v)
        Q=[[I(*x) for x in row] for row in n['matrix_intervals']]
        R=[[I(*x) for x in row] for row in r['residual_gram_surrogate']]
        q=sum((v[i]*Q[i][j]*v[j] for i in range(36) for j in range(36)),I(0))
        rr=sum((v[i]*R[i][j]*v[j] for i in range(36) for j in range(36)),I(0))
        err=F(r['actual_gram_operator_error_upper'])*norm
        b=1/F(c['physical_unrounded_lower']);upper=(q-b*rr).hi+b*err
        assert upper<0 and q.lo>0 and rr.lo>err
        threshold=q.hi/(rr.lo-err)
        assert threshold<F(357157,100000)
        return dict(unrounded_complement_inverse=str(b),same_vector_estimator_quadratic_upper=str(upper),
                    necessary_uniform_inverse_upper=str(threshold),actual_negative_witness=False,
                    raw_positive_control=True,gram_certificate_sha256=hashlib.sha256(gp.read_bytes()).hexdigest(),
                    whole_domain_positivity=False,global_endpoint_excluded=False,
                    f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
    finally:I.grid=old

if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
