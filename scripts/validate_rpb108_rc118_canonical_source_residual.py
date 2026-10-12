"""RC118: actual canonical Riesz residual for a source-shaped supported trial.
Inputs RC117 RC116 RC115 RC112 RC56. No original Weil or augmented actions.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,argparse
from validate_rpb108_rc117_source_adapted_trial import legendre_source
from validate_rpb108_rc114_positive_augmentation import up,down
from validate_rpb108_rc47_correlated_native_transport import root
from validate_rpb108_rc44_reduced_native_head import exp_bounds

def ln2_bounds():
 y=F(1,3);n=80;s=2*sum((y**(2*k+1)/F(2*k+1) for k in range(n)),F(0));e=2*y**(2*n+1)/F((2*n+1)*(1-y*y));return s,s+e

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,old,src,cov,prec=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in [prior,old,src,cov,prec]]==['RC117','RC116','RC115','RC112','RC56']
 assert prior['input_sha256'][:3]==hs[1:4] and prior['input_sha256'][4]==hs[4] and old['input_sha256'][0]==hs[2]
 B=F(11,10);rho=F(252,257);ep=F(11,4);assert exp_bounds(F(1))[1]<ep
 l2L,l2H=ln2_bounds();cL,cH=map(F,prec['actual_constant_enclosure']);constant=(cL+cH+l2L+l2H)/2;delta=(cH-cL+l2H-l2L)/2
 I2=up(ep*F(22,7)**2/3,10**20);HS2=4*B*I2;rows=[]
 for idx,r in enumerate(src['parity_rational_Fourier_adjoint_sources']):
  parity=r['parity'];odd=parity=='odd';data=r['physical_source_coefficient_intervals'];ab=legendre_source(data,replay);oldr=old['parity_canonical_adjoint_trial_certificates'][idx];Qhi=F(oldr['physical_source_norm_squared_upper']);Qlo=F(oldr['physical_source_norm_squared_lower']);U=F(r['rational_frequency_half_bandwidth']);yn=F(r['auxiliary_vector_physical_norm_squared']);es=F(r['canonical_adjoint_source_error_squared_upper']);cs=next(x for x in cov['parity_coverage_certificates'] if x['parity']==parity)
  # Full supported-source regular multiplier norm, not a global L2 multiplier norm.
  A=1+1/(3*B*U);d=1/(9*B);t=F(1,16)
  lowR=(1+t)*A*A*ep*ep/U+2*(1+1/t)*d*d*I2/(U*U) if odd else 2*A*A*I2
  highR=4*ep*ep*yn/(U*U);RJ2=up(lowR+highR,10**20)
  sumrad=sum((F(x['physical_Chebyshev_coefficient_radius']) for x in data),F(0));d2=F(cs['Fourier_restriction_squared_tail_upper']);em2=F(r['finite_model_operator_error_squared_upper'])
  sourcePhysError=root(d2*yn,10**80)+root(em2*yn,10**80)+root(2*B,10**80)*sumrad
  Rnorm=root(RJ2,10**80)+root(HS2,10**80)*sourcePhysError
  gap=F(cs['contour_exponent_gap_lower']);kernel=up(4/exp_bounds(gap)[0],10**80)
  e0=F(r['rational_pi_phase_error_upper'])+F(r['real_imaginary_axis_Taylor_remainder_upper']);L1=U if odd else 2*U
  pointError=(kernel+2*cs['Chebyshev_truncation_length']*e0)*L1+sumrad
  # Endpoint remainder h=-1/2 log(1-(x/B)^2), including the physical boundary jumps.
  p=[F(1,27)/U/(B*B) if odd else F(0),F(2,9)/(B*B),2*pointError/(3*B*B)]
  inner=2*sum((x*y*(B/2)**(i+j+1)/F(i+j+1) for i,x in enumerate(p) for j,y in enumerate(p)),F(0))
  outside=F(2,3)/B+(F(2,9)/U/(B*B) if odd else 0)+pointError
  endpoint2=up(inner+B*outside*outside,10**20);endpointNorm=root(endpoint2,10**80)
  H=F(0);firstL=F(0);secondH=F(0)
  for j,(a,b) in enumerate(ab):
   if j:H+=F(1,j)
   sqlo=0 if a<=0<=b else min(a*a,b*b);sqhi=max(a*a,b*b);m=2*B/F(2*j+1);s=H+constant
   firstL+=m*s*(sqlo if s>=0 else sqhi);secondH+=m*s*s*sqhi
  firstL=down(firstL,10**20);secondH=up(secondH,10**20);assert firstL>0 and secondH>0
  perturb=endpointNorm+Rnorm+delta*root(Qhi,10**80)
  # Select among a fixed rational scalar grid; each candidate is accepted by exact bounds.
  candidates=[]
  for a in range(100,401):
   alpha=F(a,1000);poly2=Qhi-2*alpha*firstL+alpha*alpha*secondH;assert poly2>=0
   residualNorm=root(poly2,10**80)+alpha*perturb
   error2=up(rho*residualNorm*residualNorm,10**12)
   candidates.append((error2,a,poly2,residualNorm))
  if replay:candidates.reverse()
  best=min(candidates,key=lambda x:(x[0],x[1]));err,a,poly2,residualNorm=best;alpha=F(a,1000)
  target=up((root(err,10**80)+root(es,10**80))**2,10**12);old_error=F(prior['parity_source_adapted_trial_certificates'][idx]['canonical_trial_error_squared_upper_for_exact_adjoint'])
  if odd:assert target<old_error
  rows.append(dict(parity=parity,source_global_phase=r['physical_source_global_phase'],source_shape_trial_scalar=str(alpha),trial_dimension=1,principal_harmonic_polynomial_residual_squared_upper=str(up(poly2,10**12)),endpoint_nonconstant_log_source_norm_squared_upper=str(endpoint2),regular_multiplier_source_norm_squared_upper=str(up(Rnorm*Rnorm,10**12)),band_profile_regular_multiplier_squared_upper=str(RJ2),supported_regular_multiplier_Hilbert_Schmidt_squared_upper=str(HS2),physical_polynomial_to_exact_band_source_error_norm_upper=str(up(sourcePhysError,10**40)),physical_source_pointwise_model_error_upper=str(up(pointError,10**40)),canonical_constant_residual_norm_error_upper=str(up(alpha*delta*root(Qhi,10**80),10**40)),full_canonical_metric_physical_residual_squared_upper=str(up(residualNorm*residualNorm,10**12)),canonical_Riesz_trial_error_squared_upper_for_center_source=str(err),canonical_Riesz_trial_error_squared_upper_for_exact_adjoint=str(target),previous_RC117_trial_squared_error_upper=str(old_error),strict_error_enclosure_improvement=target<old_error,canonical_metric_action_source_in_L2_certified=True,regular_source_function_numerically_evaluated=False,original_Weil_action_evaluated=False))
 return dict(milestone='RC118',status='PASS: canonical metric-action residual source bounded; odd source realization improves',input_sha256=hs,arithmetic='700-digit connection enclosures plus exact rational scalar residual budgets',aperture='11/10',parity_canonical_source_residual_certificates=rows,canonical_Riesz_residual_identity_proved_in_note=True,endpoint_jumps_and_logs_paid=True,full_canonical_metric_action_source_error_bound_certified=True,regular_multiplier_is_globally_bounded_on_physical_L2_claimed=False,high_accuracy_canonical_source_realization_completed=False,original_Weil_or_augmented_actions_performed=False,augmented_inverse_responses_computed=False,auxiliary_response_norm_below_one_certified=False,new_positive_native_directions_certified=0,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=5);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,indent=2,sort_keys=True)+'\n')
 print('RC118 PASS: canonical physical residual sources bounded; accurate augmented responses remain open')
