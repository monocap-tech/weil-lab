#!/usr/bin/env python3
"""Sharper coherent source domination and paid Young split on DNE23's frame."""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import argparse,json,hashlib
SHA=['0cb636cdf03ad09f57cfce6d4bc67d0b7094dc1c154597cb0d1fe467590a2fd6','6f1adeb39792345e857806ce4128c72b9b08dabd4d21f6f3bde8a8463bd94671','ebca74e6237cf401b7480afe08b91caba2c3412dc08e55ac2ac55f1970d8f788','316ea81720e0992699ee8a37c5cc48b1170d811ef6d88bbdf19d46d03860c7a9','96a4f1448b0aa0d347ce79345e222d260c70af22cc86e7cd998626883e6fdb90','3afa34f88c82d55c6463e08fe316f40f8f3b4a8795ede09ceda5648d2ad6ea53']
def root(x,d):
 s=10**d;n=isqrt(x.numerator*s*s//x.denominator);v=F(n+1,s);assert v*v>x;return v
def read(p):
 b=Path(p).read_bytes();return json.loads(b),hashlib.sha256(b).hexdigest()
def run(paths,d):
 inputs=[read(p) for p in paths];assert [h for _,h in inputs]==SHA;checks=1
 joint,prior,low,even,odd,oldbudget=[v for v,_ in inputs];k=F(11,25);rows=[]
 for r,p,l,s,b in zip(joint['rows'],prior['rows'],low['native_parity_gates'],(even,odd),oldbudget['rows']):
  assert r['parity']==p['parity']==l['parity']==s['parity']==b['parity'];checks+=1
  sc=list(map(F,r['congruence_scales']));V=[[(F(v[0]),F(v[1])) for v in row] for row in p['complete_coarse_matrix_intervals']];G=[[(F(v[0]),F(v[1])) for v in row] for row in s['original_complete_source_Gram']]
  def margins(rho):
   H=[[(rho*V[i][j][0]-G[i][j][1],rho*V[i][j][1]-G[i][j][0]) for j in range(3)] for i in range(3)]
   return [sc[i]**2*H[i][i][0]-sum(sc[i]*sc[j]*max(map(abs,H[i][j])) for j in range(3) if j!=i) for i in range(3)]
  rho=next(F(i,1000) for i in range(1,1001) if min(margins(F(i,1000)))>0)
  rm=margins(rho);assert 0<rho<1 and min(rm)>0;checks+=1
  dual=F(r['native_low_mixed_V_dual_square_upper']);P0=F(l['full_F112_source_square'][1]);M=root(dual,d)+root(rho*P0,d)/k;A=F(r['original_low_coarse_diagonal_lower']);g=F(p['scaled_positive_margin'])
  ps=[tuple(map(F,v)) for v in r['original_low_lift_pairings']];Q=s['original_native_energy_Gram']
  qrows=[F(l['native_Q_diagonal'][1])+sum(sc[i]*max(map(abs,ps[i])) for i in range(3))]
  qrows += [sc[i]**2*F(Q[i][i][1])+sc[i]*max(map(abs,ps[i]))+sum(sc[i]*sc[j]*max(abs(F(z)) for z in Q[i][j]) for j in range(3) if j!=i) for i in range(3)]
  candidates=[]
  for i in range(1,1000):
   theta=F(i,1000);alpha=A-M*M/(1-theta)
   if alpha>0:candidates.append((k*min([alpha/qrows[0]]+[theta*g/v for v in qrows[1:]]),theta,alpha))
  best,theta,alpha=max(candidates);credit=F((best*10**5).__floor__(),10**5)
  cm=[alpha-credit*qrows[0]/k]+[theta*g-credit*v/k for v in qrows[1:]]
  assert min(cm)>0 and credit>F(b['reported_complete_remainder_source_budget']);checks+=1
  masses=[F(1)]+list(map(F,p['lift_column_mass_upper']));sources=[P0]+[G[i][i][1] for i in range(3)];completed=[m+root(v,d)/k for m,v in zip(masses,sources)]
  lower=[alpha]+[theta*g]*3;scale=[F(1)]+sc
  gap=1/(sum((v*m)**2/ell for v,m,ell in zip(scale,completed,lower))+1/k)
  assert gap>F(r['whole_high_physical_gap_strict_lower']);checks+=1
  rows.append(dict(parity=r['parity'],source_Gram_domination_factor=str(rho),scaled_rho_V_minus_Gamma_margins=list(map(str,rm)),
   combined_low_mixed_V_dual_norm_upper=str(M),original_low_coarse_diagonal_lower=str(A),theta=str(theta),joint_low_lower=str(alpha),
   three_coordinate_lower=str(theta*g),native_scaled_absolute_row_upper=list(map(str,qrows)),
   maximal_credit_in_selected_theta_grid=str(best),reported_complete_remainder_source_credit=str(credit),
   scaled_native_comparison_margins=list(map(str,cm)),old_credit=str(F(b['reported_complete_remainder_source_budget'])),
   high_completed_column_mass_upper=list(map(str,completed)),column_scales=list(map(str,scale)),
   whole_high_physical_gap_strict_lower=str(gap),display_gap=float(gap),display_credit=float(credit),
   remaining_complete_source_Gram_certified=False))
 common=min(F(r['whole_high_physical_gap_strict_lower']) for r in rows);assert common>F(4,10**36);checks+=1
 return dict(stage='DNE27',aperture='53/50',root_digits=d,high_floor=str(k),rows=rows,input_sha256=SHA,
  exact_rational_assertions=checks,source_ratio_grid_denominator=1000,theta_grid_denominator=1000,
  eight_direction_physical_gap_guard='4/'+str(10**36),tested_original_frame_unchanged=True,
  positive_retained_dimension=8,uncovered_retained_dimension=104,
  remaining_source_credits_certified=True,remaining_source_budget_passed=False,
  new_original_source_integrations=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for k in ['dne23','dne22','low','even','odd','dne25']:p.add_argument(k)
 p.add_argument('--digits',type=int,default=160);p.add_argument('--output',required=True);a=p.parse_args();r=run([getattr(a,k) for k in ['dne23','dne22','low','even','odd','dne25']],a.digits);Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'checks':r['exact_rational_assertions'],'rows':[{k:v[k] for k in ['parity','source_Gram_domination_factor','theta','display_credit','display_gap']} for v in r['rows']]}))
