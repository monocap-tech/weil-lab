"""RC99: four signed physical mixed entries and projected-covariance bounds.

Signed residual Gram entries are converted to Loewner uppers; their signs
are never copied into entries of the unknown projected covariance.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,psd,inverse
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,entries,root
from validate_rpb108_rc65_parity_projected_residual_refinement import cong,add,scale
from validate_rpb108_rc93_targeted_weak_source_capture import contract_interval,dot
from validate_rpb108_rc90_continuous_source_balance_and_method_floor import relative40
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
RHO=F(252,257)
def upper(c,r,ds,replay):
 n=len(c);rows=[sum((r[i][j]*ds[j]/ds[i] for j in range(n)),F(0)) for i in range(n)];A=[[c[i][j]+F(i==j)*rows[i] for j in range(n)] for i in range(n)]
 assert psd(A)
 if replay:
  assert all(ds[i]**2*rows[i]==sum((ds[i]*ds[j]*r[i][j] for j in range(n)),F(0)) for i in range(n))
 return A

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];prior,head,weak,enriched,native,source,direct,pairings,transport,even,odd,norm=map(json.loads,raw);h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['milestone']=='RC98' and prior['input_sha256']==h[1:]
 V=matrix(enriched['enriched_native_trial_coefficients']);C=matrix(native['chebyshev_to_legendre']);mass=list(map(F,enriched['physical_mass']));T=cong(V,[[mass[i]*F(i==j) for j in range(64)] for i in range(64)])
 U=entries(source['nominal_complete_original_source_Gram_entries']);ER=entries(direct['nominal_Legendre_residual_Gram_entry_enclosures']);H=[[tuple(map(F,x)) for x in r] for r in pairings['nominal_physical_Legendre_source_pairing_enclosures']]
 tau=F(prior['rank_1250_complement_embedding_norm_upper']);oldtau=F(transport['canonical_complement_embedding_norm_upper']);alpha=F(prior['inherited_complement_floor']);nu=F(1,65536)
 delta=F(source['actual_source_approximation_operator_error_upper']);deltaL=F(direct['actual_operator_correction_norm_upper']);effective=F(transport['projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho'])+F(transport['projected_prime_physical_to_canonical_norm_upper_divided_by_sqrt_rho']);poles=list(map(F,transport['projected_pole_norm_uppers_divided_by_sqrt_rho']));blocks=[]
 for p,name in enumerate(['even','odd']):
  vs=[list(map(F,a['coefficients'])) for a in weak['fixed_rational_direction_certificates'] if a['parity']==name];assert len(vs)==3
  zs=tr(mm(C,tr(vs)));tw=[[dot(v,T,w,replay) for w in vs] for v in vs]
  hc=[[sum((vs[j][i]*(H[n][i][0]+H[n][i][1])/2 for i in range(22)),F(0)) for j in range(3)] for n in range(64)];hr=[[sum((abs(vs[j][i])*(H[n][i][1]-H[n][i][0])/2 for i in range(22)),F(0)) for j in range(3)] for n in range(64)]
  wc=[[F(0)]*3 for _ in range(3)];wr=[[F(0)]*3 for _ in range(3)];ec=[[F(0)]*3 for _ in range(3)];er=[[F(0)]*3 for _ in range(3)];signed=[]
  for i in range(3):
   for j in range(i,3):
    u,ur=contract_interval(vs[i],U,vs[j],replay);cap=sum((hc[n][i]*hc[n][j]/mass[n] for n in range(64)),F(0));cr=sum(((abs(hc[n][i])*hr[n][j]+abs(hc[n][j])*hr[n][i])/mass[n] for n in range(64)),F(0))
    wc[i][j]=wc[j][i]=u-cap;wr[i][j]=wr[j][i]=ur+cr
    ec[i][j],er[i][j]=contract_interval(zs[i],ER,zs[j],replay);ec[j][i]=ec[i][j];er[j][i]=er[i][j]
    if j==2 and i<2:
     a,b=wc[i][j]-wr[i][j],wc[i][j]+wr[i][j]
     sign='negative' if b<0 else 'positive' if a>0 else 'unresolved'
     assert sign==(['negative','positive'] if p==0 else ['positive','negative'])[i]
     signed.append(dict(weak_index=i,nominal_physical_source_entry_enclosure=[str(u-ur),str(u+ur)],nominal_physical_residual_entry_enclosure=[str(a),str(b)],certified_nominal_physical_residual_sign=sign))
  ds=[F(100 if p==0 else 80),F(1),F(1)];WU=upper(wc,wr,ds,replay);EU=upper(ec,er,ds,replay);Ep=scale(add(scale(EU,1+nu),tw,(1+1/nu)*deltaL**2),RHO**2);k=tau/oldtau*(effective+poles[p]);E=add(scale(Ep,RHO*(1+nu)*k*k),tw,(1+1/nu)*delta**2*tau**2);N=scale(WU,tau*tau)
  N,_=rounded_bound(N,1,10**40);E,_=rounded_bound(E,1,10**40)
  old=prior['added_control_certificates'][p];g=F(old['actual_rank_1250_added_control_coupling_squared_upper']);L=matrix(old['retained_corrected_weak_Loewner_lower']);Gw=matrix(even['actual_rank_1250_even_weak_source_coupling_Gram_upper'] if p==0 else odd['weak_source_block_certificates'][p]['actual_rank_1250_weak_source_coupling_Gram_upper_via_nesting'])
  ranges=[[-root(Gw[i][i]*g,10**40),root(Gw[i][i]*g,10**40)] for i in range(2)];original=[r[:] for r in ranges];family=[]
  for t in [F(1,64),F(1,16),F(1,4),F(1,2),F(1),F(2),F(4),F(8),F(16),F(old['Young_parameter'])]:
   A=add(scale(N,1+t),E,1+1/t);A,_=rounded_bound(A,1,10**40);assert psd(A)
   bounds=[]
   for i in range(2):
    radius=root(A[i][i]*A[2][2],10**40)/2;lo=A[i][2]/2-radius;hi=A[i][2]/2+radius
    ranges[i][0]=max(ranges[i][0],lo);ranges[i][1]=min(ranges[i][1],hi);bounds.append([str(lo),str(hi)])
   family.append(dict(Young_parameter=str(t),actual_rank_1250_source_Gram_Loewner_upper=serialize(A),projected_mixed_entry_enclosures=bounds))
  assert all(a<=0<=b for a,b in ranges)
  corrected=[]
  for i in range(2):
   r=next(z for z in head['parity_low_subspace_certificates'][p]['signed_actual_Weil_entry_certificates'] if z['i']==i and z['j']==2);a,b=map(F,r['actual_Weil_entry_enclosure']);corrected.append([a-ranges[i][1]/alpha,b-ranges[i][0]/alpha])
  Li=inverse(L);d=F(old['added_control_corrected_diagonal_lower']);vertices=[]
  for c in product(*corrected):
   energy=dot(list(c),Li,list(c),replay);vertices.append(dict(cross=list(map(str,c)),inverse_penalty=str(energy),margin=str(d-energy)))
  worst=max(vertices,key=lambda r:F(r['inverse_penalty']));passed=all(F(r['margin'])>0 for r in vertices)
  # Full weak-block PSD correlation gives an ellipsoid, stronger than two
  # independent scalar Cauchy bounds, but still no signed entry enclosure.
  assert Gw[0][0]>0 and Gw[0][0]*Gw[1][1]-Gw[0][1]**2>0
  lam=relative40(Gw,L);gamma_energy=lam*g/alpha**2
  # Sharpness example for Loewner polarization, with signed rational PSD U.
  example=[[F(1),F(3,5)],[F(3,5),F(1)]];Pplus=[[F(4,5),F(4,5)],[F(4,5),F(4,5)]];Pminus=[[F(1,5),F(-1,5)],[F(-1,5),F(1,5)]]
  assert Pplus[0][1]==(example[0][1]+1)/2 and Pminus[0][1]==(example[0][1]-1)/2
  assert psd(Pplus) and psd(Pminus) and psd(add(example,Pplus,-1)) and psd(add(example,Pminus,-1))
  blocks.append(dict(parity=name,four_mixed_physical_entries=signed,nominal_physical_residual_center=serialize(wc),nominal_physical_residual_radius=serialize(wr),common_nominal_rank_1250_source_Gram_upper=serialize(N),common_actual_source_transfer_Gram_upper=serialize(E),projection_Young_family=family,prior_scalar_Cauchy_projected_mixed_enclosures=serialize(original),intersected_projected_mixed_enclosures=serialize(ranges),projected_entry_width_ratios=[str((b-a)/(y-x)) for (a,b),(x,y) in zip(ranges,original)],corrected_cross_enclosures=serialize(corrected),robust_completion_vertices=vertices,robust_three_mode_completion_passes=passed,worst_box_inverse_penalty_to_diagonal_ratio=str(F(worst['inverse_penalty'])/d),weak_coupling_relative_corrected_weak_lower_upper=str(lam),ellipsoid_source_inverse_penalty_upper=str(gamma_energy),ellipsoid_source_upper_to_added_diagonal_ratio=str(gamma_energy/d),signed_Gram_upper_does_not_force_projected_cross_sign=True,illustrative_Loewner_upper=serialize(example),illustrative_positive_projected_Gram=serialize(Pplus),illustrative_negative_projected_Gram=serialize(Pminus)))
 out=dict(milestone='RC99',status='PASS',input_sha256=h,signed_physical_mixed_entry_count=4,new_source_integrals_evaluated=0,canonical_projection_rank=1250,inherited_complement_floor=str(alpha),parity_signed_projection_certificates=blocks,Loewner_polarization_analytic_proof_supplied=True,weak_block_covariance_ellipsoid_analytic_proof_supplied=True,six_mode_corrected_positivity_certified=all(b['robust_three_mode_completion_passes'] for b in blocks),signed_physical_entries_identified_with_actual_canonical_entries=False,actual_negative_or_null_direction_certified=False,complete_weak_mode_coverage_certified=False,strong_head_block_certified=False,weak_strong_cross_block_certified=False,matrix_Schur_positivity_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert out==saved
 return out
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates';names=['rpb108_rc98_six_mode_schur_completion.json','rpb108_rc97_additional_low_mode_coverage.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc81_direct_enriched_riesz_residuals.json','rpb108_rc83_nominal_source_canonical_response.json','rpb108_rc89_frequency_weighted_arch_transfer.json','rpb108_rc95_jump_aware_even_source_tail.json','rpb108_rc94_weak_source_capture_128.json','rpb108_rc66_arch_multiplier_transport.json'];defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: symmetric mixed interval contractions, weighted Gram uppers, projected polarization intervals, ellipsoid bound and robust completion vertices')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
