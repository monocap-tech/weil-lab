"""RC274: resolve the secondary trials and mix two global diagonal lower forms."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import argparse,hashlib,json
import validate_rpb108_rc273_projection_original_tail as parent
ROOT=parent.ROOT;orig=parent.orig;up=parent.up;down=parent.down;root=parent.root;native=parent.native;B=parent.B;END=parent.END
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc273_projection_original_tail.json':'2ebfabb63ec680c491a69b6e159ab16e0ab204fd','notes/RPB108_RC273_PROJECTION_ORIGINAL_TAIL_20261014.md':'c009113b933084c229fc516c05bc147d72fe2860'})
HELPER_PINS['scripts/validate_rpb108_rc273_projection_original_tail.py']='4f6163f36097a97190ba50b5e032d942106122ef'

def regular_bound(data,reverse):
 coefficients=list(map(F,data['regular_kernel_coefficients']));N=len(coefficients)-1;R=2*B;bernstein=[]
 for k in range(N+1):
  terms=[coefficients[j]*R**j*F(comb(k,j),comb(N,j)) for j in range(k+1)]
  if reverse:terms.reverse()
  bernstein.append(sum(terms,F(0)))
 assert N==192 and min(bernstein)>0 and all(bernstein[k+1]<bernstein[k] for k in range(N))
 integrals=[c*B**(j+1)/(j+1) for j,c in enumerate(coefficients)]
 if reverse:integrals.reverse()
 nominal=2*sum(integrals,F(0));fault=R*F(data['regular_kernel_uniform_error_upper']);bound=up(nominal+fault)
 assert 0<bound<R*max(bernstein)
 return bound,dict(polynomial_degree=N,interval_length=str(R),exact_Bernstein_coefficients=list(map(str,bernstein)),all_Bernstein_coefficients_positive=True,all_adjacent_Bernstein_differences_negative=True,nominal_center_row_integral=str(nominal),physical_uniform_kernel_fault_norm_upper=str(up(fault)),complete_actual_regular_operator_norm_upper=str(bound))

def controls():
 p=parent.parent.p
 # Two diagonal lower forms do not permit entrywise maximization.
 A=[[F(2),F(1)],[F(1),F(2)]];D1=[[F(0),F(0)],[F(0),F(1)]];D2=[[F(1),F(0)],[F(0),F(0)]]
 assert p.psd(p.add(A,D1,-1)) and p.psd(p.add(A,D2,-1))
 for t in [F(0),F(1,3),F(9,10)]:
  lower=p.add(p.scale(1-t,D1),p.scale(t,D2));assert p.psd(p.add(A,lower,-1))
  if 0<t<1:assert p.psd(p.add(p.inv(lower),p.inv(A),-1))
 # An explicit obstruction to replacing a convex combination by max(D1,D2).
 X=[[F(1),F(1)],[F(1),F(1)]];L1=[[F(-1),F(0)],[F(0),F(1,2)]];L2=[[F(1,2),F(0)],[F(0),F(-1)]]
 assert p.psd(p.add(X,L1,-1)) and p.psd(p.add(X,L2,-1))
 assert not p.psd(p.add(X,[[F(1,2),F(0)],[F(0),F(1,2)]],-1))
 return dict(global_convex_lower_form_mixing_checked=True,entrywise_maximum_of_lower_forms_not_used=True)

def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 old=get('273_projection_original_tail');sources=get('272_projection_source_responses');ref=get('271_diagonal_projection_reference')['projection_reference_models'][0];coverage=get('270_threshold_adapted_coverage')['threshold_adapted_coverage_certificates'][0];original=get('112_parity_spectral_coverage')
 arithmetic=get('43_native_prime_head');metric=get('129_four_vector_joint_moment');second=get('237_two_trial_signed_response');third=get('240_three_trial_signed_response')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);sm=(sl+sh)/2;a_metric=F(32125,230953)
 regnorm,regproof=regular_bound(get('46_native_archimedean_head'),reverse)
 harmonics=[F(0)]
 for n in range(1,END+3):harmonics.append(harmonics[-1]+F(1,n))
 dlo=[down(h+sl) for h in harmonics];dhi=[up(h+sh) for h in harmonics];rows=[]
 for base,oldr in enumerate(old['projection_original_tail_response_certificates']):
  r=sources['projection_source_response_certificates'][base];y=list(map(F,r['exact_trial_coefficients']));secondary=[F(0)]*(base+5);secondary[base+2]=y[1];secondary[base+4]=y[2]
  pc,ptail,pfault,proof=parent.prime_output(secondary,base,arithmetic,reverse);lookup={v['degree']:v for v in pc}
  assert proof['prime_controls']['chosen_prime_model_parameters']==oldr['prime_projection_certificate']['prime_controls']['chosen_prime_model_parameters']
  full=list(map(F,r['exact_trial_Legendre_coefficients']));primary=list(map(F,oldr['exact_refined_original_input_Legendre_coefficients']))
  assert all(full[n]==primary[n]+(secondary[n] if n<len(secondary) else 0) for n in range(65))
  firsttail=END+1 if (END+1)%2==base else END+2
  etail,endpointproof=parent.endpoint.tail_bound(full,firsttail,sl,harmonics)
  prime_tail=up((root(F(oldr['prime_projection_certificate']['prime_physical_tail_after_2048_upper']))+root(ptail))**2)
  tail=up((root(etail)+root(up(prime_tail/dlo[firsttail])))**2)
  removed=abs(y[1])*root(F(r['original_action_D_squared_error_bounds'][1]))+abs(y[2])*root(F(r['original_action_D_squared_error_bounds'][2]))
  nuisance=F(oldr['remaining_global_original_D_fault_norm_upper'])-removed;assert nuisance>=0
  for scale,action in [(abs(y[1]),second['parity_two_trial_signed_response_certificates'][base]['new_complete_original_action']),(abs(y[2]),third['parity_three_trial_signed_response_certificates'][base]['new_complete_original_action'])]:
   c=action['D_energy_component_squared_errors'];nuisance+=scale*(root(F(c['finite_rounding']))+2*sum((root(F(c[k])) for k in ['regular_kernel','prime_arithmetic','pole_Taylor']),F(0))+root(F(c['regular_omitted_output'])))
  nuisance=up(nuisance+root(up(pfault*pfault/sl)))
  numerator={};energy=[];rounding=[]
  for v in r['retained_actual_residual_center']:
   n=v['degree'];c=F(v['coefficient']);rad=F(v['source_D_inverse_radius'])
   if n<=64:energy.append((n,up(orig.mass(n)*dhi[n]*c*c)));rounding.append((n,up(orig.mass(n)*dhi[n]*rad*rad)));continue
   assert rad==0
   if n%2!=base:assert c==0;energy.append((n,F(0)));continue
   h,hr=native.endpoint(secondary,n,F(0),F(0));assert hr==0
   qlo=down(h+F(lookup[n]['lower']));qhi=up(h+F(lookup[n]['upper']))
   values=[d*c-q for d in [dlo[n],dhi[n]] for q in [qlo,qhi]]
   bound=max(map(abs,values));energy.append((n,up(orig.mass(n)*bound*bound/dlo[n])));numerator[n]=(min(values),max(values))
  for v in oldr['new_combined_original_output_129_through_2048']:
   n=v['degree'];h,hr=native.endpoint(secondary,n,F(0),F(0));assert hr==0
   qlo=down(F(v['combined_original_physical_numerator_lower'])+h+F(lookup[n]['lower']));qhi=up(F(v['combined_original_physical_numerator_upper'])+h+F(lookup[n]['upper']))
   bound=max(abs(qlo),abs(qhi));energy.append((n,up(orig.mass(n)*bound*bound/dlo[n])));numerator[n]=(-qhi,-qlo)
  rr=ref['parity_projection_reference_certificates'][base];retained=set(rr['retained_Legendre_degrees']);firstoutside=max(retained)+2;lam=F(rr['new_exact_projection_augmentation_coefficient'])
  allowance=up(F(789,125)+regnorm+F(original['parity_coverage_certificates'][base]['physical_negative_nonarch_allowance']));assert lam>allowance
  outside_original_lower=down(1-allowance/dlo[firstoutside]);assert outside_original_lower<0
  b=coverage['parity_certificates'][base]['original_concentration_budget'];gamma=F(b['reference_floor']);penalty=F(b['low_band_penalty_upper']);delta2=F(coverage['parity_certificates'][base]['Fourier_restriction_squared_tail_upper'])
  oldtheta=F(oldr['selected_projection_inverse_certificate']['Young_parameter']);thetas={F(k,10) for k in range(3,10)}|{F(99,100),oldtheta,F(77,100) if not base else F(61,100)};choices=[]
  for theta in sorted(thetas,reverse=reverse):
   alpha=down(gamma-penalty*(1+1/theta)*delta2);kap=lam-penalty*(1+theta)
   if alpha<=0 or kap<=0:continue
   d=down(a_metric*alpha);limit=down(d/(d-outside_original_lower));assert 0<limit<1
   for j in sorted(range(19),reverse=reverse):
    mix=F(j,20)*limit;floor=down((1-mix)*d+mix*outside_original_lower);assert floor>0
    def diag(n):
     if n in retained:return down((1-mix)*d+mix+((1-mix)*kap+mix*(lam-allowance))/dhi[n])
     return down((1-mix)*d+mix*(1-allowance/dlo[n]))
    terms=[up(e/diag(n)) for n,e in energy if e];sourceround=[up(e/diag(n)) for n,e in rounding if e]
    if reverse:terms.reverse();sourceround.reverse()
    model=up(sum(terms,F(0))+tail/diag(firsttail));roundbound=up(sum(sourceround,F(0)));fault=up(nuisance*nuisance/floor)
    correction=up((root(model)+root(roundbound)+root(fault))**2)
    choices.append((correction,theta,mix,dict(Young_parameter=str(theta),mixing_parameter=str(mix),mixing_fraction_of_safe_limit=str(F(j,20)),safe_mixing_parameter_limit_lower=str(limit),global_mixed_D_floor_lower=str(floor),canonical_Young_floor=str(alpha),retained_projection_coefficient=str(kap),outside_first_original_D_lower=str(outside_original_lower),complete_model_weighted_energy_upper=str(model),tail_model_weighted_energy_upper=str(up(tail/diag(firsttail))),source_rounding_weighted_energy_upper=str(roundbound),remaining_global_fault_weighted_energy_upper=str(fault),complete_added_inverse_correction_upper=str(correction))))
  correction,_,_,selected=min(choices,key=lambda v:(v[0],v[1],v[2]));assert correction<F(oldr['selected_projection_inverse_certificate']['complete_added_inverse_correction_upper'])
  upper=min(F(oldr['actual_auxiliary_source_inverse_response_upper']),up(F(r['variational_inverse_center_upper'])+correction));lower=F(oldr['actual_auxiliary_source_inverse_response_lower']);mass=F(r['native_auxiliary_source_mass']);gap=down(mass-lam*upper);gaphi=F(oldr['new_native_auxiliary_gate_upper']);assert lower<=upper and gap<=gaphi
  rows.append(dict(parity=r['parity'],source=r['actual_auxiliary_source'],exact_trial_coefficients=r['exact_trial_coefficients'],secondary_input_Legendre_coefficients=list(map(str,secondary)),secondary_prime_projection_certificate=proof,secondary_prime_intervals_65_through_2048=pc,full_trial_endpoint_tail_certificate=endpointproof,combined_full_prime_physical_tail_after_2048_upper=str(prime_tail),complete_full_trial_model_tail_D_energy_upper=str(tail),removed_old_secondary_trial_D_fault_norm_upper=str(up(removed)),new_complete_global_D_fault_norm_upper=str(nuisance),original_physical_negative_allowance_C=str(allowance),residual_physical_numerator_intervals_65_through_2048=[dict(degree=n,lower=str(v[0]),upper=str(v[1])) for n,v in sorted(numerator.items())],mixed_inverse_candidate_certificates=[v[3] for v in sorted(choices,key=lambda v:(v[1],v[2]))],selected_mixed_inverse_certificate=selected,actual_auxiliary_source_inverse_response_lower=str(lower),actual_auxiliary_source_inverse_response_upper=str(upper),new_native_auxiliary_gate_lower=str(gap),new_native_auxiliary_gate_upper=str(gaphi),new_native_gate_positive_certified=gap>0,actual_negative_gate_proved=gaphi<0,previous_correction_upper=oldr['selected_projection_inverse_certificate']['complete_added_inverse_correction_upper'],previous_native_gate_lower=oldr['new_native_auxiliary_gate_lower'],original_trial_unchanged=True))
  print('RC274 '+r['parity']+': correction '+str(float(correction))+'; native gate lower '+str(float(gap)),flush=True)
 return dict(milestone='RC274',starting_commit='a95e332f9ab0a36950bb398591b08570581a868f',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,regular_kernel_Schur_norm_certificate=regproof,projection_mixed_inverse_response_certificates=rows,exact_controls=controls(),new_positive_native_gate_parities=[r['parity'] for r in rows if r['new_native_gate_positive_certified']],actual_auxiliary_source_count=2,reference_full_source_rank=608,response_trials_per_parity=4,all_four_trial_original_tails_paid=True,endpoint_nonnegativity_used_in_original_diagonal_form=True,lower_forms_combined_by_single_global_convex_weight=True,entrywise_maximum_of_lower_forms_used=False,legacy_rank_639_reference_and_two_signed_pivots_preserved=True,full_projection_auxiliary_response_matrix_evaluated=False,full_projection_auxiliary_norm_below_one_certified=False,original_below_one_hundredth_count_upper_preserved=608,original_nonpositive_count_upper_preserved=582,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC275: strengthen the remaining even projection response or extend the full auxiliary cross-response matrix; a positive individual gate does not close the full rank-608 criterion')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC274 VALIDATED: mixed diagonal inverse and secondary tails; full gate open',flush=True)
