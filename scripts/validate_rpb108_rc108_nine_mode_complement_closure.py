"""RC108: nine native directions positive after the complete-head complement.
The remaining 1241 finite-head directions are not certified positive.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,hashlib,sys
from validate_rpb108_rc31_trial_riesz import mm,tr,psd,inverse
from validate_rpb108_rc47_correlated_native_transport import matrix,entries,root,serialize
from validate_rpb108_rc65_parity_projected_residual_refinement import cong,add,scale
from validate_rpb108_rc93_targeted_weak_source_capture import contract_interval,dot
from validate_rpb108_rc99_signed_source_projection_bounds import upper
from validate_rpb108_rc97_additional_low_mode_coverage import pd
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc107_original_compression_spectral_census import inertia
from validate_rpb108_rc90_continuous_source_balance_and_method_floor import relative40
from validate_rpb108_rc63_twenty_two_weak_floor_obstruction import down,up

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];c,even,odd,weak,en,na,sr,di,pa,tt,trf=map(json.loads,raw);h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert c['milestone']=='RC107' and c['entire_original_native_twenty_two_compression_positive_certified']
 assert c['input_sha256'][2:6]==h[4:8] and c['input_sha256'][8:10]==[h[9],h[8]]
 assert even['input_sha256'][4:7]==h[3:6] and even['input_sha256'][10:14]==[h[6],h[7],h[8],h[10]]
 assert odd['input_sha256'][0]==h[1] and odd['input_sha256'][5:8]==h[3:6] and odd['input_sha256'][11:15]==[h[6],h[7],h[8],h[10]]
 assert [trf['input_sha256'][i] for i in [2,4,5,7]]==[h[i] for i in [7,6,4,5]]
 assert odd['six_mode_corrected_positivity_certified'] and F(tt['inherited_1250_complement_floor'])==F(247,2500)
 V=matrix(en['enriched_native_trial_coefficients']);C=matrix(na['chebyshev_to_legendre']);mass=list(map(F,en['physical_mass']));T=cong(V,[[mass[i]*F(i==j) for j in range(64)] for i in range(64)]);U=entries(sr['nominal_complete_original_source_Gram_entries']);ER=entries(di['nominal_Legendre_residual_Gram_entry_enclosures']);H=[[tuple(map(F,x)) for x in r] for r in pa['nominal_physical_Legendre_source_pairing_enclosures']];rho=F(252,257);tau=F(tt['rank_1250_canonical_tail_certificate']['canonical_complement_embedding_norm_upper']);alpha=F(247,2500);nu=F(1,65536);delta=F(sr['actual_source_approximation_operator_error_upper']);deltaL=F(di['actual_operator_correction_norm_upper']);kbase=F(trf['projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho'])+F(trf['projected_prime_physical_to_canonical_norm_upper_divided_by_sqrt_rho']);oldtau=F(trf['canonical_complement_embedding_norm_upper'])
 rows=[]
 for p,b in enumerate(c['parity_spectral_compression_certificates']):
  name=b['parity'];assert name==['even','odd'][p]
  vs0=[list(map(F,r)) for r in b['fixed_rational_native_coordinates']];rawq=b['signed_original_Weil_entry_enclosures'];start=10 if p==0 else 9
  vs=vs0[start:];m=len(vs);zs=tr(mm(C,tr(vs)));tw=[[dot(v,T,w,replay) for w in vs] for v in vs];hc=[[sum((vs[j][i]*(H[n][i][0]+H[n][i][1])/2 for i in range(22)),F(0)) for j in range(m)] for n in range(64)];hr=[[sum((abs(vs[j][i])*(H[n][i][1]-H[n][i][0])/2 for i in range(22)),F(0)) for j in range(m)] for n in range(64)]
  wc=[[F(0)]*m for _ in range(m)];wr=[[F(0)]*m for _ in range(m)];ec=[[F(0)]*m for _ in range(m)];er=[[F(0)]*m for _ in range(m)];qc=[[F(0)]*m for _ in range(m)];qr=[[F(0)]*m for _ in range(m)]
  for i in range(m):
   for j in range(i,m):
    u,ur=contract_interval(vs[i],U,vs[j],replay);cap=sum((hc[n][i]*hc[n][j]/mass[n] for n in range(64)),F(0));cr=sum(((abs(hc[n][i])*hr[n][j]+abs(hc[n][j])*hr[n][i])/mass[n] for n in range(64)),F(0));wc[i][j]=wc[j][i]=u-cap;wr[i][j]=wr[j][i]=ur+cr
    ec[i][j],er[i][j]=contract_interval(zs[i],ER,zs[j],replay);ec[j][i]=ec[i][j];er[j][i]=er[i][j]
    row=next(x for x in rawq if x['i']==i+start and x['j']==j+start);a,z=map(F,row['actual_original_Weil_entry_enclosure']);qc[i][j]=qc[j][i]=(a+z)/2;qr[i][j]=qr[j][i]=(z-a)/2
  ds=[1/root(abs(qc[i][i]),10**40) for i in range(m)];qlo=[[qc[i][j]-F(i==j)*sum((qr[i][k]*ds[k]/ds[i] for k in range(m)),F(0)) for j in range(m)] for i in range(m)];qlo=rounded_bound(qlo,-1,10**50)[0]
  wu=upper(wc,wr,ds,replay);ep=scale(add(scale(upper(ec,er,ds,replay),1+nu),tw,(1+1/nu)*deltaL**2),rho**2);k=tau/oldtau*(kbase+F(trf['projected_pole_norm_uppers_divided_by_sqrt_rho'][p]));E=add(scale(ep,rho*(1+nu)*k*k),tw,(1+1/nu)*delta**2*tau*tau);E=rounded_bound(E,1,10**50)[0];N=scale(wu,tau*tau);N=rounded_bound(N,1,10**50)[0]

  base=[even,odd][p];wvs=[list(map(F,x['coefficients'])) for x in weak['fixed_rational_direction_certificates'] if x['parity']==name];assert len(wvs)==3
  ix=list(range(p,22,2));oldmat=[[vs0[j][i] for j in range(11)] for i in ix];newmat=[[wvs[j][i] for j in range(3)] for i in ix];A=mm(inverse(oldmat),newmat);assert mm(oldmat,A)==newmat
  # Signed original mixed entries, contracted in the complete old native basis.
  crossc=[[F(0)]*m for _ in range(3)];crossr=[[F(0)]*m for _ in range(3)]
  for i in range(3):
   for j in range(m):
    contracted=[]
    for z in rawq:
     a,z1=map(F,z['actual_original_Weil_entry_enclosure']);ii,jj=z['i'],z['j'];coef=(A[ii][i] if jj==j+start else F(0))+(A[jj][i] if ii==j+start and ii!=jj else F(0));contracted.append((coef*(a+z1)/2,abs(coef)*(z1-a)/2))
    if replay:contracted.reverse()
    crossc[i][j]=sum((x for x,y in contracted),F(0));crossr[i][j]=sum((y for x,y in contracted),F(0))
  qweak=rounded_bound(matrix(base['actual_original_'+name+'_three_mode_Weil_head_Loewner_lower']),-1,10**60)[0];gweak=rounded_bound(matrix(base['common_actual_rank_1250_source_coupling_Gram_upper']),1,10**60)[0]
  t=F(1,8);ss=F(1,8);gam=rounded_bound(add(scale(N,1+t),E,1+1/t),1,10**60)[0]
  lw=rounded_bound(add(qweak,scale(gweak,(1+ss)/alpha),-1),-1,10**60)[0];lh=rounded_bound(add(qlo,scale(gam,(1+1/ss)/alpha),-1),-1,10**60)[0];assert pd(lw) and pd(lh)
  intervals=[[down(crossc[i][j]-crossr[i][j],10**40),up(crossc[i][j]+crossr[i][j],10**40)] for i in range(3) for j in range(m)]
  allvs=wvs+vs;phys=cong(tr(allvs),matrix(na['physical_native_Gram']));Mhi=scale(phys,rho);assert pd(Mhi)
  change=[A[i]+[F(i==j+start) for j in range(m)] for i in range(11)];Mlo=rounded_bound(cong(change,matrix(b['actual_canonical_Gram_Loewner_lower'])),-1,10**60)[0];assert pd(Mlo)
  jointGamma=[[F(0)]*(3+m) for _ in range(3+m)]
  for i in range(3):
   for j in range(3):jointGamma[i][j]=(1+ss)*gweak[i][j]
  for i in range(m):
   for j in range(m):jointGamma[i+3][j+3]=(1+1/ss)*gam[i][j]
  g=relative40(jointGamma,Mlo);assert psd(add(scale(Mlo,g),jointGamma,-1))
  vertices=[]
  for cv in product(*intervals):
   cross=[list(cv[i*m:i*m+m]) for i in range(3)];full=[lw[i]+cross[i] for i in range(3)]+[tr(cross)[i]+lh[i] for i in range(m)]
   assert pd(full) and inertia(full,replay)['positive']==3+m
   vertices.append((cv,full))
  beta=None
  for power in range(10,41):
   target=F(1,10**power)
   if all(pd(add(full,Mhi,-target)) for cv,full in vertices):beta=target;break
  assert beta is not None
  proofs=[]
  for cv,full in vertices:
   assert inertia(add(full,Mhi,-beta),replay)['positive']==3+m
   # Independent Schur identity: eliminating the new strong block preserves positivity.
   cross=[list(cv[i*m:i*m+m]) for i in range(3)];hi=inverse(lh);assert mm(lh,hi)==[[F(i==j) for j in range(m)] for i in range(m)];schur=add(lw,mm(mm(cross,hi),tr(cross)),-1);assert pd(schur)
   proofs.append(dict(cross_vertex=list(map(str,cv)),positive_with_canonical_floor=True,positive_weak_Schur=True))
  whole_floor=min(beta,alpha)/max(F(2),1+2*g/alpha**2)
  rows.append(dict(parity=name,retained_weak_native_coordinates=list(map(lambda x:list(map(str,x)),wvs)),new_native_candidate_indices=list(range(start,11)),new_native_coordinates=list(map(lambda x:list(map(str,x)),vs)),corrected_parity_span_dimension=3+m,source_Young_parameter=str(t),weak_strong_covariance_Young_parameter=str(ss),nominal_fixed_polynomial_source_residual_Gram_upper=serialize(wu),actual_physical_Riesz_error_Gram_upper=serialize(ep),new_original_rank_1250_coupling_Gram_upper=serialize(gam),joint_original_rank_1250_coupling_Gram_upper=serialize(jointGamma),retained_weak_original_head_lower=serialize(qweak),new_original_head_lower=serialize(qlo),corrected_weak_diagonal_block_lower=serialize(lw),corrected_new_diagonal_block_lower=serialize(lh),original_weak_new_signed_cross_intervals=[[str(a),str(b)] for a,b in intervals],actual_canonical_metric_lower=serialize(Mlo),actual_canonical_metric_upper=serialize(Mhi),exact_vertex_certificates=proofs,corrected_selected_canonical_floor_lower=str(beta),joint_coupling_relative_actual_canonical_metric_upper=str(g),selected_plus_full_E_original_canonical_floor_lower=str(whole_floor),all_original_complement_and_finite_block_couplings_paid=True))
 dim=sum(r['corrected_parity_span_dimension'] for r in rows);assert dim==9
 out=dict(milestone='RC108',status='PASS',input_sha256=h,arithmetic='exact Fraction; no floating acceptance',aperture='11/10',parity_corrected_enlargement_certificates=rows,certified_corrected_span_dimension=dim,known_corrected_span_enlarged_from_six_to_nine=True,original_operator_nonpositive_spectral_dimension_upper=1250-dim,explicit_positive_subspace_codimension=1250-dim,explicit_positive_subspace='Retained weak six plus one new even and two new odd native directions, together with the complete original 1250-head canonical complement E.',explicit_positive_subspace_original_canonical_floor_lower=str(min(F(x['selected_plus_full_E_original_canonical_floor_lower']) for x in rows)),new_source_integrals_evaluated=0,common_complement_covariance_and_vertex_Schur_analytic_proofs_supplied=True,all_twenty_two_corrected_positive_certified=False,complete_nonpositive_mode_coverage_certified=False,strong_head_block_lower_certified=False,complete_1250_head_positive_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert out==saved
 return out

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates';names=['rpb108_rc107_original_compression_spectral_census.json','rpb108_rc100_even_three_mode_jump_tail.json','rpb108_rc101_odd_three_mode_jump_tail.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc81_direct_enriched_riesz_residuals.json','rpb108_rc83_nominal_source_canonical_response.json','rpb108_rc95_jump_aware_even_source_tail.json','rpb108_rc89_frequency_weighted_arch_transfer.json'];defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: reversed signed contractions, determinant-ratio inertia, all mixed-entry vertices and exact Schur identities')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
