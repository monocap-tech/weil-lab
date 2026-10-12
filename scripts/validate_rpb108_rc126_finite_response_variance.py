"""RC126: actual finite-column endpoint variance and response enrichment.
Other variance entries and original Weil responses remain unevaluated.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc119_reference_preconditioned_source_solver import log2_bounds
from validate_rpb108_rc114_positive_augmentation import up,down
from validate_rpb108_rc47_correlated_native_transport import root,matrix

def finite_response(p,M,B,sl,sh,replay=False):
 H=F(0);coreL=coreU=err=F(0);data=[]
 for n in range(1,M+1):
  H+=F(1,n)
  if n<=p or n%2!=p:continue
  z=n*(n+1)-p*(p+1);lo=F(2*n+1)/(z*(H+sh));hi=F(2*n+1)/(z*(H+sl));mid=down((lo+hi)/2,10**50);rad=max(abs(mid-lo),abs(mid-hi));mass=2*B/F(2*n+1)
  data.append(dict(degree=n,center=str(mid),radius=str(up(rad,10**60))))
  coreL+=down(2*B*F(2*n+1)/(z*z*(H+sh)),10**50);coreU+=up(2*B*F(2*n+1)/(z*z*(H+sl)),10**50);err+=up(mass*(H+sh)*rad*rad,10**100)
 if replay:
  # Independent prefix norm sum of directed coefficient intervals.
  altL=altU=F(0);Htable=[F(0)]
  for n in range(1,M+1):Htable.append(Htable[-1]+F(1,n))
  for x in reversed(data):
   n=x['degree'];z=n*(n+1)-p*(p+1)
   altL+=down(2*B*F(2*n+1)/(z*z*(Htable[n]+sh)),10**50);altU+=up(2*B*F(2*n+1)/(z*z*(Htable[n]+sl)),10**50)
  assert altL==coreL and altU==coreU
 return data,coreL,coreU,err

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,joint,tail,prec=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in [prior,joint,tail,prec]]==['RC125','RC124','RC122','RC56'] and prior['input_sha256'][0]==hs[1] and joint['input_sha256'][1]==hs[2] and joint['input_sha256'][3]==hs[3]
 B=F(11,10);ll,lh=log2_bounds(replay);cl,ch=map(F,prec['actual_constant_enclosure']);sl=F(789,125)+cl+ll;sh=F(789,125)+ch+lh;rows=[]
 for p,row in enumerate(joint['parity_actual_joint_endpoint_moment_certificates']):
  assert row['parity']==['even','odd'][p];M=row['tail_cutoff'];tailrow=next(x for x in tail['parity_signed_endpoint_tail_certificates'] if x['parity']==row['parity']);assert tailrow['finite_output_cutoff']==M;N=tailrow['input_degree'];lam=N*(N+1)
  data,low,high,err=finite_response(p,M,B,sl,sh,replay);GL=matrix(row['Gamma_0_Loewner_lower']);GU=matrix(row['Gamma_0_Loewner_upper']);first=M+1
  if first%2!=p:first+=1
  ratio=F(p*(p+1),first*(first+1));tailvar=GU[1][1]*(ratio/(1-ratio))**2;Rlow=low;Rhi=high+tailvar
  relL=down(Rlow/GU[0][0],10**12);relU=up(Rhi/GL[0][0],10**12);assert relL>F(1,1000)
  budgets=[]
  for digits in [6,12,24]:
   target=F(1,10**digits);K=0
   while (err+GU[1][1]*ratio**(2*(K+1))/(1-ratio)**2)/GL[0][0]>target*target:K+=1;assert K<=10
   residual=err+GU[1][1]*ratio**(2*(K+1))/(1-ratio)**2
   budgets.append(dict(relative_C_response_D_norm_target=str(target),additional_existing_tail_columns_required=K,analytic_tail_correction_coefficients=[str(F(p*(p+1),lam)**k) for k in range(1,K+1)],post_enrichment_finite_column_variance_relative_source_D_Gram_upper=str(up(residual/GL[0][0],10**(2*digits+15))),constant_and_finite_response_rounding_error_paid=True,complete_enriched_variance_matrix_computed=False))
  payload=json.dumps(data,sort_keys=True,separators=(',',':')).encode()
  rows.append(dict(parity=row['parity'],finite_input_degree=p,tail_cutoff=M,finite_response_polynomial_degree=data[-1]['degree'],finite_response_coefficient_count=len(data),finite_response_Legendre_coefficient_intervals=data,finite_response_coefficient_interval_sha256=hashlib.sha256(payload).hexdigest(),finite_response_generator='finite_response(p,M,11/10,s_lower,s_upper)',finite_response_center_rounding_grid='1e-50',finite_response_D_energy_squared_lower=str(low),finite_response_D_energy_squared_upper=str(high),finite_response_center_D_error_squared_upper=str(err),actual_finite_column_variance_lower=str(Rlow),actual_finite_column_variance_upper=str(Rhi),actual_finite_column_variance_over_source_D_Gram_lower=str(relL),actual_finite_column_variance_over_source_D_Gram_upper=str(relU),exact_even_variance_identity_proved=p==0,odd_residual_tail_variance_upper=str(tailvar),whole_two_column_small_variance_target_below_lower_bound_impossible=True,variance_coordinate_bound_is_not_full_Loewner_diagonal_lower=True,finite_response_enrichment_budgets=budgets,remaining_analytic_tail_variance_unbounded_by_this_certificate=True))
 return dict(milestone='RC126',status='PASS: actual finite-source variance quantified; one response polynomial removes its core covariance',input_sha256=hs,aperture='11/10',arithmetic='exact rational finite harmonic sums, physical coefficient intervals and geometric analytic-tail corrections',parity_finite_response_variance_certificates=rows,actual_finite_column_endpoint_second_moment_variance_evaluated=True,full_actual_variance_matrix_evaluated=False,response_enrichment_is_polynomial_combination_not_new_positive_native_direction=True,exact_symbolic_response_enrichment_closes_even_finite_column=True,rounded_polynomial_enrichment_exact_invariance_claimed=False,analytic_tail_column_response_still_open=True,high_accuracy_reference_response_completed=False,regular_multiplier_action_evaluated=False,original_Weil_or_augmented_actions_performed=False,auxiliary_response_norm_below_one_certified=False,new_positive_native_directions_certified=0,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=4);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC126 PASS: actual finite-column covariance obstruction and paid response enrichment; tail response remains open')
