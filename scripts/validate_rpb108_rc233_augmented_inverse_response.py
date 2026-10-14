"""RC233: actual augmented inverse-response Gram for native r0/r1.
Certified variational/residual enclosures; no full frequency response gate.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc232_augmented_polynomial_action as parent
bridge=parent.bridge;p=bridge.p;original=parent.parent
ROOT=Path(__file__).resolve().parents[1];GRID=10**60
up=bridge.up;down=bridge.down;rootup=bridge.rootup
def rootdown(x):
 r=rootup(x)
 return r if r*r==x else max(F(0),r-F(1,GRID))
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({
 'certificates/rpb108_rc232_augmented_polynomial_action.json':'32226a00d6cb6cfb6077106e96890ec9f739c2a3',
 'notes/RPB108_RC232_COMPLETE_AUGMENTED_POLYNOMIAL_ACTIONS_20261014.md':'69f8818efac81447b437ceb636dd9fd2879b89d6',
 'notes/RPB108_RC230_EXACT_AUGMENTATION_RANGE_AND_D_ENERGY_BRIDGE_20261014.md':'2b178b64330ec20dbd9a5e8028188705a5fa3d92'})
HELPER_PINS['scripts/validate_rpb108_rc232_augmented_polynomial_action.py']='0517cd8d8ed1688090c3085d8dd0a9171aa80a6e'
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  raw=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha,(path,'pin')
  data[path]=json.loads(raw) if path.endswith('.json') else raw.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 action=get('232_augmented_polynomial_action');metric=get('129_four_vector_joint_moment');rangeproof=get('230_augmentation_range_bridge')
 assert action['actual_complete_augmented_P0_P1_action_enclosures_certified'] and action['all_complex_combinations_of_P0_P1_covered'] and rangeproof['full_chosen_augmentation_rank']==639
 B=F(11,10);sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);rows=[]
 for j,row in enumerate(action['polynomial_augmented_action_certificates']):
  assert row['input']=='P'+str(j)
  mass=2*B/F(2*j+1);dl=original.H(j)+sl;dh=original.H(j)+sh
  gl=1/dh;gh=1/dl;g=down((gl+gh)/2);gr=max(g-gl,gh-g)
  source_round=up(mass*dh*gr**2);source_lo=down(mass/dh);source_hi=up(mass/dl)
  A=[F(r['coefficient']) for r in row['finite_complete_augmented_D_action']];assert all(x==0 for n,x in enumerate(A) if n%2!=j)
  E=F(row['complete_augmented_action_D_error_squared_upper']);mu=F(row['fresh_augmented_N_D_lower']);nu=F(row['fresh_augmented_N_D_upper'])
  flo=F(row['augmented_test_form_lower']);fhi=F(row['augmented_test_form_upper']);assert 0<flo<=fhi and 0<mu<nu
  def trial(t):
   assert t>=0
   residual=[(g if n==j else F(0))-t*x for n,x in enumerate(A)]
   terms=[(n,original.mass(n)*v*v) for n,v in enumerate(residual)]
   if reverse:terms.reverse()
   nomlo=sum((w*(original.H(n)+sl) for n,w in terms),F(0));nomhi=sum((w*(original.H(n)+sh) for n,w in terms),F(0))
   fault=up(rootup(source_round)+t*rootup(E))
   reslo=down(max(F(0),rootdown(nomlo)-fault)**2);reshi=up((rootup(nomhi)+fault)**2)
   clo=down(2*t*mass-t*t*fhi);chi=up(2*t*mass-t*t*flo)
   lo=down(clo+reslo/nu);hi=up(chi+reshi/mu)
   assert lo<=hi
   return dict(trial_coefficient=str(t),finite_trial_input='P'+str(j),finite_residual_center=[dict(degree=n,coefficient=str(v)) for n,v in enumerate(residual) if v],source_rounding_D_error_squared_upper=str(source_round),nominal_residual_D_Gram_lower=str(down(nomlo)),nominal_residual_D_Gram_upper=str(up(nomhi)),total_residual_D_Gram_lower=str(reslo),total_residual_D_Gram_upper=str(reshi),signed_variational_center_lower=str(clo),signed_variational_center_upper=str(chi),added_inverse_residual_correction_lower=str(down(reslo/nu)),added_inverse_residual_correction_upper=str(up(reshi/mu)),actual_inverse_response_lower=str(lo),actual_inverse_response_upper=str(hi))
  # Exact nominal least-residual proposal; acceptance uses paid enclosures.
  sm=(sl+sh)/2
  norm=sum((original.mass(n)*(original.H(n)+sm)*x*x for n,x in enumerate(A)),F(0))
  t0=mass*(original.H(j)+sm)*g*A[j]/norm;assert t0>0
  choices=[F(k,100)*t0 for k in range(50,151)]+[mass/fhi,mass/flo,F(0)]
  candidates=[trial(t) for t in sorted(set(choices))]
  lower=max(candidates,key=lambda x:(F(x['actual_inverse_response_lower']),-F(x['trial_coefficient'])))
  upper=min(candidates,key=lambda x:(F(x['actual_inverse_response_upper']),F(x['trial_coefficient'])))
  genericlo=down(source_lo/nu);generichi=up(source_hi/mu)
  acceptedlo=max(genericlo,F(lower['actual_inverse_response_lower']));acceptedhi=min(generichi,F(upper['actual_inverse_response_upper']))
  assert 0<acceptedlo<=acceptedhi<generichi
  rows.append(dict(parity=row['parity'],physical_source='P'+str(j),actual_canonical_source='r'+str(j)+'=i* P'+str(j),D_energy_source='D^-1 P'+str(j),source_D_Gram_lower=str(source_lo),source_D_Gram_upper=str(source_hi),augmented_N_D_lower=str(mu),augmented_N_D_upper=str(nu),generic_inverse_response_lower=str(genericlo),generic_inverse_response_upper=str(generichi),candidate_count=len(candidates),candidate_rule='101 rational multiples of nominal least-residual t0, two variational proposals, and zero; exact paid acceptance',nominal_least_residual_proposal=str(t0),selected_lower_trial=lower,selected_upper_trial=upper,actual_augmented_inverse_response_lower=str(acceptedlo),actual_augmented_inverse_response_upper=str(acceptedhi),actual_augmented_inverse_response_width_upper=str(up(acceptedhi-acceptedlo)),upper_bound_improvement_factor_lower=str(down(generichi/acceptedhi)),no_global_optimality_claimed=True))
 # Nonidentity D metric, nonorthogonal physical source columns, nonzero
 # residual: the correlated signed identity must ADD the correction.
 D=[[F(2),F(0)],[F(0),F(3)]];G=[[F(4),F(1)],[F(1),F(5)]];Q=[[F(1),F(1,4)],[F(1,3),F(1)]];Y=[[F(1,7),-F(1,9)],[F(2,11),F(1,13)]]
 N=p.mm(p.inv(D),G);R=p.mm(p.inv(D),Q);e=p.add(R,p.mm(N,Y),-1)
 exact=p.mm(p.trans(Q),p.mm(p.inv(G),Q));center=p.add(p.add(p.mm(p.trans(Q),Y),p.mm(p.trans(Y),Q)),p.mm(p.trans(Y),p.mm(G,Y)),-1)
 Egram=p.mm(p.trans(e),p.mm(D,e));correction=p.mm(p.trans(e),p.mm(D,p.mm(p.inv(N),e)))
 assert exact==p.add(center,correction) and exact!=p.add(center,correction,-1)
 assert p.psd(p.add(G,D,-1)) and p.psd(p.add(p.scale(F(3),D),G,-1))
 assert p.psd(p.add(correction,p.scale(F(1,3),Egram),-1)) and p.psd(p.add(Egram,correction,-1))
 lower=[[rows[0]['actual_augmented_inverse_response_lower'],'0'],['0',rows[1]['actual_augmented_inverse_response_lower']]]
 upper=[[rows[0]['actual_augmented_inverse_response_upper'],'0'],['0',rows[1]['actual_augmented_inverse_response_upper']]]
 return dict(milestone='RC233',starting_commit='fc15a9534376d43e6fb7a60b2543593f3e4c417f',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,chosen_operator='same actual RC115 rational Hhat, represented by N in D energy',actual_canonical_source_order=['r0=i*P0','r1=i*P1'],response_identity='S_c* Hhat^-1 S_c = R* D N^-1 R, R=D^-1[P0,P1]',actual_augmented_inverse_response_Gram_lower=lower,actual_augmented_inverse_response_Gram_upper=upper,parity_inverse_response_certificates=rows,actual_augmented_inverse_response_Gram_enclosed=True,actual_iterative_inverse_solutions_computed=False,canonical_Riesz_images_numerically_constructed=False,all_complex_combinations_of_r0_r1_covered=True,opposite_parity_inverse_response_pairing_zero=True,full_639_auxiliary_source_range_covered=False,frequency_auxiliary_preimages_or_metric_evaluated=False,auxiliary_norm_from_physical_source_Gram_inferred=False,canonical_half_width_gate_transferred_to_augmented_operator=False,added_inverse_residual_correction_used=True,abstract_correlated_residual_control=dict(D=p.ser(D),physical_form=p.ser(G),source=p.ser(Q),trial=p.ser(Y),inverse_response=p.ser(exact),variational_center=p.ser(center),added_correction=p.ser(correction),actual_residual_Gram=p.ser(Egram),full_correlated_identity_and_sandwich_verified=True,is_actual_Weil_computation=False),original_augmented_response_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC234: materialize tighter rational/band augmentation actions and richer actual response trials; certify auxiliary metric/full-range response rather than infer it from these two moment-source enclosures')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();c=run(args.replay)
 if args.replay:assert c==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC233 PASS: actual augmented inverse Gram enclosed on r0/r1; full auxiliary response gate open',flush=True)
