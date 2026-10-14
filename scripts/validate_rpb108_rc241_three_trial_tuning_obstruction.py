"""RC241: uniform coefficient-tuning obstruction for the RC240 enclosure.
An upper-bound formula floor is not a lower bound for the true response.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc240_three_trial_signed_response as parent
orig=parent.orig;p=parent.p;B=parent.B;CUT=64
up=parent.up;down=parent.down;root=parent.root;rootdown=parent.rootdown
ROOT=Path(__file__).resolve().parents[1]
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc240_three_trial_signed_response.json':'6c41b7f196052fea179b956099fb69cc5d07813c','notes/RPB108_RC240_THREE_TRIAL_SIGNED_RESPONSE_20261014.md':'c61d6f1ce20ffac15e7abcef3cde10726e2b5e36'})
HELPER_PINS['scripts/validate_rpb108_rc240_three_trial_signed_response.py']='9e1f46907a3c96d2f916d709163d0dea0db5190a'
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def mv(A,y):return [dot(row,y) for row in A]
def controls():
 # Exact completion of a strictly convex three-dimensional quadratic.
 H=[[F(3),F(1,4),F(1,7)],[F(1,4),F(4),-F(1,5)],[F(1,7),-F(1,5),F(5)]];h=[F(1,3),-F(2,5),F(3,7)];c=F(9)
 assert p.psd(H);z=mv(p.inv(H),h);ystar=[-v for v in z];minimum=c-dot(h,z)
 for y in [[F(0)]*3,[F(1),-F(2),F(3)],[F(1,5),F(2,7),-F(3,11)]]:
  v=[a-b for a,b in zip(y,ystar)];assert c+2*dot(h,y)+dot(y,mv(H,y))==minimum+dot(v,mv(H,v))
 # Analytic minimum of sqrt(d^2+sigma^2*t^2)-delta*t for t>=0.
 # Choose a rational stationary point and exact square roots for a control.
 d=F(3);sigma=F(5);delta=F(3);t=F(9,20)
 assert d*d+sigma*sigma*t*t==F(225,16)
 assert F(15,4)-delta*t==d*F(4,5)
 assert delta*delta/sigma**2<F(1)
 return dict(exact_three_dimensional_quadratic_completion=True,robust_residual_stationary_minimum_control=True,method_obstruction_is_not_true_response_lower_bound=True)
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin');data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 prior=get('240_three_trial_signed_response');old=get('237_two_trial_signed_response');refined=get('239_exterior_band_leakage');baseorig=get('231_original_polynomial_action');baseaug=get('234_materialized_band_action');bounds=get('232_augmented_polynomial_action');metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);rows=[]
 for base in [0,1]:
  r=prior['parity_three_trial_signed_response_certificates'][base];rr=refined['parity_exterior_tail_response_certificates'][base];ar=old['parity_two_trial_signed_response_certificates'][base];bound=bounds['polynomial_augmented_action_certificates'][base];lam=F(bound['augmentation_coefficient']);mu=F(bound['fresh_augmented_N_D_lower']);nu=F(bound['fresh_augmented_N_D_upper'])
  O=[F(x['coefficient']) for x in baseorig['polynomial_original_action_certificates'][base]['finite_original_D_action']]
  A=[[F(x['coefficient']) for x in c] for c in [baseaug['parity_materialized_augmented_action_certificates'][base]['finite_complete_augmented_D_action'],ar['new_complete_augmented_D_action'],r['new_complete_augmented_D_action']]]
  errors=[F(a['refined_complete_augmented_action_D_error_squared_upper']) for a in rr['action_exterior_tail_refinements']]+[F(r['new_complete_augmented_action_D_error_squared_upper'])]
  source_error=F(rr['action_exterior_tail_refinements'][0]['original_action_D_error_squared_upper'])
  terms=list(range(CUT+1));terms=terms[::-1] if reverse else terms
  weights=[orig.mass(n)*(orig.H(n)+sl) for n in range(CUT+1)]
  AG=[[sum((weights[n]*A[i][n]*A[k][n] for n in terms),F(0)) for k in range(3)] for i in range(3)]
  rhs=[sum((weights[n]*O[n]*A[i][n] for n in terms),F(0)) for i in range(3)];c=sum((weights[n]*O[n]*O[n] for n in terms),F(0));inv=p.inv(AG);assert p.psd(AG)
  Fmid=[[(F(a)+F(b))/2 for a,b in row] for row in r['original_trial_form_intervals']];Ymid=[[(F(a)+F(b))/2 for a,b in row] for row in r['frequency_trial_Gram_intervals']];Gmid=p.add(Fmid,p.scale(lam,Ymid));f=[Fmid[i][0] for i in range(3)]
  least=mv(inv,rhs);d2=c-dot(rhs,least);assert d2>0
  sigma2=1/sum((inv[i][i] for i in range(3)),F(0));sigma_matrix=p.add(AG,p.scale(-sigma2,[[F(i==k) for k in range(3)] for i in range(3)]));assert p.psd(sigma_matrix)
  delta2=sum(errors,F(0));assert delta2<sigma2
  leastnorm=root(dot(least,least));robust=down(rootdown(d2*(1-delta2/sigma2))-root(source_error)-root(delta2)*leastnorm);assert robust>0
  # U_cert(y)>=C_mid(y)+||O_center-A_center*y||_(D_lower)^2/mu.
  # Its quadratic lower envelope is globally minimized exactly.
  H=p.add(p.scale(1/mu,AG),Gmid,-1);h=[f[i]-rhs[i]/mu for i in range(3)];assert p.psd(H);hi=p.inv(H);minimum=c/mu-dot(h,mv(hi,h));minimizer=[-v for v in mv(hi,h)]
  assert minimum>F(r['original_trial_form_intervals'][0][0][1])
  gapceiling=Fmid[0][0]-minimum;assert gapceiling<0
  # Completing the quadratic at several exact vectors checks signs and the
  # dependence on the original form, augmentation, and global inverse floor.
  candidates=[[F(0)]*3,least,minimizer,list(map(F,r['source_inverse_response']['selected_inverse_upper_trial']['trial_coefficients']))]
  for y in candidates:
   residual=c-2*dot(rhs,y)+dot(y,mv(AG,y));center=2*dot(f,y)-dot(y,mv(Gmid,y));v=[a-b for a,b in zip(y,minimizer)]
   assert center+residual/mu==minimum+dot(v,mv(H,v))
   u=[1-y[0],-y[1],-y[2]];assert dot(u,mv(Fmid,u))+lam*dot(y,mv(Ymid,y))-residual/mu==Fmid[0][0]-(center+residual/mu)
  residual_poly=[O[n]-sum((least[i]*A[i][n] for i in range(3)),F(0)) for n in range(CUT+1)];assert all(v==0 for n,v in enumerate(residual_poly) if n%2!=base)
  proposal=[down(v) for v in residual_poly]
  proposal_error=up(sum((orig.mass(n)*(orig.H(n)+sh)*(v-proposal[n])**2 for n,v in enumerate(residual_poly)),F(0)))
  rows.append(dict(parity=r['parity'],source=r['source_inverse_response']['source'],response_trial_basis=r['response_trial_basis'],center_action_D_lower_Gram=p.ser(AG),center_source_action_pairings=list(map(str,rhs)),center_source_D_lower_energy=str(c),original_form_midpoint=p.ser(Fmid),frequency_Gram_midpoint=p.ser(Ymid),global_augmented_inverse_lower=str(mu),global_augmented_inverse_upper=str(nu),exact_center_least_residual_coefficients=list(map(str,least)),minimum_retained_center_D_lower_residual_energy=str(d2),center_action_smallest_singular_value_squared_lower=str(sigma2),complete_action_error_map_norm_squared_upper=str(delta2),source_action_error_D_energy_upper=str(source_error),uniform_actual_three_trial_residual_D_norm_lower=str(robust),uniform_actual_three_trial_residual_D_energy_lower=str(down(robust*robust)),exact_inverse_upper_formula_lower_envelope_quadratic_matrix=p.ser(H),exact_inverse_upper_formula_lower_envelope_linear_half=list(map(str,h)),exact_inverse_upper_formula_lower_envelope_minimizer=list(map(str,minimizer)),inverse_upper_formula_uniform_floor_lower=str(down(minimum)),same_formula_signed_gap_lower_bound_uniform_ceiling_upper=str(up(gapceiling)),actual_original_source_form_upper=r['original_trial_form_intervals'][0][0][1],coefficient_tuning_of_current_upper_formula_cannot_certify_positive_signed_gap=True,actual_inverse_response_lower_bound_inferred_from_formula_floor=False,actual_original_negative_direction_proved=False,residual_shaped_next_trial_proposal=[dict(degree=n,coefficient=str(v)) for n,v in enumerate(proposal)],proposed_residual_trial_rounding_D_energy_upper=str(proposal_error),proposed_residual_trial_complete_action_certified=False,preserved_inverse_response=r['source_inverse_response']))
 return dict(milestone='RC241',starting_commit='4bb28eccb6610bf8765b9382de9309abb2512b4a',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_response_source_count=2,response_trials_per_parity=3,no_new_actual_action_inputs=True,parity_tuning_obstruction_certificates=rows,exact_controls=controls(),uniform_all_real_and_complex_coefficients_covered=True,scope='RC240 fixed degree-64 centers and midpoint form interval upper envelope with unchanged global mu; no obstruction to other certification methods',actual_positive_distance_from_source_to_three_trial_N_action_range_certified=True,original_inverse_response_floor_claimed=False,original_negative_direction_claimed=False,previous_response_bounds_preserved=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC242: certify the proposed residual-shaped actions or a stronger complementary inverse estimate; scalar tuning in the fixed three-trial enclosure cannot close its signed gate')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC241 VALIDATED: uniform fixed-trial tuning obstruction; full signed gate open',flush=True)
