"""RC97: six-dimensional signed Rayleigh ceiling and strong-floor obstruction.

Uses only matching RC67/68 trials and RC81 actual Riesz error bounds.
Dimension arguments give low strong directions without approximate projection.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,root
from validate_rpb108_rc65_parity_projected_residual_refinement import cong,add,scale
from validate_rpb108_rc63_twenty_two_weak_floor_obstruction import up,down
from validate_rpb108_rc92_signed_weak_head_reconstruction import bil
from validate_rpb108_rc90_continuous_source_balance_and_method_floor import relative40

def pd(A):
 B=[r[:] for r in A]
 for k in range(len(B)):
  if B[k][k]<=0:return False
  for i in range(k+1,len(B)):
   for j in range(k+1,len(B)):B[i][j]-=B[i][k]*B[k][j]/B[k][k]
 return True

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];prior,weak,enriched,native,source,residual,transport,compact=map(json.loads,raw)
 h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['milestone']=='RC96' and prior['known_weak_dimension']==4
 assert compact['milestone']=='RC77' and compact['canonical_embedding_and_adjoint_compactness_analytic_proof_supplied']
 assert source['input_sha256'][:2]==[h[2],h[3]] and source['input_sha256'][6]==h[6]
 assert residual['input_sha256'][2:4]==[h[2],h[3]]
 assert enriched['input_sha256'][3]==source['input_sha256'][2]==residual['input_sha256'][4]
 assert source['trial_dimension']==enriched['trial_dimension']==residual['trial_dimension']==64
 V=matrix(enriched['enriched_native_trial_coefficients']);C=matrix(native['chebyshev_to_legendre']);G=matrix(enriched['recentered_nominal_metric_center']);mass=list(map(F,enriched['physical_mass']))
 D=[[mass[i]*F(i==j) for j in range(64)] for i in range(64)]
 X=[[mass[i]*C[i][j] if i<22 else F(0) for j in range(22)] for i in range(64)]
 T=cong(V,D);J=mm(tr(X),V);GT=cong(V,G)
 H=matrix(source['nominal_original_trial_source_pairing_center']);Rh=matrix(source['nominal_original_trial_source_pairing_halfwidths'])
 Q0=add(add(GT,H),tr(J),-1)
 Q0=[[(Q0[i][j]+Q0[j][i])/2 for j in range(22)] for i in range(22)]
 Rh=[[(Rh[i][j]+Rh[j][i])/2 for j in range(22)] for i in range(22)]
 Ep=matrix(residual['actual_physical_Riesz_error_Gram_Loewner_upper']);Ec=matrix(residual['actual_canonical_Riesz_error_Gram_Loewner_upper']);U=matrix(source['nominal_complete_original_source_Gram_Loewner_upper']);M=matrix(enriched['enriched_actual_native_Gram_Loewner_lower'])
 delta=F(source['actual_source_approximation_operator_error_upper']);dg=F(enriched['actual_recentered_metric_mass_error_upper']);ks=list(map(F,transport['complete_physical_operator_parity_norm_upper']))
 assert all(psd(A) for A in [T,Ep,Ec,U,M]);oldfloor=F(weak['retained_actual_low_eight_uniform_floor']);assert oldfloor==F(1,2900000)
 blocks=[]
 for p,name in enumerate(['even','odd']):
  selected=[a for a in weak['fixed_rational_direction_certificates'] if a['parity']==name]
  assert [a['role'] for a in selected]==['weak_0','weak_1','positive_control']
  vs=[list(map(F,a['coefficients'])) for a in selected]
  assert all(v[i]==0 for v in vs for i in range(22) if i%2!=p)
  def contract(A):return [[bil(v,A,w,replay) for w in vs] for v in vs]
  tw,ep,ec,uw,qc,ml=map(contract,[T,Ep,Ec,U,Q0,M]);assert pd(ml)
  sn=[up(root(uw[i][i],10**40)+delta*root(tw[i][i],10**40),10**40) for i in range(3)]
  lo=[[F(0)]*3 for _ in range(3)];hi=[[F(0)]*3 for _ in range(3)];ent=[]
  for i in range(3):
   for j in range(i,3):
    rt=bil(list(map(abs,vs[i])),Rh,list(map(abs,vs[j])),replay)+(delta+dg)*root(tw[i][i]*tw[j][j],10**40)
    linear=root(ep[i][i],10**40)*sn[j]+root(ep[j][j],10**40)*sn[i]
    physical=ks[p]*root(ep[i][i]*ep[j][j],10**40)
    canonical=ec[i][i] if i==j else root(ec[i][i]*ec[j][j],10**40)
    a=down(qc[i][j]-rt-linear-physical-canonical,10**40)
    b=up(qc[i][j]+rt+linear+physical+(canonical if i!=j else 0),10**40)
    lo[i][j]=lo[j][i]=a;hi[i][j]=hi[j][i]=b
    ent.append(dict(i=i,j=j,trial_Weil_center=str(qc[i][j]),trial_Weil_radius_upper=str(rt),linear_source_allowance=str(linear),physical_quadratic_allowance=str(physical),canonical_error_allowance=str(canonical),actual_Weil_entry_enclosure=[str(a),str(b)]))
  mid=[[(lo[i][j]+hi[i][j])/2 for j in range(3)] for i in range(3)];rad=[[(hi[i][j]-lo[i][j])/2 for j in range(3)] for i in range(3)];ds=[F(100 if p==0 else 80),F(1),F(1)]
  rows=[sum((rad[i][j]*ds[j]/ds[i] for j in range(3)),F(0)) for i in range(3)]
  upper=[[mid[i][j]+F(i==j)*rows[i] for j in range(3)] for i in range(3)]
  if replay:
   P=[[ds[i]*F(i==j) for j in range(3)] for i in range(3)];margin=cong(P,add(upper,mid,-1))
   assert all(margin[i][i]==sum((ds[i]*ds[j]*rad[i][j] for j in range(3)),F(0)) for i in range(3))
  # Scale to resolve the tiny generalized ceiling before exact bisection.
  eta=relative40(scale(upper,F(10**9)),ml)/10**9
  assert 0<eta<oldfloor and psd(add(scale(ml,eta),upper,-1))
  if saved is not None:
   expected=F(saved['parity_low_subspace_certificates'][p]['whole_subspace_actual_canonical_Rayleigh_upper'])
   assert eta==expected
  blocks.append(dict(parity=name,roles=[a['role'] for a in selected],fixed_native_coefficients=[a['coefficients'] for a in selected],signed_actual_Weil_entry_certificates=ent,actual_Weil_entry_lower=serialize(lo),actual_Weil_entry_upper=serialize(hi),interval_balancing_scales=list(map(str,ds)),actual_Weil_Loewner_upper=serialize(upper),actual_canonical_Gram_Loewner_lower=serialize(ml),whole_subspace_actual_canonical_Rayleigh_upper=str(eta),strictly_below_old_low_eight_floor=True,actual_subspace_dimension=3,canonical_strong_intersection_dimension_lower=1,corrected_strong_floor_upper=str(eta),known_weak_span_dimension=2))
 out=dict(milestone='RC97',status='PASS',input_sha256=h,arithmetic='exact Fraction; inherited directed source enclosures',trial_dimension=64,actual_test_subspace_dimension=6,new_source_integrals_evaluated=0,parity_low_subspace_certificates=blocks,retained_low_eight_floor=str(oldfloor),six_dimensional_actual_Rayleigh_upper=str(max(F(b['whole_subspace_actual_canonical_Rayleigh_upper']) for b in blocks)),original_operator_eigenvalues_at_or_below_reported_ceiling_count_lower=6,additional_low_strong_directions_dimension_lower=2,uniform_corrected_strong_floor_upper=str(min(F(b['corrected_strong_floor_upper']) for b in blocks)),old_low_eight_floor_ruled_out_on_corrected_strong_complement=True,canonical_orthogonal_projection_numerically_approximated=False,dimension_intersection_analytic_proof_supplied=True,compact_operator_minmax_analytic_proof_supplied=True,actual_negative_or_null_direction_certified=False,complete_weak_mode_coverage_certified=False,strong_head_block_certified=False,weak_strong_cross_block_certified=False,matrix_Schur_positivity_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert out==saved
 return out

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 names=['rpb108_rc96_weak_strong_completion_budget.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc81_direct_enriched_riesz_residuals.json','rpb108_rc66_arch_multiplier_transport.json','rpb108_rc77_canonical_adjoint_tail.json'];defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: column-first signed contractions, metric independence, weighted interval upper, and both exact three-mode Rayleigh ceilings')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
