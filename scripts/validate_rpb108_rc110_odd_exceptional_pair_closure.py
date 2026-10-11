from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
from concurrent.futures import ProcessPoolExecutor
import json,sys
import validate_rpb108_rc30_interval_metric as iv
from validate_rpb108_rc30_interval_metric import I
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc35_enriched_residuals import polyadd,reflect
from validate_rpb108_rc31_trial_riesz import mm,tr
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize
from validate_rpb108_rc43_native_prime_head import shift
from validate_rpb108_rc48_prime_source_covariance import geometry
from validate_rpb108_rc52_complete_source_covariance import primitives
from validate_rpb108_rc101_odd_three_mode_jump_tail import three_odd_source_forms
from validate_rpb108_rc94_weak_source_capture_128 import pole_test
from validate_rpb108_rc95_jump_aware_even_source_tail import deriv,primitive_alt,init,gram_worker
from validate_rpb108_rc63_twenty_two_weak_floor_obstruction import up
R=F(11,5);B=R/2
def new_odd_derivatives(en,na,arch,precision,prime,previous,replay=False,saved=None):
 for ctx in [iv.loctx,iv.hictx,iv.near]:ctx.prec=600 if replay else 800
 vs=[list(map(F,r)) for r in previous['parity_spectral_compression_certificates'][1]['fixed_rational_native_coordinates'][3:5]]+[[F(0)]*22];W=tr(vs);V=mm(matrix(en['enriched_native_trial_coefficients']),W);C=mm(matrix(na['chebyshev_to_legendre']),W)
 forms,mom,trial,target=three_odd_source_forms({'enriched_native_trial_coefficients':serialize(V)},{'chebyshev_to_legendre':serialize(C)},arch,precision)
 ds=[];eta=[]
 for j in range(3):
  A,L,M=forms[j];assert L[0].l==L[0].h==0
  ld=L[1:];a=polyadd(deriv(A),polyadd(ld,reflect(ld),1));l=deriv(L);m=deriv(M);tm=sum((I(V[n][j])*pole_test(n,replay) for n in range(64)),I(0));pt=[I(0)]*81
  for k in range(0,81,2):pt[k]=-R*tm*(B/2)**k/factorial(k)
  py=[sum((pt[n]*comb(n,k)*2**k*(-1)**(n-k) for n in range(k,len(pt))),I(0)) for k in range(len(pt))];a=polyadd(a,py);amp=max(abs(F(tm.l)),abs(F(tm.h)));eta.append(up(R*amp*2*(B/2)**81/factorial(81),10**120));ds.append((a,l,m))
 terms,segs0=geometry(prime);LP=[legendre(n) for n in range(64)];polys=[[sum((V[n][j]*(LP[n][k] if k<=n else 0) for n in range(64)),F(0)) for k in range(64)] for j in range(3)];edges=[sum((V[n][j] for n in range(64)),F(0)) for j in range(3)]
 translated=[[deriv([x*2**k for k,x in enumerate(shift([I(a) for a in p],term['offset']-1))]) for p in polys] for term in terms];segs=[];cache={}
 for ln,rn,left,right,active in segs0:
  left=(left+1)/2;right=(right+1)/2;src=[[sum((terms[k]['coefficient']*translated[k][j][l] for k in active),I(0)) for l in range(63)] for j in range(3)]
  for name,x in [(ln,left),(rn,right)]:
   if name not in cache:cache[name]=primitives(x,320,0 if name=='left' else 1 if name=='right' else None)
  pm=primitive_alt(left,right,320) if replay else [[cache[rn][a][k]-cache[ln][a][k] for k in range(321)] for a in range(3)];segs.append((left,right,src,pm))
 rows=[]
 with ProcessPoolExecutor(max_workers=3,initializer=init,initargs=((ds,mom,segs,replay),)) as pool:
  for i,j,ab in pool.map(gram_worker,[(0,0),(0,1),(1,1)]):
   if saved is not None:
    old=next(x for x in saved['rows'] if x['i']==i and x['j']==j);lo,hi=map(F,old['interval']);assert lo<=ab[0]<=ab[1]<=hi;ab=(lo,hi)
   rows.append(dict(i=i,j=j,interval=list(map(str,ab))))
 return dict(rows=rows,eta=list(map(str,eta[:2])),edges=list(map(str,edges[:2])))

