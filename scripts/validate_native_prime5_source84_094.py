"""Persisted-source normalization, complete error aggregation and custody audit."""
import hashlib,json
from pathlib import Path
from fractions import Fraction as F

def certificate(path,repeat):
    def read(p):
        b=Path(p).read_bytes()
        return __import__('gzip').decompress(b) if str(p).endswith('.gz') else b
    raw=read(path);assert raw==read(repeat)
    r=json.loads(raw);assert r['aperture']=='47/50'
    assert r['prime_terms']==[2,3,4,5] and r['prime4_amplitude']=='log(2)/2'
    assert r['coefficient_encoding']=='integer numerators with common decimal denominator and row tail'
    assert r['coefficient_grid_digits']==40 and len(r['rows'])==84
    total=F(0);checked=0
    for n,row in enumerate(r['rows']):
        assert row['degree']==n and len(row['panels'])==9
        e=F(row['unnormalized_uniform_error']);en=F(row['normalized_uniform_error'])
        assert e>0 and en>0 and en*en>=(2*n+1)*e*e
        total+=en*en
        for panel in row['panels']:
            assert len(panel['low_degree_numerators'])==n+1
            assert all(type(v) is int for v in panel['low_degree_numerators']+row['common_high_degree_numerators'])
            assert F(panel['coefficient_radius'])>=0
            assert e>=F(panel['coefficient_radius']);checked+=1
    eta=F(r['source_map_error_upper']);assert eta>0 and eta*eta>=total
    assert eta<F(2,10**36)
    # A bound below the largest individual source error cannot bound the map.
    rejected=eta/100
    assert rejected*rejected<max(F(row['normalized_uniform_error'])**2 for row in r['rows'])
    assert r['whole_domain_positivity'] is False and r['actual_schur_sign_certified'] is False
    return dict(source_sha256=hashlib.sha256(raw).hexdigest(),
        source_git_blob_sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),
        aperture='47/50',source_reproduced_byte_for_byte=True,
        physical_normalization_bounds_checked=84,coefficient_panels_checked=checked,
        complete_source_map_error_aggregation_verified=True,source_map_error_upper_display=float(eta),
        source_map_error_upper_below='2/10^36',underreported_map_error_rejected=True,
        full_residual_gram_certified=False,whole_domain_positivity=False,
        f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
