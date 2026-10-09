#!/usr/bin/env python3
"""Exact same physical source columns with positive/null/negative complete Schur signs."""
import argparse,json
from fractions import Fraction as F
from validate_correlated_high_floor_cc59 import tr,mul,add,sc,eye,inv,gram,psd,KAPPA
def block(a,b,c,d):return [r+s for r,s in zip(a,b)]+[r+s for r,s in zip(c,d)]
def zero(n,m):return [[F(0) for _ in range(m)] for _ in range(n)]
def model(d):
 A=sc(eye(3),4);C=sc(eye(2),3);K=[[F(3),F(0)],[F(0),F(3)],[F(0),F(0)]]
 D=sc(eye(3),KAPPA+9/(3-KAPPA));D[2][2]=d
 high=block(C,tr(K),K,D)
 Bfull=[r+s for r,s in zip(zero(3,2),eye(3))]
 Q=block(A,Bfull,tr(Bfull),high)
 observed=[r[:5] for r in Q]
 Schur=add(A,sc(mul(mul(Bfull,inv(high)),tr(Bfull)),-1))
 return Q,high,observed,Schur,K
def validate():
 cases=[];fixed=None;Dfixed=None;nativefixed=None;null_vector=None
 for d,sign in [(KAPPA,'negative'),(F(1,4),'null'),(F(1),'positive')]:
  Q,C,source,S,K=model(d)
  assert psd(add(C,sc(eye(5),-KAPPA)))
  # Same actual high floor: a nonzero eigenvector at kappa in the first coupled pair.
  eigen=[[F(3)], [F(0)], [-(3-KAPPA)], [F(0)], [F(0)]]
  assert mul(C,eigen)==sc(eigen,KAPPA)
  D=gram(source);native=[r[:5] for r in Q[:5]]
  if fixed is None:fixed=source;Dfixed=D;nativefixed=native
  assert source==fixed and D==Dfixed and native==nativefixed
  assert psd(add(D,sc(eye(5),-9))) # identical strictly positive full finite source frame.
  assert S[0][0]>0 and S[1][1]>0 and S[0][1]==S[0][2]==S[1][2]==0
  assert S[2][2]==4-1/d
  h=[[F(0)],[F(0)],[F(1)],[F(0)],[F(0)],[F(0)],[F(0)],[-1/d]]
  energy=mul(mul(tr(h),Q),h)[0][0];assert energy==S[2][2]
  if sign=='null':
   assert mul(Q,h)==zero(8,1) and psd(Q);null_vector=h
  elif sign=='positive':assert psd(Q) and S[2][2]>0
  else:assert energy<0 and not psd(Q)
  # CC59 correlated majorant is identical at all three completions.
  P=eye(3);H=gram(K);Z=tr(K);C2=sc(eye(2),3)
  V=add(mul(C2,add(C2,sc(eye(2),-KAPPA))),H)
  U=sc(add(P,sc(mul(mul(tr(Z),inv(V)),Z),-1)),1/KAPPA)
  blind=[[F(0)],[F(0)],[F(1)]]
  assert mul(Z,blind)==zero(2,1) and U[2][2]==1/KAPPA>4
  actual=add(sc(eye(3),4),sc(S,-1));assert psd(add(U,sc(actual,-1)))
  cases.append({'unmeasured_blind_high_diagonal':str(d),'complete_Schur_blind':str(S[2][2]),'sign':sign,
   'same_physical_source_columns':True,'same_complete_finite_source_Gram':True,'same_exact_high_floor':True,
   'correlated_majorant_blind':str(U[2][2]),'correlated_gate_cannot_certify':True})
 # Contact exclusion is false in one completion despite a positive observed source frame.
 assert null_vector is not None
 Q0,_,_,_,_=model(F(1,4));levels=[]
 for mu in [F(1,10**40),F(1,100),F(1,20)]:
  Q=add(Q0,sc(eye(8),mu));assert mul(Q,null_vector)==sc(null_vector,mu)
  assert psd(add(Q,sc(eye(8),-mu)))
  mass=mul(tr(null_vector),null_vector)[0][0]
  assert mul(mul(tr(null_vector),Q),null_vector)[0][0]==mu*mass>0
  # Retained-only shift leaves positive high shifted terms on the null vector.
  lowonly=[r[:] for r in Q]
  for j in range(3):lowonly[j][j]-=mu
  assert mul(mul(tr(null_vector),lowonly),null_vector)[0][0]>0
  levels.append({'positive_ground_level':str(mu),'whole_physical_shift_exact_null':True,'retained_only_shift_not_null':True})
 return {'status':'PASS','milestone':'CC61','classification':'abstract partial-data insufficiency control, not Weil countermodel',
  'observed_carrier_dimensions':[3,2],'unmeasured_dimension':3,'same_source_completion_cases':cases,
  'fixed_complete_source_Gram':[[str(x) for x in r] for r in Dfixed],
  'fixed_native_form':[[str(x) for x in r] for r in nativefixed],
  'full_observed_source_frame_lower':'9 I','compensated_source_Gram':'I_3',
  'positive_ground_levels':levels,'native_Weil_Gram_evaluated':False,
  'complete_Weil_identity_nonimplication_proved':False,'all_cap_frame':False,'RH':False,'Lean':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 r=validate();open(a.output,'w').write(json.dumps(r,indent=2)+'\n');print('CC61 PASS')
