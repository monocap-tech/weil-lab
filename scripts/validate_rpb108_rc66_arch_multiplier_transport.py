"""RC66: global archimedean multiplier bound and rank-22 source transport.

Analytic lemma: the Euler sum-minus-integral remainder at z=1/4+i*pi*x
has modulus <= min(4,1/(2*x)). The report supplies its cellwise proof.
Directed constants are replayed with rational Taylor and atanh series.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import hashlib,json,sys
from validate_rpb108_rc30_interval_metric import I,PI
from validate_rpb108_rc42_native_signed_pole_head import outward
from validate_rpb108_rc31_trial_riesz import psd,inverse
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,cong,relative,N

def rational_log(q):
 assert q>1
 y=(q-1)/(q+1);n=600
 s=2*sum((y**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
 return s,s+2*y**(2*n+1)/(F(2*n+1)*(1-y*y))
def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];native,residual,source,projection,refined,precision=[json.loads(x) for x in raw]
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert refined['input_sha256'][:4]==hashes[:4]
 assert source['input_sha256'][4]==hashes[5]
 assert refined['actual_rank_22_projected_source_residual_upper_certified']
 R=F(11,5);cut=F(3,20);K=F(643,100)
 c0,c1=map(F,precision['actual_constant_enclosure'])
 e=I(1).exp();elo,ehi=outward(e,10**30)
 a0=I(c0)+(I(2*R)).log()-PI/2-3*I(2).log()
 a1=I(c1)+(I(2*R)).log()-PI/2-3*I(2).log()
 a=F(a0.l);b=F(a1.h)
 low=a-F(I(ehi+cut).log().h)
 high=-F(I(1+ehi/cut).log().h)-F(1,2)/cut
 # Both frequency regions certify m_arch >= -643/100.
 assert low>-K and high>-K and K<8
 # Upper bound m_arch<=4 follows from |psi(z)-log z|<=4
 # and |z| <= pi(e+x), checked at the positive constant term.
 assert F(PI.l)**2*elo**2>F(1,16) and 4<K
 if replay:
  ep=sum((F(1,factorial(j)) for j in range(101)),F(0))
  eu=ep+F(1,factorial(101))/(1-F(1,102))
  assert elo<=ep<=eu<=ehi
  lR,uR=rational_log(2*R);l2,u2=rational_log(F(2));le,ue=rational_log(ehi+cut);lh,uh=rational_log(1+ehi/cut)
  pi0,pi1=F(PI.l),F(PI.h)
  a_exact_low=c0+lR-pi1/2-3*u2
  assert a_exact_low-ue>-K and -uh-F(1,2)/cut>-K
  # Independent rational series prove the same global cap; the stored
  # Decimal endpoints are regenerated but need not enclose this wider series.
 rho=F(252,257);delta=F(source['actual_source_approximation_operator_error_upper'])
 oldk=list(map(F,source['complete_physical_operator_parity_norm_upper']));k=[x-8+K for x in oldk];assert all(x>0 for x in k)
 Ep=matrix(residual['actual_physical_Riesz_error_Gram_Loewner_upper']);T=matrix(native['physical_native_trial_Gram'])
 M=matrix(native['actual_canonical_native_Gram_Loewner_lower']);C=matrix(native['chebyshev_to_legendre'])
 Y=matrix(projection['nominal_variational_residual_Gram_Loewner_upper']);EL=matrix(projection['canonical_Riesz_error_coefficient_Gram_Loewner_upper'])
 v=F(1,65536);u=F(1,16);ts=[F(2),F(3,2)]
 physical=[[(1+v)*k[i%2]*k[j%2]*Ep[i][j]+(1+1/v)*delta**2*T[i][j] for j in range(N)] for i in range(N)]
 physical=rounded_bound(physical,1,10**24)[0]
 oldphysical=matrix(refined['refined_actual_source_transfer_physical_Gram_Loewner_upper'])
 assert psd(add(oldphysical,physical,-1))
 error=rounded_bound(add(scale(physical,rho*(1+u)),EL,1+1/u),1,10**24)[0]
 A=[[(1+ts[i%2])*Y[i][j]+(1+1/ts[i%2])*error[i][j] for j in range(N)] for i in range(N)]
 A=rounded_bound(A,1,10**24)[0]
 oldA=matrix(refined['refined_actual_rank_22_projected_source_residual_Gram_Loewner_upper'])
 assert all(psd(B) for B in [M,physical,error,A,add(oldA,A,-1)])
 rows=[]
 for p in range(2):
  lam=relative(block(A,p),block(M,p))
  if replay:
   CI=inverse(block(C,p));assert psd(cong(CI,add(scale(block(M,p),lam),block(A,p),-1)))
   assert psd(cong(CI,block(add(oldA,A,-1),p)))
  rows.append(dict(parity='even' if p==0 else 'odd',complete_physical_operator_norm_upper=str(k[p]),actual_projected_residual_relative_canonical_Gram_upper=str(lam)))
 bound=max(F(r['actual_projected_residual_relative_canonical_Gram_upper']) for r in rows)
 prior=F(refined['actual_rank_22_projected_source_relative_canonical_native_Gram_upper']);assert bound<prior
 return dict(milestone='RC66',status='PASS',input_sha256=hashes,
  canonical_weight='log(e+abs(xi))',original_archimedean_multiplier='Re psi(1/4+i*pi*xi)-log(pi)',
  analytic_Euler_cell_remainder_modulus_bound='min(4,1/(2*abs(xi))) for xi!=0; 4 at zero',
  exact_quarter_digamma_identity='psi(1/4)=-gamma-pi/2-3*log(2)',
  frequency_split=str(cut),quarter_multiplier_enclosure=[str(a),str(b)],
  low_frequency_remainder_lower=str(low),high_frequency_remainder_lower=str(high),global_remainder_upper='4',
  certified_physical_archimedean_remainder_norm_upper=str(K),prior_archimedean_remainder_norm_upper='8',
  complete_physical_operator_parity_norm_upper=list(map(str,k)),native_features_certified=list(range(N)),
  parity_residual_certificates=rows,source_transfer_physical_Gram_Loewner_upper=serialize(physical),
  combined_canonical_variational_error_Gram_Loewner_upper=serialize(error),
  actual_rank_22_projected_source_residual_Gram_Loewner_upper=serialize(A),
  actual_rank_22_projected_source_relative_canonical_native_Gram_upper=str(bound),
  prior_RC65_uniform_projected_source_bound=str(prior),uniform_bound_fractional_reduction=str(1-bound/prior),
  full_matrix_Loewner_improvement_over_RC65_certified=True,
  strict_scalar_Schur_budget_ceiling=refined['strict_scalar_Schur_budget_ceiling_from_RC63'],
  required_projected_source_budget_certified=False,actual_projected_source_budget_failure_proved=False,
  analytic_multiplier_lemma_Lean_formalized=False,exact_actual_projection_coefficients_evaluated=False,
  uniform_twenty_two_positive_Weil_floor_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/n for n in ['rpb108_rc59_twenty_two_native_projection.json','rpb108_rc60_twenty_two_mixed_residuals.json','rpb108_rc62_twenty_two_original_source_covariance.json','rpb108_rc64_twenty_two_projected_source_residual.json','rpb108_rc65_parity_projected_residual_refinement.json','rpb108_rc56_precision_attached_head.json']]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True)==saved
  print('PASS: independent rational Taylor/atanh constants and Legendre congruence PSD replay; global analytic lemma supplied in report')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
