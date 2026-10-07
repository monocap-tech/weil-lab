"""Persisted-source normalization, complete error aggregation and custody audit."""
import hashlib,json
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from certify_native_legendre_small_window import bernoulli

def certificate(path):
    def read(p):
        b=Path(p).read_bytes()
        return __import__('gzip').decompress(b) if str(p).endswith('.gz') else b
    raw=read(path)
    r=json.loads(raw);assert r['aperture']=='399/400'
    assert r['source_pi_machin_terms']==160
    assert r['exponential_order']==90 and r['bernoulli_pairs']==114 and r['gamma_order']==56
    assert r['prime_terms']==[2,3,4,5,7] and r['prime4_amplitude']=='log(2)/2'
    assert r['coefficient_encoding']=='integer numerators with common decimal denominator and row tail'
    assert r['coefficient_grid_digits']==40 and len(r['rows'])==112
    assert r['prime7_amplitude']=='log(7)/sqrt(7)'
    for name,digest in r['constructor_sha256'].items():assert hashlib.sha256((Path(__file__).parent/name).read_bytes()).hexdigest()==digest
    assert len(r['panel_endpoints'])==12 and len(r['panel_active_argument_shifts'])==11
    a=F(399,400);d=2*a;N=90;K=114
    B=bernoulli(2*K+2)
    coefficients=[abs(B[2*k]*(2*d)**(2*k)/factorial(2*k)) for k in range(1,K+1)]
    assert all(y<x for x,y in zip(coefficients,coefficients[1:]))
    assert all((B[2*k]>0)==(k%2==1) for k in range(1,K+1))
    assert (1+d+d*d/3)/2<F(9,4) and d/2<1 and d<3
    ce=F(9,4)*(d/2)**(N+1)/factorial(N+1)
    cb=4*(d/3)**(2*K+2)/(1-(d/3)**2)
    he=ce/(N+1)+cb/(2*K+2);ae=ce/(N+2)+cb/(2*K+3)
    exp_error=2*(d/4)**(N+1)/factorial(N+1)
    oldK=110;oldcb=4*(d/3)**(2*oldK+2)/(1-(d/3)**2)
    oldhe=ce/(N+1)+oldcb/(2*oldK+2);oldae=ce/(N+2)+oldcb/(2*oldK+3)
    old_total=sum(((2*n+1)*(2*oldhe+2*n*(n+1)*oldae+10*d*exp_error)**2 for n in range(112)),F(0))
    assert old_total>F(1,10**35)**2
    total=F(0);checked=0
    for n,row in enumerate(r['rows']):
        assert row['degree']==n and len(row['panels'])==11
        assert len(row['common_high_degree_numerators'])==N+2*K
        e=F(row['unnormalized_uniform_error']);en=F(row['normalized_uniform_error'])
        truncation=2*he+2*n*(n+1)*ae+10*d*exp_error
        assert e==truncation+max(F(p['coefficient_radius']) for p in row['panels'])
        assert e>0 and en>0 and en*en>=(2*n+1)*e*e
        total+=en*en
        for panel in row['panels']:
            assert len(panel['low_degree_numerators'])==n+1
            assert all(type(v) is int for v in panel['low_degree_numerators']+row['common_high_degree_numerators'])
            assert F(panel['coefficient_radius'])>=0
            assert e>=F(panel['coefficient_radius']);checked+=1
    eta=F(r['source_map_error_upper']);assert eta>0 and eta*eta>=total
    assert 0<eta<F(309,10**38)
    # A bound below the largest individual source error cannot bound the map.
    rejected=eta/100
    assert rejected*rejected<max(F(row['normalized_uniform_error'])**2 for row in r['rows'])
    assert r['whole_domain_positivity'] is False and r['actual_schur_sign_certified'] is False
    return dict(source_sha256=hashlib.sha256(raw).hexdigest(),
        source_git_blob_sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),
        aperture='399/400',fresh_source_aggregation_audited=True,
        physical_normalization_bounds_checked=112,coefficient_panels_checked=checked,
        complete_source_map_error_aggregation_verified=True,analytic_truncation_recomputed_for_all_112_rows=True,alternating_114_pair_kernel_budget_verified=True,obsolete_110_pair_budget_exceeds_1e_minus35=True,source_map_error_upper_display=float(eta),
        source_map_error_upper_below='309/10^38',underreported_map_error_rejected=True,
        full_residual_gram_certified=False,whole_domain_positivity=False,
        f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))

