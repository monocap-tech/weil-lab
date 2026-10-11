"""RC73: actual projected signed-pole transfer at native rank 38.

The range Taylor polynomials map EXACTLY into the actual Riesz head.
Archimedean and prime transfer remain bounded by their full norms.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import json,hashlib,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,root
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,cong,relative
N=22;HEAD=38;R=F(11,5);b=F(11,20);RHO=F(252,257)
def diag(x):return [[v*F(i==j) for j in range(len(x))] for i,v in enumerate(x)]
def quad(v,A):return sum((x*y*A[i][j] for i,x in enumerate(v) for j,y in enumerate(v)),F(0))
def progress(s):print(s,file=sys.stderr,flush=True)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths]
 residual,barrier,source,enriched,head,native,prime,pole,transport=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [source['input_sha256'][k] for k in [0,1,3,4,6]]==[hashes[k] for k in [3,5,6,7,8]]
 assert [residual['input_sha256'][k] for k in [0,1,2,4,6,7]]==[hashes[k] for k in [4,3,5,6,2,8]]
 assert [barrier['input_sha256'][k] for k in [0,1,2,3,5]]==[hashes[k] for k in [0,2,3,5,8]]
 assert head['input_sha256'][:2]==[hashes[k] for k in [3,5]]
 assert head['actual_orthogonal_projection_rank_certified']==HEAD
 kp=F(prime['full_paired_prime_physical_operator_norm_upper']);ka=F(transport['certified_physical_archimedean_remainder_norm_upper'])
 norm=[F(pole[k]) for k in ['cosh_physical_norm_squared_upper','sinh_physical_norm_squared_upper']]
 oldk=list(map(F,transport['complete_physical_operator_parity_norm_upper']))
 assert oldk==[ka+kp+2*x for x in norm]
 ranges=[];beta=[]
 for p in [0,1]:
  first=HEAD+p # cosh first omitted degree 38, sinh first 39
  ratio=b*b/F((first+1)*(first+2));assert 0<ratio<1
  tail=b**first/F(factorial(first))/(1-ratio)
  poly=[b**n/F(factorial(n)) if n%2==p else F(0) for n in range(HEAD)]
  normroot=root(R*norm[p],10**80)
  z=2*normroot*tail*10**80;bet=F(-(-z.numerator//z.denominator),10**80)
  assert 0<bet<2*norm[p] and bet<F(1,10**50)
  if replay:
   partial=sum((b**(first+2*j)/F(factorial(first+2*j)) for j in range(20)),F(0))
   nextdegree=first+40;rnext=b*b/F((nextdegree+1)*(nextdegree+2))
   independent=partial+b**nextdegree/F(factorial(nextdegree))/(1-rnext)
   assert independent<=tail
   assert normroot**2>=R*norm[p] and bet>=2*normroot*tail
   assert all(poly[n]==0 for n in range(HEAD) if n%2!=p)
   assert max(n for n,x in enumerate(poly) if x)==first-2
  beta.append(bet)
  ranges.append(dict(parity='even' if p==0 else 'odd',physical_range='cosh(x/2)' if p==0 else 'sinh(x/2)',
   exact_Taylor_coefficients_in_t_equals_x_over_B=list(map(str,poly)),Taylor_degree=first-2,
   first_omitted_degree=first,successive_tail_term_ratio_upper=str(ratio),uniform_range_remainder_upper=str(tail),
   physical_range_squared_norm_upper=str(norm[p]),sqrt_range_mass_product_upper=str(normroot),
   projected_physical_to_canonical_pole_norm_upper_divided_by_sqrt_rho=str(bet),
   prior_full_physical_pole_norm_upper=str(2*norm[p])))
 progress('rank-38 signed-pole range subtraction certified')
 effective=[ka+kp+bet for bet in beta]
 Ep=matrix(enriched['enriched_actual_physical_Riesz_error_Gram_Loewner_upper']);V=matrix(enriched['enriched_native_trial_coefficients']);mass=list(map(F,enriched['physical_mass']))
 if replay:
  T=[[sum((mass[a]*V[a][i]*V[a][j] for a in range(64)),F(0)) for j in range(N)] for i in range(N)]
  raw=cong(diag([effective[i%2] for i in range(N)]),Ep)
 else:
  T=cong(V,diag(mass));raw=[[effective[i%2]*effective[j%2]*Ep[i][j] for j in range(N)] for i in range(N)]
 nu=F(1,65536);delta=F(source['actual_source_approximation_operator_error_upper'])
 Eequiv=rounded_bound(add(scale(raw,1+nu),T,(1+1/nu)*delta**2),1,10**24)[0]
 Ecan=scale(Eequiv,RHO);Eold=matrix(source['enriched_source_transfer_physical_Gram_Loewner_upper'])
 assert psd(Eequiv) and psd(add(Eold,Eequiv,-1))
 # Eequiv is rho-scaled canonical PROJECTED transfer, not a full physical
 # error Gram. Substituting it is valid only after the actual Pi38.
 W=matrix(residual['residual_certificates'][1]['nominal_physical_polynomial_residual_Gram_Loewner_upper']);Mlo=matrix(enriched['enriched_actual_native_Gram_Loewner_lower'])
 oldA=matrix(barrier['refined_actual_rank_38_projected_old_source_Gram_Loewner_upper'])
 oldt=[F(x['Young_parameter']) for x in barrier['refined_parity_certificates']]
 def upper(ts):return rounded_bound([[RHO*((1+ts[i%2])*W[i][j]+(1+1/ts[i%2])*Eequiv[i][j]) for j in range(N)] for i in range(N)],1,10**24)[0]
 baseline=upper(oldt);assert psd(add(oldA,baseline,-1))
 grids=[[F(1),F(5,4),F(3,2),F(7,4),F(2),F(9,4),F(5,2),F(11,4),F(3)],
        [F(3,2),F(7,4),F(2),F(9,4),F(5,2)]]
 selected=[];parity=[]
 for p in [0,1]:
  candidates=[]
  for t in grids[p]:
   Ap=scale(add(scale(block(W,p),1+t),block(Eequiv,p),1+1/t),RHO)
   candidates.append((relative(Ap,block(Mlo,p)),t))
  lam,t=min(candidates);selected.append(t)
  parity.append(dict(parity='even' if p==0 else 'odd',Young_parameter=str(t),effective_transfer_norm_upper_divided_by_sqrt_rho=str(effective[p]),candidate_certificates=[dict(Young_parameter=str(q),upper=str(l)) for l,q in candidates]))
 A=upper(selected);assert psd(A) and psd(add(A,Ecan,-1))
 for p in [0,1]:
  lam=relative(block(A,p),block(Mlo,p));parity[p]['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']=str(lam)
  if replay:
   Ci=inverse(block(matrix(native['chebyshev_to_legendre']),p))
   assert psd(cong(Ci,add(scale(block(Mlo,p),lam),block(A,p),-1)))
   assert psd(cong(Ci,block(add(oldA,baseline,-1),p)))
 bound=max(F(x['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']) for x in parity)
 prior=F(barrier['refined_actual_rank_38_relative_bound_for_existing_22_source_inputs']);assert bound<prior
 # Diagnose the remaining allowance-method barrier on the SAME P20
 # input. This is still a lower bound on majorants, not on actual error.
 w=barrier['strongest_fixed_allowance_method_barrier_witness'];v=list(map(F,w['exact_native_input_coefficients']));P=matrix(native['physical_native_Gram'])
 floor=quad(v,Eequiv)/quad(v,P);gamma=F(barrier['strict_inherited_scalar_source_budget_ceiling']);assert floor>gamma
 progress('actual rank-38 residual upper '+str(bound))
 return dict(milestone='RC73',status='PASS',input_sha256=hashes,source_input_features=list(range(N)),actual_projection_target_features=list(range(HEAD)),
  signed_pole_range_projection_certificates=ranges,range_Taylor_polynomials_map_exactly_into_actual_native_head=True,
  full_archimedean_physical_norm_upper_retained=str(ka),full_paired_prime_physical_norm_upper_retained=str(kp),
  projected_canonical_source_transfer_Gram_Loewner_upper=serialize(Ecan),
  projected_transfer_equivalent_Gram_divided_by_rho=serialize(Eequiv),projected_transfer_enclosure_Loewner_improves_previous_full_allowance=True,
  unchanged_Young_parameters_residual_upper=serialize(baseline),unchanged_parameters_whole_residual_Loewner_improvement_certified=True,
  refined_actual_rank_38_projected_old_source_Gram_Loewner_upper=serialize(A),parity_residual_certificates=parity,
  actual_rank_38_relative_bound_for_existing_22_source_inputs=str(bound),prior_RC72_relative_bound=str(prior),certified_fractional_upper_bound_reduction=str(1-bound/prior),
  remaining_P20_allowance_majorant_relative_actual_input_Gram_factor_lower=str(floor),remaining_P20_allowance_majorant_to_budget_ceiling_ratio_lower=str(floor/gamma),
  remaining_allowance_barrier_is_actual_leakage_lower_bound=False,
  projected_pole_transfer_certified=True,projected_archimedean_transfer_sharpened=False,projected_prime_transfer_sharpened=False,
  complete_physical_source_transfer_Gram_improved=False,required_scalar_source_budget_certified=False,
  actual_rank_38_scalar_budget_failure_proved=False,thirty_eight_source_input_covariance_evaluated=False,
  enlarged_Weil_floor_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/n for n in ['rpb108_rc71_thirty_eight_projected_old_source.json','rpb108_rc72_fixed_transfer_barrier.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc70_thirty_eight_native_projection.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc43_native_prime_head.json','rpb108_rc42_native_signed_pole_head.json','rpb108_rc66_arch_multiplier_transport.json']]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==saved
  print('PASS: independent 20-term range tails, exact root conditions, projected pole transport, physical trial sums and canonical congruence replay')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
