"""Independent support events and prime-7 coefficient jumps on both edge panels."""
import gzip,hashlib,json
from math import comb,isqrt
from pathlib import Path
from certify_native_legendre_small_window import F,I
from certify_native_exact_logarithm import log_rational

def certificate(path):
    raw=Path(path).read_bytes()
    if str(path).endswith('.gz'):raw=gzip.decompress(raw)
    c=json.loads(raw);assert c['aperture']=='399/400' and len(c['rows'])==112
    saved=I.grid;I.grid=10**500
    try:
        a=F(399,400);powers=(2,3,4,5,7)
        logs={n:log_rational(F(n),450) for n in powers};shifts={n:logs[n]/(2*a) for n in powers}
        cuts=[('0',I(0)),('1',I(1))]
        for n in powers:cuts.extend([(f'1-log({n})/(2a)',I(1)-shifts[n]),(f'log({n})/(2a)',shifts[n])])
        cuts.sort(key=lambda x:x[1].lo)
        assert c['panel_endpoints']==[x[0] for x in cuts] and len(cuts)==12
        assert all(x[1].hi<y[1].lo for x,y in zip(cuts,cuts[1:]))
        active=[]
        for left,right in zip(cuts,cuts[1:]):
            t=(left[1].hi+right[1].lo)/2;row=[]
            for index,n in enumerate(powers):
                for sign in (1,-1):
                    y=I(t)+sign*shifts[n]
                    if 0<y.lo<=y.hi<1:row.append([index,sign])
                    else:assert y.hi<0 or y.lo>1
            active.append(row)
        assert active==c['panel_active_argument_shifts']
        assert set(map(tuple,active[0]))-set(map(tuple,active[1]))=={(4,1)}
        assert set(map(tuple,active[10]))-set(map(tuple,active[9]))=={(4,-1)}
        n=isqrt(7*I.grid**2);sqrt7=I(F(n,I.grid),F(n+1,I.grid));alpha=logs[7]/sqrt7
        denominator=10**40;profiles=coefficients=controls=0
        for n,row in enumerate(c['rows']):
            p=[(-1)**(n-j)*comb(n,j)*comb(n+j,j) for j in range(n+1)]
            assert len(row['panels'])==11
            for sign,edge,neighbor in [(1,0,1),(-1,10,9)]:
                x=sign*shifts[7];xp=[I(1)]
                for _ in range(n):xp.append(xp[-1]*x)
                expected=[-alpha*sum((p[j]*comb(j,k)*xp[j-k] for j in range(k,n+1)),I(0)) for k in range(n+1)]
                observed=[F(u-v,denominator) for u,v in zip(row['panels'][edge]['low_degree_numerators'],row['panels'][neighbor]['low_degree_numerators'])]
                allowance=F(row['panels'][edge]['coefficient_radius'])+F(row['panels'][neighbor]['coefficient_radius'])
                gap=sum((max(abs(v-e.lo),abs(v-e.hi)) for v,e in zip(observed,expected)),F(0))
                assert gap<=allowance
                assert abs(observed[-1])>allowance  # omission of the new profile is rejected
                profiles+=1;coefficients+=n+1;controls+=1
        assert profiles==controls==224 and coefficients==12656
        return dict(source_sha256=hashlib.sha256(raw).hexdigest(),aperture='399/400',
            independent_500_digit_logarithm_and_sqrt_enclosures=True,
            actual_support_events_and_all_11_panels_verified=True,signed_support_tests=110,
            independent_prime7_edge_profiles_checked=profiles,coefficient_jump_checks=coefficients,
            analytic_and_quantization_radii_retained=True,omitted_prime7_profile_controls_rejected=controls,
            whole_domain_positivity=False,complete_gram_pending=True,f4_entry_closed=False,lean_formalized=False)
    finally:I.grid=saved

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(sys.argv[1]),indent=2))

