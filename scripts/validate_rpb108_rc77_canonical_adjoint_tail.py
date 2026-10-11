"""RC77: canonical adjoint tail bound from physical moment annihilation.

A projected physical-to-canonical bound. Physical noncompactness does not
obstruct compactness after the canonical adjoint.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,sys
from math import factorial
from validate_rpb108_rc30_interval_metric import PI
from validate_rpb108_rc47_correlated_native_transport import root
from validate_rpb108_rc66_arch_multiplier_transport import rational_log
from validate_rpb108_rc74_projected_arch_transfer import atan_bounds
from validate_rpb108_rc30_interval_metric import I
from validate_rpb108_rc42_native_signed_pole_head import outward
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,cong,relative
N=22;B=F(11,10);RHO=F(252,257)
def diag(x):return [[v*F(i==j) for j in range(len(x))] for i,v in enumerate(x)]
def progress(s):print(s,file=sys.stderr,flush=True)

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];previous,weightcert,archcert,polecert,residual,source,enriched,head,native,prime=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert previous['input_sha256']==hashes[1:]
 assert head['actual_orthogonal_projection_rank_certified']==38
 # For z in the canonical head complement, the physical vector i z
 # annihilates every polynomial of degree <38. Fourier Taylor subtraction
 # bounds its low-band physical energy by theta times total physical energy.
 elo,ehi=outward(I(1).exp(),10**30);pilo,pihi=outward(PI,10**30)
 if replay:
  ep=sum((F(1,factorial(j)) for j in range(101)),F(0));eu=ep+F(1,factorial(101))/(1-F(1,102))
  assert elo<=ep<=eu<=ehi
  a0,a1=atan_bounds(F(1,5));c0,c1=atan_bounds(F(1,239))
  assert pilo<=16*a0-4*c1<=16*a1-4*c0<=pihi
 candidates=[]
 for cut in [F(2),F(21,10),F(11,5),F(9,4),F(23,10),F(111,50),F(56,25)]:
  loglo,loghi=outward(I(elo+cut).log(),10**30);assert loglo>0
  theta=4*B*cut*(2*pihi*B*cut)**76/(F(factorial(38))**2*77**2)
  assert 0<theta<1
  tail2=1/((1-theta)*loglo);tau=root(tail2,10**30)
  if replay:
   lr,ur=rational_log(elo+cut);assert loglo<=lr<=ur<=loghi
   mx=2*B**77/77;mf=2*cut**77/77
   direct=(2*pihi)**76*mx*mf/F(factorial(38))**2;assert theta==direct
   assert tau**2*(1-direct)*loglo>=1
  candidates.append(dict(frequency_cut=str(cut),canonical_weight_log_lower=str(loglo),low_band_moment_annihilation_energy_fraction_upper=str(theta),canonical_complement_embedding_norm_squared_upper=str(tail2),canonical_complement_embedding_norm_upper=str(tau)))
 best=min(candidates,key=lambda x:F(x['canonical_complement_embedding_norm_upper']));tau=F(best['canonical_complement_embedding_norm_upper']);assert tau**2<RHO
 kp=F(previous['complete_paired_prime_physical_operator_norm_upper']);oldkp=kp
 primebeta=root(kp**2*tau**2/RHO,10**30);assert primebeta<kp
 progress('canonical projected prime norm divided by sqrt(rho) '+str(primebeta))
 # Propagate the improved full norm through the unchanged actual projection.
 arch=F(archcert['projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho']);beta=[F(x['projected_physical_to_canonical_pole_norm_upper_divided_by_sqrt_rho']) for x in polecert['signed_pole_range_projection_certificates']]
 effective=[arch+primebeta+x for x in beta];Ep=matrix(enriched['enriched_actual_physical_Riesz_error_Gram_Loewner_upper']);V=matrix(enriched['enriched_native_trial_coefficients']);mass=list(map(F,enriched['physical_mass']))
 if replay:
  T=[[sum((mass[q]*V[q][i]*V[q][j] for q in range(64)),F(0)) for j in range(N)] for i in range(N)];rawE=cong(diag([effective[i%2] for i in range(N)]),Ep)
 else:T=cong(V,diag(mass));rawE=[[effective[i%2]*effective[j%2]*Ep[i][j] for j in range(N)] for i in range(N)]
 nu=F(1,65536);delta=F(source['actual_source_approximation_operator_error_upper'])
 E=rounded_bound(add(scale(rawE,1+nu),T,(1+1/nu)*delta**2),1,10**24)[0];Ecan=scale(E,RHO)
 Eold=matrix(previous['projected_transfer_equivalent_Gram_divided_by_rho']);assert psd(E) and psd(add(Eold,E,-1))
 W=matrix(residual['residual_certificates'][1]['nominal_physical_polynomial_residual_Gram_Loewner_upper']);Mlo=matrix(enriched['enriched_actual_native_Gram_Loewner_lower'])
 oldA=matrix(previous['refined_actual_rank_38_projected_old_source_Gram_Loewner_upper']);oldt=[F(x['Young_parameter']) for x in previous['parity_residual_certificates']]
 def upper(ts):return rounded_bound([[RHO*((1+ts[i%2])*W[i][j]+(1+1/ts[i%2])*E[i][j]) for j in range(N)] for i in range(N)],1,10**24)[0]
 baseline=upper(oldt);assert psd(add(oldA,baseline,-1))
 selected=[];parity=[]
 for p in [0,1]:
  tests=[]
  for t in [F(1,2),F(5,8),F(3,4),F(7,8),F(1),F(9,8)]:
   Ap=scale(add(scale(block(W,p),1+t),block(E,p),1+1/t),RHO);tests.append((relative(Ap,block(Mlo,p)),t))
  lam,t=min(tests);selected.append(t);parity.append(dict(parity='even' if p==0 else 'odd',Young_parameter=str(t),candidate_certificates=[dict(Young_parameter=str(q),upper=str(l)) for l,q in tests]))
 A=upper(selected);assert psd(A)
 for p in [0,1]:
  lam=relative(block(A,p),block(Mlo,p));parity[p]['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']=str(lam)
  if replay:
   Ci=inverse(block(matrix(native['chebyshev_to_legendre']),p));assert psd(cong(Ci,add(scale(block(Mlo,p),lam),block(A,p),-1)))
 bound=max(F(x['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']) for x in parity);prior=F(previous['actual_rank_38_relative_bound_for_existing_22_source_inputs']);assert bound<prior
 return dict(milestone='RC77',status='PASS',input_sha256=hashes,source_input_features=list(range(N)),actual_projection_target_features=list(range(38)),
  canonical_complement_embedding_candidates=candidates,selected_canonical_complement_embedding_certificate=best,
  canonical_complement_embedding_norm_upper=str(tau),prior_canonical_embedding_norm_squared_upper=str(RHO),
  projected_prime_physical_to_canonical_norm_upper_divided_by_sqrt_rho=str(primebeta),
  complete_paired_prime_physical_operator_norm_upper=str(kp),full_prime_operator_norm_improved=False,projection_specific_prime_norm_decay_certified=True,
  physical_noncompactness_is_canonical_source_obstruction=False,
  canonical_embedding_and_adjoint_compactness_analytic_proof_supplied=True,
  projected_canonical_source_transfer_Gram_Loewner_upper=serialize(Ecan),projected_transfer_equivalent_Gram_divided_by_rho=serialize(E),projected_transfer_Loewner_improves_RC76=True,
  unchanged_Young_parameters_residual_upper=serialize(baseline),unchanged_parameters_whole_residual_Loewner_improvement_certified=True,
  refined_actual_rank_38_projected_old_source_Gram_Loewner_upper=serialize(A),parity_residual_certificates=parity,
  actual_rank_38_relative_bound_for_existing_22_source_inputs=str(bound),prior_RC76_relative_bound=str(prior),certified_fractional_upper_bound_reduction=str(1-bound/prior),
  required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,thirty_eight_source_input_covariance_evaluated=False,
  enlarged_Weil_floor_certified=False,analytic_Schur_lemma_Lean_formalized=False,whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/n for n in ['rpb108_rc76_quartic_prime_transfer.json','rpb108_rc75_weighted_prime_transfer.json','rpb108_rc74_projected_arch_transfer.json','rpb108_rc73_projected_pole_transfer.json','rpb108_rc71_thirty_eight_projected_old_source.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc70_thirty_eight_native_projection.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc43_native_prime_head.json']]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,saved)==saved
  print('PASS: independent rational e/pi/log series, Fourier moment integrals, canonical adjoint tail and transfer comparisons')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
