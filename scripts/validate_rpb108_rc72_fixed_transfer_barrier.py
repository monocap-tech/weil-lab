"""RC72: fixed unprojected source-transfer allowance barrier and Young refinement.

A lower bound on the MAJORANT used by RC71, never on actual leakage.
The barrier applies only while this full transfer allowance is retained.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,cong,relative
from validate_rpb108_rc29_atom_reduction import legendre
N=22;RHO=F(252,257)
def diag(x):return [[v*F(i==j) for j in range(len(x))] for i,v in enumerate(x)]
def quad(v,A):return sum((x*y*A[i][j] for i,x in enumerate(v) for j,y in enumerate(v)),F(0))
def progress(s):print(s,file=sys.stderr,flush=True)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];residual,source,enriched,native,weak,transport=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [residual['input_sha256'][k] for k in [6,1,2,7]]==[hashes[k] for k in [1,2,3,5]]
 assert [source['input_sha256'][k] for k in [0,1,6]]==[hashes[k] for k in [2,3,5]]
 assert weak['input_sha256'][0]==hashes[3]
 assert residual['source_input_features']==list(range(N))
 assert residual['actual_projection_target_features']==list(range(38))
 E=matrix(source['enriched_source_transfer_physical_Gram_Loewner_upper'])
 Ep=matrix(enriched['enriched_actual_physical_Riesz_error_Gram_Loewner_upper']);V=matrix(enriched['enriched_native_trial_coefficients'])
 mass=list(map(F,enriched['physical_mass']));delta=F(source['actual_source_approximation_operator_error_upper'])
 k=list(map(F,transport['complete_physical_operator_parity_norm_upper']));nu=F(1,65536)
 if replay:
  T=[[sum((mass[a]*V[a][i]*V[a][j] for a in range(64)),F(0)) for j in range(N)] for i in range(N)]
  K=diag([k[i%2] for i in range(N)]);Riesz=cong(K,Ep)
 else:
  T=cong(V,diag(mass));Riesz=[[k[i%2]*k[j%2]*Ep[i][j] for j in range(N)] for i in range(N)]
 rawE=add(scale(Riesz,1+nu),T,(1+1/nu)*delta**2)
 assert rounded_bound(rawE,1,10**24)[0]==E
 assert psd(E) and psd(add(E,scale(Riesz,1+nu),-1))
 P=matrix(native['physical_native_Gram']);Mlo=matrix(enriched['enriched_actual_native_Gram_Loewner_lower']);Mup=scale(P,RHO)
 C=matrix(native['chebyshev_to_legendre']);Ci=inverse(C)
 gamma=F(weak['scalar_Schur_source_budget_strict_ceiling_using_inherited_complement_floor'])
 assert gamma>0
 witnesses=[];LP=[legendre(a) for a in range(N)]
 for basis in ['native_Chebyshev','physical_Legendre']:
  for degree in range(N):
   v=[F(i==degree) for i in range(N)] if basis=='native_Chebyshev' else [Ci[i][degree] for i in range(N)]
   pnorm=quad(v,P);allowance=quad(v,E);rpart=(1+nu)*quad(v,Riesz)
   assert pnorm>0 and allowance>=rpart>0
   if basis=='physical_Legendre':assert pnorm==mass[degree] and mm(C,[[x] for x in v])==[[F(i==degree)] for i in range(N)]
   floor=allowance/pnorm
   # Any positive Young majorant B>=rho E has B(v)>=rho E(v),
   # whereas gamma M_actual(v)<=gamma rho P(v).
   difference=quad(v,add(scale(Mup,gamma),scale(E,RHO),-1))
   assert difference==RHO*(gamma*pnorm-allowance)
   if replay:
    # Independently integrate the actual physical target monomial norm.
    cv=[sum((C[a][j]*v[j] for j in range(N)),F(0)) for a in range(N)]
    target=[sum((cv[a]*(LP[a][b] if b<=a else F(0)) for a in range(N)),F(0)) for b in range(N)]
    direct=sum((x*y*F(11,5*(a+b+1)) for a,x in enumerate(target) for b,y in enumerate(target) if (a+b)%2==0),F(0))
    assert direct==pnorm
    EL=cong(Ci,E);PL=cong(Ci,P)
    if basis=='physical_Legendre':assert allowance==EL[degree][degree] and pnorm==PL[degree][degree]
   witnesses.append(dict(basis=basis,target_degree=degree,parity='even' if degree%2==0 else 'odd',exact_native_input_coefficients=list(map(str,v)),
    physical_input_squared_norm=str(pnorm),fixed_physical_transfer_allowance_quadratic=str(allowance),
    retained_Riesz_error_enclosure_component_quadratic=str(rpart),Riesz_component_fraction_of_allowance=str(rpart/allowance),
    any_positive_Young_majorant_relative_actual_input_Gram_lower=str(floor),
    ratio_to_scalar_budget_ceiling_lower=str(floor/gamma),comparison_budget_Mup_minus_rho_transfer_quadratic=str(difference),
    fixed_allowance_method_cannot_certify_scalar_budget=difference<0))
 strongest=max(witnesses,key=lambda x:F(x['any_positive_Young_majorant_relative_actual_input_Gram_lower']))
 assert strongest['fixed_allowance_method_cannot_certify_scalar_budget']
 progress('fixed-allowance method barrier certified')
 # Refine the scalar Young parameter while preserving the same data and
 # physical source-subtraction method. Every candidate is exact-PSD checked.
 W=matrix(residual['residual_certificates'][1]['nominal_physical_polynomial_residual_Gram_Loewner_upper']);assert psd(W)
 grids=[[F(5,2),F(11,4),F(3),F(13,4),F(7,2),F(15,4),F(4)],
        [F(3,2),F(7,4),F(2),F(9,4),F(5,2),F(11,4),F(3)]]
 selected=[];parity=[]
 for p in range(2):
  candidates=[]
  for t in grids[p]:
   Ap=scale(add(scale(block(W,p),1+t),block(E,p),1+1/t),RHO)
   assert psd(add(Ap,scale(block(E,p),RHO),-1))
   lam=relative(Ap,block(Mlo,p));candidates.append((lam,t))
  lam,t=min(candidates);selected.append(t)
  parity.append(dict(parity='even' if p==0 else 'odd',Young_parameter=str(t),candidate_certificates=[dict(Young_parameter=str(q),upper=str(l)) for l,q in candidates]))
 A=rounded_bound([[RHO*((1+selected[i%2])*W[i][j]+(1+1/selected[i%2])*E[i][j]) for j in range(N)] for i in range(N)],1,10**24)[0]
 assert psd(A) and psd(add(A,scale(E,RHO),-1))
 for p in range(2):
  lam=relative(block(A,p),block(Mlo,p));parity[p]['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']=str(lam)
  if replay:assert psd(cong(block(Ci,p),add(scale(block(Mlo,p),lam),block(A,p),-1)))
 bound=max(F(x['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']) for x in parity)
 prior=F(residual['actual_rank_38_relative_bound_for_existing_22_source_inputs']);assert bound<=prior
 floor=F(strongest['any_positive_Young_majorant_relative_actual_input_Gram_lower'])
 return dict(milestone='RC72',status='PASS',input_sha256=hashes,source_input_features=list(range(N)),actual_projection_target_features=list(range(38)),
  strict_inherited_scalar_source_budget_ceiling=str(gamma),fixed_source_transfer_allowance_reconstructed_exactly=True,
  method_class='B=rho[(1+t)W+(1+1/t)E_F]+PSD outward allowance, W PSD, t>0 (parity parameters allowed)',
  universal_majorant_floor_identity='B >= rho E_F; applies for any head count while the same FULL physical transfer allowance is paid',
  exact_fixed_allowance_method_barrier_witnesses=witnesses,strongest_fixed_allowance_method_barrier_witness=strongest,
  any_positive_Young_majorant_uniform_relative_actual_input_Gram_factor_lower=str(floor),
  required_directional_allowance_reduction_factor_lower=str(floor/gamma),
  required_strict_directional_physical_transfer_allowance_upper=str(gamma*F(strongest['physical_input_squared_norm'])),
  refined_actual_rank_38_projected_old_source_Gram_Loewner_upper=serialize(A),refined_parity_certificates=parity,
  refined_actual_rank_38_relative_bound_for_existing_22_source_inputs=str(bound),prior_RC71_relative_bound=str(prior),certified_fractional_upper_bound_reduction=str(1-bound/prior),
  refined_majorant_dominates_full_fixed_transfer_allowance=True,
  nominal_head_enlargement_alone_with_fixed_allowance_can_certify_inherited_budget=False,
  fixed_allowance_method_barrier_is_actual_leakage_lower_bound=False,
  actual_rank_38_scalar_budget_failure_proved=False,actual_1250_scalar_budget_failure_proved=False,
  actual_Riesz_error_directional_lower_bound_proved=False,thirty_eight_source_input_covariance_evaluated=False,
  enlarged_Weil_floor_certified=False,whole_aperture_positivity_obstructed=False,whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/n for n in ['rpb108_rc71_thirty_eight_projected_old_source.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json','rpb108_rc66_arch_multiplier_transport.json']]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==saved
  print('PASS: independent diagonal operator transport, scalar physical moments, Legendre witness congruence and exact refined Young comparisons')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
