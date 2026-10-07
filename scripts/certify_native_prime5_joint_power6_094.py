"""Exact sixth-power row-mass bound for all four actual prime translations."""
import hashlib,json
from functools import lru_cache
from pathlib import Path
from certify_native_legendre_small_window import F,I,sqrt_rational
from certify_native_exact_logarithm import log_rational

STEPS=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(2,0,0),(-2,0,0),(0,0,1),(0,0,-1))
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def ratio(v):return F(2)**v[0]*F(3)**v[1]*F(5)**v[2]

def certificate():
    old=I.grid;I.grid=10**100
    try:
        a=F(47,50);depth=6;zero=(0,0,0)
        logs={n:log_rational(F(n),400) for n in (2,3,4,5,7)}
        assert logs[5].hi<2*a<logs[7].lo
        def ceiling(x):return F((x*10**30).__ceil__(),10**30)
        amplitudes=[ceiling(logs[2].hi/sqrt_rational(F(2)).lo),
                    ceiling(logs[3].hi/sqrt_rational(F(3)).lo),
                    ceiling(logs[2].hi/2),ceiling(logs[5].hi/sqrt_rational(F(5)).lo)]
        weights=[amplitudes[j//2] for j in range(8)]
        levels=[{zero}]
        for _ in range(depth):levels.append({add(v,s) for v in levels[-1] for s in STEPS})
        states=set.union(*levels);offsets={v:log_rational(ratio(v),400) for v in states}
        cuts=[]
        for v in states:
            for sign in (-1,1):
                x=I(sign*a)-offsets[v]
                if v==zero:cuts.append((sign,v,x));continue
                if x.lo>-a and x.hi<a:cuts.append((sign,v,x))
                else:assert x.hi<-a or x.lo>a
        cuts.sort(key=lambda entry:entry[2].lo+entry[2].hi)
        assert cuts[0][2].lo==cuts[0][2].hi==-a
        assert cuts[-1][2].lo==cuts[-1][2].hi==a
        assert all(x[2].hi<y[2].lo for x,y in zip(cuts,cuts[1:]))
        rows=[];maximum=F(0)
        for index,(left,right) in enumerate(zip(cuts,cuts[1:])):
            midpoint=(left[2].hi+right[2].lo)/2
            supported={}
            for v in states:
                x=I(midpoint)+offsets[v]
                if -a<x.lo<=x.hi<a:supported[v]=True
                else:
                    assert x.hi<-a or x.lo>a;supported[v]=False
            @lru_cache(None)
            def mass(v,k):
                if not supported[v]:return F(0)
                if k==0:return F(1)
                return sum((w*mass(add(v,s),k-1) for s,w in zip(STEPS,weights)),F(0))
            value=mass(zero,depth);maximum=max(maximum,value)
            rows.append(dict(panel=index,midpoint=str(midpoint),row_mass_upper=str(value),
                supported_states=[list(v) for v in sorted(states) if supported[v]]))
        bound=F(917,500);assert maximum<bound**depth
        return dict(aperture=str(a),prime_powers=[2,3,4,5],power=depth,
            amplitude_upper=[str(x) for x in amplitudes],step_vectors=[list(x) for x in STEPS],
            reachable_levels=[list(map(list,sorted(level))) for level in levels],
            cuts=[dict(sign=sign,offset=list(v),interval=[str(x.lo),str(x.hi)]) for sign,v,x in cuts],
            panel_rows=rows,maximum_sixth_power_row_mass_upper=str(maximum),
            joint_prime_operator_norm_upper=str(bound),joint_prime_operator_norm_upper_display=float(bound),
            sixth_power_ceiling=str(bound**depth),all_finite_walks_retained=True,
            interval_grid_digits=100,log_series_terms=400,whole_domain_positivity=False,
            f4_closed=False,lean_formalized=False,
            script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
