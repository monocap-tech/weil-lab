"""Independent integer forward transfer, multinomial states and sixth-word cross-check."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from math import factorial,prod
from certify_native_legendre_small_window import I,sqrt_rational
from certify_native_exact_logarithm import log_rational

STEPS=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(2,0,0),(-2,0,0),(0,0,1),(0,0,-1))
def compositions(n,k):
    if k==1:yield (n,);return
    for first in range(n+1):
        for rest in compositions(n-first,k-1):yield (first,)+rest

def certificate(path,repeat):
    def read(p):
        p=Path(p)
        if not p.exists():p=p.with_suffix('.json.gz')
        raw=p.read_bytes()
        return __import__('gzip').decompress(raw) if p.suffix=='.gz' else raw
    raw=read(path);assert raw==read(repeat);c=json.loads(raw)
    assert c['aperture']=='19/20' and c['power']==10 and c['prime_powers']==[2,3,4,5]
    assert tuple(map(tuple,c['step_vectors']))==STEPS
    levels=[];counts=[]
    for k in range(11):
        level=set();words=0
        for multiplicities in compositions(k,8):
            v=tuple(sum(m*s[i] for m,s in zip(multiplicities,STEPS)) for i in range(3))
            level.add(v);words+=factorial(k)//prod(factorial(m) for m in multiplicities)
        assert words==8**k;levels.append(level);counts.append(words)
    assert levels==[set(map(tuple,x)) for x in c['reachable_levels']]
    states=set.union(*levels);old=I.grid;I.grid=10**140
    try:
        a=F(19,20);g=10**30
        def ratio(v):return F(2)**v[0]*F(3)**v[1]*F(5)**v[2]
        offsets={v:log_rational(ratio(v),450) for v in states}
        logs={n:log_rational(F(n),450) for n in (2,3,5,7)}
        assert logs[5].hi<2*a<logs[7].lo
        roots={n:sqrt_rational(F(n)) for n in (2,3,5)}
        actual_upper=[logs[2].hi/roots[2].lo,logs[3].hi/roots[3].lo,logs[2].hi/2,logs[5].hi/roots[5].lo]
        actual_lower=[logs[2].lo/roots[2].hi,logs[3].lo/roots[3].hi,logs[2].lo/2,logs[5].lo/roots[5].hi]
        amplitudes=list(map(F,c['amplitude_upper']));assert all(x>=y>0 for x,y in zip(amplitudes,actual_upper))
        upper=[int(x*g) for x in amplitudes];assert all(F(n,g)==x for n,x in zip(upper,amplitudes))
        lower=[(x*g).__floor__() for x in actual_lower]
        expected=set()
        for v in states:
            for sign in (-1,1):
                z=I(sign*a)-offsets[v]
                if v==(0,0,0) or -a<z.lo<=z.hi<a:expected.add((sign,v))
                else:assert z.hi<-a or z.lo>a
        assert expected=={(x['sign'],tuple(x['offset'])) for x in c['cuts']}
        assert len(expected)==len(c['cuts'])
        for cut in c['cuts']:
            z=I(cut['sign']*a)-offsets[tuple(cut['offset'])];lo,hi=map(F,cut['interval'])
            assert lo<=z.lo<=z.hi<=hi
        assert all(F(x['interval'][1])<F(y['interval'][0]) for x,y in zip(c['cuts'],c['cuts'][1:]))
        root=Path(__file__).resolve().parents[1]/'notes/data'
        parent_raw=(root/'RPB108_PRIME5_JOINT_POWER6_095_CERTIFICATE_20261007.json').read_bytes()
        parent=json.loads(parent_raw);assert parent['aperture']=='19/20' and parent['amplitude_upper']==c['amplitude_upper']
        maximum=F(0);max_lower=F(0);prefix_checks=0;retained_words=0
        assert len(c['panel_rows'])==len(c['cuts'])-1
        for panel,row in enumerate(c['panel_rows']):
            x=F(row['midpoint']);assert row['panel']==panel
            assert F(c['cuts'][panel]['interval'][1])<x<F(c['cuts'][panel+1]['interval'][0])
            support=set()
            for v,z in offsets.items():
                shifted=I(x)+z
                if -a<shifted.lo<=shifted.hi<a:support.add(v)
                else:assert shifted.hi<-a or shifted.lo>a
            assert support==set(map(tuple,row['supported_states']))
            vector={(0,0,0):(1,1,1)}
            for k in range(1,11):
                next_vector={}
                for v,(u,l,n) in vector.items():
                    for j,s in enumerate(STEPS):
                        w=tuple(v[i]+s[i] for i in range(3))
                        if w in support:
                            before=next_vector.get(w,(0,0,0))
                            next_vector[w]=(before[0]+u*upper[j//2],before[1]+l*lower[j//2],before[2]+n)
                vector=next_vector
                if k==6:
                    six=F(sum(z[0] for z in vector.values()),g**6)
                    matches=[i for i,(left,right) in enumerate(zip(parent['cuts'],parent['cuts'][1:]))
                             if F(left['interval'][1])<x<F(right['interval'][0])]
                    assert len(matches)==1
                    assert six==F(parent['panel_rows'][matches[0]]['row_mass_upper']);prefix_checks+=1
            mass=F(sum(z[0] for z in vector.values()),g**10)
            assert mass==F(row['row_mass_upper'])
            maximum=max(maximum,mass);max_lower=max(max_lower,F(sum(z[1] for z in vector.values()),g**10))
            retained_words+=sum(z[2] for z in vector.values())
        bound=F(c['joint_prime_operator_norm_upper'])
        assert maximum==F(c['maximum_tenth_power_row_mass_upper'])<bound**10==F(c['tenth_power_ceiling'])
        assert max_lower>(bound-F(1,1000))**10
        return dict(certificate_sha256=hashlib.sha256(raw).hexdigest(),byte_identical_repeat=True,
            multinomial_oriented_word_counts=counts,words_per_panel=8**10,panels_checked=len(c['panel_rows']),
            all_reachable_states_and_cuts_independently_verified=True,all_amplitudes_enclosed=True,
            exact_integer_forward_row_sums_equal=True,sixth_power_exhaustive_word_cross_checks=prefix_checks,
            sixth_power_certificate_sha256=hashlib.sha256(parent_raw).hexdigest(),
            surviving_oriented_words_across_panels=retained_words,joint_prime_norm_upper=str(bound),
            smaller_row_mass_ceiling_rejected=True,actual_operator_norm_lower_claimed=False,
            whole_domain_positivity=False,f4_entry_closed=False,lean_formalized=False)
    finally:I.grid=old

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
