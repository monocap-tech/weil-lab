#!/usr/bin/env python3
"""Exact matched-forcing finite Schur ledger and independent Cauchy replay.

Native physical and signed-kernel congruences are rebuilt separately in CI.
"""
import hashlib,json,sys,time
from pathlib import Path
from fractions import Fraction as F
from math import factorial
sys.set_int_max_str_digits(100000)
from verify_rpb108_original_signed_critical_mixed_replay import ball,dy,cball,cadd,cmul,cpow,scale,intersects

def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[1],-x[0]
def sub(x,y):return add(x,neg(y))
def sc(x,a):return (a*x[0],a*x[1]) if a>=0 else (a*x[1],a*x[0])
def mul(x,y):
 v=[a*b for a in x for b in y];return min(v),max(v)
def div(x,y):
 assert not y[0]<=0<=y[1];return mul(x,(1/y[1],1/y[0]))
def square(x):return (0 if x[0]<=0<=x[1] else min(x[0]**2,x[1]**2),max(x[0]**2,x[1]**2))
def pivots(M):
 L=[[F(0)]*4 for _ in range(4)];d=[]
 for i in range(4):
  for j in range(i):
   if d[j][0]<=0<=d[j][1]:return None
   value=M[i][j]
   for k in range(j):value=sub(value,mul(mul(L[i][k],L[j][k]),d[k]))
   L[i][j]=div(value,d[j])
  L[i][i]=(F(1),F(1));value=M[i][i]
  for k in range(i):value=sub(value,mul(square(L[i][k]),d[k]))
  d.append(value)
 return d

