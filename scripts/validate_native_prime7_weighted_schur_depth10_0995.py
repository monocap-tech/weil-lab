"""Independent translated-cut coverage and exact weighted row inequality audit."""
import bisect,gzip,hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I,sqrt_rational
from certify_native_exact_logarithm import log_rational

STEPS=((1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,-1,0,0),(2,0,0,0),(-2,0,0,0),(0,0,1,0),(0,0,-1,0),(0,0,0,1),(0,0,0,-1))
def certificate(path,repeat):
    raw=Path(path).read_bytes();assert raw==Path(repeat).read_bytes();c=json.loads(raw)
    assert c['aperture']=='199/200' and c['prime_powers']==[2,3,4,5,7]
    assert c['step_vectors']==[list(x) for x in STEPS]
    old=I.grid;I.grid=10**140
    try:
        a=F(199,200);logs={n:log_rational(F(n),450) for n in (2,3,5,7,8)}
        assert logs[7].hi<2*a<logs[8].lo
        def offset(v):return v[0]*logs[2]+v[1]*logs[3]+v[2]*logs[5]+v[3]*logs[7]
        def decode(rows):
            out=[];keys=set()
            for row in rows:
                s=row['sign'];v=tuple(row['offset']);assert s in (-1,1) and len(v)==4
                key=(s,v);assert key not in keys;keys.add(key)
                x=I(s*a)-offset(v);lo,hi=map(F,row['interval'])
                assert lo<=x.lo<=x.hi<=hi
                if v==(0,0,0,0):assert x.lo==x.hi==s*a
                else:assert -a<x.lo<=x.hi<a
                out.append((key,x))
            assert out[0][1].lo==out[0][1].hi==-a and out[-1][1].lo==out[-1][1].hi==a
            assert all(x[1].hi<y[1].lo for x,y in zip(out,out[1:]))
            return out,keys
        coarse,coarse_keys=decode(c['coarse_cuts']);fine,fine_keys=decode(c['refined_cuts'])
        assert c['coarse_offset_depth']==10
        levels=[{(0,0,0,0)}]
        for _ in range(10):levels.append({tuple(x+y for x,y in zip(v,s)) for v in levels[-1] for s in STEPS})
        expected=set()
        for v in set.union(*levels):
            for sign in (-1,1):
                x=I(sign*a)-offset(v)
                if v==(0,0,0,0) or -a<x.lo<=x.hi<a:expected.add((sign,v))
                else:assert x.hi<-a or x.lo>a
        assert coarse_keys==expected
        # Independent refinement: all source-weight cuts, support boundaries,
        # and every coarse target cut pulled back by each actual translation.
        required=set(coarse_keys)
        for (s,v),_ in coarse:
            for step in STEPS:
                new=tuple(x+y for x,y in zip(v,step));x=I(s*a)-offset(new)
                if -a<x.lo<=x.hi<a:required.add((s,new))
                else:assert x.hi<-a or x.lo>a or x.lo==x.hi in (-a,a)
        assert required<=fine_keys
        essential=next(k for k in required if k not in coarse_keys)
        assert not required<=(fine_keys-{essential})
        starts=[x.hi for _,x in coarse]
        def locate(x):
            k=bisect.bisect_right(starts,x.lo)-1
            assert 0<=k<len(coarse)-1 and coarse[k][1].hi<x.lo<=x.hi<coarse[k+1][1].lo
            return k
        amplitudes=[logs[2]/sqrt_rational(F(2)),logs[3]/sqrt_rational(F(3)),logs[2]/2,logs[5]/sqrt_rational(F(5)),logs[7]/sqrt_rational(F(7))]
        upper=list(map(F,c['amplitude_upper']))
        lower=[F((x.lo*10**30).__floor__(),10**30) for x in amplitudes]
        assert all(0<lo<=amp.lo<=amp.hi<=hi for lo,amp,hi in zip(lower,amplitudes,upper))
        weights=list(map(F,c['rational_cell_weights']));assert len(weights)==len(coarse)-1
        assert min(weights)>0 and min(weights)==F(c['weight_lower']) and max(weights)==F(c['weight_upper'])
        bound=F(c['joint_prime_operator_norm_upper']);assert bound>0
        rows=c['refined_rows'];assert len(rows)==len(fine)-1
        max_upper=max_lower=F(0);transitions=0
        for i,row in enumerate(rows):
            assert row['panel']==i
            t=F(row['midpoint']);assert fine[i][1].hi<t<fine[i+1][1].lo
            source=locate(I(t));assert source==row['source_cell']
            edges=[]
            for j,step in enumerate(STEPS):
                y=I(t)+offset(step)
                if -a<y.lo<=y.hi<a:edges.append([j,locate(y)])
                else:assert y.hi<-a or y.lo>a
            assert edges==row['edges'];transitions+=10
            value=sum((upper[j//2]*weights[k] for j,k in edges),F(0))/weights[source]
            low=sum((lower[j//2]*weights[k] for j,k in edges),F(0))/weights[source]
            assert value==F(c['exact_weighted_row_ratios'][i])<=bound
            max_upper=max(max_upper,value);max_lower=max(max_lower,low)
        assert max_upper==F(c['maximum_weighted_row_ratio'])
        assert max_lower>bound-F(1,10**6)
        assert c['actual_operator_norm_lower_claimed'] is False and c['whole_domain_positivity'] is False
        return dict(certificate_sha256=hashlib.sha256(raw).hexdigest(),byte_identical_repeat=True,
            aperture='199/200',coarse_weight_cells=len(weights),refined_cells_checked=len(rows),
            actual_translated_cut_events_checked=len(required),every_source_support_and_target_event_covered=True,
            independent_linear_logarithm_enclosures=True,transitions_checked=transitions,
            all_exact_weighted_pointwise_inequalities_verified=True,weight_lower=str(min(weights)),
            norm_upper=str(bound),omitted_essential_translated_cut_rejected=True,
            smaller_pointwise_majorant_for_same_weight_rejected=True,actual_operator_norm_lower_claimed=False,
            finite_boundary_null_set_scope=True,whole_domain_positivity=False,f4_entry_closed=False,lean_formalized=False)
    finally:I.grid=old

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))


