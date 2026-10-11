"""RC103: certified polynomial complement inverse and lifted-response route.

No arithmetic lifted response is evaluated. Conditional strong floors
are test targets, not certified lower bounds for the original strong head.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale
from validate_rpb108_rc90_continuous_source_balance_and_method_floor import relative40
from validate_rpb108_rc97_additional_low_mode_coverage import pd
from validate_rpb108_rc63_twenty_two_weak_floor_obstruction import up,down

def chebyshev(n,x,replay=False):
 if replay:
  # T_n(c) = sum_k binom(n,2k)c^(n-2k)(c^2-1)^k, c>=1.
  from math import comb
  return sum((F(comb(n,2*k))*x**(n-2*k)*(x*x-1)**k for k in range(n//2+1)),F(0))
 a,b=F(1),x
 if n==0:return a
 for _ in range(1,n):a,b=b,2*x*b-a
 return b

def padd(a,b):
 return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def pmul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c

def residual_polynomial(n,a,b):
 x=[(b+a)/(b-a),-2/(b-a)];p0=[F(1)];p1=x
 for _ in range(1,n):p0,p1=p1,padd([2*z for z in pmul(x,p1)],[-z for z in p0])
 p=[z/chebyshev(n,x[0]) for z in p1];assert p[0]==1
 q=[-z for z in p[1:]]
 assert padd([F(1)],[-z for z in pmul([F(0),F(1)],q)])==p
 return p,q

def polyval(p,A,replay=False):
 n=len(A);ident=[[F(i==j) for j in range(n)] for i in range(n)];out=[[F(0)]*n for _ in range(n)]
 if replay:
  power=ident
  for a in p:out=add(out,scale(power,a));power=mm(power,A)
 else:
  for a in reversed(p):out=add(mm(A,out),scale(ident,a))
 return out

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];prior,odd,even,tail,norm=map(json.loads,raw);h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['milestone']=='RC102' and prior['input_sha256'][:3]==[h[1],h[2],h[3]] and prior['input_sha256'][8]==h[4]
 assert odd['input_sha256'][0]==h[2] and odd['input_sha256'][2]==h[3] and odd['input_sha256'][15]==h[4]
 assert even['input_sha256']==odd['input_sha256'][1:] and odd['six_mode_corrected_positivity_certified']
 a=F(prior['inherited_complement_floor']);assert a==F(247,2500)
 tau=F(tail['rank_1250_canonical_tail_certificate']['canonical_complement_embedding_norm_upper']);rho=F(252,257);rows=[]
 for j,parity in enumerate(['even','odd']):
  old=prior['parity_completion_certificates'][j];cert=[even,odd][j];L=matrix(cert['corrected_'+parity+'_three_mode_Loewner_lower']);G=matrix(cert['common_actual_rank_1250_source_coupling_Gram_upper']);V=matrix(old['corrected_source_norm_transport_Gram_upper']);k=F(norm['complete_physical_operator_parity_norm_upper'][j]);g=rho*tau*tau*k*k
  assert pd(L) and psd(G) and V==scale(G,g/(a*a))
  b=up(1+tau*tau*k,10**6);assert b>=1+tau*tau*k>a and b>1
  c=(b+a)/(b-a);assert c>1
  lam=relative40(V,L);assert psd(add(scale(L,lam),V,-1))
  targets=[]
  for beta in [F(1),F(1,1000),F(1,10**6),F(1,10**9),F(1,10**12)]:
   n=1
   while lam/chebyshev(n,c)**2>beta/8:n+=1
   eps=1/chebyshev(n,c,replay);assert eps==1/chebyshev(n,c) and eps>0 and eps<1
   assert eps*eps*lam<=beta/8 and (n==1 or lam/chebyshev(n-1,c)**2>beta/8)
   assert psd(add(scale(L,beta/8),scale(V,eps*eps),-1))
   targets.append(dict(hypothetical_strong_floor=str(beta),floor_is_certified=False,polynomial_residual_degree=n,inverse_polynomial_degree=n-1,uniform_relative_residual_upper=str(eps),uniform_inverse_error_norm_upper=str(eps/a),residual_correction_relative_weak_lower_upper=str(eps*eps*lam),allocated_correction_budget=str(beta/8),lifted_response_Gram_target_relative_weak_lower=str(beta/4),completion_margin_relative_weak_lower=str(beta/4),minimal_degree_for_this_relative_enclosure_certified=True))
  # Verify quotient and residual identities on a noncommuting cross example.
  n=targets[0]['polynomial_residual_degree'];p,q=residual_polynomial(n,a,b)
  ident=[[F(1),F(0)],[F(0),F(1)]];D=[[F(2),F(1,4)],[F(1,4),F(1)]];assert pd(add(D,scale(ident,a),-1)) and pd(add(scale(ident,b),D,-1))
  R=[[F(1),F(1,3)],[F(1,2),F(-1,4)]];det=D[0][0]*D[1][1]-D[0][1]*D[1][0];Di=[[D[1][1]/det,-D[0][1]/det],[-D[1][0]/det,D[0][0]/det]] if replay else inverse(D);Q=[[F(4),F(1,5)],[F(1,5),F(3)]]
  Y=mm(polyval(q,D,replay),R);r=add(R,mm(D,Y),-1);assert r==mm(polyval(p,D,replay),R)
  # Weak Schur block from an approximate lift, paid by its residual.
  Fexact=add(Q,mm(mm(tr(R),Di),R),-1)
  lift=add(add(add(Q,mm(tr(R),Y),-1),mm(tr(Y),R),-1),mm(mm(tr(Y),D),Y))
  assert Fexact==add(lift,mm(mm(tr(r),Di),r),-1)
  eps=1/chebyshev(n,c,replay);assert psd(add(scale(mm(tr(R),R),eps*eps),mm(tr(r),r),-1))
  # The exact elimination preserves positivity; scalar-floor elimination need not.
  scalar=add(Q,scale(mm(tr(R),R),1/a),-1);assert pd(Fexact) and not psd(scalar)
  full=[Q[i]+tr(R)[i] for i in range(2)]+[R[i]+D[i] for i in range(2)];assert pd(full)
  rows.append(dict(parity=parity,complement_spectral_lower=str(a),complement_spectral_upper=str(b),complement_upper_rounding_grid='1e-6',Chebyshev_exterior_point=str(c),generic_correction_relative_weak_lower_upper=str(lam),degree_budget_certificates=targets,exact_inverse_retains_RC101_weak_lower=True,polynomial_quotient_identity_verified=True,abstract_noncommuting_inverse_residual_Gram_verified=True,abstract_approximate_lift_Schur_identity_verified=True,abstract_exact_elimination_positive_while_scalar_elimination_rejects=True,abstract_control_scope='illustrative matrices, not original arithmetic lifts'))
 out=dict(milestone='RC103',status='PASS',input_sha256=h,arithmetic='exact Fraction; no floating acceptance',certified_corrected_span_dimension=6,original_operator_nonpositive_spectral_dimension_upper=1244,
 complement_inverse_polynomial_theorem='For alpha I<=D<=b I, p_n(x)=T_n((b+alpha-2x)/(b-alpha))/T_n((b+alpha)/(b-alpha)), q_(n-1)(x)=(1-p_n(x))/x is a polynomial and ||I-Dq(D)||<=epsilon_n=1/T_n((b+alpha)/(b-alpha)).',
 exact_effective_head='F=A_H-B D^(-1) B*, D=P_E A_Q P_E, B=P_H A_Q P_E; F>=T_alpha, retaining the certified weak lower L.',
 residual_lift_identity='R=P_E A_Q W, Y=q(D)R, r=R-DY; P_S F W=P_S A_Q(W-Y)-P_S B D^(-1)r.',
 residual_weak_form_identity='W*F W=Gram_A_Q(W-Y)-r*D^(-1)r; hence the lifted weak form minus alpha^(-1)Gram(r) is a lower.',
 conditional_completion_theorem='If F|S>=beta I, Gram(P_S A_Q(W-Y))<=beta L/4 and epsilon_n^2(g/alpha^2)G<=beta L/8, then Gram(P_S F W)<=3beta L/4 and the full original form is positive.',
 posterior_residual_version='For any certified approximate lift Yhat, replace epsilon_n^2 G by an actual upper for Gram(R-DYhat); the exact residual identities remain valid.',
 uniform_complement_inverse_analytic_proof_supplied=True,parity_inverse_lift_certificates=rows,
 complement_inverse_computed_on_actual_arithmetic_sources=False,actual_lifted_response_Gram_certified=False,hypothetical_strong_floors_are_not_original_certificates=True,strong_head_block_certified=False,complete_weak_mode_coverage_certified=False,matrix_Schur_positivity_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False,
 new_source_integrals_evaluated=0,dense_remaining_head_matrix_required_by_inverse_polynomial_theorem=False)
 if saved is not None:assert out==saved
 return out

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates';names=['rpb108_rc102_six_response_completion_boundary.json','rpb108_rc101_odd_three_mode_jump_tail.json','rpb108_rc100_even_three_mode_jump_tail.json','rpb108_rc95_jump_aware_even_source_tail.json','rpb108_rc66_arch_multiplier_transport.json'];defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: positive-binomial Chebyshev replay, minimal degree budgets, exact quotient and noncommuting Schur-residual controls')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
