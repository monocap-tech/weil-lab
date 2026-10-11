"""RC88: frequency-layer canonical tail coercivity and actual source transport.

Integrate nested Fourier energy bounds using a rational lower staircase.
This strengthens the same rank-38 complement map; source count stays 22.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,prod
import hashlib,json,sys
from validate_rpb108_rc30_interval_metric import I,PI
from validate_rpb108_rc42_native_signed_pole_head import outward
from validate_rpb108_rc74_projected_arch_transfer import atan_bounds
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,root
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,cong,relative
N=22;M=38;B=F(11,10);RHO=F(252,257)
def diag(v):return [[x*F(i==j) for j in range(len(v))] for i,x in enumerate(v)]
def ceilgrid(x,q):return F(-((-x*q).numerator//(-x*q).denominator),q)
def floorgrid(x,q):return F((x*q).numerator//(x*q).denominator,q)
def logbounds(q):
 # Positive atanh series, with an exact geometric tail.
 y=(q-1)/(q+1);assert 0<y<F(1,100);n=24
 lo=2*sum((y**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
 return lo,lo+2*y**(2*n+1)/(F(2*n+1)*(1-y*y))
def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths]
 prior,old,fourier,transport,residual,source,enriched,head,native,direct=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['milestone']=='RC87' and prior['input_sha256'][2:4]==[hashes[6],hashes[1]]
 assert [old['input_sha256'][i] for i in range(7)]==[hashes[i] for i in [9,3,6,5,4,8,7]]
 assert transport['input_sha256']==[hashes[i] for i in [2,4,5,6,7,8]]+[transport['input_sha256'][6]]
 assert head['actual_orthogonal_projection_rank_certified']==M
 assert old['source_input_features']==list(range(N))
 oldtau=F(old['canonical_complement_embedding_norm_upper']);assert oldtau==F(fourier['canonical_complement_embedding_norm_upper'])==F(transport['canonical_complement_embedding_norm_upper'])
 elo,ehi=outward(I(1).exp(),10**30);pilo,pihi=outward(PI,10**30)
 df=prod(range(1,2*M+2,2));assert str(df)==fourier['odd_double_factorial']
 if replay:
  ep=sum((F(1,factorial(j)) for j in range(101)),F(0));eu=ep+F(1,factorial(101))/(1-F(1,102));assert elo<=ep<=eu<=ehi
  a,b=atan_bounds(F(1,5));c,d=atan_bounds(F(1,239));assert pilo<=16*a-4*d<=16*b-4*c<=pihi
  assert df==F(factorial(2*M+1),2**M*factorial(M))
 rows=[];prev=F(0);energy=F(1);lasttheta=F(0)
 for k in range(1,451):
  cut=F(k,100);z=2*pihi*B*cut;r=z*z/F(2*M+3)**2;assert r<1
  leading=4*B*cut*z**(2*M)/F(df)**2;theta=leading/(1-r)
  th=min(F(1),ceilgrid(theta,10**50));assert lasttheta<=th<=1
  # The logarithmic weight increment decreases with e, hence ehi.
  q=(ehi+cut)/(ehi+prev);lo,hi=outward(I(q).log(),10**40);assert lo>0
  if replay:
   rl,ru=logbounds(q);assert lo<=rl<=ru<=hi
   integrated=B*F(2*M+1,2)*F(4,df**2)*(2*pihi*B)**(2*M)*2*cut**(2*M+1)/F(2*M+1)
   assert leading==integrated and theta*(1-r)==integrated and th>=min(F(1),theta)
  term=lo*(1-th);energy+=term
  rows.append(dict(frequency_cut=str(cut),cumulative_physical_Fourier_energy_fraction_upper=str(th),canonical_weight_increment_lower=str(lo),canonical_energy_lower_contribution=str(term)))
  prev=cut;lasttheta=th
  if th==1:break
 assert len(rows)>400 and lasttheta==1
 tail2=1/energy;tau=root(tail2,10**30);assert tau**2*energy>=1 and tau<oldtau
 if replay:
  # Independent telescoping staircase: a point with |xi| in shell j
  # receives exactly the sum of all completed weight increments.
  levels=[];h=F(1)
  for row in rows:h+=F(row['canonical_weight_increment_lower']);levels.append(h)
  alternate=levels[-1]
  for j,row in enumerate(rows):alternate-=F(row['canonical_weight_increment_lower'])*F(row['cumulative_physical_Fourier_energy_fraction_upper'])
  assert alternate==energy
 gamma=tau/oldtau;s=tau**2/RHO;assert 0<gamma<1
 oldarch=F(old['projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho']);oldprime=F(old['projected_prime_physical_to_canonical_norm_upper_divided_by_sqrt_rho']);oldpoles=list(map(F,old['projected_pole_norm_uppers_divided_by_sqrt_rho']))
 assert oldarch==F(transport['projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho']) and oldprime==F(transport['projected_prime_physical_to_canonical_norm_upper_divided_by_sqrt_rho']) and oldpoles==list(map(F,transport['projected_pole_norm_uppers_divided_by_sqrt_rho']))
 arch=gamma*oldarch;prime=gamma*oldprime;poles=[gamma*x for x in oldpoles];effective=[arch+prime+x for x in poles]
 Ep=matrix(direct['actual_physical_Riesz_error_Gram_Loewner_upper']);assert Ep==matrix(old['physical_Riesz_error_Gram_Loewner_upper'])
 V=matrix(enriched['enriched_native_trial_coefficients']);mass=list(map(F,enriched['physical_mass']))
 T=cong(V,diag(mass)) if not replay else [[sum((mass[k]*V[k][i]*V[k][j] for k in range(64)),F(0)) for j in range(N)] for i in range(N)]
 rawE=cong(diag([effective[i%2] for i in range(N)]),Ep);nu=F(1,65536);delta=F(source['actual_source_approximation_operator_error_upper'])
 E,eround=rounded_bound(add(scale(rawE,1+nu),T,(1+1/nu)*delta**2*s),1,10**24);Ec=scale(E,RHO)
 oldEc=matrix(old['projected_canonical_source_transfer_Gram_Loewner_upper']);assert psd(Ec) and psd(add(oldEc,Ec,-1))
 W=matrix(residual['residual_certificates'][1]['nominal_physical_polynomial_residual_Gram_Loewner_upper']);nominal=scale(W,tau**2)
 assert scale(W,oldtau**2)==matrix(old['projected_nominal_polynomial_residual_Gram_Loewner_upper']) and psd(W)
 Mlo=matrix(enriched['enriched_actual_native_Gram_Loewner_lower']);oldA=matrix(old['refined_actual_rank_38_projected_old_source_Gram_Loewner_upper'])
 def upper(ts):
  if replay:raw=[[RHO*((1+ts[i%2])*s*W[i][j]+(1+1/ts[i%2])*E[i][j]) for j in range(N)] for i in range(N)]
  else:raw=[[(1+ts[i%2])*nominal[i][j]+(1+1/ts[i%2])*Ec[i][j] for j in range(N)] for i in range(N)]
  return rounded_bound(raw,1,10**24)
 oldts=[F(x['Young_parameter']) for x in old['parity_residual_certificates']];baseline=upper(oldts)[0];assert psd(add(oldA,baseline,-1))
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
 result=dict(milestone='RC88',status='PASS',input_sha256=hashes,actual_Riesz_projection_head_rank=M,canonical_trial_dimension=64,source_input_features=list(range(N)),
  Fourier_convention='exp(-2*pi*i*xi*x)',canonical_weight='log(e+abs(xi))',frequency_step='1/100',odd_double_factorial=str(df),e_enclosure=list(map(str,[elo,ehi])),pi_enclosure=list(map(str,[pilo,pihi])),frequency_layer_certificates=rows,
  canonical_energy_relative_physical_energy_lower=str(energy),canonical_complement_embedding_norm_squared_upper=str(tail2),canonical_complement_embedding_norm_upper=str(tau),prior_canonical_complement_embedding_norm_upper=str(oldtau),tail_norm_ratio=str(gamma),squared_tail_to_global_embedding_ratio=str(s),
  multi_frequency_layer_coercivity_analytic_proof_supplied=True,actual_canonical_projection_complement_used=True,prime_bound_receives_no_duplicate_tail_factor=True,
  projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho=str(arch),projected_prime_physical_to_canonical_norm_upper_divided_by_sqrt_rho=str(prime),projected_pole_norm_uppers_divided_by_sqrt_rho=list(map(str,poles)),
  projected_nominal_polynomial_residual_Gram_Loewner_upper=serialize(nominal),projected_canonical_source_transfer_Gram_Loewner_upper=serialize(Ec),source_transfer_rounding_row_allowances=list(map(str,eround)),projected_transfer_whole_Loewner_improves_RC82=True,
  unchanged_Young_parameters_residual_upper=serialize(baseline),unchanged_parameters_whole_residual_Loewner_improvement_certified=True,refined_actual_rank_38_projected_original_source_Gram_Loewner_upper=serialize(A),source_rounding_row_allowances=list(map(str,ar)),final_source_whole_Loewner_improves_RC82=psd(add(oldA,A,-1)),parity_residual_certificates=parity,
  actual_rank_38_relative_bound_for_existing_22_source_inputs=str(bound),prior_retained_relative_bound=str(priorbound),certified_fractional_upper_bound_reduction=str(1-bound/priorbound),
  physical_source_and_Riesz_trials_unchanged=True,RC81_direct_Riesz_error_enclosure_unchanged=True,required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,thirty_eight_source_input_covariance_evaluated=False,enlarged_Weil_floor_certified=False,enlarged_complement_floor_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert result==saved
 return result
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 names=['rpb108_rc87_fixed_space_response_and_fusion_audit.json','rpb108_rc82_direct_error_source_attachment.json','rpb108_rc78_legendre_fourier_transfer.json','rpb108_rc79_uniform_adjoint_tail_transport.json','rpb108_rc71_thirty_eight_projected_old_source.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc70_thirty_eight_native_projection.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc81_direct_enriched_riesz_residuals.json']
 defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()))
  print('PASS: independent e/pi/log bounds, integrated Legendre term and telescoping frequency layers; exact physical trial contraction, actual source assembly and parity congruences')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
