#!/usr/bin/env python3
"""NF431: original signed p=q+r Chebyshev moments, n=0..1499.

Native Arb 2048bit for true NF406 irrational endpoints J6, original
NF407 true signed endpoint/source and all five active source primes.
Exact Cheb-log expansion and exact Chebyshev antiderivative eliminate
numeric x quadrature. K=110 log modes, analytic coefficient tail paid.
Only linear signed p*P functional established. No z coefficients beyond
the separately certified original NF427 prefix; no signed pz or z² integral.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
from flint import arb,ctx
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);C=F(7,20);H=F(7,100)
PS=((3,3),(4,2))
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def A(x):return arb(str(x))
def encl(x,digits=75):
 m,r,e=x.mid_rad_10exp(digits);fac=F(10)**int(e)
 return [F(int(m)-int(r))*fac,F(int(m)+int(r))*fac]
def ov(a,b):return a[0]<=b[1] and b[0]<=a[1]
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 ap.add_argument('--principal',default='notes/data/provisional/NF407_original_prime_jump_log_power_exact.json')
 ap.add_argument('--nf410',default='notes/data/provisional/NF410_original_signed_taylor_moments.json')
 ap.add_argument('--nf430',default='scripts/local_replay/nf430_original_cells3_7_source_branch_transfer_exact.py')
 ap.add_argument('--precision',type=int,default=2048)
 ap.add_argument('--degree',type=int,default=1499)
 ap.add_argument('--log-modes',type=int,default=110)
 ap.add_argument('--output',required=True)
 args=ap.parse_args()
 assert args.precision>=1024 and args.degree==1499 and args.log_modes>=100
 ctx.prec=args.precision
 s,ssha=read(args.source);knots,ksha=read(args.seams)
 principal,psha=read(args.principal);old,oldsha=read(args.nf410)
 pin=hashlib.sha256(Path(args.nf430).read_bytes()).hexdigest()
 assert principal['original_nf406_seams_sha256']==ksha
 assert old['original_nf406_source_sha256']==ksha
 assert old['original_nf407_source_sha256']==psha
 assert s['original_dimension']==242
 assert len(s['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert len(s['original_source_critical_sine_frequencies'])==32
 assert s['W_ODD_NEG']==s['RH']=='OPEN'
 assert principal['W_ODD_NEG']==principal['RH']=='OPEN'
 assert old['W_ODD_NEG']==old['RH']=='OPEN'
 assert knots['certified_ordered_knots'][10]['label']=='-B+log(4)'
 assert knots['certified_ordered_knots'][11]['label']=='B-log(2)'
 assert old['original_positive_original_physical_cells'][2]['cell']==3
 assert (old['original_positive_original_physical_cells'][2]['left_label'],
         old['original_positive_original_physical_cells'][2]['right_label'])==('-B+log(4)','B-log(2)')
 L=A(4).log()-A(B)
 R=A(B)-A(2).log()
 assert A(F(7,25))<L<R<A(F(21,50))
 tL=(L-A(C))/A(H);tR=(R-A(C))/A(H)
 assert -1<tL<tR<1
 vpair=list(map(F,principal['original_source_u4_endpoint_interval']))
 assert vpair[0]<vpair[1]<0
 vmid=(vpair[0]+vpair[1])/2;vrad=(vpair[1]-vpair[0])/2
 v=A(vmid)
 weight=[]
 for n,base in PS:
  entry=next(q for q in principal['source_true_original_prime_jump_terms'] if q['n']==n)
  a=A(base).log()/A(n).sqrt()
  actual=encl(a)
  source_weight=list(map(F,entry['signed_mangoldt_weight_positive_interval']))
  assert ov(actual,source_weight),('original NF407 signed prime mismatch',n)
  weight.append(a)
 W=sum(weight,arb(0))
 assert A(F(1,2))<W<A(F(3,2))
 D=A(B-C);disc=(D*D-A(H)**2).sqrt()
 Q=(D+disc)/2;q=A(H)/(D+disc)
 assert A(0)<q<A(F(1,5))
 # Compute T_n at true irrational original endpoints via theta arccos,
 # not interval recurrence (which can create spurious radius blowup).
 K=args.log_modes;N=args.degree+K+2
 thetaL=tL.acos();thetaR=tR.acos()
 ds=[(arb(n)*thetaR).cos()-(arb(n)*thetaL).cos() for n in range(N+2)]
 J=[A(H)*(tR-tL),A(H)*(tR*tR-tL*tL)/2]
 for n in range(2,N+1):
  J.append(A(H)*(ds[n+1]/(2*(n+1))-ds[n-1]/(2*(n-1))))
 assert len(J)==N+1
 ell0=(A(B)/Q).log()
 ell=[ell0]
 for k in range(1,K+1):ell.append(2*q**k/k)
 # Entire log residual |L(x)-sum_(k=0)^K ell_k T_k| <
 # 2(1/5)^(K+1)/[(K+1)(1-1/5)] uniformly real [.84,.98].
 log_tail=F(2)*F(1,5)**(K+1)/(F(K+1)*(1-F(1,5)))
 # J6 length log(8/7)<1/7 and |T_n|<=1 on both true endpoints.
 log_moment_tail=log_tail/F(7)
 assert log_tail<F(1,10**70)
 assert log_moment_tail<F(1,10**70)
 # Principal source interval radius propagated independently, with
 # valid conservative |log(B/(B-x))|<20, |W|<4,
 # original physical cell width <1/7 => |moment|<3|v|.
 endpoint_charge=3*vrad
 assert endpoint_charge<F(1,10**40)
 n0_old=list(map(F,old['original_positive_original_physical_cells'][2]['signed_original_p_moments_by_degree_0_to_3'][0]))
 assert n0_old[0]<n0_old[1]
 vals=[]
 for n in range(args.degree+1):
  logmom=ell0*J[n]
  for k in range(1,K+1):
   logmom+=ell[k]*(J[n+k]+J[abs(n-k)])/2
  pvalue=v*(W*J[n]+logmom/2)
  lo,hi=encl(pvalue)
  charge=endpoint_charge+abs(vpair[1])*log_moment_tail/2
  lo-=charge;hi+=charge
  assert lo<=hi and hi-lo<F(1,10**25),(n,'interval moment too wide')
  if n==0:
   assert ov([lo,hi],n0_old),('NF410 genuine signed p zeroth-moment nonoverlap',str(lo),str(hi),str(n0_old))
  vals.append([str(lo),str(hi)])
  if (n+1)%300==0:print('NF431 original signed native Chebyshev moments',n+1,'/',args.degree+1,flush=True)
 out={'pass':'NF431','standing':'ORIGINAL TRUE CELL6 SIGNED CHEBYSHEV P MOMENTS n0..1499 SOURCE-CERTIFIED; ORIGINAL Z COEFFICIENT COMPLETION AND pz/z2 OPEN',
      'nf407_original_full_source_sha256':ssha,
      'nf406_original_seams_sha256':ksha,
      'nf407_principal_jump_source_sha256':psha,
      'nf410_original_signed_Taylor_moment_parent_sha256':oldsha,
      'nf430_exact_cell3_branch_script_sha256':pin,
      'original_full_source_generators_count':246,
      'original_signed_primes_on_cell3':[3,4],
      'original_both_shift_in_z_only':[2],
      'original_inactive_prime_branches':[5,7,8,9],
      'original_x_domain':'(log(4)-11/10,11/10-log(2))',
      'Chebyshev_center':'7/20','Chebyshev_halfwidth':'7/100',
      'degree':args.degree,'original_irrational_endpoints_arb_bits':args.precision,
      'log_Chebyshev_modes':K,'log_Chebyshev_uniform_tail_exact':str(log_tail),
      'each_signed_log_moment_tail_upper_exact':str(log_moment_tail),
      'original_uB_source_interval':list(map(str,vpair)),
      'original_source_uB_uncertainty_charge_per_moment_exact':str(endpoint_charge),
      'original_nf410_n0_signed_principal_moment_overlap':True,
      'all_1500_source_signed_chebyshev_moments_certified':True,
      'original_signed_p_chebyshev_moments_n0_to_n1499':vals,
      'original_all_1500_z_coefficients_available':False,
      'true_original_cell3_pz_integral_certified':False,
      'true_original_cell3_z2_integral_certified':False,
      'original_nf404_signed_scalar_decided':False,'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF431 all 1500 signed original cell3 Chebyshev p moments PASS and n0 independently overlaps NF410; z coefficients and scalar OPEN',flush=True)
if __name__=='__main__':main()
