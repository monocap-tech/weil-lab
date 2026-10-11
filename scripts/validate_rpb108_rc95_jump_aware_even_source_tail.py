"""RC95: signed weighted derivative and rank-one jump source-tail bound.

The even weak source is decomposed into a continuous weighted-H1 part
and its exact common prime jump profile. No dense enlarged Weil head.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb,prod
from concurrent.futures import ProcessPoolExecutor
import json,hashlib,sys
import validate_rpb108_rc30_interval_metric as iv
from validate_rpb108_rc30_interval_metric import I,PI
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc35_enriched_residuals import transformed,integrate,convolution,reflect,polyadd,scalar
from validate_rpb108_rc31_trial_riesz import mm,tr,psd
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from validate_rpb108_rc43_native_prime_head import shift,poly_value
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize,root
from validate_rpb108_rc48_prime_source_covariance import geometry
from validate_rpb108_rc52_complete_source_covariance import primitives
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,cong
from validate_rpb108_rc89_frequency_weighted_arch_transfer import serieslog
from validate_rpb108_rc88_multiband_canonical_tail_transport import ceilgrid
from validate_rpb108_rc90_continuous_source_balance_and_method_floor import relative40
from validate_rpb108_rc93_targeted_weak_source_capture import upper
from validate_rpb108_rc94_weak_source_capture_128 import weak_source_forms,pole_test
from validate_rpb108_rc63_twenty_two_weak_floor_obstruction import up
R=F(11,5);B=R/2;RHO=F(252,257);HEAD=1250

def deriv(p):return [p[k]*k for k in range(1,len(p))]
def weighted(p):return convolution(p,[I(0),I(1),I(-1)])
def init(config):
 global WORK
 WORK=config

def primitive_alt(left,right,degree):
 # log(1-y) moments by reflection into log(u) and binomial expansion.
 a=primitives(left,degree,0 if left.l==left.h==0 else None);b=primitives(right,degree,1 if right.l==right.h==1 else None)
 out=[[b[q][k]-a[q][k] for k in range(degree+1)] for q in range(3)]
 ra=primitives(1-right,degree,0 if right.l==right.h==1 else None);rb=primitives(1-left,degree,1 if left.l==left.h==0 else None)
 out[2]=[sum(((-1)**l*comb(k,l)*(rb[1][l]-ra[1][l]) for l in range(k+1)),I(0)) for k in range(degree+1)]
 return out

def gram_worker(ij):
 i,j=ij;forms,mom,segs,replay=WORK;kind=[[0,1,2],[1,3,5],[2,5,4]]
 value=I(0)
 if replay:
  for a in range(3):
   for b in range(3):value+=integrate(weighted(forms[i][a]),forms[j][b],mom[kind[a][b]])
 else:
  value=integrate(weighted(forms[i][0]),forms[j][0],mom[0])+integrate(weighted(forms[i][1]),forms[j][1],mom[3])+integrate(weighted(forms[i][2]),forms[j][2],mom[4])
  for a,b,k in [(0,1,1),(0,2,2),(1,2,5)]:value+=integrate(weighted(forms[i][a]),forms[j][b],mom[k])+integrate(weighted(forms[i][b]),forms[j][a],mom[k])
 for left,right,src,pm in segs:
  if replay:
   length=right-left;a=shift(weighted(src[i]),left);b=shift(src[j],left);powers=[I(1)]
   for _ in range(len(a)+len(b)):powers.append(powers[-1]*length)
   value+=length*sum((x*y*powers[k+l]/F(k+l+1) for k,x in enumerate(a) for l,y in enumerate(b)),I(0))
  else:value+=integrate(weighted(src[i]),src[j],pm[0])
  for k in range(3):value+=integrate(weighted(forms[i][k]),src[j],pm[k])+integrate(weighted(src[i]),forms[j][k],pm[k])
  print('weighted signed derivative',i,j,'segment checked',file=sys.stderr,flush=True)
 return i,j,outward(value,10**(32 if replay else 30))

def jump_tail(prime,replay,saved=None):
 terms,segs=geometry(prime);rows=prime['active_prime_powers'];cs=[1-I(r['n']).log()/B for r in rows];weights=[-I(r['base_prime']).log()/I(r['n']).sqrt() for r in rows]
 knots=[]
 for c,w in zip(cs,weights):knots.extend([(-c,w),(c,-w)])
 knots.sort(key=lambda z:z[0].l)
 for (c,_),(d,_) in zip(knots,knots[1:]):assert c.h<d.l
 if replay:
  norm=B*sum((a*b*(1-(c if c.l>d.h else d)) for c,a in knots for d,b in knots),I(0))
 else:
  norm=I(0);value=I(0);left=I(-1)
  for c,w in knots:norm+=B*(c-left)*value*value;value+=w;left=c
  # The exact total jump is zero, so the final exterior value is zero.
 P=[[I(1),c] for c in cs];DP=[[I(0),I(1)] for _ in cs]
 for k in range(1,HEAD):
  for a,c in enumerate(cs):
   P[a].append(((2*k+1)*c*P[a][k]-k*P[a][k-1])/(k+1))
   if replay:DP[a].append(((2*k+1)*(P[a][k]+c*DP[a][k])-k*DP[a][k-1])/(k+1))
 capture=I(0);coefs=[]
 for n in range(0,HEAD,2):
  if n==0:h=2*B*sum((w*c for w,c in zip(weights,cs)),I(0))
  elif replay:h=-2*B*sum((w*(1-c*c)*d[n]/F(n*(n+1)) for w,c,d in zip(weights,cs,DP)),I(0))
  else:h=-2*B*sum((w*(p[n-1]-p[n+1])/F(2*n+1) for w,p in zip(weights,P)),I(0))
  capture+=h*h/(R/F(2*n+1));lo,hi=outward(h,10**40);coefs.append([str(lo),str(hi)])
 tl,tu=outward(norm-capture,10**(42 if replay else 40));assert 0<tl<tu
 if saved is not None:
  a,b=map(F,saved['physical_jump_profile_tail_norm_squared_enclosure']);assert a<=tl<=tu<=b;tl,tu=a,b
  old=saved['even_jump_profile_Legendre_pairing_enclosures'];assert all(F(a)<=F(c)<=F(d)<=F(b) for (a,b),(c,d) in zip(old,coefs));coefs=old
 return tu,dict(head_degree_count=HEAD,physical_jump_profile_norm_squared_enclosure=list(map(str,outward(norm,10**40))),physical_jump_profile_capture_squared_enclosure=list(map(str,outward(capture,10**40))),physical_jump_profile_tail_norm_squared_enclosure=list(map(str,[tl,tu])),even_jump_profile_Legendre_pairing_enclosures=coefs)

def tail1250(replay):
 elo,ehi=outward(I(1).exp(),10**30);pilo,pihi=outward(PI,10**30);df=prod(range(1,2*HEAD+2,2));energy=F(1);prev=F(0);rows=[]
 if replay:assert df==F(factorial(2*HEAD+1),2**HEAD*factorial(HEAD))
 for k in range(1,400):
  cut=F(k,2);z=2*pihi*B*cut;r=z*z/F(2*HEAD+3)**2;assert r<1
  theta=4*B*cut*z**(2*HEAD)/(F(df)**2*(1-r));th=min(F(1),ceilgrid(theta,10**50));q=(ehi+cut)/(ehi+prev);lo,hi=outward(I(q).log(),10**40)
  if replay:
   a,b=serieslog(q);assert lo<=a<=b<=hi
  term=lo*(1-th);energy+=term;rows.append(dict(cut=str(cut),low_frequency_energy_fraction_upper=str(th),weight_increment_lower=str(lo),energy_contribution=str(term)));prev=cut
  if th==1:break
 assert th==1
 tau=root(1/energy,10**30);assert tau*tau*energy>=1
 return tau,dict(head_degree_count=HEAD,frequency_step='1/2',e_enclosure=list(map(str,[elo,ehi])),pi_enclosure=list(map(str,[pilo,pihi])),layers=rows,canonical_energy_relative_physical_lower=str(energy),canonical_complement_embedding_norm_upper=str(tau))

def run(paths,replay=False,saved=None):
 # Direct interval recurrence at degree 1250 needs a guard against
 # dependency amplification. These contexts are private to this process.
 for ctx in [iv.loctx,iv.hictx,iv.near]:ctx.prec=800
 raw=[Path(p).read_bytes() for p in paths];prior,weak,enriched,native,precision,prime,arch,source=map(json.loads,raw);h=[hashlib.sha256(x).hexdigest() for x in raw]
 assert prior['input_sha256'][2:9]==[h[i] for i in [1,2,3,4,5,6,7]]
 assert source['input_sha256'][:4]==[h[i] for i in [2,3,4,5]] and source['input_sha256'][5]==h[6]
 assert prior['certified_known_weak_Schur_parities']==['odd']
 selected=[next(a for a in weak['fixed_rational_direction_certificates'] if a['parity']==p and a['role']==r) for r in ['weak_0','weak_1'] for p in ['even','odd']];vs=[list(map(F,a['coefficients'])) for a in selected];W=tr(vs);V=mm(matrix(enriched['enriched_native_trial_coefficients']),W);C=mm(matrix(native['chebyshev_to_legendre']),W)
 forms,mom,trial,target=weak_source_forms({'enriched_native_trial_coefficients':serialize(V)},{'chebyshev_to_legendre':serialize(C)},arch,precision)
 assert all(V[n][j]==0 for n in range(1,64,2) for j in [0,2]) and all(C[n][j]==0 for n in range(1,22,2) for j in [0,2])
 ds=[];eta=[]
 for j in [0,2]:
  A,L,M=forms[j];assert L[0].l==L[0].h==0
  ld=L[1:];a=polyadd(deriv(A),polyadd(ld,reflect(ld),-1));l=deriv(L);m=deriv(M)
  tm=sum((I(V[n][j])*pole_test(n,replay) for n in range(64)),I(0))
  pt=[I(0)]*81
  for k in range(1,81,2):pt[k]=R*tm*(B/2)**k/factorial(k)
  # Rational affine transformation of the Taylor polynomial.
  py=[sum((pt[n]*comb(n,k)*2**k*(-1)**(n-k) for n in range(k,len(pt))),I(0)) for k in range(len(pt))];a=polyadd(a,py)
  amp=max(abs(F(tm.l)),abs(F(tm.h)));eta.append(up(R*amp*2*(B/2)**81/factorial(81),10**120));ds.append((a,l,m))
 terms,segs0=geometry(prime);LP=[legendre(n) for n in range(64)];polys=[[sum((V[n][j]*(LP[n][k] if k<=n else 0) for n in range(64)),F(0)) for k in range(64)] for j in [0,2]];edges=[sum((V[n][j] for n in range(64)),F(0)) for j in [0,2]]
 assert all(sum(polys[i],F(0))==edges[i] and sum(((-1)**k*a for k,a in enumerate(polys[i])),F(0))==edges[i] for i in range(2))
 translated=[[deriv([x*2**k for k,x in enumerate(shift([I(a) for a in p],term['offset']-1))]) for p in polys] for term in terms];segs=[];cache={}
 for ln,rn,left,right,active in segs0:
  left=(left+1)/2;right=(right+1)/2;src=[[sum((terms[k]['coefficient']*translated[k][j][l] for k in active),I(0)) for l in range(63)] for j in range(2)]
  if replay:pm=primitive_alt(left,right,320)
  else:
   for name,x in [(ln,left),(rn,right)]:
    if name not in cache:cache[name]=primitives(x,320,0 if name=='left' else 1 if name=='right' else None)
   pm=[[cache[rn][a][k]-cache[ln][a][k] for k in range(321)] for a in range(3)]
  segs.append((left,right,src,pm))
 dc=[[F(0)]*2 for _ in range(2)];dr=[[F(0)]*2 for _ in range(2)];intervals=[]
 with ProcessPoolExecutor(max_workers=3,initializer=init,initargs=((ds,mom,segs,replay),)) as pool:
  for i,j,(a,b) in pool.map(gram_worker,[(0,0),(0,1),(1,1)]):
   if saved is not None:
    row=next(z for z in saved['weighted_signed_derivative_Gram_entry_enclosures'] if z['i']==i and z['j']==j);x,y=map(F,row['interval']);assert x<=a<=b<=y;a,b=x,y
   dc[i][j]=dc[j][i]=(a+b)/2;dr[i][j]=dr[j][i]=(b-a)/2;intervals.append(dict(i=i,j=j,interval=list(map(str,[a,b]))))
 du=upper(dc,dr,[F(100),F(1)]);nu=F(1,65536);poleerror=[[F(i==j)*eta[i]**2/3 for j in range(2)] for i in range(2)];D=add(scale(du,1+nu),poleerror,1+1/nu)
 jt,jumpcert=jump_tail(prime,replay,None if saved is None else saved['jump_profile_certificate']);J=[[jt*edges[i]*edges[j] for j in range(2)] for i in range(2)];assert psd(J) and psd(D)
 tau,tailcert=tail1250(replay);oldtau=F(prior['rank_128_canonical_tail_certificate']['canonical_complement_embedding_norm_upper']);assert tau<oldtau
 continuous=scale(D,R/F(HEAD*(HEAD+1)));old=prior['weak_source_block_certificates'][0];E=scale(matrix(old['actual_projected_transfer_Gram_upper']),tau*tau/(oldtau*oldtau));qlo=matrix(old['updated_actual_original_weak_head_Loewner_lower']);alpha=F(prior['inherited_1250_complement_floor']);tests=[]
 grid=[F(1,32),F(1,16),F(1,8),F(1,4),F(1,2),F(1),F(2),F(4),F(8),F(16)]
 for s in grid:
  N=scale(add(scale(continuous,1+s),J,1+1/s),tau*tau)
  for t in grid:
   A=add(scale(N,1+t),E,1+1/t);tests.append((relative40(A,qlo),s,t))
 lam,s,t=min(tests);N=scale(add(scale(continuous,1+s),J,1+1/s),tau*tau);A=add(scale(N,1+t),E,1+1/t);corrected=add(qlo,A,-1/alpha);assert psd(add(scale(qlo,lam),A,-1));positive=corrected[0][0]>0 and corrected[0][0]*corrected[1][1]-corrected[0][1]**2>0
 result=dict(milestone='RC95',status='PASS',input_sha256=h,precision=800,source_target='known even weak_0 and weak_1, unchanged original RC67 trials',weighted_signed_derivative_Gram_entry_enclosures=intervals,weighted_signed_derivative_Gram_upper=serialize(D),pole_derivative_Taylor_error_norm_uppers=list(map(str,eta)),trial_right_endpoint_values=list(map(str,edges)),jump_profile_certificate=jumpcert,rank_one_jump_tail_Gram_upper=serialize(J),continuous_weighted_H1_physical_tail_Gram_upper=serialize(continuous),rank_1250_canonical_tail_certificate=tailcert,inner_continuous_jump_Young_parameter=str(s),outer_nominal_transfer_Young_parameter=str(t),nominal_projected_source_Gram_upper=serialize(N),actual_projected_transfer_Gram_upper=serialize(E),actual_rank_1250_even_weak_source_coupling_Gram_upper=serialize(A),source_relative_RC94_even_weak_head_lower_upper=str(lam),inherited_1250_complement_floor=str(alpha),corrected_even_weak_block_Loewner_lower=serialize(corrected),corrected_even_weak_block_positive_definite=positive,whole_even_source_upper_improves_RC94=psd(add(matrix(old['actual_rank_128_weak_source_coupling_Gram_upper']),A,-1)),odd_weak_Schur_certificate_retained_from_RC94=True,known_weak_Schur_blocks_certified=positive,weighted_Legendre_tail_analytic_proof_supplied=True,prime_jump_covariance_rank_one=True,dense_1250_Weil_head_evaluated=False,actual_coupling_lower_certified=False,complete_weak_mode_coverage_certified=False,strong_head_block_certified=False,weak_strong_cross_block_certified=False,matrix_Schur_positivity_certified=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
 result=finish(result,prior,weak,native)
 if saved is not None:assert result==saved
 return result
def finish(result,prior,weak,native):
 alpha=F(result['inherited_1250_complement_floor']);lam=F(result['source_relative_RC94_even_weak_head_lower_upper']);qlo=matrix(prior['weak_source_block_certificates'][0]['updated_actual_original_weak_head_Loewner_lower']);corrected=matrix(result['corrected_even_weak_block_Loewner_lower']);floor=F(0)
 if result['corrected_even_weak_block_positive_definite']:
  fraction=1-lam/alpha;assert fraction>0 and psd(add(corrected,scale(qlo,fraction),-1))
  vs=[list(map(F,a['coefficients'])) for a in weak['fixed_rational_direction_certificates'] if a['parity']=='even' and a['role'].startswith('weak')];Mhi=scale(cong(tr(vs),matrix(native['physical_native_Gram'])),F(native['actual_canonical_native_Gram_physical_upper_factor']));sc=scale(corrected,F(10**18));left,right=F(0),F(1)
  while psd(add(sc,scale(Mhi,right),-1)):right*=2
  for _ in range(40):
   middle=(left+right)/2
   if psd(add(sc,scale(Mhi,middle),-1)):left=middle
   else:right=middle
  floor=left/10**18;assert floor>0 and psd(add(corrected,scale(Mhi,floor),-1))
 odd=prior['weak_source_block_certificates'][1];oddC=matrix(odd['corrected_weak_block_Loewner_lower']);assert odd['corrected_weak_block_positive_definite'] and oddC[0][0]>0 and oddC[0][0]*oddC[1][1]-oddC[0][1]**2>0
 result.update(corrected_even_weak_block_canonical_floor_lower=str(floor),fraction_of_even_head_lower_retained=str(1-lam/alpha) if floor>0 else None,retained_odd_weak_block_canonical_floor_lower=odd['corrected_weak_block_canonical_floor_lower'],parity_orthogonality_analytic_proof_supplied=True,full_four_known_weak_span_corrected_positive_definite=floor>0,full_four_known_weak_span_canonical_floor_lower=str(min(floor,F(odd['corrected_weak_block_canonical_floor_lower']))) if floor>0 else '0')
 return result

if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates';names=['rpb108_rc94_weak_source_capture_128.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc56_precision_attached_head.json','rpb108_rc43_native_prime_head.json','rpb108_rc46_native_archimedean_head.json','rpb108_rc68_enriched_original_source_covariance.json'];defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  run(sys.argv[3:] or defaults,True,json.loads(Path(sys.argv[2]).read_text()));print('PASS: ordered log Gram, reflected incomplete log moments, affine prime derivative overlaps, derivative jump coefficients and step-overlap kernel, exact source-tail Schur tests')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
