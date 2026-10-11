"""RC74: projected archimedean multiplier via Fourier polynomial subtraction.

Low-frequency output is approximated by degree-37 polynomials whose Riesz
images belong exactly to Pi38. High frequencies use the RC66 Euler bound.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import hashlib,json,sys
from validate_rpb108_rc30_interval_metric import I,PI
from validate_rpb108_rc42_native_signed_pole_head import outward
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,root
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,cong,relative
from validate_rpb108_rc66_arch_multiplier_transport import rational_log
N=22;HEAD=38;B=F(11,10);R=2*B;RHO=F(252,257)
def diag(x):return [[v*F(i==j) for j in range(len(x))] for i,v in enumerate(x)]
def quad(v,A):return sum((x*y*A[i][j] for i,x in enumerate(v) for j,y in enumerate(v)),F(0))
def atan_bounds(x):
 n=100;s=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
 return s,s+x**(2*n+1)/F(2*n+1)
def progress(s):print(s,file=sys.stderr,flush=True)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];previous,residual,source,enriched,head,native,prime,transport=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [previous['input_sha256'][k] for k in [0,2,3,4,5,6,8]]==hashes[1:]
 assert [residual['input_sha256'][k] for k in [0,1,2,4,6,7]]==[hashes[k] for k in [4,3,5,6,2,7]]
 assert [source['input_sha256'][k] for k in [0,1,3,6]]==[hashes[k] for k in [3,5,6,7]]
 assert head['actual_orthogonal_projection_rank_certified']==HEAD
 ka=F(transport['certified_physical_archimedean_remainder_norm_upper']);assert ka==F(643,100)
 kp=F(prime['full_paired_prime_physical_operator_norm_upper'])
 elo,ehi=outward(I(1).exp(),10**30);pilo,pihi=outward(PI,10**30)
 assert pilo*pilo*elo*elo>F(1,16)
 if replay:
  ep=sum((F(1,factorial(j)) for j in range(101)),F(0));eu=ep+F(1,factorial(101))/(1-F(1,102))
  assert elo<=ep<=eu<=ehi
  a0,a1=atan_bounds(F(1,5));c0,c1=atan_bounds(F(1,239))
  assert pilo<=16*a0-4*c1<=16*a1-4*c0<=pihi
 candidates=[]
 for cut in [F(2),F(41,20),F(21,10),F(43,20),F(11,5)]:
  loglo,loghi=outward(I(1+ehi/cut).log(),10**30)
  high=loghi+1/(2*cut)
  # Integrate the squared real-axis exponential Taylor remainder.
  low2=ka**2*4*B*cut*(2*pihi*B*cut)**(2*HEAD)/(F(factorial(HEAD))**2*F(2*HEAD+1)**2)
  beta=root(low2+high**2,10**30)
  assert beta**2>=low2+high**2 and beta<ka
  if replay:
   lr,ur=rational_log(1+ehi/cut);assert loglo<=lr<=ur<=loghi
   mx=2*B**(2*HEAD+1)/F(2*HEAD+1);mf=2*cut**(2*HEAD+1)/F(2*HEAD+1)
   direct=ka**2*(2*pihi)**(2*HEAD)*mx*mf/F(factorial(HEAD))**2
   assert direct==low2
   assert beta**2>=direct+high**2
  candidates.append(dict(frequency_cut=str(cut),logarithm_enclosure=[str(loglo),str(loghi)],high_frequency_multiplier_modulus_upper=str(high),
   low_frequency_polynomial_remainder_operator_norm_squared_upper=str(low2),projected_arch_norm_upper_divided_by_sqrt_rho=str(beta)))
 best=min(candidates,key=lambda x:F(x['projected_arch_norm_upper_divided_by_sqrt_rho']));archbeta=F(best['projected_arch_norm_upper_divided_by_sqrt_rho'])
 progress('projected archimedean norm '+str(archbeta))
 polebeta=[F(x['projected_physical_to_canonical_pole_norm_upper_divided_by_sqrt_rho']) for x in previous['signed_pole_range_projection_certificates']]
 effective=[archbeta+kp+x for x in polebeta]
 Ep=matrix(enriched['enriched_actual_physical_Riesz_error_Gram_Loewner_upper']);V=matrix(enriched['enriched_native_trial_coefficients']);mass=list(map(F,enriched['physical_mass']))
 if replay:
  T=[[sum((mass[a]*V[a][i]*V[a][j] for a in range(64)),F(0)) for j in range(N)] for i in range(N)]
  raw=cong(diag([effective[i%2] for i in range(N)]),Ep)
 else:
  T=cong(V,diag(mass));raw=[[effective[i%2]*effective[j%2]*Ep[i][j] for j in range(N)] for i in range(N)]
 nu=F(1,65536);delta=F(source['actual_source_approximation_operator_error_upper'])
 Eequiv=rounded_bound(add(scale(raw,1+nu),T,(1+1/nu)*delta**2),1,10**24)[0];Ecan=scale(Eequiv,RHO)
 Eold=matrix(previous['projected_transfer_equivalent_Gram_divided_by_rho']);assert psd(Eequiv) and psd(add(Eold,Eequiv,-1))
 W=matrix(residual['residual_certificates'][1]['nominal_physical_polynomial_residual_Gram_Loewner_upper']);Mlo=matrix(enriched['enriched_actual_native_Gram_Loewner_lower'])
 oldA=matrix(previous['refined_actual_rank_38_projected_old_source_Gram_Loewner_upper']);oldt=[F(x['Young_parameter']) for x in previous['parity_residual_certificates']]
 def upper(ts):return rounded_bound([[RHO*((1+ts[i%2])*W[i][j]+(1+1/ts[i%2])*Eequiv[i][j]) for j in range(N)] for i in range(N)],1,10**24)[0]
 baseline=upper(oldt);assert psd(add(oldA,baseline,-1))
 selected=[];parity=[]
 grid=[F(1,2),F(5,8),F(3,4),F(7,8),F(1),F(9,8),F(5,4),F(3,2)]
 for p in [0,1]:
  tests=[]
  for t in grid:
   Ap=scale(add(scale(block(W,p),1+t),block(Eequiv,p),1+1/t),RHO)
   tests.append((relative(Ap,block(Mlo,p)),t))
  lam,t=min(tests);selected.append(t)
  parity.append(dict(parity='even' if p==0 else 'odd',Young_parameter=str(t),effective_transfer_norm_upper_divided_by_sqrt_rho=str(effective[p]),candidate_certificates=[dict(Young_parameter=str(q),upper=str(l)) for l,q in tests]))
 A=upper(selected);assert psd(A) and psd(add(A,Ecan,-1))
 for p in [0,1]:
  lam=relative(block(A,p),block(Mlo,p));parity[p]['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']=str(lam)
  if replay:
   Ci=inverse(block(matrix(native['chebyshev_to_legendre']),p));assert psd(cong(Ci,add(scale(block(Mlo,p),lam),block(A,p),-1)))
   assert psd(cong(Ci,block(add(oldA,baseline,-1),p)))
 bound=max(F(x['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']) for x in parity)
 prior=F(previous['actual_rank_38_relative_bound_for_existing_22_source_inputs']);assert bound<prior
 progress('actual rank-38 residual upper '+str(bound))
 return dict(milestone='RC74',status='PASS',input_sha256=hashes,source_input_features=list(range(N)),actual_projection_target_features=list(range(HEAD)),
  Fourier_convention='exp(-2*pi*i*xi*x)',polynomial_subtraction_degree=HEAD-1,
  analytic_high_frequency_arch_bound='abs(m_arch(xi)) <= log(1+e/abs(xi))+1/(2*abs(xi)), xi!=0',
  real_axis_plane_wave_Taylor_remainder='abs(exp(i*t)-sum_{n=0}^{37}(i*t)^n/n!) <= abs(t)^38/38!',
  low_high_input_orthogonality_norm_combination='beta_arch^2 >= low_Hilbert_Schmidt_norm_upper^2 + high_multiplier_norm_upper^2',
  e_enclosure=[str(elo),str(ehi)],pi_enclosure=[str(pilo),str(pihi)],frequency_split_candidates=candidates,selected_frequency_split_certificate=best,
  prior_full_physical_arch_norm_upper=str(ka),projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho=str(archbeta),
  polynomial_subtraction_maps_exactly_into_actual_native_head=True,projected_archimedean_transfer_certified=True,
  projected_pole_allowance_retained=True,full_prime_operator_norm_retained=str(kp),projected_prime_transfer_sharpened=False,
  projected_canonical_source_transfer_Gram_Loewner_upper=serialize(Ecan),projected_transfer_equivalent_Gram_divided_by_rho=serialize(Eequiv),
  projected_transfer_Loewner_improves_RC73=True,unchanged_Young_parameters_residual_upper=serialize(baseline),unchanged_parameters_whole_residual_Loewner_improvement_certified=True,
  refined_actual_rank_38_projected_old_source_Gram_Loewner_upper=serialize(A),parity_residual_certificates=parity,
  actual_rank_38_relative_bound_for_existing_22_source_inputs=str(bound),prior_RC73_relative_bound=str(prior),certified_fractional_upper_bound_reduction=str(1-bound/prior),
  full_physical_arch_operator_norm_replaced=False,exact_actual_projection_coefficients_evaluated=False,
  required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,
  thirty_eight_source_input_covariance_evaluated=False,enlarged_Weil_floor_certified=False,analytic_projection_lemma_Lean_formalized=False,
  whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/n for n in ['rpb108_rc73_projected_pole_transfer.json','rpb108_rc71_thirty_eight_projected_old_source.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc70_thirty_eight_native_projection.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc43_native_prime_head.json','rpb108_rc66_arch_multiplier_transport.json']]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==saved
  print('PASS: independent rational e/pi/log series, exact Fourier remainder moments, projected arch transfer and canonical matrix congruence replay')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
