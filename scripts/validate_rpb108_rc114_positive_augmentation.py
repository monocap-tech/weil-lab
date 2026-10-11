"""RC114: projection-free positive augmentation and exact finite response criterion.
Inputs RC113 RC112 RC111 RC106 RC103 RC66. No arithmetic responses computed.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,argparse
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale
from validate_rpb108_rc97_additional_low_mode_coverage import pd
from validate_rpb108_rc47_correlated_native_transport import root
from validate_rpb108_rc103_complement_inverse_lift import chebyshev
from validate_rpb108_rc107_original_compression_spectral_census import inertia

def up(x,d):return F(-((-x.numerator*d)//x.denominator),d)
def down(x,d):return F(x.numerator*d//x.denominator,d)
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];old,cov,prior,sand,inv,norm=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in [old,cov,prior,sand,inv,norm]]==['RC113','RC112','RC111','RC106','RC103','RC66']
 assert old['input_sha256'][:4]==hs[1:5] and old['input_sha256'][5]==hs[5]
 assert cov['explicit_exceptional_space_dimension']==639 and old['original_count_below_one_hundredth_upper']==639
 assert cov['input_sha256'][0]==hs[2] and cov['input_sha256'][5]==hs[5] and sand['input_sha256'][1]==hs[4]
 rho=F(252,257);t=F(1,100);rows=[]
 for i,r in enumerate(cov['parity_coverage_certificates']):
  a=F(r['reference_floor']);p=F(r['low_band_penalty_upper']);d2=F(r['Fourier_restriction_squared_tail_upper']);k=F(norm['complete_physical_operator_parity_norm_upper'][i])
  sr=root(rho,10**12);sd=root(d2,10**12);assert sr*sr>=rho and sd*sd>=d2
  x2=up((sr+sd)**2,10**12);variants=[]
  for name,u in [('positivity',F(1,4)),('threshold_count',F(32) if i==0 else F(4))]:
   lam=(1+u)*p;aa=down(a-(1+1/u)*p*d2,10**9);v=up(lam*x2,10**12);b=up(1+rho*k+v,10**6)
   assert aa>0 and b>aa and v/aa>1
   if name=='threshold_count':assert aa>t
   budgets=[]
   if name=='positivity':
    c=(b+aa)/(b-aa);n=1;prev=F(1);tn=c
    for target in [F(1,10**6),F(1,10**12),F(1,10**24)]:
     while 4*up(1/tn,10**40)**2*v/aa>target:
      prev,tn=tn,2*c*tn-prev;n+=1
     exact=1/chebyshev(n,c,replay);eps=up(exact,10**40);H=F(n*(n+1),2);eta=eps/(b*H)
     assert tn==chebyshev(n,c) and 4*eps*eps*v/aa<=target and 4*up(1/prev,10**40)**2*v/aa>target
     assert eps+b*H*eta==2*eps
     budgets.append(dict(auxiliary_response_residual_correction_allowance=str(target),residual_degree=n,inverse_polynomial_degree=n-1,relative_residual_upper=str(eps),total_local_error_norm_factor_relative_source_Gram=str(eta),conservative_recurrence_amplification_upper=str(H),inexact_response_correction_operator_norm_upper=str(4*eps*eps*v/aa),actual_arithmetic_action_contract_verified=False,correlated_response_form_enclosure_error_not_included=True))
   variants.append(dict(purpose=name,Young_parameter=str(u),finite_augmentation_coefficient=str(lam),positive_augmented_operator_lower=str(aa),positive_augmented_operator_upper=str(b),augmentation_squared_factor_norm_upper=str(v),generic_auxiliary_response_norm_upper=str(v/aa),generic_auxiliary_response_norm_bound_is_below_one=False,uniform_inverse_budgets=budgets,threshold_one_hundredth_counting_allowed=aa>t))
  rows.append(dict(parity=r['parity'],reference_floor=str(a),low_band_penalty=str(p),Fourier_approximation_squared_error_upper=str(d2),finite_Fourier_approximation_squared_norm_upper=str(x2),augmentation_rank_upper=r['parity_exceptional_dimension'],positive_augmentation_certificates=variants))
 # Nonidentity canonical metric: A, H are forms, inverses are inverse form matrices.
 M=[[F(2),F(1,3)],[F(1,3),F(1)]];assert pd(M)
 H=[[F(3),F(1,4)],[F(1,4),F(2)]];I=eye(2)
 if replay:
  det=H[0][0]*H[1][1]-H[0][1]*H[1][0];Hi=[[H[1][1]/det,-H[0][1]/det],[-H[1][0]/det,H[0][0]/det]]
 else:Hi=inverse(H)
 controls=[]
 for label,T in [('positive',[[F(1,4),F(1,5)],[F(-1,6),F(1,7)]]),('negative',[[F(2),F(1,5)],[F(-1,6),F(1,7)]])]:
  A=add(H,mm(tr(T),T),-1);BS=mm(mm(T,Hi),tr(T));assert pd(A)==pd(add(I,BS,-1))
  Ht=add(H,scale(M,t),-1);assert pd(Ht)
  BSt=mm(mm(T,inverse(Ht)),tr(T))
  assert inertia(add(A,scale(M,t),-1),replay)['negative']==inertia(add(I,BSt,-1),replay)['negative']
  # C_response + residual inverse correction = exact BS, arbitrary approximate lift.
  Y=[[F(1,9),F(1,11)],[F(-1,13),F(1,15)]];rr=add(tr(T),mm(H,Y),-1)
  response=add(add(mm(T,Y),mm(tr(Y),tr(T))),mm(mm(tr(Y),H),Y),-1)
  assert BS==add(response,mm(mm(tr(rr),Hi),rr))
  # H >=a M and <=b M; residual covector norm uses inverse canonical metric.
  aa=F(1,2);bb=F(4);assert pd(add(H,scale(M,aa),-1)) and pd(add(scale(M,bb),H,-1))
  GG=mm(mm(tr(rr),inverse(M)),rr)
  lo=add(response,scale(GG,1/bb));upper=add(response,scale(GG,1/aa))
  assert psd(add(BS,lo,-1)) and psd(add(upper,BS,-1))
  controls.append(dict(scope='abstract noncommuting rational forms, not original Weil responses',label=label,nonidentity_canonical_metric_used=True,positive_equivalence_verified=True,threshold_inertia_with_actual_metric_verified=True,response_plus_residual_identity_verified=True,canonical_dual_metric_residual_sandwich_verified=True))
 # Exact first-contact null mapping, not a crossing-exclusion theorem.
 H1=F(2);T1=F(2);A1=H1-T1*T1;BS1=T1*T1/H1;assert A1<0 and BS1>1
 H0=F(4);T0=F(2);x=F(1);y=T0*x;assert H0*x-T0*y==0 and (T0*T0/H0-1)*y==0 and x==T0*y/H0
 return dict(milestone='RC114',status='PASS: certified projection-free positive augmentation and finite response equivalence; arithmetic response operator open',input_sha256=hs,arithmetic='exact fractions; Chebyshev recurrence/binomial and inverse-form replay',aperture='11/10',parity_positive_augmentation_certificates=rows,abstract_response_controls=controls,exact_null_mapping_control_verified=True,original_spectral_count_below_one_hundredth_lower=10,original_spectral_count_below_one_hundredth_upper=639,finite_auxiliary_response_rank_upper=639,positive_augmentation_of_full_original_operator_certified=True,finite_auxiliary_response_inertia_equivalence_proved_in_note=True,canonical_head_Gram_inverse_required_by_this_route=False,canonical_W_projection_required_by_this_route=False,actual_Fourier_adjoint_source_actions_certified=False,actual_auxiliary_response_operator_evaluated=False,actual_auxiliary_metric_conditioning_certified=False,auxiliary_response_norm_below_one_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=6);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,indent=2,sort_keys=True)+'\n')
 print('RC114 PASS: original positive augmentation and finite response criterion; actual auxiliary norm open')
