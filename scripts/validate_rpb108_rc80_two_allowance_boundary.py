"""RC80: exact boundary of the fixed rank-38 two-allowance Young method.

Every lower bound here concerns an upper-enclosure family, never the actual
source residual or the actual Riesz error.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import json,hashlib,sys
from validate_rpb108_rc31_trial_riesz import inverse,psd,mm
from validate_rpb108_rc47_correlated_native_transport import matrix
from validate_rpb108_rc65_parity_projected_residual_refinement import scale,add,cong
from validate_rpb108_rc29_atom_reduction import legendre
N=22;RHO=F(252,257)
def quad(v,A):return sum((x*y*A[i][j] for i,x in enumerate(v) for j,y in enumerate(v)),F(0))
def lower_root(q,den=10**40):
 assert q>=0
 r=F(isqrt(q.numerator*den**2//q.denominator),den)
 assert r*r<=q<(r+F(1,den))**2
 return r

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];previous,native,enriched,weak=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert previous['input_sha256'][5]==hashes[1] and previous['input_sha256'][3]==hashes[2]
 assert weak['input_sha256'][0]==hashes[1]
 assert previous['source_input_features']==list(range(N)) and previous['actual_projection_target_features']==list(range(38))
 Nom=matrix(previous['projected_nominal_polynomial_residual_Gram_Loewner_upper'])
 Err=matrix(previous['projected_canonical_source_transfer_Gram_Loewner_upper'])
 A=matrix(previous['refined_actual_rank_38_projected_old_source_Gram_Loewner_upper'])
 assert psd(Nom) and psd(Err) and psd(add(A,add(Nom,Err),-1))
 P=matrix(native['physical_native_Gram']);Mup=scale(P,RHO)
 Mlo=matrix(enriched['enriched_actual_native_Gram_Loewner_lower']);assert psd(add(Mup,Mlo,-1))
 C=matrix(native['chebyshev_to_legendre']);Ci=inverse(C)
 gamma=F(weak['scalar_Schur_source_budget_strict_ceiling_using_inherited_complement_floor']);assert gamma>0
 LP=[legendre(n) for n in range(N)];witnesses=[]
 if replay:NL=cong(Ci,Nom);EL=cong(Ci,Err);PL=cong(Ci,P)
 for basis in ['native_Chebyshev','physical_Legendre']:
  for degree in range(N):
   v=[F(i==degree) for i in range(N)] if basis=='native_Chebyshev' else [Ci[i][degree] for i in range(N)]
   p=quad(v,P);den=RHO*p;w=quad(v,Nom);e=quad(v,Err);assert p>0 and w>0 and e>0
   if basis=='physical_Legendre':assert p==F(11,5*(2*degree+1)) and mm(C,[[x] for x in v])==[[F(i==degree)] for i in range(N)]
   if replay:
    cv=[sum((C[a][j]*v[j] for j in range(N)),F(0)) for a in range(N)]
    target=[sum((cv[a]*(LP[a][b] if b<=a else 0) for a in range(N)),F(0)) for b in range(N)]
    direct=sum((x*y*F(11,5*(a+b+1)) for a,x in enumerate(target) for b,y in enumerate(target) if (a+b)%2==0),F(0))
    assert direct==p
    if basis=='physical_Legendre':assert (w,e,p)==(NL[degree][degree],EL[degree][degree],PL[degree][degree])
   cross=lower_root(w*e);lower=w+e+2*cross
   assert lower>=w+e and lower>gamma*den
   witnesses.append(dict(basis=basis,target_degree=degree,parity='even' if degree%2==0 else 'odd',exact_native_input_coefficients=list(map(str,v)),
    physical_input_squared_norm=str(p),actual_canonical_input_Gram_upper_quadratic=str(den),
    nominal_allowance_quadratic=str(w),transfer_allowance_quadratic=str(e),product_square_root_lower=str(cross),
    optimally_Young_balanced_allowance_quadratic_lower=str(lower),any_fixed_allowance_Young_factor_relative_actual_input_Gram_lower=str(lower/den),
    ratio_to_inherited_scalar_budget_ceiling_lower=str(lower/(den*gamma)),
    nominal_component_only_method_factor_lower=str(w/den),transfer_component_only_method_factor_lower=str(e/den),
    required_strict_nominal_allowance_upper=str(gamma*den),required_strict_transfer_allowance_upper=str(gamma*den),
    nominal_component_reduction_factor_necessary_lower=str(w/(gamma*den)),transfer_component_reduction_factor_necessary_lower=str(e/(gamma*den)),
    eliminating_transfer_alone_still_cannot_certify_budget=w>gamma*den,
    eliminating_nominal_alone_still_cannot_certify_budget=e>gamma*den))
 best=max(witnesses,key=lambda x:F(x['any_fixed_allowance_Young_factor_relative_actual_input_Gram_lower']))
 nominalbest=max(witnesses,key=lambda x:F(x['nominal_component_only_method_factor_lower']))
 transferbest=max(witnesses,key=lambda x:F(x['transfer_component_only_method_factor_lower']))
 assert nominalbest['eliminating_transfer_alone_still_cannot_certify_budget'] and transferbest['eliminating_nominal_alone_still_cannot_certify_budget']
 # At arbitrary rank m, the RC78 Legendre geometric-tail prescription
 # requires L<(2m+3)/(2*pi*B)<m. Its certified tau_m^2 is >=1/log(e+L).
 # Thus a retained generic prime-norm transport of the same Ep enclosure
 # can decay no faster, within this prescription, than C/log(4m).
 v=list(map(F,best['exact_native_input_coefficients']))
 Ep=matrix(enriched['enriched_actual_physical_Riesz_error_Gram_Loewner_upper'])
 kappa=F(11669,4096);nu=F(1,65536)
 coefficient=(1+nu)*kappa**2*quad(v,Ep)/(RHO*quad(v,P))
 log_required=coefficient/gamma
 exponent=1000000;log_rank_cap_upper=F(3*exponent+2)
 assert log_required>log_rank_cap_upper
 generic_rank_boundary=dict(retained_physical_prime_norm_allowance=str(kappa),retained_source_transfer_Young_parameter=str(nu),
  generic_prime_transfer_relative_factor_coefficient=str(coefficient),necessary_log_4m_lower=str(log_required),
  excluded_rank_upper_description='10^1000000',log_4m_upper_for_excluded_rank_range=str(log_rank_cap_upper),
  scope='RC78 geometric Legendre tail prescription, retained RC67 physical Riesz-error enclosure and retained full-prime norm allowance; not all projected-prime estimates or all Riesz approximations')
 return dict(milestone='RC80',status='PASS',input_sha256=hashes,source_input_features=list(range(N)),actual_projection_target_features=list(range(38)),
  fixed_allowance_method_class='A(t)=(1+t_p)N+(1+1/t_p)E+PSD outward allowance, t_p>0; N and E are RC79 canonical upper-enclosure matrices',
  directional_Young_infimum_identity='inf_{t>0} [(1+t)w+(1+1/t)e]=(sqrt(w)+sqrt(e))^2',
  inherited_scalar_source_budget_strict_ceiling=str(gamma),directional_certificates=witnesses,
  strongest_combined_allowance_boundary_certificate=best,strongest_nominal_allowance_boundary_certificate=nominalbest,strongest_transfer_allowance_boundary_certificate=transferbest,
  any_fixed_allowance_Young_method_uniform_relative_factor_lower=str(F(best['any_fixed_allowance_Young_factor_relative_actual_input_Gram_lower'])),
  changing_Young_parameters_alone_can_certify_inherited_budget=False,eliminating_only_one_current_allowance_can_certify_inherited_budget=False,
  RC79_certified_actual_residual_relative_upper=previous['actual_rank_38_relative_bound_for_existing_22_source_inputs'],
  nominal_and_transfer_upper_enclosures_both_require_redesign_or_sharpening=True,
  generic_rank_only_retained_Riesz_allowance_boundary_certificate=generic_rank_boundary,
  bound_family_boundary_is_actual_residual_lower_bound=False,actual_Riesz_error_directional_lower_bound_proved=False,
  actual_rank_38_scalar_budget_failure_proved=False,head_enlargement_with_recomputed_allowances_obstructed=False,
  required_scalar_source_budget_certified=False,thirty_eight_source_input_covariance_evaluated=False,enlarged_Weil_floor_certified=False,
  whole_aperture_positivity_obstructed=False,whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/n for n in ['rpb108_rc79_uniform_adjoint_tail_transport.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json']]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==saved
  print('PASS: independent polynomial physical moments, allowance congruences and exact Young-infimum root floors')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
