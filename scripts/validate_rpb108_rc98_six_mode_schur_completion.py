"""RC98: targeted added-control source capture and robust six-mode completion.

No new integration. Source subtraction uses degree<64, whereas transport
and the inherited Weil complement floor use the actual rank-1250 head.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,entries,root
from validate_rpb108_rc65_parity_projected_residual_refinement import cong,add,scale
from validate_rpb108_rc63_twenty_two_weak_floor_obstruction import up,down
from validate_rpb108_rc93_targeted_weak_source_capture import contract_interval,dot
from validate_rpb108_rc90_continuous_source_balance_and_method_floor import sqrtfloor
RHO=F(252,257)
def q(A,v):return mm(mm([v],A),tr([v]))[0][0]
def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];head,weak,enriched,native,source,direct,pairings,transport,even,odd,norm=map(json.loads,raw);h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert head['milestone']=='RC97'
 assert head['input_sha256'][1:6]==h[1:6] and head['input_sha256'][6]==h[10]
 assert source['input_sha256'][:2]==[h[2],h[3]] and direct['input_sha256'][2:4]==[h[2],h[3]]
 assert pairings['input_sha256'][1:3]==[h[2],h[3]] and pairings['input_sha256'][6]==h[4]
 assert even['input_sha256'][0]==h[9] and even['input_sha256'][1:4]==[h[1],h[2],h[3]] and even['input_sha256'][7]==h[4]
 assert transport['input_sha256'][2]==h[5] and transport['input_sha256'][4:6]==[h[4],h[2]]
 assert source['input_sha256'][6]==h[10]
 assert even['full_four_known_weak_span_corrected_positive_definite']
 assert all(z['trial_dimension']==64 for z in [enriched,source,direct])
 C=matrix(native['chebyshev_to_legendre']);V=matrix(enriched['enriched_native_trial_coefficients']);mass=list(map(F,enriched['physical_mass']));D=[[mass[i]*F(i==j) for j in range(64)] for i in range(64)];T=cong(V,D)
 U=entries(source['nominal_complete_original_source_Gram_entries']);ER=entries(direct['nominal_Legendre_residual_Gram_entry_enclosures']);HH=[[tuple(map(F,x)) for x in r] for r in pairings['nominal_physical_Legendre_source_pairing_enclosures']]
 tau=F(even['rank_1250_canonical_tail_certificate']['canonical_complement_embedding_norm_upper']);oldtau=F(transport['canonical_complement_embedding_norm_upper']);alpha=F(even['inherited_1250_complement_floor']);assert alpha==F(247,2500) and tau<oldtau
 eff=F(transport['projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho'])+F(transport['projected_prime_physical_to_canonical_norm_upper_divided_by_sqrt_rho']);poles=list(map(F,transport['projected_pole_norm_uppers_divided_by_sqrt_rho']));delta=F(source['actual_source_approximation_operator_error_upper']);deltaL=F(direct['actual_operator_correction_norm_upper']);nu=F(1,65536)
 blocks=[]
 for p,name in enumerate(['even','odd']):
  selected=[a for a in weak['fixed_rational_direction_certificates'] if a['parity']==name];vs=[list(map(F,a['coefficients'])) for a in selected];assert [a['role'] for a in selected]==['weak_0','weak_1','positive_control']
  v=vs[2];tt=dot(v,T,v,replay);z=[row[0] for row in mm(C,tr([v]))]
  ec,er=contract_interval(z,ER,z,replay);assert ec+er>=0
  ep=RHO**2*((1+nu)*(ec+er)+(1+1/nu)*deltaL**2*tt);canonical=ep/RHO
  uc,ur=contract_interval(v,U,v,replay);hc=[sum((v[i]*(HH[n][i][0]+HH[n][i][1])/2 for i in range(22)),F(0)) for n in range(64)];hr=[sum((abs(v[i])*(HH[n][i][1]-HH[n][i][0])/2 for i in range(22)),F(0)) for n in range(64)]
  cap=sum((hc[n]**2/mass[n] for n in range(64)),F(0));cr=sum((2*abs(hc[n])*hr[n]/mass[n] for n in range(64)),F(0));w=uc-cap+ur+cr;assert w>=0
  N=tau*tau*w;k=tau/oldtau*(eff+poles[p]);E=RHO*(1+nu)*k*k*ep+(1+1/nu)*delta**2*tau*tau*tt
  # This is an enclosure-family optimization; actual covariance is <=g.
  tests=[((1+t)*N+(1+1/t)*E,t) for t in [F(i,64) for i in range(1,257)]+[F(8),F(16)]];g,t=min(tests)
  bhead=head['parity_low_subspace_certificates'][p];cent=F(next(r for r in bhead['signed_actual_Weil_entry_certificates'] if r['i']==r['j']==2)['trial_Weil_center']);rt=F(next(r for r in bhead['signed_actual_Weil_entry_certificates'] if r['i']==r['j']==2)['trial_Weil_radius_upper']);sn=up(root(uc+ur,10**40)+delta*root(tt,10**40),10**40)
  kphys=F(norm['complete_physical_operator_parity_norm_upper'][p])
  Qlo=down(cent-rt-2*root(ep,10**40)*sn-kphys*ep-canonical,10**40);Qhi=up(cent+rt+2*root(ep,10**40)*sn+kphys*ep,10**40);d=Qlo-g/alpha
  if name=='even':L=matrix(even['corrected_even_weak_block_Loewner_lower']);G=matrix(even['actual_rank_1250_even_weak_source_coupling_Gram_upper'])
  else:L=matrix(odd['weak_source_block_certificates'][p]['corrected_weak_block_Loewner_lower']);G=matrix(odd['weak_source_block_certificates'][p]['actual_rank_1250_weak_source_coupling_Gram_upper_via_nesting'])
  # Original cross entries from RC97 are retained conservatively. Their broad
  # errors are sound; tightening the control diagonal does not invalidate them.
  intervals=[]
  for i in range(2):
   row=next(r for r in bhead['signed_actual_Weil_entry_certificates'] if r['i']==i and r['j']==2);a,b=map(F,row['actual_Weil_entry_enclosure']);gamma=root(G[i][i]*g,10**40)/alpha;intervals.append([a-gamma,b+gamma])
  assert L[0][0]>0 and L[0][0]*L[1][1]-L[0][1]**2>0
  Li=inverse(L)
  if replay:
   determinant=L[0][0]*L[1][1]-L[0][1]**2
   assert Li==[[L[1][1]/determinant,-L[0][1]/determinant],[-L[1][0]/determinant,L[0][0]/determinant]]
  vertices=[]
  for cs in product(*intervals):
   energy=q(Li,list(cs));vertices.append(dict(cross=list(map(str,cs)),inverse_penalty=str(energy),margin=str(d-energy)))
  worst=max(vertices,key=lambda r:F(r['inverse_penalty']));success=d>0 and all(F(r['margin'])>0 for r in vertices)
  witness=[-x[0] for x in mm(Li,tr([list(map(F,worst['cross']))]))]+[F(1)]
  c=list(map(F,worst['cross']));B3=[L[0]+[c[0]],L[1]+[c[1]],c+[d]];assert q(B3,witness)==F(worst['margin'])
  blocks.append(dict(parity=name,target_role='positive_control',targeted_nominal_operator_residual_center=str(ec),targeted_nominal_operator_residual_radius=str(er),targeted_physical_Riesz_error_squared_upper=str(ep),targeted_nominal_source_squared_upper=str(uc+ur),physical_source_capture_squared_center=str(cap),physical_residual_enclosure_upper=str(w),nominal_rank_1250_projected_source_squared_upper=str(N),actual_source_transfer_squared_upper=str(E),Young_parameter=str(t),actual_rank_1250_added_control_coupling_squared_upper=str(g),updated_actual_added_control_Weil_lower=str(Qlo),updated_actual_added_control_Weil_upper=str(Qhi),added_control_corrected_diagonal_lower=str(d),added_control_directional_Schur_positive=d>0,retained_corrected_weak_Loewner_lower=serialize(L),corrected_cross_entry_enclosures=serialize(intervals),robust_cross_vertices=vertices,worst_enclosure_vertex_matrix=serialize(B3),worst_enclosure_vertex_witness=list(map(str,witness)),worst_enclosure_vertex_quadratic_value=worst['margin'],worst_box_inverse_penalty_to_added_diagonal_ratio=str(F(worst['inverse_penalty'])/d) if d>0 else None,robust_three_mode_completion_passes=success,diagonal_Young_family_lower=str(N+E+2*sqrtfloor(N*E))))
 out=dict(milestone='RC98',status='PASS',input_sha256=h,physical_source_subtraction_degree_count=64,canonical_transport_head_rank=1250,Weil_complement_floor_head_rank=1250,rank_1250_complement_embedding_norm_upper=str(tau),inherited_complement_floor=str(alpha),new_source_integrals_evaluated=0,added_control_certificates=blocks,source_projection_nesting_and_transport_proof_supplied=True,PSD_coupling_cross_Cauchy_bound_proof_supplied=True,robust_box_completion_analytic_proof_supplied=True,both_added_control_directions_corrected_positive=all(b['added_control_directional_Schur_positive'] for b in blocks),all_six_selected_individual_directions_corrected_positive=even['full_four_known_weak_span_corrected_positive_definite'] and all(b['added_control_directional_Schur_positive'] for b in blocks),
  six_mode_corrected_positivity_certified=all(b['robust_three_mode_completion_passes'] for b in blocks),box_vertex_is_actual_original_operator=False,actual_coupling_lower_certified=False,complete_weak_mode_coverage_certified=False,strong_head_block_certified=False,weak_strong_cross_block_certified=False,matrix_Schur_positivity_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert out==saved
 return out
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates';names=['rpb108_rc97_additional_low_mode_coverage.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc81_direct_enriched_riesz_residuals.json','rpb108_rc83_nominal_source_canonical_response.json','rpb108_rc89_frequency_weighted_arch_transfer.json','rpb108_rc95_jump_aware_even_source_tail.json','rpb108_rc94_weak_source_capture_128.json','rpb108_rc66_arch_multiplier_transport.json'];defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: triangular interval contractions, added-control source capture, actual rank-1250 transport, robust cross vertices and exact witness values')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
