"""RC276: full projection-gate cross-column centers and joint covariance bounds."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc275_canonical_shift_inverse as parent
ROOT=parent.ROOT;orig=parent.orig;p=parent.p;up=parent.up;down=parent.down;root=parent.root
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc275_canonical_shift_inverse.json':'2e55499fe4bb2513313b0cd36310f781f7e44d68','notes/RPB108_RC275_CANONICAL_SHIFT_INVERSE_20261014.md':'492f1a3af199251c48ad77c970bd7c20684e49b3'})
HELPER_PINS['scripts/validate_rpb108_rc275_canonical_shift_inverse.py']='ad5ac0c7a4e3eb5c4a2837237c5ed7fd612e1cb2'

def controls():
 # Complete a norm quadratic at an exactly rational delta.
 gamma=F(1,5);penalty=F(2);lam=F(4);delta=F(1,10)
 beta=gamma-penalty*delta**2;kappa=gamma+lam-penalty-penalty**2*delta**2/beta
 assert beta>0 and kappa>0
 for a,b in [(F(1,3),F(4,5)),(F(7,5),F(1,10))]:
  quadratic=(gamma+lam-penalty)*a*a+beta*b*b-2*penalty*delta*a*b
  assert quadratic-kappa*a*a==beta*(b-penalty*delta*a/beta)**2>=0
 # Two parity-supported cross rows; every within-parity error can correlate.
 M=[[F([2,3,4,5][i] if i==j else 0) for j in range(4)] for i in range(4)];Mi=p.inv(M)
 G=[[F(3),F(0)],[F(0),F(4)]];Glo=[[F(1),F(0)],[F(0),F(2)]]
 Chat=[[F(1,7),F(0),F(-2,9),F(0)],[F(0),F(1,6),F(0),F(1,8)]]
 E=[[F(1,20),F(0),F(1,30),F(0)],[F(0),F(-1,40),F(0),F(1,50)]]
 C=p.add(Chat,E);dual=p.mm(E,p.mm(Mi,p.trans(E)));assert dual[0][1]==dual[1][0]==0
 envelope=[[F(0) for j in range(4)] for i in range(4)]
 for n in range(4):envelope[n][n]=M[n][n]*dual[n%2][n%2]/Glo[n%2][n%2]
 actual=p.mm(p.trans(C),p.mm(p.inv(G),C));weightedE=p.mm(p.trans(E),p.mm(p.inv(Glo),E));center=p.mm(p.trans(Chat),p.mm(p.inv(Glo),Chat))
 assert p.psd(p.add(envelope,weightedE,-1))
 for theta in [F(1,3),F(1),F(3)]:
  paid=p.add(p.scale(1+theta,center),p.scale(1+1/theta,envelope))
  assert p.psd(p.add(paid,actual,-1))
 # Per-entry squared bounds miss the off-diagonal covariance.
 correlated=[[F(1),F(1)],[F(1),F(1)]];I=[[F(1),F(0)],[F(0),F(1)]]
 assert not p.psd(p.add(I,correlated,-1)) and p.psd(p.add(p.scale(F(2),I),correlated,-1))
 return dict(exact_projection_coercivity_completion=True,joint_dual_mass_covariance_bound=True,weighted_cross_Young_payments_checked=True,entrywise_squared_errors_not_used_as_covariance=True,nonzero_same_parity_cross_terms_checked=True)

def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('275_canonical_shift_inverse');sources=get('272_projection_source_responses');refs=get('271_diagonal_projection_reference')['projection_reference_models'][0];coverage=get('270_threshold_adapted_coverage')['threshold_adapted_coverage_certificates'][0]
 assert prior['both_projection_auxiliary_source_gates_positive'] and prior['remaining_exact_projection_auxiliary_Schur_dimension']==606
 ordering=[];rows=[];offset=0
 for base,r in enumerate(prior['canonical_shift_response_certificates']):
  source=sources['projection_source_response_certificates'][base];ref=refs['parity_projection_reference_certificates'][base];degrees=r['remaining_auxiliary_native_degrees']
  assert source['exact_trial_coefficients']==r['exact_trial_coefficients']
  assert degrees==ref['retained_Legendre_degrees'][1:] and len(degrees)==[235,371][base]
  lam=F(ref['new_exact_projection_augmentation_coefficient']);b=coverage['parity_certificates'][base]
  gamma=F(b['original_concentration_budget']['reference_floor']);penalty=F(b['original_concentration_budget']['low_band_penalty_upper']);delta2=F(b['Fourier_restriction_squared_tail_upper']);beta=gamma-penalty*delta2
  exact_kappa=gamma+lam-penalty-penalty*penalty*delta2/beta;kappa=down(exact_kappa);assert beta>0 and exact_kappa>kappa>0
  assert beta*exact_kappa==beta*(gamma+lam-penalty)-penalty*penalty*delta2
  residual=F(r['selected_canonical_shift_inverse_certificate']['complete_added_inverse_correction_upper']);pivot=F(r['new_native_auxiliary_gate_lower']);assert residual>0 and pivot>0
  radius2=up(lam*lam*residual/kappa);weighted_error=up(radius2/pivot)
  Z=list(map(F,source['exact_trial_Legendre_coefficients']));centers=[];dual_terms=[]
  for local,n in enumerate(degrees):
   mass=orig.mass(n);z=Z[n] if n<len(Z) else F(0);center=-lam*mass*z
   centers.append(dict(global_remaining_index=offset+local,Legendre_degree=n,native_mass=str(mass),cross_center=str(center),scalar_entry_error_absolute_upper=str(root(radius2*mass)),center_zero_by_trial_degree=n>=len(Z)))
   ordering.append(dict(index=offset+local,parity=r['parity'],Legendre_degree=n,native_mass=str(mass)))
   dual_terms.append(center*center/mass)
  if reverse:dual_terms.reverse()
  center_dual=sum(dual_terms,F(0));center_payment=center_dual/pivot
  norm_payment=up((root(center_dual)+root(radius2))**2/pivot)
  assert norm_payment>=center_payment and norm_payment>=weighted_error
  factor2=up(2*center_payment+2*weighted_error);assert factor2>=norm_payment
  uniform_auxiliary=up(lam/kappa);assert uniform_auxiliary>1
  coarse_lower=down(1-uniform_auxiliary-norm_payment);assert coarse_lower<0
  rows.append(dict(parity=r['parity'],pivot_source='P'+str(base),remaining_same_parity_dimension=len(degrees),actual_native_pivot_lower=str(pivot),native_inverse_pivot_upper=str(up(1/pivot)),exact_original_reference_gamma=str(gamma),exact_original_low_band_penalty=str(penalty),physical_high_projection_Fourier_squared_norm_upper=str(delta2),physical_complement_reference_beta=str(beta),exact_physical_projection_coercivity=str(exact_kappa),physical_projection_coercivity_lower=str(kappa),complete_inverse_residual_correction_upper=str(residual),augmentation_coefficient=str(lam),complete_cross_center_native_row=centers,cross_center_dual_mass_norm_squared=str(center_dual),cross_error_dual_mass_norm_squared_upper=str(radius2),weighted_cross_error_covariance_native_mass_coefficient_upper=str(weighted_error),exact_center_payment_rank_at_most=1,center_payment_native_mass_operator_norm_upper=str(up(center_payment)),complete_actual_cross_payment_native_mass_operator_norm_upper=str(norm_payment),theta_one_structured_payment_center_factor='2',theta_one_structured_payment_error_native_mass_coefficient_upper=str(up(2*weighted_error)),theta_one_total_payment_native_mass_operator_norm_upper=str(factor2),uniform_full_auxiliary_response_norm_upper=str(uniform_auxiliary),coarse_complete_remaining_Schur_lower_native_mass_coefficient=str(coarse_lower),coarse_remaining_Schur_lower_is_positive=False,actual_negative_direction_proved=False,all_opposite_parity_cross_entries_exactly_zero=True,actual_cross_error_rank_at_most=1,scalar_intervals_not_assumed_independent=True))
  offset+=len(degrees)
  print('RC276 '+r['parity']+': '+str(len(degrees))+' cross centers; dual error squared '+str(float(radius2))+'; weighted covariance coefficient '+str(float(weighted_error)),flush=True)
 assert offset==606 and len(ordering)==606
 return dict(milestone='RC276',starting_commit='dc1c08ac86a1429d475e44921e34efd447cd9dfc',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,projection_cross_column_certificates=rows,remaining_native_auxiliary_ordering=ordering,exact_controls=controls(),projection_reference_rank=608,positive_auxiliary_pivot_count=2,remaining_exact_projection_Schur_dimension=606,complete_cross_column_centers_and_covariance_bounds_materialized=True,actual_cross_matrix_exactly_evaluated=False,full_remaining_principal_response_block_evaluated=False,complete_actual_cross_payment_rank_at_most=2,cross_error_covariance_is_Loewner_not_entrywise=True,cross_center_formula='C_hat_bj=-lambda_b mass_j Z_bj; opposite parity zero',projection_coercivity_formula='kappa=gamma+lambda-p-p^2 delta^2/(gamma-p delta^2)',cross_error_dual_mass_bound='E_b Mass_b^-1 E_b* <= lambda_b^2 residual_b/kappa_b',structured_cross_payment_contract='C* Gamma^-1 C <= (1+theta) Chat* Gamma_lo^-1 Chat + (1+1/theta) direct_sum_b[(radius_b^2/Gamma_lo_b) Mass_b]',remaining_Schur_lower_contract='if F>=F_lo, then R>=F_lo minus the certified full cross payment',new_projection_reference_or_response_trial_introduced=False,actual_new_original_Weil_actions_performed=False,positive_auxiliary_pair_preserved=True,full_projection_auxiliary_norm_below_one_certified=False,legacy_rank_639_reference_and_signed_pivots_preserved=True,original_below_one_hundredth_count_upper_preserved=608,original_nonpositive_count_upper_preserved=582,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC277: bound the remaining principal auxiliary gate F or improve the inverse-response trials enough to tighten the paid cross covariance; the full 606-dimensional Schur inequality remains the acceptance gate')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC276 VALIDATED: complete cross-column covariance contract; full Schur gate open',flush=True)
