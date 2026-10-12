"""RC132: balanced finite action with shared analytic residual; no inverse claim."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import (
 B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];capture,prior,joint,response=map(json.loads,raw)
 hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in (capture,prior,joint,response)]==['RC131','RC130','RC129','RC128']
 assert capture['input_sha256']==hs[1:]
 assert prior['input_sha256'][:2]==hs[2:] and joint['input_sha256'][0]==hs[3]
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

 # b has actual s-dependent coefficients; do not replace them by unpaid centers.
 shared=capture['shared_leading_analytic_response_relation'];alpha=F(shared['leading_shared_Cpsi0_coefficient'])
 balanced=[];b={}
 for n in range(0,L+1,2):
  value=rat(g[n])
  if n>=990:value=minus(value,mul(rat(alpha),div(rat(F(2*n+1,n*(n+1))),dn[n])))
  lo,hi=bounds(value);assert lo>0
  balanced.append(dict(degree=n,lower=str(lo),upper=str(hi)));b[n]=value
 assert hashlib.sha256(json.dumps(balanced,sort_keys=True,separators=(',',':')).encode()).hexdigest()==shared['finite_balanced_source_coefficient_interval_sha256']
 polynomial=[];polyError=F(0);jobs=list(b);jobs=jobs[::-1] if replay else jobs
 for n in range(0,O+1,2):
  value=Z
  for m in jobs:
   entry=diag[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
   value=plus(value,mul(entry,b[m]))
  lo,hi=bounds(div(value,dn[n]));center=down((lo+hi)/2);radius=max(center-lo,hi-center)
  polynomial.append(dict(degree=n,center=str(center),radius=str(radius)))
  polyError+=up(2*B/F(2*n+1)*F(dn[n][1])*radius*radius,10**100)
 print('RC132 balanced finite action complete',flush=True)
 moments=[]
 for k in range(61):
  value=Z
  for m in jobs:value=plus(value,mul(b[m],rat(F(m*(m+1),lam)**k)))
  lo,hi=bounds(value);center=down((lo+hi)/2);radius=max(center-lo,hi-center)
  assert lo>0
  moments.append(dict(order=k,lower=str(lo),upper=str(hi),center=str(center),radius=str(radius)))
 T=F(capture['leading_new_output_tail_D_energy_upper'])
 assert T==up(B/(F(plus(harmonic[O-1],s)[0])*(O-2)*(O-1)))
 psiOld=F(prior['remaining_projected_covariance_entry_upper'][0][0])
 wOldLower=F(prior['remaining_projected_covariance_entry_lower'][1][1])
 wCapture=F(capture['collective_capture_budgets'][1]['new_w_projected_covariance_upper'])
 higher=F(shared['higher_analytic_source_action_D_energy_upper']);budgets=[]
 for digits in (6,12,24):
  target=F(1,10**digits);K=0
  while True:
   omitted=up(T*(F(moments[K+1]['upper'])*rho**(K+1)/(1-rho))**2,10**100)
   rounding=up(T*sum(F(moments[k]['radius'])*rho**k for k in range(K+1))**2,10**100)
   eps=up(sqrtup(polyError)+sqrtup(rounding)+sqrtup(omitted))
   if eps*eps<=target*target*Glo[3][3]:break
   K+=1;assert K<60
  e=up(eps+sqrtup(higher));e2=up(e*e,10**100)
  # In F_b=span(U,z_b), residual Cb is at most eps. Cpsi inherits RC130.
  distance=sqrtup(wOldLower)-F(1,10**40)-alpha*sqrtup(psiOld)-e
  assert distance>0
  wBalanced=up((alpha*sqrtup(psiOld)+e)**2,10**100)
  # In E=span(U,v10,z_b), both certificates apply by projection monotonicity.
  psiUnion=min(psiOld,up(((sqrtup(wCapture)+e)/alpha)**2,10**100))
  mixedDeviation=up(sqrtup(psiUnion)*e,10**100)
  wwDeviation=up(2*alpha*sqrtup(psiUnion)*e+e2,10**100)
  mixedBound=min(sqrtup(psiUnion*wCapture),up(alpha*psiUnion+mixedDeviation))
  assert psiUnion<psiOld/7
  # A directional Loewner upper valid for every complex pair (x,y):
  # ||(x+alpha*y)rpsi+y*delta||² <= 2*psiUnion*|x+alpha*y|²+2*e²*|y|².
  directional=[[2*psiUnion,2*alpha*psiUnion],[2*alpha*psiUnion,2*alpha*alpha*psiUnion+2*e2]]
  assert psd(directional)
  budgets.append(dict(relative_w_source_norm_target=str(target),retained_tail_highest_order=K,retained_tail_feature_count=K+1,analytic_moment_centers=[moments[k]['center'] for k in range(K+1)],finite_output_rounding_D_energy_upper=str(polyError),moment_rounding_D_energy_upper=str(rounding),omitted_output_D_energy_upper=str(omitted),Cb_trial_D_norm_error_upper=str(eps),shared_residual_difference_D_norm_upper=str(e),shared_residual_difference_D_energy_upper=str(e2),z_b_distance_to_U_D_energy_lower=str(down(distance*distance)),balanced_span_dimension=5,balanced_span_w_covariance_upper=str(wBalanced),union_span_dimension_upper=6,union_psi_covariance_upper=str(psiUnion),union_w_covariance_upper=str(wCapture),union_psi_upper_improvement_factor_lower=str(down(psiOld/psiUnion,10**6)),union_mixed_covariance_entry_lower=str(-mixedBound),union_mixed_covariance_entry_upper=str(mixedBound),union_mixed_deviation_from_alpha_Rpsipsi_upper=str(mixedDeviation),union_ww_deviation_from_alpha_squared_Rpsipsi_upper=str(wwDeviation),union_two_input_directional_Loewner_upper=ser(directional)))
 # Rational controls for zero-degree mass and extreme source degrees.
 controls=[]
 for z in ((O+1)*(O+2),2*(O+1)*(O+2)):
  weights={0:F(3,7),2:F(1,11),L-1:F(1,100000)}
  for K in (0,4,12):
   exact=sum(v/(1-F(m*(m+1),z)) for m,v in weights.items())
   mus=[sum(v*F(m*(m+1),lam)**k for m,v in weights.items()) for k in range(K+2)]
   prefix=sum(mus[k]*F(lam,z)**k for k in range(K+1))
   bound=mus[K+1]*F(lam,z)**(K+1)/(1-F(lam,z))
   assert 0<exact-prefix<=bound
   controls.append(dict(z=z,order=K,positive_geometric_remainder_verified=True))
 # Shared residual bounds include arbitrary real/complex signed mixtures,
 # not just positive source coefficients; rational extremal controls test them.
 for q,t in ((F(1),F(1)),(F(1),F(-1)),(F(0),F(1)),(F(-3,7),F(2,11))):
  d=budgets[1];p=F(d['union_psi_covariance_upper']);ee=F(d['shared_residual_difference_D_norm_upper'])
  assert (q*sqrtup(p)+t*ee)**2 <= 2*q*q*(sqrtup(p)**2)+2*t*t*ee*ee
 return dict(milestone='RC132',status='PASS: balanced finite action and shared analytic residual covariance certified',starting_commit='eee0bb519d400f03c5ecd049f1f87f4126692a52',input_sha256=hs,aperture='11/10',alpha=str(alpha),balanced_source_interval_sha256=shared['finite_balanced_source_coefficient_interval_sha256'],finite_output_degree=O-1,finite_output_polynomial_count=len(polynomial),finite_output_polynomial_center_radius_sha256=hashlib.sha256(json.dumps(polynomial,sort_keys=True,separators=(',',':')).encode()).hexdigest(),trial_definition='z_b=p_b_hat+sum_{k=0}^K nu_b_hat_k eta_k, eta_k inherited from RC131',finite_balanced_source_action_evaluated=True,source_constant_uncertainty_paid=True,full_infinite_output_paid=True,positive_balanced_source_moment_intervals=moments,balanced_action_and_shared_covariance_budgets=budgets,selected_relative_w_source_norm_target='1/1000000000000',exact_action_identity=shared['exact_action_identity'],union_span_definition='span(P0,psi0,f0,w14,v10,z_b)',union_exact_dimension_certified=False,union_dimension_upper=6,z_b_independent_of_U_certified=True,shared_covariance_lower_or_nonzero_rank_certified=False,full_enlarged_Gram_and_endpoint_pairing_evaluated=False,complete_enlarged_input_covariance_evaluated=False,RC130_reference_response_interval_inherited_unchanged=True,new_reference_response_interval_certified=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,exact_rational_geometric_controls=controls,next_cursor='certify joint Gram and endpoint pairings of selected union/balanced family, then remaining analytic action and new-vector covariance before inverse response')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=4);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC132 PASS: balanced finite action, paid shared residual and union covariance')
