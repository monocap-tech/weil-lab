"""RC105: scaled inverse recurrence and certified local-error budgets.
All operator-action accuracies below are requirements, not performed actions.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
from validate_rpb108_rc103_complement_inverse_lift import chebyshev,residual_polynomial,polyval
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale
from validate_rpb108_rc47_correlated_native_transport import serialize

def amplification(n,c,replay=False):
 t=[chebyshev(k,c,replay) for k in range(n+1)]
 if replay:return sum((F(k)*t[n-k+1]/t[n] for k in range(1,n+1)),F(0))
 return sum((F(n-j+1)*t[j]/t[n] for j in range(1,n+1)),F(0))

def lift(D,R,n,a,b,replay=False,errors=None):
 d=len(D);I=[[F(i==j) for j in range(d)] for i in range(d)];Z=scale(add(scale(I,b+a),D,-2),1/(b-a));t=[chebyshev(k,(b+a)/(b-a),replay) for k in range(n+1)]
 errors=errors or [[[F(0)]*len(R[0]) for _ in range(d)] for _ in range(n)]
 y0=[[F(0)]*len(R[0]) for _ in range(d)];y1=add(scale(R,2/((b-a)*t[1])),errors[0])
 for k in range(1,n):
  nxt=add(add(scale(mm(Z,y1),2*t[k]/t[k+1]),y0,-t[k-1]/t[k+1]),R,4*t[k]/((b-a)*t[k+1]));y0,y1=y1,add(nxt,errors[k])
 return y1

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];low,prior=map(json.loads,raw);h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert low['milestone']=='RC104' and prior['milestone']=='RC103' and low['input_sha256'][0]==h[1]
 rows=[]
 for j,name in enumerate(['even','odd']):
  old=prior['parity_inverse_lift_certificates'][j];a=F(old['complement_spectral_lower']);b=F(old['complement_spectral_upper']);c=(b+a)/(b-a);lam=F(old['generic_correction_relative_weak_lower_upper']);ceiling=F(low['parity_low_subspace_certificates'][j]['exact_effective_strong_floor_upper']);budgets=[]
  for beta in [ceiling,F(1,10**6),F(1,10**9),F(1,10**12)]:
   n=1
   while lam/chebyshev(n,c)**2>beta/32:n+=1
   eps=1/chebyshev(n,c,replay);H=amplification(n,c,replay);eta=eps/(b*H)
   assert H==amplification(n,c) and 0<H<=F(n*(n+1),2)
   assert 4*eps*eps*lam<=beta/8 and lam/chebyshev(n-1,c)**2>beta/32
   assert eps+b*H*eta==2*eps
   budgets.append(dict(strong_floor_target=str(beta),target_is_certified_lower=False,target_is_RC104_upper_ceiling=beta==ceiling,residual_degree=n,inverse_polynomial_degree=n-1,ideal_relative_residual_upper=str(eps),scaled_recurrence_local_error_amplification_upper=str(H),each_total_local_error_common_Gram_factor_upper=str(eta*eta),each_total_local_error_common_norm_factor_upper=str(eta),isolated_Z_action_error_common_norm_factor_upper=str(eta/2),final_lift_error_common_norm_factor_upper=str(H*eta),actual_residual_common_norm_factor_upper=str(2*eps),residual_correction_relative_weak_lower_upper=str(4*eps*eps*lam),allocated_correction_budget=str(beta/8),lifted_response_relative_weak_lower_target=str(beta/4),minimal_degree_for_reserved_ideal_budget=True))
  # Noncommuting rational control: recurrence vs independent polynomial evaluation.
  D=[[F(2),F(1,4)],[F(1,4),F(1)]];R=[[F(1),F(1,3)],[F(1,2),F(-1,4)]];n=9;p,q=residual_polynomial(n,a,b)
  ideal=lift(D,R,n,a,b,replay);assert ideal==mm(polyval(q,D,replay),R)
  delta=F(1,10**8);errors=[scale(R,delta*(-1)**k) for k in range(n)];actual=lift(D,R,n,a,b,replay,errors);E=add(actual,ideal,-1);H=amplification(n,c,replay);RG=mm(tr(R),R)
  assert psd(add(scale(RG,(delta*H)**2),mm(tr(E),E),-1))
  r=add(R,mm(D,actual),-1);bound=1/chebyshev(n,c,replay)+b*delta*H
  assert psd(add(scale(RG,bound*bound),mm(tr(r),r),-1))
  # At Z=I (D=alpha I), identical impulses attain the amplification H.
  edge=scale([[F(1),F(0)],[F(0),F(1)]],a);err=[scale(R,delta) for _ in range(n)];edge_error=add(lift(edge,R,n,a,b,replay,err),lift(edge,R,n,a,b,replay),-1)
  assert edge_error==scale(R,delta*H)
  rows.append(dict(parity=name,complement_spectral_lower=str(a),complement_spectral_upper=str(b),Chebyshev_exterior_point=str(c),generic_correction_relative_weak_lower_upper=str(lam),local_error_budgets=budgets,noncommuting_exact_polynomial_recurrence_verified=True,inexact_recurrence_and_actual_residual_Gram_controls_verified=True,endpoint_common_error_amplification_equality_verified=True,control_scope='abstract rational operators, not arithmetic actions'))
 out=dict(milestone='RC105',status='PASS',input_sha256=h,arithmetic='exact Fraction; no floating acceptance',scaled_inverse_recurrence_analytic_proof_supplied=True,
 scaled_recurrence='t_k=T_k(c), Z=(b+alpha-2D)/(b-alpha), Y_0=0, Y_1=2R/((b-alpha)t_1), Y_(k+1)=2(t_k/t_(k+1)) ZY_k-(t_(k-1)/t_(k+1))Y_(k-1)+4t_k R/((b-alpha)t_(k+1)); Y_n=q_(n-1)(D)R.',
 perturbation_identity='If each completed step j adds E_j, including initial step, Yhat_n-Y_n=sum_(j=1)^n (t_j/t_n) U_(n-j)(Z) E_j.',
 common_Gram_error_theorem='If E_j*E_j<=eta_j^2 G, then Gram(Yhat_n-Y_n)<=H_eta^2 G, H_eta=sum_j (n-j+1)(t_j/t_n)eta_j; Gram(R-DYhat_n)<=(epsilon_n+b H_eta)^2 G.',
 local_error_scope='Each E_j is total additive step error relative to the displayed exact recurrence on the actual previous iterates. Includes operator, projection, source, coefficient and arithmetic errors. Errors need not be independent or orthogonal.',
 isolated_action_budget_scope='If only Z-action error is present, its common norm factor eta/2 suffices because 2t_k/t_(k+1)<2; other step errors require their own share of the total eta allowance.',
 conditional_completion='With actual strong floor beta and actual Gram(P_S A_Q(W-Yhat_n))<=beta L/4, the listed residual budget implies original positivity by RC103. No listed beta is a proved lower.',
 parity_inexact_inverse_certificates=rows,known_corrected_positive_span_dimension=6,original_operator_nonpositive_spectral_dimension_upper=1244,new_source_integrals_evaluated=0,actual_operator_actions_performed=False,actual_lifted_response_Gram_certified=False,strong_head_block_lower_certified=False,complete_nonpositive_mode_coverage_certified=False,matrix_Schur_positivity_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert out==saved
 return out

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates';defaults=[base/'rpb108_rc104_eight_mode_strong_floor_ceiling.json',base/'rpb108_rc103_complement_inverse_lift.json']
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: positive-binomial replay, reversed error sum, independent polynomial controls and endpoint sharpness')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
