"""RC113: covered-complement embedding, inverse and correlated Schur budgets.
Actual arithmetic responses and projections have not been evaluated.
Inputs: RC112 RC111 RC106 RC103 RC105 RC66.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,argparse
from validate_rpb108_rc103_complement_inverse_lift import chebyshev,residual_polynomial,polyval
from validate_rpb108_rc105_inexact_inverse_recurrence import lift
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale
from validate_rpb108_rc97_additional_low_mode_coverage import pd

def up(q,d):return F(-((-q.numerator*d)//q.denominator),d)
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];cov,prior,sand,inv,action,norm=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in [cov,prior,sand,inv,action,norm]]==['RC112','RC111','RC106','RC103','RC105','RC66']
 assert cov['input_sha256'][0]==hs[1] and cov['input_sha256'][5]==hs[5]
 assert prior['input_sha256'][2:4]==hs[2:4] and prior['input_sha256'][6]==hs[5]
 assert sand['input_sha256']==[hs[4],hs[3]] and action['input_sha256'][1]==hs[3]
 assert cov['explicit_exceptional_space_dimension']==639 and cov['inherited_effective_strong_dimension']==611
 rho=F(252,257);t=F(1,100);rows=[]
 for i,r in enumerate(cov['parity_coverage_certificates']):
  L=F(r['frequency_log_cutoff']);d2=F(r['Fourier_restriction_squared_tail_upper']);a=F(r['original_complement_floor_grid_lower']);k=F(norm['complete_physical_operator_parity_norm_upper'][i]);assert L>1 and d2<1 and a>t
  s_exact=1/L+(1-1/L)*d2;s=up(s_exact,10**12);assert s_exact<=s<rho
  b=up(1+k*s,10**6);assert b>=1+k*s>a
  g=up(rho*s*k*k,10**12);assert g>=rho*s*k*k
  c=(b+a)/(b-a);targets=[]
  for delta in [F(1,10**6),F(1,10**12),F(1,10**24)]:
   n=1
   while 4*up(1/chebyshev(n,c),10**40)**2*g/a>delta:n+=1
   eps=up(1/chebyshev(n,c,replay),10**40);assert eps==up(1/chebyshev(n,c),10**40)
   H=F(n*(n+1),2);eta=eps/(b*H)
   assert 4*eps*eps*g/a<=delta and 4*up(1/chebyshev(n-1,c),10**40)**2*g/a>delta
   assert eps+b*H*eta==2*eps
   targets.append(dict(canonical_metric_residual_correction_allowance=str(delta),residual_degree=n,inverse_polynomial_degree=n-1,uniform_ideal_relative_residual_upper=str(eps),uniform_inverse_error_upper=str(eps/a),each_total_local_error_norm_factor_relative_source_Gram=str(eta),conservative_recurrence_amplification_upper=str(H),inexact_relative_residual_upper=str(2*eps),inexact_residual_correction_relative_actual_head_metric_upper=str(4*eps*eps*g/a),actual_action_contract_verified=False,actual_correlated_form_error_not_included=True))
  # Correlated lift with nonidentity actual head metric, signed mixing and inexact actions.
  D=[[F(2),F(1,4)],[F(1,4),F(1)]];I=eye(2);assert pd(add(D,scale(I,a),-1)) and pd(add(scale(I,b),D,-1))
  R=[[F(1),F(1,3)],[F(1,2),F(-1,4)]];M=[[F(2),F(1,3)],[F(1,3),F(1)]];Q=[[F(100),F(1,5)],[F(1,5),F(99)]]
  if replay:
   det=D[0][0]*D[1][1]-D[0][1]*D[1][0];Di=[[D[1][1]/det,-D[0][1]/det],[-D[1][0]/det,D[0][0]/det]]
  else:Di=inverse(D)
  Fe=add(Q,mm(mm(tr(R),Di),R),-1);scalar=add(Q,scale(mm(tr(R),R),1/a),-1);assert pd(M) and pd(Fe) and not psd(scalar)
  n=17;p,q=residual_polynomial(n,a,b);Y=lift(D,R,n,a,b,replay);assert Y==mm(polyval(q,D,replay),R)
  res=add(R,mm(D,Y),-1);G=mm(tr(R),R);eps=1/chebyshev(n,c,replay);assert psd(add(scale(G,eps*eps),mm(tr(res),res),-1))
  C=add(add(add(Q,mm(tr(R),Y),-1),mm(tr(Y),R),-1),mm(mm(tr(Y),D),Y))
  assert Fe==add(C,mm(mm(tr(res),Di),res),-1)
  lo=add(C,scale(mm(tr(res),res),1/a),-1);hi=add(C,scale(mm(tr(res),res),1/b),-1)
  assert psd(add(Fe,lo,-1)) and psd(add(hi,Fe,-1)) and pd(lo)
  eta=eps/(b*F(n*(n+1),2));errors=[scale(R,eta/F(2*(j+1))) for j in range(n)]
  Yhat=lift(D,R,n,a,b,replay,errors);rhat=add(R,mm(D,Yhat),-1)
  assert psd(add(scale(G,4*eps*eps),mm(tr(rhat),rhat),-1))
  # Separate positive W+E and S+E do not certify W+S+E.
  full=[[F(1),F(2),F(1,10)],[F(2),F(1),F(1,10)],[F(1,10),F(1,10),F(1)]]
  assert pd([[F(1),F(1,10)],[F(1,10),F(1)]]) and not psd(full)
  # Eliminate E, then S; agree with direct inverse of the combined complement.
  ee=full[2][2];fww=full[0][0]-full[0][2]**2/ee;fss=full[1][1]-full[1][2]**2/ee;fws=full[0][1]-full[0][2]*full[1][2]/ee
  nested=fww-fws*fws/fss;V=[row[1:] for row in full[1:]];rv=[[full[1][0]],[full[2][0]]]
  direct=full[0][0]-mm(mm(tr(rv),inverse(V)),rv)[0][0];assert nested==direct<0
  # Correlated nested residual correction decomposition, arbitrary signed residual.
  rs=F(1,7);re=F(-1,11);z=[[rs],[re]];h=rs-full[1][2]*re/ee
  assert mm(mm(tr(z),inverse(V)),z)[0][0]==re*re/ee+h*h/fss
  rows.append(dict(parity=r['parity'],new_complement_embedding_squared_norm_exact_upper=str(s_exact),new_complement_embedding_squared_norm_grid_upper=str(s),new_original_complement_floor_lower=str(a),new_original_complement_operator_upper=str(b),same_bounds_hold_for_inherited_effective_strong_compression=True,new_original_head_coupling_squared_norm_upper=str(g),unshifted_interval_condition_ratio=str(b/a),threshold_shifted_interval_condition_ratio=str((b-t)/(a-t)),inverse_budget_certificates=targets,abstract_noncommuting_actual_metric_correlated_sandwich_verified=True,abstract_inexact_action_residual_contract_verified=True,abstract_positive_separate_blocks_with_negative_full_coupling_verified=True,abstract_nested_and_direct_Schur_identity_verified=True,abstract_nested_signed_residual_correction_identity_verified=True))
 return dict(milestone='RC113',status='PASS: new covered-complement upper bounds and exact inverse-action budgets; arithmetic response open',input_sha256=hs,arithmetic='exact fractions; Chebyshev recurrence vs binomial replay',aperture='11/10',original_exceptional_space_dimension=639,inherited_effective_strong_space_dimension=611,parity_covered_complement_inverse_certificates=rows,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,original_floor_outside_exceptional_space=cov['original_floor_on_canonical_exceptional_orthogonal_complement'],covered_complement_embedding_bound_certified=True,new_complement_inverse_uniform_polynomial_theorem_certified=True,exact_nested_and_direct_Schur_reduction_theorem_in_note=True,actual_new_canonical_projection_constructed=False,actual_arithmetic_operator_actions_performed=False,actual_exceptional_correlated_forms_evaluated=False,actual_exceptional_response_Grams_evaluated=False,all_twelve_RC110_directions_positive_after_new_complement_coupling_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=6);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,indent=2,sort_keys=True)+'\n')
 print('RC113 PASS: certified covered-complement inverse budgets and signed Schur controls; actual responses open')