from validate_rpb108_rc31_trial_riesz import psd,inverse
from validate_rpb108_rc47_correlated_native_transport import entries,root
from validate_rpb108_rc65_parity_projected_residual_refinement import cong,add,scale
from validate_rpb108_rc93_targeted_weak_source_capture import contract_interval,dot
from validate_rpb108_rc99_signed_source_projection_bounds import upper
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc97_additional_low_mode_coverage import pd
from validate_rpb108_rc107_original_compression_spectral_census import inertia
from validate_rpb108_rc109_direct_mixed_ten_mode_closure import direct_entries
from validate_rpb108_rc90_continuous_source_balance_and_method_floor import relative40
import hashlib
from itertools import product
RHO=F(252,257)

def sub(A,ix):return [[A[i][j] for j in ix] for i in ix]

def robust_schur(W,H,C,radii,M,beta,t,replay):
 nw=len(W);nh=len(H);w=add(W,sub(M,list(range(nw))),-beta);h=add(H,sub(M,list(range(nw,nw+nh))),-beta)
 if not pd(w) or not pd(h):return None
 cc=[[C[i][j]-beta*M[i][j+nw] for j in range(nh)] for i in range(nw)];hi=inverse(h)
 assert mm(h,hi)==[[F(i==j) for j in range(nh)] for i in range(nh)]
 abs_hi=[[abs(x) for x in row] for row in hi];Berr=mm(mm(radii,abs_hi),tr(radii));ds=[1/root(w[i][i],10**40) for i in range(nw)]
 error_diag=[sum((Berr[i][j]*ds[j]/ds[i] for j in range(nw)),F(0)) for i in range(nw)]
 if replay:assert all(ds[i]**2*error_diag[i]==sum((Berr[i][j]*ds[i]*ds[j] for j in range(nw)),F(0)) for i in range(nw))
 error=[[F(i==j)*error_diag[i] for j in range(nw)] for i in range(nw)]
 nominal=mm(mm(cc,hi),tr(cc));margin=add(add(w,scale(nominal,1+t),-1),error,-(1+1/t));margin=rounded_bound(margin,-1,10**60)[0]
 if not pd(margin):return None
 assert inertia(margin,replay)['positive']==nw and inertia(h,replay)['positive']==nh
 return dict(beta=str(beta),mixed_error_Young_parameter=str(t),new_block_inverse=serialize(hi),nominal_inverse_penalty=serialize(nominal),mixed_error_inverse_Gram_upper=serialize(error),robust_weak_Schur_Loewner_lower=serialize(margin),all_mixed_entry_intervals_paid=True)

