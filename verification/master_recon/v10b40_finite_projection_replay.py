"""Independent exact projection of the degree-63 Taylor polynomial.
Checks finite rational identities; does not establish native orthogonality,
Taylor transport or custody of the original frozen archive.
"""
from fractions import Fraction as Q
from math import comb, factorial as f, prod, lcm
N=64
D=8**(N-1)*f(N-1)
# Integral coordinate z; T64 = sum (2z-1)^r/(8^r r!).
T=[sum((-1)**(r-k)*comb(r,k)*2**k*(D//(8**r*f(r)))
       for r in range(k,N)) for k in range(N)]
L=lcm(*range(1,2*N))
W=[L//(i+1) for i in range(2*N-1)]
def df(n): return prod(range(1,n+1,2))
C={}
for j in range(N):
    P=[(-1)**(j-i)*comb(j,i)*comb(j+i,i) for i in range(j+1)]
    got=Q((2*j+1)*sum(a*b*W[i+k] for i,a in enumerate(P)
                       for k,b in enumerate(T)),D*L)
    want=sum((Q(2*j+1,8**(j+2*m)*2**m*f(m)*df(2*j+2*m+1))
              for m in range((N-j+1)//2)),Q(0))
    assert got==want,(j,got,want)
    C[j]=got
# Reassemble Taylor polynomial exactly in the shifted Legendre basis.
R=[Q(0)]*N
for j,c in C.items():
    for i in range(j+1):
        R[i]+=c*(-1)**(j-i)*comb(j,i)*comb(j+i,i)
assert R==[Q(t,D) for t in T]
print('64/64 exact coefficient projections; 64/64 monomial reconstruction PASS')
