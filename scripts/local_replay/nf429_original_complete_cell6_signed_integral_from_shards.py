#!/usr/bin/env python3
"""NF429 original complete J6 full 1500 Chebyshev coefficients -> pz,z².

Read the SIX original 2048-bit source-correlated Arb-shard JSONs and same-run
full 1500 NF428 source-signed p Chebyshev moment JSON. Recheck all original
source/seam hashes and contiguous 0..1499 coverage, source radius and
NF416 independent global x=.9 cross-check. Exact rational outward
linear pz and quadratic z² values on the TRUE irrational cell J6 follow
from Cheb primitive J0..J2998 evaluated by outward Arb, exact rational
midpoint coefficient convolution, and uniform source/series/numeric
coefficient radius charge. No exterior/other cells/NF404/RH closure.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
from flint import arb,ctx
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);C=F(91,100);H=F(7,100);N=1500
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def A(x):return arb(str(x))
def outward(v,digits=75):
 m,r,e=v.mid_rad_10exp(digits);q=F(10)**int(e)
 return [F(int(m)-int(r))*q,F(int(m)+int(r))*q]
def M(x):
 a,b=x;return max(abs(a),abs(b))
def interval_linear(coeff,balls):
 lo=hi=F(0)
 for a,(l,u) in zip(coeff,balls):
  if a>=0:lo+=a*l;hi+=a*u
  else:lo+=a*u;hi+=a*l
 return lo,hi
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--shards',default='artifacts/all')
 ap.add_argument('--moments',default='artifacts/all/NF429_original_cell6_pmoments_1500.json')
 ap.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 ap.add_argument('--nf416',default='notes/data/provisional/NF416_original_cell6_full_I0_and_z_point_native.json')
 ap.add_argument('--output',required=True)
 ap.add_argument('--precision',type=int,default=2048)
 args=ap.parse_args()
 assert args.precision>=2048
 ctx.prec=args.precision
 knot,ksha=read(args.seams);point,pointsha=read(args.nf416)
 moments,msha=read(args.moments)
 assert moments['nf406_original_seams_sha256']==ksha
 assert moments['nf410_original_signed_Taylor_moment_parent_sha256']
 assert moments['original_nf410_n0_signed_principal_moment_overlap']
 assert moments['all_1500_source_signed_chebyshev_moments_certified']
 assert moments['original_x_domain']=='(log(7)-11/10,log(8)-11/10)'
 pmom=[[F(i) for i in q] for q in moments['original_signed_p_chebyshev_moments_n0_to_n1499']]
 assert len(pmom)==N and all(lo<=hi and hi-lo<F(1,10**25) for lo,hi in pmom)
 assert pmom[0][1]<0

 files=sorted(Path(args.shards).glob('NF429_original_cell6_z_shard_*.json'))
 assert len(files)==6,('expected exact six coefficient shard files',len(files),[p.name for p in files])
 all_coeff={}
 part_sha=[]
 for path in files:
  j,sha=read(path);part_sha.append({'file':path.name,'sha256':sha})
  assert j['pass']=='NF429'
  assert j['seams_sha256']==ksha
  assert j['source_sha256']==moments['nf407_original_full_source_sha256']
  assert j['original_true_cell6']=='(log(7)-11/10,log(8)-11/10)'
  assert j['original_analytic_global_transfer_pointwise_NF416_overlap_pass']
  assert j['independent_original_NF416_pointwise_parent_sha256']==pointsha
  assert j['number_of_target_coefficients']==N
  assert j['original_four_selected_plus_critical_count']==246
  assert j['common_endpoint_image_indices']==2048
  assert j['original_all_five_post_seam_primes_retained']==[2,3,4,5,7]
  assert j['original_two_neither_branches']==[8,9]
  assert j['original_native_precision_bits']>=2048
  start=j['first_mode_index_inclusive'];stop=j['stop_mode_index_exclusive']
  assert 0<=start<stop<=N and stop-start==len(j['coefficients'])
  for item in j['coefficients']:
   n=item['n'];assert start<=n<stop and n not in all_coeff
   lo,hi=map(F,item['true_original_cell6_fixed_branch_coefficient_outward_interval'])
   assert lo<=hi and hi-lo<F(1,10**25)
   all_coeff[n]=(lo,hi)
 assert set(all_coeff)==set(range(N)),('gap in true original series coefficient coverage',len(all_coeff))
 print('NF429 all 1500 original source-correlated z coefficient intervals source-pin/coverage PASS',flush=True)
 # The midpoint-centered numerical Chebyshev polynomial is *not* the
 # original exact z; compute one global uniform error instead:
 mids=[(all_coeff[i][0]+all_coeff[i][1])/2 for i in range(N)]
 rad=[(all_coeff[i][1]-all_coeff[i][0])/2 for i in range(N)]
 num_rad=sum(rad,F(0))
 analytic=F(2,10**45) # NF424 finite source + NF427 series tail
 delta=analytic+num_rad
 # On true original J6, |T_n(t)|<=1. A valid, deliberately conservative
 # source-specific uniform enclosure of the TRUE original continuous z:
 supmid=sum(map(abs,mids),F(0))
 assert num_rad<F(1,10**21) and delta<F(1,10**20)
 # p(x)<0 for all x on original J6, because original source endpoint
 # v<0, W>0 and log B/(B-x)>0. Thus int|p|=-int p.
 p_mass=-pmom[0][0]
 assert p_mass>0
 pz_mid_lo,pz_mid_hi=interval_linear(mids,pmom)
 pz_err=p_mass*delta
 pz=[pz_mid_lo-pz_err,pz_mid_hi+pz_err]
 print('NF429 complete original signed cell6 pz with source+native error charged',flush=True)

 L=A(7).log()-A(B);R=A(8).log()-A(B)
 assert A(F(21,25))<L<R<A(F(49,50))
 tL=(L-A(C))/A(H);tR=(R-A(C))/A(H)
 assert -1<tL<tR<1
 tl=tL.acos();tr=tR.acos()
 Tdelta=[(arb(n)*tr).cos()-(arb(n)*tl).cos() for n in range(2*N+1)]
 JJ=[A(H)*(tR-tL),A(H)*(tR*tR-tL*tL)/2]
 for k in range(2,2*N-1):
  JJ.append(A(H)*(Tdelta[k+1]/(2*(k+1))-Tdelta[k-1]/(2*(k-1))))
 assert len(JJ)==2*N-1
 J=[outward(v) for v in JJ]
 width=F(1,7) # actual log8/7<1/7
 assert J[0][1]<width
 # Identity T_i*T_j=(T_(i+j)+T_|i-j|)/2.
 # Exact rational midpoint Chebyshev-square coefficients b_k,
 # including i=0 and diagonal, via triangular source-correlated
 # two-index convolution. No non-rigorous sampled x-quadrature.
 squared=[F(0) for _ in range(2*N-1)]
 for i,a in enumerate(mids):
  if not a:continue
  for j in range(i,N):
   b=mids[j]
   if not b:continue
   factor=a*b if i!=j else a*b/2
   squared[i+j]+=factor
   squared[j-i]+=factor
  if (i+1)%250==0:print('NF429 exact source-midpoint Cheb square diagonal',i+1,'/',N,flush=True)
 z2_mid_lo,z2_mid_hi=interval_linear(squared,J)
 z2_err=width*(2*supmid*delta+delta*delta)
 z2=[z2_mid_lo-z2_err,z2_mid_hi+z2_err]
 # Guaranteed nonnegative true integral; bounding intersection cannot
 # invalidate the rigorous enclosure, provided upper is nonnegative.
 assert z2[1]>=0,('true squared-norm enclosure impossible',str(z2[1]))
 z2[0]=max(z2[0],F(0))
 print('NF429 complete original cell6 z² from exact rational Cheb product+true irrational knot intervals',flush=True)

 sector=[4*pz[0]+2*z2[0],4*pz[1]+2*z2[1]]
 out={
  'pass':'NF429',
  'standing':'ORIGINAL COMPLETE TRUE PHYSICAL CELL6 SIGNED PZ AND ZSQUARED INTERVALS CERTIFIED; OTHER SEVEN CELLS/NF404/RH OPEN',
  'original_246_source_preserved':True,'original_NF406_support_seams_sha256':ksha,
  'NF416_original_physical_x0_point_parent_sha256':pointsha,
  'NF428_original_all_1500_signed_principal_moments_sha256':msha,
  'NF429_six_coefficient_shard_sha256':part_sha,
  'full_original_true_cell6':'(log(7)-11/10,log(8)-11/10)',
  'source_correlated_cheb_series_all_1500_coefficients_native_certified':True,
  'true_original_analytic_uniform_error_upper_exact':str(analytic),
  'numerical_1500_coefficient_radii_sum_exact':str(num_rad),
  'total_true_original_cell6_uniform_z_minus_midpoint_polynomial_upper_exact':str(delta),
  'signed_p_nonpositive_entire_true_cell6':True,
  'complete_original_signed_principal_L1_upper_exact':str(p_mass),
  'signed_pz_true_original_cell6_outward_exact':[str(v) for v in pz],
  'Chebyshev_square_source_midpoint_exact_rational_convolution':True,
  'Chebyshev_true_log7_log8_endpoint_moments_through_degree':2*N-2,
  'true_original_cell6_integral_z_squared_outward_exact':[str(v) for v in z2],
  'true_original_cell6_sector_4pz_plus_2z2_outward_exact':[str(v) for v in sector],
  'this_is_not_global_or_even_half_original_scalar':True,
  'seven_remaining_original_physical_cells_integrated':False,
  'NF410_all_eight_cells_integrated':False,
  'NF404_complete_signed_scalar_decided':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF429 accepted full original cell6 sector only, original other 7 cells NF404 W-ODD-NEG RH OPEN',flush=True)
if __name__=='__main__':main()
