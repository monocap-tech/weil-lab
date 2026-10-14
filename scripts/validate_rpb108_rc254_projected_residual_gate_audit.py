"""RC254: orthogonal projected residual lower bounds and inverse-gate budgets."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc253_prime_boundary_tail as parent
direct=parent.direct;orig=parent.orig;p=parent.p;B=parent.B
up=parent.up;down=parent.down;root=parent.root;rootdown=parent.rootdown
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc253_prime_boundary_tail.json':'d7ccfdce0b5a62e1dcfbbc0722b547b5da171b7d','notes/RPB108_RC253_PRIME_BOUNDARY_TAIL_20261014.md':'8282fea9746a67a12c641dc22a0b508b4dec0f06'})
HELPER_PINS['scripts/validate_rpb108_rc253_prime_boundary_tail.py']='60747d655e73e4426faf4a52db4e4cfe2637e438'
def controls():
 # Unknown omitted model output cannot cancel a disjoint retained block.
 w=[F(2),F(3),F(5)];center=[F(1,7),F(-2,11),F(0)];finite=[F(1,1000),F(-1,1200),F(0)];fault=[F(-1,700),F(1,900),F(1,800)]
 norm=lambda v:sum((wi*x*x for wi,x in zip(w,v)),F(0))
 lower=down(max(F(0),rootdown(norm(center))-root(norm(finite))-root(norm(fault)))**2)
 for sf in [-1,1]:
  for sg in [-1,1]:
   for tail in [F(-30),F(-1,13),F(0),F(3,13),F(100)]:
    actual=[center[k]+sf*finite[k]+sg*fault[k]+(tail if k==2 else 0) for k in range(3)]
    projected=[actual[0],actual[1],F(0)];assert lower<=norm(projected)<=norm(actual)
 # A floor on an upper formula is not a lower bound on the true inverse.
 N=[[F(1),F(0)],[F(0),F(2)]];e=[[F(1)],[F(1)]];mu=F(1,100)
 true=p.mm(p.trans(e),p.mm(p.inv(N),e))[0][0];coarse=p.mm(p.trans(e),e)[0][0]/mu;assert true<coarse
 return dict(nonidentity_metric_retained_projection_orthogonal_to_omitted_output=True,global_model_faults_retained_in_projection_error=True,upper_formula_floor_not_true_inverse_lower_bound=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin');data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('253_prime_boundary_tail');centers=get('251_extended_coupled_residual');forms=get('247_materialized_four_trial_response');bounds=get('232_augmented_polynomial_action');metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);rows=[]
 for parity,r in enumerate(prior['prime_boundary_tail_response_certificates']):
  c=centers['extended_coupled_residual_response_certificates'][parity];residual=c['extended_complete_direct_residual_center'];assert len(residual)==257
  assert c['selected_trial_coefficients']==r['selected_trial_coefficients']
  degrees=list(range(257));degrees=degrees[::-1] if reverse else degrees
  nl=sum((orig.mass(n)*(orig.H(n)+sl)*F(residual[n]['coefficient'])**2 for n in degrees),F(0));nh=sum((orig.mass(n)*(orig.H(n)+sh)*F(residual[n]['coefficient'])**2 for n in degrees),F(0))
  finite=F(c['residual_finite_rounding_D_energy_upper']);original_fault=F(c['unchanged_original_model_fault_D_norm_upper']);rational=F(c['unchanged_rational_augmentation_comparison_D_error_squared_upper'])
  # The omitted model tail has exactly zero projection onto degrees <=256.
  # Actual original and rational comparison faults need not be orthogonal:
  # their complete norm bounds are still included in this projection error.
  projected_error=up(root(finite)+original_fault+root(rational));projected_lower=down(max(F(0),rootdown(nl)-projected_error)**2)
  rl=max(F(r['complete_direct_residual_actual_D_energy_lower']),projected_lower);rh=F(r['complete_direct_residual_actual_D_energy_upper']);assert 0<rl<=rh
  b=bounds['polynomial_augmented_action_certificates'][parity];mu=F(b['fresh_augmented_N_D_lower']);nu=F(b['fresh_augmented_N_D_upper']);lam=F(b['augmentation_coefficient']);pr=forms['parity_materialized_four_trial_response_certificates'][parity];F0=[[(F(a),F(b)) for a,b in row] for row in pr['original_trial_form_intervals']];Gy=[[(F(a),F(b)) for a,b in row] for row in pr['frequency_trial_Gram_intervals']];y=list(map(F,r['selected_trial_coefficients']))
  cl,ch=direct.center_intervals(F0,Gy,y,lam);tl=down(cl+rl/nu);u=[1-y[0],-y[1],-y[2],-y[3]];ql,qh=direct.quadratic(F0,u);al,ah=direct.quadratic(Gy,y);dh=up(qh+lam*ah-rl/nu)
  actualtl=max(F(r['actual_original_action_inverse_response_lower']),tl);actualth=F(r['actual_original_action_inverse_response_upper']);actualdl=max(F(r['actual_signed_gap_lower']),down(F0[0][0][0]-actualth));actualdh=min(F(r['actual_signed_gap_upper']),dh,up(F0[0][0][1]-actualtl));assert actualtl<=actualth and actualdl<=actualdh
  # For this fixed actual Z, any certified upper-center >= cl and any
  # full residual energy upper >= rl. Thus C_upper+r_upper/mu >= this floor.
  # This applies to the specified coercivity formula, not the true response.
  floor=down(cl+rl/mu);ceiling=up(F0[0][0][1]-floor);assert floor>F0[0][0][1] and ceiling<0
  necessary=rl/(F0[0][0][1]-cl);sufficient=rh/(F0[0][0][0]-ch);assert 0<mu<necessary<sufficient<nu
  # kappa is a hypothetical residual-specific inverse bound: e*N^-1e <= ||e||^2/kappa.
  # A value strictly above sufficient would close this fixed source test using
  # the current upper residual norm, if its inverse inequality were certified.
  assert ch+rh/sufficient==F0[0][0][0]
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],retained_residual_center_origin='RC251 degree 256',retained_model_center_D_energy_lower=str(down(nl)),retained_model_center_D_energy_upper=str(up(nh)),finite_coefficient_rounding_D_energy_upper=str(finite),complete_original_model_fault_D_norm_upper=str(original_fault),complete_rational_augmentation_fault_D_error_squared_upper=str(rational),projected_actual_residual_error_D_norm_upper=str(projected_error),omitted_model_output_projection_exactly_zero=True,global_model_faults_not_assumed_orthogonal=True,projected_actual_residual_D_energy_lower=str(projected_lower),complete_direct_residual_actual_D_energy_lower=str(rl),previous_complete_residual_D_energy_lower=r['complete_direct_residual_actual_D_energy_lower'],complete_direct_residual_actual_D_energy_upper=str(rh),unchanged_complete_direct_residual_D_error_squared_upper=r['complete_direct_residual_D_error_squared_upper'],variational_center_lower=str(cl),variational_center_upper=str(ch),augmented_global_D_coercivity_lower=str(mu),augmented_global_D_operator_upper=str(nu),direct_inverse_response_lower=str(tl),direct_signed_gap_upper=str(dh),actual_original_action_inverse_response_lower=str(actualtl),previous_original_action_inverse_response_lower=r['actual_original_action_inverse_response_lower'],actual_original_action_inverse_response_upper=str(actualth),actual_signed_gap_lower=str(actualdl),actual_signed_gap_upper=str(actualdh),inverse_lower_improved=actualtl>F(r['actual_original_action_inverse_response_lower']),fixed_trial_coercivity_formula_obstruction=dict(inverse_UPPER_formula_floor=str(floor),signed_gap_LOWER_formula_ceiling=str(ceiling),original_source_form_upper=str(F0[0][0][1]),all_improved_residual_norm_upper_bounds_covered=True,selected_actual_trial_fixed=True,current_global_mu_fixed=True,tail_refinement_alone_cannot_close_this_formula=True,true_inverse_lower_bound_claimed=False,actual_negative_gap_claimed=False,all_four_trial_coefficients_obstructed=False),hypothetical_residual_specific_inverse_budget=dict(inequality='e*D N^-1 e <= ||e||_D^2/kappa',necessary_strict_kappa_floor=str(necessary),necessary_kappa_to_current_mu_ratio=str(necessary/mu),sufficient_strict_kappa_threshold_using_current_enclosures=str(sufficient),sufficient_kappa_to_current_mu_ratio=str(sufficient/mu),kappa_inequality_certified=False,global_N_coercivity_improvement_claimed=False),signed_gap_positive_certified=actualdl>0,actual_negative_gap_proved=actualdh<0))
 return dict(milestone='RC254',starting_commit='0b32221fc4a32a11ec5de1304cf0ac24c3230878',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_response_source_count=2,response_trials_per_parity=4,projected_residual_gate_audit_certificates=rows,source_and_trial_spaces_unchanged=True,retained_direct_residual_output_degree_unchanged=256,all_original_and_rational_augmentation_model_faults_preserved=True,exact_controls=controls(),new_response_enclosures_intersected_with_RC253=True,fixed_trial_tail_only_refinement_closure_obstructed_for_current_mu=True,stronger_residual_inverse_bound_required_or_trial_must_change=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC255: strengthen the residual-specific inverse estimate or change the actual response trial; further tail refinement alone cannot close the fixed-trial current-mu source tests')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC254 VALIDATED: projected residual lower bounds and fixed-trial inverse-gate audit; Stage I open',flush=True)
