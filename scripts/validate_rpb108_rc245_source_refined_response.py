"""RC245: refined original source output with exactly shared trial actions."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
from math import factorial
import argparse,hashlib,json
import validate_rpb108_rc244_four_trial_signed_response as parent
native=parent.parent.parent
orig=parent.orig;p=parent.p;B=parent.B
up=parent.up;down=parent.down;root=parent.root;rootdown=parent.rootdown
quadratic=parent.quadratic;CUT=128;ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc244_four_trial_signed_response.json':'c184e3cdad510fcd10fe1d8a15cae677a4321a92','notes/RPB108_RC244_FOUR_TRIAL_SIGNED_RESPONSE_20261014.md':'904513e14d7747aa3820a0c6b47a06921c478e7a'})
HELPER_PINS['scripts/validate_rpb108_rc244_four_trial_signed_response.py']='7512b8363151af8512f2553b39e7f5c88973ac8a'
def refined_source(base,old,reg,eps,prime,sl,sh,reverse):
 a=[F(0)]*65;a[base]=F(1);q=native.input_poly(a)
 rp=native.regular(q,base,reg);rc=[orig.project(rp,n) for n in range(len(rp))]
 rt=up(sum((orig.mass(n)*v*v for n,v in enumerate(rc) if n>CUT),F(0)))
 pc,pt,pfault,proof=native.prime_action(q,a,base,prime,reverse)
 phi=[F(11,20)**k/factorial(k) if k%2==base else F(0) for k in range(41)];moment=B*orig.integral(orig.product(q,phi));pole=[2*(-1)**base*moment*v for v in phi];oc=[orig.project(pole,n) for n in range(CUT+1)]
 ll=2*sum((F(1,3)**(2*k+1)/F(2*k+1) for k in range(100)),F(0));lh=ll+2*F(1,3)**201/(201*(1-F(1,9)));out=deepcopy(old['finite_original_D_action']);rounding=F(0)
 for n,x in enumerate(out):rounding+=orig.mass(n)*(orig.H(n)+sh)*F(x['radius'])**2
 for n in range(65,CUT+1):
  if n%2!=base:out.append(dict(degree=n,coefficient='0',radius='0'));continue
  h,hr=native.endpoint(a,n,ll,lh);v=h-rc[n]+pc[n]+oc[n]
  values=[x/(orig.H(n)+s) for x in [v-hr,v+hr] for s in [sl,sh]];lo=min(values);hi=max(values);c=down((lo+hi)/2);rad=max(c-lo,hi-c);rounding+=orig.mass(n)*(orig.H(n)+sh)*rad*rad;out.append(dict(degree=n,coefficient=str(c),radius=str(up(rad))))
 et,eproof=native.endpoint_tail(a,base,sl,ll,lh,reverse);mass=orig.mass(base);first=129 if base else 130;tau=2*F(11,20)**41/factorial(41);polefault=up(16*B*tau*root(mass))
 # The first 65 coefficients retain the original fine-parameter model.
 # The extended block uses the paid 16-digit prime model. Projected model
 # faults are contractive in D energy; add both full model fault norms.
 newprime=up(pfault*pfault/sl);oldprime=F(old['D_energy_component_squared_errors']['prime_arithmetic']);hybridprime=up((root(oldprime)+root(newprime))**2)
 comp=dict(finite_rounding=up(rounding),endpoint_omitted_output=et,regular_omitted_output=up(rt/(orig.H(first)+sl)),prime_omitted_output=up(pt/(orig.H(first)+sl)),regular_kernel=up((2*B*eps)**2*mass/sl),prime_arithmetic=hybridprime,pole_Taylor=up(polefault*polefault/sl));E=up(sum((root(v) for v in comp.values()),F(0))**2)
 r=deepcopy(old);r['finite_original_D_action']=out;r['D_energy_component_squared_errors']={k:str(v) for k,v in comp.items()};r['complete_original_action_D_error_squared_upper']=str(E)
 return r,dict(retained_old_original_coefficients_through_degree=64,extended_original_coefficients_through_degree=CUT,prime_controls=proof,old_fine_prime_model_D_error_squared_upper=str(oldprime),new_extension_prime_model_D_error_squared_upper=str(newprime),hybrid_prime_model_D_error_squared_upper=str(hybridprime),endpoint_tail_controls=eproof)
def response(base,columns,F0,Gy,lam,mu,nu,sl,sh,prior,reverse):
 O=[[F(r['coefficient']) for r in c['original']['finite_original_D_action']] for c in columns];A=[[F(r['coefficient']) for r in c['finite_complete_augmented_D_action']] for c in columns]
 Eo=[F(c['original']['complete_original_action_D_error_squared_upper']) for c in columns];Ea=[F(c['augmentation_action_D_error_squared_upper']) for c in columns];sm=(sl+sh)/2
 AG=[[sum((orig.mass(n)*(orig.H(n)+sm)*A[i][n]*A[k][n] for n in range(CUT+1)),F(0)) for k in range(4)] for i in range(4)]
 rhs=[sum((orig.mass(n)*(orig.H(n)+sm)*O[0][n]*A[i][n] for n in range(CUT+1)),F(0)) for i in range(4)];source=sum((orig.mass(n)*(orig.H(n)+sm)*O[0][n]**2 for n in range(CUT+1)),F(0));assert p.psd(AG)
 least_exact=[r[0] for r in p.mm(p.inv(AG),[[v] for v in rhs])];least=[down(v) for v in least_exact]
 twoGram=[row[:3] for row in AG[:3]];two=[r[0] for r in p.mm(p.inv(twoGram),[[v] for v in rhs[:3]])]
 twofit=source-sum((rhs[i]*two[i] for i in range(3)),F(0));threefit=source-sum((rhs[i]*least_exact[i] for i in range(4)),F(0));assert 0<=threefit<=twofit
 GM=[[(F0[i][k][0]+F0[i][k][1]+lam*(Gy[i][k][0]+Gy[i][k][1]))/2 for k in range(4)] for i in range(4)];fm=[(F0[i][0][0]+F0[i][0][1])/2 for i in range(4)];gal=[down(r[0]) for r in p.mm(p.inv(GM),[[v] for v in fm])]
 old=list(map(F,prior['selected_inverse_upper_trial']['trial_coefficients']));assert len(old)==4
 choices={tuple(old),(F(0),)*4,tuple(least),tuple(gal)}
 for k in range(-10,21):choices.add(tuple(down(old[i]+F(k,10)*(least[i]-old[i])) for i in range(4)))
 for k in range(8,13):
  choices.add(tuple(down(F(k,10)*v) for v in least));choices.add(tuple(down(F(k,10)*v) for v in gal))
 def evaluate(y):
  v=[O[0][n]-sum((y[i]*A[i][n] for i in range(4)),F(0)) for n in range(CUT+1)];terms=[(n,orig.mass(n)*x*x) for n,x in enumerate(v)]
  if reverse:terms.reverse()
  nl=sum((x*(orig.H(n)+sl) for n,x in terms),F(0));nh=sum((x*(orig.H(n)+sh) for n,x in terms),F(0))
  fault=abs(1-y[0])*root(Eo[0])+sum((abs(y[i])*root(Eo[i]) for i in [1,2,3]),F(0))+sum((abs(y[i])*root(Ea[i]) for i in range(4)),F(0))
  rl=down(max(F(0),rootdown(nl)-fault)**2);rh=up((root(nh)+fault)**2);u=[1-y[0],-y[1],-y[2],-y[3]];qlo,qhi=quadratic(F0,u);alo,ahi=quadratic(Gy,y)
  cl=ch=F(0)
  for i in range(4):
   for k in range(4):
    w=(y[k] if i==0 else 0)+(y[i] if k==0 else 0)-y[i]*y[k];a,b=F0[i][k];cl+=min(w*a,w*b);ch+=max(w*a,w*b)
    w=-lam*y[i]*y[k];a,b=Gy[i][k];cl+=min(w*a,w*b);ch+=max(w*a,w*b)
  return dict(trial_coefficients=list(map(str,y)),retained_center_residual_D_energy_lower=str(down(nl)),retained_center_residual_D_energy_upper=str(up(nh)),shared_complete_fault_D_norm_upper=str(up(fault)),actual_residual_D_energy_lower=str(rl),actual_residual_D_energy_upper=str(rh),original_action_inverse_response_lower=str(down(cl+rl/nu)),original_action_inverse_response_upper=str(up(ch+rh/mu)),coupled_signed_gap_lower=str(down(qlo+lam*alo-rh/mu)),coupled_signed_gap_upper=str(up(qhi+lam*ahi-rl/nu)))
 candidates=[evaluate(y) for y in sorted(choices)];lower=max(candidates,key=lambda r:F(r['original_action_inverse_response_lower']));upper=min(candidates,key=lambda r:F(r['original_action_inverse_response_upper']))
 tl=max(F(prior['actual_original_action_inverse_response_lower']),F(lower['original_action_inverse_response_lower']));th=min(F(prior['actual_original_action_inverse_response_upper']),F(upper['original_action_inverse_response_upper']));dl=max(F(prior['actual_signed_gap_lower']),max(F(r['coupled_signed_gap_lower']) for r in candidates),down(F0[0][0][0]-th));dh=min(F(prior['actual_signed_gap_upper']),min(F(r['coupled_signed_gap_upper']) for r in candidates),up(F0[0][0][1]-tl));assert tl<=th and dl<=dh
 return dict(source='N0 P'+str(base),response_trial_basis=['P'+str(base),'P'+str(base+2),'P'+str(base+4),'R'+str(base)],candidate_count=len(candidates),nominal_least_residual_proposal=list(map(str,least)),nominal_Galerkin_proposal=list(map(str,gal)),three_trial_nominal_minimum_retained_Dmid_residual_energy=str(twofit),four_trial_nominal_minimum_retained_Dmid_residual_energy=str(threefit),nominal_fit_is_actual_response_certificate=False,selected_inverse_lower_trial=lower,selected_inverse_upper_trial=upper,actual_original_action_inverse_response_lower=str(tl),actual_original_action_inverse_response_upper=str(th),previous_original_action_inverse_response_upper=prior['actual_original_action_inverse_response_upper'],actual_signed_gap_lower=str(dl),actual_signed_gap_upper=str(dh),previous_signed_gap_lower=prior['actual_signed_gap_lower'],original_action_inverse_upper_improved=th<F(prior['actual_original_action_inverse_response_upper']),signed_gap_lower_improved=dl>F(prior['actual_signed_gap_lower']),signed_gap_positive_certified=dl>0,actual_negative_gap_proved=dh<0)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin');data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('244_four_trial_signed_response');p240=get('240_three_trial_signed_response');p243=get('243_residual_augmented_actions');p242=get('242_residual_original_actions');p239=get('239_exterior_band_leakage');p238=get('238_weighted_action_tails');p237=get('237_two_trial_signed_response');baseorig=get('231_original_polynomial_action');baseaug=get('234_materialized_band_action');bounds=get('232_augmented_polynomial_action');metric=get('129_four_vector_joint_moment');kernel=get('46_native_archimedean_head');prime=get('43_native_prime_head')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);reg=list(map(F,kernel['regular_kernel_coefficients']));eps=F(kernel['regular_kernel_uniform_error_upper']);rows=[]
 for base in [0,1]:
  pr=prior['parity_four_trial_signed_response_certificates'][base];ar=p237['parity_two_trial_signed_response_certificates'][base];r240=p240['parity_three_trial_signed_response_certificates'][base];r239=p239['parity_exterior_tail_response_certificates'][base];bound=bounds['polynomial_augmented_action_certificates'][base];columns=[]
  original,proof=refined_source(base,baseorig['polynomial_original_action_certificates'][base],reg,eps,prime,sl,sh,reverse)
  previousE=r239['action_exterior_tail_refinements'][0]['original_action_D_error_squared_upper'];assert F(original['complete_original_action_D_error_squared_upper'])<F(previousE)
  oldO=parent.pad(baseorig['polynomial_original_action_certificates'][base]['finite_original_D_action']);oldN=parent.pad(baseaug['parity_materialized_augmented_action_certificates'][base]['finite_complete_augmented_D_action']);newN=[]
  for x,o,n in zip(original['finite_original_D_action'],oldO,oldN):
   aug=F(n['coefficient'])-F(o['coefficient']);c=F(x['coefficient'])+aug
   assert c-F(x['coefficient'])==aug
   newN.append(dict(degree=x['degree'],coefficient=str(c),radius=str(up(F(x['radius'])+F(n['radius'])+F(o['radius'])))))
  AE=r239['action_exterior_tail_refinements'][0]['refined_augmentation_action_D_error_squared_upper'];E=up((root(F(original['complete_original_action_D_error_squared_upper']))+root(F(AE)))**2)
  columns.append(dict(original=original,finite_complete_augmented_D_action=newN,augmentation_action_D_error_squared_upper=AE,complete_augmented_action_D_error_squared_upper=str(E)))
  second=deepcopy(ar['new_complete_original_action']);second['finite_original_D_action']=parent.pad(second['finite_original_D_action']);second['complete_original_action_D_error_squared_upper']=r239['action_exterior_tail_refinements'][1]['original_action_D_error_squared_upper'];second['D_energy_component_squared_errors']['endpoint_omitted_output']=p238['parity_weighted_tail_response_certificates'][base]['action_tail_refinements'][1]['accepted_endpoint_omitted_output_D_energy_upper']
  columns.append(dict(original=second,finite_complete_augmented_D_action=parent.pad(ar['new_complete_augmented_D_action']),augmentation_action_D_error_squared_upper=r239['action_exterior_tail_refinements'][1]['refined_augmentation_action_D_error_squared_upper'],complete_augmented_action_D_error_squared_upper=r239['action_exterior_tail_refinements'][1]['refined_complete_augmented_action_D_error_squared_upper']))
  third=deepcopy(r240['new_complete_original_action']);third['finite_original_D_action']=parent.pad(third['finite_original_D_action'])
  columns.append(dict(original=third,finite_complete_augmented_D_action=parent.pad(r240['new_complete_augmented_D_action']),augmentation_action_D_error_squared_upper=r240['new_augmentation_action_D_error_squared_upper'],complete_augmented_action_D_error_squared_upper=r240['new_complete_augmented_action_D_error_squared_upper']))
  fourth=deepcopy(p242['parity_residual_original_action_certificates'][base]);fourth['finite_original_D_action']=fourth['finite_complete_original_D_action'];aug=p243['parity_residual_augmented_action_certificates'][base]
  columns.append(dict(original=fourth,finite_complete_augmented_D_action=aug['finite_complete_augmented_D_action'],augmentation_action_D_error_squared_upper=aug['complete_rational_augmentation_action_D_error_squared_upper'],complete_augmented_action_D_error_squared_upper=aug['complete_augmented_action_D_error_squared_upper']))
  F0=[[(F(a),F(b)) for a,b in row] for row in pr['original_trial_form_intervals']];Gy=[[(F(a),F(b)) for a,b in row] for row in pr['frequency_trial_Gram_intervals']]
  result=response(base,columns,F0,Gy,F(bound['augmentation_coefficient']),F(bound['fresh_augmented_N_D_lower']),F(bound['fresh_augmented_N_D_upper']),sl,sh,pr['source_inverse_response'],reverse)
  # A second rigorous option keeps the old center, but splits its model
  # error into orthogonal output-degree blocks. This is output orthogonality,
  # not an assumption that different input-column faults are independent.
  comp=original['D_energy_component_squared_errors']
  finite_low=sum((orig.mass(n)*(orig.H(n)+sh)*F(x['radius'])**2 for n,x in enumerate(oldO[:65])),F(0))
  resolved=sum((orig.mass(n)*(orig.H(n)+sh)*(abs(F(x['coefficient']))+F(x['radius']))**2 for n,x in enumerate(original['finite_original_D_action']) if n>64),F(0))
  tail128=up(sum((root(F(comp[k])) for k in ['endpoint_omitted_output','regular_omitted_output','prime_omitted_output']),F(0))**2)
  model_fault=sum((root(F(comp[k])) for k in ['regular_kernel','prime_arithmetic','pole_Taylor']),F(0))
  E64=up((root(up(finite_low+resolved+tail128))+model_fault)**2);assert E64<F(previousE)
  old_center_source=deepcopy(baseorig['polynomial_original_action_certificates'][base]);old_center_source['finite_original_D_action']=oldO;old_center_source['complete_original_action_D_error_squared_upper']=str(E64)
  old_center_N_error=up((root(E64)+root(F(AE)))**2);alternate=deepcopy(columns);alternate[0]=dict(original=old_center_source,finite_complete_augmented_D_action=oldN,augmentation_action_D_error_squared_upper=AE,complete_augmented_action_D_error_squared_upper=str(old_center_N_error))
  revised=response(base,alternate,F0,Gy,F(bound['augmentation_coefficient']),F(bound['fresh_augmented_N_D_lower']),F(bound['fresh_augmented_N_D_upper']),sl,sh,result,reverse)
  splitproof=dict(old_center_retained_degree=64,old_low_degree_model_rounding_D_energy_upper=str(up(finite_low)),combined_original_model_degree_65_through_128_D_energy_upper=str(up(resolved)),original_model_beyond_128_D_energy_upper=str(tail128),actual_to_hybrid_model_fault_D_norm_upper=str(up(model_fault)),refined_old_center_original_source_D_error_squared_upper=str(E64),updated_old_center_first_augmented_action_D_error_squared_upper=str(old_center_N_error),different_output_degree_blocks_orthogonal_in_actual_D=True,different_input_column_errors_assumed_independent=False)
  rows.append(dict(parity=pr['parity'],refined_complete_original_source_action=original,refined_original_source_action_controls=proof,previous_original_source_D_error_squared_upper=previousE,refined_original_source_D_error_squared_upper=original['complete_original_action_D_error_squared_upper'],updated_first_complete_augmented_trial_center=newN,updated_first_complete_augmented_action_D_error_squared_upper=str(E),unchanged_first_augmentation_action_D_error_squared_upper=AE,original_trial_form_intervals=pr['original_trial_form_intervals'],frequency_trial_Gram_intervals=pr['frequency_trial_Gram_intervals'],degree_128_center_response=result,old_center_orthogonal_output_split_certificate=splitproof,source_inverse_response=revised,exact_first_augmentation_center_difference_preserved=True,original_source_and_first_trial_updated_together=True))
 return dict(milestone='RC245',starting_commit='6e56c17f165645933ea481d90bf755f4561ae5b9',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_response_source_count=2,response_trials_per_parity=4,retained_original_source_degree=128,parity_source_refined_response_certificates=rows,first_65_original_source_center_coefficients_preserved=True,actual_original_and_frequency_form_intervals_preserved=True,shared_original_source_action_fault_preserved=True,prime_model_extension_rounding_and_hybrid_faults_paid=True,all_same_parity_cross_terms_paid=True,same_parity_action_errors_assumed_orthogonal=False,exact_controls=parent.controls(),new_response_enclosures_intersected_with_RC244=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC246: materialize or refine the residual-trial augmentation output, now that original source tails are sharper; full signed positivity remains required')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC245 VALIDATED: refined original sources and correlated trial actions; full signed gate open',flush=True)

