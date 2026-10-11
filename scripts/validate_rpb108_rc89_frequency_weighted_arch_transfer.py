"""RC89: frequency-weighted Legendre arch remainder and source attachment.

The multiplier envelope is retained separately on each Fourier shell.
All infinite tails, source uncertainty and actual projection factors are paid.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,prod
import json,hashlib,sys
from validate_rpb108_rc30_interval_metric import I,PI
from validate_rpb108_rc42_native_signed_pole_head import outward
from validate_rpb108_rc74_projected_arch_transfer import atan_bounds
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,root
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,cong,relative
N=22;M=38;TERMS=12;B=F(11,10);RHO=F(252,257)
def diag(v):return [[x*F(i==j) for j in range(len(v))] for i,x in enumerate(v)]
def ceilgrid(x,q):return F(-((-x*q).numerator//(-x*q).denominator),q)
def serieslog(q):
 def small(t):
  y=(t-1)/(t+1);assert 0<=y<=F(1,3);n=80
  lo=2*sum((y**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
  return lo,lo+2*y**(2*n+1)/(F(2*n+1)*(1-y*y))
 k=0
 while q>=2:q/=2;k+=1
 lo,hi=small(q);a,b=small(F(2));return lo+k*a,hi+k*b

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];prior,fourier,direct,residual,source,enriched,head,native,archcert=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['milestone']=='RC88' and prior['status']=='PASS'
 assert [prior['input_sha256'][i] for i in [2,9,4,5,6,7,8]]==hashes[1:8]
 assert fourier['input_sha256'][3]==hashes[8]
 assert head['actual_orthogonal_projection_rank_certified']==M and prior['source_input_features']==list(range(N))
 tau=F(prior['canonical_complement_embedding_norm_upper']);s=tau**2/RHO
 K=F(archcert['prior_full_physical_arch_norm_upper']);assert K==F(643,100)
 elo,ehi=outward(I(1).exp(),10**30);pilo,pihi=outward(PI,10**30)
 assert list(map(str,[elo,ehi]))==prior['e_enclosure'] and list(map(str,[pilo,pihi]))==prior['pi_enclosure']
 if replay:
  ep=sum((F(1,factorial(j)) for j in range(101)),F(0));eu=ep+F(1,factorial(101))/(1-F(1,102));assert elo<=ep<=eu<=ehi
  a,b=atan_bounds(F(1,5));c,d=atan_bounds(F(1,239));assert pilo<=16*a-4*d<=16*b-4*c<=pihi
 D=[prod(range(1,2*n+2,2)) for n in range(M,M+TERMS+1)]
 if replay:assert all(D[j]==F(factorial(2*(M+j)+1),2**(M+j)*factorial(M+j)) for j in range(TERMS+1))
 multcache={}
 def high(L):
  if L not in multcache:
   q=1+ehi/L;lo,hi=outward(I(q).log(),10**40)
   if replay:
    rl,ru=serieslog(q);assert lo<=rl<=ru<=hi
   multcache[L]=hi+1/(2*L)
  return multcache[L]
 rows=[];candidates=[];accum=F(0)
 for k in range(1,91):
  a=F(k-1,20);b=F(k,20);finite=F(0)
  for j in range(TERMS):
   n=M+j;p=2*n+1
   difference=b**p-a**p
   if replay:
    alternate=(b-a)*sum((b**(p-1-l)*a**l for l in range(p)),F(0));assert alternate==difference
   finite+=4*B*(2*pihi*B)**(2*n)*difference/F(D[j])**2
  n=M+TERMS;z=2*pihi*B*b;r=z*z/F(2*n+3)**2;assert r<1
  tail=4*B*b*z**(2*n)/(F(D[-1])**2*(1-r))
  shell=ceilgrid(finite+tail,10**50);assert shell>=finite+tail>=0
  mult=K if a==0 else min(K,high(a));contribution=shell*mult**2;accum+=contribution
  rows.append(dict(lower_frequency=str(a),upper_frequency=str(b),retained_Legendre_terms=TERMS,first_omitted_degree=n,shell_plane_wave_remainder_Hilbert_Schmidt_squared_upper=str(shell),shell_arch_multiplier_norm_upper=str(mult),weighted_shell_Hilbert_Schmidt_squared_upper=str(contribution)))
  if k>=70:
   h=high(b);physical2=accum+h**2;beta=root(physical2,10**30)
   candidates.append(dict(frequency_cut=str(b),weighted_low_frequency_remainder_Hilbert_Schmidt_squared_upper=str(accum),high_frequency_multiplier_norm_upper=str(h),physical_arch_remainder_operator_norm_squared_upper=str(physical2),physical_arch_remainder_operator_norm_upper=str(beta)))
 best=min(candidates,key=lambda x:F(x['physical_arch_remainder_operator_norm_upper']));physical=F(best['physical_arch_remainder_operator_norm_upper']);assert physical**2>=F(best['physical_arch_remainder_operator_norm_squared_upper'])
 arch=root(tau**2*physical**2/RHO,10**30);oldarch=F(prior['projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho']);assert arch<oldarch
 prime=F(prior['projected_prime_physical_to_canonical_norm_upper_divided_by_sqrt_rho']);poles=list(map(F,prior['projected_pole_norm_uppers_divided_by_sqrt_rho']));effective=[arch+prime+x for x in poles]
 Ep=matrix(direct['actual_physical_Riesz_error_Gram_Loewner_upper']);V=matrix(enriched['enriched_native_trial_coefficients']);mass=list(map(F,enriched['physical_mass']))
 T=cong(V,diag(mass)) if not replay else [[sum((mass[k]*V[k][i]*V[k][j] for k in range(64)),F(0)) for j in range(N)] for i in range(N)]
 rawE=cong(diag([effective[i%2] for i in range(N)]),Ep);nu=F(1,65536);delta=F(source['actual_source_approximation_operator_error_upper'])
 E,eround=rounded_bound(add(scale(rawE,1+nu),T,(1+1/nu)*delta**2*s),1,10**24);Ec=scale(E,RHO);oldEc=matrix(prior['projected_canonical_source_transfer_Gram_Loewner_upper']);assert psd(Ec) and psd(add(oldEc,Ec,-1))
 W=matrix(residual['residual_certificates'][1]['nominal_physical_polynomial_residual_Gram_Loewner_upper']);nominal=scale(W,tau**2);assert nominal==matrix(prior['projected_nominal_polynomial_residual_Gram_Loewner_upper'])
 Mlo=matrix(enriched['enriched_actual_native_Gram_Loewner_lower']);oldA=matrix(prior['refined_actual_rank_38_projected_original_source_Gram_Loewner_upper'])
 def upper(ts):
  if replay:raw=[[RHO*((1+ts[i%2])*s*W[i][j]+(1+1/ts[i%2])*E[i][j]) for j in range(N)] for i in range(N)]
  else:raw=[[(1+ts[i%2])*nominal[i][j]+(1+1/ts[i%2])*Ec[i][j] for j in range(N)] for i in range(N)]
  return rounded_bound(raw,1,10**24)
 oldts=[F(x['Young_parameter']) for x in prior['parity_residual_certificates']];baseline=upper(oldts)[0];assert psd(add(oldA,baseline,-1))
 selected=[];parity=[]
 for p in range(2):
  tests=[]
  for t in [F(1,8),F(3,16),F(1,4),F(5,16),F(3,8),F(7,16),F(1,2),F(5,8),F(3,4)]:
   Ap=upper([t,t])[0];tests.append((relative(block(Ap,p),block(Mlo,p)),t))
  lam,t=min(tests);selected.append(t);parity.append(dict(parity='even' if p==0 else 'odd',Young_parameter=str(t),candidate_certificates=[dict(Young_parameter=str(ti),relative_upper=str(li)) for li,ti in tests]))
 A,ar=upper(selected);assert psd(A)
 for p in range(2):
  lam=relative(block(A,p),block(Mlo,p));parity[p]['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']=str(lam)
  if replay:
   Ci=inverse(block(matrix(native['chebyshev_to_legendre']),p));assert psd(cong(Ci,add(scale(block(Mlo,p),lam),block(A,p),-1)))
 bound=max(F(x['actual_rank_38_residual_relative_original_canonical_input_Gram_upper']) for x in parity);priorbound=F(prior['actual_rank_38_relative_bound_for_existing_22_source_inputs']);assert bound<priorbound
 result=dict(milestone='RC89',status='PASS',input_sha256=hashes,actual_Riesz_projection_head_rank=M,canonical_trial_dimension=64,source_input_features=list(range(N)),
  e_enclosure=list(map(str,[elo,ehi])),pi_enclosure=list(map(str,[pilo,pihi])),frequency_shell_step='1/20',arch_full_physical_multiplier_norm_upper=str(K),Legendre_degree=M,finite_Legendre_terms=TERMS,frequency_shell_certificates=rows,arch_remainder_cutoff_candidates=candidates,selected_arch_remainder_certificate=best,
  physical_frequency_weighted_arch_remainder_operator_norm_upper=str(physical),canonical_complement_embedding_norm_upper=str(tau),canonical_tail_norm_unchanged=True,
  projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho=str(arch),prior_projected_arch_norm_upper_divided_by_sqrt_rho=str(oldarch),arch_norm_fractional_upper_reduction=str(1-arch/oldarch),projected_prime_physical_to_canonical_norm_upper_divided_by_sqrt_rho=str(prime),projected_pole_norm_uppers_divided_by_sqrt_rho=list(map(str,poles)),prime_and_pole_constants_unchanged=True,
  weighted_shell_arch_transport_analytic_proof_supplied=True,infinite_Legendre_tail_paid_explicitly=True,actual_projection_polynomial_subtraction_used=True,low_and_high_frequency_outputs_not_assumed_orthogonal=True,
  projected_nominal_polynomial_residual_Gram_Loewner_upper=serialize(nominal),nominal_source_residual_upper_unchanged=True,projected_canonical_source_transfer_Gram_Loewner_upper=serialize(Ec),source_transfer_rounding_row_allowances=list(map(str,eround)),projected_transfer_whole_Loewner_improves_RC88=True,
  unchanged_Young_parameters_residual_upper=serialize(baseline),unchanged_parameters_whole_residual_Loewner_improvement_certified=True,refined_actual_rank_38_projected_original_source_Gram_Loewner_upper=serialize(A),source_rounding_row_allowances=list(map(str,ar)),final_source_whole_Loewner_improves_RC88=psd(add(oldA,A,-1)),parity_residual_certificates=parity,
  actual_rank_38_relative_bound_for_existing_22_source_inputs=str(bound),prior_retained_relative_bound=str(priorbound),certified_fractional_upper_bound_reduction=str(1-bound/priorbound),physical_source_and_Riesz_trials_unchanged=True,RC81_direct_Riesz_error_enclosure_unchanged=True,
  required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,thirty_eight_source_input_covariance_evaluated=False,enlarged_Weil_floor_certified=False,enlarged_complement_floor_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert result==saved
 return result
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 names=['rpb108_rc88_multiband_canonical_tail_transport.json','rpb108_rc78_legendre_fourier_transfer.json','rpb108_rc81_direct_enriched_riesz_residuals.json','rpb108_rc71_thirty_eight_projected_old_source.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc70_thirty_eight_native_projection.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc74_projected_arch_transfer.json']
 defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()))
  print('PASS: independent e/pi/log bounds, positive shell power differences and infinite tail closure; exact physical trial contraction, actual source attachment and parity congruences')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
