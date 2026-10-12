"""RC131: capture C g_hat inside C w14; analytic-source action remains paid.
One added collective vector; old four-input covariance only after enrichment.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import (
 B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,joint,response=map(json.loads,raw)
 hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in (prior,joint,response)]==['RC130','RC129','RC128']
 assert prior['input_sha256'][:2]==hs[1:] and joint['input_sha256'][0]==hs[2]
 Glo=[[F(x) for x in r] for r in joint['actual_D_Gram_entry_lower']]
 Ghi=[[F(x) for x in r] for r in joint['actual_D_Gram_entry_upper']]
 L=4095;O=8191;lam=(L-1)*L;rho=F(lam,(O+1)*(O+2))
 s=(rat(Glo[0][0]/(2*B))[0],rat(Ghi[0][0]/(2*B))[1])
 log=(rat(1-F(joint['actual_endpoint_pairing_entry_upper'][0][0])/(2*B))[0],rat(1-F(joint['actual_endpoint_pairing_entry_lower'][0][0])/(2*B))[1])
 harmonic=[Z]
 for n in range(1,2*O+1):harmonic.append(plus(harmonic[-1],rat(F(1,n))))
 dn={n:plus(harmonic[n],s) for n in range(0,O+1,2)}
 diag={n:minus(plus(minus(mul(rat(2),harmonic[2*n]),mul(rat(2),harmonic[n])),rat(F(1,2*n+1))),log) for n in range(0,O+1,2)}
 f={n:div(rat(F(2*n+1,n*(n+1))),dn[n]) for n in range(2,989,2)}
 jobs=list(f);jobs=jobs[::-1] if replay else jobs
 g={};gp=[]
 for n in range(0,L+1,2):
  value=Z
  for m in jobs:
   entry=diag[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
   value=plus(value,mul(entry,f[m]))
  lo,hi=bounds(div(value,dn[n]));center=down((lo+hi)/2);radius=max(center-lo,hi-center)
  g[n]=center;gp.append(dict(degree=n,center=str(center),radius=str(radius)))
 assert hashlib.sha256(json.dumps(gp,sort_keys=True,separators=(',',':')).encode()).hexdigest()==response['finite_output_polynomial_coefficient_sha256']
 assert min(g.values())>0
 # Complete finite-output polynomial of Cg, rounded with actual constant uncertainty paid.
 polynomial=[];polyError=F(0);jobs=list(g);jobs=jobs[::-1] if replay else jobs
 for n in range(0,O+1,2):
  value=Z
  for m in jobs:
   entry=diag[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
   value=plus(value,mul(entry,rat(g[m])))
  lo,hi=bounds(div(value,dn[n]));center=down((lo+hi)/2);radius=max(center-lo,hi-center)
  polynomial.append(dict(degree=n,center=str(center),radius=str(radius)))
  polyError+=up(2*B/F(2*n+1)*F(dn[n][1])*radius*radius,10**100)
 print('RC131 collective finite output complete',flush=True)
 # Positive finite Stieltjes moments give the exact infinite output after cutoff O.
 moments=[]
 for k in range(61):
  value=Z
  for m in jobs:value=plus(value,mul(rat(g[m]),rat(F(m*(m+1),lam)**k)))
  lo,hi=bounds(value);center=down((lo+hi)/2);radius=max(center-lo,hi-center)
  moments.append(dict(order=k,lower=str(lo),upper=str(hi),center=str(center),radius=str(radius)))
 assert min(F(x['lower']) for x in moments)>0
 T=up(B/(F(plus(harmonic[O-1],s)[0])*(O-2)*(O-1)))
 analyticInput=F(prior['input_w_tail_D_energy_upper'])
 oldWLower=F(prior['remaining_projected_covariance_entry_lower'][1][1])
 psiVar=F(prior['remaining_projected_covariance_entry_upper'][0][0]);fVar=F(prior['paid_f0_covariance_upper'])
 assert oldWLower>0 and analyticInput>0
 budgets=[]
 for digits in (6,12,24):
  target=F(1,10**digits);K=0
  while True:
   omitted=up(T*(F(moments[K+1]['upper'])*rho**(K+1)/(1-rho))**2,10**100)
   rounding=up(T*sum(F(moments[k]['radius'])*rho**k for k in range(K+1))**2,10**100)
   finiteNorm=up(sqrtup(polyError)+sqrtup(rounding)+sqrtup(omitted))
   if finiteNorm*finiteNorm<=target*target*Glo[3][3]:break
   K+=1;assert K<60
  wholeNorm=up(finiteNorm+sqrtup(analyticInput));wVar=up(wholeNorm*wholeNorm,10**100)
  distance= sqrtup(oldWLower)-F(1,10**40)-wholeNorm;assert distance>0
  residual=[F(0),psiVar,fVar,wVar]
  entryL=[[F(0)]*4 for _ in range(4)];entryU=[[F(0)]*4 for _ in range(4)]
  for i in range(1,4):
   entryU[i][i]=residual[i]
   for j in range(i+1,4):
    cross=sqrtup(residual[i]*residual[j]);entryL[i][j]=entryL[j][i]=-cross;entryU[i][j]=entryU[j][i]=cross
  fullUpper=[[3*residual[i] if i==j else F(0) for j in range(4)] for i in range(4)];assert psd(fullUpper)
  assert wVar<oldWLower/1000
  budgets.append(dict(finite_part_action_relative_w_source_D_norm_target=str(target),retained_tail_highest_order=K,retained_tail_feature_count=K+1,added_collective_vector_count=1,enriched_family_dimension=5,finite_output_polynomial_degree=O-1,analytic_moment_center_coefficients=[moments[k]['center'] for k in range(K+1)],finite_output_rounding_D_energy_upper=str(polyError),retained_analytic_moment_rounding_D_energy_upper=str(rounding),omitted_finite_source_output_D_energy_upper=str(omitted),full_Cg_approximation_D_norm_error_upper=str(finiteNorm),analytic_source_action_D_energy_upper=str(analyticInput),full_Cw_approximation_D_norm_error_upper=str(wholeNorm),new_w_projected_covariance_upper=str(wVar),new_w_covariance_relative_own_D_Gram_upper=str(up(wVar/Glo[3][3],10**15)),collective_vector_distance_to_old_four_family_D_energy_lower=str(down(distance*distance)),old_w_coordinate_lower_over_new_upper=str(down(oldWLower/wVar,10**6)),remaining_psi_projected_covariance_upper=str(psiVar),psi_w_mixed_covariance_absolute_upper=str(sqrtup(psiVar*wVar)),old_four_input_projected_covariance_entry_lower=ser(entryL),old_four_input_projected_covariance_entry_upper=ser(entryU),old_four_input_projected_covariance_Loewner_upper=ser(fullUpper),analytic_source_endpoint_action_evaluated=False,complete_five_vector_covariance_evaluated=False))
 # Exact shared leading analytic action: xi0=psi0-psi_prefix.
  # This does not claim that the finite balanced source action has been evaluated.
 oldBudget=response['collective_response_enrichment_budgets'][2]
 mu=list(map(F,oldBudget['analytic_moment_center_coefficients']));oldRho=F(response['tail_geometric_ratio_upper']);oldTail=F(joint['analytic_tail_base_D_energy_upper'])
 balanced=[];balancedPositive=True
 for n in range(0,L+1,2):
  value=rat(g[n])
  if n>=990:value=minus(value,mul(rat(mu[0]),div(rat(F(2*n+1,n*(n+1))),dn[n])))
  lo,hi=bounds(value);balancedPositive=balancedPositive and lo>0
  balanced.append(dict(degree=n,lower=str(lo),upper=str(hi)))
 assert balancedPositive
 higherAmplitude=up(sum(mu[k]*oldRho**k for k in range(1,15)))
 higherEnergy=up(oldTail*higherAmplitude*higherAmplitude,10**100)
 shared=dict(exact_action_identity='Cw14=mu0_hat*Cpsi0+C(g_hat-mu0_hat*psi_prefix)+C(sum_{k=1}^{14} mu_k_hat*xi_k)',leading_shared_Cpsi0_coefficient=str(mu[0]),finite_balanced_source_support='even degrees 0..4094',finite_balanced_source_coefficients_positive_certified=balancedPositive,finite_balanced_source_coefficient_interval_sha256=hashlib.sha256(json.dumps(balanced,sort_keys=True,separators=(',',':')).encode()).hexdigest(),higher_analytic_source_action_D_energy_upper=str(higherEnergy),higher_analytic_source_action_D_norm_upper=str(sqrtup(higherEnergy)),finite_balanced_source_action_evaluated=False,shared_leading_response_is_existing_Cpsi0_not_a_new_independent_analytic_action=True)
 # Controls include zero-degree mass, retained orders and the true worst denominator.
 controls=[]
 for z in ((O+1)*(O+2),2*(O+1)*(O+2)):
  weights={0:F(3,7),2:F(1,11),L-1:F(1,100000)}
  for K in (0,4,12):
   exact=sum(v/(1-F(m*(m+1),z)) for m,v in weights.items())
   mus=[sum(v*F(m*(m+1),lam)**k for m,v in weights.items()) for k in range(K+2)]
   prefix=sum(mus[k]*F(lam,z)**k for k in range(K+1))
   bound=mus[K+1]*F(lam,z)**(K+1)/(1-F(lam,z))
   assert 0<exact-prefix<=bound
   controls.append(dict(z=z,order=K,zero_degree_and_positive_geometric_remainder_verified=True))
 return dict(milestone='RC131',status='PASS: finite-part collective capture removes dominant w14 residual; complete analytic-source action remains paid',starting_commit='c3bf608700e4be85f67fc2bee1de5c46982738e3',input_sha256=hs,aperture='11/10',old_family=['P_0','psi_0','f_0','w_14'],source_split='w14=g_hat+a, a exact analytic tail above even degree 4094',new_collective_vector_definition='v_K=p_hat+sum_{k=0}^K nu_hat_k eta_k, eta_k(n)=(2n+1)*Lambda^k/((H_n+s)*[n(n+1)]^(k+1)) on even n>=8192',finite_source_degree=L-1,finite_output_degree=O-1,tail_Lambda=str(lam),tail_geometric_ratio_upper=str(rho),leading_new_output_tail_D_energy_upper=str(T),finite_output_polynomial_coefficient_count=len(polynomial),finite_output_polynomial_center_radius_sha256=hashlib.sha256(json.dumps(polynomial,sort_keys=True,separators=(',',':')).encode()).hexdigest(),finite_output_polynomial_generator='actual positive Cg_hat coefficient formula, even outputs 0..8190, 1e-40 rational centers',positive_finite_source_moment_intervals=moments,collective_capture_budgets=budgets,shared_leading_analytic_response_relation=shared,exact_rational_geometric_controls=controls,selected_next_joint_family_finite_source_target='1/1000000000000',complete_analytic_source_action_paid_by_contraction=True,analytic_source_action_assigned_zero=False,analytic_source_action_covariance_lower_certified=False,old_input_full_mixed_covariance_paid=True,new_vector_independence_certified=True,full_five_vector_Gram_and_endpoint_pairing_evaluated=False,complete_five_input_covariance_evaluated=False,RC130_reference_response_interval_inherited_unchanged=True,new_reference_response_interval_certified=False,high_accuracy_reference_inverse_completed=False,regular_multiplier_action_evaluated=False,original_Weil_or_augmented_actions_performed=False,new_positive_native_directions_certified=0,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=3);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC131 PASS: collective finite-source response and full old-input residual mixtures paid; analytic action remains open')