def main():
 start=time.monotonic();assert len(sys.argv)==8
 paths=sys.argv[1:];z,v,frame,rank,budget,block,candidate=[json.loads(Path(p).read_bytes()) for p in paths]
 def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
 for name,index in [('frame',2),('rank',3),('budget',4),('block',5),('candidate',6)]:assert z['input_sha256'][name]==sha(paths[index])
 assert z['input_sha256']['frame']=='e78c29dc930274e5522c665d073044a6de6ac1fee832cac65c13128f57fe80d4'
 assert z['input_sha256']['rank']=='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
 assert z['input_sha256']['budget']=='eececa96d8db2ab1625c79bf3a13d2ce14d2de97c921c9dec967834281f16e90'
 assert z['input_sha256']['block']=='2cb869033f2c6722d356e769f35fc0e1b041ae46a8c11360e66cd7d2c694c548'
 assert v['matrix_sha256']==sha(paths[0]);assert z['raw_working_precision_bits']==3072 and z['Laplace_terms']==384 and z['flint_version']=='0.8.0'
 assert z['selected_rank']==242 and z['complete_upper_triangle_entries']==z['all_prime_pole_physical_cross_checks']==242*243//2 and z['complete_real_matrix_entries']==242**2
 ns=[n for n in rank['selected_multiplicities'] if n]+[1];assert sum(ns)==242
 assert z['coincident_block_diagonal_checks']==len(ns) and z['distinct_one_variable_coefficient_checks']==3*sum(i*n for i,n in enumerate(ns))
 assert z['maximum_required_I_jet_order']==2*max(ns)-1==27
 # Elementary generalized omitted-tail proof.
 x=F(7,10);assert sum((x**j/factorial(j) for j in range(5)),F(0))>2
 alpha=F(2*z['Laplace_terms'])-F(1,4);m=int(alpha*F(11,5)/x);q=0
 while 2**(q+1)*2<alpha*F(63,64):q+=1
 assert alpha*F(11,5)>=m*x and F(22,5)>6*x
 assert 2*F(2)**-m/(alpha*F(63,64))<F(2)**-(m+q)==F(z['raw_Laplace_tail_upper'])
 assert z['Laplace_tail_exponent']==m+q==2420 and z['Cauchy_radius']=='1/4' and z['analytic_tail_strip_imaginary_bound']=='3/4'
 assert z['exact_dyadic_frame_transform_sha256']==frame['exact_dyadic_frame_transform_sha256']
 assert len(z['physical_frame_error_row_upper'])==242 and all(0<=F(t)<F(1,100) for t in z['physical_frame_error_row_upper'])
 assert F(z['frame_Frobenius_norm_upper'])<F(2)**496
 rho=F(z['maximum_raw_entry_radius']);assert 0<=rho
 assert F(z['double_frame_uniform_error_Frobenius_squared_upper'])==F(2)**1984*242**2*rho**2<F(2)**-160
 assert z['diagnostic_transport_target_bits']==80 and z['diagnostic_target_is_Schur_budget'] is False
 assert len(z['householder_vectors'])==4
 for j,w in enumerate(z['householder_vectors']):
  assert w['start']==j and len(w['vector'])==242-j and sum((dy(t)**2 for t in w['vector']),F(0))>0
 assert len(z['householder_orthogonality_error_row_upper'])==242 and all(0<=F(t)<F(1,10**900) for t in z['householder_orthogonality_error_row_upper'])
 # Unconditional exact orthogonality of each H=I-2vv^t/(v^tv) follows
 # from each nonzero exact dyadic v, independently of its eigenvector origin.
 tri=z['finite_transformed_signed_matrix_upper_native'];assert len(tri)==242 and all(len(row)==i+1 for i,row in enumerate(tri))
 M=[[None]*242 for _ in range(242)]
 for i,row in enumerate(tri):
  for j,t in enumerate(row):M[i][j]=M[j][i]=ball(t)
 native_radius2=sum((dy(t[1])**2*(1 if i==j else 2) for i,row in enumerate(tri) for j,t in enumerate(row)),F(0))
 assert native_radius2<=F(z['native_matrix_radius_Frobenius_squared_upper'])<F(2)**-160
 assert z['finite_complement_dimension']==238 and len(z['finite_complement_preconditioned_error_row_upper'])==238
 assert all(0<=F(t)<F(1,100) for t in z['finite_complement_preconditioned_error_row_upper'])
 invtrace=F(z['finite_complement_preconditioner_Frobenius_squared_upper']);gamma=F(z['finite_complement_coefficient_floor']);assert invtrace>0 and gamma==F(99,100)/invtrace>0
 Y=[[dy(t) for t in row] for row in z['matched_exact_dyadic_inverse_action_candidate']];assert len(Y)==238 and all(len(row)==4 for row in Y)
 # Independently compose H Y and the residual in exact dyadic intervals.
 Z=[[(F(0),F(0)) for _ in range(4)] for _ in range(238)];r2=F(0)
 for i in range(238):
  for t in range(4):
   mid=sum(((M[i+4][j+4][0]+M[i+4][j+4][1])/2*Y[j][t] for j in range(238)),F(0))
   rad=sum(((M[i+4][j+4][1]-M[i+4][j+4][0])/2*abs(Y[j][t]) for j in range(238)),F(0));Z[i][t]=(mid-rad,mid+rad)
   residual=sub(Z[i][t],M[i+4][t]);r2+=max(map(abs,residual))**2
 assert r2<=F(z['matched_forcing_residual_Frobenius_squared_upper'])
 penalty=F(z['finite_Schur_remainder_operator_upper']);assert penalty==F(z['matched_forcing_residual_Frobenius_squared_upper'])/gamma
 U=[[M[i][j] for j in range(4)] for i in range(4)]
 for i in range(4):
  for j in range(4):
   for k in range(238):
    U[i][j]=sub(U[i][j],sc(M[k+4][i],Y[k][j]));U[i][j]=sub(U[i][j],sc(M[k+4][j],Y[k][i]));U[i][j]=add(U[i][j],sc(Z[k][j],Y[k][i]))
   intersects(U[i][j],ball(z['finite_Schur_upper_native'][i][j]))
 lower=[[sub(U[i][j],(penalty,penalty)) if i==j else U[i][j] for j in range(4)] for i in range(4)];d=pivots(lower)
 native_piv=z['finite_Schur_lower_pivots_native']
 assert z['finite_selected_signed_positive_definite_certified']==(native_piv is not None and len(native_piv)==4 and all(ball(t)[0]>0 for t in native_piv))
 if z['finite_selected_signed_positive_definite_certified']:assert d is not None and all(t[0]>0 for t in d)
 # Independent two-variable Cauchy comparison through the original
 # one-variable jet, including rigorous aliasing and both factorials.
 B=F(11,10);Nu=2*B*F(3,2)**2;Aou=36*Nu+8*F(3,2)**2+8*B*B*6**2
 assert F(44,7)*F(37,64)+F(1,4)<4 and 1/(1-B/4)<F(3,2)
 assert Nu==F(v['circle_sine_norm_upper']) and Aou==F(v['circle_sine_Ao_upper'])
 assert Aou+39*Nu==F(v['analytic_bivariate_composed_upper'])<10**8==v['analytic_bivariate_majorant']
 n=256;r=F(1,8);R=F(1,4);alias=F(10**8)*R**-26*factorial(13)**2*(r/R)**n/(1-(r/R)**n)
 assert alias==F(v['derivative_alias_upper']) and v['Cauchy_nodes']==n and v['Cauchy_radius']==str(r) and v['analytic_radius']==str(R)
 total=((F(0),F(0)),(F(0),F(0)));assert len(v['points'])==256
 for j,point in enumerate(v['points']):
  assert point['index']==j;omega=cball(point['omega']);phase=cball(point['phase']);identity=cmul(cpow(omega,13),phase)
  assert identity[0][0]<=1<=identity[0][1] and identity[1][0]<=0<=identity[1][1]
  total=cadd(total,cmul(cball(point['value']),phase))
 factor=F(factorial(13),n)/r**13;estimate=(scale(total[0],factor),scale(total[1],factor));recorded=cball(v['Cauchy_estimate']);wanted=cball(v['coincident_mixed_jet'])
 for j in range(2):
  intersects(estimate[j],recorded[j]);intersects((estimate[j][0]-alias,estimate[j][1]+alias),wanted[j])
 assert v['working_precision_bits']==3072 and v['Laplace_terms']==384 and v['source_order']==v['target_order']==13 and v['source_center']=='37/64'
 assert z['global_complementary_action_computed']==z['full_infinite_Schur_certified']==z['finite_BS_block_computed']==v['global_domain_proved']==False
 assert z['W_ODD_NEG']==z['inherited_original_domain_review']==v['W_ODD_NEG']=='OPEN'
 print('EXACT FINITE SIGNED SCHUR / MIXED-CAUCHY REPLAY PASS; finite positivity',z['finite_selected_signed_positive_definite_certified'],'seconds',round(time.monotonic()-start,2),'global signed gate OPEN')
if __name__=='__main__':main()
