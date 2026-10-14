"""RC255: weighted canonical inverse comparison with orthogonal model outputs."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import validate_rpb108_rc254_projected_residual_gate_audit as parent
direct=parent.direct;orig=parent.orig;p=parent.p;B=parent.B
up=parent.up;down=parent.down;root=parent.root;rootdown=parent.rootdown
ROOT=Path(__file__).resolve().parents[1];RHO=F(252,257);SHIFT=F(789,125)
PINS=dict(parent.PINS);HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc254_projected_residual_gate_audit.json':'b8bd7bec56d2295e66e8da081056ee04ccbb0acc','notes/RPB108_RC254_PROJECTED_RESIDUAL_GATE_AUDIT_20261014.md':'4baa11c8a63b8a9c312489c6850f99558a307129'})
HELPER_PINS['scripts/validate_rpb108_rc254_projected_residual_gate_audit.py']='7b26e807b89ff2d504ee6fa1b6b1b2543cacf20b'
def controls():
 # Inverse order uses congruence in the actual metric, without commutation.
 D=[[F(2),F(0)],[F(0),F(3)]];L=[[F(2),F(1,5)],[F(1,5),F(3)]];I=[[F(1),F(0)],[F(0),F(1)]];eta=F(1,3)
 assert p.psd(p.add(L,I,-1)) and p.psd(p.add(L,p.add(D,I,-1),-1))
 theta=F(3,4);W=p.add(p.scale(theta,I),p.scale(1-theta,p.add(D,I,-1)));assert p.psd(p.add(L,W,-1))
 G=p.add(p.scale(eta,L),[[F(1),F(2,5)],[F(2,5),F(1,2)]]);M=p.mm(p.inv(D),L);N=p.mm(p.inv(D),G);assert p.mm(M,N)!=p.mm(N,M)
 Ni=p.mm(D,p.mm(p.inv(G),D));Mi=p.mm(D,p.mm(p.inv(L),D));Wi=p.mm(D,p.mm(p.inv(W),D))
 assert p.psd(p.add(p.scale(1/eta,Mi),Ni,-1)) and p.psd(p.add(Wi,Mi,-1))
 # Retained and omitted model output are orthogonal in every diagonal weight.
 w=[F(2),F(3),F(5)];head=[F(1,7),F(-2,11),F(0)];tail=[F(0),F(0),F(3,13)]
 norm=lambda v:sum((a*x*x for a,x in zip(w,v)),F(0))
 assert norm([a+b for a,b in zip(head,tail)])==norm(head)+norm(tail)
 return dict(nonidentity_metric_noncommuting_inverse_order=True,canonical_comparison_not_operator_identification=True,orthogonal_model_output_energy_before_global_faults=True)
def weighted_candidate(theta,coefficients,harmonics,sl,sh,first,eta,finite,tail,globalfault,reverse):
 A=1-theta;C=theta/RHO-A*SHIFT;beta=min(A,A+C/sl);assert A>0 and beta>0
 betat=min(A,A+C/(harmonics[first]+sl));assert betat>0
 terms=[]
 for n,c in enumerate(coefficients):
  ds=[harmonics[n]+sl,harmonics[n]+sh];assert all(A*d+C>0 for d in ds)
  # d^2/(A*d+C) is convex: its second derivative is 2*C^2/(A*d+C)^3.
  terms.append(up(orig.mass(n)*max(d*d/(A*d+C) for d in ds)*c*c))
 if reverse:terms.reverse()
 center=up(sum(terms,F(0)));rounding=up(finite/beta);model=up((root(center)+root(rounding))**2+tail/betat);fault=root(up(globalfault*globalfault/beta));bound=up((root(model)+fault)**2/eta)
 return dict(theta=str(theta),diagonal_D_coefficient=str(A),diagonal_physical_constant=str(C),global_relative_metric_floor=str(beta),omitted_output_relative_metric_floor=str(betat),retained_center_weighted_energy_upper=str(center),finite_rounding_weighted_energy_upper=str(rounding),complete_model_weighted_energy_upper=str(model),global_model_fault_weighted_norm_upper=str(fault),actual_residual_augmented_inverse_correction_upper=str(bound))
def run(reverse=False):
 data={}
 for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
  b=(ROOT/path).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha,(path,'pin');data[path]=json.loads(b) if path.endswith('.json') else b.decode()
 get=lambda s:data['certificates/rpb108_rc'+s+'.json']
 assert F(get('230_augmentation_range_bridge')['canonical_embedding_squared_norm_upper'])==RHO
 metric_control=get('121_diagonal_metric_equivalence');assert metric_control['whole_supported_canonical_form_domain_covered'] and F(metric_control['actual_canonical_diagonal_metric_upper'])==2
 prior=get('254_projected_residual_gate_audit');centers=get('251_extended_coupled_residual');tails=get('253_prime_boundary_tail');bounds=get('232_augmented_polynomial_action');forms=get('247_materialized_four_trial_response');metric=get('129_four_vector_joint_moment')
 sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(metric['actual_D_Gram_entry_upper'][0][0])/(2*B);harmonics=[F(0)]
 for n in range(1,259):harmonics.append(harmonics[-1]+F(1,n))
 rows=[]
 for parity,r in enumerate(prior['projected_residual_gate_audit_certificates']):
  c=centers['extended_coupled_residual_response_certificates'][parity];t=tails['prime_boundary_tail_response_certificates'][parity];b=bounds['polynomial_augmented_action_certificates'][parity];eta=F(b['fresh_canonical_H_lower']);mu=F(b['fresh_augmented_N_D_lower']);nu=F(b['fresh_augmented_N_D_upper']);lam=F(b['augmentation_coefficient'])
  assert c['selected_trial_coefficients']==t['selected_trial_coefficients']==r['selected_trial_coefficients']
  finite=F(c['residual_finite_rounding_D_energy_upper']);globalfault=up(F(c['unchanged_original_model_fault_D_norm_upper'])+root(F(c['unchanged_rational_augmentation_comparison_D_error_squared_upper'])));tail=up((root(F(t['accepted_original_D_energy_beyond_256_upper']))+root(F(c['augmentation_D_omitted_output_energy_upper'])))**2)
  nh=F(r['retained_model_center_D_energy_upper']);model=up((root(nh)+root(finite))**2+tail);rh=min(F(r['complete_direct_residual_actual_D_energy_upper']),up((root(model)+globalfault)**2));rl=F(r['complete_direct_residual_actual_D_energy_lower']);assert rl<=rh
  coeff=list(F(row['coefficient']) for row in c['extended_complete_direct_residual_center']);first=257 if parity else 258
  weights=[F(k,1000) for k in range(715,951)];weights=weights[::-1] if reverse else weights
  proposals=[weighted_candidate(theta,coeff,harmonics,sl,sh,first,eta,finite,tail,globalfault,reverse) for theta in weights]
  selected=min(proposals,key=lambda row:(F(row['actual_residual_augmented_inverse_correction_upper']),F(row['theta'])));canonical=F(selected['actual_residual_augmented_inverse_correction_upper']);coarse=up(rh/mu);correction=min(canonical,coarse)
  pr=forms['parity_materialized_four_trial_response_certificates'][parity];F0=[[(F(a),F(b)) for a,b in row] for row in pr['original_trial_form_intervals']];Gy=[[(F(a),F(b)) for a,b in row] for row in pr['frequency_trial_Gram_intervals']];y=list(map(F,r['selected_trial_coefficients']));cl,ch=direct.center_intervals(F0,Gy,y,lam)
  tl=down(cl+rl/nu);th=up(ch+correction);u=[1-y[0],-y[1],-y[2],-y[3]];ql,qh=direct.quadratic(F0,u);al,ah=direct.quadratic(Gy,y);dl=down(ql+lam*al-correction);dh=up(qh+lam*ah-rl/nu)
  actualtl=max(F(r['actual_original_action_inverse_response_lower']),tl);actualth=min(F(r['actual_original_action_inverse_response_upper']),th);actualdl=max(F(r['actual_signed_gap_lower']),dl,down(F0[0][0][0]-actualth));actualdh=min(F(r['actual_signed_gap_upper']),dh,up(F0[0][0][1]-actualtl));assert actualtl<=actualth and actualdl<=actualdh
  # M<=2I implies M^-1>=I/2. Any upper certificate obtained purely
  # from eta^-1 M^-1 must therefore be >= this formula floor for fixed Z.
  canonical_floor=down(cl+rl/(2*eta));canonical_ceiling=up(F0[0][0][1]-canonical_floor)
  rows.append(dict(parity=r['parity'],source=r['source'],selected_trial_coefficients=r['selected_trial_coefficients'],retained_residual_center_origin='RC251 degree 256',canonical_Hhat_floor=str(eta),canonical_metric_D_upper='2',canonical_embedding_squared_norm_upper=str(RHO),canonical_metric_lower_forms=['L >= rho^-1 I_physical','L >= D-r I_physical; h and R are positive'],weighted_diagonal_form='W_theta=(1-theta)D+[theta/rho-(1-theta)r]I_physical',inverse_order='N^-1 <= eta^-1 M^-1 <= eta^-1 (D^-1 W_theta)^-1 in D energy',model_finite_rounding_D_energy_upper=str(finite),complete_model_omitted_D_energy_upper=str(tail),complete_global_model_fault_D_norm_upper=str(globalfault),complete_model_D_energy_upper=str(model),previous_complete_actual_residual_D_energy_upper=r['complete_direct_residual_actual_D_energy_upper'],complete_actual_residual_D_energy_upper=str(rh),complete_actual_residual_D_energy_lower=str(rl),model_retained_and_omitted_output_orthogonal=True,global_model_faults_combined_in_norm=True,finite_weight_search=dict(first='143/200',last='19/20',step='1/1000',candidate_count=236,continuous_optimality_claimed=False),selected_weighted_inverse_certificate=selected,orthogonal_energy_global_mu_inverse_correction_upper=str(coarse),canonical_weighted_inverse_correction_upper=str(canonical),accepted_actual_inverse_correction_upper=str(correction),direct_inverse_response_lower=str(tl),direct_inverse_response_upper=str(th),direct_signed_gap_lower=str(dl),direct_signed_gap_upper=str(dh),actual_original_action_inverse_response_lower=str(actualtl),actual_original_action_inverse_response_upper=str(actualth),previous_original_action_inverse_response_upper=r['actual_original_action_inverse_response_upper'],actual_signed_gap_lower=str(actualdl),actual_signed_gap_upper=str(actualdh),original_action_inverse_upper_improved=actualth<F(r['actual_original_action_inverse_response_upper']),pure_canonical_comparison_fixed_trial_audit=dict(inverse_UPPER_formula_floor=str(canonical_floor),signed_gap_LOWER_formula_ceiling=str(canonical_ceiling),pure_eta_M_inverse_comparison_cannot_close_this_source=canonical_floor>=F0[0][0][1],eta_and_selected_Z_fixed=True,true_N_inverse_lower_bound_claimed=False),signed_gap_positive_certified=actualdl>0,actual_negative_gap_proved=actualdh<0))
 return dict(milestone='RC255',starting_commit='6b615e60439ee3c03a7277e0bc9f0a675bae3f00',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_response_source_count=2,response_trials_per_parity=4,weighted_canonical_inverse_response_certificates=rows,source_and_trial_spaces_unchanged=True,retained_direct_residual_output_degree_unchanged=256,all_original_and_rational_augmentation_model_faults_preserved=True,exact_controls=controls(),new_response_enclosures_intersected_with_RC254=True,canonical_metric_not_identified_with_augmented_operator=True,full_639_signed_response_matrix_evaluated=False,full_signed_gap_positive_certified=False,original_full_auxiliary_norm_below_one_certified=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC256: obtain N-specific residual inverse control or change the actual response trial; the fixed odd source cannot close using only eta^-1 M^-1 domination')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');a=ap.parse_args();c=run(a.replay)
 if a.replay:assert c==json.loads(a.output.read_text())
 else:a.output.write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC255 VALIDATED: weighted inverse comparison and orthogonal model upper bounds; Stage I open',flush=True)
