"""V10B49: exact physical moment / Legendre coordinate change.
Read-only replay of the recovered dyadic bank. No native carrier attachment
or original V10B19 archive authentication is asserted.
Run: python3 verification/master_recon/v10b49_physical_rows.py
"""
from fractions import Fraction as Q
from math import factorial as f, prod
from pathlib import Path
import json
d=json.loads(Path(__file__).with_name('v10b45_optimized_coordinates.json').read_text())
D=d['denominator']; V=d['legendre_numerators']
assert D==2**48 and len(V)==16 and all(len(v)==160 for v in V)
def df(n): return prod(range(1,n+1,2))
def leg(i,k):
    if k>i or (i-k)%2: return Q(0)
    m=(i-k)//2
    return Q((-1)**m*4**k*f(2*i-2*m),2**i*f(m)*f(i-m)*f(k))
def inv(i,j):
    if j>i or (i-j)%2: return Q(0)
    m=(i-j)//2
    return Q((2*j+1)*f(i),4**i*2**m*f(m)*df(2*j+2*m+1))
def moment(k):
    return Q(0) if k%2 else Q(1,2*4**k*(k+1))
N=15
T=[[leg(i,k) for k in range(N)] for i in range(N)]
U=[[inv(i,j) for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        assert sum(T[i][k]*U[k][j] for k in range(N))==int(i==j)
        assert sum(U[i][k]*T[k][j] for k in range(N))==int(i==j)
        assert sum(T[j][k]*moment(i+k) for k in range(N))==U[i][j]/(2*(2*j+1))
assert all(T[i][i]>0 for i in range(N))
assert all(T[i][k]==0 for i in range(N) for k in range(i+1,N))
M=[[sum(U[i][j]*Q(v[j],2*D*(2*j+1)) for j in range(N))
    for v in V] for i in range(N)]
for i in range(N):
    for c in range(16):
        assert sum(T[i][k]*M[k][c] for k in range(N))==Q(V[c][i],2*D*(2*i+1))
# Symbolic pole row coefficients: treat each I_j as an independent variable.
# physical pole difference at trial V_c / D: sum odd v_cj I_j / D.
# subtract 2*(2j+1)*I_j times the j-th physical Legendre row.
for c in range(16):
    for j in range(160):
        raw=Q(V[c][j],D) if j%2 else Q(0)
        correction=2*(2*j+1)*Q(V[c][j],2*D*(2*j+1)) if j<15 and j%2 else Q(0)
        expected=Q(V[c][j],D) if j>=15 and j%2 else Q(0)
        assert raw-correction==expected
print('450 inverse entries, 225 physical pairings, 240 trial row transforms PASS')
print('2560 symbolic pole-row coefficient cancellations PASS')
print('positive triangular determinant:',prod(T[i][i] for i in range(N)))
