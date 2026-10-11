"""RC64: paid variational upper bound for the actual rank-22 source residual.

Generation expands the residual; replay independently completes its square.
Actual projection coefficients are never identified with rational trial solves.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,entries,serialize,product
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
N=22

def add(A,B,s=F(1)):
 return [[A[i][j]+s*B[i][j] for j in range(N)] for i in range(N)]
def scale(A,s):return [[s*x for x in row] for row in A]
def rounded(A):return [[F(round(x*10**20),10**20) for x in row] for row in A]
def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];metric,native,residual,head,source,weak=[json.loads(x) for x in raw]
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert source['input_sha256'][:4]==hashes[:4]
 assert weak['input_sha256'][:4]==hashes[1:5]
 V=matrix(native['native_trial_coefficients']);C=matrix(native['chebyshev_to_legendre'])
 D=list(map(F,metric['physical_mass']));G=matrix(metric['metric_center'])
 P=matrix(native['physical_native_Gram']);T=matrix(native['physical_native_trial_Gram'])
 GT=mm(mm(tr(V),G),V)
 X=[[D[i]*C[i][j] if i<N else F(0) for j in range(N)] for i in range(32)]
 J=mm(tr(X),V)
 arch=entries(head['nominal_arch_trial_head_entry_enclosures']);prime=entries(head['nominal_prime_trial_head_entry_enclosures'])
 moments=[tuple(map(F,x)) for x in head['nominal_trial_pole_moment_enclosures']]
 H0=[[F(0)]*N for _ in range(N)];Rh=[[F(0)]*N for _ in range(N)]
 for i in range(N):
  for j in range(N):
   if (i-j)%2:continue
   a,b=arch[tuple(sorted((i,j)))];c,d=prime[tuple(sorted((i,j)))];e,f=product(moments[i],moments[j])
   sign=2*(-1)**(i%2);e,f=sorted([sign*e,sign*f])
   lo=J[j][i]+a-GT[i][j]+c+e;hi=J[j][i]+b-GT[i][j]+d+f
   H0[i][j]=(lo+hi)/2;Rh[i][j]=(hi-lo)/2
 # Keep finite rational enclosures; pay every center rounding in its radius.
 for i in range(N):
  for j in range(N):
   center=F(round(H0[i][j]*10**24),10**24)
   radius=Rh[i][j]+abs(center-H0[i][j]);q=radius*10**24
   Rh[i][j]=F(-(-q.numerator//q.denominator),10**24);H0[i][j]=center
 rho=F(252,257);alpha=F(native['actual_canonical_native_Gram_physical_lower_factor'])
 deltaG=F(native['actual_metric_error_upper_used'])
 Gup=rounded_bound(add(GT,T,deltaG),1,10**24)[0];GI=inverse(Gup)
 L=rounded(mm(GI,H0));Z=[[abs(x) for x in row] for row in L]
 B=mm(tr(Z),Rh);BT=mm(tr(Rh),Z)
 rounding=[[sum((B[i][j]+BT[i][j] for j in range(N)),F(0))*(i==k) for k in range(N)] for i in range(N)]
 U=matrix(source['nominal_complete_original_source_Gram_Loewner_upper'])
 if replay:
  Lopt=mm(GI,H0);E=add(L,Lopt,-1)
  Y=add(add(scale(U,rho),mm(mm(tr(H0),GI),H0),-1),mm(mm(tr(E),Gup),E))
 else:
  HL=mm(tr(H0),L)
  Y=add(add(add(scale(U,rho),HL,-1),tr(HL),-1),mm(mm(tr(L),Gup),L))
 Y=rounded_bound(add(Y,rounding),1,10**24)[0];assert psd(Y)
 Ep=matrix(residual['actual_physical_Riesz_error_Gram_Loewner_upper']);Ec=matrix(residual['actual_canonical_Riesz_error_Gram_Loewner_upper'])
 k=list(map(F,source['complete_physical_operator_parity_norm_upper']));delta=F(source['actual_source_approximation_operator_error_upper'])
 phys=[[F(33,32)*k[i%2]*k[j%2]*Ep[i][j]+33*delta**2*T[i][j] for j in range(N)] for i in range(N)]
 phys=rounded_bound(phys,1,10**24)[0]
 EL=rounded_bound(mm(mm(tr(L),Ec),L),1,10**24)[0]
 # Fixed explicit Young parameters. They split source transfer, projection
 # representative error, and the nominal/error variational residual.
 u=F(1);t=F(1,4)
 error=rounded_bound(add(scale(phys,rho*(1+u)),EL,1+1/u),1,10**24)[0]
 A=rounded_bound(add(scale(Y,1+t),error,1+1/t),1,10**24)[0]
 assert all(psd(B) for B in [Gup,phys,EL,error,A])
 # Exact PSD doubling gives a dimension-independent uniform bound.
 lam=F(1)
 while not psd(add(scale(P,lam),A,-1)):lam*=2
 low=lam/2
 for _ in range(12):
  mid=(low+lam)/2
  if psd(add(scale(P,mid),A,-1)):lam=mid
  else:low=mid
 assert psd(add(scale(P,lam),A,-1))
 bound=lam/alpha;prior=F(source['actual_complete_original_canonical_source_Gram_relative_actual_native_metric_upper'])
 ceiling=F(weak['scalar_Schur_source_budget_strict_ceiling_using_inherited_complement_floor'])
 return dict(milestone='RC64',status='PASS',input_sha256=hashes,native_features_certified=list(range(N)),
  projection_target='actual canonical orthogonal rank-22 native Riesz projection',
  source_definition='original source Sigma_plus=R+sigma; identity R projects to zero',
  exact_rational_variational_coefficients=serialize(L),nominal_trial_original_source_pairing_center=serialize(H0),
  nominal_pairing_halfwidths=serialize(Rh),pairing_rounding_Gram_allowance=serialize(rounding),
  actual_trial_canonical_Gram_Loewner_upper=serialize(Gup),
  nominal_variational_residual_Gram_Loewner_upper=serialize(Y),
  actual_source_transfer_physical_Gram_Loewner_upper=serialize(phys),
  canonical_Riesz_error_coefficient_Gram_Loewner_upper=serialize(EL),
  combined_variational_error_Gram_Loewner_upper=serialize(error),
  actual_rank_22_projected_source_residual_Gram_Loewner_upper=serialize(A),
  actual_projected_source_relative_physical_native_Gram_upper=str(lam),
  actual_projected_source_relative_canonical_native_Gram_upper=str(bound),
  prior_unprojected_source_relative_canonical_native_Gram_upper=str(prior),
  strict_scalar_Schur_budget_ceiling_from_RC63=str(ceiling),
  certified_upper_bound_to_required_budget_ceiling_ratio=str(bound/ceiling),
  source_transfer_Young_parameter=str(u),nominal_error_Young_parameter=str(t),
  actual_rank_22_projection_residual_upper_certified=True,
  exact_actual_projection_coefficients_evaluated=False,
  required_projected_source_budget_certified=bound<ceiling,
  actual_projected_source_budget_failure_proved=False,
  uniform_twenty_two_positive_Weil_floor_certified=False,
  whole_aperture_positivity_extended=False,RH=False,F4=False)
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/n for n in ['rpb108_rc38_thirty_two_metric.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc60_twenty_two_mixed_residuals.json','rpb108_rc61_twenty_two_signed_head.json','rpb108_rc62_twenty_two_original_source_covariance.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json']]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==saved
  print('PASS: independent square completion, exact PSD variational and transfer bounds, actual rank-22 canonical projection attachment')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
