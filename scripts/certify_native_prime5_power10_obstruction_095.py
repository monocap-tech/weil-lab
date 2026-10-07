"""Rational outward audit of a candidate obstruction to the scalar Schur estimate."""
import hashlib,json
from pathlib import Path
from decimal import Decimal,localcontext,ROUND_HALF_EVEN
from certify_native_legendre_small_window import F,I

EXPECTED={'gram':'64aea866d3ff9b7c2bd4db98324cd447301fb0d93b2610a1e8cd56c800c82c8b','native':'ff15a6c33d09e1439b51a53fcec686f51090fb1aba59d59dbbd49f29cff0410f','source':'bf4cb64eb0328add621d22a85f76c9d32bcf852d44a2d3b351ed238f9584b76e'}

def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    names={k:'RPB108_PRIME5_'+v+'_20261007.json' for k,v in {'gram':'GRAM84_095_CERTIFICATE','native':'MATRIX84_095_COMPACT80','source':'SOURCE84_095_CERTIFICATE'}.items()}
    def read(n):
        p=root/n
        return p.read_bytes() if p.exists() else __import__('gzip').decompress(p.with_suffix('.json.gz').read_bytes())
    raw={k:read(n) for k,n in names.items()};hashes={k:hashlib.sha256(v).hexdigest() for k,v in raw.items()};assert hashes==EXPECTED
    data={k:json.loads(v) for k,v in raw.items()};g=data['gram'];native=data['native']
    assert g['aperture']==native['aperture']==data['source']['aperture']=='19/20'
    assert g['native_certificate_sha256']==hashes['native'] and g['source_certificate_sha256']==hashes['source']
    cp=root/'RPB108_PRIME5_POWER10_COMPLEMENT84_095_CERTIFICATE_20261007.json';comp=json.loads(cp.read_bytes());c=F(comp['physical_lower']);assert c==F(399,500);beta=1/c
    q=[[None]*84 for _ in range(84)];index=0
    for i in range(84):
        for j in range(i+1):q[i][j]=q[j][i]=tuple(F(int(x),10**80) for x in native['lower_triangle_row_major'][index]);index+=1
    r=[[tuple(map(F,p)) for p in row] for row in g['residual_gram_surrogate']]
    delta=F(g['actual_gram_operator_error_upper']);eta=F(data['source']['source_map_error_upper']);M=F(g['surrogate_residual_map_norm_upper']);assert delta==eta*(2*M+eta)
    with localcontext() as ctx:
        ctx.prec=120
        def dec(x):return Decimal(x.numerator)/Decimal(x.denominator)
        # Probe a stronger scalar value only to locate a more informative
        # rational direction. Proof below still uses the pinned actual c.
        search_c=F(17,20);search_beta=1/search_c
        work=[[dec((q[i][j][0]+q[i][j][1]-search_beta*(r[i][j][0]+r[i][j][1]))/2) for j in range(84)] for i in range(84)]
        L=[[Decimal(int(i==j)) for j in range(84)] for i in range(84)];v=None
        for k in range(84):
            pivot=work[k][k]
            if pivot<=0:
                v=[Decimal(0)]*84;v[k]=Decimal(1)
                for i in range(k-1,-1,-1):v[i]=-sum((L[j][i]*v[j] for j in range(i+1,k+1)),Decimal(0))
                scale=max(map(abs,v));v=[F(int((x/scale*Decimal(10**40)).to_integral_value(rounding=ROUND_HALF_EVEN)),10**40) for x in v];break
            for i in range(k+1,84):
                L[i][k]=work[i][k]/pivot
                for j in range(i,84):work[i][j]-=work[i][k]*work[k][j]/pivot;work[j][i]=work[i][j]
        assert v is not None
    old=I.grid;I.grid=10**160
    try:
        def energy(matrix):return sum((v[i]*I(*matrix[i][j])*v[j] for i in range(84) for j in range(84)),I(0))
        Q=energy(q);R=energy(r);norm=sum((x*x for x in v),F(0));assert norm>0 and Q.lo>0
        upper=Q.hi-beta*R.lo+beta*delta*norm;assert upper<0
        required=(R.lo-delta*norm)/Q.hi;assert required>c
        assert required>search_c
        false_v=[F(0)]*84;false_v[0]=F(1)
        false_upper=q[0][0][1]-beta*r[0][0][0]+beta*delta;assert false_upper>0
        return dict(aperture='19/20',input_sha256=hashes,complement_certificate_sha256=hashlib.sha256(cp.read_bytes()).hexdigest(),
            candidate_generation='120-digit Decimal LDL search; no Decimal value is proof evidence',rational_vector=[str(x) for x in v],
            candidate_search_scalar=str(search_c),necessary_scalar_lower_above_search_value_verified=True,
            outward_interval_grid_digits=160,physical_complement_lower=str(c),complement_inverse_factor=str(beta),
            actual_gram_operator_error_upper=str(delta),vector_norm_squared=str(norm),
            estimator_quadratic_upper=str(upper),estimator_rayleigh_upper=str(upper/norm),estimator_rayleigh_upper_display=float(upper/norm),
            same_vector_native_quadratic_lower=str(Q.lo),same_vector_native_rayleigh_lower_display=float(Q.lo/norm),
            required_scalar_complement_lower_bound=str(required),required_scalar_complement_lower_display=float(required),
            nonnegative_coordinate_control_rejected_as_negative=True,negative_scalar_estimator_certified=True,
            actual_full_form_negative_witness=False,whole_domain_positivity=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
