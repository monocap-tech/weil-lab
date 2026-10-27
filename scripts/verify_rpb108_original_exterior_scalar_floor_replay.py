#!/usr/bin/env python3
"""Stdlib rational replay of physical residual probes and the scalar-floor stop.

Physical projection/coupling enclosures are rebuilt natively in CI. This
replay independently composes source energies, variational witnesses and
the four-probe inverse-action remainder from retained interval data.
"""
import hashlib,json,sys,time
from pathlib import Path
from fractions import Fraction as F
from math import factorial
sys.set_int_max_str_digits(100000)
def dy(v):return F(int(v[0]))*F(2)**int(v[1])
def ball(v):
 m,r=dy(v[0]),dy(v[1]);assert r>=0;return m-r,m+r
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[1],-x[0]
def sub(x,y):return add(x,neg(y))
def sc(x,a):return (a*x[0],a*x[1]) if a>=0 else (a*x[1],a*x[0])
def mul(x,y):
 a=[u*v for u in x for v in y];return min(a),max(a)
def div(x,y):
 assert not y[0]<=0<=y[1];return mul(x,(1/y[1],1/y[0]))
def square(x):return (0 if x[0]<=0<=x[1] else min(v*v for v in x),max(v*v for v in x))
def overlap(x,y):assert max(x[0],y[0])<=min(x[1],y[1])
def subset(x,y):assert y[0]<=x[0]<=x[1]<=y[1]
def sym(A):
 for i in range(4):
  for j in range(i):
   a,b=A[i][j],A[j][i];lo,hi=max(a[0],b[0]),min(a[1],b[1]);assert lo<=hi;A[i][j]=A[j][i]=(lo,hi)
 return A
def ldl_floor(A):
 L=[[(F(0),F(0)) for _ in range(4)] for _ in range(4)];d=[]
 for i in range(4):
  for j in range(i):
   x=A[i][j]
   for k in range(j):x=sub(x,mul(mul(L[i][k],L[j][k]),d[k]))
   L[i][j]=div(x,d[j])
  L[i][i]=(F(1),F(1));x=A[i][i]
  for k in range(i):x=sub(x,mul(square(L[i][k]),d[k]))
  assert x[0]>0;d.append(x)
 V=[[(F(0),F(0)) for _ in range(4)] for _ in range(4)]
 for i in range(4):
  V[i][i]=(F(1),F(1))
  for j in range(i):
   x=(F(0),F(0))
   for k in range(j,i):x=sub(x,mul(L[i][k],V[k][j]))
   V[i][j]=x
 norm=sum((max(map(abs,t))**2 for row in V for t in row),F(0));assert norm>0
 return min(x[0] for x in d)/norm

def variational(A,Z,Y):
 # Columns of Y give the exact coefficient vectors of the test functions.
 n=4;R=[[(F(0),F(0)) for _ in range(n)] for _ in range(n)];B=[[(F(0),F(0)) for _ in range(n)] for _ in range(n)]
 for i in range(n):
  for j in range(n):
   for k in range(n):R[i][j]=add(R[i][j],sc(A[i][k],Y[k][j]))
   R[i][j]=sub(R[i][j],Z[i][j])
 for i in range(n):
  for j in range(n):
   for k in range(n):
    B[i][j]=add(B[i][j],sc(Z[k][i],Y[k][j]));B[i][j]=add(B[i][j],sc(Z[k][j],Y[k][i]))
    for l in range(n):B[i][j]=sub(B[i][j],sc(A[k][l],Y[k][i]*Y[l][j]))
 return B,R

