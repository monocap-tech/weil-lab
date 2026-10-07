"""Exact full prime-7 weighted Schur majorant at 973/1000."""
import bisect,gzip,hashlib,json
from pathlib import Path
import numpy as np
from certify_native_legendre_small_window import F,I,sqrt_rational
from certify_native_exact_logarithm import log_rational

STEPS=((1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,-1,0,0),(2,0,0,0),(-2,0,0,0),(0,0,1,0),(0,0,-1,0),(0,0,0,1),(0,0,0,-1))
def add(v,s):return tuple(x+y for x,y in zip(v,s))
def ratio(v):return F(2)**v[0]*F(3)**v[1]*F(5)**v[2]*F(7)**v[3]

def certificate():
    old=I.grid;I.grid=10**100
    try:
        a=F(973,1000);zero=(0,0,0,0)
        levels=[{zero}]
        for _ in range(8):levels.append({add(v,s) for v in levels[-1] for s in STEPS})
        states=set.union(*levels)
        refined=states|{add(v,s) for v in states for s in STEPS}
        offsets={v:log_rational(ratio(v),400) for v in refined}
        def cuts(vectors):
            out=[]
            for v in vectors:
                for sign in (-1,1):
                    x=I(sign*a)-offsets[v]
                    if v==zero or -a<x.lo<=x.hi<a:out.append((sign,v,x))
                    else:assert x.hi<-a or x.lo>a
            out.sort(key=lambda z:z[2].lo)
            assert out[0][2].lo==out[0][2].hi==-a and out[-1][2].lo==out[-1][2].hi==a
            assert all(x[2].hi<y[2].lo for x,y in zip(out,out[1:]))
            return out
        coarse=cuts(states);fine=cuts(refined)
        starts=[c[2].hi for c in coarse]
        def locate(x):
            k=bisect.bisect_right(starts,x.lo)-1
            assert 0<=k<len(coarse)-1 and coarse[k][2].hi<x.lo<=x.hi<coarse[k+1][2].lo
            return k
        logs={n:log_rational(F(n),400) for n in (2,3,5,7,8)}
        assert logs[7].hi<2*a<logs[8].lo
        amps=[logs[2]/sqrt_rational(F(2)),logs[3]/sqrt_rational(F(3)),logs[2]/2,logs[5]/sqrt_rational(F(5)),logs[7]/sqrt_rational(F(7))]
        amp_upper=[F((x.hi*10**30).__ceil__(),10**30) for x in amps]
        rows=[]
        for j,(left,right) in enumerate(zip(fine,fine[1:])):
            t=(left[2].hi+right[2].lo)/2;source=locate(I(t));edges=[]
            for step_index,s in enumerate(STEPS):
                y=I(t)+offsets[s]
                if -a<y.lo<=y.hi<a:edges.append([step_index,locate(y)])
                else:assert y.hi<-a or y.lo>a
            rows.append(dict(panel=j,source_cell=source,midpoint=str(t),edges=edges))
        size=len(coarse)-1;weights=np.ones(size)
        # Numerical search only. Every asserted bound below is rational.
        sources=np.array([row['source_cell'] for row in rows],dtype=int)
        edge_rows=np.array([i for i,row in enumerate(rows) for _ in row['edges']],dtype=int)
        targets=np.array([k for row in rows for _,k in row['edges']],dtype=int)
        factors=np.array([float(amp_upper[s//2]) for row in rows for s,_ in row['edges']])
        for _ in range(2000):
            values=np.bincount(edge_rows,weights=factors*weights[targets],minlength=len(rows))
            target=np.zeros(size);np.maximum.at(target,sources,values)
            target=target/target.max()
            weights=(weights/weights.max()+target)/2
        w=[F(max(1,round(float(x/weights.max())*10**12)),10**12) for x in weights]
        assert all(x>0 for x in w)
        ratios=[sum((amp_upper[s//2]*w[k] for s,k in row['edges']),F(0))/w[row['source_cell']] for row in rows]
        maximum=max(ratios);bound=F((maximum*10**6).__ceil__(),10**6)
        assert all(x<=bound for x in ratios)
        encode=lambda cs:[dict(sign=s,offset=list(v),interval=[str(x.lo),str(x.hi)]) for s,v,x in cs]
        return dict(aperture='973/1000',prime_powers=[2,3,4,5,7],step_vectors=[list(s) for s in STEPS],
            coarse_offset_depth=8,coarse_cuts=encode(coarse),refined_cuts=encode(fine),
            rational_cell_weights=[str(x) for x in w],weight_lower=str(min(w)),weight_upper=str(max(w)),
            amplitude_upper=[str(x) for x in amp_upper],refined_rows=rows,
            exact_weighted_row_ratios=[str(x) for x in ratios],maximum_weighted_row_ratio=str(maximum),
            joint_prime_operator_norm_upper=str(bound),joint_prime_operator_norm_upper_display=float(bound),
            method='positive weighted Schur: every supported translated-cell sum <= b times source-cell weight',
            numerical_candidate_search='2000 damped max-row iterations; floats are not proof evidence',
            finite_boundary_points_are_null_sets=True,interval_grid_digits=100,log_series_terms=400,
            whole_domain_positivity=False,actual_operator_norm_lower_claimed=False,f4_entry_closed=False,lean_formalized=False,
            constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
