"""RC247: four-trial responses with materialized R0/R1 augmentation."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import argparse,hashlib,json
import validate_rpb108_rc246_materialized_residual_band_actions as parent
response=parent.parent.response;interface=parent.parent.parent
orig=parent.orig;p=parent.p;B=parent.B;up=parent.up;down=parent.down;root=parent.root
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc246_materialized_residual_band_actions.json':'b59a1ae3e401b2cf670c64cc55fbc05c7286bf62','notes/RPB108_RC246_MATERIALIZED_RESIDUAL_BAND_ACTIONS_20261014.md':'75a76bfc6e4f884da5ae03480fc2be9643b97c3e'})
HELPER_PINS['scripts/validate_rpb108_rc246_materialized_residual_band_actions.py']='96cd2b2d6a5ec3c8c69e7758c40d91fd79800066'
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin');data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('245_source_refined_response');material=get('246_materialized_residual_band_actions');p240=get('240_three_trial_signed_response');p242=get('242_residual_original_actions');p239=get('239_exterior_band_leakage');p238=get('238_weighted_action_tails');p237=get('237_two_trial_signed_response');baseorig=get('231_original_polynomial_action');baseaug=get('234_materialized_band_action');bounds=get('232_augmented_polynomial_action');metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);rows=[]
 for base in [0,1]:
  pr=prior['parity_source_refined_response_certificates'][base];mr=material['parity_materialized_residual_action_certificates'][base];r240=p240['parity_three_trial_signed_response_certificates'][base];r239=p239['parity_exterior_tail_response_certificates'][base];ar=p237['parity_two_trial_signed_response_certificates'][base];bound=bounds['polynomial_augmented_action_certificates'][base];columns=[]
  original=deepcopy(baseorig['polynomial_original_action_certificates'][base]);original['finite_original_D_action']=interface.pad(original['finite_original_D_action']);original['complete_original_action_D_error_squared_upper']=pr['old_center_orthogonal_output_split_certificate']['refined_old_center_original_source_D_error_squared_upper']
  columns.append(dict(original=original,finite_complete_augmented_D_action=interface.pad(baseaug['parity_materialized_augmented_action_certificates'][base]['finite_complete_augmented_D_action']),augmentation_action_D_error_squared_upper=pr['unchanged_first_augmentation_action_D_error_squared_upper'],complete_augmented_action_D_error_squared_upper=pr['old_center_orthogonal_output_split_certificate']['updated_old_center_first_augmented_action_D_error_squared_upper']))
  second=deepcopy(ar['new_complete_original_action']);second['finite_original_D_action']=interface.pad(second['finite_original_D_action']);second['complete_original_action_D_error_squared_upper']=r239['action_exterior_tail_refinements'][1]['original_action_D_error_squared_upper'];second['D_energy_component_squared_errors']['endpoint_omitted_output']=p238['parity_weighted_tail_response_certificates'][base]['action_tail_refinements'][1]['accepted_endpoint_omitted_output_D_energy_upper']
  columns.append(dict(original=second,finite_complete_augmented_D_action=interface.pad(ar['new_complete_augmented_D_action']),augmentation_action_D_error_squared_upper=r239['action_exterior_tail_refinements'][1]['refined_augmentation_action_D_error_squared_upper'],complete_augmented_action_D_error_squared_upper=r239['action_exterior_tail_refinements'][1]['refined_complete_augmented_action_D_error_squared_upper']))
  third=deepcopy(r240['new_complete_original_action']);third['finite_original_D_action']=interface.pad(third['finite_original_D_action'])
  columns.append(dict(original=third,finite_complete_augmented_D_action=interface.pad(r240['new_complete_augmented_D_action']),augmentation_action_D_error_squared_upper=r240['new_augmentation_action_D_error_squared_upper'],complete_augmented_action_D_error_squared_upper=r240['new_complete_augmented_action_D_error_squared_upper']))
  fourth=deepcopy(p242['parity_residual_original_action_certificates'][base]);fourth['finite_original_D_action']=fourth['finite_complete_original_D_action']
  columns.append(dict(original=fourth,finite_complete_augmented_D_action=mr['finite_complete_augmented_D_action'],augmentation_action_D_error_squared_upper=mr['complete_rational_augmentation_action_D_error_squared_upper'],complete_augmented_action_D_error_squared_upper=mr['complete_augmented_action_D_error_squared_upper']))
  assert all(len(c['original']['finite_original_D_action'])==129 and len(c['finite_complete_augmented_D_action'])==129 for c in columns)
  F0=[[(F(a),F(b)) for a,b in row] for row in pr['original_trial_form_intervals']];Gy=[[(F(a),F(b)) for a,b in row] for row in pr['frequency_trial_Gram_intervals']]
  epsilon=F(bound['physical_Fhat_star_Fhat_to_J_star_J_operator_norm_upper']);massR=F(fourth['input_physical_energy'])
  for i in range(4):
   if i<3:
    row=mr['actual_band_Gram_column'][base+2*i];lo,hi=F(row['lower']),F(row['upper']);mass=orig.mass(base+2*i)
   else:lo,hi=F(mr['intersected_physical_band_input_form_lower']),F(mr['intersected_physical_band_input_form_upper']);mass=massR
   fault=up(epsilon*root(mass*massR));old=Gy[i][3];v=(max(old[0],down(lo-fault)),min(old[1],up(hi+fault)));assert v[0]<=v[1];Gy[i][3]=Gy[3][i]=v
  FL,FH=interface.loewner(F0);YL,YH=interface.loewner(Gy);lam=F(bound['augmentation_coefficient']);GL=p.add(FL,p.scale(lam,YL));GH=p.add(FH,p.scale(lam,YH));assert p.psd(YL) and p.inv(YL) and p.psd(GL) and p.inv(GL)
  mu=F(bound['fresh_augmented_N_D_lower']);nu=F(bound['fresh_augmented_N_D_upper'])
  oldcenter=response(base,columns,F0,Gy,lam,mu,nu,sl,sh,pr['source_inverse_response'],reverse)
  extended=deepcopy(columns);extended[0]=dict(original=pr['refined_complete_original_source_action'],finite_complete_augmented_D_action=pr['updated_first_complete_augmented_trial_center'],augmentation_action_D_error_squared_upper=pr['unchanged_first_augmentation_action_D_error_squared_upper'],complete_augmented_action_D_error_squared_upper=pr['updated_first_complete_augmented_action_D_error_squared_upper'])
  final=response(base,extended,F0,Gy,lam,mu,nu,sl,sh,oldcenter,reverse)
  combined=deepcopy(final)
  upper_name,upper_case=min([('old_source_center',oldcenter),('extended_source_center',final)],key=lambda x:F(x[1]['selected_inverse_upper_trial']['original_action_inverse_response_upper']))
  lower_name,lower_case=max([('old_source_center',oldcenter),('extended_source_center',final)],key=lambda x:F(x[1]['selected_inverse_lower_trial']['original_action_inverse_response_lower']))
  combined['selected_inverse_upper_trial']=deepcopy(upper_case['selected_inverse_upper_trial']);combined['selected_inverse_upper_trial_representation']=upper_name
  combined['selected_inverse_lower_trial']=deepcopy(lower_case['selected_inverse_lower_trial']);combined['selected_inverse_lower_trial_representation']=lower_name
  assert F(combined['selected_inverse_upper_trial']['original_action_inverse_response_upper'])==F(combined['actual_original_action_inverse_response_upper'])
  assert F(combined['selected_inverse_lower_trial']['original_action_inverse_response_lower'])==F(combined['actual_original_action_inverse_response_lower'])
  combined['previous_original_action_inverse_response_upper']=pr['source_inverse_response']['actual_original_action_inverse_response_upper'];combined['previous_signed_gap_lower']=pr['source_inverse_response']['actual_signed_gap_lower']
  combined['original_action_inverse_upper_improved']=F(combined['actual_original_action_inverse_response_upper'])<F(combined['previous_original_action_inverse_response_upper'])
  combined['signed_gap_lower_improved']=F(combined['actual_signed_gap_lower'])>F(combined['previous_signed_gap_lower'])
  errors=[[str(4*F(extended[i]['complete_augmented_action_D_error_squared_upper'])) if i==k else '0' for k in range(4)] for i in range(4)]
  rows.append(dict(parity=pr['parity'],response_trial_basis=final['response_trial_basis'],old_source_center_response=oldcenter,extended_source_center_response=final,source_inverse_response=combined,previous_inverse_response_upper=pr['source_inverse_response']['actual_original_action_inverse_response_upper'],original_trial_form_intervals=pr['original_trial_form_intervals'],frequency_trial_Gram_intervals=[[[str(a),str(b)] for a,b in row] for row in Gy],frequency_trial_Gram_Loewner_lower=p.ser(YL),frequency_trial_Gram_Loewner_upper=p.ser(YH),augmented_trial_form_Loewner_lower=p.ser(GL),augmented_trial_form_Loewner_upper=p.ser(GH),extended_center_four_trial_action_error_D_Gram_upper=errors,complete_materialized_R_augmented_action_error_squared_upper=mr['complete_augmented_action_D_error_squared_upper'],updated_rational_frequency_cross_entries_intersected_with_previous=True,original_form_intervals_preserved=True,shared_original_source_first_trial_fault_preserved=True,actual_negative_gap_proved=final['actual_negative_gap_proved'],signed_gap_positive_certified=final['signed_gap_positive_certified']))
 return dict(milestone='RC247',starting_commit='36ff5ec47fdadbbac35f98704a7941e7a7421705',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_response_source_count=2,actual_response_source_order=['N0 P0','N0 P1'],response_trials_per_parity=4,parity_materialized_four_trial_response_certificates=rows,two_valid_source_center_representations_intersected=True,all_same_parity_cross_terms_paid=True,same_parity_action_errors_assumed_orthogonal=False,complete_original_and_rational_augmentation_errors_paid=True,exact_controls=interface.controls(),new_response_enclosures_intersected_with_RC245=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC248: sharpen the dominant complete source/trial faults or obtain a stronger residual inverse bound; full signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC247 VALIDATED: materialized four-trial responses; full signed gate open',flush=True)
