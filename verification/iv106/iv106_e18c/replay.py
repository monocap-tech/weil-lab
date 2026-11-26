#!/usr/bin/env python3
"""Conditional response rank lower bounds; exact rational algebra, not native attachment."""
from fractions import Fraction as F
from math import ceil
import sys
sys.set_int_max_str_digits(0)
import json
from pathlib import Path
h=F(11,3325); a=F(11,10); L=F(4393,4000); width=F(3,2000)
# Use exactly the first k consecutive interior cells, disjoint from all shifts for k<=34.
def log_bounds(n,m=80):
    t=F(n-1,n+1)
    s=2*sum((t**(2*j+1)/F(2*j+1) for j in range(m)),F(0))
    return s,s+2*t**(2*m+1)/((2*m+1)*(1-t*t))
for n in [2,3,4,5,7,8,9]:
    lo,hi=log_bounds(n)
    assert L+lo>a
    assert -a+35*h<L-hi or L+width-lo<-a+h

def bound(k):
    assert 1<=k<=34
    q=width/k; ell=-a+h; d=L+q-ell
    lam=[F(2*n)+F(1,2) for n in range(1,k+1)]
    # e<3, e^u>=1+u for u>=0.
    weights=[h**4*(l**3-l/4)/F(2772*1000*k)/3**ceil(l*d) for l in lam]
    det=F(1)
    for w in weights: det*=w
    for p in range(k):
        for r in range(p+1,k):
            delta=lam[r]-lam[p]
            det*=delta*h*delta*q/3**ceil(lam[r]*q)
    assert det>0
    # integer-only decimal magnitude certificate: det >= 10**(-e).
    e=0
    while det*10**e<1: e+=1
    return {'k':k,'sign_after_row_reversal':1,'lower_bound_power_of_ten':-e,
            'numerator_digits':len(str(det.numerator)),'denominator_digits':len(str(det.denominator))}
result={'gate':'IV106-E18C','classification':'conditional exact rational determinant lower bound; no native attachment','cell_indices':'1..k','max_consecutive_k':34,'cases':[bound(k) for k in (1,2,3,4,8,16,32,34)],'premises':['off-support Fourier kernel transport','normalized plateau mass and identical translated packed profiles','E18A physical carrier attachment','Cauchy-Binet and Vandermonde expansion of finite truncations and determinant continuity'],'not_claimed':['native-certified response rank','explicit corrected trials','positive Schur matrix']}
if __name__=='__main__':
    path=Path(__file__).with_name('pilot.json')
    if path.exists(): assert json.loads(path.read_text())==result
    print(json.dumps(result,indent=2))
