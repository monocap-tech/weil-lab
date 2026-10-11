"""RC101: common three-input odd jump-aware weighted derivative tail."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
from concurrent.futures import ProcessPoolExecutor
import json,hashlib,sys
import validate_rpb108_rc30_interval_metric as iv
from validate_rpb108_rc30_interval_metric import I,PI
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc35_enriched_residuals import transformed,integrate,convolution,reflect,polyadd,scalar
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from validate_rpb108_rc42_native_signed_pole_head import outward
from validate_rpb108_rc43_native_prime_head import shift
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,root,entries
from validate_rpb108_rc48_prime_source_covariance import geometry
from validate_rpb108_rc52_complete_source_covariance import primitives
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,cong
from validate_rpb108_rc90_continuous_source_balance_and_method_floor import relative40
from validate_rpb108_rc94_weak_source_capture_128 import pole_test
from validate_rpb108_rc95_jump_aware_even_source_tail import deriv,weighted,primitive_alt,gram_worker,init
from validate_rpb108_rc93_targeted_weak_source_capture import contract_interval,dot
from validate_rpb108_rc63_twenty_two_weak_floor_obstruction import up,down
from validate_rpb108_rc99_signed_source_projection_bounds import upper
from validate_rpb108_rc97_additional_low_mode_coverage import pd
R=F(11,5);B=R/2;RHO=F(252,257);HEAD=1250
def three_odd_source_forms(enriched,native,arch,precision):
    V=matrix(enriched['enriched_native_trial_coefficients']);C=matrix(native['chebyshev_to_legendre']);ntrial=64;N=192
    H=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(2*(N+ntrial)+2)]
    H2=[sum((F(1,k*k) for k in range(1,n+1)),F(0)) for n in range(len(H))]
    cmid=F(precision['constant_midpoint']);Z=I(1).exp()*2*PI*I(R);assert Z.h<42
    q=[];l=[];power=I(1)
    for n in range(1,N+1):
        power=power*Z/n
        if n%2==0:q.append((-1)**(n//2+1)*power/2);l.append(I(0))
        else:
            sign=(-1)**((n-1)//2);q.append(sign*power*I(H[n]+cmid-1)/PI);l.append(-sign*power/PI)
    moments=[[],[],[],[],[],[]];zeta=PI*PI/6
    for k in range(2*(N+ntrial)+1):
        a=k+1;ha=H[a];hb=H2[a]
        for value,arr in zip([I(F(1,a)),I(-F(1,a*a)),I(-ha/a),I(F(2,a**3)),I((ha*ha+hb)/a),I(ha/F(a*a)+hb/a)-zeta/a],moments):arr.append(value)
    LP=[transformed(legendre(n)) for n in range(ntrial)]
    reg=list(map(F,arch['regular_kernel_coefficients']));forms=[];trials=[];targets=[]
    for j in range(3):
        v=[sum((V[n][j]*(LP[n][k] if k<=n else 0) for n in range(ntrial)),F(0)) for k in range(ntrial)]
        target=[sum((C[n][j]*(LP[n][k] if k<=n else 0) for n in range(22)),F(0)) for k in range(22)]
        al=[I(0)]*(N+ntrial);bl=[I(0)]*(N+ntrial);regular=[F(0)]*(N+ntrial+1)
        for p in range(N):
            for m,vm in enumerate(v):
                if vm==0:continue
                d=p+m+1;beta=F(factorial(p)*factorial(m),factorial(d))
                bl[d]+=l[p]*I(vm*beta)
                al[d]+=(q[p]+l[p]*I(H[p]-H[d]))*I(vm*beta)
                regular[d]+=R*reg[p]*R**p*vm*beta
        A=polyadd([I(x) for x in target],polyadd(al,reflect(al),-1),-1)
        A=polyadd(A,polyadd([I(x) for x in regular],reflect([I(x) for x in regular]),-1),-1)
        forms.append((A,scalar(bl,-1),scalar(reflect(bl),1)));trials.append(v);targets.append(target)
        print('enriched original source form',j,'built',file=sys.stderr,flush=True)
    return forms,moments,trials,targets

def jump_tail(prime,replay,saved=None):
 # J_o has +w at both knots. Actual odd sources have jumps -e_j*w,
 # so F_j=g_j-e_j*J_o; the common covariance is j_tail*e*e.T.
 terms,segs=geometry(prime);rows=prime['active_prime_powers'];cs=[1-I(r['n']).log()/B for r in rows];weights=[-I(r['base_prime']).log()/I(r['n']).sqrt() for r in rows]
 knots=[]
 for c,w in zip(cs,weights):knots.extend([(-c,w),(c,w)])
 knots.sort(key=lambda z:z[0].l)
 for (c,_),(d,_) in zip(knots,knots[1:]):assert c.h<d.l
 abs_cs=[c if c.l>0 else -c for c in cs];assert all(c.l>0 for c in abs_cs)
 if replay:
  norm=2*B*sum((a*b*(1-(c if c.l>d.h else d)) for c,a in zip(abs_cs,weights) for d,b in zip(abs_cs,weights)),I(0))
 else:
  norm=I(0);value=-sum(weights,I(0));left=I(-1)
  for c,w in knots:norm+=B*(c-left)*value*value;value+=w;left=c
  norm+=B*(1-left)*value*value
 P=[[I(1),c] for c in cs];DP=[[I(0),I(1)] for _ in cs]
 for k in range(1,HEAD):
  for a,c in enumerate(cs):
   P[a].append(((2*k+1)*c*P[a][k]-k*P[a][k-1])/(k+1))
   if replay:DP[a].append(((2*k+1)*(P[a][k]+c*DP[a][k])-k*DP[a][k-1])/(k+1))
 capture=I(0);coefs=[]
 for n in range(1,HEAD,2):
  if replay:h=2*B*sum((w*(1-c*c)*d[n]/F(n*(n+1)) for w,c,d in zip(weights,cs,DP)),I(0))
  else:h=2*B*sum((w*(p[n-1]-p[n+1])/F(2*n+1) for w,p in zip(weights,P)),I(0))
  capture+=h*h/(R/F(2*n+1));lo,hi=outward(h,10**40);coefs.append([str(lo),str(hi)])
 tl,tu=outward(norm-capture,10**(42 if replay else 40));assert 0<tl<tu
 if saved is not None:
  a,b=map(F,saved['physical_jump_profile_tail_norm_squared_enclosure']);assert a<=tl<=tu<=b;tl,tu=a,b
  old=saved['odd_jump_profile_Legendre_pairing_enclosures'];assert all(F(a)<=F(c)<=F(d)<=F(b) for (a,b),(c,d) in zip(old,coefs));coefs=old
 return tu,dict(head_degree_count=HEAD,physical_jump_profile_norm_squared_enclosure=list(map(str,outward(norm,10**40))),physical_jump_profile_capture_squared_enclosure=list(map(str,outward(capture,10**40))),physical_jump_profile_tail_norm_squared_enclosure=list(map(str,[tl,tu])),odd_jump_profile_Legendre_pairing_enclosures=coefs)

def run(paths,replay=False,saved=None,checkpoint=None):
 for ctx in [iv.loctx,iv.hictx,iv.near]:ctx.prec=800
 raw=[Path(p).read_bytes() for p in paths];even=json.loads(raw.pop(0));eh=hashlib.sha256(Path(paths[0]).read_bytes()).hexdigest();prior,old,head,control,weak,enriched,native,precision,prime,arch,source,direct,pairings,transport,norm=map(json.loads,raw);h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert even['milestone']=='RC100' and even['input_sha256']==h and even['corrected_even_three_mode_positive_certified']
 assert prior['milestone']=='RC99' and prior['input_sha256'][0]==h[3]
 assert prior['input_sha256'][1:]==[h[2],h[4],h[5],h[6],h[10],h[11],h[12],h[13],h[1],control['input_sha256'][9],h[14]]
 assert head['parity_low_subspace_certificates'][1]['fixed_native_coefficients']==[a['coefficients'] for a in weak['fixed_rational_direction_certificates'] if a['parity']=='odd']
 assert old['full_four_known_weak_span_corrected_positive_definite'] and old['parity_orthogonality_analytic_proof_supplied']
 assert old['input_sha256'][1:]==h[4:11] and old['input_sha256'][0]==control['input_sha256'][9]
 assert source['input_sha256'][:4]==[h[5],h[6],h[7],h[8]] and source['input_sha256'][5]==h[9]
 assert control['input_sha256'][1:6]==[h[4],h[5],h[6],h[10],h[11]]
 vs=[list(map(F,a['coefficients'])) for a in weak['fixed_rational_direction_certificates'] if a['parity']=='odd'];assert len(vs)==3;W=tr(vs);V=mm(matrix(enriched['enriched_native_trial_coefficients']),W);C=mm(matrix(native['chebyshev_to_legendre']),W)
 assert all(V[n][j]==0 for n in range(0,64,2) for j in range(3)) and all(C[n][j]==0 for n in range(0,22,2) for j in range(3))
 forms,mom,trial,target=three_odd_source_forms({'enriched_native_trial_coefficients':serialize(V)},{'chebyshev_to_legendre':serialize(C)},arch,precision)
 ds=[];eta=[]
 for j in range(3):
  A,L,M=forms[j];assert L[0].l==L[0].h==0
  ld=L[1:];a=polyadd(deriv(A),polyadd(ld,reflect(ld),1));l=deriv(L);m=deriv(M);tm=sum((I(V[n][j])*pole_test(n,replay) for n in range(64)),I(0));pt=[I(0)]*81
  for k in range(0,81,2):pt[k]=-R*tm*(B/2)**k/factorial(k)
  py=[sum((pt[n]*comb(n,k)*2**k*(-1)**(n-k) for n in range(k,len(pt))),I(0)) for k in range(len(pt))];a=polyadd(a,py);amp=max(abs(F(tm.l)),abs(F(tm.h)));eta.append(up(R*amp*2*(B/2)**81/factorial(81),10**120));ds.append((a,l,m))
 terms,segs0=geometry(prime);LP=[legendre(n) for n in range(64)];polys=[[sum((V[n][j]*(LP[n][k] if k<=n else 0) for n in range(64)),F(0)) for k in range(64)] for j in range(3)];edges=[sum((V[n][j] for n in range(64)),F(0)) for j in range(3)]
 assert all(sum(polys[i],F(0))==edges[i] and sum(((-1)**k*a for k,a in enumerate(polys[i])),F(0))==-edges[i] for i in range(3))
 translated=[[deriv([x*2**k for k,x in enumerate(shift([I(a) for a in p],term['offset']-1))]) for p in polys] for term in terms];segs=[];cache={}
 for ln,rn,left,right,active in segs0:
  left=(left+1)/2;right=(right+1)/2;src=[[sum((terms[k]['coefficient']*translated[k][j][l] for k in active),I(0)) for l in range(63)] for j in range(3)]
  if replay:pm=primitive_alt(left,right,320)
  else:
   for name,x in [(ln,left),(rn,right)]:
    if name not in cache:cache[name]=primitives(x,320,0 if name=='left' else 1 if name=='right' else None)
   pm=[[cache[rn][a][k]-cache[ln][a][k] for k in range(321)] for a in range(3)]
  segs.append((left,right,src,pm))
 dc=[[F(0)]*3 for _ in range(3)];dr=[[F(0)]*3 for _ in range(3)];intervals=[]
 with ProcessPoolExecutor(max_workers=3,initializer=init,initargs=((ds,mom,segs,replay),)) as pool:
  for i,j,(a,b) in pool.map(gram_worker,[(i,j) for i in range(3) for j in range(i,3)]):
   if saved is not None:
    row=next(z for z in saved['new_weighted_derivative_entries'] if z['i']==i and z['j']==j);x,y=map(F,row['interval']);assert x<=a<=b<=y;a,b=x,y
   dc[i][j]=dc[j][i]=(a+b)/2;dr[i][j]=dr[j][i]=(b-a)/2;intervals.append(dict(i=i,j=j,interval=[str(a),str(b)]))
 if checkpoint is not None:
  Path(checkpoint).write_text(json.dumps(dict(input_sha256=h,new_entries=intervals,eta=list(map(str,eta)),edges=list(map(str,edges))),indent=2))
 jt,jumpcert=jump_tail(prime,replay,None if saved is None else saved['jump_profile_certificate'])
 return finish([eh]+h,even,jt,jumpcert,old,head,control,weak,enriched,native,source,direct,transport,norm,dc,dr,eta,edges,intervals,replay,saved)

def finish(h,even,jt,jumpcert,old,head,control,weak,enriched,native,source,direct,transport,norm,dc,dr,eta,edges,intervals,replay,saved):
 ds=[F(8000),F(100),F(1)];nu=F(1,65536);D=add(scale(upper(dc,dr,ds,replay),1+nu),[[F(i==j)*eta[i]**2/2 for j in range(3)] for i in range(3)],1+1/nu)
 J=[[jt*edges[i]*edges[j] for j in range(3)] for i in range(3)];tau=F(old['rank_1250_canonical_tail_certificate']['canonical_complement_embedding_norm_upper']);alpha=F(old['inherited_1250_complement_floor'])
 vs=[list(map(F,a['coefficients'])) for a in weak['fixed_rational_direction_certificates'] if a['parity']=='odd'];VV=matrix(enriched['enriched_native_trial_coefficients']);mass=list(map(F,enriched['physical_mass']));T=cong(VV,[[mass[i]*F(i==j) for j in range(64)] for i in range(64)]);tw=[[dot(v,T,w,replay) for w in vs] for v in vs];zs=tr(mm(matrix(native['chebyshev_to_legendre']),tr(vs)));ER=entries(direct['nominal_Legendre_residual_Gram_entry_enclosures']);ec=[[F(0)]*3 for _ in range(3)];er=[[F(0)]*3 for _ in range(3)]
 for i in range(3):
  for j in range(i,3):ec[i][j],er[i][j]=contract_interval(zs[i],ER,zs[j],replay);ec[j][i]=ec[i][j];er[j][i]=er[i][j]
 deltaL=F(direct['actual_operator_correction_norm_upper']);delta=F(source['actual_source_approximation_operator_error_upper']);ep=scale(add(scale(upper(ec,er,ds,replay),1+nu),tw,(1+1/nu)*deltaL**2),RHO**2)
 oldtau=F(transport['canonical_complement_embedding_norm_upper']);eff=F(transport['projected_arch_physical_to_canonical_norm_upper_divided_by_sqrt_rho'])+F(transport['projected_prime_physical_to_canonical_norm_upper_divided_by_sqrt_rho'])+F(transport['projected_pole_norm_uppers_divided_by_sqrt_rho'][1]);k=tau/oldtau*eff;E=add(scale(ep,RHO*(1+nu)*k*k),tw,(1+1/nu)*delta**2*tau*tau)
 U=entries(source['nominal_complete_original_source_Gram_entries']);sn=[]
 for i in range(3):a,b=contract_interval(vs[i],U,vs[i],replay);sn.append(up(root(a+b,10**40)+delta*root(tw[i][i],10**40),10**40))
 rows=head['parity_low_subspace_certificates'][1]['signed_actual_Weil_entry_certificates'];qc=[[F(0)]*3 for _ in range(3)];qr=[[F(0)]*3 for _ in range(3)];ks=F(norm['complete_physical_operator_parity_norm_upper'][1])
 for z in rows:
  i,j=z['i'],z['j'];center=F(z['trial_Weil_center']);radius=F(z['trial_Weil_radius_upper'])+root(ep[i][i],10**40)*sn[j]+root(ep[j][j],10**40)*sn[i]+ks*root(ep[i][i]*ep[j][j],10**40);can=ep[i][i]/RHO if i==j else root(ep[i][i]*ep[j][j],10**40)/RHO
  lo=center-radius-can;hi=center+radius+(can if i!=j else 0);qc[i][j]=qc[j][i]=(lo+hi)/2;qr[i][j]=qr[j][i]=(hi-lo)/2
 qlo=[[qc[i][j]-F(i==j)*sum((qr[i][k]*ds[k]/ds[i] for k in range(3)),F(0)) for j in range(3)] for i in range(3)]
 positive_head=pd(qlo)
 tests=[];continuous=scale(D,R/F(HEAD*(HEAD+1)))
 for s in [F(1,4),F(1,2),F(1),F(2),F(4)]:
  N=scale(add(scale(continuous,1+s),J,1+1/s),tau*tau)
  for t in [F(1,4),F(1,2),F(1),F(2),F(4)]:
   G=add(scale(N,1+t),E,1+1/t)
   if positive_head:tests.append((relative40(G,qlo),s,t))
 if tests:lam,s,t=min(tests)
 else:lam,s,t=None,F(1),F(2)
 N=scale(add(scale(continuous,1+s),J,1+1/s),tau*tau);G=add(scale(N,1+t),E,1+1/t);corrected=add(qlo,G,-1/alpha);passes=lam is not None and lam<alpha
 floor=F(0)
 if lam is not None:assert psd(add(scale(qlo,lam),G,-1))
 if passes:
  assert pd(corrected)
  Mhi=scale(cong(tr(vs),matrix(native['physical_native_Gram'])),RHO)
  scaled=scale(corrected,F(10**18));left,right=F(0),F(1)
  while psd(add(scaled,scale(Mhi,right),-1)):right*=2
  for _ in range(40):
   mid=(left+right)/2
   if psd(add(scaled,scale(Mhi,mid),-1)):left=mid
   else:right=mid
  floor=left/10**18;assert floor>0 and psd(add(corrected,scale(Mhi,floor),-1))
 out=dict(milestone='RC101',status='PASS',input_sha256=h,precision=800,new_weighted_derivative_entries=intervals,all_six_odd_derivative_entries_newly_certified=True,jump_profile_certificate=jumpcert,weighted_derivative_Gram_upper=serialize(D),pole_derivative_uniform_error_uppers=list(map(str,eta)),trial_odd_endpoint_values=list(map(str,edges)),rank_one_jump_tail_Gram_upper=serialize(J),common_actual_physical_Riesz_error_Gram_upper=serialize(ep),common_actual_source_transfer_Gram_upper=serialize(E),actual_original_odd_three_mode_Weil_head_Loewner_lower=serialize(qlo),head_lower_PSD=positive_head,inner_Young_parameter=str(s),outer_Young_parameter=str(t),common_actual_rank_1250_source_coupling_Gram_upper=serialize(G),coupling_relative_head_lower_upper=str(lam) if lam is not None else None,corrected_odd_three_mode_Loewner_lower=serialize(corrected),corrected_odd_three_mode_positive_certified=passes,corrected_odd_three_mode_canonical_floor_lower=str(floor),certified_corrected_span_dimension=6 if passes else 5,original_operator_nonpositive_spectral_dimension_upper=1244 if passes else 1245,even_three_mode_positive_certificate_retained=True,six_mode_corrected_positivity_certified=passes,six_mode_canonical_floor_lower=str(min(floor,F(even['corrected_even_three_mode_canonical_floor_lower']))) if passes else '0',complete_weak_mode_coverage_certified=False,strong_head_block_certified=False,weak_strong_cross_block_certified=False,matrix_Schur_positivity_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert out==saved
 return out
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates';names=['rpb108_rc100_even_three_mode_jump_tail.json','rpb108_rc99_signed_source_projection_bounds.json','rpb108_rc95_jump_aware_even_source_tail.json','rpb108_rc97_additional_low_mode_coverage.json','rpb108_rc98_six_mode_schur_completion.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc56_precision_attached_head.json','rpb108_rc43_native_prime_head.json','rpb108_rc46_native_archimedean_head.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc81_direct_enriched_riesz_residuals.json','rpb108_rc83_nominal_source_canonical_response.json','rpb108_rc89_frequency_weighted_arch_transfer.json','rpb108_rc66_arch_multiplier_transport.json'];defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--checkpoint':
  print(json.dumps(run(sys.argv[3:] or defaults,checkpoint=sys.argv[2]),indent=2))
 elif len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: six new signed derivative entries and common odd three-mode jump-aware source and head tests')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
