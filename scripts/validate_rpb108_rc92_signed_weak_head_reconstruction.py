"""RC92: six signed actual Weil entries on the fixed RC63 weak spans.

Uses matching 64-mode source pairings and RC81 errors. No dense enlarged
head, complete weak-mode coverage, or full matrix Schur claim.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,root
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,cong
from validate_rpb108_rc63_twenty_two_weak_floor_obstruction import up,down

def bil(v,A,w,replay=False):
 if replay:return sum((sum((v[i]*A[i][j]*w[j] for i in range(len(v))),F(0)) for j in range(len(w))),F(0))
 return mm(mm([v],A),tr([w]))[0][0]
def positive(A):return A[0][0]>0 and A[0][0]*A[1][1]-A[0][1]**2>0

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];prior,weak,enriched,native,source,residual,transport=map(json.loads,raw)
 h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['input_sha256'][1:]==[h[i] for i in [1,2,3]]
 assert source['input_sha256'][:2]==[h[2],h[3]] and source['input_sha256'][6]==h[6]
 assert residual['input_sha256'][2:4]==[h[2],h[3]]
 assert enriched['input_sha256'][3]==source['input_sha256'][2]==residual['input_sha256'][4]
 assert source['trial_dimension']==enriched['trial_dimension']==residual['trial_dimension']==64
 V=matrix(enriched['enriched_native_trial_coefficients']);C=matrix(native['chebyshev_to_legendre']);G=matrix(enriched['recentered_nominal_metric_center']);mass=list(map(F,enriched['physical_mass']))
 D=[[mass[i]*F(i==j) for j in range(64)] for i in range(64)]
 X=[[mass[i]*C[i][j] if i<22 else F(0) for j in range(22)] for i in range(64)]
 T=cong(V,D);J=mm(tr(X),V);GT=cong(V,G)
 H=matrix(source['nominal_original_trial_source_pairing_center']);Rh=matrix(source['nominal_original_trial_source_pairing_halfwidths'])
 # H_ij=<V_i,q_j+Knom V_j>. Thus Qtrial=V*L V+H-J*.
 Q0=add(add(GT,H),tr(J),-1)
 # Pairing serialization can break center symmetry by <= its paid radii.
 Q0=[[ (Q0[i][j]+Q0[j][i])/2 for j in range(22)] for i in range(22)]
 Rh=[[ (Rh[i][j]+Rh[j][i])/2 for j in range(22)] for i in range(22)]
 Ep=matrix(residual['actual_physical_Riesz_error_Gram_Loewner_upper']);Ec=matrix(residual['actual_canonical_Riesz_error_Gram_Loewner_upper']);U=matrix(source['nominal_complete_original_source_Gram_Loewner_upper'])
 delta=F(source['actual_source_approximation_operator_error_upper']);dg=F(enriched['actual_recentered_metric_mass_error_upper']);ks=list(map(F,transport['complete_physical_operator_parity_norm_upper']))
 assert all(psd(A) for A in [T,Ep,Ec,U]) and min(delta,dg)>0
 blocks=[];directions=[]
 for p,name in enumerate(['even','odd']):
  selected=[a for a in weak['fixed_rational_direction_certificates'] if a['parity']==name and a['role'].startswith('weak')];vs=[list(map(F,a['coefficients'])) for a in selected];W=tr(vs)
  contraction=lambda A:[[bil(v,A,w,replay) for w in vs] for v in vs]
  tw=contraction(T);ep=contraction(Ep);ec=contraction(Ec);uw=contraction(U);qc=contraction(Q0)
  assert all(psd(A) for A in [tw,ep,ec,uw])
  sn=[up(root(uw[i][i],10**40)+delta*root(tw[i][i],10**40),10**40) for i in range(2)]
  entries=[];lo=[[F(0)]*2 for _ in range(2)];hi=[[F(0)]*2 for _ in range(2)]
  for i in range(2):
   for j in range(i,2):
    tradius=bil(list(map(abs,vs[i])),Rh,list(map(abs,vs[j])),replay)+(delta+dg)*root(tw[i][i]*tw[j][j],10**40)
    linear=root(ep[i][i],10**40)*sn[j]+root(ep[j][j],10**40)*sn[i]
    physical=ks[p]*root(ep[i][i]*ep[j][j],10**40)
    canonical=ec[i][i] if i==j else root(ec[i][i]*ec[j][j],10**40)
    a=down(qc[i][j]-tradius-linear-physical-canonical,10**40)
    b=up(qc[i][j]+tradius+linear+physical+(canonical if i!=j else 0),10**40)
    lo[i][j]=lo[j][i]=a;hi[i][j]=hi[j][i]=b
    if replay:
     assert linear>=root(ep[i][i],10**40)*sn[j]+root(ep[j][j],10**40)*sn[i]
     assert a<=qc[i][j]-tradius-linear-physical-canonical and b>=qc[i][j]+tradius+linear+physical+(canonical if i!=j else 0)
    entries.append(dict(i=i,j=j,trial_Weil_center=str(qc[i][j]),trial_Weil_radius_upper=str(tradius),linear_original_source_allowance=str(linear),physical_quadratic_allowance=str(physical),canonical_error_allowance=str(canonical),actual_original_Weil_lower=str(a),actual_original_Weil_upper=str(b)))
  # Weighted symmetric interval matrix -> Loewner lower. Fixed rational
  # scales balance disparate head magnitudes; every radius is paid.
  d=[F(100 if p==0 else 80),F(1)]
  mid=[[(lo[i][j]+hi[i][j])/2 for j in range(2)] for i in range(2)]
  rad=[[(hi[i][j]-lo[i][j])/2 for j in range(2)] for i in range(2)]
  row=[sum((rad[i][j]*d[j]/d[i] for j in range(2)),F(0)) for i in range(2)]
  lower=[[mid[i][j]-F(i==j)*row[i] for j in range(2)] for i in range(2)]
  Mhi=scale(contraction(matrix(native['physical_native_Gram'])),F(native['actual_canonical_native_Gram_physical_upper_factor']))
  # Exact lower bisection; 1e15 scaling resolves very small positive floors.
  left,right=F(0),F(1);scaled=scale(lower,F(10**15));assert psd(scaled) and not psd(add(scaled,Mhi,-1))
  for _ in range(40):
   middle=(left+right)/2
   if psd(add(scaled,scale(Mhi,middle),-1)):left=middle
   else:right=middle
  floor=left/10**15;assert floor>0 and psd(add(lower,scale(Mhi,floor),-1))
  coupling=matrix(prior['full_weak_mode_block_certificates'][p]['inherited_1250_Schur_penalty_Gram_Loewner_upper']);corrected=add(lower,coupling,-1)
  if replay:
   # Verify Gershgorin domination after the explicit diagonal congruence.
   D2=[[d[i]*F(i==j) for j in range(2)] for i in range(2)]
   margin=cong(D2,add(mid,lower,-1));assert all(margin[i][i]==sum((d[i]*d[j]*rad[i][j] for j in range(2)),F(0)) for i in range(2))
  blocks.append(dict(parity=name,weak_roles=['weak_0','weak_1'],signed_entry_certificates=entries,actual_original_Weil_entry_lower=serialize(lo),actual_original_Weil_entry_upper=serialize(hi),interval_balancing_scales=list(map(str,d)),actual_original_weak_head_Loewner_lower=serialize(lower),weak_head_lower_positive_definite=positive(lower),actual_weak_span_canonical_floor_lower=str(floor),weak_input_canonical_Gram_upper=serialize(Mhi),inherited_1250_Schur_penalty_Gram_upper=serialize(coupling),corrected_weak_block_Loewner_lower=serialize(corrected),corrected_weak_block_lower_positive_definite=positive(corrected)))
  for i,a in enumerate(selected):
   norm=F(a['canonical_native_squared_norm_lower']);normlo=bil(vs[i],matrix(enriched['enriched_actual_native_Gram_Loewner_lower']),vs[i],replay);normhi=F(native['actual_canonical_native_Gram_physical_upper_factor'])*bil(vs[i],matrix(native['physical_native_Gram']),vs[i],replay);assert normhi>=normlo>0;oldwidth=F(a['actual_original_Weil_quadratic_upper'])-F(a['actual_original_Weil_quadratic_lower']);margin=lo[i][i]-coupling[i][i]
   directions.append(dict(parity=name,role=a['role'],actual_original_Weil_quadratic_lower=str(lo[i][i]),actual_original_Weil_quadratic_upper=str(hi[i][i]),canonical_squared_norm_lower=str(normlo),canonical_squared_norm_upper=str(normhi),actual_canonical_Rayleigh_lower=str(lo[i][i]/normhi),actual_canonical_Rayleigh_upper=str(hi[i][i]/normlo),interval_width_improvement_factor=str(oldwidth/(hi[i][i]-lo[i][i])),actual_Weil_direction_certified_positive=lo[i][i]>0,directional_Schur_lower=str(margin),directional_Schur_positivity_certified=margin>0))
 result=dict(milestone='RC92',status='PASS',input_sha256=h,trial_dimension=64,target_direction_count=4,signed_same_parity_entry_count=6,known_weak_head_blocks=blocks,known_weak_direction_certificates=directions,matching_trial_and_source_certificates_used=True,original_source_cancellation_retained=True,all_four_known_weak_direction_signs_positive=all(a['actual_Weil_direction_certified_positive'] for a in directions),both_known_weak_spans_positive=all(a['weak_head_lower_positive_definite'] for a in blocks),known_weak_Schur_blocks_positive=all(a['corrected_weak_block_lower_positive_definite'] for a in blocks),actual_coupling_lower_certified=False,complete_1250_weak_mode_coverage_certified=False,strong_head_block_positivity_certified=False,weak_strong_cross_block_certified=False,matrix_Schur_positivity_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert result==saved
 return result
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 names=['rpb108_rc91_weak_mode_coupling_alignment.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc81_direct_enriched_riesz_residuals.json','rpb108_rc66_arch_multiplier_transport.json']
 defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: alternate column-first contractions, six signed source-cancellation bounds and weighted interval Loewner domination')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
