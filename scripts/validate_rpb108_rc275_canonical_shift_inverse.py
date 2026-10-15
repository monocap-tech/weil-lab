"""RC275: retain L >= D-rI in the inverse bound; positive auxiliary pivot pair."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc274_mixed_diagonal_inverse as parent
import validate_rpb108_rc230_augmentation_range_bridge as bridge
import validate_rpb108_rc268_two_pivot_schur_reduction as signed
ROOT=parent.ROOT;orig=parent.orig;up=parent.up;down=parent.down;root=parent.root;p=bridge.p;B=parent.B;END=parent.END;SHIFT=F(789,125)
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc274_mixed_diagonal_inverse.json':'2059b48ee4e0b22a0dfb8a9a803644cf0c5fb5f8','notes/RPB108_RC274_MIXED_DIAGONAL_INVERSE_20261014.md':'217130affc5b5ce8f4bac17efa9e68cd17d8d440'})
HELPER_PINS['scripts/validate_rpb108_rc274_mixed_diagonal_inverse.py']='f65f8ac22b74ef3e608a84109c65a16719dc45e0'

def controls():
 D=[[F([4,8,12][i] if i==j else 0) for j in range(3)] for i in range(3)];I=[[F(i==j) for j in range(3)] for i in range(3)]
 h=[[F(3),F(1,4),F(0)],[F(1,4),F(1),F(0)],[F(0),F(0),F(1)]];R=[[F([1,2,3][i] if i==j else 0) for j in range(3)] for i in range(3)]
 r=F(6);L=p.add(p.add(p.add(D,h),R),p.scale(r,I),-1);P=[[F(i==j==0) for j in range(3)] for i in range(3)]
 assert p.psd(h) and p.psd(R) and p.psd(L)
 assert p.psd(p.add(L,p.add(D,p.scale(r,I),-1),-1))
 alpha=F(1,100);kap=F(1,10)
 G=p.add(p.scale(alpha,L),p.scale(kap,P));lower=p.add(p.scale(alpha,p.add(D,p.scale(r,I),-1)),p.scale(kap,P))
 assert p.psd(p.add(G,lower,-1)) and p.inv(lower) and p.psd(lower)
 N=p.mm(p.inv(D),G);bound=p.mm(p.inv(D),lower)
 assert p.mm(N,D)!=p.mm(D,N)
 e=[[F(1,3)],[F(2,5)],[F(-1,7)]]
 actual=p.mm(p.trans(e),p.mm(D,p.mm(p.inv(N),e)))[0][0]
 paid=p.mm(p.trans(e),p.mm(D,p.mm(p.inv(bound),e)))[0][0];assert actual<=paid
 # Two positive parity pivots do not imply positivity of the remaining block.
 gate=[[F(1),F(0),F(2),F(0)],[F(0),F(1),F(0),F(2)],[F(2),F(0),F(1),F(0)],[F(0),F(2),F(0),F(1)]]
 reduced=[[F(-3),F(0)],[F(0),F(-3)]]
 assert signed.inertia(gate)==dict(positive=2,negative=2,zero=0)
 assert signed.inertia(reduced)==dict(positive=0,negative=2,zero=0)
 return dict(canonical_shift_identity_with_positive_remainders_checked=True,noncommuting_D_inverse_order_control=True,exact_response_upper=str(paid),exact_response=str(actual),positive_pair_does_not_close_remaining_Schur_form=True)

def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('274_mixed_diagonal_inverse');sources=get('272_projection_source_responses');refs=get('271_diagonal_projection_reference')['projection_reference_models'][0];coverage=get('270_threshold_adapted_coverage')['threshold_adapted_coverage_certificates'][0];metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B)
 harmonics=[F(0)]
 for n in range(1,END+3):harmonics.append(harmonics[-1]+F(1,n))
 dlo=[down(h+sl) for h in harmonics];dhi=[up(h+sh) for h in harmonics];rows=[]
 for base,old in enumerate(prior['projection_mixed_inverse_response_certificates']):
  source=sources['projection_source_response_certificates'][base];ref=refs['parity_projection_reference_certificates'][base]
  retained=set(ref['retained_Legendre_degrees']);first=max(retained)+2;firsttail=END+1 if (END+1)%2==base else END+2
  assert dlo[first]>SHIFT
  lam=F(ref['new_exact_projection_augmentation_coefficient']);C=F(old['original_physical_negative_allowance_C']);assert lam>C
  b=coverage['parity_certificates'][base]['original_concentration_budget'];gamma=F(b['reference_floor']);penalty=F(b['low_band_penalty_upper']);delta2=F(coverage['parity_certificates'][base]['Fourier_restriction_squared_tail_upper'])
  energy=[];rounding=[]
  for v in source['retained_actual_residual_center'][:65]:
   n=v['degree'];c=F(v['coefficient']);rad=F(v['source_D_inverse_radius']);energy.append((n,up(orig.mass(n)*dhi[n]*c*c)));rounding.append((n,up(orig.mass(n)*dhi[n]*rad*rad)))
  for v in old['residual_physical_numerator_intervals_65_through_2048']:
   n=v['degree'];maximum=max(abs(F(v['lower'])),abs(F(v['upper'])));energy.append((n,up(orig.mass(n)*maximum**2/dlo[n])))
  tail=F(old['complete_full_trial_model_tail_D_energy_upper']);eps=F(old['new_complete_global_D_fault_norm_upper'])
  proposals={F(k,10) for k in range(3,10)}|{F(99,100),F(old['selected_mixed_inverse_certificate']['Young_parameter']),F(66,100) if not base else F(47,100)};choices=[]
  for theta in sorted(proposals,reverse=reverse):
   alpha=down(gamma-penalty*(1+1/theta)*delta2);kap=lam-penalty*(1+theta)
   if alpha<=0 or kap<=SHIFT*alpha:continue
   first_Young=down(alpha*(1-SHIFT/dlo[first]));first_original=down(1-C/dlo[first]);assert first_Young>0 and first_original<0
   limit=down(first_Young/(first_Young-first_original));assert 0<limit<1
   for j in sorted(range(19),reverse=reverse):
    mix=F(j,20)*limit;floor=down((1-mix)*first_Young+mix*first_original);assert floor>0
    def diag(n):
     if n in retained:return down((1-mix)*alpha+mix+((1-mix)*(kap-SHIFT*alpha)+mix*(lam-C))/dhi[n])
     return down((1-mix)*alpha+mix-((1-mix)*SHIFT*alpha+mix*C)/dlo[n])
    terms=[up(e/diag(n)) for n,e in energy if e];sr=[up(e/diag(n)) for n,e in rounding if e]
    if reverse:terms.reverse();sr.reverse()
    model=up(sum(terms,F(0))+tail/diag(firsttail));source_rounding=up(sum(sr,F(0)));fault=up(eps*eps/floor)
    correction=up((root(model)+root(source_rounding)+root(fault))**2)
    choices.append((correction,theta,mix,dict(Young_parameter=str(theta),canonical_Young_floor=str(alpha),retained_projection_coefficient=str(kap),retained_shifted_coefficient=str(kap-SHIFT*alpha),first_omitted_canonical_shift_floor_lower=str(first_Young),original_first_omitted_diagonal_lower=str(first_original),mixing_parameter=str(mix),mixing_fraction_of_safe_limit=str(F(j,20)),safe_mixing_limit_lower=str(limit),global_D_floor_lower=str(floor),tail_inverse_diagonal_lower=str(diag(firsttail)),complete_model_weighted_energy_upper=str(model),source_rounding_weighted_energy_upper=str(source_rounding),remaining_global_fault_weighted_energy_upper=str(fault),complete_added_inverse_correction_upper=str(correction))))
  correction,_,_,selected=min(choices,key=lambda v:(v[0],v[1],v[2]));assert correction<F(old['selected_mixed_inverse_certificate']['complete_added_inverse_correction_upper'])
  upper=min(F(old['actual_auxiliary_source_inverse_response_upper']),up(F(source['variational_inverse_center_upper'])+correction));lower=F(old['actual_auxiliary_source_inverse_response_lower']);mass=F(source['native_auxiliary_source_mass']);gap=down(mass-lam*upper);gaphi=F(old['new_native_auxiliary_gate_upper']);assert lower<=upper and 0<gap<=gaphi
  # A fresh all-source spectral floor, independent of the optimized source mix.
  uniform_theta=F(99,100);uniform_alpha=down(gamma-penalty*(1+1/uniform_theta)*delta2);uniform_kap=lam-penalty*(1+uniform_theta)
  assert uniform_kap>SHIFT*uniform_alpha>0
  mu=down(uniform_alpha*(1-SHIFT/dlo[first]));nu=F(ref['D_energy_reference_upper']);oldmu=F(ref['D_energy_reference_lower']);assert oldmu<mu<nu
  budgets=bridge.polynomial_budgets(mu,nu,up(1/sl),lam)
  rows.append(dict(parity=old['parity'],source=old['source'],exact_trial_coefficients=old['exact_trial_coefficients'],first_omitted_projection_degree=first,first_omitted_D_energy_weight_lower=str(dlo[first]),all_canonical_shift_inverse_candidates=[v[3] for v in sorted(choices,key=lambda v:(v[1],v[2]))],selected_canonical_shift_inverse_certificate=selected,previous_added_inverse_correction_upper=old['selected_mixed_inverse_certificate']['complete_added_inverse_correction_upper'],actual_auxiliary_source_inverse_response_lower=str(lower),actual_auxiliary_source_inverse_response_upper=str(upper),new_native_auxiliary_gate_lower=str(gap),new_native_auxiliary_gate_upper=str(gaphi),native_gate_inverse_pivot_upper=str(up(1/gap)),native_physical_auxiliary_normalized_gate_floor_lower=str(down(gap/mass)),new_native_gate_positive_certified=True,uniform_all_source_Young_parameter=str(uniform_theta),uniform_all_source_canonical_Young_floor=str(uniform_alpha),uniform_all_source_retained_projection_coefficient=str(uniform_kap),fresh_all_source_N_D_floor_lower=str(mu),previous_all_source_N_D_floor_lower=str(oldmu),unchanged_all_source_N_D_upper=str(nu),fresh_all_source_condition_number_upper=str(up(nu/mu)),conditional_exact_action_inverse_budgets=budgets,remaining_auxiliary_native_degrees=ref['retained_Legendre_degrees'][1:],remaining_auxiliary_Schur_dimension=ref['rank']-1))
  print('RC275 '+old['parity']+': correction '+str(float(correction))+'; positive native gate '+str(float(gap))+'; all-source D floor '+str(float(mu)),flush=True)
 remaining=sum(r['remaining_auxiliary_Schur_dimension'] for r in rows);assert remaining==606
 pair=min(F(r['native_physical_auxiliary_normalized_gate_floor_lower']) for r in rows);assert pair>0
 return dict(milestone='RC275',starting_commit='1ea489864b2ba62f5f94c521b8f55c79128e5683',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,canonical_shift_response_certificates=rows,exact_controls=controls(),canonical_form_identity='L=D+h-(789/125)I+R; h>=0 and R>=0',canonical_shift_lower_form='L>=D-(789/125)I',positive_remainder_is_supported_Fourier_log_one_plus_e_over_abs_xi=True,new_actual_auxiliary_source_count=2,response_trials_per_parity=4,projection_reference_rank_unchanged=608,both_projection_auxiliary_source_gates_positive=True,opposite_parity_gate_pairing_exactly_zero=True,positive_pair_physical_auxiliary_metric_floor_lower=str(pair),remaining_exact_projection_auxiliary_Schur_dimension=remaining,remaining_Schur_cross_column_payment_required=True,remaining_projection_Schur_matrix_evaluated=False,full_projection_auxiliary_norm_below_one_certified=False,old_signed_rank_639_reference_and_pivots_preserved=True,old_inverse_budgets_transferred=False,actual_new_augmented_operator_actions_performed=False,actual_residual_model_and_trial_unchanged=True,all_original_model_and_global_faults_preserved=True,original_below_one_hundredth_count_upper_preserved=608,original_nonpositive_count_upper_preserved=582,positive_pair_not_subtracted_from_independent_582_bound=True,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC276: extend the rank-608 projection auxiliary gate beyond the positive P0/P1 pair; certify its two same-parity cross columns and the remaining 235-even/371-odd Schur form, retaining weighted residual covariance')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC275 VALIDATED: positive projection auxiliary pair; full gate open',flush=True)
