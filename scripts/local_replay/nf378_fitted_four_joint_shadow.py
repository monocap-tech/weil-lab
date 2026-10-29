#!/usr/bin/env python3
"""Exact-fraction original NF369 fitted E4 signed dual vs actual physical Gram.

Proves an UPPER on joint response inside the pre-fitted 4D shadow.
Not a full exterior signed residual or original Weil theorem.
"""
from fractions import Fraction as F
import argparse,hashlib,json
from pathlib import Path

SLICE_SHA='8148dfed729816d3af4a5ca20798f2a3454cfd99eb53621c8cd4646f24237df8'
PARENT_JSON='1b22cd77dd555749b8dcc41f92ddd91d982f2eca23ebf3a7638e512147b39d18'
PARENT_ZIP='1bacc7ae7967d1282eb28fd9d8566204eb21ba93246f6e81b174a18cc2ab1e96'
TNUM=[[1048576,-83468,750212,-2271087],[0,1048576,-1546322,-1621433],[0,0,1048576,1115405],[0,0,0,1048576]]

def dy(p):return F(int(p[0]))*F(2)**int(p[1])
def bound(z):
 m,r=dy(z[0]),dy(z[1]);assert r>=0
 return m-r,m+r

def plus(a,b):return a[0]+b[0],a[1]+b[1]
def prod(a,b):
 vals=[x*y for x in a for y in b]
 return min(vals),max(vals)
def neg(a):return -a[1],-a[0]
def sub(a,b):return plus(a,neg(b))
def mm(A,B):return [[fold([prod(A[i][k],B[k][j]) for k in range(len(B))]) for j in range(len(B[0]))] for i in range(len(A))]
def fold(terms):
 return sum((t[0] for t in terms),F(0)),sum((t[1] for t in terms),F(0))
def trans(A):return list(map(list,zip(*A)))
def inv(A):
 n=len(A);B=[[A[i][j] for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
 for col in range(n):
  pivot=B[col][col];assert pivot!=0
  B[col]=[x/pivot for x in B[col]]
  for row in range(n):
   if row!=col:
    fac=B[row][col]
    B[row]=[B[row][j]-fac*B[col][j] for j in range(2*n)]
 return [x[n:] for x in B]

def spd_pivots(A):
 n=len(A);M=[[x for x in row] for row in A];p=[]
 for i in range(n):
  piv=M[i][i];assert piv>0,piv
  p.append(piv)
  for j in range(i+1,n):
   for k in range(i+1,n):M[j][k]-=M[j][i]*M[i][k]/piv
  for j in range(i+1,n):M[j][i]=0
 return p

def run(path):
 raw=Path(path).read_bytes();assert hashlib.sha256(raw).hexdigest()==SLICE_SHA
 d=json.loads(raw);c=d['custody']
 assert c['original_nf369_json_sha256']==PARENT_JSON and c['original_nf369_zip_sha256']==PARENT_ZIP
 a=d['data']
 S_ball=[[bound(v) for v in row] for row in a['physical_quotient_Gram_native']]
 assert len(S_ball)==4 and all(len(row)==4 for row in S_ball)
 # Native balls for a symmetric exact Gram can have independently rounded
 # ij/ji entries. Their intersections still enclose the common true entry.
 for i in range(4):
  for j in range(i):
   a0,b0=S_ball[i][j],S_ball[j][i]
   z=(max(a0[0],b0[0]),min(a0[1],b0[1]));assert z[0]<=z[1]
   S_ball[i][j]=S_ball[j][i]=z
 M=[[(lo+hi)/2 for lo,hi in row] for row in S_ball]
 assert M==trans(M)
 piv=spd_pivots(M);M_inv=inv(M)
 assert all(sum((M[i][k]*M_inv[k][j] for k in range(4)),F(0))==F(i==j) for i in range(4) for j in range(4))
 norm_inv=max(sum((abs(v) for v in row),F(0)) for row in M_inv)
 radial=max(sum(((hi-lo)/2 for lo,hi in row),F(0)) for row in S_ball)
 eig_floor=1/norm_inv-radial
 assert eig_floor>0
 # This floor is for the actual original physical 4x4 native interval Gram.
 BP=[[bound(x) for x in row] for row in a['nf369_selected_to_original_quotient_signed_coupling_native']]
 CE=[[bound(x) for x in row] for row in a['actual_exterior_signed_Gram_native']]
 Y=[[(dy(x),dy(x)) for x in row] for row in a['nf369_quotient_response_exact_dyadic_coefficients']]
 T=[[(F(v,2**20),F(v,2**20)) for v in row] for row in TNUM]
 C=mm(CE,Y); R=mm([[sub(x,y) for x,y in zip(A,B)] for A,B in zip(trans(BP),C)],T)
 rows=[]
 for i in range(4):
  squared=sum((max(abs(R[k][i][0]),abs(R[k][i][1]))**2 for k in range(4)),F(0))
  upper=squared/eig_floor
  assert upper<F(1,10**100),('fitted response too large',i)
  rows.append({'direction':i+1,'certified_joint_fitted_four_projection_squared_lt':'1e-100',
    'certified_joint_fitted_four_projection_norm_lt':'1e-50',
    'actual_complete_original_fitted_four_coupling_interval_checked':True})
 assert eig_floor>F(1,10**240)
 assert radial<F(1,10**240)
 return dict(status='EXACT_RATIONAL_ORIGINAL_FITTED_FOUR_JOINT_SHADOW_SMALL_UPPER_ONLY',
  original_nf369_parent_json_sha256=PARENT_JSON,original_nf369_parent_zip_sha256=PARENT_ZIP,
  exact_original_nf369_slices_sha256=SLICE_SHA,
  original_selected_rank=242,original_fitted_exterior_rank=4,original_critical_directions=4,
  actual_native_physical_S4_interval_checked=True,exact_midpoint_spd_pivots_checked=True,
  exact_native_interval_Gram_lower_gt='1e-240',exact_Gram_entry_radius_row_sum_lt='1e-240',
  original_fitted_four_complete_signed_coupling_formula='R_E=(BP^T-CE*Y0)*T',
  original_fitted_four_joint_signed_projection=rows,
  original_full_exterior_witness_measured=False,
  original_full_exterior_signed_residual_certified=False,
  actual_source_adapted_unfitted_signed_coupling_computed=False,
  W_ODD_NEG='OPEN',RH='OPEN')

def main():
 p=argparse.ArgumentParser();p.add_argument('--slices',required=True);p.add_argument('--output',required=True)
 a=p.parse_args();obj=run(a.slices);Path(a.output).write_text(json.dumps(obj,indent=2)+'\n')
 print('PASS original fitted four JOINT signed dual norm <1e-50 in all four directions; unfitted response OPEN')
if __name__=='__main__':main()
