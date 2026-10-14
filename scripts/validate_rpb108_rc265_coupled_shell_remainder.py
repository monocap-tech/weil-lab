"""RC265: keep one common omitted-mode energy across inverse Fourier shells."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse,copy,hashlib,json
import validate_rpb108_rc264_frequency_shell_inverse as parent
coercive=parent.coercive;source=parent.source;ROOT=parent.ROOT;orig=parent.orig
up=parent.up;down=parent.down;root=parent.root
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc264_frequency_shell_inverse.json':'d5b2ae62caf2743edc5723e60bf7df3bcc3469c7','notes/RPB108_RC264_FREQUENCY_SHELL_INVERSE_20261014.md':'caf401d8cf7580880a2e6d906e68617ffc35ae79'})
HELPER_PINS['scripts/validate_rpb108_rc264_frequency_shell_inverse.py']='fbe353e40ef63dcf48050f5552acb5dbb83c4021'

def joint_bound(A,R,Yhi,eps0,I,weights,shells):
 assert 0<1/I<weights[0] and all(0<b<a for a,b in zip(weights,weights[1:]))
 flat=up(A/I+(weights[0]-1/I)*Yhi+weights[0]*R+2*(weights[0]-1/I)*eps0)
 deductions=[];constant_deductions=[];controls=[];quadratic_coefficient=weights[0]
 for j,s in enumerate(shells):
  dw=weights[j]-weights[j+1];K=F(s['high_mode_trace_certificate']['high_space_band_operator_norm_upper']);Y=F(s['retained_Fourier_certificate']['outside_physical_Fourier_energy_lower']);assert 0<=K<=1 and 0<=Y<=A
  eps=up(root(up((A-Y)*K*R)));constant=F(s['model_outside_energy_lower'])
  # This value is a joint-bound endpoint at u=1, NOT a tail lower bound
  # for an unknown ||q||. The same u=||q||/sqrt(R) is used in every shell.
  endpoint=down(Y+(1-K)*R-2*eps);use_quadratic=endpoint>constant
  effective=max(constant,endpoint)
  if use_quadratic:quadratic_coefficient-=dw*(1-K)
  deductions.append(down(dw*effective));constant_deductions.append(down(dw*constant))
  controls.append(dict(bandwidth_ratio=s['bandwidth_ratio'],weight_drop=str(dw),high_space_band_operator_norm_upper=str(K),band_cross_at_full_R_absolute_upper=str(eps),constant_actual_model_tail_lower=str(constant),joint_quadratic_at_full_R=str(endpoint),joint_endpoint_is_not_an_unconditional_tail_lower=True,quadratic_selected=use_quadratic,selected_joint_weight_deduction=str(deductions[-1])))
 assert quadratic_coefficient>=weights[-1]>0
 model=up(flat-sum(deductions,F(0)));constant_model=up(flat-sum(constant_deductions,F(0)));assert 0<model<=constant_model<=flat
 return model,constant_model,flat,quadratic_coefficient,controls

def controls():
 p=coercive.p;ident=[[F(i==j) for j in range(3)] for i in range(3)]
 C0=[[F(1,2),F(0),F(1,100)],[F(0),F(1,3),F(1,200)],[F(1,100),F(1,200),F(1,4)]]
 C=[C0,p.add(C0,p.scale(F(1,10),ident)),p.add(C0,p.scale(F(1,5),ident))]
 assert all(p.psd(c) and p.psd(p.add(ident,c,-1)) and p.mm(c,c)!=c for c in C)
 assert all(p.psd(p.add(b,a,-1)) for a,b in zip(C,C[1:]))
 inner=lambda a,M,b:sum((a[i]*M[i][j]*b[j] for i in range(3) for j in range(3)),F(0))
 v=[F(1),F(1),F(0)];A=F(2);R=F(1);I=F(2);weights=[F(5),F(4),F(3)];Y=[A-inner(v,c,v) for c in C];K=[c[2][2] for c in C];eps=[root((A-y)*k*R) for y,k in zip(Y,K)]
 W=p.add(p.scale(1/I,C[0]),p.scale(weights[0],p.add(C[1],C[0],-1)))
 W=p.add(W,p.scale(weights[1],p.add(C[2],C[1],-1)));W=p.add(W,p.scale(weights[2],p.add(ident,C[2],-1)));assert p.psd(W)
 for selections in product([False,True],repeat=2):
  # Zero is an unconditional tail lower, making this a mixed-branch control.
  coefficient=weights[0]-sum(((weights[j]-weights[j+1])*(1-K[j+1]) for j in range(2) if selections[j]),F(0));assert coefficient>=weights[-1]
  endpoint=A/I+(weights[0]-1/I)*Y[0]+weights[0]*R+2*(weights[0]-1/I)*eps[0]
  endpoint-=sum(((weights[j]-weights[j+1])*(Y[j+1]+(1-K[j+1])*R-2*eps[j+1]) for j in range(2) if selections[j]),F(0))
  for u in [F(0),F(1,5),F(1,2),F(1)]:
   g=v[:];g[2]=u
   value=A/I+(weights[0]-1/I)*Y[0]+weights[0]*R*u*u+2*(weights[0]-1/I)*eps[0]*u
   value-=sum(((weights[j]-weights[j+1])*(Y[j+1]+(1-K[j+1])*R*u*u-2*eps[j+1]*u) for j in range(2) if selections[j]),F(0))
   assert inner(g,W,g)<=value<=endpoint
 c=parent.controls();c.update(common_omitted_energy_parameter_not_fixed_to_upper=True,all_mixed_constant_quadratic_branches_checked=True,positive_joint_quadratic_and_linear_coefficients=True,nested_nonprojective_compressed_band_controls=True)
 return c

def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('264_frequency_shell_inverse');r263=get('263_high_mode_inverse');r262=get('262_prime_tail_source_1024');r261=get('261_materialized_source_fourier');reference=get('256_retained_band_inverse');kernel=get('115_rational_fourier_adjoint');forms=get('247_materialized_four_trial_response');rows=[]
 pi0=F(kernel['rational_pi']);pierr=F(kernel['rational_pi_error_upper'])
 for parity,r in enumerate(prior['frequency_shell_inverse_response_certificates']):
  ref=reference['retained_band_inverse_response_certificates'][parity];old=r263['high_mode_inverse_response_certificates'][parity];s=r262['prime_tail_source_response_certificates'][parity]
  A=F(r['retained_physical_polynomial_energy']);R=F(r['omitted_model_physical_energy_above_1024_upper']);delta=F(r['complete_finite_and_global_physical_error_norm_upper']);U=F(ref['rational_half_bandwidth'])
  a=[F(v['coefficient']) for v in r261['materialized_source_Fourier_response_certificates'][parity]['retained_physical_source_center_0_through_512']]+[F(0)]*512
  for v in s['physical_source_centers_513_through_1024']:a[v['degree']]=F(v['physical_source_center'])
  assert A==sum((orig.mass(n)*v*v for n,v in enumerate(a)),F(0))
  A512=sum((orig.mass(n)*v*v for n,v in enumerate(a[:513])),F(0));parseval={'outside_physical_Fourier_energy_lower':'0','outside_physical_Fourier_energy_upper':str(A512)}
  ratio=F(21,20) if parity else F(8,5);V=ratio*U;Y,Acheck,proof=source.fourier(a,parity,V,pi0,pierr,parseval,reverse);assert Acheck==A
  proof['principal_512_Parseval_control_lower']=proof.pop('independent_RC261_degree_512_control_lower');proof['principal_512_Parseval_control_upper']=proof.pop('independent_RC261_degree_512_control_upper');proof.pop('degree_512_control_intersects');proof['principal_512_control_origin']='Parseval [0,A512], no old numerical tail at new V';proof['principal_512_physical_energy']=str(A512)
  K,kproof=parent.high_trace(V,pi0+pierr,parity);kproof['high_space_band_operator_norm_upper']=kproof.pop('Poisson_trace_upper_capped_at_one');Mlo,lproof=parent.shell_lower(A,Y[0],R,K)
  loglo,loghi,lp=coercive.log_interval(V+F(old['exponential_one_lower']))
  shells=copy.deepcopy(r['additional_frequency_shells'])
  for v in shells:v['high_mode_trace_certificate']['high_space_band_operator_norm_upper']=v['high_mode_trace_certificate'].pop('Poisson_trace_upper_capped_at_one')
  shells.append(dict(bandwidth_ratio=str(ratio),rational_half_bandwidth=str(V),retained_Fourier_certificate=proof,high_mode_trace_certificate=kproof,model_outside_energy_lower=str(Mlo),model_lower_controls=lproof,outside_log_lower=str(loglo),outside_log_upper=str(loghi),outside_log_control=lp));shells.sort(key=lambda v:F(v['rational_half_bandwidth']))
  assert all(F(a['retained_Fourier_certificate']['outside_physical_Fourier_energy_lower'])>F(b['retained_Fourier_certificate']['outside_physical_Fourier_energy_upper']) for a,b in zip(shells,shells[1:]))
  choices=[]
  for k in range(1000,2000):
   t=coercive.retained_band(F(k,10000),F(ref['original_canonical_reference_floor']),F(ref['original_low_band_penalty']),F(ref['unchanged_actual_rational_augmentation_coefficient']),F(ref['complete_canonical_J_to_Fhat_error_squared_upper']),F(old['outside_log_lower']))
   I=F(t['physical_inside_band_multiplier_lower']);O=F(t['physical_outside_band_multiplier_lower']);eta=F(t['canonical_metric_floor'])
   if I<=O:continue
   weights=[1/O]+[1/(eta*F(v['outside_log_lower'])) for v in shells]
   model,constant,flat,coef,details=joint_bound(A,R,F(old['retained_outside_Fourier_energy_upper']),F(old['model_retained_omitted_band_cross_absolute_upper']),I,weights,shells)
   wf=up(delta*root(1/O));correction=up((root(model)+wf)**2);choices.append((correction,F(t['tau']),t,model,constant,flat,coef,details,weights,wf))
  if reverse:choices.reverse()
  correction,_,selected,model,constant,flat,coef,details,weights,wf=min(choices,key=lambda v:(v[0],v[1]))
  center=F(ref['direct_inverse_response_upper'])-F(ref['actual_augmented_inverse_correction_upper']);candidate=up(center+correction);upper=min(F(r['actual_original_action_inverse_response_upper']),candidate)
  f0=forms['parity_materialized_four_trial_response_certificates'][parity]['original_trial_form_intervals'][0][0];gap=max(F(r['actual_signed_gap_lower']),down(F(f0[0])-upper))
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],new_frequency_cutoff_ratio=str(ratio),retained_physical_polynomial_energy=str(A),omitted_model_physical_energy_above_1024_upper=str(R),complete_finite_and_global_physical_error_norm_upper=str(delta),frequency_shells=shells,selected_retained_band_multiplier_certificate=selected,outside_shell_inverse_weights=list(map(str,weights)),selected_joint_shell_controls=details,joint_omitted_energy_quadratic_coefficient=str(coef),uncoupled_three_shell_model_inverse_upper=str(constant),flat_model_inverse_upper=str(flat),coupled_three_shell_model_inverse_upper=str(model),weighted_finite_and_global_fault_norm_upper=str(wf),actual_inverse_correction_upper=str(correction),candidate_inverse_response_upper=str(candidate),actual_original_action_inverse_response_lower=r['actual_original_action_inverse_response_lower'],actual_original_action_inverse_response_upper=str(upper),previous_original_action_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_inverse_upper_improved=upper<F(r['actual_original_action_inverse_response_upper']),actual_signed_gap_lower=str(gap),actual_signed_gap_upper=r['actual_signed_gap_upper'],signed_gap_positive_certified=gap>0,all_original_and_rational_augmentation_faults_paid=True))
  print('RC265 '+r['parity']+' inverse upper '+str(float(upper))+'; joint model '+str(float(model)),flush=True)
 return dict(milestone='RC265',starting_commit='dee8de1cd531cc210c73f134cb6ab7fff12ac19e',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,coupled_shell_remainder_response_certificates=rows,exact_controls=controls(),actual_response_source_count=2,response_trials_per_parity=4,retained_physical_source_degree_unchanged=1024,prime_output_cutoff_unchanged=2048,source_and_trial_spaces_unchanged=True,chosen_rational_augmentation_unchanged=True,omitted_model_energy_upper_not_assumed_equal_to_actual=True,finite_and_global_faults_paid_after_weighted_model_bound=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC266: source-specific rational augmentation action error or response-trial optimization; full signed gate remains open')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC265 VALIDATED: common omitted-mode energy across shells; Stage I open',flush=True)
