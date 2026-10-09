#!/usr/bin/env python3
"""Exact finite polynomial identity used by the DNE13 numerical probe.

Checks D[P_n]=H_n P_n in scaled coordinates through degree 114.
This validates a finite polynomial action, not source integration errors.
"""
from fractions import Fraction as F
from math import comb
import json

def run():
    polys=[[F(1)],[F(0),F(1)]]
    for n in range(1,114):
        p=[F(0)]*(n+2)
        for k,v in enumerate(polys[-1]):p[k+1]+=(F(2*n+1,n+1))*v
        for k,v in enumerate(polys[-2]):p[k]-=F(n,n+1)*v
        polys.append(p)
    checks=0
    for n,p in enumerate(polys):
        result=[F(0)]*len(p)
        for m,c in enumerate(p):
            for k in range(m):
                result[m]+=c/F(k+1)
                if k%2:result[m-1-k]-=c/F(k+1)
        harmonic=sum((F(1,k) for k in range(1,n+1)),F(0))
        assert result==[harmonic*c for c in p]
        checks+=1
    return dict(status='PASS',exact_polynomial_identities=checks,
        maximum_degree=114,source_quadrature_certified=False)

if __name__=='__main__':print(json.dumps(run(),indent=2))