def main():
 start=time.monotonic();assert len(sys.argv)==7
 paths=sys.argv[1:];z,matrix,frame,rank,critical,mixed=[json.loads(Path(p).read_bytes()) for p in paths]
 def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
 for name,i in [('matrix',1),('frame',2),('rank',3),('critical',4),('mixed',5)]:assert z['input_sha256'][name]==sha(paths[i])
 assert z['input_sha256']['matrix']=='33b52b01e813982bd1a73b9bb81b0ca79f76e4bfd5af0821c4e13b4360bb40fa'
 assert z['input_sha256']['frame']=='e78c29dc930274e5522c665d073044a6de6ac1fee832cac65c13128f57fe80d4'
 assert z['input_sha256']['rank']==mixed['rank_input_sha256']=='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
 assert z['input_sha256']['critical']==mixed['critical_input_sha256']=='a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922'
 assert matrix['finite_selected_signed_positive_definite_certified'] and z['selected_rank']==242
 assert z['working_precision_bits']==4096 and mixed['working_precision_bits']==z['raw_mixed_precision_bits']==3072 and mixed['Laplace_terms']==z['raw_mixed_Laplace_terms']==384
 assert z['existing_critical_witness_count']==z['source_direction_count']==4 and z['flint_version']=='0.8.0'
 assert mixed['target_probes']==critical['exact_candidates']['probes'] and mixed['target_sine_frequencies']==critical['exact_candidates']['sine_frequencies']
 # Replay every refined raw entry and its complete prime/pole cross-check.
 expected=[];offset=0
 for j,((c,p),n) in enumerate(zip(rank['original_nodes'],rank['selected_multiplicities'])):
  for k in range(n):expected.append((offset+k,j,c,k))
  offset+=p
 expected.append((469,None,None,None));assert len(expected)==242 and offset==469
 rho=F(0)
 for row,meta in zip(mixed['rows'],expected):
  assert tuple(row[k] for k in ['original_source_index','cluster','center','order'])==meta and len(row['entries'])==4
  for t,e in enumerate(row['entries']):
   assert e['target_index']==t;parts=e['components_native'];v=add(add(ball(parts['arch']),ball(parts['prime'])),ball(parts['pole']))
   interval=tuple(map(F,e['signed_interval']));subset(v,interval);subset(ball(e['signed_native']),interval)
   for key in ['prime','pole']:overlap(ball(parts[key]),ball(e['independent_'+key+'_native']))
   rho=max(rho,dy(e['signed_native'][1]))
 assert rho==F(mixed['maximum_native_block_radius']) and rho>0
 for i in range(4):
  for j in range(4):subset(ball(mixed['target_signed_kernel_Gram_native'][i][j]),tuple(map(F,critical['complete_signed_Gram_intervals'][i][j])))
 x=F(7,10);assert sum((x**j/factorial(j) for j in range(5)),F(0))>2
 a=F(2*384)-F(1,4);n=int(a*F(11,5)/x);q=0
 while 2**(q+1)*2<a*F(63,64):q+=1
 assert n+q==mixed['Laplace_tail_exponent']==2420 and 2*F(2)**-n/(a*F(63,64))<F(2)**-2420==F(mixed['Laplace_tail_Cauchy_base_upper'])
 assert mixed['all_968_seven_prime_and_true_pole_cross_checks_passed'] and mixed['complete_mixed_entry_count']==968
 assert z['physical_frame_transform_sha256']==frame['exact_dyadic_frame_transform_sha256']==matrix['exact_dyadic_frame_transform_sha256']
 for key,nr in [('physical_frame_error_row_upper',242),('physical_quotient_normalized_error_row_upper',4),('exterior_floor_subtraction_preconditioned_error_row_upper',4),('signed_energy_error_row_upper',4)]:
  assert len(z[key])==nr and all(0<=F(t)<F(1,100) for t in z[key])
 assert len(z['householder_orthogonality_error_row_upper'])==242 and all(0<=F(t)<F(1,10**900) for t in z['householder_orthogonality_error_row_upper'])
 mu=F(1,1000)-F(rank['pruned_physical_complement_negative_upper']);assert mu==F(z['inherited_global_exterior_floor'])>F(98,10**5)
 # All source energies are recomposed from the actual retained full matrix.
 tri=matrix['finite_transformed_signed_matrix_upper_native'];M=[[None]*242 for _ in range(242)]
 for i,row in enumerate(tri):
  for j,t in enumerate(row):M[i][j]=M[j][i]=ball(t)
 P=[[dy(t) for t in row] for row in z['signed_energy_source_exact_dyadic_coefficients']];assert len(P)==242 and all(len(row)==4 for row in P)
 MP=[[(F(0),F(0)) for _ in range(4)] for _ in range(242)]
 for i in range(242):
  for t in range(4):
   mid=sum(((M[i][j][0]+M[i][j][1])/2*P[j][t] for j in range(242)),F(0));rad=sum(((M[i][j][1]-M[i][j][0])/2*abs(P[j][t]) for j in range(242)),F(0));MP[i][t]=(mid-rad,mid+rad)
 E=[[(F(0),F(0)) for _ in range(4)] for _ in range(4)]
 for i in range(4):
  for j in range(4):
   for k in range(242):E[i][j]=add(E[i][j],sc(MP[k][j],P[k][i]))
   overlap(E[i][j],ball(z['signed_energy_Gram_native'][i][j]))
 for i in range(4):assert sum((max(map(abs,sub(E[i][j],(F(int(i==j)),F(int(i==j)))))) for j in range(4)),F(0))<F(1,100)
 S=sym([[ball(t) for t in row] for row in z['physical_quotient_Gram_native']]);C=sym([[ball(t) for t in row] for row in z['actual_exterior_signed_Gram_native']]);Z=[[ball(t) for t in row] for row in z['actual_exterior_weak_coupling_native']]
 for i in range(4):
  for j in range(4):overlap(S[i][j],tuple(map(F,frame['physical_critical_quotient_Gram_intervals'][i][j])))
 sigma=ldl_floor(S);assert sigma>0
 # Independent rational positivity of C-mu S in the actual probe basis.
 ldl_floor([[sub(C[i][j],sc(S[i][j],mu)) for j in range(4)] for i in range(4)])
 Y=[[dy(t) for t in row] for row in z['exact_L2_variational_coefficients']];YC=[[dy(t) for t in row] for row in z['exact_complement_variational_coefficients']]
 L2,_=variational(S,Z,Y);G,RC=variational(C,Z,YC)
 rc2=sum((max(map(abs,t))**2 for row in RC for t in row),F(0));extra=rc2/(mu*sigma)
 clean_upper=(sum((G[i][i][1] for i in range(4)),F(0))+4*extra)/F(99,100)
 assert clean_upper<F(2,1000) and F(z['four_probe_Schur_energy_operator_upper'])<F(2,1000)
 assert F(z['physical_quotient_coefficient_floor'])==F(99,100)/F(z['physical_quotient_preconditioner_Frobenius_squared_upper'])
 assert F(z['four_probe_signed_coefficient_floor'])==mu*F(z['physical_quotient_coefficient_floor'])
 assert F(z['four_probe_Schur_remainder_operator_upper'])==F(z['four_probe_inverse_action_residual_Frobenius_squared_upper'])/F(z['four_probe_signed_coefficient_floor'])
 strict=[]
 for i,case in enumerate(z['cases']):
  assert case['direction']==i;qn=tuple(map(F,case['source_signed_energy_interval']));bn=tuple(map(F,case['projected_strong_norm_variational_interval']));gn=tuple(map(F,case['complementary_Schur_variational_interval']))
  overlap(E[i][i],qn);overlap(L2[i][i],bn);overlap(G[i][i],gn)
  assert F(case['complementary_Schur_fraction_lower'])==gn[0]/qn[1]
  assert F(case['four_probe_Schur_fraction_upper'])==(gn[1]+F(z['four_probe_Schur_remainder_operator_upper']))/qn[0]
  assert F(case['scalar_floor_budget_upper'])==mu*qn[1] and F(case['scalar_floor_violation_factor_lower'])==bn[0]/(mu*qn[1])
  if F(case['scalar_floor_violation_factor_lower'])>1:
   assert L2[i][i][0]>mu*E[i][i][1];strict.append(i)
 assert z['scalar_floor_strong_action_method_stopped']==bool(strict) and strict==[0,1,2]
 assert z['negative_extension_witness_found'] is False
 for key in ['complete_strong_action_computed','global_Schur_penalty_upper_computed','global_infinite_Schur_sign_certified','rounded_projection_treated_as_exact','selected_source_space_enlarged','new_original_witnesses_introduced','four_probe_upper_is_global_upper']:assert z[key] is False
 assert z['physical_residuals_are_exact_defining_projection'] is True
 assert z['W_ODD_NEG']==z['inherited_original_domain_review']=='OPEN'
 print('EXACT ACTUAL-EXTERIOR SCALAR-FLOOR STOP REPLAY PASS; violating axes',strict,'four-probe correction <0.002; GLOBAL correction not bounded; seconds',round(time.monotonic()-start,2))
if __name__=='__main__':main()
