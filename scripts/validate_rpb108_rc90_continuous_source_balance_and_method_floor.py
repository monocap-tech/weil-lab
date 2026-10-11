"""RC90: continuous Young-family near-optimum and nominal enclosure floor.

Exact primal upper and scalar directional lower certificates. Lower
bounds concern these upper-enclosure matrices, never actual leakage.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import json,sys,hashlib
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,cong
N=22
WEIGHTS=[F(265289494,10**9),F(284355267,10**9)]
VECTORS=[[-490271078,-983700233,-991728841,-1000000000,-999996984,-978777633,-919793616,-806853935,-632788903,-411527947,-184908254],[-906499507,-914777754,-931215807,-954641988,-980885117,-1000000000,-993776332,-936265693,-801335183,-579327638,-295936351]]
def quad(v,A,replay):
 if replay:return sum((v[i]*v[i]*A[i][i]+2*sum((v[i]*v[j]*A[i][j] for j in range(i+1,len(v))),F(0)) for i in range(len(v))),F(0))
 return mm(mm([v],A),[[x] for x in v])[0][0]
def sqrtfloor(q):
 den=10**30;r=F(isqrt(q.numerator*den**2//q.denominator),den)
 assert r*r<=q<(r+F(1,den))**2
 return r
def relative40(A,M):
 high=F(1)
 while not psd(add(scale(M,high),A,-1)):high*=2
 low=F(0) if high==1 else high/2
 for _ in range(40):
  mid=(high+low)/2
  if psd(add(scale(M,mid),A,-1)):high=mid
  else:low=mid
 assert psd(add(scale(M,high),A,-1));return high

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];prior,enriched,native,weak=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['milestone']=='RC89' and [prior['input_sha256'][i] for i in [5,7]]==hashes[1:3]
 assert weak['input_sha256'][0]==hashes[2]
 assert prior['actual_Riesz_projection_head_rank']==38 and prior['canonical_trial_dimension']==64 and prior['source_input_features']==list(range(N))
 M=matrix(enriched['enriched_actual_native_Gram_Loewner_lower']);Nom=matrix(prior['projected_nominal_polynomial_residual_Gram_Loewner_upper']);E=matrix(prior['projected_canonical_source_transfer_Gram_Loewner_upper'])
 assert all(psd(A) for A in [M,Nom,E])
 for A in [M,Nom,E]:assert all(A[i][j]==0 for i in range(N) for j in range(N) if (i-j)%2)
 if replay:rawA=add([[Nom[i][j]*(1+WEIGHTS[i%2]) for j in range(N)] for i in range(N)],[[E[i][j]*(1+1/WEIGHTS[i%2]) for j in range(N)] for i in range(N)])
 else:rawA=[[(1+WEIGHTS[i%2])*Nom[i][j]+(1+1/WEIGHTS[i%2])*E[i][j] for j in range(N)] for i in range(N)]
 A,rounding=rounded_bound(rawA,1,10**24);assert psd(A)
 ceiling=F(weak['scalar_Schur_source_budget_strict_ceiling_using_inherited_complement_floor']);parity=[]
 for p in range(2):
  v=list(map(F,VECTORS[p]));m=quad(v,block(M,p),replay);n=quad(v,block(Nom,p),replay);e=quad(v,block(E,p),replay);assert m>0 and n>0 and e>0
  a=n/m;b=e/m;r=sqrtfloor(a*b);lower=a+b+2*r
  lam=relative40(block(A,p),block(M,p));gap=lam-lower;assert 0<=gap<F(1,10**9)
  # For EVERY t>0, a(1+t)+b(1+1/t) >= a+b+2sqrt(ab).
  # PSD rounding only increases the directional quadratic.
  assert lower>ceiling and a>ceiling
  old=F(prior['parity_residual_certificates'][p]['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']);assert lam<old
  tests=[]
  for amp in [F(0),F(1,4),F(1,2),F(1)]:
   ideal_lower=a+amp**2*b+2*amp*r
   tests.append(dict(hypothetical_transfer_amplitude=str(amp),transfer_covariance_scale=str(amp**2),all_positive_Young_family_relative_factor_lower=str(ideal_lower),actual_source_certificate_when_amplitude_below_one=False))
  if replay:
   Ci=inverse(block(matrix(native['chebyshev_to_legendre']),p));assert psd(cong(Ci,add(scale(block(M,p),lam),block(A,p),-1)))
  parity.append(dict(parity='even' if p==0 else 'odd',Young_parameter=str(WEIGHTS[p]),native_parity_direction=list(map(str,v)),reference_input_Gram_quadratic=str(m),nominal_upper_quadratic=str(n),transfer_upper_quadratic=str(e),nominal_upper_Rayleigh_ratio=str(a),transfer_upper_Rayleigh_ratio=str(b),square_root_product_lower=str(r),all_continuous_positive_Young_family_relative_factor_lower=str(lower),actual_rank_38_residual_relative_original_canonical_input_Gram_upper=str(lam),certified_global_family_optimality_gap_upper=str(gap),prior_retained_relative_upper=str(old),idealized_transfer_sensitivity_certificates=tests,zero_transfer_nominal_upper_to_inherited_scalar_ceiling_ratio_lower=str(a/ceiling)))
 bound=max(F(r['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']) for r in parity);oldbound=F(prior['actual_rank_38_relative_bound_for_existing_22_source_inputs']);oldA=matrix(prior['refined_actual_rank_38_projected_original_source_Gram_Loewner_upper'])
 result=dict(milestone='RC90',status='PASS',input_sha256=hashes,actual_Riesz_projection_head_rank=38,canonical_trial_dimension=64,source_input_features=list(range(N)),
  continuous_family_definition='A(t)=(1+t_p)N+(1+1/t_p)E, t_p>0, followed by upward Loewner rounding; N and E fixed from RC89',relative_factor_reference='unchanged RC67 actual original 22-input canonical Gram lower matrix, not the unknown full actual input Gram',
  relative_PSD_bisection_steps=40,primal_response_upper_rounding_grid='1e-24',directional_sqrt_lower_grid='1e-30',parity_residual_certificates=parity,
  projected_nominal_polynomial_residual_Gram_Loewner_upper=serialize(Nom),projected_canonical_source_transfer_Gram_Loewner_upper=serialize(E),component_matrices_unchanged=True,refined_actual_rank_38_projected_original_source_Gram_Loewner_upper=serialize(A),source_rounding_row_allowances=list(map(str,rounding)),final_source_whole_Loewner_improves_RC89=psd(add(oldA,A,-1)),
  actual_rank_38_relative_bound_for_existing_22_source_inputs=str(bound),prior_retained_relative_bound=str(oldbound),certified_fractional_upper_bound_reduction=str(1-bound/oldbound),
  all_continuous_positive_Young_family_optima_bracketed_to_one_billionth=True,zero_transfer_nominal_enclosure_cannot_meet_inherited_scalar_gate=True,scalar_Schur_source_budget_strict_ceiling_using_inherited_complement_floor=str(ceiling),
  lower_bounds_are_on_fixed_upper_enclosure_family_not_actual_leakage=True,idealized_transfer_sensitivity_is_not_an_actual_source_certificate=True,physical_source_and_Riesz_trials_unchanged=True,
  required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,thirty_eight_source_input_covariance_evaluated=False,enlarged_Weil_floor_certified=False,enlarged_complement_floor_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert result==saved
 return result
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 names=['rpb108_rc89_frequency_weighted_arch_transfer.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json']
 defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()))
  print('PASS: independent triangular quadratics, exact continuous-family brackets, final source assembly and native-to-Legendre PSD congruences')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
