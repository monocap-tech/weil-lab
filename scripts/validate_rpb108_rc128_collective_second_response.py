"""RC128: one collective finite/analytic approximation to C f0.
Residual source-family covariance paid; enlarged-family inverse remains open.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import (
 B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,finite,joint=map(json.loads,raw)
 hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [p['milestone'] for p in (prior,finite,joint)]==['RC127','RC126','RC124']
 assert prior['input_sha256']==hs[1:]
 pr=finite['parity_finite_response_variance_certificates'][0]
 jr=joint['parity_actual_joint_endpoint_moment_certificates'][0]
 M=989;L=4095;last=988;lam=last*(last+1);first=L+1;rho=F(lam,first*(first+1))
 assert pr['tail_cutoff']==jr['tail_cutoff']==M and F(58,1000)<rho<F(59,1000)
 sl=F(jr['Gamma_0_Loewner_lower'][0][0])/(2*B)
 sh=F(jr['Gamma_0_Loewner_upper'][0][0])/(2*B)
 s=(rat(sl)[0],rat(sh)[1])
 log=(rat(1-F(jr['endpoint_pairing_entry_upper'][0][0])/(2*B))[0],rat(1-F(jr['endpoint_pairing_entry_lower'][0][0])/(2*B))[1])
 harmonic=[Z]
 for n in range(1,2*L+1):harmonic.append(plus(harmonic[-1],rat(F(1,n))))
 dn={n:plus(harmonic[n],s) for n in range(0,L+1,2)}
 diagonal={n:minus(plus(minus(mul(rat(2),harmonic[2*n]),mul(rat(2),harmonic[n])),rat(F(1,2*n+1))),log) for n in range(0,L+1,2)}
 f={n:div(rat(F(2*n+1,n*(n+1))),dn[n]) for n in range(2,M,2)}
 jobs=list(f);jobs=jobs[::-1] if replay else jobs
 coeff=[];finiteError=F(0)
 for n in range(0,L+1,2):
  value=Z
  for m in jobs:
   entry=diagonal[n] if m==n else rat(F(2*n+1,abs(n-m)*(n+m+1)))
   value=plus(value,mul(entry,f[m]))
  lo,hi=bounds(div(value,dn[n]));center=down((lo+hi)/2);radius=max(center-lo,hi-center)
  finiteError+=up(2*B/F(2*n+1)*F(dn[n][1])*radius*radius,10**100)
  coeff.append(dict(degree=n,center=str(center),radius=str(radius)))
 assert finiteError<=F(prior['finite_action_trial_rounding_D_energy_upper'][2])
 # Actual signed tail coefficients are positive Stieltjes moments of f0.
 moments=[]
 for k in range(41):
  value=Z
  for m in jobs:value=plus(value,mul(f[m],rat(F(m*(m+1),lam)**k)))
  lo,hi=bounds(value);center=down((lo+hi)/2);radius=max(center-lo,hi-center)
  moments.append(dict(order=k,lower=str(lo),upper=str(hi),center=str(center),radius=str(radius)))
 assert all(F(moments[k]['lower'])>0 and F(moments[k+1]['upper'])<=F(moments[k]['upper']) for k in range(40))
 tail=up(B/(F(plus(harmonic[L-1],s)[0])*(L-2)*(L-1)))
 assert tail==F(prior['finite_output_leading_tail_D_energy_upper'])
 Gfl=F(prior['D_Gram_Loewner_lower'][2][2]);Gfu=F(prior['D_Gram_Loewner_upper'][2][2])
 Gpl=F(prior['D_Gram_Loewner_lower'][1][1]);Gpu=F(prior['D_Gram_Loewner_upper'][1][1])
 oldF=F(prior['projected_covariance_entry_lower'][2][2])
 psiVariance=F(prior['projected_covariance_entry_upper'][1][1]);assert psiVariance>0
 budgets=[]
 for digits in (6,12,24):
  target=F(1,10**digits);K=0
  while True:
   remainder=up(tail*(F(moments[K+1]['upper'])*rho**(K+1)/(1-rho))**2,10**100)
   rounding=up(tail*sum(F(moments[k]['radius'])*rho**k for k in range(K+1))**2,10**100)
   normError=up(sqrtup(finiteError)+sqrtup(rounding)+sqrtup(remainder))
   variance=up(normError*normError,10**100)
   if variance<=target*target*Gfl:break
   K+=1;assert K<40
  cross=sqrtup(psiVariance*variance)
  distanceLower=down((sqrtup(oldF)-F(1,10**40)-normError)**2)
  assert sqrtup(oldF)-F(1,10**40)>normError and distanceLower>0
  # Residual Gram Cauchy-Schwarz pays every mixture of the old input columns.
  t=target
  covarianceUpper=[[F(0)]*3,[F(0),(1+t)*psiVariance,F(0)],[F(0),F(0),(1+1/t)*variance]]
  assert psd(covarianceUpper)
  normalized=up(variance/Gfl,10**(2*digits+12))
  assert variance<oldF/1000
  budgets.append(dict(relative_Cf0_D_norm_target=str(target),retained_tail_highest_order=K,retained_tail_feature_count=K+1,added_collective_energy_vector_count=1,enriched_family_dimension=4,collective_response_distance_to_old_family_D_energy_lower=str(distanceLower),finite_polynomial_degree=L-1,analytic_moment_center_coefficients=[moments[k]['center'] for k in range(K+1)],omitted_analytic_output_D_energy_upper=str(remainder),retained_moment_rounding_D_energy_upper=str(rounding),full_Cf0_approximation_D_norm_error_upper=str(normError),new_f0_projected_covariance_upper=str(variance),new_f0_covariance_relative_own_D_Gram_upper=str(normalized),remaining_psi0_projected_covariance_upper=str(psiVariance),psi0_f0_mixed_covariance_absolute_upper=str(cross),old_three_input_projected_covariance_Loewner_upper=ser(covarianceUpper),old_f0_coordinate_lower_over_new_coordinate_upper=str(down(oldF/variance,10**6)),full_enlarged_four_vector_covariance_evaluated=False))
 # Exact rational scalar control of the signed moment expansion and remainder.
 control=[]
 for z in (first*(first+1),2*first*(first+1),10*first*(first+1)):
  weights={2:F(2,7),6:F(3,11),last:F(1,100000)}
  for K in (0,3,9):
   exact=sum(v/(1-F(m*(m+1),z)) for m,v in weights.items())
   mus=[sum(v*F(m*(m+1),lam)**k for m,v in weights.items()) for k in range(K+2)]
   partial=sum(mus[k]*F(lam,z)**k for k in range(K+1))
   bound=mus[K+1]*F(lam,z)**(K+1)/(1-F(lam,z))
   assert 0<exact-partial<=bound
   control.append(dict(z=z,order=K,positive_remainder_bound_verified=True))
 return dict(milestone='RC128',status='PASS: one collective second-response vector removes f0 covariance to prescribed single-action budgets',starting_commit='08bb3ae5a77142a6d1a70205c50b175a15a8db02',input_sha256=hs,aperture='11/10',source_family=['P_0','full infinite psi_0','exact symbolic f_0'],collective_response_definition='w_K=g_hat+sum_{k=0}^K mu_hat_k xi_k; xi_k(n)=(2n+1)*lambda^k/((H_n+s)*[n(n+1)]^(k+1)) on even n>4095',tail_lambda=str(lam),tail_geometric_ratio_upper=str(rho),old_cutoff_geometric_ratio=str(F(lam,990*991)),analytic_output_tail_D_Gram_upper=str(tail),finite_output_polynomial_coefficient_count=len(coeff),finite_output_polynomial_coefficient_sha256=hashlib.sha256(json.dumps(coeff,sort_keys=True,separators=(',',':')).encode()).hexdigest(),finite_output_polynomial_generator='directed equation (10) from RC127 for exact f0, even outputs 0..4094, rational 1e-40 centers',finite_output_polynomial_rounding_D_energy_upper=str(finiteError),positive_f0_tail_moment_intervals=moments,collective_response_enrichment_budgets=budgets,exact_rational_geometric_controls=control,exact_P0_projected_covariance_row_stays_zero=True,projection_family_includes_all_RC127_vectors=True,remaining_psi0_covariance_paid_by_projection_monotonicity=True,all_old_input_mixed_covariance_paid=True,full_four_vector_Gram_and_endpoint_pairing_evaluated=False,collective_response_vector_endpoint_action_evaluated=False,analytic_tail_covariance_small_certified=False,high_accuracy_reference_inverse_completed=False,regular_multiplier_action_evaluated=False,original_Weil_or_augmented_actions_performed=False,new_positive_native_directions_certified=0,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=3);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC128 PASS: collective Cf0 response and all old-input residual mixtures paid; enlarged-family action remains open')
