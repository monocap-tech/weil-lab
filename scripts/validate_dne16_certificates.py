#!/usr/bin/env python3
"""Exact rational verification of displayed interval gates and replay overlap."""
from fractions import Fraction as F
import json,sys
checks=0
def bounds(x):
 global checks
 l,h=map(F,x);assert l<=h;checks+=1
 return l,h
def overlap(x,y):
 global checks
 a,b=bounds(x);c,d=bounds(y);assert a<=d and c<=b;checks+=1
summary=[]
for parity in ('even','odd'):
 p=json.load(open(sys.argv[1]+'/'+parity+'_certificate.json'))
 r=json.load(open(sys.argv[1]+'/'+parity+'_replay_certificate.json'))
 old=json.load(open(sys.argv[2]+'/'+parity+'_replay_certificate.json'))
 for obj in (p,r):
  assert obj['parity']==parity and len(obj['projected_basis_indices'])==58
  assert obj['projected_basis_indices']==list(range(0 if parity=='even' else 1,116,2))
  assert obj['native_finite_pairing_overlap_checks']==60;checks+=3
  for key in ('P2','optimized_gain','gain_fraction','required_gain_fraction','optimized_J','optimized_J_over_energy','fixed_rational_J','fixed_rational_J_over_energy','energy','budget','det_V'):
   bounds(obj[key])
  assert bounds(obj['det_V'])[0]>0
  assert bounds(obj['V'][0][0])[0]>0
  assert bounds(obj['gain_fraction'])[0]>0 and bounds(obj['gain_fraction'])[1]<1;checks+=3
  fail=bounds(obj['optimized_J'])[0]>bounds(obj['budget'])[1]
  passed=bounds(obj['fixed_rational_J'])[1]<bounds(obj['budget'])[0]
  assert fail==obj['optimized_gate_failure_proved'] and passed==obj['fixed_gate_passed'];checks+=2
  # PSD is a mathematical consequence of joint projection; these two strict
  # principal-minor guards also reject gross numerical/custody errors.
  h=obj['H'];h00=bounds(h[0][0]);h11=bounds(h[1][1]);h01=bounds(h[0][1])
  assert h00[0]>0 and h11[0]>0 and h00[0]*h11[0]>max(abs(v) for v in h01)**2;checks+=1
  assert len([F(v) for v in obj['fixed_rational_Y']])==2;checks+=1
 for i in range(3):
  for j in range(3):overlap(p['native_exact_H2_projected_Gram'][i][j],r['native_exact_H2_projected_Gram'][i][j])
 for key in ('gain_fraction','optimized_J','fixed_rational_J'):overlap(p[key],r[key])
 # DNE15 projected F112; DNE16 projects U. Exact H2 target has zero measured
 # high pairings, and its transfer is paid in both certificates.
 prior=list(map(F,old['actual_full_F112_residual_square']))
 prior=[str(prior[0]-F(1,10**72)),str(prior[1]+F(1,10**72))]
 overlap(r['P2'],prior)
 summary.append({'parity':parity,'fixed_gate_passed':r['fixed_gate_passed'],'optimized_gate_failure_proved':r['optimized_gate_failure_proved']})
print(json.dumps({'stage':'DNE16','exact_fraction_checks':checks,'primary_replay_overlap':True,'DNE15_exact_target_overlap':True,'results':summary,'all_passed':True},indent=2))
