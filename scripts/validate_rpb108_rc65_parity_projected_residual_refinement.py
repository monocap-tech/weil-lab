"""RC65: exact parity-aware refinement of the actual rank-22 residual bound.

Fixed rational Young parameters; floating optimization is not proof evidence.
Replay checks equivalent diagonal congruences and comparisons in Legendre coordinates.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
N=22

def add(A,B,s=F(1)):return [[x+s*y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,s):return [[s*x for x in r] for r in A]
def block(A,p):return [[A[i][j] for j in range(p,N,2)] for i in range(p,N,2)]
def cong(C,A):return mm(mm(tr(C),A),C)
def relative(A,B):
 high=F(1)
 while not psd(add(scale(B,high),A,-1)):high*=2
 low=F(0) if high==1 else high/2
 for _ in range(12):
  mid=(low+high)/2
  if psd(add(scale(B,mid),A,-1)):high=mid
  else:low=mid
 assert psd(add(scale(B,high),A,-1))
 return high

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];native,residual,source,projection,weak=[json.loads(x) for x in raw]
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [projection['input_sha256'][k] for k in [1,2,4,5]]==[hashes[k] for k in [0,1,2,4]]
 assert source['input_sha256'][1:3]==hashes[:2]
 assert weak['input_sha256'][0:2]==hashes[:2] and weak['input_sha256'][3]==hashes[2]
 assert projection['actual_rank_22_projection_residual_upper_certified']
 M=matrix(native['actual_canonical_native_Gram_Loewner_lower']);P=matrix(native['physical_native_Gram']);C=matrix(native['chebyshev_to_legendre'])
 Ep=matrix(residual['actual_physical_Riesz_error_Gram_Loewner_upper']);T=matrix(native['physical_native_trial_Gram'])
 Y=matrix(projection['nominal_variational_residual_Gram_Loewner_upper']);EL=matrix(projection['canonical_Riesz_error_coefficient_Gram_Loewner_upper'])
 assert all(psd(A) for A in [M,P,Ep,T,Y,EL])
 assert all(A[i][j]==0 for A in [M,P,Ep,T,Y,EL] for i in range(N) for j in range(N) if (i-j)%2)
 rho=F(252,257);delta=F(source['actual_source_approximation_operator_error_upper']);k=list(map(F,source['complete_physical_operator_parity_norm_upper']))
 v=F(1,65536);u=F(1,16);ts=[F(2),F(3,2)]
 A=[[F(0)]*N for _ in range(N)];physical=[[F(0)]*N for _ in range(N)];error=[[F(0)]*N for _ in range(N)]
 for i in range(N):
  for j in range(N):
   if (i-j)%2:continue
   p=i%2;physical[i][j]=(1+v)*k[p]**2*Ep[i][j]+(1+1/v)*delta**2*T[i][j]
 if replay:
  S=[[k[i%2]*(i==j) for j in range(N)] for i in range(N)]
  assert physical==add(scale(cong(S,Ep),1+v),T,(1+1/v)*delta**2)
 physical=rounded_bound(physical,1,10**24)[0]
 error=rounded_bound(add(scale(physical,rho*(1+u)),EL,1+1/u),1,10**24)[0]
 for i in range(N):
  for j in range(N):
   t=ts[i%2];A[i][j]=(1+t)*Y[i][j]+(1+1/t)*error[i][j]
 A=rounded_bound(A,1,10**24)[0]
 assert all(psd(B) for B in [physical,error,A])
 rows=[]
 for p in range(2):
  Ap=block(A,p);Mp=block(M,p);Pp=block(P,p)
  lam=relative(Ap,Mp);physical_lam=relative(Ap,Pp)
  components={label:str(relative(block(B,p),Mp)) for label,B in [('nominal_variational_residual',Y),('source_transfer_physical',physical),('canonical_representative_error',EL),('combined_variational_error',error)]}
  if replay:
   # Invert only the exact Chebyshev/Legendre polynomial coordinate map.
   CI=inverse(block(C,p));compare=add(scale(Mp,lam),Ap,-1)
   assert psd(cong(CI,compare)) and psd(cong(CI,add(scale(Pp,physical_lam),Ap,-1)))
   for label,B in [('nominal_variational_residual',Y),('source_transfer_physical',physical),('canonical_representative_error',EL),('combined_variational_error',error)]:
    assert psd(cong(CI,add(scale(Mp,F(components[label])),block(B,p),-1)))
  rows.append(dict(parity='even' if p==0 else 'odd',source_approximation_Young_parameter=str(v),source_representative_Young_parameter=str(u),nominal_error_Young_parameter=str(ts[p]),actual_projected_residual_relative_canonical_Gram_upper=str(lam),actual_projected_residual_relative_physical_Gram_upper=str(physical_lam),component_relative_canonical_Gram_uppers=components))
 bound=max(F(r['actual_projected_residual_relative_canonical_Gram_upper']) for r in rows)
 prior=F(projection['actual_projected_source_relative_canonical_native_Gram_upper']);ceiling=F(weak['scalar_Schur_source_budget_strict_ceiling_using_inherited_complement_floor'])
 assert bound<F(183,10) and prior/bound>4 and psd(add(scale(M,bound),A,-1))
 return dict(milestone='RC65',status='PASS',input_sha256=hashes,native_features_certified=list(range(N)),
  projection_target=projection['projection_target'],parity_residual_certificates=rows,
  refined_actual_source_transfer_physical_Gram_Loewner_upper=serialize(physical),
  refined_combined_variational_error_Gram_Loewner_upper=serialize(error),
  refined_actual_rank_22_projected_source_residual_Gram_Loewner_upper=serialize(A),
  actual_rank_22_projected_source_relative_canonical_native_Gram_upper=str(bound),
  prior_RC64_projected_source_relative_canonical_native_Gram_upper=str(prior),
  prior_to_refined_uniform_bound_ratio=str(prior/bound),
  uniform_bound_fractional_reduction=str(1-bound/prior),
  strict_scalar_Schur_budget_ceiling_from_RC63=str(ceiling),
  refined_upper_to_required_budget_ceiling_ratio=str(bound/ceiling),
  refined_uniform_comparison_uses_actual_canonical_Gram_lower_matrix=True,
  matrix_Loewner_dominance_over_RC64_claimed=False,
  actual_rank_22_projected_source_residual_upper_certified=True,
  exact_actual_projection_coefficients_evaluated=False,required_projected_source_budget_certified=False,
  actual_projected_source_budget_failure_proved=False,uniform_twenty_two_positive_Weil_floor_certified=False,
  whole_aperture_positivity_extended=False,RH=False,F4=False)
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/n for n in ['rpb108_rc59_twenty_two_native_projection.json','rpb108_rc60_twenty_two_mixed_residuals.json','rpb108_rc62_twenty_two_original_source_covariance.json','rpb108_rc64_twenty_two_projected_source_residual.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json']]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==saved
  print('PASS: independent transfer congruence and Legendre-coordinate exact PSD replay of both parity residual and component comparisons')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
