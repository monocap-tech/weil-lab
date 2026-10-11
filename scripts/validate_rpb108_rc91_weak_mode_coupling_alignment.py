"""RC91: exact coupling alignment on RC63's two weak modes per parity.

Rank-38 coupling upper also bounds rank-1250 coupling by nested actual
projections. The inherited complement floor is only for rank 1250.
No head positivity, complete weak-mode coverage or actual leakage lower.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,cong
from validate_rpb108_rc90_continuous_source_balance_and_method_floor import relative40
N=22
def bilinear(v,A,w,replay):
 if replay:return sum((v[i]*A[i][i]*w[i]+sum(((v[i]*w[j]+v[j]*w[i])*A[i][j] for j in range(i+1,N)),F(0)) for i in range(N)),F(0))
 return mm(mm([v],A),[[x] for x in w])[0][0]
def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];prior,weak,enriched,native=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['milestone']=='RC90' and prior['input_sha256'][1:]==[hashes[i] for i in [2,3,1]]
 assert weak['input_sha256'][0]==hashes[3]
 assert prior['actual_Riesz_projection_head_rank']==38 and prior['source_input_features']==list(range(N))
 G=matrix(prior['refined_actual_rank_38_projected_original_source_Gram_Loewner_upper']);Mlo=matrix(enriched['enriched_actual_native_Gram_Loewner_lower']);P=matrix(native['physical_native_Gram'])
 alpha=F(weak['inherited_1250_complement_floor']);assert alpha>0
 assert all(psd(A) for A in [G,Mlo,P]);directions=[];blocks=[]
 for name in ['even','odd']:
  selected=[r for r in weak['fixed_rational_direction_certificates'] if r['parity']==name and r['role'].startswith('weak')];assert [r['role'] for r in selected]==['weak_0','weak_1']
  vs=[list(map(F,r['coefficients'])) for r in selected];V=tr(vs)
  if replay:
   C=[[bilinear(v,G,w,True) for w in vs] for v in vs];L=[[bilinear(v,Mlo,w,True) for w in vs] for v in vs]
  else:C=cong(V,G);L=cong(V,Mlo)
  assert psd(C) and psd(L) and L[0][0]*L[1][1]-L[0][1]**2>0
  # Scale the small block before relative bisection to retain useful digits.
  lam=relative40(scale(C,F(10**15)),L)/10**15;assert psd(add(scale(L,lam),C,-1))
  penalty=scale(C,1/alpha);plam=lam/alpha;assert psd(add(scale(L,plam),penalty,-1))
  blocks.append(dict(parity=name,weak_roles=['weak_0','weak_1'],weak_basis_native_coefficients=serialize(V),weak_input_canonical_Gram_Loewner_lower=serialize(L),actual_rank_38_weak_source_coupling_Gram_Loewner_upper=serialize(C),actual_rank_1250_weak_source_coupling_Gram_Loewner_upper_via_nesting=serialize(C),weak_coupling_relative_weak_input_Gram_upper=str(lam),inherited_1250_Schur_penalty_Gram_Loewner_upper=serialize(penalty),Schur_penalty_relative_weak_input_Gram_upper=str(plam),all_two_mode_cross_correlations_retained=True,full_two_mode_span_bound_certified=True))
  for j,r in enumerate(selected):
   v=vs[j];cu=C[j][j];normlo=F(r['canonical_native_squared_norm_lower']);assert normlo>0
   qlo=F(r['actual_original_Weil_quadratic_lower']);qhi=F(r['actual_original_Weil_quadratic_upper']);assert qlo<0<qhi
   margin=qlo-cu/alpha;assert margin<0
   directions.append(dict(parity=name,role=r['role'],native_coefficients=list(map(str,v)),actual_rank_38_source_coupling_squared_upper=str(cu),coupling_upper_relative_RC63_canonical_norm_lower=str(cu/normlo),inherited_1250_Schur_penalty_relative_RC63_canonical_norm_lower=str(cu/(alpha*normlo)),actual_original_Weil_quadratic_lower=str(qlo),actual_original_Weil_quadratic_upper=str(qhi),actual_Weil_Rayleigh_lower_using_RC63_norm=str(qlo/normlo),actual_Weil_Rayleigh_upper_using_RC63_norm=str(qhi/normlo),directional_Schur_lower_from_available_enclosures=str(margin),Schur_penalty_upper_divided_by_positive_Weil_quadratic_upper=str(cu/(alpha*qhi)),head_sign_unresolved=True,directional_Schur_positivity_certified=False))
 # Actual heads i*P_<38 and i*P_<1250 are nested by polynomial inclusion.
 # ||(I-Pi1250)S v||^2 <= ||(I-Pi38)S v||^2 for every input v.
 result=dict(milestone='RC91',status='PASS',input_sha256=hashes,source_input_features=list(range(N)),coupling_projection_head_rank_evaluated=38,complement_floor_projection_head_rank=1250,inherited_1250_complement_floor=str(alpha),
  weak_mode_definition='the four fixed RC63 directions weak_0 and weak_1 in each parity; two-dimensional span in each parity',weak_mode_direction_certificates=directions,full_weak_mode_block_certificates=blocks,
  source_Gram_unchanged_from_RC90=True,actual_rank_38_relative_bound_for_existing_22_source_inputs=prior['actual_rank_38_relative_bound_for_existing_22_source_inputs'],
  actual_projection_nesting_analytic_proof_supplied=True,rank_38_coupling_is_an_upper_for_rank_1250_coupling=True,rank_38_coupling_identified_with_rank_1250_coupling=False,inherited_1250_floor_applied_to_rank_38_complement=False,
  weak_mode_coupling_is_certified_small=True,original_weak_head_signs_certified=False,complete_1250_head_weak_mode_coverage_certified=False,strong_head_block_positivity_certified=False,weak_strong_head_cross_block_certified=False,
  matrix_Schur_positivity_certified=False,required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert result==saved
 return result
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 names=['rpb108_rc90_continuous_source_balance_and_method_floor.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json']
 defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()))
  print('PASS: independent symmetric bilinear weak-block contraction; all exact covariance, Gram, penalty and projection-scope checks')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
