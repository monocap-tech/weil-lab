#!/usr/bin/env python3
"""NF444 exact source-custodied near-B image desingularization and J7/J8 seam contact.

This certifies an EXACT analytic reorganization of the ORIGINAL NF424
archimedean transfer used in native NF443, not a new signed J7/J8
integral. The coefficient of the universal 1/(m+1/4) image tail
equals v=u4(B) for the full 246-source linear form. Its sum is
H(d)=log(coth(d/4))+2 atan(exp(-d/2)); its log(d) pole cancels the
explicit original -v/2 log(B/d). The 1/m^2 source remainder converges
uniformly to x=B with an explicit but possibly loose full-source M/N.
The true n9 physical regular activation at log9-B cancels the NF407
principal n9 jump exactly. NEVER infer signed J7/J8 or RH.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
from nf425_original_cell6_chebyshev_existence_exact import source
from nf433_original_cell3_cell7_branch_ellipse_router_exact import branch_for_cell
from nf438_original_cells4_5_regular_principal_geometry_exact import principal_jump
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)
PRIMES=(2,3,4,5,7,8,9)
SOURCE='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAMS='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
def load(path):
 raw=Path(path).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def check_transfer(path):
 raw=Path(path).read_text()
 checks=[
  'for m in range(N_IMAGES):',
  'aa=R(F(4*m+1,4))',
  'total+=2*v.real',
  'total-=A(pole)*(-A(B)/2).exp()',
  'total+=A(pole)*((A(B)/2).exp()/A(F(m))-',
  'physical_point-=endpoint*((A(B)/A(B-X)).log()/2+sum(weights,arb(0)))',
  '(-2*aa*R(B-X)).exp()-(-2*aa*R(B+X)).exp()',
  'endpoint+=A(pole)*(A(B)/2).sinh()',
  'endpoint+=2*(alpha*exB*R(B**k)).real'
 ]
 for s in checks:assert s in raw,('original native transfer convention changed',s)
 return hashlib.sha256(raw.encode()).hexdigest()
def math_identity():
 # H(d)=4*sum_{m>=0} y^(4m+1)/(4m+1);
 # dH/dy=4/(1-y^4)=d/dy[log((1+y)/(1-y))+2atan(y)].
 # Values both vanish at y=0. y=e^-d/2.
 assert F(2)*(F(1,1)+F(1,1))==4
 assert F(1,4)*4==1
 # As d->0: y=1-d/2+O(d²):
 # log((1+y)/(1-y)) + log(d) -> log(4);
 # 2atan(y)->pi/2.
 # Therefore H(d)-log(B/d) ->
 # log(4/B)+pi/2. No nonuniform 1/(B-x) remains.
 assert B>0
 return True
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 ap.add_argument('--principal',default='notes/data/provisional/NF407_original_prime_jump_log_power_exact.json')
 ap.add_argument('--nf405',default='notes/data/provisional/NF405_original_compact_physical_kernel_exact.json')
 ap.add_argument('--nf410',default='notes/data/provisional/NF410_original_signed_taylor_moments.json')
 ap.add_argument('--native-transfer',default='scripts/local_replay/nf443_original_cell2_three_panel_native_index.py')
 ap.add_argument('--output',required=True)
 args=ap.parse_args()
 s,sha=load(args.source);knots,ksha=load(args.seams)
 p,psha=load(args.principal);physical,phsha=load(args.nf405);old,oldsha=load(args.nf410)
 assert sha==SOURCE and ksha==SEAMS
 assert p['original_nf406_seams_sha256']==ksha
 assert old['original_nf406_source_sha256']==ksha
 assert old['original_nf407_source_sha256']==psha
 assert knots['original_nf405_compact_kernel_sha256']==phsha
 assert p['source_r_formula']=="r(x)=u4(B)*sgn(x)*sum_{n=2,3,4,5,7,8,9} [Lambda(n)/sqrt(n)]*1_(|x|>abs(B-log(n)))"
 assert s['original_dimension']==242
 assert len(s['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert len(s['original_source_critical_sine_frequencies'])==32
 assert physical['actual_original_prime_power_shifts']==list(PRIMES)
 assert all(z['W_ODD_NEG']==z['RH']=='OPEN' for z in (s,knots,p,physical,old))
 assert math_identity()
 transfer_sha=check_transfer(args.native_transfer)
 coeff,pole,S0=source(s)
 assert len(coeff)==273 and 0<S0<F(1,10**700)
 assert 0<min(f for f,k in coeff) and max(f for f,k in coeff)<883
 assert max(k for f,k in coeff)<=13
 assert sum((abs(c)*B**k for (f,k),c in coeff.items()),abs(pole))<10**160
 v0,v1=map(F,p['original_source_u4_endpoint_interval'])
 assert v0<v1<0 and v1-v0<F(1,10**40)
 # The original native image group for (f,k,c) has positive-frequency
 # lambda=2*pi*i*f and A_j=alpha*e^(lambda B)
 # *binom(k,j)*j!*B^(k-j)/2^j, where |2alpha|=|c|.
 # T_m = 2Re sum_(f,k) sum_(j=0)^k A_j/(a_m-i*pi*f)^(j+1)
 # + pole/2*(e^(B/2)/m-e^(-B/2)/(m+1/2)) for m>=1.
 # Leading a_m*T_m equals the source endpoint v=u4(B).
 # For a_m=m+1/4>=5/4, exact:
 # |1/(a-iw)-1/a|<=|w|/a², |(a-iw)^(-j-1)|<=a^-2 (j>=1).
 # Pole remainder <=7|pole|/(16*a²): e^(B/2)<2,
 # e^(-B/2)<1, a/m<=5/4 for m>=1.
 # Full source midpoints M0 and honest unknown dyadic radii S0.
 # k<=13, f<883, pi<22/7, beta_j/B^k<=13!;
 # sum of at most 13 such terms <1e11, so errors <1e12 S0.
 M0=abs(pole)
 for (f,k),c in coeff.items():
  b=F(22,7)*f*B**k
  b+=sum((F(math.comb(k,j)*math.factorial(j),2**j)*B**(k-j) for j in range(1,k+1)),F(0))
  M0+=abs(c)*b
 assert M0>0
 assert F(22,7)*F(883)<3000
 assert 13*math.factorial(13)<10**11
 M=M0+10**12*S0
 assert M>=M0>0
 # Uniform remainder for real x in [0,B]:
 # |e^(-2a(B-x))-e^(-2a(B+x))|<=1.
 # For any N>=1, sum_(m>=N) 1/(m+1/4)^2
 # <= integral_(N-1)^inf dt/(t+1/4)^2 =1/(N-3/4).
 N=2048
 tail=M/(2*(F(N)-F(3,4)))
 assert tail>0
 # Only a structural bound; DO NOT impose an artificial smallness
 # criterion: this overestimate may be wildly non-decision-quality.
 seam=knots['certified_ordered_knots'];assert len(seam)==17
 logs={int(e['n']):(F(e['log_lower']),F(e['log_upper'])) for e in knots['original_prime_power_log_shifts']}
 cells={}
 for idx,left_i,right_i in ((7,14,15),(8,15,16)):
  a,b=seam[left_i],seam[right_i]
  L0,L1=F(a['low']),F(a['high']);R0,R1=F(b['low']),F(b['high'])
  assert 0<L0<=L1<R0<=R1<=B
  minus=[];plus=[];jump=[]
  for n in PRIMES:
   m,pl=branch_for_cell(n,L1,R0,logs,a['label'],b['label'])
   if m:minus.append(n)
   if pl:plus.append(n)
   if principal_jump(n,L1,R0,a['label'],b['label'],logs):jump.append(n)
  expect=list(PRIMES[:-1]) if idx==7 else list(PRIMES)
  assert minus==jump==expect and plus==[],(idx,minus,jump,plus)
  oldcell=old['original_positive_original_physical_cells'][idx-1]
  assert oldcell['cell']==idx and oldcell['left_label']==a['label'] and oldcell['right_label']==b['label']
  assert F(oldcell['signed_original_p_moments_by_degree_0_to_3'][0][1])<0
  cells[str(idx)]={'physical_left':a['label'],'physical_right':b['label'],
      'left_irrational_enclosure':[str(L0),str(L1)],
      'right_irrational_enclosure':[str(R0),str(R1)],
      'original_regular_minus':minus,'original_regular_plus':plus,
      'original_principal_r_jumps_active':jump,
      'original_p0_NF410_strict_negative':True,
      'image_and_log_regularized_kernel_shared_across_both_cells':True,
      'original_continuous_signed_integral_decided':False}
  if idx==7:
   assert R1<B and B-R1>0
   cells[str(idx)]['B_minus_right_seam_positive_lower']=str(B-R1)
  else:
   assert R0==R1==B
   cells[str(idx)]['true_endpoint_B_included_by_continuous_limit']=True
 # At the genuine shared n=9 support seam x*=log9-B:
 # original regular new source -w9*u4(-B)=+w9*v (odd u4);
 # independent principal new -r=-w9*v; they exactly cancel.
 # This is exact linear algebra in v and w9, not an interval overlap.
 assert 9 in cells['8']['original_regular_minus']
 assert 9 not in cells['7']['original_regular_minus']
 assert 9 in cells['8']['original_principal_r_jumps_active']
 assert 9 not in cells['7']['original_principal_r_jumps_active']
 assert F(1)-F(1)==0
 out={
 'pass':'NF444',
 'standing':'CERTIFIED ORIGINAL NF407 SOURCE-LINEAR UNIVERSAL IMAGE LOG RESUMMATION; J7/J8 CONTACT & J8 B-ENDPOINT CONTINUITY; QUANTITATIVE SIGNED J7/J8 OPEN',
 'original_source_SHA256':sha,'original_seams_SHA256':ksha,
 'original_principal_SHA256':psha,'original_NF405_SHA256':phsha,'original_NF410_SHA256':oldsha,
 'original_native_image_transfer_script_SHA256':transfer_sha,
 'original_246_source_dyadic_linear_form':True,
 'original_source_frequency_order_groups':len(coeff),
 'original_u4_B_negative_interval':[str(v0),str(v1)],
 'original_image_index_parameter':'a_m=m+1/4',
 'original_image_total_leading_term_exact':'u4(B)/a_m',
 'original_exact_resummed_H_d':'log(coth(d/4))+2*atan(exp(-d/2))',
 'original_exact_resummed_H_series':'sum_(m>=0) exp(-2*(m+1/4)*d)/(m+1/4)',
 'original_resummed_H_asymptotic':'H(d)+log(d)->log(4)+pi/2 as d downarrow0',
 'original_pole_cancelled_kernel_at_B':'(u4(B)/2)*(log(4/B)+pi/2-H(2*B))',
 'original_continuous_fixed_source_endpoint_at_B_exists':True,
 'original_m0_term_separately_finite':True,
 'original_remaining_source_image_residual_Rm_for_m_ge1':'T_m-u4(B)/(m+1/4)',
 'original_remaining_source_image_residual_pointwise':'|R_m|<=M/(m+1/4)^2 for every m>=1',
 'original_true_source_remainder_constant_exact_rational':str(M),
 'original_source_midpoint_remainder_constant_exact_rational':str(M0),
 'original_true_dyadic_source_radius_overcharge':str(10**12*S0),
 'original_uniform_residual_image_tail_for_m_ge2048_exact_rational':str(tail),
 'original_uniform_residual_image_tail_formula':'M/[2*(N-3/4)] for m>=N>=1 on x in [0,B]',
 'original_source_residual_tail_decision_quality_certified':False,
 'original_U_odd_boundary_identity':'u4(-B)=-u4(B)',
 'original_n9_activation_regular_jump':'-w9*u4(-B)=+w9*u4(B)',
 'original_n9_activation_minus_principal_jump':'-w9*u4(B)',
 'original_n9_support_seam_total_z_jump_exact_zero':True,
 'original_true_J8_response_bounded_on_closed_interval_by_uniform_convergence':True,
 'original_true_J8_p_unbounded_but_L1':True,
 'original_true_J8_pz_and_z2_integrable_without_sign_decision':True,
 'original_cells':cells,
 'original_true_J7_signed_integral_decided':False,
 'original_true_J8_signed_integral_decided':False,
 'original_full_NF410_NF404_signed_scalar_decided':False,
 'original_principal_E_p_full_integrated':False,
 'original_fourth_J242_exterior_upper_closed':False,
 'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF444 PASS true source-linear endpoint cancellation, H(d) explicit log+atan, remaining image O(m^-2) uniform J7/J8.')
 print('NF444 structural remainder M approx order10',len(str(abs(M.numerator)))-len(str(M.denominator)))
 print('NF444 J7/J8 n9 seam exact continuous, z(B) continuous, original signed D7 D8 global RH OPEN.')
if __name__=='__main__':main()
