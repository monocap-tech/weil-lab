"""RC83: certified 64-mode canonical response to the complete nominal source.

The trial space is canonical physical Legendre span, not the rank-38 Riesz
projection head. The source retains 22 inputs and the original RC67 trials.
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

N=22;HEAD=64;R=F(11,5);B=R/2;RHO=F(252,257)
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

from validate_rpb108_rc59_twenty_two_native_projection import nearest
def run(paths,replay=False,saved=None):
 raw=[Path(p).read_bytes() for p in paths]
 head,enriched,native,precision,prime,arch,source,transport,prior,attachment=map(json.loads,raw)
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert head['input_sha256'][:2]==hashes[1:3]
 assert [source['input_sha256'][k] for k in [0,1,2,3,5,6]]==[hashes[k] for k in [1,2,3,4,5,7]]
 assert head['actual_orthogonal_projection_rank_certified']==38
 assert prior['input_sha256']==hashes[:8]
 assert attachment['milestone']=='RC82'
 assert [attachment['input_sha256'][k] for k in [2,3,4,5,6]]==[hashes[k] for k in [1,6,8,2,0]]
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
    if n<38:
     old=tuple(map(F,prior['nominal_physical_Legendre_source_pairing_enclosures'][n][j]));assert old[0]<=a<=b<=old[1],(n,j);a,b=old
    if saved is not None:
     old=tuple(map(F,saved['nominal_physical_Legendre_source_pairing_enclosures'][n][j]));assert old[0]<=a<=b<=old[1],(n,j);a,b=old
    H[n][j]=(a+b)/2;Rh[n][j]=(b-a)/2
   progress('rectangular physical source pairing column '+str(j)+' checked')
 for n in range(HEAD):intervals.append([[str(H[n][j]-Rh[n][j]),str(H[n][j]+Rh[n][j])] for j in range(N)])
 G=matrix(enriched['recentered_nominal_metric_center']);delta=F(enriched['actual_recentered_metric_mass_error_upper'])
 mass=list(map(F,enriched['physical_mass']));D=[[mass[i]*F(i==j) for j in range(HEAD)] for i in range(HEAD)]
 assert len(G)==HEAD and psd(add(add(G,D,-delta),D,-1))
 GI=inverse(G);Zexact=mm(GI,H);Z=[[nearest(x,10**40) for x in row] for row in Zexact]
 assert all(Z[n][j]==0 for n in range(HEAD) for j in range(N) if (n-j)%2)
 if saved is not None:assert serialize(Z)==saved['nominal_source_canonical_trial_response_coefficients']
 ZT=mm(mm(tr(Z),D),Z);ZG=mm(mm(tr(Z),G),Z);HZ=mm(tr(H),Z)
 Q=mm(tr([[abs(x) for x in row] for row in Z]),Rh)
 # |Z' DeltaH + DeltaH' Z| is bounded in Loewner order by
 # the diagonal row sums of Q+Q'. No pointwise interval shortcut.
 pairing=[[F(i==j)*sum((Q[i][k]+Q[k][i] for k in range(N)),F(0)) for j in range(N)] for i in range(N)]
 allowance=add(pairing,ZT,delta)
 Lraw=add(add(add(HZ,tr(HZ)),ZG,-1),allowance,-1)
 if replay:
  # Independent square completion, including rational solve rounding.
  diff=add(Z,Zexact,-1)
  alternate=add(mm(tr(H),Zexact),mm(mm(tr(diff),G),diff),-1)
  assert alternate==add(Lraw,allowance)
  for i in range(HEAD):
   for j in range(N):assert sum((G[i][k]*Zexact[k][j] for k in range(HEAD)),F(0))==H[i][j]
 L,lround=rounded_bound(Lraw,-1,10**24);assert psd(L)
 U=matrix(source['nominal_complete_original_source_Gram_Loewner_upper']);baseline=scale(U,RHO)
 # ||i* F_nom - Z||^2 <= rho U - (H'Z+Z'H-Z'G_actual Z).
 error,eround=rounded_bound(add(baseline,Lraw,-1),1,10**24)
 assert psd(error) and psd(add(baseline,error,-1))
 # L also lower-bounds the actual canonical Ritz capture H_actual' G_actual^-1 H_actual.
 energylo=rounded_bound(add(ZG,ZT,-delta),-1,10**24)[0]
 energyhi=rounded_bound(add(ZG,ZT,delta),1,10**24)[0]
 assert psd(energylo) and psd(add(energyhi,energylo,-1))
 Mlo=matrix(enriched['enriched_actual_native_Gram_Loewner_lower']);bounds=[]
 for p in range(2):
  b=relative(block(error,p),block(Mlo,p));zero=relative(block(baseline,p),block(Mlo,p))
  assert psd(add(scale(block(Mlo,p),b),block(error,p),-1))
  bounds.append(dict(parity='even' if p==0 else 'odd',trial_response_error_relative_original_canonical_input_Gram_upper=str(b),zero_response_relative_upper=str(zero)))
 diagnostics=[dict(feature=j,zero_response_squared_norm_upper=str(baseline[j][j]),canonical_trial_response_error_squared_upper=str(error[j][j]),diagonal_upper_bound_fractional_reduction=str(1-error[j][j]/baseline[j][j])) for j in range(N)]
 progress('canonical nominal-source response and exact Loewner bounds checked')
 return dict(milestone='RC83',status='PASS',input_sha256=hashes,physical_canonical_trial_dimension=HEAD,actual_Riesz_projection_head_rank_retained=38,source_input_features=list(range(N)),
  nominal_source_definition='F_nom=q+K_nom V64, with the unchanged RC67 original Riesz trial coefficients and complete RC68 signed source',
  response_definition='Z=round_1e40(G64_center^-1 H64_center); canonical physical Legendre trial response to i* F_nom',
  nominal_physical_Legendre_source_pairing_enclosures=intervals,first_38_pairing_enclosures_preserved_exactly=True,
  same_parity_pairings_certified=HEAD*N//2,nominal_source_canonical_trial_response_coefficients=serialize(Z),
  pairing_uncertainty_Loewner_allowance=serialize(pairing),actual_metric_response_uncertainty_Loewner_allowance=serialize(scale(ZT,delta)),
  actual_canonical_trial_response_Gram_Loewner_lower=serialize(energylo),actual_canonical_trial_response_Gram_Loewner_upper=serialize(energyhi),
  actual_canonical_nominal_source_and_Ritz_capture_Gram_Loewner_lower=serialize(L),capture_lower_rounding_row_allowances=list(map(str,lround)),
  actual_canonical_nominal_source_trial_response_error_Gram_Loewner_upper=serialize(error),response_error_rounding_row_allowances=list(map(str,eround)),
  whole_Loewner_improvement_over_zero_response_certified=True,parity_response_error_certificates=bounds,diagonal_response_error_diagnostics=diagnostics,
  actual_metric_used=True,complete_nominal_source_used=True,actual_original_source_uncertainty_attached=False,
  actual_rank_38_projected_response_evaluated=False,RC82_rank_38_source_bound_retained_unchanged=True,
  required_scalar_source_budget_certified=False,actual_rank_38_scalar_budget_failure_proved=False,
  thirty_eight_positive_Weil_floor_certified=False,thirty_eight_complement_floor_certified=False,
  whole_aperture_positivity_extended=False,RH=False,F4=False)
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 names=['rpb108_rc70_thirty_eight_native_projection.json','rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc56_precision_attached_head.json','rpb108_rc43_native_prime_head.json','rpb108_rc46_native_archimedean_head.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc66_arch_multiplier_transport.json','rpb108_rc71_thirty_eight_projected_old_source.json','rpb108_rc82_direct_error_source_attachment.json']
 defaults=[base/n for n in names]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,saved)==saved
  print('PASS: reflected archimedean, affine prime and closed exponential pairing replay; exact response square completion and Loewner bounds')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
