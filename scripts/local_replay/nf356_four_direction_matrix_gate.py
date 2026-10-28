#!/usr/bin/env python3
"""Exact rational verification: 4x4 retained variational lower matrix N_low.

Shows mu*H_phi - N_low > 1/500 I using FULL native dyadic interval
entry boxes for all possible retained matrices (not just sampled rays).
This is only a no-obstruction check: N_low <= B*B, not an upper bound.
"""
from fractions import Fraction as F
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))
import zipfile,hashlib,json,sys
sys.set_int_max_str_digits(100000)
archive=Path(str(CUSTODY_ROOT / 'pr355-exterior.zip')).read_bytes()
assert hashlib.sha256(archive).hexdigest()=='f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0'
with zipfile.ZipFile(str(CUSTODY_ROOT / 'pr355-exterior.zip')) as z:raw=z.read('original_exterior_scalar_floor_stop.json')
assert hashlib.sha256(raw).hexdigest()=='d853e2ecf665b8bb3978ee203371c07f67d050b79e7427d6c673331fd1d60ab9'
a=json.loads(raw)

def dy(x):return F(int(x[0]))*F(2)**int(x[1])
M=a['projected_strong_norm_variational_lower_matrix_native']
H=a['signed_energy_Gram_native']
mu=F(499,50000) # .00998 < independently rechecked conditional floor
n=len(M)
assert n==4
# Inputs are independently boxed entries and may be asymmetric at the
# last dyadic bit. The real underlying 4x4 matrices are symmetric. Intersect
# both native enclosures for off-diagonal entries, then symmetrize exactly.
lo=[[mu*(dy(H[i][j][0])-dy(H[i][j][1]))-(dy(M[i][j][0])+dy(M[i][j][1])) for j in range(n)] for i in range(n)]
hi=[[mu*(dy(H[i][j][0])+dy(H[i][j][1]))-(dy(M[i][j][0])-dy(M[i][j][1])) for j in range(n)] for i in range(n)]
C=[[F(0)]*n for _ in range(n)]
R=[[F(0)]*n for _ in range(n)]
for i in range(n):
 for j in range(i,n):
  a=max(lo[i][j],lo[j][i]);b=min(hi[i][j],hi[j][i]);assert a<=b,(i,j)
  C[i][j]=C[j][i]=(a+b)/2
  R[i][j]=R[j][i]=(b-a)/2
r=max(sum(row) for row in R)
# Prove C - (r + 1/500) I strictly positive using exact rational LDL.
S=[[C[i][j]-int(i==j)*(r+F(1,500)) for j in range(n)] for i in range(n)]
D=[];L=[[F(0) for _ in range(n)] for _ in range(n)]
for i in range(n):
  L[i][i]=F(1)
  d=S[i][i]-sum(L[i][k]*L[i][k]*D[k] for k in range(i))
  D.append(d)
  assert d>0, ('not positive at pivot',i,float(d))
  for j in range(i+1,n):
   L[j][i]=(S[j][i]-sum(L[j][k]*L[i][k]*D[k] for k in range(i)))/d
# Since ||Delta||_op <= maximum row sum of interval radius,
# exact C+rI encloses? Each actual matrix E bounded elementwise by R,
# therefore mu*H - N_low >= C - rI > (1/500)I.
print('Exact 4x4 matrix comparison PASS: mu*H_phi - N_low >1/500 I (mu=499/50000)')
print('max interval error row sum',float(r));print('exact LDL pivots floats',[float(x) for x in D])
report={
 'status':'EXACT_RATIONAL_NO_OBSTRUCTION_FOR_RETAINED_4x4_LOWER_MATRIX',
 'mu_conservative':'499/50000', 'matrix_gap_lower':'1/500',
 'exact_dyadic_radii_row_max':str(r),
 'ldl_pivots_c_minus_r_minus_1_over_500':[str(x) for x in D],
 'interpretation':'N_low is a LOWER bound to B*B. This proves ONLY that this 4x4 variational lower matrix does not refute the stronger floor. It does not prove B*B <=mu M.',
 'global_schur_positive_certified':False,'W_ODD_NEG':'OPEN','original_domain_review':'OPEN'
}
Path(str(CUSTODY_ROOT / 'nf356_four_direction_matrix_gate.json')).write_text(json.dumps(report,indent=2)+'\n')
