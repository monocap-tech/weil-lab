"""RC102: six-response completion and a quantified norm-transport boundary.

All failure witnesses concern sufficient upper matrices, not the actual
original arithmetic cross block or a negative original Weil direction.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,entries
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,cong
from validate_rpb108_rc93_targeted_weak_source_capture import contract_interval,dot
from validate_rpb108_rc99_signed_source_projection_bounds import upper
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc97_additional_low_mode_coverage import pd
from validate_rpb108_rc63_twenty_two_weak_floor_obstruction import up,down
RHO=F(252,257);N=3

def adjugate3(a):
 # Cyclic minors already contain their alternating signs.
 cof=[[a[(i+1)%3][(j+1)%3]*a[(i+2)%3][(j+2)%3]-a[(i+1)%3][(j+2)%3]*a[(i+2)%3][(j+1)%3] for j in range(3)] for i in range(3)]
 det=sum((a[0][j]*cof[0][j] for j in range(3)),F(0));assert det>0
 return [[cof[j][i]/det for j in range(3)] for i in range(3)]

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];new,even,tail,weak,enriched,native,source,pairings,norm,interface=map(json.loads,raw);h=[hashlib.sha256(a).hexdigest() for a in raw]
 assert new['milestone']=='RC101' and even['milestone']=='RC100' and new['input_sha256'][0]==h[1]
 assert [new['input_sha256'][i] for i in [2,5,6,7,11,13,15]]==[h[i] for i in [2,3,4,5,6,7,8]]
 assert even['input_sha256']==new['input_sha256'][1:]
 assert [pairings['input_sha256'][i] for i in [1,2,6,7]]==[h[i] for i in [4,5,6,8]]
 assert source['input_sha256'][:2]==h[4:6]
 assert F(native['actual_canonical_native_Gram_physical_upper_factor'])==RHO
 assert interface['milestone']=='RC96' and interface['input_sha256'][0]==h[2]
 assert new['six_mode_corrected_positivity_certified'] and new['certified_corrected_span_dimension']==6
 assert even['corrected_even_three_mode_positive_certified']
 assert tail['parity_orthogonality_analytic_proof_supplied']
 alpha=F(tail['inherited_1250_complement_floor']);tau=F(tail['rank_1250_canonical_tail_certificate']['canonical_complement_embedding_norm_upper']);assert alpha==F(247,2500)
 V=matrix(enriched['enriched_native_trial_coefficients']);C=matrix(native['chebyshev_to_legendre']);P=matrix(native['physical_native_Gram']);mass=list(map(F,enriched['physical_mass']));T=cong(V,[[mass[i]*F(i==j) for j in range(64)] for i in range(64)])
 assert P==cong(C,[[mass[i]*F(i==j) for j in range(22)] for i in range(22)])
 U=entries(source['nominal_complete_original_source_Gram_entries']);H=[[tuple(map(F,x)) for x in row] for row in pairings['nominal_physical_Legendre_source_pairing_enclosures']]
 delta=F(source['actual_source_approximation_operator_error_upper']);nu=F(1,65536);rows=[]
 for p,parity in enumerate(['even','odd']):
  cert=[even,new][p];vs=[list(map(F,z['coefficients'])) for z in weak['fixed_rational_direction_certificates'] if z['parity']==parity];assert len(vs)==3
  W=tr(vs);q=mm(C,W);Mq=cong(W,P);assert pd(Mq)
  Mi=adjugate3(Mq) if replay else inverse(Mq);assert mm(Mq,Mi)==[[F(i==j) for j in range(3)] for i in range(3)]
  hc=[[F(0)]*3 for _ in range(3)];hr=[[F(0)]*3 for _ in range(3)]
  for i in range(3):
   for j in range(3):
    pairs=[(q[n][i]*vs[j][k],H[n][k]) for n in range(22) for k in range(22)]
    if replay:pairs=list(reversed(pairs))
    hc[i][j]=sum((v*(a+b)/2 for v,(a,b) in pairs),F(0));hr[i][j]=sum((abs(v)*(b-a)/2 for v,(a,b) in pairs),F(0))
  Z=mm(Mi,hc);assert mm(Mq,Z)==hc
  uc=[[F(0)]*3 for _ in range(3)];ur=[[F(0)]*3 for _ in range(3)]
  for i in range(3):
   for j in range(i,3):uc[i][j],ur[i][j]=contract_interval(vs[i],U,vs[j],replay);uc[j][i]=uc[i][j];ur[j][i]=ur[i][j]
  capture=mm(tr(hc),Z)
  if replay:
   rc=add(add(add(uc,mm(tr(hc),Z),-1),mm(tr(Z),hc),-1),mm(mm(tr(Z),Mq),Z))
  else:rc=add(uc,capture,-1)
  assert rc==add(uc,capture,-1)
  rr=[[ur[i][j]+sum((abs(Z[k][i])*hr[k][j]+hr[k][i]*abs(Z[k][j]) for k in range(3)),F(0)) for j in range(3)] for i in range(3)]
  ds=[F(10000 if p==0 else 8000),F(100),F(1)];RU=upper(rc,rr,ds,replay);RU,_=rounded_bound(RU,1,10**40)
  tw=[[dot(v,T,w,replay) for w in vs] for v in vs];Ep=matrix(cert['common_actual_physical_Riesz_error_Gram_upper']);kappa=F(norm['complete_physical_operator_parity_norm_upper'][p])
  Ephys=add(scale(Ep,(1+nu)*kappa*kappa),tw,(1+1/nu)*delta*delta);Ephys,_=rounded_bound(Ephys,1,10**40)
  UA=scale(add(RU,Ephys),2*RHO);UA,_=rounded_bound(UA,1,10**40)
  Q=matrix(cert['actual_original_'+parity+'_three_mode_Weil_head_Loewner_lower']);G=matrix(cert['common_actual_rank_1250_source_coupling_Gram_upper']);L=matrix(cert['corrected_'+parity+'_three_mode_Loewner_lower']);assert L==add(Q,G,-1/alpha) and pd(L) and psd(G)
  Li=adjugate3(L) if replay else inverse(L);assert mm(L,Li)==[[F(i==j) for j in range(3)] for i in range(3)]
  # Correlated 3+1 abstract controls, with a nonidentity canonical metric.
  c=[L[i][0]/2 for i in range(3)];d=L[0][0];A=[L[i]+[c[i]] for i in range(3)]+[c+[d]]
  MI=[[F(i==j)/[2,3,5,7][i] for j in range(4)] for i in range(4)];RW=mm(mm(A,MI),A);captureW=mm(mm(L,[r[:3] for r in MI[:3]]),L)
  residual=add([r[:3] for r in RW[:3]],captureW,-1);expected=[[a*b/7 for b in c] for a in c]
  if replay:assert residual==[[7*(a/7)*(b/7) for b in c] for a in c]
  assert residual==expected and pd(A) and pd(add(scale(L,d/7),residual,-1))
  cb=[L[i][0] for i in range(3)];boundary=[L[i]+[cb[i]] for i in range(3)]+[cb+[d]];w0=[F(-1),F(0),F(0),F(1)]
  assert psd(boundary) and dot(w0,boundary,w0,replay)==0 and not pd(boundary)
  g=RHO*tau*tau*kappa*kappa;beta_max=1+RHO*kappa;VG=scale(G,g/alpha**2);axes=[]
  for i in range(3):
   ratio=VG[i][i]/L[i][i];margin=VG[i][i]-beta_max*L[i][i];assert margin>0
   axes.append(dict(axis=i,correction_upper_to_weak_lower_ratio_lower=str(down(ratio,10**20)),largest_possible_strong_floor=str(beta_max),excess_ratio_lower=str(down(ratio/beta_max,10**20)),negative_completion_margin_upper=str(up(-margin,10**40))))
  traceA=sum(mm(Li,UA)[i][i] for i in range(3));traceG=sum(mm(Li,VG)[i][i] for i in range(3));assert traceA>=0 and traceG>3*beta_max
  family=[]
  for t in [F(1,16),F(1,4),F(1),F(4),F(16)]:
   total=add(scale(UA,1+t),VG,1+1/t);assert psd(total) and total[0][0]>beta_max*L[0][0]
   family.append(dict(Young_parameter=str(t),completion_axis_0_margin_at_universal_strong_ceiling=str(up(beta_max*L[0][0]-total[0][0],10**40))))
  rows.append(dict(parity=parity,physical_target_Gram=serialize(Mq),physical_nominal_source_target_pairing_center=serialize(hc),physical_nominal_source_target_pairing_radius=serialize(hr),physical_least_squares_target_subtraction_coefficients=serialize(Z),nominal_physical_source_residual_center=serialize(rc),nominal_physical_source_residual_radius=serialize(rr),nominal_physical_source_residual_Gram_upper=serialize(RU),actual_physical_source_error_Gram_upper=serialize(Ephys),actual_original_strong_response_Gram_upper=serialize(UA),corrected_weak_lower_inherited_exactly=True,inverse_corrected_weak_lower_recomputed_and_verified=True,complete_head_complement_cross_operator_norm_squared_upper=str(g),corrected_source_norm_transport_Gram_upper=serialize(VG),universal_corrected_strong_floor_ceiling=str(beta_max),correction_trace_budget_lower_for_all_positive_Young_parameters=str(down(traceG,10**20)),original_response_trace_upper=str(up(traceA,10**20)),axis_norm_transport_obstructions=axes,sample_Young_family=family,all_positive_Young_norm_transport_completion_rejected=True,abstract_three_mode_correlated_completion_control_passes=True,abstract_metric_response_capture_identity_verified=True,abstract_cross_boundary_null_verified=True,abstract_controls_scope='illustrative forms and metrics, not additional original arithmetic certificates'))
 # Squaring a positive lower matrix does not preserve Loewner order.
 base=[[F(2),F(0)],[F(0),F(1)]];larger=[[F(3),F(1)],[F(1),F(2)]];difference=add(mm(larger,larger),mm(base,base),-1);w=[F(5),F(-6)]
 assert pd(base) and pd(larger) and psd(add(larger,base,-1)) and dot(w,difference,w,replay)==-6 and not psd(difference)
 t=F(1,1000);v=[2*t/(1+t*t),(1-t*t)/(1+t*t)];GP=[[a*b for b in v] for a in v];gamma=GP[0][0];retained=GP[0][1]**2
 assert sum((a*a for a in v),F(0))==1 and mm(GP,GP)==GP and psd(GP) and retained==gamma*(1-gamma) and retained/gamma>F(99999,100000)
 out=dict(milestone='RC102',status='PASS',input_sha256=h,arithmetic='exact Fraction; no floating acceptance',head_rank=1250,certified_corrected_weak_dimension=6,remaining_head_dimension=1244,original_operator_nonpositive_spectral_dimension_upper=1244,inherited_complement_floor=str(alpha),parity_completion_certificates=rows,
 six_response_completion_theorem='For T_alpha=P_H A_Q P_H-alpha^(-1)P_H A_Q P_E A_Q P_H, W the certified six-dimensional span, S=H orthogonal W, and L<=W*T_alpha W positive: D=T_alpha|S>=beta I and U>=Gram(P_S T_alpha W) with beta L-U positive imply original Weil positivity.',
 fused_response_identity='P_S T_alpha W=P_S A_Q(W-alpha^(-1)P_E A_Q W).',
 exact_response_capture_identity='Gram(P_S T_alpha W)=W*T_alpha^2 W-B M_W^(-1)B, B=W*T_alpha W, M_W=W*W; actual metric and actual B required.',
 physical_subtraction_identity='P_S P_H A_Q W=P_S i*(F_actual-qZ), since i*qZ=WZ is annihilated; no actual weak capture inversion required.',
 generic_correction_transport_theorem='Gram(P_S Gamma_H W)<=g Gamma_W<=g G, g=rho*tau1250^2*kappa^2. Therefore Gram(P_S T_alpha W)<=(1+t)UA+(1+1/t)g G/alpha^2 for t>0.',
 projection_and_transport_analytic_proofs_supplied=True,new_source_integrals_evaluated=0,dense_remaining_head_evaluation_required_by_completion_criterion=False,
 actual_original_strong_response_Gram_upper_certified=True,actual_corrected_strong_response_Gram_upper_certified=True,generic_upper_sufficient_completion_passes=False,norm_transport_upper_architecture_failure_certified=True,lower_bounds_are_on_upper_enclosure_family_not_actual_cross=True,
 norm_transport_near_sharp_abstract_control=dict(positive_contraction=serialize(GP),weak_compression=str(gamma),strong_correction_response_squared=str(retained),norm_envelope=str(gamma),retained_fraction=str(1-gamma),scope='abstract positive contraction; not the original arithmetic operator or its joint source constraints'),
 squared_capture_lower_counterexample=dict(lower=serialize(base),larger=serialize(larger),square_difference=serialize(difference),negative_witness=list(map(str,w)),quadratic_value='-6',scope='abstract matrix-order counterexample, not the original operator'),
 complete_weak_mode_coverage_certified=False,strong_head_block_certified=False,weak_strong_cross_block_sufficient_completion_certified=False,matrix_Schur_positivity_certified=False,whole_aperture_positivity_extended=False,actual_negative_or_null_direction_certified=False,RH=False,F4=False)
 if saved is not None:assert out==saved
 return out

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates';names=['rpb108_rc101_odd_three_mode_jump_tail.json','rpb108_rc100_even_three_mode_jump_tail.json','rpb108_rc95_jump_aware_even_source_tail.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc83_nominal_source_canonical_response.json','rpb108_rc66_arch_multiplier_transport.json','rpb108_rc96_weak_strong_completion_budget.json'];defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: adjugate inverses, expanded residual Gram, reordered source contractions, exact all-Young upper-architecture obstructions')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
