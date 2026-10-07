"""Independent exhaustive four-step path sums and exact support-cut audit."""
import hashlib,json
from pathlib import Path
from itertools import product
from math import prod
from fractions import Fraction as F
from certify_native_legendre_small_window import I,sqrt_rational
from certify_native_exact_logarithm import log_rational

def certificate(path,repeat):
    raw=Path(path).read_bytes();assert raw==Path(repeat).read_bytes();c=json.loads(raw)
    assert c['aperture']=='47/50' and c['power']==4 and c['prime_powers']==[2,3,4,5]
    steps=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(2,0,0),(-2,0,0),(0,0,1),(0,0,-1)]
    assert list(map(tuple,c['step_vectors']))==steps
    words=list(product(range(8),repeat=4));paths=[];states={(0,0,0)};levels=[{(0,0,0)}]
    for k in range(1,5):
        level=set()
        for word in product(range(8),repeat=k):
            level.add(tuple(sum(steps[j][i] for j in word) for i in range(3)))
        levels.append(level);states|=level
    assert [set(map(tuple,v)) for v in c['reachable_levels']]==levels
    for word in words:
        v=(0,0,0);prefix=[]
        for j in word:
            v=tuple(v[i]+steps[j][i] for i in range(3));prefix.append(v)
        paths.append((word,prefix))
    old=I.grid;I.grid=10**140
    try:
        a=F(47,50)
        def ratio(v):return F(2)**v[0]*F(3)**v[1]*F(5)**v[2]
        offsets={v:log_rational(ratio(v),450) for v in states}
        logs={n:log_rational(F(n),450) for n in (2,3,4,5,7)}
        assert logs[5].hi<2*a<logs[7].lo
        roots={n:sqrt_rational(F(n)) for n in (2,3,5)}
        upper=[logs[2].hi/roots[2].lo,logs[3].hi/roots[3].lo,logs[2].hi/2,logs[5].hi/roots[5].lo]
        lower=[logs[2].lo/roots[2].hi,logs[3].lo/roots[3].hi,logs[2].lo/2,logs[5].lo/roots[5].hi]
        amplitudes=list(map(F,c['amplitude_upper']));assert all(v>=u>0 for v,u in zip(amplitudes,upper))
        expected=set()
        for v in states:
            for sign in (-1,1):
                z=I(sign*a)-offsets[v]
                if v==(0,0,0) or (-a<z.lo<=z.hi<a):expected.add((sign,v))
                else:assert z.hi<-a or z.lo>a
        actual={(p['sign'],tuple(p['offset'])) for p in c['cuts']}
        assert actual==expected and len(actual)==len(c['cuts'])
        for cut in c['cuts']:
            z=I(cut['sign']*a)-offsets[tuple(cut['offset'])];lo,hi=map(F,cut['interval'])
            assert lo<=z.lo<=z.hi<=hi
        assert all(F(x['interval'][1])<F(y['interval'][0]) for x,y in zip(c['cuts'],c['cuts'][1:]))
        products=[prod(amplitudes[j//2] for j in word) for word,_ in paths]
        lower_products=[prod(lower[j//2] for j in word) for word,_ in paths]
        maximum=F(0);max_lower=F(0);total=0
        assert len(c['panel_rows'])==len(c['cuts'])-1
        for panel,row in enumerate(c['panel_rows']):
            assert row['panel']==panel
            x=F(row['midpoint']);assert F(c['cuts'][panel]['interval'][1])<x<F(c['cuts'][panel+1]['interval'][0])
            supported=set()
            for v in states:
                z=I(x)+offsets[v]
                if -a<z.lo<=z.hi<a:supported.add(v)
                else:assert z.hi<-a or z.lo>a
            assert supported==set(map(tuple,row['supported_states']))
            good=[i for i,(_,prefix) in enumerate(paths) if all(v in supported for v in prefix)]
            exact=sum((products[i] for i in good),F(0))
            assert exact==F(row['row_mass_upper'])
            maximum=max(maximum,exact);max_lower=max(max_lower,sum((lower_products[i] for i in good),F(0)))
            total+=len(paths)
        bound=F(c['joint_prime_operator_norm_upper']);assert bound==F(15,8)
        assert maximum==F(c['maximum_fourth_power_row_mass_upper'])<bound**4==F(c['fourth_power_ceiling'])
        # This rejects the smaller row-mass ceiling; it is not a norm lower bound.
        assert max_lower>(bound-F(1,1000))**4
        return dict(certificate_sha256=hashlib.sha256(raw).hexdigest(),byte_identical_repeat=True,
            exhaustive_words=4096,panels_checked=len(c['panel_rows']),path_region_tests=total,
            all_reachable_levels_and_boundary_cuts_verified=True,all_amplitudes_enclosed=True,
            all_exact_row_sums_equal=True,maximum_row_mass=str(maximum),joint_prime_norm_upper='15/8',
            smaller_row_mass_ceiling_rejected=True,actual_operator_norm_lower_claimed=False,
            whole_domain_positivity=False,f4_closed=False,lean_formalized=False)
    finally:I.grid=old

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
