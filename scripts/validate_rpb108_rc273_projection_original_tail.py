"""RC273: combined original prime/endpoint output for the projection responses."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc272_projection_source_responses as parent
import validate_rpb108_rc262_prime_tail_source_1024 as high
import validate_rpb108_rc253_prime_boundary_tail as prime
import validate_rpb108_rc252_signed_endpoint_tail as endpoint
ROOT=parent.ROOT;orig=parent.orig;up=parent.up;down=parent.down;root=parent.root;m=high.m;native=prime.native;B=F(11,10);END=2048
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc272_projection_source_responses.json':'36de4fd3468640c2181b608d0f9d9fbc48bb0814','notes/RPB108_RC272_PROJECTION_SOURCE_RESPONSES_20261014.md':'2b2129c1751936a3f7a6cfff30ce89dd9c35169f'})
HELPER_PINS['scripts/validate_rpb108_rc272_projection_source_responses.py']='797d6b5120c4ed6dc8c4eaa648fc474b6c72cdcb'

def prime_output(a,parity,arithmetic,reverse):
 q=native.input_poly(a);old=native.OUT
 try:
  native.OUT=64;low,tail,fault,proof=native.prime_action(q,a,parity,arithmetic,reverse)
 finally:native.OUT=old
 assert native.OUT==128
 print('RC273 '+('even' if not parity else 'odd')+' combined prime model through 64 complete',flush=True)
 segments=prime.model_segments(q,proof['chosen_prime_model_parameters'],parity)
 assert native.segment_digest(segments)==proof['prime_segment_polynomial_sha256']
 boundaries=[];digits=140 if reverse else 120
 for i in range(len(segments)-1):
  b=segments[i][1]
  if b<0:continue
  jump=[x-y for x,y in zip(segments[i][2],segments[i+1][2])];jc=[orig.project(jump,d) for d in range(len(q))]
  assert not any(native.addpoly(native.input_poly(jc),[-v for v in jump]))
  values=prime.legendre_values(b,len(q)-1);dv=[F(0)]+[d*(b*values[d]-values[d-1])/(b*b-1) for d in range(1,len(q))]
  jv=[m.outer_grid(m.ip(jc[d]*values[d]),digits) for d in range(len(q))];jd=[m.outer_grid(m.ip(jc[d]*dv[d]),digits) for d in range(len(q))]
  boundaries.append((b,jv,jd,high.legendre_intervals(b,reverse)))
 assert len(boundaries)==7
 rows=[];captured=[];checks=[]
 for n in range(65,END+1):
  if n%2!=parity:continue
  parts=[];ln=n*(n+1)
  for b,jv,jd,pn in boundaries:
   value=m.ip(F(0));slope=m.ip(F(0))
   for d in range(len(q)):
    value=m.ia(value,m.isc(jv[d],F(1,ln-d*(d+1))));slope=m.ia(slope,m.isc(jd[d],F(1,ln-d*(d+1))))
   dp=m.isc(m.ia(m.isc(pn[n],b),m.neg(pn[n-1])),F(n)/(b*b-1))
   parts.append(m.isc(m.ia(m.im(slope,pn[n]),m.neg(m.im(value,dp))),1-b*b))
  if reverse:parts.reverse()
  v=m.ip(F(0))
  for part in parts:v=m.ia(v,part)
  v=m.outer_grid(m.isc(v,2*n+1),60);assert v[1]-v[0]<F(1,10**50)
  if n in [65,66]:
   exact=F(2*n+1,2)*sum((orig.integral(orig.product(poly,orig.legendre(n)),l,r) for l,r,poly in segments),F(0))
   assert v[0]<=exact<=v[1];checks.append(n)
  minimum=0 if v[0]<=0<=v[1] else min(abs(v[0]),abs(v[1]))
  captured.append(down(orig.mass(n)*minimum**2));rows.append(dict(degree=n,lower=str(v[0]),upper=str(v[1])))
  if n in [511,512,1023,1024,1535,1536,2047,2048]:print('RC273 '+('odd' if parity else 'even')+' combined prime through '+str(n),flush=True)
 if reverse:captured.reverse()
 remaining=up(tail-sum(captured,F(0)));assert 0<remaining<tail
 return rows,remaining,fault,dict(prime_controls=proof,direct_high_degree_integral_control_indices=checks,prime_projection_cutoff=END,additional_prime_capture_lower=str(down(sum(captured,F(0)))),prime_physical_tail_after_64_upper=str(tail),prime_physical_tail_after_2048_upper=str(remaining),low_prime_coefficient_digest=native.segment_digest([(F(0),F(64),low)]),all_cross_prime_and_input_terms_preserved=True,Legendre_generation_grid_digits=1500,Legendre_replay_grid_digits=1540,static_generation_grid_digits=120,static_replay_grid_digits=140,coefficient_output_grid_digits=60)

def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 old=get('272_projection_source_responses');refs=get('271_diagonal_projection_reference')['projection_reference_models'][0];coverage=get('270_threshold_adapted_coverage')['threshold_adapted_coverage_certificates'][0]
 first=get('245_source_refined_response');last=get('242_residual_original_actions');arithmetic=get('43_native_prime_head');metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);a_metric=F(32125,230953)
 harmonics=[F(0)]
 for n in range(1,END+3):harmonics.append(harmonics[-1]+F(1,n))
 dlo=[down(h+sl) for h in harmonics];dhi=[up(h+sh) for h in harmonics];rows=[]
 for base,r in enumerate(old['projection_source_response_certificates']):
  y=list(map(F,r['exact_trial_coefficients']));R=list(map(F,last['parity_residual_original_action_certificates'][base]['exact_input_Legendre_coefficients']))
  A=[y[3]*v for v in R];A[base]+=y[0]
  pc,ptail,pfault,proof=prime_output(A,base,arithmetic,reverse)
  firsttail=END+1 if (END+1)%2==base else END+2
  etail,ep=endpoint.tail_bound(A,firsttail,sl,harmonics)
  model_tail=up((root(etail)+root(up(ptail/dlo[firsttail])))**2)
  comp0=first['parity_source_refined_response_certificates'][base]['refined_complete_original_source_action']['D_energy_component_squared_errors'];compR=last['parity_residual_original_action_certificates'][base]['D_energy_component_squared_errors']
  # Low blocks use the old centers. High prime output is a fresh common model.
  # Pay all old global faults twice, plus fresh high prime parameter faults.
  nuisance=F(0)
  for scale,comp in [(abs(y[0]),comp0),(abs(y[3]),compR)]:
   nuisance+=scale*(root(F(comp['finite_rounding']))+2*sum((root(F(comp[k])) for k in ['regular_kernel','prime_arithmetic','pole_Taylor']),F(0))+root(F(comp['regular_omitted_output'])))
  nuisance+=abs(y[1])*root(F(r['original_action_D_squared_error_bounds'][1]))+abs(y[2])*root(F(r['original_action_D_squared_error_bounds'][2]))+root(up(pfault*pfault/sl))
  nuisance=up(nuisance)
  output=[]
  for v in pc:
   n=v['degree']
   if n<=128:continue
   h,rad=native.endpoint(A,n,F(0),F(0));assert rad==0
   lo=down(h+F(v['lower']));hi=up(h+F(v['upper']))
   output.append(dict(degree=n,combined_original_physical_numerator_lower=str(lo),combined_original_physical_numerator_upper=str(hi)))
  ref=refs['parity_projection_reference_certificates'][base];retained=set(ref['retained_Legendre_degrees']);lam=F(ref['new_exact_projection_augmentation_coefficient'])
  b=coverage['parity_certificates'][base]['original_concentration_budget'];gamma=F(b['reference_floor']);penalty=F(b['low_band_penalty_upper']);delta2=F(coverage['parity_certificates'][base]['Fourier_restriction_squared_tail_upper'])
  assert END>max(retained)
  choices=[]
  for k in sorted(range(1,100),reverse=reverse):
   theta=F(k,100);alpha=down(gamma-penalty*(1+1/theta)*delta2);kap=lam-penalty*(1+theta)
   if alpha<=0 or kap<=0:continue
   floor=down(a_metric*alpha)
   weight=lambda n:up(1/(floor+(kap/dhi[n] if n in retained else 0)))
   low=[];rounding=[];inside=[];outside=[]
   for v in r['retained_actual_residual_center']:
    n=v['degree'];c=F(v['coefficient']);rad=F(v['source_D_inverse_radius']);w=weight(n)
    low.append(up(orig.mass(n)*dhi[n]*c*c*w));rounding.append(up(orig.mass(n)*dhi[n]*rad*rad*w))
   for v in output:
    n=v['degree'];bound=max(abs(F(v['combined_original_physical_numerator_lower'])),abs(F(v['combined_original_physical_numerator_upper'])))
    term=up(orig.mass(n)*bound*bound*weight(n)/dlo[n]);(inside if n in retained else outside).append(term)
   if reverse:low.reverse();rounding.reverse();inside.reverse();outside.reverse()
   lowenergy=up(sum(low,F(0)));within=up(sum(inside,F(0)));beyond=up(sum(outside,F(0)));tailweighted=up(model_tail/floor);model=up(lowenergy+within+beyond+tailweighted);rr=up(sum(rounding,F(0)));fault=up(nuisance*nuisance/floor)
   correction=up((root(model)+root(rr)+root(fault))**2)
   choices.append((correction,theta,dict(Young_parameter=str(theta),canonical_floor=str(alpha),retained_projection_coefficient=str(kap),global_D_floor=str(floor),old_low_center_weighted_energy_upper=str(lowenergy),new_output_inside_projection_weighted_energy_upper=str(within),new_output_outside_projection_weighted_energy_upper=str(beyond),model_tail_above_2048_weighted_energy_upper=str(tailweighted),complete_model_weighted_energy_upper=str(model),source_rounding_weighted_energy_upper=str(rr),remaining_global_fault_weighted_energy_upper=str(fault),complete_added_inverse_correction_upper=str(correction))))
  correction,_,selected=min(choices,key=lambda v:(v[0],v[1]));assert correction<F(r['selected_retained_projection_inverse_certificate']['complete_added_inverse_residual_correction_upper'])
  upper=min(F(r['actual_auxiliary_source_inverse_response_upper']),up(F(r['variational_inverse_center_upper'])+correction));lower=F(r['actual_auxiliary_source_inverse_response_lower']);mass=F(r['native_auxiliary_source_mass']);gap=down(mass-lam*upper);gaphi=F(r['new_native_auxiliary_gate_upper']);assert lower<=upper and gap<=gaphi
  rows.append(dict(parity=r['parity'],source=r['actual_auxiliary_source'],exact_trial_coefficients=r['exact_trial_coefficients'],exact_refined_original_input_Legendre_coefficients=list(map(str,A)),prime_projection_certificate=proof,prime_output_intervals_65_through_2048=pc,endpoint_tail_certificate=ep,combined_original_model_tail_D_energy_after_2048_upper=str(model_tail),remaining_global_original_D_fault_norm_upper=str(nuisance),new_combined_original_output_129_through_2048=output,all_projection_inverse_weight_candidates=[v[2] for v in sorted(choices,key=lambda v:v[1])],selected_projection_inverse_certificate=selected,previous_inverse_correction_upper=r['selected_retained_projection_inverse_certificate']['complete_added_inverse_residual_correction_upper'],actual_auxiliary_source_inverse_response_lower=str(lower),actual_auxiliary_source_inverse_response_upper=str(upper),previous_inverse_response_upper=r['actual_auxiliary_source_inverse_response_upper'],new_native_auxiliary_gate_lower=str(gap),new_native_auxiliary_gate_upper=str(gaphi),new_native_gate_positive_certified=gap>0,actual_negative_gate_proved=gaphi<0,original_low_center_and_trial_unchanged=True,all_unresolved_secondary_trial_faults_preserved=True))
  print('RC273 '+r['parity']+': correction '+str(float(correction))+'; native gate lower '+str(float(gap)),flush=True)
 return dict(milestone='RC273',starting_commit='9a51c7978992b91dca65c24f3eba62c060fe1550',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,projection_original_tail_response_certificates=rows,actual_auxiliary_source_count=2,reference_full_source_rank=608,response_trials_per_parity=4,prime_output_cutoff=2048,old_low_residual_centers_preserved=True,actual_original_prime_endpoint_output_extended=True,all_original_prime_parameter_and_other_global_faults_paid=True,legacy_rank_639_reference_and_two_signed_pivots_preserved=True,full_projection_auxiliary_response_matrix_evaluated=False,full_projection_auxiliary_norm_below_one_certified=False,original_below_one_hundredth_count_upper_preserved=608,original_nonpositive_count_upper_preserved=582,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC274: use the paid source-tail split to improve projection response trials or extend the coupled auxiliary response range; individual positive gate entries do not prove the full matrix gate')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC273 VALIDATED: combined original output tail; full gate open',flush=True)
