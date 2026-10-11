"""RC79: propagate the actual canonical adjoint tail through all residual terms.

The physical polynomial remainder is subtracted before the adjoint tail map.
No second independent projection factor is applied to the prime term.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,sys
from validate_rpb108_rc31_trial_riesz import inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,root
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,cong,relative
N=22;RHO=F(252,257)
def diag(x):return [[v*F(i==j) for j in range(len(x))] for i,v in enumerate(x)]

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths]
 previous,residual,source,enriched,head,native,pole=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [previous['input_sha256'][i] for i in [5,6,7,8,9,4]]==hashes[1:]
 assert head['actual_orthogonal_projection_rank_certified']==38
 tau=F(previous['canonical_complement_embedding_norm_upper'])
 s=tau**2/RHO;assert 0<s<1
 sigma=root(s,10**30);assert sigma**2>=s and sigma<1
 # RC78's arch certificate is derived from a physical output remainder.
 # Replace its sqrt(rho) adjoint contraction by tau. The pole certificate
 # likewise subtracts an actual degree<38 physical polynomial first.
 oldarch=F(previous['projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho'])
 arch=oldarch*sigma
 oldpoles=[F(x['projected_physical_to_canonical_pole_norm_upper_divided_by_sqrt_rho']) for x in pole['signed_pole_range_projection_certificates']]
 poles=[x*sigma for x in oldpoles]
 prime=F(previous['projected_prime_physical_to_canonical_norm_upper_divided_by_sqrt_rho'])
 effective=[arch+prime+x for x in poles]
 Ep=matrix(enriched['enriched_actual_physical_Riesz_error_Gram_Loewner_upper'])
 V=matrix(enriched['enriched_native_trial_coefficients']);mass=list(map(F,enriched['physical_mass']))
 if replay:
  T=[[sum((mass[q]*V[q][i]*V[q][j] for q in range(64)),F(0)) for j in range(N)] for i in range(N)]
  rawE=cong(diag([effective[i%2] for i in range(N)]),Ep)
 else:
  T=cong(V,diag(mass));rawE=[[effective[i%2]*effective[j%2]*Ep[i][j] for j in range(N)] for i in range(N)]
 nu=F(1,65536);delta=F(source['actual_source_approximation_operator_error_upper'])
 E=rounded_bound(add(scale(rawE,1+nu),T,(1+1/nu)*delta**2*s),1,10**24)[0]
 Ecan=scale(E,RHO);oldE=matrix(previous['projected_transfer_equivalent_Gram_divided_by_rho'])
 assert psd(E) and psd(add(oldE,E,-1))
 W=matrix(residual['residual_certificates'][1]['nominal_physical_polynomial_residual_Gram_Loewner_upper'])
 assert psd(W)
 # Nominal residual B(F_nom-p), B=(I-Pi38)i*, has covariance <=tau^2 W.
 nominal=scale(W,tau**2);oldnominal=scale(W,RHO)
 assert psd(add(oldnominal,nominal,-1))
 Mlo=matrix(enriched['enriched_actual_native_Gram_Loewner_lower'])
 def upper(ts):
  if replay:
   # Independent entrywise sum below uses no approximate matrix factors.
   raw=[[((1+ts[i%2])*nominal[i][j]+(1+1/ts[i%2])*Ecan[i][j]) for j in range(N)] for i in range(N)]
  else:
   raw=[[RHO*((1+ts[i%2])*s*W[i][j]+(1+1/ts[i%2])*E[i][j]) for j in range(N)] for i in range(N)]
  return rounded_bound(raw,1,10**24)[0]
 oldt=[F(x['Young_parameter']) for x in previous['parity_residual_certificates']]
 baseline=upper(oldt);oldA=matrix(previous['refined_actual_rank_38_projected_old_source_Gram_Loewner_upper'])
 assert psd(add(oldA,baseline,-1))
 parity=[];selected=[]
 for p in [0,1]:
  tests=[]
  for t in [F(1,2),F(5,8),F(3,4),F(7,8),F(1),F(9,8),F(5,4),F(3,2)]:
   Ap=add(scale(block(nominal,p),1+t),block(Ecan,p),1+1/t)
   tests.append((relative(Ap,block(Mlo,p)),t))
  lam,t=min(tests);selected.append(t)
  parity.append(dict(parity='even' if p==0 else 'odd',Young_parameter=str(t),candidate_certificates=[dict(Young_parameter=str(q),upper=str(l)) for l,q in tests]))
 A=upper(selected);assert psd(A)
 for p in [0,1]:
  lam=relative(block(A,p),block(Mlo,p))
  parity[p]['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']=str(lam)
  if replay:
   Ci=inverse(block(matrix(native['chebyshev_to_legendre']),p))
   assert psd(cong(Ci,add(scale(block(Mlo,p),lam),block(A,p),-1)))
 bound=max(F(x['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']) for x in parity)
 prior=F(previous['actual_rank_38_relative_bound_for_existing_22_source_inputs']);assert bound<prior
 return dict(milestone='RC79',status='PASS',input_sha256=hashes,source_input_features=list(range(N)),actual_projection_target_features=list(range(38)),
  canonical_complement_embedding_norm_upper=str(tau),squared_tail_to_global_embedding_ratio=str(s),tail_to_global_embedding_ratio_upper=str(sigma),
  projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho=str(arch),projected_prime_physical_to_canonical_norm_upper_divided_by_sqrt_rho=str(prime),
  projected_pole_norm_uppers_divided_by_sqrt_rho=list(map(str,poles)),prime_bound_receives_no_duplicate_tail_factor=True,
  projected_nominal_polynomial_residual_Gram_Loewner_upper=serialize(nominal),nominal_residual_Loewner_improves_global_embedding_bound=True,
  projected_canonical_source_transfer_Gram_Loewner_upper=serialize(Ecan),projected_transfer_equivalent_Gram_divided_by_rho=serialize(E),projected_transfer_Loewner_improves_RC78=True,
  unchanged_Young_parameters_residual_upper=serialize(baseline),unchanged_parameters_whole_residual_Loewner_improvement_certified=True,
  refined_actual_rank_38_projected_old_source_Gram_Loewner_upper=serialize(A),parity_residual_certificates=parity,
  actual_rank_38_relative_bound_for_existing_22_source_inputs=str(bound),prior_RC78_relative_bound=str(prior),certified_fractional_upper_bound_reduction=str(1-bound/prior),
  required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,thirty_eight_source_input_covariance_evaluated=False,
  enlarged_Weil_floor_certified=False,analytic_Schur_lemma_Lean_formalized=False,whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/n for n in ['rpb108_rc78_legendre_fourier_transfer.json','rpb108_rc71_thirty_eight_projected_old_source.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc70_thirty_eight_native_projection.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc73_projected_pole_transfer.json']]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==saved
  print('PASS: independent physical trial contraction, canonical covariance assembly and exact congruence replay')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
