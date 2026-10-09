#!/usr/bin/env python3
"""Authenticated packet response rank and full retained correction budget."""
import argparse,itertools,json
from pathlib import Path
from fractions import Fraction as F
import certify_cc80_defect_response_acceptance as exact
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as direct
import certify_cc91_both_joined_pass as joined
import certify_cc92_conditional_physical_restriction as custody

def controls():
 crossings=[];kap=F(207,1000)
 for scale in [F(1),F(1,10**18)]:
  for theta in [F(-1,100),F(0),F(1,100)]:
   a=scale;b=F(1)
   q=exact.mat([[2*kap*a*a,theta*kap*a*b],[theta*kap*a*b,2*kap*b*b]])
   r=[[kap*a],[kap*b]]
   reaction=exact.mul(exact.mul(r,[[1/kap]]),exact.tr(r))
   s=exact.add(q,exact.neg(reaction))
   assert all(x>0 for x in exact.pivots(q))
   assert s[0][0]==kap*a*a>0 and s[1][1]==kap*b*b>0
   v=[b,-a];assert exact.mul(exact.tr(r),[[z] for z in v])==[[F(0)]]
   kernel=sum(v[i]*s[i][j]*v[j] for i in range(2) for j in range(2))
   assert kernel==2*kap*a*a*b*b*(2-theta)>0
   determinant=s[0][0]*s[1][1]-s[0][1]**2
   assert determinant==kap**2*a*a*b*b*theta*(2-theta)
   crossings.append(dict(scale=str(scale),theta=str(theta),finite_native_positive=True,
    both_separate_high_Schur_diagonals_positive=True,kernel_value=str(kernel),joint_determinant=str(determinant)))
 # Positivity on the update kernel is necessary but not sufficient.
 s0=exact.mat([[-2,0],[0,1]]);delta=exact.diag([1,0]);s=exact.add(s0,delta)
 assert s0[1][1]>0 and s[0][0]<0
 # A non-coordinate update cannot remove a negative value on its kernel.
 v=[F(1),F(-1),F(0)];u=[[F(1)],[F(1)],[F(2)]]
 floor=exact.diag([-1,-1,3]);update=exact.mul(u,exact.tr(u));corrected=exact.add(floor,update)
 assert exact.mul(exact.tr(u),[[z] for z in v])==[[0]]
 assert sum(v[i]*corrected[i][j]*v[j] for i in range(3) for j in range(3))==-2
 # Nine negative directions cannot all be repaired by a rank-eight update.
 floor=exact.diag([-1]*9+[1]*3);update=exact.diag([2]*8+[0]*4)
 assert exact.add(floor,update)[8][8]==-1
 return dict(exact_crossings=crossings,kernel_positivity_not_sufficient=True,
  noncoordinate_blind_negative_control=True,nine_negative_rank_eight_rejection=True)

def run(massroot,newroot,parentroot):
 rows=[]
 for parity,count,columns in [('even','eight',8),('odd','seven',7)]:
  if parity=='even':d=joined.load(newroot,'RPB108_NF46_EVEN_NEXT_SHELL_CERTIFICATE_20261009.json')
  else:d=joined.seven.load(parentroot,'RPB108_NF45_ODD_INVERSE_WITNESS_CERTIFICATE_20261009.json')
  n=direct.sub(direct.scale(c.matrix(d[count+'_high_complete_source_Gram']),1/direct.K),c.matrix(d[count+'_high_native_Gram']))
  _,rho,_=direct.inverse(n);assert rho<1
  w=direct.sub(c.matrix(d['joined_'+count+'_high_source_crosses']),direct.scale(c.matrix(d['joined_'+count+'_high_native_crosses']),direct.K))
  assert len(w)==3 and all(len(row)==columns for row in w)
  minors=[]
  for cols in itertools.combinations(range(columns),3):
   determinant=c.det3([[w[i][j] for j in cols] for i in range(3)])
   if determinant[0]>0 or determinant[1]<0:minors.append((cols,determinant))
  assert minors;cols,determinant=minors[0]
  move=custody.load(massroot,'RPB108_NF37_'+parity.upper()+'_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE_20261009.json')
  floor=direct.sub(c.matrix(move['original_selected_native_energy_Gram']),direct.scale(c.matrix(move['original_selected_complete_source_Gram']),1/direct.K))
  leading=c.det2([row[:2] for row in floor[:2]]);det=c.det3(floor)
  assert floor[0][0][0]>0 and leading[0]>0 and det[1]<0
  rows.append(dict(parity=parity,paid_high_columns=columns,packet_response_rank=3,
   response_rank_witness_column_indices=list(cols),response_rank_witness_determinant=c.pair(determinant),
   certified_nonzero_three_column_minor_count=len(minors),high_response_inverse_residual_upper=c.pair(c.iv(rho))[1],
   actual_packet_scalar_floor_inertia=dict(positive=2,negative=1,zero=0),
   actual_packet_scalar_floor_determinant=c.pair(det),
   full_retained_dimension=56,full_response_rank_upper=columns,
   full_retained_correction_kernel_dimension_lower=56-columns,
   remaining_dimension=53,additional_response_profile_rank_upper=columns-3,
   remaining_profile_kernel_dimension_lower=53-(columns-3),
   maximum_full_scalar_floor_negative_index_repairable=columns,
   whole_scalar_floor_negative_index_already_at_least=1,
   additional_negative_index_budget_upper=columns-1))
 return dict(milestone='CC95',integration_parent='779aec35c365e36fbc98b24499a3e6bbe4ec4855',
  read_only_source='6658ff2837838ab00b9b9c605fdd200d473c3293',parity_checks=rows,
  combined_full_response_rank_upper=15,combined_full_correction_kernel_dimension_lower=97,
  exact_controls=controls(),full_remaining_response_entries_available=False,
  actual_full_scalar_floor_negative_index_known=False,
  existing_high_columns_proved_insufficient=False,
  background_floor_newly_proved=False,original_form_domain_attachment_inherited=True,
  whole_aperture_positive=False,highest_certified_whole_aperture='21/20')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('mass_root',type=Path);ap.add_argument('NF46_root',type=Path);ap.add_argument('NF45_root',type=Path);ap.add_argument('--output',type=Path,required=True)
 a=ap.parse_args();d=run(a.mass_root,a.NF46_root,a.NF45_root);a.output.write_text(json.dumps(d,indent=2)+'\n')
 print('CC95 PASS: packet response rank three in both parities; full correction kernel dimension >=97')
