"""RC272: paid P0/P1 auxiliary responses for the rank-608 projection reference."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc271_diagonal_projection_reference as parent
import validate_rpb108_rc248_direct_coupled_residual as interval
ROOT=parent.ROOT;p=parent.p;orig=parent.orig;up=parent.up;down=parent.down;root=parent.parent.ellipse.root
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc271_diagonal_projection_reference.json':'e382f3c0d21dda94e523548080c9a4d6167bac27','notes/RPB108_RC271_DIAGONAL_PROJECTION_REFERENCE_20261014.md':'6f6d8d1d64e1676efe75272d44380eceddbc621b'})
HELPER_PINS['scripts/validate_rpb108_rc271_diagonal_projection_reference.py']='d4816c77f10c25187a309a045108cadaf82ca193'

def controls(reverse):
 # A diagonal stronger inverse bound must weight the center before paying faults.
 G=[[F(4),F(1,5)],[F(1,5),F(2)]];Wlo=[[F(3),F(0)],[F(0),F(1)]]
 assert p.psd(p.add(G,Wlo,-1))
 for c,e in [([F(1),F(-1,2)],[F(1,100),F(1,70)]),([F(-1,3),F(2)],[F(-1,90),F(1,80)])]:
  norm=lambda v,A:p.mm([v],p.mm(A,[[x] for x in v]))[0][0]
  actual=norm([x+y for x,y in zip(c,e)],p.inv(G))
  paid=up((root(norm(c,p.inv(Wlo)))+root(norm(e,p.inv(Wlo))))**2)
  assert actual<=paid
 return dict(diagonal_inverse_order_and_weighted_error_payment_checked=True,
             inherited_noncommuting_response_controls=parent.controls(reverse))

def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 refs=get('271_diagonal_projection_reference')['projection_reference_models'][0]
 assert refs['model_rank']==608
 coverage=get('270_threshold_adapted_coverage')['threshold_adapted_coverage_certificates'][0]
 forms=get('247_materialized_four_trial_response');refined=get('245_source_refined_response');second=get('237_two_trial_signed_response');third=get('240_three_trial_signed_response');fourth=get('242_residual_original_actions');metric=get('129_four_vector_joint_moment')
 B=F(11,10);slo=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);shi=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);sm=(slo+shi)/2;a=F(32125,230953)
 rows=[]
 for base,ref in enumerate(refs['parity_projection_reference_certificates']):
  parity=ref['parity'];cov=coverage['parity_certificates'][base];budget=cov['original_concentration_budget']
  gamma=F(budget['reference_floor']);penalty=F(budget['low_band_penalty_upper']);delta2=F(cov['Fourier_restriction_squared_tail_upper']);lam=F(ref['new_exact_projection_augmentation_coefficient']);mu=F(ref['D_energy_reference_lower']);nu=F(ref['D_energy_reference_upper'])
  R=list(map(F,fourth['parity_residual_original_action_certificates'][base]['exact_input_Legendre_coefficients']));trials=[]
  for j in [base,base+2,base+4]:trials.append([F(n==j) for n in range(65)])
  trials.append(R);assert all(len(v)==65 for v in trials)
  retained=set(ref['retained_Legendre_degrees']);assert all(n in retained for v in trials for n,x in enumerate(v) if x)
  actions=[refined['parity_source_refined_response_certificates'][base]['refined_complete_original_source_action'],second['parity_two_trial_signed_response_certificates'][base]['new_complete_original_action'],third['parity_three_trial_signed_response_certificates'][base]['new_complete_original_action'],fourth['parity_residual_original_action_certificates'][base]]
  vectors=[list(v['finite_original_D_action'] if 'finite_original_D_action' in v else v['finite_complete_original_D_action']) for v in actions]
  for v in vectors:
   assert len(v) in [65,129]
   v.extend(dict(degree=n,coefficient='0',radius='0') for n in range(len(v),129))
  errors=list(map(lambda v:F(v['complete_original_action_D_error_squared_upper']),actions))
  F0=[[(F(l),F(h)) for l,h in row] for row in forms['parity_materialized_four_trial_response_certificates'][base]['original_trial_form_intervals']]
  mass=[[sum((orig.mass(n)*u[n]*v[n] for n in range(65)),F(0)) for v in trials] for u in trials]
  G=[[(F0[i][j][0]+lam*mass[i][j],F0[i][j][1]+lam*mass[i][j]) for j in range(4)] for i in range(4)]
  midpoint=[[(l+h)/2 for l,h in row] for row in G]
  f=[orig.mass(base)*v[base] for v in trials]
  y=[down(v[0]) for v in p.mm(p.inv(midpoint),[[v] for v in f])]
  z=[sum((y[j]*trials[j][n] for j in range(4)),F(0)) for n in range(65)]
  qlo,qhi=interval.quadratic(G,y);linear=2*sum((f[j]*y[j] for j in range(4)),F(0));centerlo=down(linear-qhi);centerhi=up(linear-qlo)
  original_fault=up(sum((abs(y[j])*root(errors[j]) for j in range(4)),F(0)))
  residual=[];source_radius=[];dlo=[];dhi=[]
  for n in range(129):
   h=orig.H(n);dl=h+slo;dh=h+shi;dlo.append(dl);dhi.append(dh)
   numerator=F(n==base)-(lam*z[n] if n<65 else 0)
   source=numerator/(h+sm)
   rad=max(abs(source-numerator/dl),abs(source-numerator/dh))
   c=source-sum((y[j]*F(vectors[j][n]['coefficient']) for j in range(4)),F(0))
   residual.append(c);source_radius.append(rad)
  choices=[]
  for k in sorted(range(1,100),reverse=reverse):
   theta=F(k,100);alpha=down(gamma-penalty*(1+1/theta)*delta2);kap=lam-penalty*(1+theta)
   if alpha<=0 or kap<=0:continue
   floor=down(a*alpha);weights=[up(1/(floor+(kap/dhi[n] if n in retained else 0))) for n in range(129)]
   indices=sorted(range(129),reverse=reverse)
   model=up(sum((orig.mass(n)*dhi[n]*residual[n]**2*weights[n] for n in indices),F(0)))
   rounding=up(sum((orig.mass(n)*dhi[n]*source_radius[n]**2*weights[n] for n in indices),F(0)))
   faults=up(original_fault**2/floor)
   correction=up((root(model)+root(rounding)+root(faults))**2)
   choices.append((correction,theta,dict(Young_parameter=str(theta),canonical_metric_floor=str(alpha),retained_projection_form_coefficient=str(kap),global_D_floor=str(floor),retained_center_weighted_inverse_energy_upper=str(model),source_D_inverse_rounding_weighted_inverse_energy_upper=str(rounding),complete_original_action_fault_weighted_inverse_energy_upper=str(faults),complete_added_inverse_residual_correction_upper=str(correction))))
  correction,theta,chosen=min(choices,key=lambda v:(v[0],v[1]))
  residual_energy=up(sum((orig.mass(n)*dhi[n]*residual[n]**2 for n in range(129)),F(0)))
  sround=up(sum((orig.mass(n)*dhi[n]*source_radius[n]**2 for n in range(129)),F(0)))
  uniform=up((root(residual_energy)+root(sround)+original_fault)**2/mu)
  assert correction<=uniform
  upper=up(centerhi+correction);lower=centerlo;assert 0<lower<=upper
  native_mass=orig.mass(base);gaplo=down(native_mass-lam*upper);gaphi=up(native_mass-lam*lower);assert gaplo<=gaphi
  allowance=down(native_mass/lam-centerhi);assert allowance>0
  diagnostics=dict(fixed_trial_inverse_correction_allowance_for_positive_gate=str(allowance),current_correction_to_allowance_ratio=str(up(correction/allowance)),uniform_to_projection_weighted_correction_ratio=str(down(uniform/correction)),error_reduction_is_required_not_actual_negative_gate=True)
  rows.append(dict(parity=parity,actual_auxiliary_source='P'+str(base),response_trial_basis=['P'+str(base),'P'+str(base+2),'P'+str(base+4),'R'+str(base)],exact_trial_coefficients=list(map(str,y)),exact_trial_Legendre_coefficients=list(map(str,z)),exact_physical_trial_Gram=p.ser(mass),new_augmented_trial_form_intervals=[[[str(l),str(h)] for l,h in row] for row in G],actual_source_trial_pairings=list(map(str,f)),original_action_D_squared_error_bounds=list(map(str,errors)),complete_original_action_combination_D_fault_norm_upper=str(original_fault),retained_actual_residual_center=[dict(degree=n,coefficient=str(residual[n]),source_D_inverse_radius=str(source_radius[n])) for n in range(129)],variational_inverse_center_lower=str(centerlo),variational_inverse_center_upper=str(centerhi),retained_projection_inverse_weight_candidates=[v[2] for v in sorted(choices,key=lambda v:v[1])],selected_retained_projection_inverse_certificate=chosen,uniform_inverse_residual_correction_upper=str(uniform),actual_auxiliary_source_inverse_response_lower=str(lower),actual_auxiliary_source_inverse_response_upper=str(upper),native_auxiliary_source_mass=str(native_mass),new_native_auxiliary_gate_lower=str(gaplo),new_native_auxiliary_gate_upper=str(gaphi),new_native_auxiliary_gate_positive_certified=gaplo>0,actual_negative_gate_proved=gaphi<0,augmentation_action_error_exactly_zero_in_physical_form=True,all_same_parity_action_faults_paid_by_norm_triangle=True))
  rows[-1]['fixed_trial_closure_diagnostics']=diagnostics
  print('RC272 '+parity+': inverse upper '+str(float(upper))+'; native gate ['+str(float(gaplo))+', '+str(float(gaphi))+']',flush=True)
 return dict(milestone='RC272',starting_commit='a568390fb3ba6634a4a3142a8055bf92a0e545e2',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,projection_source_response_certificates=rows,exact_controls=controls(reverse),new_auxiliary_source_count=2,reference_full_source_rank=608,response_trials_per_parity=4,all_original_action_and_source_faults_paid=True,augmentation_uses_exact_diagonal_projection=True,new_inverse_residual_correction_added=True,old_source_signed_pivots_used_as_new_pivots=False,full_projection_auxiliary_response_matrix_evaluated=False,full_projection_auxiliary_norm_below_one_certified=False,legacy_rank_639_reference_and_positive_pivots_preserved=True,original_below_one_hundredth_count_upper_preserved=608,original_nonpositive_count_upper_preserved=582,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC273: sharpen original-action omitted-output faults for the projection-source trial combinations, especially their part beyond the retained projection; retain weighted inverse covariance and do not infer failure from a nonpositive lower enclosure')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC272 VALIDATED: paid projection-source responses; full gate open',flush=True)
