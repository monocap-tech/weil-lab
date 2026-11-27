"""Exact centered monomial projection replay, independent of spherical recurrence.
Checks finite rational identities, not convergence or native Lean attachment.
"""
from fractions import Fraction as Q
from math import comb, factorial, prod, lcm
from pathlib import Path
import json
J,M=33,65
# z in [0,1], y=2z-1; P_j(y)=(-1)^j shiftedLegendre_j(z).
P=[[(-1)**(j-k)*comb(j,k)*comb(j+k,k) for k in range(j+1)] for j in range(J+1)]
Y=[[(-1)**(n-k)*comb(n,k)*2**k for k in range(n+1)] for n in range(M+1)]
D=lcm(*range(1,J+M+2))
W=[D//(k+1) for k in range(J+M+1)]
def pair(a,b):
    return Q(sum(x*y*W[i+k] for i,x in enumerate(a) for k,y in enumerate(b)),D)
def odd_df(n): return prod(range(1,n+1,2))
checks=0; zero=0
for j,p in enumerate(P):
    for n,y in enumerate(Y):
        got=pair(p,y)
        if n<j or (n-j)%2:
            expect=Q(0);zero+=1
        else:
            m=(n-j)//2
            expect=Q(factorial(n),2**m*factorial(m)*odd_df(2*j+2*m+1))
        assert got==expect,(j,n,got,expect)
        checks+=1
orth=0
for j,p in enumerate(P):
    for k in range(j+1):
        assert pair(p,P[k])==(Q(1,2*j+1) if j==k else Q(0))
        orth+=1
# Reconstruct the exact inner 17-term spherical series from projections.
coeff={}
for j in range(15,34,2):
    a=sum(((2*j+1)*pair(P[j],Y[j+2*m])*Q(1,8**(j+2*m)*factorial(j+2*m)) for m in range(17)),Q(0))
    term=Q(1,8**j*odd_df(2*j+1)); s=term
    for m in range(1,17):
        term/=128*m*(2*j+2*m+1);s+=term
    assert a==(2*j+1)*s
    coeff[j]=a
c={j:v/coeff[15] for j,v in coeff.items()}
assert c[15]==1 and all(c[j+2]/c[j]<=Q(1,64*(2*j+1)*(2*j+3)) for j in range(15,33,2))
out={'monomial_projection_checks':checks,'zero_projections':zero,'orthogonality_checks':orth,'spherical_partial_sum_checks':len(c),'normalized_ratio_checks':len(c)-1,'normalized_coefficients':{str(j):str(v) for j,v in c.items()},'status':'exact finite arithmetic PASS; analytic series and literal attachment outstanding'}
Path(__file__).with_name('legendre_projection_result.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k!='normalized_coefficients'})
