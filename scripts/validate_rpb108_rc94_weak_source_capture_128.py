"""RC94: four-input original-source capture through degree below 128.

Only the missing 128 same-parity physical source pairings are integrated.
Actual projection nesting replaces a dense enlarged Weil-head evaluation.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb,prod
from concurrent.futures import ProcessPoolExecutor
import json,hashlib,sys
from validate_rpb108_rc30_interval_metric import I,PI
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc35_enriched_residuals import transformed,integrate
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from validate_rpb108_rc43_native_prime_head import shift
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,root
from validate_rpb108_rc48_prime_source_covariance import geometry
from validate_rpb108_rc68_enriched_original_source_covariance import polyadd,reflect,scalar
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,cong
from validate_rpb108_rc88_multiband_canonical_tail_transport import ceilgrid,logbounds
from validate_rpb108_rc90_continuous_source_balance_and_method_floor import relative40
from validate_rpb108_rc93_targeted_weak_source_capture import upper,dot
from validate_rpb108_rc63_twenty_two_weak_floor_obstruction import up,down
R=F(11,5);B=R/2;RHO=F(252,257);HEAD=128

def weak_source_forms(enriched,native,arch,precision):
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
    for j in range(4):
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
        A=polyadd([I(x) for x in target],polyadd(al,reflect(al),(-1)**j),-1)
        A=polyadd(A,polyadd([I(x) for x in regular],reflect([I(x) for x in regular]),(-1)**j),-1)
        forms.append((A,scalar(bl,-1),scalar(reflect(bl),-(-1)**j)));trials.append(v);targets.append(target)
        print('enriched original source form',j,'built',file=sys.stderr,flush=True)
    return forms,moments,trials,targets

def init(config):
 global WORK
 WORK=config

def pole_test(n,replay):
 if replay:
  value=F(2**(n+1)*factorial(n),factorial(2*n+1))*(B/2)**n;total=F(0)
  for l in range(41):
   total+=value;value*= (B/2)**2/F(2*(l+1)*(2*l+2*n+3))
  return rational_interval(B*total,B*(total+2*value))
 def term(l):return F(2**(n+1)*factorial(l+n),factorial(l)*factorial(2*l+2*n+1))*(B/2)**(n+2*l)
 assert (B/2)**2/F(2*42*(2*41+2*n+3))<F(1,2)
 return rational_interval(B*sum((term(l) for l in range(41)),F(0)),B*(sum((term(l) for l in range(41)),F(0))+2*term(41)))

def worker(j):
 forms,mom,segs,trialmom,replay=WORK
 pm=[I(0) for _ in range(HEAD)]
 for left,right,src,affine,powers in segs:
  if replay:
   length=right-left;am=[B*length*sum((x/F(l+k+1) for l,x in enumerate(affine[j])),I(0)) for k in range(HEAD)]
   lp=[I(1)];dp=[I(1)]
   for _ in range(HEAD):lp.append(lp[-1]*left);dp.append(dp[-1]*length)
   for k in range(HEAD):pm[k]+=sum((I(comb(k,m))*lp[k-m]*dp[m]*am[m] for m in range(k+1)),I(0))
  else:
   for k in range(HEAD):pm[k]+=B*sum((x*powers[k+l] for l,x in enumerate(src[j])),I(0))
 A,L,M=forms[j];out=[]
 for n in range(64+j%2,HEAD,2):
  z=legendre(n);zy=[I(x) for x in transformed(z)]
  arch=R*(integrate(zy,A,mom[0])+2*integrate(zy,L,mom[1])) if replay else R*(integrate(zy,A,mom[0])+integrate(zy,L,mom[1])+integrate(zy,M,mom[2]))
  prime=sum((I(x)*pm[k] for k,x in enumerate(z)),I(0));pole=2*(-1)**j*pole_test(n,replay)*trialmom[j]
  out.append((n,outward(arch+prime+pole,10**(36 if replay else 34))))
  print('weak source',j,'Legendre',n,'enclosed',file=sys.stderr,flush=True)
 return j,out

def tail128(replay):
 elo,ehi=outward(I(1).exp(),10**30);pilo,pihi=outward(PI,10**30);df=prod(range(1,2*HEAD+2,2));energy=F(1);prev=F(0);rows=[]
 if replay:assert df==F(factorial(2*HEAD+1),2**HEAD*factorial(HEAD))
 for k in range(1,1001):
  cut=F(k,50);z=2*pihi*B*cut;r=z*z/F(2*HEAD+3)**2;assert r<1
  theta=4*B*cut*z**(2*HEAD)/(F(df)**2*(1-r));th=min(F(1),ceilgrid(theta,10**50));q=(ehi+cut)/(ehi+prev);lo,hi=outward(I(q).log(),10**40)
  if replay:
   a,b=logbounds(q);assert lo<=a<=b<=hi
  term=lo*(1-th);energy+=term;rows.append(dict(cut=str(cut),low_frequency_energy_fraction_upper=str(th),weight_increment_lower=str(lo),energy_contribution=str(term)));prev=cut
  if th==1:break
 assert th==1
 if replay:assert energy==1+sum((F(x['weight_increment_lower'])*(1-F(x['low_frequency_energy_fraction_upper'])) for x in rows),F(0))
 tau=root(1/energy,10**30);assert tau*tau*energy>=1
 return tau,dict(head_degree_count=HEAD,frequency_step='1/50',odd_double_factorial=str(df),e_enclosure=list(map(str,[elo,ehi])),pi_enclosure=list(map(str,[pilo,pihi])),layers=rows,canonical_energy_relative_physical_lower=str(energy),canonical_complement_embedding_norm_upper=str(tau))

def run(paths,replay=False,saved=None,pairing_cache=None):
 raw=[Path(p).read_bytes() for p in paths];prior,head,weak,enriched,native,precision,prime,arch,source,transport=map(json.loads,raw);h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['input_sha256'][0]==h[1] and prior['input_sha256'][2:6]==[h[i] for i in [2,4,3,8]]
 assert source['input_sha256'][:4]==[h[i] for i in [3,4,5,6]] and source['input_sha256'][5:]==[h[7],h[9]]
 assert head['input_sha256'][1:5]==[h[i] for i in [2,3,4,8]]
 assert precision['input_sha256'][4]==h[6] and precision['input_sha256'][5]==h[7]
 directions=[next(x for x in weak['fixed_rational_direction_certificates'] if x['parity']==parity and x['role']==role) for role in ['weak_0','weak_1'] for parity in ['even','odd']];vs=[list(map(F,x['coefficients'])) for x in directions];W=tr(vs)
 if pairing_cache is None:
  Vsmall=mm(matrix(enriched['enriched_native_trial_coefficients']),W);Csmall=mm(matrix(native['chebyshev_to_legendre']),W)
  forms,mom,trials,targets=weak_source_forms({'enriched_native_trial_coefficients':serialize(Vsmall)},{'chebyshev_to_legendre':serialize(Csmall)},arch,precision)
  LP=[legendre(n) for n in range(64)];polys=[[sum((Vsmall[n][j]*(LP[n][k] if k<=n else 0) for n in range(64)),F(0)) for k in range(64)] for j in range(4)]
  terms,segments=geometry(prime);shifted=[[shift([I(x) for x in poly],term['offset']) for poly in polys] for term in terms];segs=[]
  for _,_,left,right,active in segments:
   src=[[sum((terms[a]['coefficient']*shifted[a][j][k] for a in active),I(0)) for k in range(64)] for j in range(4)];affine=[];length=right-left
   if replay:
    for poly in src:
     sh=shift(poly,left);power=I(1);row=[]
     for x in sh:row.append(x*power);power*=length
     affine.append(row)
   lp=rp=I(1);powers=[]
   for k in range(HEAD+64):lp*=left;rp*=right;powers.append((rp-lp)/F(k+1))
   segs.append((left,right,src,affine,powers))
  tm=[tuple(map(F,r)) for r in source['nominal_trial_exponential_moments']];trialmom=[]
  for v in vs:
   center=sum((v[i]*sum(tm[i])/2 for i in range(22)),F(0));radius=sum((abs(v[i])*(tm[i][1]-tm[i][0])/2 for i in range(22)),F(0));trialmom.append(rational_interval(center-radius,center+radius))
  H=[[ (F(0),F(0)) for _ in range(4)] for _ in range(64)]
  with ProcessPoolExecutor(max_workers=8,initializer=init,initargs=((forms,mom,segs,trialmom,replay),)) as pool:
   for j,values in pool.map(worker,range(4)):
    for n,(a,b) in values:
     if saved is not None:
      x,y=map(F,saved['new_weak_source_Legendre_pairing_enclosures'][n-64][j]);assert x<=a<=b<=y,(n,j,a,b,x,y);a,b=x,y
     H[n-64][j]=(a,b)
 else:
  assert not replay and pairing_cache['input_sha256']==h
  H=[[tuple(map(F,z)) for z in row] for row in pairing_cache['new_weak_source_Legendre_pairing_enclosures']]
 tau,tailcert=tail128(replay);oldtau=F(prior['rank_64_canonical_tail_certificate']['canonical_complement_embedding_norm_upper']);assert tau<oldtau
 assert tailcert['e_enclosure']==prior['rank_64_canonical_tail_certificate']['e_enclosure'] and tailcert['pi_enclosure']==prior['rank_64_canonical_tail_certificate']['pi_enclosure'];ratio=tau*tau/(oldtau*oldtau);alpha=F(prior['inherited_1250_complement_floor']);blocks=[];direction_results=[]
 for p,name in enumerate(['even','odd']):
  old=prior['weak_source_block_certificates'][p];hc=[[sum(H[n][p+2*j])/2 for j in range(2)] for n in range(64)];hr=[[(H[n][p+2*j][1]-H[n][p+2*j][0])/2 for j in range(2)] for n in range(64)];mass=[R/F(2*(n+64)+1) for n in range(64)]
  cap=[[sum((hc[n][i]*hc[n][j]/mass[n] for n in range(64)),F(0)) for j in range(2)] for i in range(2)];allow=[[sum(((abs(hc[n][i])*hr[n][j]+abs(hc[n][j])*hr[n][i])/mass[n] for n in range(64)),F(0)) for j in range(2)] for i in range(2)];assert psd(cap)
  wc=add(matrix(old['targeted_nominal_physical_residual_center']),cap,-1);wr=add(matrix(old['targeted_nominal_physical_residual_halfwidths']),allow);d=list(map(F,old['interval_balancing_scales']));wu=upper(wc,wr,d);N=scale(wu,tau*tau);E=scale(matrix(old['actual_projected_transfer_Gram_upper']),ratio)
  # Transport the tighter matching RC93 Riesz errors into the six signed
  # RC92 trial entries. This changes no trial, original source or basis.
  ep=matrix(old['targeted_physical_Riesz_error_Gram_upper']);ec=scale(ep,1/RHO)
  pv=[vs[p],vs[p+2]];tw=cong(tr(pv),cong(matrix(enriched['enriched_native_trial_coefficients']),[[R/F(2*n+1)*F(n==m) for m in range(64)] for n in range(64)]))
  uw=cong(tr(pv),matrix(source['nominal_complete_original_source_Gram_Loewner_upper']));delta=F(source['actual_source_approximation_operator_error_upper']);kp=F(transport['complete_physical_operator_parity_norm_upper'][p]);sn=[up(root(uw[i][i],10**40)+delta*root(tw[i][i],10**40),10**40) for i in range(2)]
  qlower=[[F(0)]*2 for _ in range(2)];qupper=[[F(0)]*2 for _ in range(2)];signed=[]
  for entry in head['known_weak_head_blocks'][p]['signed_entry_certificates']:
   i,j=entry['i'],entry['j'];qc=F(entry['trial_Weil_center']);qr=F(entry['trial_Weil_radius_upper']);linear=root(ep[i][i],10**40)*sn[j]+root(ep[j][j],10**40)*sn[i];physical=kp*root(ep[i][i]*ep[j][j],10**40);canonical=ec[i][i] if i==j else root(ec[i][i]*ec[j][j],10**40)
   a=down(qc-qr-linear-physical-canonical,10**40);b=up(qc+qr+linear+physical+(canonical if i!=j else 0),10**40);qlower[i][j]=qlower[j][i]=a;qupper[i][j]=qupper[j][i]=b
   signed.append(dict(i=i,j=j,trial_Weil_center=str(qc),trial_Weil_radius_upper=str(qr),linear_original_source_allowance=str(linear),physical_quadratic_allowance=str(physical),canonical_error_allowance=str(canonical),actual_original_Weil_lower=str(a),actual_original_Weil_upper=str(b)))
  qm=[[(qlower[i][j]+qupper[i][j])/2 for j in range(2)] for i in range(2)];qrad=[[(qupper[i][j]-qlower[i][j])/2 for j in range(2)] for i in range(2)];qlo=[[qm[i][j]-F(i==j)*sum((qrad[i][k]*d[k]/d[i] for k in range(2)),F(0)) for j in range(2)] for i in range(2)];assert qlo[0][0]>0 and qlo[0][0]*qlo[1][1]-qlo[0][1]**2>0
  tests=[]
  for t in [F(k,64) for k in range(1,129)]+[F(3),F(4),F(8),F(16)]:
   A=add(scale(N,1+t),E,1+1/t);tests.append((relative40(A,qlo),t))
  lam,t=min(tests);A=add(scale(N,1+t),E,1+1/t);corrected=add(qlo,A,-1/alpha);oldA=matrix(old['actual_rank_64_weak_source_coupling_Gram_upper']);assert psd(add(scale(qlo,lam),A,-1))
  positive=corrected[0][0]>0 and corrected[0][0]*corrected[1][1]-corrected[0][1]**2>0
  floor=F(0)
  if positive:
   # A<=lambda Qlo implies the retained corrected head fraction.
   assert lam<alpha and psd(add(corrected,scale(qlo,1-lam/alpha),-1))
   pv=[vs[p],vs[p+2]];Mhi=scale(cong(tr(pv),matrix(native['physical_native_Gram'])),F(native['actual_canonical_native_Gram_physical_upper_factor']));sc=scale(corrected,F(10**18));left,right=F(0),F(1)
   while psd(add(sc,scale(Mhi,right),-1)):right*=2
   for _ in range(40):
    middle=(left+right)/2
    if psd(add(sc,scale(Mhi,middle),-1)):left=middle
    else:right=middle
   floor=left/10**18;assert floor>0 and psd(add(corrected,scale(Mhi,floor),-1))
  blocks.append(dict(parity=name,new_physical_capture_increment_Gram=serialize(cap),new_capture_pairing_allowances=serialize(allow),nominal_physical_residual_center=serialize(wc),nominal_physical_residual_halfwidths=serialize(wr),nominal_physical_residual_Gram_upper=serialize(wu),nominal_projected_Gram_upper=serialize(N),actual_projected_transfer_Gram_upper=serialize(E),actual_rank_128_weak_source_coupling_Gram_upper=serialize(A),actual_rank_1250_weak_source_coupling_Gram_upper_via_nesting=serialize(A),Young_parameter=str(t),updated_signed_weak_head_entries=signed,updated_actual_original_weak_head_Loewner_lower=serialize(qlo),updated_actual_original_weak_head_entry_lower=serialize(qlower),updated_actual_original_weak_head_entry_upper=serialize(qupper),source_relative_updated_weak_head_lower_upper=str(lam),whole_weak_block_improves_RC93=psd(add(oldA,A,-1)),corrected_weak_block_Loewner_lower=serialize(corrected),corrected_weak_block_positive_definite=positive,corrected_weak_block_canonical_floor_lower=str(floor),fraction_of_updated_head_lower_retained=str(1-lam/alpha) if positive else None))
  for j in range(2):
   qdlower=qlower[j][j];qhi=qupper[j][j];margin=qdlower-A[j][j]/alpha
   direction_results.append(dict(parity=name,role='weak_'+str(j),actual_rank_128_coupling_squared_upper=str(A[j][j]),prior_rank_64_coupling_squared_upper=str(oldA[j][j]),upper_bound_fractional_reduction=str(1-A[j][j]/oldA[j][j]),actual_head_quadratic_lower=str(qdlower),actual_head_quadratic_upper=str(qhi),directional_Schur_lower=str(margin),directional_Schur_positivity_certified=margin>0))
 result=dict(milestone='RC94',status='PASS',input_sha256=h,trial_dimension=64,new_physical_source_pairing_degrees=[64,127],new_same_parity_source_pairing_count=128,weak_input_order=[dict(parity=d['parity'],role=d['role']) for d in directions],new_weak_source_Legendre_pairing_enclosures=[[[str(a),str(b)] for a,b in row] for row in H],rank_128_canonical_tail_certificate=tailcert,weak_source_block_certificates=blocks,weak_direction_certificates=direction_results,actual_projection_rank_bounded=128,complement_floor_projection_rank=1250,inherited_1250_complement_floor=str(alpha),actual_projection_nesting_analytic_proof_supplied=True,rank_128_Weil_head_evaluated=False,rank_128_Weil_complement_floor_claimed=False,complete_1250_head_evaluated=False,actual_coupling_lower_certified=False,certified_known_weak_Schur_parities=[b['parity'] for b in blocks if b['corrected_weak_block_positive_definite']],known_weak_Schur_blocks_certified=all(b['corrected_weak_block_positive_definite'] for b in blocks),complete_weak_mode_coverage_certified=False,strong_head_block_certified=False,weak_strong_cross_block_certified=False,matrix_Schur_positivity_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 if saved is not None:assert result==saved
 return result
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates';names=['rpb108_rc93_targeted_weak_source_capture.json','rpb108_rc92_signed_weak_head_reconstruction.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc56_precision_attached_head.json','rpb108_rc43_native_prime_head.json','rpb108_rc46_native_archimedean_head.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc66_arch_multiplier_transport.json'];defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: reflected arch moments, affine prime overlaps, positive pole recurrence, all 128 new weak source pairings, factorial/log tail replay and exact capture/Schur tests')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
