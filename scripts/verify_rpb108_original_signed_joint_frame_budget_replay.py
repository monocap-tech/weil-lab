#!/usr/bin/env python3
"""Independent exact ledger replay for raw joint precision and physical transport."""
import hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from math import factorial

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dy(x):return F(int(x[0]))*F(2)**int(x[1])
def ball(v):
 m,r=dy(v[0]),dy(v[1]);assert r>=0;return m-r,m+r
def overlap(x,y):assert max(x[0],y[0])<=min(x[1],y[1])
def plus(x,y):return x[0]+y[0],x[1]+y[1]
def subset(x,y):assert y[0]<=x[0]<=x[1]<=y[1]
z,b,frame,old,rank,critical=[json.loads(Path(p).read_bytes()) for p in sys.argv[1:7]]
assert len(sys.argv)==7
for name,index in [('block',2),('frame',3),('old',4),('rank',5),('critical',6)]:assert z['input_sha256'][name]==sha(sys.argv[index])
assert z['input_sha256']['frame']=='e78c29dc930274e5522c665d073044a6de6ac1fee832cac65c13128f57fe80d4'
assert z['input_sha256']['old']=='2cb869033f2c6722d356e769f35fc0e1b041ae46a8c11360e66cd7d2c694c548'
assert b['rank_input_sha256']==z['input_sha256']['rank']=='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
assert b['critical_input_sha256']==z['input_sha256']['critical']=='a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922'
assert b['working_precision_bits']==z['raw_working_precision_bits']==1024 and b['Laplace_terms']==z['raw_Laplace_terms']==128
assert z['physical_frame_working_precision_bits']==4096 and z['flint_version']==b['flint_version']=='0.8.0'
assert b['target_probes']==old['target_probes']==critical['exact_candidates']['probes']
assert b['target_sine_frequencies']==old['target_sine_frequencies']==critical['exact_candidates']['sine_frequencies']
expected=[];offset=0
for j,((c,p),n) in enumerate(zip(rank['original_nodes'],rank['selected_multiplicities'])):
 for k in range(n):expected.append((offset+k,j,c,k))
 offset+=p
expected.append((469,None,None,None));assert offset==469 and len(expected)==242
rho=F(0)
for row,prev,spec in zip(b['rows'],old['rows'],expected):
 assert tuple(row[k] for k in ['original_source_index','cluster','center','order'])==spec==tuple(prev[k] for k in ['original_source_index','cluster','center','order'])
 assert len(row['entries'])==4
 for t,(e,oe) in enumerate(zip(row['entries'],prev['entries'])):
  assert e['target_index']==t;parts=e['components_native'];op=oe['components_native'];total=(F(0),F(0))
  for key in ['arch','prime','pole']:
   overlap(ball(parts[key]),ball(op[key]));total=plus(total,ball(parts[key]))
  interval=tuple(map(F,e['signed_interval']));subset(total,interval);subset(ball(e['signed_native']),interval)
  overlap(ball(e['signed_native']),ball(oe['signed_native']))
  for key in ['prime','pole']:overlap(ball(parts[key]),ball(e['independent_'+key+'_native']))
  rho=max(rho,dy(e['signed_native'][1]))
assert rho==F(b['maximum_native_block_radius'])==F(z['maximum_raw_native_radius'])<F(2)**-581
for i in range(4):
 for j in range(4):
  prior=tuple(map(F,critical['complete_signed_Gram_intervals'][i][j]));subset(ball(b['target_signed_kernel_Gram_native'][i][j]),prior)
  parts=b['target_signed_kernel_Gram_components_native'][i][j];subset(plus(plus(ball(parts['arch']),ball(parts['prime'])),ball(parts['pole'])),prior)
x=F(7,10);assert sum((x**k/factorial(k) for k in range(5)),F(0))>2
alpha=F(2*b['Laplace_terms'])-F(1,4);m=int(alpha*F(11,5)/x);q=0
while 2**(q+1)*2<alpha*F(63,64):q+=1
assert alpha*F(11,5)>=m*x and F(22,5)>6*x
rough=2*F(2)**-m/(alpha*F(63,64));tail=F(2)**-(m+q)
assert rough<tail==F(b['Laplace_tail_Cauchy_base_upper']) and b['Laplace_tail_exponent']==m+q==809
assert b['analytic_tail_strip_imaginary_bound']=='3/4' and b['Cauchy_radius']=='1/4'
assert z['exact_dyadic_frame_transform_sha256']==frame['exact_dyadic_frame_transform_sha256']
assert len(z['physical_frame_error_row_upper'])==242 and all(0<=F(v)<F(1,100) for v in z['physical_frame_error_row_upper'])
assert z['physical_frame_Gram_lower']==z['critical_physical_Gram_lower']==critical['physical_Gram_lower']=='99/100'
d=F(z['frame_Frobenius_norm_upper']);assert 0<d<F(2)**496
u=d*d*968*rho*rho;assert u==F(z['uniform_transport_Frobenius_error_squared_upper'])<F(2)**-160
T=z['transported_signed_frame_block_native'];assert len(T)==242 and all(len(row)==4 for row in T)
radius2=sum((dy(v[1])**2 for row in T for v in row),F(0));assert radius2<=F(z['transported_native_radius_Frobenius_squared_upper'])<F(2)**-160
norm2=sum((max(map(abs,ball(v)))**2 for row in T for v in row),F(0))
bound=F(z['physical_finite_form_coupling_Frobenius_upper']);assert bound>0 and norm2/F(99,100)**2<=bound**2
assert z['diagnostic_transported_error_target_bits']==80 and z['diagnostic_budget_is_Schur_budget'] is False
for name in ['old_all_component_intervals_overlap','all_968_prime_pole_checks_passed','same_accepted_physical_frame_verified']:assert z[name] is True
for name in ['critical_quotient_normalized','strong_complementary_action_computed','full_selected_signed_matrix_computed','finite_BS_block_computed','signed_Schur_certified']:assert z[name] is False
assert z['W_ODD_NEG']==z['inherited_original_domain_review']=='OPEN'
print('EXACT JOINT TAIL / FRAME ERROR REPLAY PASS: all 968 raw entries, complete critical Gram, clean 2^-809 tail, transported error <2^-80; Schur and domain OPEN')
