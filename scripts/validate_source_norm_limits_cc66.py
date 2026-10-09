#!/usr/bin/env python3
"""Exact partial-data controls: a full trial source does not fix high response."""
from fractions import Fraction as F
import argparse,json
from pathlib import Path
from validate_correlated_high_floor_cc59 import tr,mul,inv,add,sc,eye,block,psd,KAPPA

def run():
 C2=[[F(3),F(0)],[F(0),F(4)]]
 shifted=add(C2,sc(eye(2),-KAPPA))
 k=[[F(1,3),F(1,5)]]
 u=[[F(1,1000)],[F(-1,500)]];v=F(1);w=F(1,2)
 zobs=add(mul(shifted,u),sc(tr(k),v))
 ell=sc(tr(zobs),-1/w)
 r=u+[[v],[w]];P=mul(tr(r),r)[0][0]
 W=mul(C2,shifted)
 def completion(t):
  K=k+sc(ell,t)
  D=add(sc(eye(2),KAPPA),mul(mul(K,inv(shifted)),tr(K)))
  C=block(C2,tr(K),K,D)
  assert psd(add(C,sc(eye(4),-KAPPA)))
  y=[[F(1)],[F(0)]]
  floor_vector=sc(mul(mul(inv(shifted),tr(K)),y),-1)+y
  assert mul(C,floor_vector)==sc(floor_vector,KAPPA)
  V=add(W,mul(tr(K),K))
  z=add(mul(shifted,u),mul(tr(K),[[v],[w]]))
  credit=mul(mul(tr(z),inv(V)),z)[0][0]
  reaction=mul(mul(tr(r),inv(C)),r)[0][0]
  assert reaction==(P-credit)/KAPPA
  # Same complete retained source r, same C2 and observed high source row.
  assert C[:2]==[C2[i]+[k[0][i],t*ell[0][i]] for i in range(2)]
  return C,credit,reaction,z
 C0,credit0,q,z0=completion(F(0));assert credit0>0
 native_observed=C0[2][:3]
 Qbase=block([[q]],tr(r),r,C0)
 cases=[]
 for t,sign in [(F(-1),1),(F(0),0),(F(1),-1)]:
  C,credit,reaction,z=completion(t)
  Q=block([[q]],tr(r),r,C)
  assert [row[:4] for row in Q[:4]]==[row[:4] for row in Qbase[:4]]
  assert [Q[i][0] for i in range(1,5)]==[row[0] for row in r]
  assert C[2][:3]==native_observed
  schur=q-reaction
  assert (schur>0)-(schur<0)==sign
  h=[[F(1)]]+sc(mul(inv(C),r),-1)
  assert mul(mul(tr(h),Q),h)[0][0]==schur
  if t==0:
   assert psd(Q) and mul(Q,h)==[[F(0)]]*5
   Qzero=Q;null=h
  if t==1:
   assert z==[[F(0)],[F(0)]] and credit==0 and reaction==P/KAPPA
   assert mul(C,r)==sc(r,KAPPA)
  cases.append(dict(unseen_high_source_scale=str(t),complete_trial_source_square=str(P),
   retained_energy=str(q),correlation_credit=str(credit),true_high_reaction=str(reaction),
   full_Schur=str(schur),actual_null=t==0,
   complete_retained_source_unchanged=True,measured_native_block_unchanged=True,
   complete_native_block_on_retained_H2_and_observed_J_unchanged=True,
   scalar_high_floor_unchanged=True))
 scaled=[]
 for eps in [F(1,10**18),F(1,10**16)]:
  source=sc(r,eps);low=q*eps*eps
  native=None
  for t,sign in [(F(-1),1),(F(0),0),(F(1),-1)]:
   C,credit,reaction,z=completion(t)
   Q=block([[low]],tr(source),source,C)
   fixed=[row[:4] for row in Q[:4]]
   if native is None:native=fixed
   else:assert native==fixed
   assert [row[0] for row in Q[1:]]==[row[0] for row in source]
   schur=low-reaction*eps*eps
   assert (schur>0)-(schur<0)==sign
   scaled.append(dict(source_scale=str(eps),retained_original_energy=str(low),
    unseen_scale=str(t),full_Schur=str(schur),complete_trial_source_square=str(P*eps*eps),
    defect_relative_source_ratio=str(P/q),same_source_and_observed_native_block=True))
 levels=[]
 for mu in [F(1,10**40),F(1,100),F(1,20)]:
  Q=add(Qzero,sc(eye(5),mu));assert mul(Q,null)==sc(null,mu)
  assert psd(add(Q,sc(eye(5),-mu)))
  wrong=[row[:] for row in Q];wrong[0][0]-=mu
  assert mul(wrong,null)!=[[F(0)]]*5
  levels.append(dict(original_positive_ground_level=str(mu),original_null=False,
    whole_mass_shift_has_null=True,retained_only_shift_does_not_create_this_null=True))
 return dict(milestone='CC66',status='PASS',floor=str(KAPPA),complete_trial_source_square=str(P),
  exact_partial_data_coarse_majorant_attained=True,
  fixed_complete_trial_source_crossings=cases,positive_ground_level_controls=levels,
  near_critical_scaled_crossings=scaled,
  missing_fields=['complete_measured_high_source_Gram','complete_corrected_source_correlation'],
  actual_Weil_countermodel=False,logical_nonimplication_from_all_Weil_identities=False,
  new_native_source_arithmetic=False,whole_aperture_positive=False,all_cap_frame=False,RH=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 Path(a.output).write_text(json.dumps(run(),indent=2)+'\n');print('CC66 exact complete-trial-source controls PASS')
