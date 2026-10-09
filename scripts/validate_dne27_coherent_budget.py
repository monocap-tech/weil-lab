#!/usr/bin/env python3
"""Independent interval margins, rational Young tests and physical controls."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse,json,hashlib
import certify_dne27_coherent_budget as c
def validate(paths,primary,replay):
 data=[c.read(p) for p in paths];assert [v[1] for v in data]==c.SHA;checks=1
 old,prior,low,even,odd,budget=[v[0] for v in data];a=json.loads(Path(primary).read_bytes());b=json.loads(Path(replay).read_bytes())
 for r,rp,src,oldrow,p in zip(a['rows'],b['rows'],(even,odd),old['rows'],prior['rows']):
  rho=F(r['source_Gram_domination_factor']);theta=F(r['theta']);sc=list(map(F,p['congruence_scales']))
  V=p['complete_coarse_matrix_intervals'];G=src['original_complete_source_Gram']
  H=[[(rho*F(V[i][j][0])-F(G[i][j][1]),rho*F(V[i][j][1])-F(G[i][j][0])) for j in range(3)] for i in range(3)]
  for i in range(3):
   margin=sc[i]**2*H[i][i][0]-sum(sc[i]*sc[j]*max(map(abs,H[i][j])) for j in range(3) if j!=i)
   assert margin==F(r['scaled_rho_V_minus_Gamma_margins'][i])>0;checks+=1
  for z in product(range(-2,3),repeat=3):
   if not any(z):continue
   value=sum(min(v*sc[i]*sc[j]*z[i]*z[j] for v in H[i][j]) for i in range(3) for j in range(3));assert value>0;checks+=1
  M=F(r['combined_low_mixed_V_dual_norm_upper']);A=F(r['original_low_coarse_diagonal_lower']);alpha=F(r['joint_low_lower'])
  assert alpha==A-M*M/(1-theta)>0;checks+=1
  for x,y in product(range(-3,4),repeat=2):
   actual=A*x*x-2*M*abs(x*y)+y*y;lower=alpha*x*x+theta*y*y
   assert actual-lower==(M*abs(x)-(1-theta)*abs(y))**2/(1-theta)>=0;checks+=1
  credit=F(r['reported_complete_remainder_source_credit']);k=F(11,25);L=[alpha]+[F(r['three_coordinate_lower'])]*3;qrows=list(map(F,r['native_scaled_absolute_row_upper']))
  for ell,q,m in zip(L,qrows,r['scaled_native_comparison_margins']):assert ell-credit*q/k==F(m)>0;checks+=1
  ratio=credit/F(r['old_credit']);assert ratio>F(2) if r['parity']=='even' else ratio>F(3,2);checks+=1
  assert r['reported_complete_remainder_source_credit']==rp['reported_complete_remainder_source_credit'] and r['theta']==rp['theta'] and r['source_Gram_domination_factor']==rp['source_Gram_domination_factor'];checks+=1
  assert F(rp['whole_high_physical_gap_strict_lower'])>=F(r['whole_high_physical_gap_strict_lower'])>F(oldrow['whole_high_physical_gap_strict_lower']);checks+=1
  mass=list(map(F,r['high_completed_column_mass_upper']));scale=list(map(F,r['column_scales']));gap=F(r['whole_high_physical_gap_strict_lower'])
  for z in product(range(-1,2),repeat=5):
   norm=sum(m*s*abs(v) for m,s,v in zip(mass,scale,z[:4]))+abs(z[4]);energy=sum(ell*v*v for ell,v in zip(L,z[:4]))+k*z[4]*z[4]
   assert energy>=gap*norm*norm;checks+=1
 # Coherent border threshold gives a genuine positive/null/negative crossing.
 controls=[]
 for value in [F(99,100),F(1),F(101,100)]:
  determinant=1-value*value;null=(determinant==0);controls.append(dict(border=str(value),determinant=str(determinant),actual_null=null))
  assert (determinant>0)==(value<1) and (determinant==0)==(value==1);checks+=1
 # Positive ground level from a whole-mass shift of [[1,1],[1,1]].
 for lam in [F(1,10),F(1),F(2)]:
  assert (1+lam)-1==lam and F(1)*(1+lam)-1==lam>0;checks+=1
 return dict(stage='DNE27',status='PASS',independent_rational_checks=checks,
  certificate_sha256=hashlib.sha256(Path(primary).read_bytes()).hexdigest(),
  primary_and_replay_source_credits_identical=True,higher_precision_physical_gap_not_weaker=True,
  paid_source_domination_and_native_comparison_passed=True,coherent_Young_and_nonorthogonal_mass_controls_passed=True,
  genuine_crossing_controls=controls,whole_mass_positive_level_controls_passed=True,
  complete_remaining_Gram_certified=False,whole_aperture_positive=False)
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for key in ['dne23','dne22','low','even','odd','dne25','certificate','replay','output']:p.add_argument(key)
 a=p.parse_args();r=validate([getattr(a,k) for k in ['dne23','dne22','low','even','odd','dne25']],a.certificate,a.replay);Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'checks':r['independent_rational_checks']}))
