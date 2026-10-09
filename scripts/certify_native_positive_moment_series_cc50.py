"""Exact positive Legendre tail intervals and analytic-budget checks."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def doublefact(n):
    p=1
    for j in range(1,n+1,2):p*=j
    return p
def series(n,t,M=24):
    term=F(1); s=term
    for k in range(1,M+1):
        term*=t*t/F(2*k*(2*n+2*k+1));s+=term
    omitted=term*t*t/F(2*(M+1)*(2*n+2*(M+1)+1))
    return s,s+omitted/(1-F(1,1600))
def sqrtinterval(lo,hi,places=80):
    scale=10**places
    a=isqrt(lo.numerator*scale**2//lo.denominator)
    b=isqrt(hi.numerator*scale**2//hi.denominator)+1
    return F(a,scale),F(b,scale)
def encode(v):return {'numerator':str(v.numerator),'denominator':str(v.denominator)}
def run():
    count=0;rows=[];t=F(53,100);q=F(1,180000)
    def check(x):
        nonlocal count
        assert x
        count+=1
    for n in (112,113):
        check(t**4/F((2*n+1)*(2*n+3)**2*(2*n+5))<q*q)
        check(t*t/F(2*(2*n+3))<F(1,1600))
        for K,p in ((1,3),(6,27),(12,59)):
            b=q**K*((K+1)/(1-q)+q/(1-q)**2)+q**(2*K)/(2*(1-q*q)*(1-q)**2)
            check((10*n+13)*b*b<F(1,10**(2*p)))
        s0lo,s0hi=series(n,t)
        for k in range(12):
            m=n+2*k;slo,shi=series(m,t)
            factor=F(2*m+1,2*n+1)*t**(2*(m-n))*F(doublefact(2*n+1),doublefact(2*m+1))**2
            lo= factor*(slo/s0hi)**2;hi=factor*(shi/s0lo)**2
            a,b=sqrtinterval(lo,hi)
            check(a*a<=lo<=hi<=b*b)
            check(0<a<=b and b-a<=F(1,10**79))
            rows.append(dict(parity='even' if n==112 else 'odd',degree=m,
                             relative_coefficient_lower=encode(a),relative_coefficient_upper=encode(b)))
    return dict(stage='CC50 positive moment-tail series',all_passed=True,new_exact_checks=count,
                coefficient_series_terms=24,coefficient_rounding_grid='1e-80',
                normalized_D_truncation_bounds={'1':'1e-3','6':'1e-27','12':'1e-59'},
                coefficients=rows,native_response_evaluated=False,native_gate_certified=False,
                RH_proved=False,lean_certified=False,
                constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_POSITIVE_MOMENT_SERIES_CC50_CERTIFICATE_20261009.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='coefficients'},indent=2))
