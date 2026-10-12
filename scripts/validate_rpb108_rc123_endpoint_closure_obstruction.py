"""RC123: actual analytic-tail nonclosure and positive response moment criterion.
No endpoint action on infinite columns or original Weil response is evaluated.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc119_reference_preconditioned_source_solver import log2_bounds
from validate_rpb108_rc114_positive_augmentation import up,down
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale

def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def gram(X,D):return mm(tr(X),mm(D,X))

def abstract_controls(replay=False):
 D=[[F(2),F(1,4)],[F(1,4),F(1)]];K=[[F(11,10),F(11,40)],[F(11,40),F(2,5)]];assert psd(K) and psd(add(D,K,-1))
 C=mm(inverse(D),K);assert mm(D,C)==K and C!=tr(C);T=add(eye(2),C,-1);X=[[F(1),F(2)],[F(0),F(-1)]];G0=gram(X,D);S=mm(tr(X),mm(D,mm(inverse(add(eye(2),C)),X)));power=eye(2);partial=[[F(0)]*2 for _ in range(2)];mom=[]
 for j in range(17):
  Gj=mm(tr(X),mm(D,mm(power,X)));assert psd(Gj);mom.append(Gj);partial=add(partial,scale(Gj,F(1,2**(j+1))));tail=add(S,partial,-1);assert psd(tail) and psd(add(scale(G0,F(1,2**(j+1))),tail,-1));power=mm(power,T);Gn=mm(tr(X),mm(D,mm(power,X)));assert psd(add(tail,scale(Gn,F(1,2**(j+2))),-1)) and psd(add(scale(Gn,F(1,2**(j+1))),tail,-1))
 alt=[[F(0)]*2 for _ in range(2)]
 for j in reversed(range(17)):alt=add(alt,scale(mom[j],F(1,2**(j+1))))
 assert alt==partial
 # Noncommutative positive moment finite differences are PSD for a single contraction.
 for j in range(8):
  assert psd(add(mom[j],mom[j+1],-1)) and psd(add(add(mom[j],scale(mom[j+1],-2)),mom[j+2]))
 # Same G0, two permitted abstract contractions give different inverse responses.
 Szero=G0;Sone=scale(G0,F(1,2));assert Szero!=Sone and psd(add(Szero,Sone,-1))
 return dict(scope='abstract rational contractions, not the original endpoint action or Weil operator',physical_coordinate_metric_nonidentity=True,operator_selfadjoint_in_D_not_Euclidean=True,positive_moment_response_remainder_sandwich_checks=17,moment_monotonicity_and_second_difference_checks=8,response_from_Gram_only_not_determined_control_verified=True,reversed_exact_moment_sum_verified=True)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,metric,prec=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in [prior,metric,prec]]==['RC122','RC121','RC56'] and prior['input_sha256'][0]==hs[1] and prior['input_sha256'][2]==hs[2]
 ll,lh=log2_bounds(replay);cl,ch=map(F,prec['actual_constant_enclosure']);shi=F(789,125)+ch+lh;assert shi>0;rows=[]
 for p in prior['parity_signed_endpoint_tail_certificates']:
  M=p['finite_output_cutoff'];j0=1
  while 2**j0<=M:j0+=1
  targets=[]
  for target in [F(1),F(2),F(3)]:
   J=j0-1;lower=F(0)
   while lower<=target:
    J+=1;lower+=down(F(1)/(2*(shi+1+(J+1)*lh)),10**30)
   assert lower>target
   targets.append(dict(coefficient_ratio_growth_threshold=str(target),complete_dyadic_input_blocks_from=j0,complete_dyadic_input_blocks_through=J,output_degree_at_least_power_of_two_exponent=J+2,output_degree_parity=p['parity'],actual_C_psi0_to_psi0_coefficient_ratio_lower=str(down(lower,10**20)),huge_output_degree_not_numerically_evaluated=True))
  rows.append(dict(parity=p['parity'],analytic_tail_start_after_degree=M,first_positive_dyadic_block_exponent=j0,quantitative_ratio_growth_certificates=targets,all_positive_input_tail_coefficients_retained_in_proof=True,C_psi0_coefficient_ratio_diverges=True,any_fixed_polynomial_plus_finite_existing_psi_span_exact_closure_impossible=True,arbitrary_accuracy_approximation_impossibility_claimed=False))
 budgets=[]
 for digits in [6,12,24]:
  eta=F(1,10**digits);n=0
  while F(1,2**(n+1))>eta/3:n+=1
  eps=F(1,2**(n+1));delta=eta/3;weight=1-eps;assert 2*weight*delta+eps<=eta and F(1,2**n)>eta/3
  budgets.append(dict(relative_response_Loewner_width_target=str(eta),highest_required_positive_moment_degree=n,number_of_moments=n+1,positive_series_remainder_factor=str(eps),per_moment_center_error_relative_initial_Gram_allowance=str(delta),weighted_center_error_factor_upper=str(weight*delta),complete_sandwich_width_factor_upper=str(2*weight*delta+eps),minimal_degree_for_one_third_tail_allocation=True,actual_endpoint_moments_evaluated=False))
 return dict(milestone='RC123',status='PASS: actual finite analytic-tail nonclosure obstruction and finite positive-moment response stopping rule',input_sha256=hs,aperture='11/10',arithmetic='exact dyadic harmonic-growth and noncommuting positive response controls',endpoint_operator='C=D^(-1) h, positive contraction in actual D energy',parity_analytic_tail_nonclosure_certificates=rows,positive_response_operator='(I+C)^(-1) = (1/2) sum_j ((I-C)/2)^j',positive_response_moments='Gamma_j=V^* D (I-C)^j V for a specified joint source/analytic-tail family V',response_remainder_Loewner_bound='0 <= Sigma-S_n <= 2^(-n-1) Gamma_0',sharper_correlated_response_remainder_bound='2^(-n-2) Gamma_(n+1) <= Sigma-S_n <= 2^(-n-1) Gamma_(n+1)',conditional_positive_moment_certificates=budgets,abstract_noncommuting_controls=abstract_controls(replay),actual_nonclosure_of_any_fixed_finite_existing_tail_basis_proved=True,positive_moment_conditional_stopping_rule_proved=True,initial_Gram_alone_identifies_exact_response_claimed=False,minimal_next_endpoint_correlation='V^* h V, equivalently Gamma_1=Gamma_0-V^*hV, including signed cross pairings',actual_infinite_tail_endpoint_action_evaluated=False,actual_endpoint_response_moments_evaluated=False,regular_multiplier_action_evaluated=False,canonical_Riesz_iteration_performed=False,original_Weil_or_augmented_actions_performed=False,auxiliary_response_norm_below_one_certified=False,new_positive_native_directions_certified=0,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=3);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC123 PASS: finite-tail nonclosure proved; correlated positive moment response criterion; arithmetic moments open')
