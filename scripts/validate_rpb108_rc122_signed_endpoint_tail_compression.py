"""RC122: signed endpoint-jet analytic tail replacement, uniformly over inputs.
No full endpoint iteration or original Weil response is computed.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,argparse
from validate_rpb108_rc119_reference_preconditioned_source_solver import log2_bounds
from validate_rpb108_rc114_positive_augmentation import up,down
from validate_rpb108_rc117_source_adapted_trial import legendre_source
from validate_rpb108_rc47_correlated_native_transport import root

def controls(replay=False):
 cases=0
 for N in range(1,9):
  lam=N*(N+1);a=[F((-1)**n*(n+1),7) for n in range(N+1) if n%2==N%2];ns=list(range(N%2,N+1,2));A=sum(map(abs,a),F(0))
  for m in range(2*N+2,2*N+12):
   z=m*(m+1);exact=sum((x/F(z-n*(n+1)) for n,x in zip(ns,a)),F(0))
   for K in [1,2,4,8]:
    moments=[sum((x*F(n*(n+1),lam)**k for n,x in zip(ns,a)),F(0)) for k in range(K)]
    terms=[moments[k]*F(lam,z)**k/z for k in range(K)];approx=sum(reversed(terms) if replay else terms,F(0));rem=sum((x*F(n*(n+1),z)**K/F(z-n*(n+1)) for n,x in zip(ns,a)),F(0))
    assert exact==approx+rem and abs(rem)<=A*F(lam,z)**K/F(z-lam)
    cases+=1
 # Exact telescoping weight and weighted Cauchy bound for signed analytic coefficients.
 for R in [8,19,47]:
  partial=sum((F(2*m+1,m*m*(m+1)**2) for m in range(R+1,R+301)),F(0))
  assert partial+F(1,(R+301)**2)==F(1,(R+1)**2)
  for q in [F(1,4),F(1,2)]:
   for t in [q/2,q]:
    for K in [1,4,9]:
     x=[F((-1)**k*(k+1),7) for k in range(K)]
     lhs=sum((x[k]*t**k for k in range(K)),F(0))**2
     rhs=sum((x[k]**2*q**k for k in range(K)),F(0))/(1-q)
     assert lhs<=rhs;cases+=1
 return cases

def gram_profile(N,M,K,B,slo,shi,replay=False):
 R=M+128;lam=N*(N+1);degree=2*K-2;H=sum((F(1,j) for j in range(1,M+1)),F(0));lo=[F(0)]*(degree+1);hi=[F(0)]*(degree+1);terms=[]
 for m in range(M+1,R+1):
  H+=F(1,m)
  if m%2!=N%2:continue
  z=m*(m+1);t=F(lam,z);bl=2*B*F(2*m+1)/(F(z*z)*(H+shi));bh=2*B*F(2*m+1)/(F(z*z)*(H+slo));power=F(1);row=[]
  for k in range(degree+1):row.append((down(bl*power,10**60),up(bh*power,10**60)));power*=t
  terms.append(row)
 if replay:terms.reverse()
 for row in terms:
  for k,(a,b) in enumerate(row):lo[k]+=a;hi[k]+=b
 lo=[down(x,10**50) for x in lo];hi=[up(x,10**50) for x in hi];err=up(F(K)*max((b-a)/2 for a,b in zip(lo,hi)),10**50)
 qt=F(lam,(R+1)*(R+2));mass=up(2*B/(slo*(R+1)**2),10**50);diag=[up(mass*qt**k/(1-qt),10**50) for k in range(K)]
 return dict(analytic_tail_rank=K,analytic_tail_start_after_degree=M,explicit_Gram_prefix_end_degree=R,positive_Gram_prefix_hankel_moment_lower=list(map(str,lo)),positive_Gram_prefix_hankel_moment_upper=list(map(str,hi)),prefix_center_operator_norm_enclosure_error_upper=str(err),unevaluated_Gram_tail_squared_weight_mass_upper=str(mass),unevaluated_Gram_tail_ratio_upper=str(qt),unevaluated_Gram_tail_diagonal_Loewner_upper=list(map(str,diag)),Gram_lower_recipe='Hankel midpoint minus prefix_error I',Gram_upper_recipe='Hankel midpoint plus prefix_error I plus tail_diagonal',Gram_inverse_or_conditioning_required=False,actual_constant_uncertainty_paid=True)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,old,prec=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in [prior,old,prec]]==['RC121','RC120','RC56'] and prior['input_sha256'][0]==hs[1] and prior['input_sha256'][3]==hs[2]
 B=F(11,10);slo=F(prior['diagonal_reference_floor_lower']);cl,ch=map(F,prec['actual_constant_enclosure']);ll,lh=log2_bounds(replay);gram_slo=F(789,125)+cl+ll;shi=F(789,125)+ch+lh;assert 0<slo<=gram_slo<shi
 checks=controls(replay);rows=[]
 for p,w in zip(prior['parity_diagonal_source_and_endpoint_action_certificates'],old['parity_reference_inverse_action_certificates']):
  assert p['parity']==w['parity'];N=p['input_source_degree'];box=p['finite_cutoff_endpoint_action_contracts'][0];M=box['output_degree_cutoff'];T=F(box['omitted_endpoint_preconditioned_action_D_energy_squared_factor_upper']);lam=N*(N+1);q=F(lam,(M+1)*(M+2));assert q<F(1,4)
  budgets=[]
  for digits in [6,12,24]:
   tau=F(1,10**digits);K=0
   while T*q**(2*K)>tau*tau:K+=1
   assert K>0 and T*q**(2*(K-1))>tau*tau
   budgets.append(dict(endpoint_action_D_norm_relative_tail_target=str(tau),analytic_tail_rank=K,uniform_residual_D_energy_squared_factor_upper=str(up(T*q**(2*K),10**(2*digits+12))),minimal_rank_for_inherited_uniform_enclosure=True,finite_output_cutoff=M,input_degree=N,full_input_space_covered=True))
  K=budgets[-1]['analytic_tail_rank'];profile=gram_profile(N,M,K,B,gram_slo,shi,replay)
  # Actual signed endpoint moments of the existing RC120 rational trial, all its degrees.
  ab=legendre_source(w['trial_Chebyshev_coefficients'],replay);mom=[]
  for k in range(K):
   terms=[(a*F(n*(n+1),lam)**k,b*F(n*(n+1),lam)**k) for n,(a,b) in enumerate(ab) if n%2==N%2]
   if replay:terms.reverse()
   lo=down(sum((a for a,b in terms),F(0)),10**70);hi=up(sum((b for a,b in terms),F(0)),10**70);mom.append(dict(order=k,normalized_signed_endpoint_moment_lower=str(lo),normalized_signed_endpoint_moment_upper=str(hi)))
  # Independent exact boundary evaluation of zeroth moment from stored Chebyshev centers.
  boundary=sum((F(x['physical_Chebyshev_coefficient_center']) for x in w['trial_Chebyshev_coefficients']),F(0));assert F(mom[0]['normalized_signed_endpoint_moment_lower'])<=boundary<=F(mom[0]['normalized_signed_endpoint_moment_upper'])
  mid=[(F(a)+F(b))/2 for a,b in zip(profile['positive_Gram_prefix_hankel_moment_lower'],profile['positive_Gram_prefix_hankel_moment_upper'])];moment_intervals=[(F(x['normalized_signed_endpoint_moment_lower']),F(x['normalized_signed_endpoint_moment_upper'])) for x in mom];norms=[max(a*a,b*b) for a,b in moment_intervals];quadhi=F(0)
  for i,(ai,bi) in enumerate(moment_intervals):
   for j,(aj,bj) in enumerate(moment_intervals):
    z=mid[i+j];values=[ai*aj,ai*bj,bi*aj,bi*bj];quadhi+=z*(max(values) if z>=0 else min(values))
  approx_upper=up(quadhi+F(profile['prefix_center_operator_norm_enclosure_error_upper'])*sum(norms,F(0))+sum((x*F(d) for x,d in zip(norms,profile['unevaluated_Gram_tail_diagonal_Loewner_upper'])),F(0)),10**40);assert approx_upper>0
  energy=F(w['reference_trial_P_energy_upper']);replacement_error2=T*q**(2*K)*energy;true_tail=up((root(approx_upper,10**90)+root(replacement_error2,10**90))**2,10**30);unsigned=T*energy;gain=down(unsigned/true_tail,10**6);assert gain>1
  rows.append(dict(parity=p['parity'],input_degree=N,finite_output_cutoff=M,expansion_ratio_upper=str(q),inherited_unsigned_squared_tail_factor_upper=str(T),rank_accuracy_certificates=budgets,analytic_tail_Gram_certificate=profile,tested_RC120_trial_signed_endpoint_moments=mom,tested_trial_endpoint_value_exact=str(boundary),trial_source_global_phase=w['source_global_phase'],zeroth_moment_independently_verified=True,tested_trial_analytic_tail_D_energy_squared_upper=str(approx_upper),tested_trial_full_omitted_endpoint_action_D_energy_squared_upper=str(true_tail),tested_trial_inherited_unsigned_tail_D_energy_squared_upper=str(unsigned),tested_trial_unsigned_to_signed_enclosure_improvement_factor_lower=str(gain),test_uses_entire_stored_trial_and_full_Gram_upper=True,full_retained_endpoint_output_evaluated=False))
 return dict(milestone='RC122',status='PASS: full-input signed endpoint-tail finite-rank replacement with correlated Gram bounds',input_sha256=hs,aperture='11/10',arithmetic='exact geometric kernel and telescoping controls; 700-digit input moments; rational Hankel Gram enclosures',exact_geometric_and_Gram_controls=checks,reference_metric='actual D energy with RC56 constant uncertainty paid',uniform_operator_tail_replacement_proved=True,correlated_full_source_map_residual_contract_proved=True,analytic_tail_Gram_inverse_required=False,finite_output_action_evaluated=False,analytic_tail_columns_closed_under_endpoint_iteration_proved=False,full_endpoint_iteration_performed=False,regular_multiplier_action_evaluated=False,canonical_Riesz_iteration_performed=False,original_Weil_or_augmented_actions_performed=False,auxiliary_response_norm_below_one_certified=False,new_positive_native_directions_certified=0,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,parity_signed_endpoint_tail_certificates=rows,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=3);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC122 PASS: uniform analytic endpoint-tail compression and signed Gram certificate; iterative closure open')
