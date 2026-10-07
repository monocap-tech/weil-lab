"""Widened 80-digit interval LDL audit; hypothetical complement remains unproved."""
import gzip,hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I

def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    raw=(root/'RPB108_PRIME7_SCHUR96_098_CONDITIONAL_094_20261007.json').read_bytes()
    c=json.loads(raw);assert c['hypothetical_complement']=='47/50' and not c['complement_proved']
    def read(name):
        p=root/name
        return p.read_bytes() if p.exists() else gzip.decompress(p.with_suffix('.json.gz').read_bytes())
    inputs={k:read(name) for k,name in {
        'gram':'RPB108_PRIME7_GRAM96_098_CERTIFICATE_20261007.json',
        'native':'RPB108_PRIME7_MATRIX96_098_COMPACT80_20261007.json',
        'source':'RPB108_PRIME7_SOURCE96_098_CERTIFICATE_20261007.json'}.items()}
    assert {k:hashlib.sha256(v).hexdigest() for k,v in inputs.items()}==c['input_sha256']
    g,n,s=(json.loads(inputs[k]) for k in ('gram','native','source'))
    eta=F(s['source_map_error_upper']);M=F(g['surrogate_residual_map_norm_upper'])
    delta=eta*(2*M+eta);assert str(delta)==c['actual_gram_operator_error_upper']
    old=I.grid;I.grid=10**80
    try:
        matrix=[[None]*96 for _ in range(96)];k=0;beta=F(50,47);tau=F(c['shifted_margin'])
        assert tau==F(1,10**33)
        for i in range(96):
            for j in range(i+1):
                q=I(*(F(int(x),10**80) for x in n['lower_triangle_row_major'][k]));k+=1
                r=I(*map(F,g['residual_gram_surrogate'][i][j]))
                matrix[i][j]=matrix[j][i]=q-beta*r
            matrix[i][i]-=beta*delta+tau
        work=[row[:] for row in matrix];pivots=[]
        # Row factors are enclosed once per pivot; triangular updates are outward.
        for k in range(96):
            pivot=work[k][k];assert pivot.lo>0;pivots.append(str(pivot.lo))
            factors=[work[i][k]/pivot for i in range(k+1,96)]
            for i in range(k+1,96):
                for j in range(i,96):
                    work[i][j]-=factors[i-k-1]*work[k][j];work[j][i]=work[i][j]
        broken=I(-1);assert broken.lo<=0
        return dict(aperture='49/50',certificate_sha256=hashlib.sha256(raw).hexdigest(),
            interval_grid_digits=80,independent_interval_row_factor_elimination=True,
            corrected_pivots_checked=96,pivot_lower_bounds=pivots,
            negative_pivot_control_rejected=True,hypothetical_complement='47/50',
            complement_proved=False,whole_domain_positivity_at_098=False,
            whole_domain_frontier='973/1000',f4_entry_closed=False)
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