def abstract_controls(replay):
 W=[[F(4),F(0)],[F(0),F(3)]];H=[[F(2),F(1,4)],[F(1,4),F(1)]];C=[[F(1,5),F(1,4)],[F(1,3),F(1,6)]];rad=[[F(1,100),F(1,200)],[F(1,150),F(1,120)]];M=[[F(i==j) for j in range(4)] for i in range(4)]
 assert robust_schur(W,H,C,rad,M,F(1,10),F(1),replay) is not None
 for signs in product([-1,1],repeat=4):
  cc=[[C[i][j]+signs[2*i+j]*rad[i][j] for j in range(2)] for i in range(2)];full=[W[i]+cc[i] for i in range(2)]+[tr(cc)[i]+H[i] for i in range(2)];assert pd(add(full,M,-F(1,10)))
 I2=[[F(1),F(0)],[F(0),F(1)]]
 assert robust_schur([[F(1)]],[[F(1)]],[[F(2)]],[[F(0)]],I2,F(0),F(1),replay) is None
 assert not psd([[F(1),F(2)],[F(2),F(1)]])
 assert robust_schur([[F(1)]],[[F(1)]],[[F(9,10)]],[[F(0)]],I2,F(0),F(1),replay) is None and pd([[F(1),F(9,10)],[F(9,10),F(1)]])
 return dict(positive_interval_control_all_sixteen_vertices_verified=True,genuine_negative_control_rejected=True,positive_control_rejected_at_fixed_Young_one=True,scope='Illustrative rational matrices only; fixed-parameter sufficient-bound failure is not original negativity.')

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths];c,even,odd,weak,en,na,sr,di,pa,tt,trf,response_residual,norm,old108,arch,precision,prime,previous=map(json.loads,raw);h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert previous['milestone']=='RC109' and previous['certified_corrected_span_dimension']==10 and previous['input_sha256']==h[:17]
 assert c['milestone']=='RC107' and c['input_sha256'][2:6]==h[4:8] and c['input_sha256'][6]==h[12] and c['input_sha256'][10]==h[11]
 assert odd['input_sha256'][0]==h[1] and odd['input_sha256'][5:8]==h[3:6] and odd['input_sha256'][11:15]==[h[i] for i in [6,7,8,10]]
 assert sr['input_sha256'][2:4]==[h[15],h[16]] and sr['input_sha256'][5]==h[14]
 proof=new_odd_derivatives(en,na,arch,precision,prime,c,replay,None if saved is None else saved['new_odd_weighted_derivative_proof'])
 b=c['parity_spectral_compression_certificates'][1];vs0=[list(map(F,r)) for r in b['fixed_rational_native_coordinates']];lowvs=vs0[3:5];highvs=vs0[9:11];newvs=lowvs+highvs
 wvs=[list(map(F,x['coefficients'])) for x in weak['fixed_rational_direction_certificates'] if x['parity']=='odd'];allvs=wvs+newvs
 assert previous['parity_corrected_enlargement_certificates'][1]['retained_weak_native_coordinates']==[list(map(str,x)) for x in wvs]
 assert previous['parity_corrected_enlargement_certificates'][1]['new_native_coordinates']==[list(map(str,x)) for x in highvs]
 a=F(tt['inherited_1250_complement_floor']);assert a==F(247,2500)
 tau=F(tt['rank_1250_canonical_tail_certificate']['canonical_complement_embedding_norm_upper']);nu=F(1,65536)
 V=matrix(en['enriched_native_trial_coefficients']);Cnative=matrix(na['chebyshev_to_legendre']);mass=list(map(F,en['physical_mass']));T=cong(V,[[mass[i]*F(i==j) for j in range(64)] for i in range(64)]);tw=[[dot(v,T,w,replay) for w in lowvs] for v in lowvs];zs=tr(mm(Cnative,tr(lowvs)));ER=entries(di['nominal_Legendre_residual_Gram_entry_enclosures'])
 qc,qr,head_entries=direct_entries(allvs,1,en,na,sr,di,pa,response_residual,norm,replay)
 ds=[1/root(abs(qc[i+3][i+3]),10**40) for i in range(2)];dc=[[F(0)]*2 for _ in range(2)];dr=[[F(0)]*2 for _ in range(2)]
 for row in proof['rows']:
  i,j=row['i'],row['j'];lo,hi=map(F,row['interval']);dc[i][j]=dc[j][i]=(lo+hi)/2;dr[i][j]=dr[j][i]=(hi-lo)/2
 eta=list(map(F,proof['eta']));D=add(scale(upper(dc,dr,ds,replay),1+nu),[[F(i==j)*eta[i]**2/2 for j in range(2)] for i in range(2)],1+1/nu)
 edges=list(map(F,proof['edges']));jt=F(odd['jump_profile_certificate']['physical_jump_profile_tail_norm_squared_enclosure'][1]);jump=[[jt*edges[i]*edges[j] for j in range(2)] for i in range(2)]
 N=rounded_bound(scale(add(scale(D,2*R/F(1250*1251)),jump,2),tau*tau),1,10**50)[0]
 ec=[[F(0)]*2 for _ in range(2)];er=[[F(0)]*2 for _ in range(2)]
 for i in range(2):
  for j in range(i,2):ec[i][j],er[i][j]=contract_interval(zs[i],ER,zs[j],replay);ec[j][i]=ec[i][j];er[j][i]=er[i][j]
 deltaL=F(di['actual_operator_correction_norm_upper']);delta=F(sr['actual_source_approximation_operator_error_upper']);ep=scale(add(scale(upper(ec,er,ds,replay),1+nu),tw,(1+1/nu)*deltaL**2),RHO**2)
 oldtau=F(trf['canonical_complement_embedding_norm_upper']);eff=sum((F(trf[k]) for k in ['projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho','projected_prime_physical_to_canonical_norm_upper_divided_by_sqrt_rho']),F(0))+F(trf['projected_pole_norm_uppers_divided_by_sqrt_rho'][1]);k=tau/oldtau*eff
 E=rounded_bound(add(scale(ep,RHO*(1+nu)*k*k),tw,(1+1/nu)*delta**2*tau*tau),1,10**50)[0]
 Ghigh=matrix(previous['parity_corrected_enlargement_certificates'][1]['new_original_rank_1250_coupling_Gram_upper']);Gw=rounded_bound(matrix(odd['common_actual_rank_1250_source_coupling_Gram_upper']),1,10**60)[0];Qw=rounded_bound(matrix(odd['actual_original_odd_three_mode_Weil_head_Loewner_lower']),-1,10**60)[0]
 qn=sub(qc,list(range(3,7)));rn=sub(qr,list(range(3,7)));dn=[1/root(abs(qn[i][i]),10**40) for i in range(4)];Qn=rounded_bound([[qn[i][j]-F(i==j)*sum((rn[i][k]*dn[k]/dn[i] for k in range(4)),F(0)) for j in range(4)] for i in range(4)],-1,10**60)[0]
 cross=[r[3:] for r in qc[:3]];radii=[r[3:] for r in qr[:3]]
 Mhi=scale(cong(tr(allvs),matrix(na['physical_native_Gram'])),RHO);assert pd(Mhi)
 ix=list(range(1,22,2));oldmat=[[vs0[j][i] for j in range(11)] for i in ix];newmat=[[allvs[j][i] for j in range(7)] for i in ix];change=mm(inverse(oldmat),newmat);assert mm(oldmat,change)==newmat
 Mlo=rounded_bound(cong(change,matrix(b['actual_canonical_Gram_Loewner_lower'])),-1,10**60)[0];assert pd(Mlo)
 selected=None
 for t in [F(1),F(1,2),F(2),F(1,4),F(4)]:
  Glow=rounded_bound(add(scale(N,1+t),E,1+1/t),1,10**60)[0]
  for u in [F(1),F(1,2),F(2)]:
   Gn=[[F(0)]*4 for _ in range(4)]
   for i in range(2):
    for j in range(2):Gn[i][j]=(1+u)*Glow[i][j];Gn[i+2][j+2]=(1+1/u)*Ghigh[i][j]
   for s in [F(1,4),F(1,2),F(1,8)]:
    W=rounded_bound(add(Qw,scale(Gw,(1+s)/a),-1),-1,10**60)[0];H=rounded_bound(add(Qn,scale(Gn,(1+1/s)/a),-1),-1,10**60)[0]
    if not pd(W) or not pd(H):continue
    for v in [F(1,4),F(1,2),F(1),F(2),F(4)]:
     test=robust_schur(W,H,cross,radii,Mhi,F(0),v,replay)
     if test is not None:selected=(t,u,s,v,Glow,Gn,W,H);break
    if selected is not None:break
   if selected is not None:break
  if selected is not None:break
 assert selected is not None,'no robust odd seven-mode certificate'
 t,u,s,v,Glow,Gn,W,H=selected;accepted=None
 for power in range(10,41):
  beta=F(1,10**power);accepted=robust_schur(W,H,cross,radii,Mhi,beta,v,replay)
  if accepted is not None:break
 assert accepted is not None
 joint=[[F(0)]*7 for _ in range(7)]
 for i in range(3):
  for j in range(3):joint[i][j]=(1+s)*Gw[i][j]
 for i in range(4):
  for j in range(4):joint[i+3][j+3]=(1+1/s)*Gn[i][j]
 g=relative40(joint,Mlo);assert psd(add(scale(Mlo,g),joint,-1));mu=min(beta,a)/max(F(2),1+2*g/a**2)
 oddcert=dict(parity='odd',corrected_parity_span_dimension=7,retained_weak_native_coordinates=[list(map(str,x)) for x in wvs],new_native_candidate_indices=[3,4,9,10],new_native_coordinates=[list(map(str,x)) for x in newvs],direct_original_head_entry_certificates=head_entries,actual_canonical_metric_lower=serialize(Mlo),actual_canonical_metric_upper=serialize(Mhi),accepted_low_nominal_tail_Gram_upper=serialize(N),actual_low_source_transfer_Gram_upper=serialize(E),new_low_original_rank_1250_coupling_Gram_upper=serialize(Glow),retained_high_original_rank_1250_coupling_Gram_upper=serialize(Ghigh),joint_original_rank_1250_coupling_Gram_upper=serialize(joint),source_Young_parameter=str(t),low_high_covariance_Young_parameter=str(u),weak_new_covariance_Young_parameter=str(s),corrected_weak_block_lower=serialize(W),corrected_new_block_lower=serialize(H),original_mixed_entry_centers=serialize(cross),original_mixed_entry_halfwidths=serialize(radii),robust_Schur_certificate=accepted,corrected_selected_canonical_floor_lower=str(beta),joint_coupling_relative_actual_canonical_metric_upper=str(g),selected_plus_full_E_original_canonical_floor_lower=str(mu),all_mixed_interval_vertices_controlled_analytically_without_enumeration=True)
 even_cert=previous['parity_corrected_enlargement_certificates'][0];assert even_cert['corrected_parity_span_dimension']==5
 out=dict(abstract_robust_Schur_controls=abstract_controls(replay),milestone='RC110',status='PASS',input_sha256=h,arithmetic='exact Fraction; directed source integration; no floating acceptance',aperture='11/10',new_odd_weighted_derivative_proof=proof,parity_corrected_enlargement_certificates=[even_cert,oddcert],certified_corrected_span_dimension=12,known_corrected_span_enlarged_from_ten_to_twelve=True,original_operator_nonpositive_spectral_dimension_upper=1238,explicit_positive_subspace_codimension=1238,explicit_positive_subspace_original_canonical_floor_lower=str(min(F(even_cert['selected_plus_full_E_original_canonical_floor_lower']),mu)),new_weighted_derivative_Gram_entries_evaluated=3,robust_mixed_Schur_analytic_proof_supplied=True,original_odd_low_candidate_indices_three_and_four_admitted=True,all_twenty_two_corrected_positive_certified=False,complete_nonpositive_mode_coverage_certified=False,strong_head_block_lower_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert out==saved
 return out

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates';names=['rpb108_rc107_original_compression_spectral_census.json','rpb108_rc100_even_three_mode_jump_tail.json','rpb108_rc101_odd_three_mode_jump_tail.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc81_direct_enriched_riesz_residuals.json','rpb108_rc83_nominal_source_canonical_response.json','rpb108_rc95_jump_aware_even_source_tail.json','rpb108_rc89_frequency_weighted_arch_transfer.json','rpb108_rc84_direct_nominal_response_residual.json','rpb108_rc66_arch_multiplier_transport.json','rpb108_rc108_nine_mode_complement_closure.json','rpb108_rc46_native_archimedean_head.json','rpb108_rc56_precision_attached_head.json','rpb108_rc43_native_prime_head.json','rpb108_rc109_direct_mixed_ten_mode_closure.json'];defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: odd derivative integration replay, signed mixed entries, inverse checks and robust interval Schur floor')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
