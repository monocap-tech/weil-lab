"""V10B29 frozen trial conversion; input is V10B19 frozen_coefficients.json.
No floating point. Independent recurrence versus binomial comparison.
Usage: python v10b29_frozen_trials.py INPUT OUTPUT
Output includes physical monomial numerators (x in [0,1/2]).
No claim of native Lean certification.
"""
import hashlib,json,sys
from fractions import Fraction as Q
from math import comb
from pathlib import Path
p=Path(sys.argv[1]);d=json.loads(p.read_text());n=160;den=d['denominator']
digest=hashlib.sha256(p.read_bytes()).hexdigest()
assert digest=='bccbd53fd2e02cb887868f588ef7f8765e780086f7fabe748518d5685d7c7616'
assert den==2**48 and len(d['trial'])==16 and all(len(row)==n for row in d['trial'])
leg=[[1],[-1,4]]
for j in range(1,n-1):
    a,b=leg[j],leg[j-1];v=[0]*(j+2)
    for k,c in enumerate(a):
        v[k]-=(2*j+1)*c;v[k+1]+=4*(2*j+1)*c
    for k,c in enumerate(b):v[k]-=j*c
    assert all(x%(j+1)==0 for x in v)
    leg.append([x//(j+1) for x in v])
for j,a in enumerate(leg):
    assert a==[(-1)**(j-k)*comb(j,k)*comb(j+k,k)*2**k for k in range(j+1)]
rows=[]
for row in d['trial']:
    a=[sum(row[j]*leg[j][k] for j in range(k,n)) for k in range(n)]
    b=[2**k*sum(row[j]*(-1)**(j-k)*comb(j,k)*comb(j+k,k) for j in range(k,n)) for k in range(n)]
    assert a==b
    assert sum(a[k]*Q(1,2)**k for k in range(n))==sum(row)
    assert a[0]==sum((-1)**j*v for j,v in enumerate(row))
    rows.append(a)
out=Path(sys.argv[2])
out.write_text(json.dumps({'parent_sha256':digest,'denominator':den,'coordinate':'x in [0,1/2], Legendre argument 4*x-1','physical_monomial_numerators':rows,'legendre_numerators':d['trial'],'subtraction_numerators':d['subtraction']},indent=1)+'\n')
assert hashlib.sha256(out.read_bytes()).hexdigest()=='1fea00167929e3f5312c16dcd680154a34ead4b8934a520c7a23fd60e79e8c5f'
print('12880 basis coefficients, 2560 trial coefficients, 32 endpoints: exact PASS')
