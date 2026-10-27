#!/usr/bin/env python3
"""Independent exact arithmetic and coupled graph proof regression."""
import hashlib,json,sys
from fractions import Fraction as F
from math import factorial
from pathlib import Path

def dy(v):
 n,e=int(v[0]),int(v[1]);return F(n*2**max(e,0),2**max(-e,0))
def mm(A,B):return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def tr(A):return [list(r) for r in zip(*A)]
def add(A,B,s=1):return [[a+s*b for a,b in zip(x,y)] for x,y in zip(A,B)]
def inv(A):
 n=len(A);Z=[row[:]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
 for i in range(n):
  j=next(j for j in range(i,n) if Z[j][i]);Z[i],Z[j]=Z[j],Z[i];v=Z[i][i];Z[i]=[x/v for x in Z[i]]
  for j in range(n):
   if j!=i:
    v=Z[j][i];Z[j]=[a-v*b for a,b in zip(Z[j],Z[i])]
 return [r[n:] for r in Z]
def spd(A):
 A=[row[:] for row in A]
 for k in range(len(A)):
  assert A[k][k]>0
  for i in range(k+1,len(A)):
   for j in range(k+1,len(A)):A[i][j]-=A[i][k]*A[k][j]/A[k][k]

def regression():
 G=[[F(2),F(1,4)],[F(1,4),F(3)]];M=[[F(1,50),F(1,100)],[F(1,200),F(1,80)]]
 H=[[F(4),F(1,5)],[F(1,5),F(5)]];I=[[F(1),F(0)],[F(0),F(1)]]
 A=[G[i]+M[i] for i in range(2)]+[tr(M)[i]+H[i] for i in range(2)]
 V=[row[:] for row in I]+[[-x for x in row] for row in mm(inv(H),tr(M))]
 AV=mm(A,V);assert AV[2:]==[[F(0),F(0)],[F(0),F(0)]]
 S=[[F(1),F(1,10)],[F(1,10),F(1)]]
 J=[[F(1),F(0)],[F(0),F(1)],[F(0),F(0)],[F(0),F(0)]]
 RHS=S+[[F(0),F(0)],[F(0),F(0)]]
 Z=mm(inv(A),RHS);preimage=mm(inv(S),AV[:2]);assert mm(Z,preimage)==V
 N=[[F(1,1000),F(1,2000)],[F(1,3000),F(1,4000)]]
 KU=[[F(199,100),F(1,4)],[F(1,4),F(2)]];KW=[[F(1,100000),F(0)],[F(0),F(1,100000)]]
 K=[KU[i]+N[i] for i in range(2)]+[tr(N)[i]+KW[i] for i in range(2)]
 spd(K);spd(add(A,K,-1)) # True signed positivity can coexist with method failure.
 f=[[F(1)],[F(0)],[F(0)],[F(0)]];g=[[row[0]] for row in V]
 theta=F(97,100);gap=mm(tr(f),mm(add(K,A,-theta),f))[0][0]
 actual=mm(tr(g),mm(add(K,A,-theta),g))[0][0]
 h=F(3);spd(add(H,[[h,F(0)],[F(0),h]],-1))
 # Toy metric is Euclidean for the norm/payment test, independent of S above.
 beta=sum((K[i][j]**2 for i in range(4) for j in range(2,4)),F(0))
 assert actual>=gap-beta/(theta*h)>0
 assert mm(tr(f),mm(add(A,K,-1),f))[0][0]>0
 return True

def main():
 z=json.load(open(sys.argv[1]));old=json.load(open(sys.argv[2]));stop=json.load(open(sys.argv[3]))
 assert hashlib.sha256(Path(sys.argv[2]).read_bytes()).hexdigest()==z['input_sha256']['negative']=='a693261c31f01a4a1e11ea6400e5173435a8260b41b1f6b43aa6f67f784ccb7f'
 assert hashlib.sha256(Path(sys.argv[3]).read_bytes()).hexdigest()==z['input_sha256']['stop']=='4cc8e320de50918965ce1c47acbf7cdd87747bdb373c6a5da6a2ae1b3b0d8ba2'
 assert z['status']=='CONDITIONAL_ORIGINAL_FULL_SI29_AUGMENTED_RITZ_CAP_METHOD_STOP'
 assert z['original_source_count']==470 and z['actual_continuous_feature_count']==14 and z['trial_dimension']==484
 assert z['extra_omitted_jets']==2 and z['working_precision_bits']==4096 and len(z['cluster_witnesses'])==107
 beta=F(0);B=F(11,10)
 for i,(r,o) in enumerate(zip(z['cluster_witnesses'],old['cluster_witnesses'])):
  assert r['cluster']==i and r['lo']==o['lo'] and r['hi']==o['hi'] and r['order']==o['order']
  radius=(F(r['hi'])-F(r['lo']))/2;p=r['order'];finite=F(0)
  assert len(r['jets'])==3
  for k,j in zip(range(p,p+3),r['jets']):
   assert j['degree']==k and len(j['vector_balls'])==14
   norm=sum(((abs(dy(v[0]))+dy(v[1]))**2 for v in j['vector_balls']),F(0))
   assert norm==F(j['exact_box_norm_squared_upper'])
   cap=F(j['dyadic_norm_upper']);assert cap*cap>=norm>cap*cap/4
   finite+=radius**k*cap
  assert finite==F(r['finite_norm_upper'])
  P=p+2;rem=2*B*F(101,100)*(F(44,7)*B*radius)**(2*P+2)/factorial(P+1)**2
  assert rem==F(r['remainder_squared_upper'])
  young=F(r['young_parameter']);L=(1+young)*finite**2+(1+1/young)*rem
  assert L==F(r['packet_squared_upper']) and young>0
  M2=F(r['two_sided_squared_height_mass']);assert M2==F(o['two_sided_squared_height_mass'])
  assert M2*L==F(r['squared_action_payment']);beta+=M2*L
 assert beta==F(z['exact_KW_squared_operator_upper'])<F(z['clean_KW_squared_operator_upper'])==F(9,400000000)
 assert F(z['full_action_improvement_factor'])==F(old['exact_squared_multiplier_action_upper'])/beta>397
 x=B/2;sh=sum((x**(2*k+1)/factorial(2*k+1) for k in range(17)),F(0))+x**35/factorial(35)/(1-x*x/F(36*37))
 assert sh==F(z['sinh_B_over_2_upper'])<F(3,5)
 h=F(z['quotient_energy_H_lower']);theta=F(z['threshold_ceiling']);assert h==F(9,9091) and theta==F(97,100)
 assert F(stop['same_original_SM40_threshold_exact'])<theta
 for r,s,(a,b) in zip(z['ray_witnesses'],stop['rays'],[(12001,16384),(3013,4096)]):
  assert r['ray']==s['ray'] and r['original_sine_coefficient']==a and r['original_pole_coefficient']==b
  gap=F(s['low_0_12_signed_method_lower'])+theta*(F(s['genuine_original_pole_payment_lower'])-F(s['entire_original_Ao_high12_upper']))
  assert gap==F(r['accepted_original_method_gap_lower'])==F(s['complete_original_Kminus_minus_97pct_Astar_lower'])
  norm=2*B*(a+F(3,5)*b)**2;payment=beta*norm/(theta*h)
  assert norm==F(r['physical_norm_squared_upper']) and payment==F(r['whole_14_correction_payment_upper'])
  assert gap-payment==F(r['augmented_graph_method_gap_lower'])>0 and r['strict_augmented_ritz_cap_stop'] is True
 assert len(z['ray_witnesses'])==2 and regression()
 for key in ('supported_operator_square_identified_with_squared_multiplier','energy_projected_negative_action_assumed_invariant','original_signed_negative_direction_proved','all_trial_spaces_ruled_out','original_W_ODD_NEG_closed'):
  assert z[key] is False
 assert z['W_ODD_NEG']=='OPEN' and z['inherited_original_domain_review']=='OPEN'
 print('INDEPENDENT EXACT FULL-AUGMENTED METHOD STOP REPLAY PASS: 321 jets, 107 complete payments, both graph gaps, coupled graph/signed-positive regression')
if __name__=='__main__':main()
