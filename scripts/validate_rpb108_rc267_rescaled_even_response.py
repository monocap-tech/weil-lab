"""RC267: certify the even response trial (27/20) Z with correlated prime tails."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc266_integrated_contour_augmentation as parent
joint=parent.parent;fourier=joint.parent;src=fourier.source;prime=src.prime
m=src.m;orig=parent.orig;B=parent.B;ROOT=parent.ROOT;coercive=parent.coercive
up=parent.up;down=parent.down;root=parent.root;SCALE=F(27,20)
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc266_integrated_contour_augmentation.json':'4425c2ee6113a8d6278bd08e9a4a9681d1dc323d','notes/RPB108_RC266_INTEGRATED_CONTOUR_AUGMENTATION_20261014.md':'4291d4339133c4fe82bb4b4edd940c23122f3941'})
HELPER_PINS['scripts/validate_rpb108_rc266_integrated_contour_augmentation.py']='ee6ce0b3dc4954df5cc06bfd1b95191e0c113dc0'

def rescaling_controls():
 p=coercive.p;G0=[[F(1),F(1,4)],[F(1,4),F(2)]];G=p.add(G0,[[F(3),F(1,7)],[F(1,7),F(4)]]);v=[[F(1)],[F(0)]];z=[[F(1,9)],[F(-1,11)]]
 f=p.mm(G0,v);g=p.add(f,p.mm(G,z),-1);zt=p.scale(SCALE,z);gt=p.add(f,p.mm(G,zt),-1)
 assert p.mm(G0,G)!=p.mm(G,G0) and gt==p.add(p.scale(SCALE,g),p.scale(1-SCALE,f))
 inner=lambda a,M,b:p.mm(p.trans(a),p.mm(M,b))[0][0]
 I=[[F(1),F(0)],[F(0),F(1)]];center=2*inner(zt,I,f)-inner(zt,G,zt)
 assert inner(f,p.inv(G),f)==center+inner(gt,p.inv(G),gt)

def source_and_prime(a,parameters,oldsource,oldprimewindow,old_prime_digest,reverse):
 q=prime.native.input_poly(a);segments=prime.model_segments(q,parameters,0)
 constants=prime.model_segments([F(1)],parameters,0)
 previous_q=[v/SCALE for v in q];previous_q[0]-=(1-SCALE)/SCALE;previous_segments=prime.model_segments(previous_q,parameters,0)
 assert prime.native.segment_digest(previous_segments)==old_prime_digest
 for (l,r,v),(ll,rr,w),(_,_,c) in zip(segments,previous_segments,constants):
  assert (l,r)==(ll,rr) and v==[SCALE*x+((1-SCALE)*c[0] if d==0 else 0) for d,x in enumerate(w)]
 norm=B*sum((orig.integral(orig.product(v,v),l,r) for l,r,v in segments),F(0));assert norm>0
 boundaries=[];digits=140 if reverse else 120
 for i in range(len(segments)-1):
  b=segments[i][1]
  if b<0:continue
  jump=prime.native.addpoly(segments[i][2],[-v for v in segments[i+1][2]])
  jc=[orig.project(jump,d) for d in range(len(q))]
  assert not any(prime.native.addpoly(prime.native.input_poly(jc),[-v for v in jump]))
  values=prime.legendre_values(b,len(q)-1);dv=[F(0)]+[d*(b*values[d]-values[d-1])/(b*b-1) for d in range(1,len(q))]
  pn=src.legendre_intervals(b,reverse)
  pn.append(m.outer_grid(m.isc(m.ia(m.isc(pn[-1],4097*b),m.isc(pn[-2],-2048)),F(1,2049)),digits))
  jump0=constants[i][2][0]-constants[i+1][2][0]
  boundaries.append((b,[m.outer_grid(m.ip(jc[d]*values[d]),digits) for d in range(len(q))],[m.outer_grid(m.ip(jc[d]*dv[d]),digits) for d in range(len(q))],pn,jump0))
 assert len(boundaries)==7
 # P0 source uses these SAME rounded prime parameters as the old Q model.
 pc0=[m.ip(F(0)) for _ in range(2049)]
 pc0[0]=m.ip(sum((v[0]*(r-l)/2 for l,r,v in constants),F(0)))
 for n in range(2,2049,2):
  terms=[m.isc(m.ia(pn[n+1],m.neg(pn[n-1])),jump0) for b,jv,jd,pn,jump0 in boundaries]
  if reverse:terms.reverse()
  val=m.ip(F(0))
  for t in terms:val=m.ia(val,t)
  pc0[n]=m.outer_grid(val,60)
 oldsegments=[(F(s['left']),F(s['right']),list(map(F,s['physical_t_polynomial']))) for s in oldsource['prime_physical_segments']]
 oldpc0=[F(0)]*65
 for n in range(0,65,2):oldpc0[n]=F(2*n+1,2)*sum((orig.integral(orig.product(v,orig.legendre(n)),l,r) for l,r,v in oldsegments),F(0))
 oldnorm=B*sum((orig.integral(orig.product(v,v),l,r) for l,r,v in oldsegments),F(0))
 assert up(oldnorm-sum((orig.mass(n)*v*v for n,v in enumerate(oldpc0)),F(0)))==F(oldsource['prime_nominal_physical_omitted_norm_squared_upper'])
 old={v['degree']:v for v in oldprimewindow};coeff=[m.ip(F(0)) for _ in range(2049)]
 def boundary(n):
  parts=[];ln=n*(n+1)
  for b,jv,jd,pn,jump0 in boundaries:
   val=slope=m.ip(F(0))
   for d in range(len(q)):
    val=m.ia(val,m.isc(jv[d],F(1,ln-d*(d+1))));slope=m.ia(slope,m.isc(jd[d],F(1,ln-d*(d+1))))
   dp=m.isc(m.ia(m.isc(pn[n],b),m.neg(pn[n-1])),F(n)/(b*b-1))
   parts.append(m.isc(m.ia(m.im(slope,pn[n]),m.neg(m.im(val,dp))),1-b*b))
  if reverse:parts.reverse()
  val=m.ip(F(0))
  for t in parts:val=m.ia(val,t)
  return m.outer_grid(m.isc(val,2*n+1),60)
 for n in range(0,2049,2):
  if n<=64:
   v=F(2*n+1,2)*sum((orig.integral(orig.product(poly,orig.legendre(n)),l,r) for l,r,poly in segments),F(0));coeff[n]=m.outer_grid(m.ip(v),60)
  elif n<=512:coeff[n]=boundary(n)
  else:coeff[n]=m.outer_grid(m.ia(m.isc((F(old[n]['lower']),F(old[n]['upper'])),SCALE),m.isc(pc0[n],1-SCALE)),60)
  if n in [66,514,1024,2048]:
   independent=boundary(n) if n!=66 else m.ip(F(2*n+1,2)*sum((orig.integral(orig.product(poly,orig.legendre(n)),l,r) for l,r,poly in segments),F(0)))
   assert max(coeff[n][0],independent[0])<=min(coeff[n][1],independent[1]),('prime control',n)
  assert coeff[n][1]-coeff[n][0]<F(1,10**50)
  if n in [64,256,512,1024,2048]:print('RC267 correlated even prime projection through '+str(n),flush=True)
 capture=down(sum((orig.mass(n)*src.band.minabs(v)**2 for n,v in enumerate(coeff)),F(0)));remaining=up(norm-capture);assert 0<remaining<norm
 return pc0,oldpc0,coeff,remaining,dict(full_rescaled_prime_model_physical_energy=str(norm),captured_prime_physical_energy_through_2048_lower=str(capture),prime_physical_energy_beyond_2048_upper=str(remaining),same_rounded_prime_parameters_used_for_both_inputs=True,prime_projection_controls=[66,514,1024,2048],low_prime_coefficients_direct_polynomial_integration=True,high_prime_coefficients_reuse_RC262_by_exact_linearity=True,full_model_segment_digest=prime.native.segment_digest(segments),retained_boundary_jump_polynomials_exactly_reconstructed=True)

def run(reverse=False):
 rescaling_controls()
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('266_integrated_contour_augmentation');old=prior['integrated_contour_response_certificates'][0];r263=get('263_high_mode_inverse')['high_mode_inverse_response_certificates'][0];s=get('262_prime_tail_source_1024')['prime_tail_source_response_certificates'][0];prefix=get('261_materialized_source_fourier')['materialized_source_Fourier_response_certificates'][0];ref=get('256_retained_band_inverse')['retained_band_inverse_response_certificates'][0];source0=get('231_original_polynomial_action')['polynomial_original_action_certificates'][0];trial=get('248_direct_coupled_residual')['selected_direct_residual_certificates'][0];parameters=get('250_coupled_original_output_tail')['coupled_output_tail_response_certificates'][0]['coupled_original_output_tail_certificate']['prime_controls']['chosen_prime_model_parameters'];forms=get('247_materialized_four_trial_response')['parity_materialized_four_trial_response_certificates'][0];metric=get('129_four_vector_joint_moment');kernel=get('115_rational_fourier_adjoint')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);sm=(sl+sh)/2;sr=(sh-sl)/2
 Z=list(map(F,trial['exact_Z_input_Legendre_coefficients']));Q=[-SCALE*v for v in Z];Q[0]+=1;assert all(not v or n%2==0 for n,v in enumerate(Q))
 old_prime_digest=get('250_coupled_original_output_tail')['coupled_output_tail_response_certificates'][0]['coupled_original_output_tail_certificate']['prime_controls']['prime_segment_polynomial_sha256']
 pc0,oldpc0,pc,primetail,primeproof=source_and_prime(Q,parameters,source0,s['prime_window_513_through_2048'],old_prime_digest,reverse)
 harmonic=[F(0)]
 for n in range(1,2052):harmonic.append(harmonic[-1]+F(1,n))
 f0=[F(0)]*1025;f0errors=[]
 for n in range(0,1025,2):
  c0=(pc0[n][0]+pc0[n][1])/2;rad=(pc0[n][1]-pc0[n][0])/2
  if n<=64:
   v=source0['finite_original_D_action'][n];c=F(v['coefficient']);radius=F(v['radius']);f0[n]=(harmonic[n]+sm)*c+c0-oldpc0[n];rad+=(harmonic[n]+sh)*radius+sr*abs(c)
  else:f0[n]=F(2*n+1,n*(n+1))+c0
  raw=f0[n];f0[n]=down(raw);rad+=abs(raw-f0[n])
  f0errors.append(orig.mass(n)*rad*rad)
 finite0=up(sum(f0errors,F(0)));primefault0=up(sum((2*(F(v['actual_coefficient_distance_upper'])*root(2*B)+(F(v['chosen_coefficient'])+F(v['actual_coefficient_distance_upper']))*root(2*F(v['actual_translation_distance_upper']))) for v in parameters),F(0)))
 regular0=root(up(sl*F(source0['D_energy_component_squared_errors']['regular_kernel'])));global0=up(primefault0+regular0+F(source0['signed_pole_actual_physical_error_norm_upper'])+root(F(source0['regular_omitted_physical_norm_squared_upper'])));delta0=up(root(finite0)+global0)
 a=[F(v['coefficient']) for v in prefix['retained_physical_source_center_0_through_512']]+[F(0)]*512
 for v in s['physical_source_centers_513_through_1024']:a[v['degree']]=F(v['physical_source_center'])
 a=[SCALE*v+(1-SCALE)*w for v,w in zip(a,f0)];A=sum((orig.mass(n)*v*v for n,v in enumerate(a)),F(0));delta=up(SCALE*F(old['complete_finite_and_global_physical_error_norm_upper'])+abs(1-SCALE)*delta0)
 # Recompute the COMPLETE original model tail for Q=P0-(27/20)Z.
 explicit=[]
 for n in range(1026,2049,2):
  h,rad=prime.native.endpoint(Q,n,F(0),F(0));assert rad==0
  explicit.append(up(orig.mass(n)*max(abs(h+pc[n][0]),abs(h+pc[n][1]))**2))
 if reverse:explicit.reverse()
 _,ep=prime.parent.tail_bound(Q,2050,sl,harmonic);endpoint=up(2*B*F(ep['uniform_combined_endpoint_bracket_upper'])**2*F(ep['parity_telescoping_weight_sum_upper']));original=up(sum(explicit,F(0))+(root(endpoint)+root(primetail))**2);augmentation=up(SCALE*SCALE*F(s['augmentation_physical_energy_beyond_1024_upper']));R=up((root(original)+root(augmentation))**2)
 U=F(ref['rational_half_bandwidth']);pi0=F(kernel['rational_pi']);pierr=F(kernel['rational_pi_error_upper']);A512=sum((orig.mass(n)*v*v for n,v in enumerate(a[:513])),F(0));parseval={'outside_physical_Fourier_energy_lower':'0','outside_physical_Fourier_energy_upper':str(A512)};shells=[]
 oldshells=get('265_coupled_shell_remainder')['coupled_shell_remainder_response_certificates'][0]['frequency_shells'];Y0=None;eps0=None
 for ratio in [F(1),F(3,2),F(8,5),F(2)]:
  Y,Acheck,proof=src.fourier(a,0,ratio*U,pi0,pierr,parseval,reverse);assert Acheck==A
  proof['principal_512_Parseval_control_lower']=proof.pop('independent_RC261_degree_512_control_lower');proof['principal_512_Parseval_control_upper']=proof.pop('independent_RC261_degree_512_control_upper');proof.pop('degree_512_control_intersects');proof['principal_512_control_origin']='Parseval [0,A512], new rescaled source';proof['principal_512_physical_energy']=str(A512)
  if ratio==1:
   Y0=proof;K0=F(r263['high_Legendre_compressed_band_trace_upper']);eps0=up(root(up((A-Y[0])*K0*R)))
  else:
   inherited=next(v for v in oldshells if F(v['bandwidth_ratio'])==ratio);K=F(inherited['high_mode_trace_certificate']['high_space_band_operator_norm_upper']);L,lp=fourier.shell_lower(A,Y[0],R,K)
   shells.append(dict(bandwidth_ratio=str(ratio),rational_half_bandwidth=str(ratio*U),retained_Fourier_certificate=proof,high_mode_trace_certificate=inherited['high_mode_trace_certificate'],model_outside_energy_lower=str(L),model_lower_controls=lp,outside_log_lower=inherited['outside_log_lower']))
  print('RC267 even rescaled Fourier cutoff '+str(ratio),flush=True)
 y=[SCALE*F(v) for v in old['selected_trial_coefficients']];F0=[[(F(a),F(b)) for a,b in row] for row in forms['original_trial_form_intervals']];Gy=[[(F(a),F(b)) for a,b in row] for row in forms['frequency_trial_Gram_intervals']];lam=F(ref['unchanged_actual_rational_augmentation_coefficient']);cl,ch=prime.direct.center_intervals(F0,Gy,y,lam)
 taus={F(k,10000) for k in range(1000,2000)}|{F(k,10**j) for j in range(3,10) for k in range(1,100)};choices=[];gamma=F(ref['original_canonical_reference_floor']);penalty=F(ref['original_low_band_penalty']);d2=F(old['complete_physical_and_canonical_J_to_Fhat_error_squared_upper'])
 for tau in sorted(taus,reverse=reverse):
  if gamma-lam*(1/tau-1)*d2<=0:continue
  t=coercive.retained_band(tau,gamma,penalty,lam,d2,F(r263['outside_log_lower']));I=F(t['physical_inside_band_multiplier_lower']);O=F(t['physical_outside_band_multiplier_lower']);eta=F(t['canonical_metric_floor'])
  if I<=O:continue
  weights=[1/O]+[1/(eta*F(v['outside_log_lower'])) for v in shells];model,constant,flat,coef,details=joint.joint_bound(A,R,F(Y0['outside_physical_Fourier_energy_upper']),eps0,I,weights,shells);wf=up(delta*root(1/O));correction=up((root(model)+wf)**2);choices.append((up(ch+correction),tau,t,model,coef,details,weights,wf,correction))
 candidate,_,selected,model,coef,details,weights,wf,correction=min(choices,key=lambda v:(v[0],v[1]));upper=min(F(old['actual_original_action_inverse_response_upper']),candidate);gap=max(F(old['actual_signed_gap_lower']),down(F0[0][0][0]-upper));assert F(old['actual_original_action_inverse_response_lower'])<=upper and gap<=F(old['actual_signed_gap_upper'])
 rows=[dict(parity='even',source=old['source'],selected_trial_coefficients=list(map(str,y)),actual_original_action_inverse_response_lower=old['actual_original_action_inverse_response_lower'],actual_original_action_inverse_response_upper=str(upper),previous_original_action_inverse_response_upper=old['actual_original_action_inverse_response_upper'],actual_signed_gap_lower=str(gap),actual_signed_gap_upper=old['actual_signed_gap_upper'],signed_gap_positive_certified=gap>0),dict(parity='odd',source=prior['integrated_contour_response_certificates'][1]['source'],actual_original_action_inverse_response_lower=prior['integrated_contour_response_certificates'][1]['actual_original_action_inverse_response_lower'],actual_original_action_inverse_response_upper=prior['integrated_contour_response_certificates'][1]['actual_original_action_inverse_response_upper'],actual_signed_gap_lower=prior['integrated_contour_response_certificates'][1]['actual_signed_gap_lower'],actual_signed_gap_upper=prior['integrated_contour_response_certificates'][1]['actual_signed_gap_upper'],signed_gap_positive_certified=prior['integrated_contour_response_certificates'][1]['signed_gap_positive_certified'],unchanged_from_pinned_RC266=True)]
 print('RC267 even inverse upper '+str(float(upper))+'; signed gap lower '+str(float(gap)),flush=True)
 return dict(milestone='RC267',starting_commit='8b0d8a60fdb4a7d315cc249115c20fb07ee04d97',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,trial_rescaling_response_certificates=rows,even_trial_scale=str(SCALE),exact_scaled_Z_input_Legendre_coefficients=list(map(str,[SCALE*v for v in Z])),exact_original_combination_input=list(map(str,Q)),new_retained_physical_source_coefficients=list(map(str,a)),retained_physical_polynomial_energy=str(A),P0_same_prime_model_source_finite_energy_error_upper=str(finite0),P0_same_prime_model_source_global_error_norm_upper=str(global0),P0_prime_model_arithmetic_fault_norm_upper=str(primefault0),complete_finite_and_global_physical_error_norm_upper=str(delta),prime_projection_certificate=primeproof,prime_physical_energy_beyond_2048_upper=str(primetail),endpoint_physical_energy_beyond_2048_upper=str(endpoint),endpoint_tail_control=ep,explicit_original_physical_energy_1025_through_2048_upper=str(up(sum(explicit,F(0)))),complete_original_physical_energy_beyond_1024_upper=str(original),complete_model_physical_energy_beyond_1024_upper=str(R),base_retained_Fourier_certificate=Y0,frequency_shells=shells,selected_retained_band_multiplier_certificate=selected,new_variational_center_lower=str(cl),new_variational_center_upper=str(ch),coupled_shell_model_inverse_upper=str(model),joint_omitted_energy_quadratic_coefficient=str(coef),selected_joint_shell_controls=details,outside_shell_inverse_weights=list(map(str,weights)),weighted_finite_and_global_fault_norm_upper=str(wf),actual_inverse_correction_upper=str(correction),candidate_inverse_response_upper=str(candidate),exact_controls=parent.controls(),individual_source_signed_gap_positive_certified_parities=[v['parity'] for v in rows if v['signed_gap_positive_certified']],actual_response_source_count=2,response_trials_per_parity=4,response_trial_space_unchanged=True,selected_even_response_trial_changed=True,chosen_rational_augmentation_unchanged=True,all_original_and_rational_augmentation_faults_paid=True,retained_physical_source_degree_unchanged=1024,prime_output_cutoff_unchanged=2048,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC268: extend signed-response certification beyond the current P0/P1 pair; full auxiliary response gate remains open')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC267 VALIDATED: rescaled even response with complete correlated tails; Stage I open',flush=True)
