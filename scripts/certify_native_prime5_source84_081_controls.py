"""Independent nine-panel polynomial jump controls for all 84 actual sources."""
import json,hashlib
from pathlib import Path
from certify_native_legendre_small_window import F,I,log_rational
from certify_native_prime3_matrix36 import precise_sqrt as sqrt_rational
from certify_native_endpoint_log_gram import shifted_legendre
from certify_native_prime5_source_codec import expand_sources


def evaluate(coefficients,t):
    value=I(0)
    for c in reversed(coefficients):value=value*t+F(c)
    return value


def certificate():
    old=I.grid;I.grid=10**400
    try:
        path=Path(__file__).resolve().parents[1]/'notes/data/RPB108_PRIME5_SOURCE84_081_CERTIFICATE_20261005.json'
        encoded=json.loads(path.read_text());source=expand_sources(encoded)
        assert source['aperture']=='81/100' and source['prime_terms']==[2,3,4,5]
        assert len(source['rows'])==84 and all(len(r['panels'])==9 for r in source['rows'])
        d=F(81,50);logs={n:log_rational(F(n),220) for n in (2,3,4,5)}
        ell={n:s/d for n,s in logs.items()}
        amp={n:logs[n]/sqrt_rational(F(n)) for n in (2,3,5)};amp[4]=logs[2]/2
        cuts=[I(0),I(1)-ell[5],I(1)-ell[4],I(1)-ell[3],ell[2],I(1)-ell[2],ell[3],ell[4],ell[5],I(1)]
        assert all(x.hi<y.lo for x,y in zip(cuts,cuts[1:]))
        changes=[(5,1,1),(4,1,1),(3,1,1),(2,-1,-1),(2,1,1),(3,-1,-1),(4,-1,-1),(5,-1,-1)]
        p=shifted_legendre(83);count=0;maximum=F(0)
        for row in source['rows']:
            degree=row['degree'];assert degree==count//8
            for k,(n,direction,sign) in enumerate(changes):
                t=I((cuts[k+1].lo+cuts[k+1].hi)/2)
                right=evaluate(row['panels'][k+1]['coefficients'],t)
                left=evaluate(row['panels'][k]['coefficients'],t)
                expected=sign*amp[n]*evaluate(p[degree],t+direction*ell[n])
                difference=right-left-expected
                error=max(abs(difference.lo),abs(difference.hi))
                assert error<2*F(row['unnormalized_uniform_error']),(degree,k)
                maximum=max(maximum,error);count+=1
        # On the constant row the first panel jump is exactly the missing A5 term.
        difference=evaluate(source['rows'][0]['panels'][1]['coefficients'],I(0))-evaluate(source['rows'][0]['panels'][0]['coefficients'],I(0))
        assert difference.lo>F(7,10) and difference.lo>2*F(source['rows'][0]['unnormalized_uniform_error'])
        return dict(aperture='81/100',source_count=84,actual_panel_count=9,all_adjacent_panel_jump_checks=count,
                    maximum_polynomial_jump_discrepancy_upper=str(maximum),
                    constant_row_prime5_omission_control_rejected=True,lossless_source_encoding_roundtrip_checked=True,
                    source_certificate_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                    full_residual_gram_certified=False,whole_domain_positivity=False,lean_formalized=False)
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
