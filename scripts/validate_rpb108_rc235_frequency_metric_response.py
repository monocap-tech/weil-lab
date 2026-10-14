"""RC235: actual frequency metric and restricted rational auxiliary response.
Shared augmentation errors are coupled before residual norm payment.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc234_materialized_band_action as parent
bridge=parent.bridge;orig=parent.orig;p=bridge.p
up=bridge.up;down=bridge.down;root=bridge.rootup;rootdown=parent.parent.rootdown
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc234_materialized_band_action.json':'a90747a23f48bb0583acdd2d814856d605b41469','notes/RPB108_RC234_MATERIALIZED_BAND_ACTION_AND_TIGHTER_INVERSE_RESPONSES_20261014.md':'1af7293c8e9f69086de5f22d478d7f9905fa2b74'})
HELPER_PINS['scripts/validate_rpb108_rc234_materialized_band_action.py']='f1f68e92d521337cea8303867821c363fe59a1ad'
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  raw=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha,(path,'pin')
  data[path]=json.loads(raw) if path.endswith('.json') else raw.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 new=get('234_materialized_band_action');previous=get('232_augmented_polynomial_action');original=get('231_original_polynomial_action');rangeproof=get('230_augmentation_range_bridge');metric=get('129_four_vector_joint_moment')
 assert new['chosen_rational_operator_unchanged'] and new['actual_rational_augmentation_difference_paid'] and rangeproof['full_chosen_augmentation_rank']==639
 B=F(11,10);sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);rows=[]
 for j,row in enumerate(new['parity_materialized_augmented_action_certificates']):
  old=original['polynomial_original_action_certificates'][j];pr=previous['polynomial_augmented_action_certificates'][j]
  lam=F(pr['augmentation_coefficient']);epsilon=F(pr['physical_Fhat_star_Fhat_to_J_star_J_operator_norm_upper']);mass=orig.mass(j)
  band=row['actual_band_Gram_column'][j];gyl=down(F(band['lower'])-epsilon*mass);gyh=up(F(band['upper'])+epsilon*mass);assert 0<gyl<=gyh
  flo=F(row['sharper_original_test_form_lower']);fhi=F(row['sharper_original_test_form_upper']);assert 0<flo<=fhi
  O=[F(r['coefficient']) for r in old['finite_original_D_action']];A=[F(r['coefficient']) for r in row['finite_complete_augmented_D_action']]
  R=[(a-o)/lam for a,o in zip(A,O)]
  Eo=F(old['complete_original_action_D_error_squared_upper']);Ea=F(row['actual_augmentation_action_D_error_squared_upper'])
  mu=F(pr['fresh_augmented_N_D_lower']);nu=F(pr['fresh_augmented_N_D_upper'])
  assert all(v==0 for n,v in enumerate(R) if n%2!=j)
  def trial(t):
   assert 0<=t<=2/lam
   alpha=1-lam*t
   residual=[alpha*r-t*o for r,o in zip(R,O)]
   terms=[(n,orig.mass(n)*v*v) for n,v in enumerate(residual)]
   if reverse:terms.reverse()
   nl=sum((v*(orig.H(n)+sl) for n,v in terms),F(0));nh=sum((v*(orig.H(n)+sh) for n,v in terms),F(0))
   sharedfault=up(abs(alpha)*root(Ea)/lam+t*root(Eo))
   independentfault=up(root(Ea)/lam+t*root(F(row['complete_augmented_action_D_error_squared_upper'])))
   rl=down(max(F(0),rootdown(nl)-sharedfault)**2);rh=up((root(nh)+sharedfault)**2)
   coeff=lam*(2*t-lam*t*t);assert coeff>=0
   cl=down(coeff*gyl-lam*t*t*fhi);ch=up(coeff*gyh-lam*t*t*flo)
   abslo=down(cl+lam*rl/nu);abshi=up(ch+lam*rh/mu)
   # Keep the common exact Gy in the variational center and denominator.
   relo=down(coeff-lam*t*t*fhi/gyl+lam*rl/(nu*gyh))
   relhi=up(coeff-lam*t*t*flo/gyh+lam*rh/(mu*gyl))
   assert abslo<=abshi and relo<=relhi
   return dict(trial_coefficient=str(t),shared_augmentation_residual_multiplier=str(alpha),nominal_residual_D_Gram_lower=str(down(nl)),nominal_residual_D_Gram_upper=str(up(nh)),shared_residual_fault_D_norm_upper=str(sharedfault),independently_paid_fault_D_norm_upper=str(independentfault),actual_residual_D_Gram_lower=str(rl),actual_residual_D_Gram_upper=str(rh),scaled_variational_center_lower=str(cl),scaled_variational_center_upper=str(ch),added_scaled_inverse_correction_lower=str(down(lam*rl/nu)),added_scaled_inverse_correction_upper=str(up(lam*rh/mu)),actual_auxiliary_response_Gram_lower=str(abslo),actual_auxiliary_response_Gram_upper=str(abshi),relative_to_actual_frequency_Gram_lower=str(relo),relative_to_actual_frequency_Gram_upper=str(relhi))
  candidates=sorted(set([F(k,1000)/lam for k in range(950,1051)]+[F(0),1/lam]))
  trials=[trial(t) for t in candidates]
  l=max(trials,key=lambda r:(F(r['relative_to_actual_frequency_Gram_lower']),-F(r['trial_coefficient'])))
  h=min(trials,key=lambda r:(F(r['relative_to_actual_frequency_Gram_upper']),F(r['trial_coefficient'])))
  cancellation=trial(1/lam);assert cancellation['shared_augmentation_residual_multiplier']=='0'
  assert F(cancellation['shared_residual_fault_D_norm_upper'])<F(cancellation['independently_paid_fault_D_norm_upper'])
  abslo=max(F(0),max(F(r['actual_auxiliary_response_Gram_lower']) for r in trials));abshi=min(F(r['actual_auxiliary_response_Gram_upper']) for r in trials)
  relo=max(F(0),F(l['relative_to_actual_frequency_Gram_lower']));relhi=F(h['relative_to_actual_frequency_Gram_upper']);assert 0<relo<=relhi
  rows.append(dict(parity=row['parity'],actual_frequency_vector='y'+str(j)+'=Fhat P'+str(j),actual_canonical_source='Xhat* y'+str(j)+'=i* Fhat* Fhat P'+str(j),actual_D_source='D^-1 Fhat* Fhat P'+str(j),physical_input='P'+str(j),augmentation_coefficient=str(lam),actual_frequency_Gram_lower=str(gyl),actual_frequency_Gram_upper=str(gyh),actual_auxiliary_response_Gram_lower=str(abslo),actual_auxiliary_response_Gram_upper=str(abshi),relative_auxiliary_response_lower=str(relo),relative_auxiliary_response_upper=str(relhi),selected_relative_lower_trial=l,selected_relative_upper_trial=h,exact_shared_augmentation_cancellation_trial=cancellation,candidate_count=len(trials),frequency_metric_rational_to_band_error_paid=str(up(epsilon*mass)),source_and_action_augmentation_errors_identified_before_payment=True,restricted_direction_upper_below_one_certified=relhi<1,minimum_actual_frequency_norm_squared_lower=str(gyl)))
 # Nonidentity D, arbitrary trial and noncommuting original/augmentation:
 # R=Aq, N=N0+lambda A; e=(1-lambda t)R-tN0q exactly.
 D=[[F(2),F(0)],[F(0),F(3)]];G0=[[F(4),F(1)],[F(1),F(5)]];Fhat=[[F(1),F(1,2)],[F(1,3),F(2,3)]];lam=F(9,4)
 K=p.mm(p.trans(Fhat),Fhat);Di=p.inv(D);N0=p.mm(Di,G0);Aop=p.mm(Di,K);N=p.add(N0,p.scale(lam,Aop));G=p.add(G0,p.scale(lam,K));q=[[F(1)],[F(1,5)]];R=p.mm(Aop,q)
 assert p.mm(N0,Aop)!=p.mm(Aop,N0)
 for t in [F(0),F(1,7),1/lam,F(2,5)]:
  Y=p.scale(t,q);e=p.add(R,p.mm(N,Y),-1);coupled=p.add(p.scale(1-lam*t,R),p.scale(t,p.mm(N0,q)),-1);assert e==coupled
  source=p.mm(K,q);exact=p.scale(lam,p.mm(p.trans(source),p.mm(p.inv(G),source)))
  center=p.add(p.add(p.mm(p.trans(source),Y),p.mm(p.trans(Y),source)),p.mm(p.trans(Y),p.mm(G,Y)),-1)
  correction=p.mm(p.trans(e),p.mm(D,p.mm(p.inv(N),e)));assert exact==p.scale(lam,p.add(center,correction))
 theta=max(F(r['relative_auxiliary_response_upper']) for r in rows);lower=max(F(r['relative_auxiliary_response_lower']) for r in rows)
 return dict(milestone='RC235',starting_commit='1426c6461d22ba2f570695fda5683801b352df64',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,chosen_operator='same actual RC115 rational Hhat and full frequency operator Bhat=lambda Fhat N^-1 D^-1 Fhat*',actual_frequency_test_vector_order=['y0=Fhat P0','y1=Fhat P1'],frequency_test_dimension=2,full_chosen_augmentation_rank=639,actual_frequency_metric_certified_on_test_span=True,actual_frequency_Gram_lower=[[rows[0]['actual_frequency_Gram_lower'],'0'],['0',rows[1]['actual_frequency_Gram_lower']]],actual_frequency_Gram_upper=[[rows[0]['actual_frequency_Gram_upper'],'0'],['0',rows[1]['actual_frequency_Gram_upper']]],actual_restricted_auxiliary_response_Gram_lower=[[rows[0]['actual_auxiliary_response_Gram_lower'],'0'],['0',rows[1]['actual_auxiliary_response_Gram_lower']]],actual_restricted_auxiliary_response_Gram_upper=[[rows[0]['actual_auxiliary_response_Gram_upper'],'0'],['0',rows[1]['actual_auxiliary_response_Gram_upper']]],parity_frequency_metric_response_certificates=rows,restricted_auxiliary_operator_norm_upper=str(theta),restricted_operator_means_orthogonal_compression=True,test_span_invariance_claimed=False,full_auxiliary_operator_norm_lower=str(lower),if_full_norm_below_one_then_gap_upper=str(up(1-lower)),restricted_auxiliary_norm_below_one_certified=theta<1,full_auxiliary_norm_upper_claimed=False,full_auxiliary_norm_below_one_certified=False,actual_auxiliary_norm_above_one_proved=False,all_complex_combinations_of_frequency_test_vectors_covered=True,opposite_parity_frequency_and_response_pairings_zero=True,exact_augmentation_source_action_residual_cancellation_proved=True,nonidentity_noncommuting_shared_residual_control_verified=True,physical_moment_inverse_uppers_reused_as_auxiliary_norm=False,full_frequency_Gram_evaluated=False,all_639_channels_exhausted=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC236: tighten original-action residuals and richer response trials for the actual frequency sources; extend beyond the two-vector auxiliary span with a paid full-range bound')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();c=run(args.replay)
 if args.replay:assert c==json.loads(args.output.read_text())
 else:args.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC235 VALIDATED: actual frequency metric and restricted response enclosed; below-one gate status',c['restricted_auxiliary_norm_below_one_certified'],flush=True)
