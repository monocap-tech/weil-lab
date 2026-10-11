"""RC71: actual rank-38 residual for the existing 22-input original source.

Physical polynomial subtraction maps EXACTLY into the actual Riesz head.
No enlarged 38-input covariance or Weil/complement floor is asserted.
"""
from fractions import Fraction as F
from pathlib import Path
from math import comb
from concurrent.futures import ProcessPoolExecutor
import json,hashlib,sys
from validate_rpb108_rc30_interval_metric import I
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc35_enriched_residuals import transformed,integrate
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from validate_rpb108_rc43_native_prime_head import shift
from validate_rpb108_rc47_correlated_native_transport import matrix,serialize
from validate_rpb108_rc48_prime_source_covariance import geometry
from validate_rpb108_rc57_uniform_low_head_floor import rounded_bound
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale,block,cong,relative
from validate_rpb108_rc68_enriched_original_source_covariance import source_forms
from validate_rpb108_rc69_enriched_complementary_leakage import exp_moment

N=22;HEAD=38;R=F(11,5);B=R/2;RHO=F(252,257)
def progress(s):print(s,file=sys.stderr,flush=True)
def init(data):
 global WORK
 WORK=data

def worker(j):
 forms,mom,segs,testmom,trialmom,replay=WORK
 prime_mom=[I(0)]*HEAD
 for left,right,source,affine,powers in segs:
  if replay:
   length=right-left
   # Affine u-moments followed by the binomial reconstruction of t^k.
   am=[B*length*sum((x/F(l+m+1) for l,x in enumerate(affine[j])),I(0)) for m in range(HEAD)]
   lp=[I(1)];dp=[I(1)]
   for _ in range(HEAD):lp.append(lp[-1]*left);dp.append(dp[-1]*length)
   for k in range(HEAD):prime_mom[k]+=sum((I(comb(k,m))*lp[k-m]*dp[m]*am[m] for m in range(k+1)),I(0))
  else:
   for k in range(HEAD):prime_mom[k]+=B*sum((x*powers[k+l] for l,x in enumerate(source[j])),I(0))
 A,L,M=forms[j];out=[]
 for n in range(j%2,HEAD,2):
  z=legendre(n);zy=[I(x) for x in transformed(z)]
  ap=R*(integrate(zy,A,mom[0])+2*integrate(zy,L,mom[1])) if replay else R*(integrate(zy,A,mom[0])+integrate(zy,L,mom[1])+integrate(zy,M,mom[2]))
  pp=sum((I(x)*prime_mom[k] for k,x in enumerate(z)),I(0))
  pole=2*(-1)**n*testmom[n]*trialmom[j]
  out.append((n,outward(ap+pp+pole,10**24)))
 return j,out

