#!/usr/bin/env python3
"""Paid marginal source budget for a native-energy orthogonal remainder."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
HASHES=['0cb636cdf03ad09f57cfce6d4bc67d0b7094dc1c154597cb0d1fe467590a2fd6','ebca74e6237cf401b7480afe08b91caba2c3412dc08e55ac2ac55f1970d8f788','316ea81720e0992699ee8a37c5cc48b1170d811ef6d88bbdf19d46d03860c7a9','96a4f1448b0aa0d347ce79345e222d260c70af22cc86e7cd998626883e6fdb90','c73aff9e17a5e659449a3d6e232ffa4c97603f3300afedbae8188500cfbf81ce']
def read(p):
 b=Path(p).read_bytes();return json.loads(b),hashlib.sha256(b).hexdigest()
def run(paths):
 data=[read(p) for p in paths];assert [h for _,h in data]==HASHES;checks=1
 prior,low,even,odd,reduction=[v for v,_ in data];k=F(11,25);rows=[]
 assert prior['eight_direction_mixed_union_certified'] and reduction['remaining_finite_dimension']==104;checks+=1
 for idx,(r,l,s,w) in enumerate(zip(prior['rows'],low['native_parity_gates'],(even,odd),reduction['rows'])):
  assert r['parity']==l['parity']==s['parity']==w['parity'];checks+=1
  assert w['remaining_dimension']==52;checks+=1
  scales=[F(1)]+list(map(F,r['congruence_scales']));Q=[[None]*4 for _ in range(4)];Q[0][0]=tuple(map(F,l['native_Q_diagonal']))
  for j,p in enumerate(r['original_low_lift_pairings'],1):Q[0][j]=Q[j][0]=tuple(map(F,p))
  for i in range(3):
   for j in range(3):Q[i+1][j+1]=tuple(map(F,s['original_native_energy_Gram'][i][j]))
  for i in range(4):
   for j in range(4):assert Q[i][j]==Q[j][i];checks+=1
  scaled=[[tuple(z*scales[i]*scales[j] for z in Q[i][j]) for j in range(4)] for i in range(4)]
  L=[F(r['joint_low_diagonal_lower'])]+[F(r['joint_remaining_coordinate_lower'])]*3
  assert all(z>0 for z in L);checks+=1
  loading=[(scaled[i][i][1]+sum(max(map(abs,scaled[i][j])) for j in range(4) if j!=i))/L[i] for i in range(4)]
  assert all(z>1 for z in loading);checks+=1
  maximal_budget=k/max(loading);c=F(29,20000) if idx==0 else F(1,160);mu=c/k
  assert 0<c<maximal_budget<k;checks+=1
  margins=[L[i]-mu*(scaled[i][i][1]+sum(max(map(abs,scaled[i][j])) for j in range(4) if i!=j)) for i in range(4)]
  for z in margins:assert z>0;checks+=1
  # Independently useful trace comparison; Gershgorin improves it here.
  trace=sum(scaled[i][i][1]/L[i] for i in range(4));trace_budget=k/trace
  assert maximal_budget>trace_budget>0;checks+=1
  rows.append(dict(parity=r['parity'],remaining_dimension=52,
   tested_native_scaled_matrix_intervals=[[[str(z) for z in v] for v in row] for row in scaled],
   native_column_scales=list(map(str,scales)),coarse_scaled_diagonal_lower=list(map(str,L)),
   relative_native_row_bounds=list(map(str,loading)),relative_native_trace_upper=str(trace),
   trace_source_budget=str(trace_budget),maximal_row_comparison_source_budget=str(maximal_budget),
   reported_complete_remainder_source_budget=str(c),native_energy_comparison_fraction=str(mu),
   scaled_L_minus_mu_Q_strict_Gershgorin_margins=list(map(str,margins)),
   tested_complete_source_Gram_native_energy_ratio_upper=str(k-c),
   sufficient_remaining_condition='c*B_Y-Gamma_Y strictly positive definite',
   frozen_rational_remainder_source_ratio_budget=str(c/2),
   frozen_rational_native_mixed_dual_norm_budget=str(c/(4*k)),
   frozen_rational_condensed_energy_relative_margin=str(c/(4*k)),
   display_paid_source_budget=float(c),display_maximal_row_budget=float(maximal_budget),
   native_remainder_orthogonalization_evaluated=False,remaining_complete_source_Gram_evaluated=False))
 return dict(stage='DNE25',aperture='53/50',high_floor=str(k),rows=rows,input_sha256=HASHES,
  exact_rational_assertions=checks,remaining_retained_dimension=104,
  tested_frame_source_native_energy_contraction_certified=True,
  complete_mixed_source_crosses_not_needed_IF_remainder_budget_passes=True,
  remainder_budget_passed=False,new_positive_retained_directions=0,
  whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for key in ['dne23','low','even','odd','dne24']:p.add_argument(key)
 p.add_argument('--output',required=True);a=p.parse_args();r=run([getattr(a,k) for k in ['dne23','low','even','odd','dne24']]);Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'checks':r['exact_rational_assertions'],'rows':[{k:v[k] for k in ['parity','display_paid_source_budget','display_maximal_row_budget']} for v in r['rows']]}))
