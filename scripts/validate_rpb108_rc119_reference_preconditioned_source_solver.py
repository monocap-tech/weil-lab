"""RC119: uniform source preconditioning and correlated stopping rules.
No reference inverse, original Weil action, or augmented response is executed.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
from validate_rpb108_rc103_complement_inverse_lift import chebyshev,residual_polynomial,polyval
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale
from validate_rpb108_rc114_positive_augmentation import up,down
from validate_rpb108_rc47_correlated_native_transport import root
from validate_rpb108_rc44_reduced_native_head import exp_bounds

def log2_bounds(replay=False):
 terms=[2*F(1,3)**(2*k+1)/F(2*k+1) for k in range(80)]
 if replay:terms.reverse()
 s=sum(terms,F(0));return s,s+2*F(1,3)**161/F(161*(1-F(1,9)))

def gram(X,G):return mm(tr(X),mm(G,X))
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]

def control(replay):
 N=[[F(2),F(1,4)],[F(1,4),F(1)]];P=[[F(8),F(1)],[F(1),F(5)]];R=[[F(2),F(1,2)],[F(1,2),F(1)]];shift=F(3,2);L=add(add(P,scale(N,-shift)),R)
 assert psd(R) and psd(add(scale(N,shift),R,-1)) and psd(add(L,N,-1)) and mm(P,L)!=mm(L,P)
 a=F(2,5);b=F(1);assert psd(add(L,scale(P,-a))) and psd(add(P,L,-1))
 M=mm(inverse(P),L);Z=add(scale(eye(2),(a+b)/(b-a)),scale(M,-2/(b-a)));c=(a+b)/(b-a)
 S=[[F(1),F(2)],[F(3),F(-1)]];f=mm(N,S);Y=[[F(1,10),F(1,5)],[F(-1,10),F(3,10)]];r=add(f,mm(L,Y),-1);g=mm(inverse(P),r)
 n=8;rp,qp=residual_polynomial(n,a,b);Q=polyval(qp,M,replay);exact=mm(Q,g)
 x0=[[F(0)]*2 for _ in range(2)];x1=scale(g,2/(a+b));pert0=x0;eta=F(1,10000)
 faults=[None]+[[[F(j,10**6),F(-j,10**6)],[F(1,10**6),F(2,10**6)]] for j in range(1,n+1)]
 pert1=add(x1,faults[1]);assert all(psd(add(scale(eye(2),eta*eta),gram(v,P),-1)) for v in faults[1:])
 for k in range(1,n):
  den=chebyshev(k+1,c,replay);A=2*chebyshev(k,c,replay)/den;B=chebyshev(k-1,c,replay)/den;C=4*chebyshev(k,c,replay)/((b-a)*den)
  x0,x1=x1,add(add(scale(mm(Z,x1),A),scale(x0,-B)),scale(g,C))
  pert0,pert1=pert1,add(add(add(scale(mm(Z,pert1),A),scale(pert0,-B)),scale(g,C)),faults[k+1])
 assert x1==exact
 U=[eye(2),scale(Z,2)]
 for k in range(1,n-1):U.append(add(scale(mm(Z,U[-1]),2),U[-2],-1))
 predicted=[[F(0)]*2 for _ in range(2)]
 for j in range(1,n+1):predicted=add(predicted,scale(mm(U[n-j],faults[j]),chebyshev(j,c,replay)/chebyshev(n,c,replay)))
 err=add(pert1,exact,-1);assert err==predicted
 H=F(n*(n+1),2);assert psd(add(scale(eye(2),(H*eta)**2),gram(err,P),-1))
 W=add(Y,exact);res=add(f,mm(L,W),-1);Ec=gram(res,inverse(L));GP=gram(res,inverse(P))
 assert psd(add(Ec,GP,-1)) and psd(add(scale(GP,1/a),Ec,-1))
 # Reference inverse response identity for arbitrary approximate columns.
 Ahat=Y;t=add(r,mm(P,Ahat),-1);C=add(add(mm(tr(r),Ahat),mm(tr(Ahat),r)),gram(Ahat,P),-1);G=gram(r,inverse(P));corr=gram(t,inverse(P))
 assert G==add(C,corr) and psd(add(G,C,-1)) and psd(add(add(C,gram(t,inverse(N))),G,-1))
 return dict(scope='abstract noncommuting rational forms, not original arithmetic actions',dimension=2,physical_metric_nonidentity=True,preconditioned_metric_selfadjoint_identity_verified=mm(P,M)==L,normalized_Chebyshev_quotient_recurrence_verified=True,inexact_second_kind_propagation_identity_verified=True,correlated_local_fault_and_total_Gram_bound_verified=True,canonical_error_correlated_posterior_sandwich_verified=True,reference_inverse_plus_residual_Gram_identity_verified=True)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,src,prec=map(json.loads,raw);h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in [prior,src,prec]]==['RC118','RC115','RC56'] and prior['input_sha256'][2]==h[1] and prior['input_sha256'][4]==h[2]
 B=F(11,10);rho=F(252,257);shift=F(789,125);ep=F(11,4);assert exp_bounds(F(1))[1]<ep
 HS2=4*B*up(ep*F(22,7)**2/3,10**20);assert all(F(x['supported_regular_multiplier_Hilbert_Schmidt_squared_upper'])==HS2 for x in prior['parity_canonical_source_residual_certificates']) and shift*shift>HS2
 ll,lh=log2_bounds(replay);cl,ch=map(F,prec['actual_constant_enclosure']);slo=down(shift+cl+ll,10**20);shi=up(shift+ch+lh,10**20);assert slo>0
 a=1/(1+shift*rho);b=F(1);kap=1/a;assert kap<F(36,5)
 c=(b+a)/(b-a);budgets=[]
 for digits in [6,12,24]:
  target=F(1,10**digits);n=1
  while 1/chebyshev(n,c,replay)>target/3:n+=1
  eps=1/chebyshev(n,c,replay);prev=1/chebyshev(n-1,c,replay);assert prev>target/3
  H=F(n*(n+1),2);dg=a*target/(3*(1+eps));eta=target/(3*H)
  assert eps+(1+eps)*dg/a+H*eta<=target
  budgets.append(dict(relative_canonical_error_norm_target=str(target),residual_degree=n,inverse_polynomial_degree=n-1,minimal_degree_for_one_third_allocation=True,uniform_relative_residual_upper=str(up(eps,10**(digits+8))),previous_degree_relative_residual_lower=str(down(prev,10**(digits+8))),preconditioned_source_error_P_norm_allowance_per_initial_error_norm=str(dg),normalized_local_fault_P_norm_allowance_per_initial_error_norm=str(eta),recurrence_fault_amplification_upper=str(H),actual_reference_inverse_or_action_contract_verified=False))
 rows=[]
 for p,s in zip(prior['parity_canonical_source_residual_certificates'],src['parity_rational_Fourier_adjoint_sources']):
  assert p['parity']==s['parity'];alpha=F(p['source_shape_trial_scalar']);k=1
  while alpha*(F(k,2)+cl+ll)<=2:k+=1
  degree=2**k+(p['parity']=='odd');lb=F(k,2)+cl+ll;assert alpha*lb>2
  warm=F(p['canonical_Riesz_trial_error_squared_upper_for_center_source']);es=F(s['canonical_adjoint_source_error_squared_upper']);targets=[]
  for z in budgets:
   tau=F(z['relative_canonical_error_norm_target']);total=up((tau*root(warm,10**90)+root(es,10**90))**2,10**60)
   targets.append(dict(relative_error_norm_target=str(tau),conditional_final_exact_model_adjoint_error_squared_upper=str(total),source_rounding_and_model_error_paid=True,computed_correction=False))
  rows.append(dict(parity=p['parity'],RC118_center_source_trial_error_squared_upper=str(warm),scalar_unpreconditioned_noncontraction_polynomial_degree=degree,dyadic_harmonic_lower_block_count=k,metric_Rayleigh_lower_for_normalized_Legendre_test=str(down(lb,10**20)),physical_scalar_residual_norm_ratio_lower=str(down(alpha*lb-1,10**20)),noncontraction_is_actual_metric_obstruction_not_negative_Weil_direction=True,conditional_warm_start_targets=targets))
 return dict(milestone='RC119',status='PASS: universal positive principal-reference source solver and correlated residual stopping theorem; actions open',input_sha256=h,arithmetic='exact rational endpoint/constant, Hilbert-Schmidt, polynomial and noncommuting Gram checks',aperture='11/10',canonical_embedding_squared_norm_upper=str(rho),supported_regular_multiplier_squared_norm_upper=str(HS2),positive_principal_reference_shift=str(shift),reference_harmonic_plus_endpoint_constant_lower=str(slo),reference_harmonic_plus_endpoint_constant_upper=str(shi),reference_form_floor_lower=str(slo),preconditioned_spectral_lower=str(a),preconditioned_spectral_upper=str(b),preconditioned_condition_number_upper=str(kap),preconditioned_spectrum_uniform_over_full_physical_source_space=True,canonical_Riesz_source_stopping_rule='G_P <= G_error_c <= a^(-1) G_P; G_P = residual^* P^(-1) residual',reference_inverse_posterior_rule='G_P = C_W + t^* P^(-1) t <= C_W + s_lower^(-1) Gram_physical(t)',conditional_degree_and_action_budgets=budgets,parity_source_solver_certificates=rows,exact_noncommuting_control=control(replay),unpreconditioned_fixed_scalar_metric_correction_uniform_contraction_impossible=True,reference_inverse_action_evaluated=False,reference_metric_dense_matrix_required_by_theorem=False,efficient_reference_inverse_implementation_proved=False,canonical_full_range_source_realization_completed=False,original_Weil_or_augmented_actions_performed=False,augmented_inverse_responses_computed=False,auxiliary_response_norm_below_one_certified=False,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,new_positive_native_directions_certified=0,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=3);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC119 PASS: full-space preconditioned source bound and correlated controls; reference actions remain open')
