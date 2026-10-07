"""Conditional scalar Schur threshold; no complement or whole-domain claim."""
import hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I,positive_pivots



EXPECTED_HASHES = {'gram': '9eb9038963ffaaa8576cd39f51ae281d00840869c0d352a046cefbd70fc38e58', 'native': 'ca44a724478afa905e392f3bd3e728df45c9b000e6dd23d8fe84b0447c709329', 'source': '742e1e689d83098dac8bccbae4f32648beb95bab99d06e24f3e8016c535ab29d'}


def certificate():
    old=I.grid;I.grid=10**160
    try:
        root=Path(__file__).resolve().parents[1]/'notes/data'
        names={'gram':'RPB108_PRIME7_GRAM96_098_CERTIFICATE_20261007.json',
               'native':'RPB108_PRIME7_MATRIX96_098_COMPACT80_20261007.json',
               'source':'RPB108_PRIME7_SOURCE96_098_CERTIFICATE_20261007.json'}
        def read(name):
            p=root/name
            return p.read_bytes() if p.exists() else __import__('gzip').decompress(p.with_suffix('.json.gz').read_bytes())
        raw={key:read(name) for key,name in names.items()}
        hashes={key:hashlib.sha256(value).hexdigest() for key,value in raw.items()}
        assert hashes==EXPECTED_HASHES
        data={key:json.loads(value) for key,value in raw.items()};g=data['gram'];native=data['native'];source=data['source']
        assert g['source_certificate_sha256']==hashes['source'] and g['native_certificate_sha256']==hashes['native']
        assert g['aperture']==native['aperture']==source['aperture']=='49/50'
        assert g['physical_degrees']==g['projected_away_degrees']==list(range(96))
        assert g['native_source_pairing_count']==9216 and g['all_mixed_terms_retained']
        assert native['matrix_encoding']=='row-major lower triangle integer endpoints on grid 10^-80'
        triangle=native['lower_triangle_row_major'];assert len(triangle)==4656
        Q=[[None]*96 for _ in range(96)];index=0
        for i in range(96):
            for j in range(i+1):
                Q[i][j]=Q[j][i]=I(*(F(int(x),10**80) for x in triangle[index]));index+=1
        exactR=[[(F(lo),F(hi)) for lo,hi in row] for row in g['residual_gram_surrogate']]
        assert len(exactR)==96 and all(len(row)==96 for row in exactR)
        assert all(exactR[i][j]==exactR[j][i] and exactR[i][j][0]<=exactR[i][j][1] for i in range(96) for j in range(96))
        R=[[I(lo,hi) for lo,hi in row] for row in exactR]
        trace=sum((pair[1] for i,row in enumerate(exactR) for pair in [row[i]]),F(0))
        M=F(g['surrogate_residual_map_norm_upper']);assert M>0 and M*M>=trace
        eta=F(source['source_map_error_upper']);delta=eta*(2*M+eta)
        assert delta==F(g['actual_gram_operator_error_upper'])
        c=F(47,50);beta=1/c;tau=F(1,10**33)
        G=[[Q[i][j]-beta*R[i][j] for j in range(96)] for i in range(96)]
        for i in range(96):G[i][i]-=beta*delta+tau
        pivots=positive_pivots(G)
        return dict(status='conditional scalar threshold only; complement 47/50 is NOT proved',
            aperture='49/50',input_sha256=hashes,hypothetical_complement=str(c),
            interval_grid_digits=160,actual_gram_operator_error_upper=str(delta),
            shifted_margin=str(tau),shifted_pivot_lower_bounds=[str(x.lo) for x in pivots],
            all_96_corrected_pivots_positive=True,complement_proved=False,
            whole_domain_positivity_at_098=False,whole_domain_frontier='973/1000',f4_entry_closed=False)
    finally:I.grid=old
if __name__=='__main__':print(json.dumps(certificate(),indent=2))
