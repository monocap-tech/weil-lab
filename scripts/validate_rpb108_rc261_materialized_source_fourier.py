"""RC261: complete physical source through degree 512 and stable Fourier Gram."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc260_projection_defect_free_tail as parent
m=parent.m;band=parent.band;orig=parent.orig;B=parent.B;ROOT=parent.ROOT
up=parent.up;down=parent.down;root=parent.root;rootdown=parent.parent.fourier.rootdown
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc260_projection_defect_free_tail.json':'7718930c66222c3f4677d00fc99b6050eea6f7c6','notes/RPB108_RC260_PROJECTION_DEFECT_FREE_TAIL_20261014.md':'55259bc8b836eea3fd57dfe433fc12e6ccca0dd3'})
HELPER_PINS['scripts/validate_rpb108_rc260_projection_defect_free_tail.py']='640dc16d2897a3c457f48c77789b1f652bdecac9'
def diagonal_control():
 for n in [0,1,2,17,256,512]:
  z=F(431,3);a=F(1,7);b=F(-2,9);da=n*a/z-b;db=a-(n+2)*b/z
  assert a*a+b*b+2*z*(a*da+b*db)==(2*n+1)*a*a-(2*n+3)*b*b
 return dict(exact_diagonal_Bessel_energy_derivative_identity=True)
def fourier_energy(a,parity,U,pi0,pierr,reference,reverse):
 z,j,dj=parent.endpoint_values(U,pi0,pierr,reverse);digits=170 if reverse else 150
 j=[m.outer_grid(v,digits) for v in j[:513]];dj=[m.outer_grid(v,digits) for v in dj[:513]]
 # j_0=sin(z)/z, j_1=sin(z)/z^2-cos(z)/z.
 sine=m.isc(j[0],z);cosine=m.ia(j[0],m.isc(j[1],-z))
 c2=m.ia(m.im(cosine,cosine),m.neg(m.im(sine,sine)));s2=m.isc(m.im(sine,cosine),2)
 L=520 if reverse else 500;rr,ii,rem=m.ibp_parts(2,L,z,[(2*z.numerator)**k for k in range(L)])
 realI2=m.isc(m.ia(m.im(c2,(rr-rem,rr+rem)),m.neg(m.im(s2,(ii-rem,ii+rem)))),1/z**2)
 J0=m.outer_grid(m.ia(m.ip(1/(2*z)),m.isc(realI2,-F(1,2))),digits);assert J0[0]>0
 J=[J0]
 for n in range(512):
  squares=m.ia(m.im(j[n],j[n]),m.im(j[n+1],j[n+1]))
  value=m.isc(m.ia(m.isc(J[n],2*n+1),m.isc(squares,z)),F(1,2*n+3))
  J.append(m.outer_grid(value,digits));assert J[-1][0]>0
 terms=[];lowterms=[];degrees=[n for n,c in enumerate(a) if c]
 assert all(n%2==parity for n in degrees) and len(a)==513
 for n in degrees:
  term=m.isc(J[n],a[n]*a[n]);terms.append(term)
  if n<=256:lowterms.append(term)
  for d in degrees:
   if d>=n:break
   W=m.ia(m.im(dj[n],j[d]),m.neg(m.im(j[n],dj[d])))
   # Integral_z^infinity j_n j_d = -z^2 W/(n(n+1)-d(d+1)).
   term=m.isc(W,-2*a[n]*a[d]*(-1)**((n-parity)//2+(d-parity)//2)*z*z/F(n*(n+1)-d*(d+1)))
   terms.append(term)
   if n<=256:lowterms.append(term)
  if n in [127,128,255,256,383,384,511,512]:print('RC261 '+('odd' if parity else 'even')+' Fourier pairs through '+str(n),flush=True)
 if reverse:terms.reverse();lowterms.reverse()
 def finish(values,coefficients):
  v=m.ip(F(0))
  for t in values:v=m.ia(v,t)
  S=sum(map(abs,coefficients),F(0));pil=pi0-pierr;fault=up(S*S*(4*B/pil*(2*B*U*pierr)+8*B*pierr/(pil*pi0)))
  v=m.isc(v,4*B/pi0);return band.outer24((v[0]-fault,v[1]+fault)),fault
 low,lowfault=finish(lowterms,a[:257]);old=(F(reference['outside_physical_Fourier_energy_lower']),F(reference['outside_physical_Fourier_energy_upper']))
 assert max(low[0],old[0])<=min(low[1],old[1]),'independent RC257 Fourier control'
 result,fault=finish(terms,a);A=sum((orig.mass(n)*c*c for n,c in enumerate(a)),F(0));assert 0<result[0]<=result[1]<A
 return result,A,dict(full_retained_degree=512,all_source_mode_cross_terms_retained=True,off_diagonal_spherical_boundary_identity=True,diagonal_tail_recurrence='(2n+3) J_(n+1) = (2n+1) J_n + z*(j_n(z)^2+j_(n+1)(z)^2)',diagonal_base='J_0=1/(2z)-Re(I_2)/2',base_I2_generation_IBP_terms=500,base_I2_replay_IBP_terms=520,endpoint_and_diagonal_generation_grid_digits=150,endpoint_and_diagonal_replay_grid_digits=170,phase_and_initial_Bessel_intervals_origin='RC260 endpoint_values through 1024',independent_RC257_degree_256_control_lower=str(low[0]),independent_RC257_degree_256_control_upper=str(low[1]),independent_RC257_degree_256_control_intersects=True,actual_pi_lower_limit_and_prefactor_source_squared_fault_upper=str(fault),physical_polynomial_energy=str(A),outside_physical_Fourier_energy_lower=str(result[0]),outside_physical_Fourier_energy_upper=str(result[1]),stored_Fourier_energy_grid_digits=24)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin')
  if path.endswith('.json'):data[path]=json.loads(b)
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('260_projection_defect_free_tail');material=get('259_coupled_augmentation_tail');low=get('251_extended_coupled_residual');reference=get('257_physical_source_fourier_tail');physical=get('256_retained_band_inverse');kernel=get('115_rational_fourier_adjoint');forms=get('247_materialized_four_trial_response');rows=[]
 harmonic=[F(0)]
 for n in range(1,257):harmonic.append(harmonic[-1]+F(1,n))
 for parity,r in enumerate(prior['projection_defect_free_tail_response_certificates']):
  ref=physical['retained_band_inverse_response_certificates'][parity];src=ref['actual_physical_residual_source_certificate'];sm=F(src['retained_source_center_parameter']);c=low['extended_coupled_residual_response_certificates'][parity];a=[(harmonic[n]+sm)*F(v['coefficient']) for n,v in enumerate(c['extended_complete_direct_residual_center'])]+[F(0)]*256
  high=material['coupled_augmentation_tail_response_certificates'][parity]['coupled_physical_model_output_257_through_512'];error_terms=[]
  for v in high:
   n=v['degree'];a[n]=F(v['physical_model_source_center']);error_terms.append(up(orig.mass(n)*F(v['radius'])**2))
  if reverse:error_terms.reverse()
  finite=up(F(src['finite_coefficient_and_actual_s_uncertainty_physical_energy_upper'])+sum(error_terms,F(0)));R=F(r['coupled_physical_model_energy_beyond_512_upper']);fault=F(src['complete_global_physical_fault_norm_upper']);U=F(ref['rational_half_bandwidth'])
  Y,A,proof=fourier_energy(a,parity,U,F(kernel['rational_pi']),F(kernel['rational_pi_error_upper']),reference['physical_source_Fourier_tail_certificates'][parity]['retained_physical_source_Fourier_certificate'],reverse)
  modelout,active=parent.parent.parent.orthogonal_tail(A,Y[1],R);assert active
  S=min(F(r['actual_full_source_physical_energy_upper']),up((root(up((root(A)+root(finite))**2+R))+fault)**2));X=min(S,F(r['actual_full_source_outside_Fourier_energy_upper']),up((root(modelout)+root(finite)+fault)**2));Xlo=down(max(F(0),rootdown(Y[0])-root(up(finite+R))-fault)**2);assert 0<=Xlo<=X<=S
  choices=[]
  lam=F(ref['unchanged_actual_rational_augmentation_coefficient'])
  for k in range(1000,2000):
   t=parent.parent.parent.band.retained_band(F(k,10000),F(ref['original_canonical_reference_floor']),F(ref['original_low_band_penalty']),lam,F(ref['complete_canonical_J_to_Fhat_error_squared_upper']),F(ref['log_U_lower']));I=F(t['physical_inside_band_multiplier_lower']);O=F(t['physical_outside_band_multiplier_lower'])
   if I>O:choices.append((up(S/I+X*(1/O-1/I)),F(t['tau']),t))
  if reverse:choices.reverse()
  correction,_,selected=min(choices,key=lambda v:(v[0],v[1]));center=F(ref['direct_inverse_response_upper'])-F(ref['actual_augmented_inverse_correction_upper']);candidate=up(center+correction);upper=min(F(r['actual_original_action_inverse_response_upper']),candidate);f0=forms['parity_materialized_four_trial_response_certificates'][parity]['original_trial_form_intervals'][0][0];gap=max(F(r['actual_signed_gap_lower']),down(F(f0[0])-upper))
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],retained_physical_source_center_0_through_512=[dict(degree=n,coefficient=str(v)) for n,v in enumerate(a)],retained_physical_source_Fourier_certificate=proof,retained_physical_coefficient_uncertainty_energy_upper=str(finite),complete_model_physical_energy_beyond_512_upper=str(R),unchanged_global_physical_fault_norm_upper=str(fault),orthogonality_nonsaturated_regime_certified=active,orthogonal_model_outside_Fourier_energy_upper=str(modelout),actual_full_source_physical_energy_upper=str(S),actual_full_source_outside_Fourier_energy_lower=str(Xlo),actual_full_source_outside_Fourier_energy_upper=str(X),previous_full_source_outside_Fourier_energy_upper=r['actual_full_source_outside_Fourier_energy_upper'],selected_two_band_multiplier_certificate=selected,actual_inverse_correction_upper=str(correction),candidate_inverse_response_upper=str(candidate),actual_original_action_inverse_response_lower=r['actual_original_action_inverse_response_lower'],actual_original_action_inverse_response_upper=str(upper),previous_original_action_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_inverse_upper_improved=upper<F(r['actual_original_action_inverse_response_upper']),actual_signed_gap_lower=str(gap),actual_signed_gap_upper=r['actual_signed_gap_upper'],all_original_and_rational_augmentation_faults_paid=True,signed_gap_positive_certified=gap>0))
  print('RC261 '+r['parity']+' retained outside '+str(float(Y[1]))+'; full outside '+str(float(X))+'; inverse upper '+str(float(upper)),flush=True)
 return dict(milestone='RC261',starting_commit='fdb624ba35037b8eb74347d0b86fffe0929080d6',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,materialized_source_Fourier_response_certificates=rows,exact_controls=diagonal_control(),actual_response_source_count=2,response_trials_per_parity=4,retained_physical_source_degree=512,source_and_trial_spaces_unchanged=True,chosen_rational_augmentation_unchanged=True,compression_defect_free_band_tail_from_RC260_preserved=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC262: control remaining original prime output beyond 512 or exploit the complete retained Fourier Gram for a sharper residual inverse bound; full signed gate remains open')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
 if args.replay:assert result==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('RC261 VALIDATED: materialized degree-512 Fourier source; Stage I open',flush=True)