def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths]
 head,enriched,native,precision,prime,arch,source,transport=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert head['input_sha256'][:2]==hashes[1:3]
 assert [source['input_sha256'][k] for k in [0,1,2,3,5,6]]==[hashes[k] for k in [1,2,3,4,5,7]]
 assert head['actual_orthogonal_projection_rank_certified']==HEAD
 assert source['native_features_certified']==list(range(N))
 forms,mom,trials,targets=source_forms(enriched,native,arch,precision)
 V=matrix(enriched['enriched_native_trial_coefficients']);LP=[legendre(n) for n in range(64)]
 polys=[[sum((V[n][j]*(LP[n][k] if k<=n else 0) for n in range(64)),F(0)) for k in range(64)] for j in range(N)]
 terms,segments=geometry(prime);shifted=[[shift([I(x) for x in poly],term['offset']) for poly in polys] for term in terms]
 segs=[]
 for _,_,left,right,active in segments:
  src=[[sum((terms[h]['coefficient']*shifted[h][j][k] for h in active),I(0)) for k in range(64)] for j in range(N)]
  affine=[];length=right-left
  if replay:
   for poly in src:
    sh=shift(poly,left);power=I(1);row=[]
    for x in sh:row.append(x*power);power*=length
    affine.append(row)
  lp=I(1);rp=I(1);powers=[]
  for k in range(HEAD+64):
   lp*=left;rp*=right;powers.append((rp-lp)/F(k+1))
  segs.append((left,right,src,affine,powers))
 testmom=[exp_moment(legendre(n),F(1),replay) for n in range(HEAD)]
 trialmom=[rational_interval(*map(F,row)) for row in source['nominal_trial_exponential_moments']]
 H=[[F(0)]*N for _ in range(HEAD)];Rh=[[F(0)]*N for _ in range(HEAD)]
 intervals=[]
 with ProcessPoolExecutor(max_workers=8,initializer=init,initargs=((forms,mom,segs,testmom,trialmom,replay),)) as pool:
  for j,values in pool.map(worker,range(N)):
   for n,(a,b) in values:
    if saved is not None:
     old=tuple(map(F,saved['nominal_physical_Legendre_source_pairing_enclosures'][n][j]));assert old[0]<=a<=b<=old[1],(n,j);a,b=old
    H[n][j]=(a+b)/2;Rh[n][j]=(b-a)/2
   progress('rectangular physical source pairing column '+str(j)+' checked')
 for n in range(HEAD):intervals.append([[str(H[n][j]-Rh[n][j]),str(H[n][j]+Rh[n][j])] for j in range(N)])
 U=matrix(source['nominal_complete_original_source_Gram_Loewner_upper']);mass=list(map(F,enriched['physical_mass']))
 Mlo=matrix(enriched['enriched_actual_native_Gram_Loewner_lower']);phys=matrix(source['enriched_source_transfer_physical_Gram_Loewner_upper'])
 assert psd(U) and psd(phys)
 results=[];Ws=[];Ls=[]
 for count in [22,38]:
  Hc=H[:count];Rc=Rh[:count];L=[[x/mass[n] for x in row] for n,row in enumerate(Hc)]
  G= [[mass[i]*F(i==j) for j in range(count)] for i in range(count)]
  absL=[[abs(x) for x in row] for row in L];Q=mm(tr(absL),Rc);QT=mm(tr(Rc),absL)
  allowance=[[F(i==j)*sum((Q[i][k]+QT[i][k] for k in range(N)),F(0)) for j in range(N)] for i in range(N)]
  if replay:
   # Complete square in physical polynomial coefficient space.
   Lopt=[[x/mass[n] for x in row] for n,row in enumerate(Hc)];diff=[[x-y for x,y in zip(a,b)] for a,b in zip(L,Lopt)]
   W=add(add(U,mm(tr(Hc),Lopt),-1),mm(mm(tr(diff),G),diff))
  else:
   HL=mm(tr(Hc),L);W=add(add(add(U,HL,-1),tr(HL),-1),mm(mm(tr(L),G),L))
  W=rounded_bound(add(W,allowance),1,10**24)[0];assert psd(W);Ws.append(W);Ls.append(L)
  parity=[];chosen=[]
  grid=[F(1,16),F(1,8),F(1,4),F(1,2),F(1),F(2),F(4),F(8),F(16)]
  for p in range(2):
   candidates=[]
   for t in grid:
    Ap=scale(add(scale(block(W,p),1+t),block(phys,p),1+1/t),RHO)
    lam=relative(Ap,block(Mlo,p));candidates.append((lam,t))
   lam,t=min(candidates);chosen.append(t)
   parity.append(dict(parity='even' if p==0 else 'odd',Young_parameter=str(t),actual_residual_relative_original_canonical_input_Gram_upper=str(lam),candidate_bounds=[dict(Young_parameter=str(t0),upper=str(l0)) for l0,t0 in candidates]))
  A=rounded_bound([[RHO*((1+chosen[i%2])*W[i][j]+(1+1/chosen[i%2])*phys[i][j]) for j in range(N)] for i in range(N)],1,10**24)[0]
  # Recheck after the final rounding; no uncharged displayed bound.
  for p in range(2):
   lam=relative(block(A,p),block(Mlo,p));parity[p]['actual_residual_relative_original_canonical_input_Gram_upper']=str(lam)
  bound=max(F(x['actual_residual_relative_original_canonical_input_Gram_upper']) for x in parity)
  results.append(dict(actual_projection_rank=count,nominal_physical_polynomial_residual_Gram_Loewner_upper=serialize(W),physical_pairing_interval_Gram_allowance=serialize(allowance),actual_canonical_projected_source_residual_Gram_Loewner_upper=serialize(A),parity_certificates=parity,actual_residual_relative_original_canonical_input_Gram_upper=str(bound)))
  progress('projection rank '+str(count)+' actual 22-input bound '+str(bound))
 # The nominal central capture increment is exact PSD. It is not asserted
 # to equal the actual canonical gain, whose pairings are not evaluated.
 capture=mm(tr(H[22:]),Ls[1][22:]);assert psd(capture)
 if replay:
  C=matrix(native['chebyshev_to_legendre']);Ci=inverse(C)
  for result in results:
   A=matrix(result['actual_canonical_projected_source_residual_Gram_Loewner_upper'])
   for p in range(2):
    lam=F(result['parity_certificates'][p]['actual_residual_relative_original_canonical_input_Gram_upper'])
    assert psd(cong(block(Ci,p),add(scale(block(Mlo,p),lam),block(A,p),-1)))
  for n in range(HEAD):
   for k in range(HEAD):
    exact=sum((x*y*R/F(a+b+1) for a,x in enumerate(LP[n]) for b,y in enumerate(LP[k]) if (a+b)%2==0),F(0))
    assert exact==mass[n]*F(n==k)
 prior=F(source['enriched_actual_rank_22_projected_source_relative_canonical_native_Gram_upper']);new=F(results[1]['actual_residual_relative_original_canonical_input_Gram_upper'])
 retained=min(prior,new)
 return dict(milestone='RC71',status='PASS',input_sha256=hashes,source_input_features=list(range(N)),actual_projection_target_features=list(range(HEAD)),
  source_definition=source['original_source_definition'],physical_polynomial_subtraction_maps_exactly_into_actual_head=True,
  nominal_physical_Legendre_source_pairing_enclosures=intervals,physical_polynomial_subtraction_coefficients=serialize(Ls[1]),
  residual_certificates=results,nominal_center_physical_capture_increment_Gram=serialize(capture),
  prior_RC68_rank_22_relative_bound=str(prior),direct_rank_38_physical_subtraction_relative_bound=str(new),
  actual_rank_38_relative_bound_for_existing_22_source_inputs=str(retained),certified_uniform_fractional_reduction_from_RC68=str(1-retained/prior),
  actual_canonical_projection_gain_evaluated=False,thirty_eight_source_input_covariance_evaluated=False,
  required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,
  thirty_eight_positive_Weil_floor_certified=False,thirty_eight_complement_floor_certified=False,
  whole_aperture_positivity_extended=False,RH=False,F4=False)
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/n for n in ['rpb108_rc70_thirty_eight_native_projection.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc56_precision_attached_head.json','rpb108_rc43_native_prime_head.json','rpb108_rc46_native_archimedean_head.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc66_arch_multiplier_transport.json']]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,saved)==saved
  print('PASS: reflected archimedean and affine prime moments, closed exponential tests, exact physical orthogonality, square completion and canonical comparison replay')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
