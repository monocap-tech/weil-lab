"""RC87: certified fixed-space stationarity gain and convex fusion obstruction.

These are limits of two certificate routes, not a lower bound for actual
projected source leakage and not a positivity or scalar-budget failure.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,cong,relative
N=22;DIM=64
VECTORS=[[-490901,-984801,-992380,-1000000,-999307,-977601,-918634,-806462,-633906,-414340,-188253],[-894862,-903866,-921809,-947589,-977036,-1000000,-997712,-943242,-809269,-585418,-298210]]
def diag(v):return [[x*F(i==j) for j in range(len(v))] for i,x in enumerate(v)]
def quad(v,A,replay):
 if replay:return sum((v[i]*A[i][i]*v[i]+2*sum((v[i]*A[i][j]*v[j] for j in range(i+1,len(v))),F(0)) for i in range(len(v))),F(0))
 return mm(mm([v],A),[[x] for x in v])[0][0]
def decimal_upper(A,B):
 # An exact decade bound; this also handles factors much smaller than the
 # old 12-step unit-interval resolution without floating arithmetic.
 q=F(1,10**100)
 while not psd(add(scale(B,q),A,-1)):q*=10
 assert psd(add(scale(B,q),A,-1))
 return q

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];prior,response,enriched,old,weak=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['milestone']=='RC86' and prior['status']=='PASS'
 assert [prior['input_sha256'][i] for i in [1,5,2]]==hashes[1:4]
 assert response['input_sha256'][1]==hashes[2]
 assert [old['input_sha256'][i] for i in [2,8]]==[hashes[2],hashes[4]]
 assert prior['actual_Riesz_projection_head_rank']==38 and prior['canonical_trial_dimension']==DIM
 assert prior['source_input_features']==list(range(N))
 M=matrix(enriched['enriched_actual_native_Gram_Loewner_lower']);assert psd(M)
 G=matrix(enriched['recentered_nominal_metric_center']);D=diag(list(map(F,enriched['physical_mass'])));Di=diag([1/D[i][i] for i in range(DIM)])
 delta=F(enriched['actual_recentered_metric_mass_error_upper']);Gl=add(G,D,-delta)
 assert psd(add(Gl,D,-1))
 Z=matrix(response['nominal_source_canonical_trial_response_coefficients'])
 pairs=response['nominal_physical_Legendre_source_pairing_enclosures']
 H=[[(F(a)+F(b))/2 for a,b in row] for row in pairs];Rh=[[(F(b)-F(a))/2 for a,b in row] for row in pairs]
 d=add(H,mm(G,Z),-1);nominal=cong(d,Di)
 nominal_up,nround=rounded_bound(nominal,1,10**100);assert psd(nominal_up)
 # Normal-equation completion proves that no 64-mode correction can
 # improve nominal capture by more than d'G^-1d <= d'D^-1d.
 T=mm(inverse(G),d);assert mm(G,T)==d
 exact_gain=mm(tr(d),T);assert psd(exact_gain) and psd(add(nominal_up,exact_gain,-1))
 if replay:
  W=add(Z,T)
  capture=lambda C:add(add(mm(tr(H),C),mm(tr(C),H)),cong(C,G),-1)
  assert add(capture(W),capture(Z),-1)==exact_gain
  for i in range(DIM):
   for j in range(N):assert sum((G[i][k]*W[k][j] for k in range(DIM)),F(0))==H[i][j]
 Kh=cong(Rh,Di);assert all(x>=0 for row in Kh for x in row)
 box=diag([sum(row,F(0)) for row in Kh]);ZT=cong(Z,D)
 Omega,oround=rounded_bound(scale(add(add(nominal,box),ZT,delta**2),3),1,10**60)
 assert Omega==matrix(prior['canonical_trial_space_response_error_projection_Gram_Loewner_upper']) and psd(Omega)
 gains=[]
 for p in range(2):
  m=block(M,p);bn=decimal_upper(block(nominal_up,p),m);ba=decimal_upper(block(Omega,p),m)
  gains.append(dict(parity='even' if p==0 else 'odd',nominal_midpoint_metric_maximal_capture_gain_relative_input_upper=str(bn),actual_metric_nominal_source_maximal_trial_response_error_reduction_relative_input_upper=str(ba)))
 A=matrix(prior['retained_actual_rank_38_projected_original_source_Gram_Loewner_upper']);B=matrix(prior['response_attachment_actual_projected_original_source_Gram_Loewner_upper'])
 assert A==matrix(old['refined_actual_rank_38_projected_old_source_Gram_Loewner_upper'])
 assert all(psd(C) for C in [A,B])
 for C in [M,A,B,nominal_up,Omega]:assert all(C[i][j]==0 for i in range(N) for j in range(N) if (i-j)%2)
 ceiling=F(weak['scalar_Schur_source_budget_strict_ceiling_using_inherited_complement_floor'])
 witnesses=[]
 for p in range(2):
  v=list(map(F,VECTORS[p]));m=quad(v,block(M,p),replay);a=quad(v,block(A,p),replay);b=quad(v,block(B,p),replay);assert m>0
  ra=a/m;rb=b/m;lower=min(ra,rb)
  retained=F(prior['parity_residual_certificates'][p]['retained_relative_upper']);threshold=retained-F(1,4096)
  assert lower>threshold>ceiling and rb>ra
  assert psd(add(scale(block(M,p),retained),block(A,p),-1))
  # For EVERY theta in [0,1], its Rayleigh quotient on this same exact
  # direction is (1-theta)*ra+theta*rb >= lower > threshold.
  witnesses.append(dict(parity='even' if p==0 else 'odd',native_parity_direction=list(map(str,v)),input_Gram_quadratic=str(m),retained_upper_quadratic=str(a),RC86_candidate_upper_quadratic=str(b),retained_upper_Rayleigh_ratio=str(ra),RC86_candidate_upper_Rayleigh_ratio=str(rb),all_convex_fusions_relative_upper_factor_lower_bound=str(lower),next_lower_12_step_dyadic_factor=str(threshold),retained_relative_factor=str(retained),strict_threshold_margin=str(lower-threshold),all_convex_fusions_fail_next_lower_dyadic_factor=True,all_convex_fusions_fail_inherited_scalar_gate=True))
 result=dict(milestone='RC87',status='PASS',input_sha256=hashes,actual_Riesz_projection_head_rank=38,canonical_trial_dimension=DIM,source_input_features=list(range(N)),
  nominal_normal_equation_defect=serialize(d),nominal_midpoint_metric_maximal_capture_gain_Loewner_upper=serialize(nominal_up),nominal_gain_rounding_row_allowances=list(map(str,nround)),
  actual_metric_nominal_source_maximal_trial_response_error_reduction_Loewner_upper=serialize(Omega),actual_gain_rounding_row_allowances=list(map(str,oround)),gain_relative_input_certificates=gains,
  nominal_normal_equation_square_completion_certified=True,actual_trial_correction_gain_bounded_by_certified_orthogonality_defect=True,RC86_orthogonality_defect_preserved_exactly=True,
  convex_fusion_definition='C(theta)=(1-theta) A_RC82_retained + theta A_RC86_candidate; independently for each parity, 0<=theta<=1',all_continuous_convex_fusion_witnesses=witnesses,
  scalar_Schur_source_budget_strict_ceiling_using_inherited_complement_floor=str(ceiling),retained_actual_rank_38_projected_original_source_Gram_Loewner_upper=serialize(A),actual_rank_38_relative_bound_for_existing_22_source_inputs=prior['actual_rank_38_relative_bound_for_existing_22_source_inputs'],
  original_Riesz_trials_unchanged=True,RC83_response_coefficients_unchanged=True,retained_source_upper_unchanged=True,all_continuous_convex_fusions_excluded_at_next_lower_12_step_factor=True,
  obstruction_is_to_certificate_routes_not_actual_source_leakage=True,projected_response_attachment_global_optimality_claimed=False,actual_source_uncertainty_improvement_by_trial_correction_claimed=False,
  required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,thirty_eight_source_input_covariance_evaluated=False,enlarged_Weil_floor_certified=False,enlarged_complement_floor_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert result==saved
 return result
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 names=['rpb108_rc86_complete_head_error_covariance.json','rpb108_rc83_nominal_source_canonical_response.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc82_direct_error_source_attachment.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json']
 defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()))
  print('PASS: exact normal equations and capture square completion; actual trial-correction gain; independent quadratic replay of all continuous convex-fusion witnesses')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
