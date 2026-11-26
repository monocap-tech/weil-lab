#!/usr/bin/env python3
"""Exact rational geometry and conditional off-support gamma response bounds.
No evaluation of the choice-defined bump; no native Fourier-kernel attachment.
"""
from fractions import Fraction as F
import json
from pathlib import Path
N=665; a=F(11,10); h=2*a/N
collar=(F(4393,4000),F(4399,4000))
def log_bounds(p,m=80):
    t=F(p-1,p+1)
    s=2*sum((t**(2*j+1)/F(2*j+1) for j in range(m)),F(0))
    return s,s+2*t**(2*m+1)/((2*m+1)*(1-t*t))
def outward(lo,hi,den=10**12):
    return F((lo*den).__floor__(),den),F((hi*den).__ceil__(),den)
logs={n:outward(*log_bounds(n)) for n in (2,3,4,5,7,8,9)}
assert all(collar[0]+lo>a for lo,hi in logs.values())
shifted={n:(collar[0]-hi,collar[1]-lo) for n,(lo,hi) in logs.items()}
cells={j:(-a+j*h,-a+(j+1)*h) for j in range(1,N-1)}
excluded={j:[n for n,(lo,hi) in shifted.items() if l<=hi and lo<=r] for j,(l,r) in cells.items()}
pure=[j for j in cells if not excluded[j]]
assert len(pure)==654
def expneg(x,m=60):
    assert 0<=x<m+2
    term=F(1); s=term
    for j in range(1,m+1):
        term=term*x/j; s+=term
    tail=term*x/(m+1)/(1-x/F(m+2))
    return 1/(s+tail),1/s
# Conditional identity after three integrations by parts:
# h^4 int b(u) w(y) sum_{n>=1} [(2n+1/2)^3-(2n+1/2)/4]
#                   * exp(-(2n+1/2)*(y-x)) du dy.
# Lower n=1 only; upper via sum n^3 z^n=z(1+4z+z^2)/(1-z)^4.
def response_bounds(j,k,i):
    assert j in pure and 0<=i<k
    l,r=cells[j]
    yl=collar[0]+F(3*i,2000*k); yr=yl+F(3,2000*k)
    dmin=yl-r; dmax=yr-l
    assert dmin>0
    scale=h**4/F(2772*1000*k)
    lo=scale*15*expneg(F(5,2)*dmax)[0]
    z=expneg(2*dmin)[1]
    assert z<1
    hi=scale*F(125,8)*z*(1+4*z+z*z)/(1-z)**4
    assert 0<lo<=hi
    return outward(lo,hi,10**30)
picks=[pure[0],pure[len(pure)//4],pure[len(pure)//2],pure[3*len(pure)//4],pure[-1]]
result={"gate":"IV106-E18B","classification":"exact rational geometry; conditional gamma bounds, not native response certificates","frozen_research":"018f7e59f4129ce521cd3ae86d1afd59d3b64b5f","pure_count":len(pure),"excluded_cells":{str(j):ns for j,ns in excluded.items() if ns},"log_bounds":{str(n):list(map(str,b)) for n,b in logs.items()},"k1_bounds":{str(j):list(map(str,response_bounds(j,1,0))) for j in picks},"assumptions":["off-support digamma Fourier kernel identity","plateau integral via Fubini and normalized bump","E18A physical carrier attachment"],"not_claimed":["exact response row values","full kernel trial membership","native certification","Schur positivity"]}
if __name__=='__main__':
    assert json.loads(Path(__file__).with_name('pilot.json').read_text())==result
    print(json.dumps(result,indent=2))
    print("Exact rational conditional pilot replay PASS")
