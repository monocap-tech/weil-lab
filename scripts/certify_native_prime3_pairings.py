"""Same-vector source/native custody at a=11/20; no complement sign claim."""
import hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I,log_rational,mul,sqrt_rational
from certify_native_endpoint_log_gram import exact_log_data
from certify_native_coupled_schur import integral


def certificate():
    previous=I.grid;I.grid=10**120
    try:
        root=Path(__file__).resolve().parents[1]/'notes/data'
        paths=[root/'RPB108_PRIME3_SOURCE_CERTIFICATE_20261005.json',
               root/'RPB108_PRIME3_MATRIX_CERTIFICATE_20261005.json']
        source,native=[json.loads(p.read_text()) for p in paths]
        assert source['aperture']==native['aperture']=='11/20'
        assert source['prime_terms']==native['prime_terms']==[2,3]
        p,CL,_=exact_log_data(19,20)
        d=F(11,10);ell2=log_rational(F(2),220)/d;ell3=log_rational(F(3),220)/d
        cuts=[I(0),I(1)-ell3,I(1)-ell2,ell2,ell3,I(1)]
        assert all(cuts[i].hi<cuts[i+1].lo for i in range(5))
        Q=[[I(*x) for x in row] for row in native['matrix_intervals']]
        CS=[[I(0) for _ in range(20)] for _ in range(20)]
        for i,row in enumerate(source['rows']):
            assert len(row['panels'])==5
            for panel,entry in enumerate(row['panels']):
                poly=[F(x) for x in entry['coefficients']]
                for j in range(20):
                    CS[j][i]+=integral(mul(p[j],poly),cuts[panel],cuts[panel+1])
        largest=F(0)
        for i in range(20):
            for j in range(20):
                pairing=sqrt_rational(F((2*i+1)*(2*j+1)))*(CL[j][i]+CS[j][i])
                difference=pairing-Q[i][j]
                error=max(abs(difference.lo),abs(difference.hi))
                assert error<F(source['rows'][i]['normalized_uniform_error'])
                largest=max(largest,error)
        # Omitting prime 3 shifts the normalized constant-vector pairing by this gap.
        gap=2*log_rational(F(3))/sqrt_rational(F(3))*(I(1)-ell3)
        assert gap.lo>largest+F(source['rows'][0]['normalized_uniform_error'])
        return dict(status='certified all 400 actual source/native pairings at aperture 11/20',
                    aperture='11/20',prime_terms=[2,3],panel_count=5,
                    source_pairing_error_upper=str(largest),
                    omitted_prime3_constant_pairing_gap_lower=str(gap.lo),
                    omitted_prime3_control_rejected=True,
                    input_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
                    full_residual_gram_certified=False,complement_coercivity_certified=False,
                    whole_domain_positivity=False,actual_negative_witness=False,
                    f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
    finally:
        I.grid=previous


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
