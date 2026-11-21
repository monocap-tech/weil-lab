#!/usr/bin/env python3
"""CP002 exact-rational three-bump prime graph preflight (NOT Lean or a spectral certificate).
Every logarithm is bounded by a rigorous rational atanh series with tail.
"""
from fractions import Fraction as F

H = F(1, 2000)
A = F(1099, 1000)
CENTER = F(1, 5)
WINDOW = (F(-11, 10), F(11, 10))
OLD_LEFT = (F(-11, 10), F(-11, 10) + F(1, 500))
OLD_RIGHT = (F(11, 10) - F(1, 500), F(11, 10))
LOG9_LO, LOG9_HI = F(219722, 100000), F(219723, 100000)

def log_interval(n: int, terms: int = 64):
    assert n >= 2
    x = F(n - 1, n + 1)
    lo = sum((2*x**(2*k+1)/(2*k+1) for k in range(terms)), F(0))
    tail = 2*x**(2*terms+1)/((2*terms+1)*(1-x*x))
    return lo, lo+tail

def neg(a):
    return -a[1], -a[0]

def diff(a, b):
    return a[0]-b[1], a[1]-b[0]

def disjoint(a, b):
    return a[1] < b[0] or b[1] < a[0]

def strict_inside(a, b):
    return b[0] < a[0] and a[1] < b[1]

def closed_inside(a, b):
    return b[0] <= a[0] and a[1] <= b[1]

def check_radius(r):
    intervals = {"minus":(-A-H,-A+H), "plus":(A-H,A+H),
                 "central":(CENTER-r,CENTER+r)}
    assert strict_inside(intervals["minus"],OLD_LEFT)
    assert strict_inside(intervals["plus"],OLD_RIGHT)
    assert all(closed_inside(v,WINDOW) for v in intervals.values())
    assert all(disjoint(intervals[i],intervals[j]) for i,j in
               (("minus","plus"),("minus","central"),("plus","central")))
    only_edges=set()
    min_clearance=None
    checks=0
    for n in range(2,10):
        pos=log_interval(n)
        for sign, logn in ((1,pos),(-1,neg(pos))):
            for i, ai in intervals.items():
                for j, aj in intervals.items():
                    checks+=1
                    d=diff(ai,aj)
                    if disjoint(d,logn):
                        gap=logn[0]-d[1] if d[1]<logn[0] else d[0]-logn[1]
                        assert gap>0
                        min_clearance=gap if min_clearance is None else min(gap,min_clearance)
                    else:
                        assert d[0]<logn[0] and logn[1]<d[1], (r,n,i,j,sign)
                        only_edges.add((n,sign,i,j))
    assert only_edges=={(9,1,"plus","minus"),(9,-1,"minus","plus")}
    assert min_clearance>F(1,20)
    assert log_interval(10)[0]>F(11,5)
    assert LOG9_LO<log_interval(9)[0] and log_interval(9)[1]<LOG9_HI
    x0=F(-5493,5000)
    witness=(x0-F(1,20000),x0+F(1,20000))
    assert strict_inside(witness,intervals["minus"])
    assert strict_inside((witness[0]+LOG9_LO,witness[1]+LOG9_HI),intervals["plus"])
    assert witness[1]-witness[0]==F(1,10000)
    width=F(1,250)+2*r
    margin=F(7,10)-75*width
    expected=F(1,4) if r==F(1,1000) else F(1,10)
    assert margin==expected
    # This specific three-bump family occupies a STRICT subset of the old collars.
    # The support-length bound is weaker than its exact bump-shape L1 capacity.
    frozen_width=4*H+2*r
    assert frozen_width==(F(1,250) if r==F(1,1000) else F(3,500))
    assert log_interval(3)[1]<F(6,5), "Lambda(9)/sqrt(9)=log3/3 < 2/5"
    conditional_frozen_floor=F(11,10)-75*frozen_width-F(2,5)
    assert conditional_frozen_floor==(F(2,5) if r==F(1,1000) else F(1,4))
    # Common translation preserves support differences, not the fixed window.
    shift=F(1,50)
    shifted_diff=diff(tuple(v+shift for v in intervals["plus"]),
                      tuple(v+shift for v in intervals["minus"]))
    assert shifted_diff==diff(intervals["plus"],intervals["minus"])
    assert intervals["plus"][1]+shift>WINDOW[1]
    return checks, sorted(only_edges),width,margin,witness

if __name__=="__main__":
    assert F(2,5)-150*F(1,375)==0
    for r in (F(1,1000),F(1,500)):
        checks, edges,width,margin,witness=check_radius(r)
        print(f"r={r} | {checks} exact interval/log comparisons | edges={edges}")
        print(f"  excluded signed gaps > 1/20; original n>=10 cutoff; positive n9 witness={witness}")
        print(f"  total support width={width}, conditional margin={margin}")
    print("CP002 EXACT FRACTION PREFLIGHT PASS; NO LEAN/WEIL/SPECTRAL KERNEL CERTIFICATION")
