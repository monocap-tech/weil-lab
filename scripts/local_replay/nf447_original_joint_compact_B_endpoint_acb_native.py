#!/usr/bin/env python3
"""NF447 original TRUE compact support joint-response x=B native Arb pilot.

No original exterior U_ent, no finite image truncation, no unverified Gauss.
At x=B: J(B)= c0*v + (1/2)int_0^(4B) K(t)[v-U(B-t/2)]dt
                  + (v/2)[log(4/B)+pi/2+H(2B)],
H(d)=log(coth(d/4))+2atan(exp(-d/2)).
Actual original physical z(B) subtracts all n2,3,4,5,7,8,9 shifted
prime source+endpoint terms and exact NF404 dyadic centering.

Small collar [0,h] is NOT sampled: NF413 true ||U''||_2<256,
NF445 original |U'(B)|<1e-6 and h=1e-12 certify
|I_collar|<h/4(1e-6+256e-6)(1+h)<1.3e-16.
Source midpoint coefficient radius on the remaining interval is paid.
Only after acb.integral gives a finite outward enclosure and correct
independent checks do we call a point value SOURCE-CERTIFIED.
J7/J8 full signed moments remain OPEN.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
from nf415_original_cell6_I1_validated_acb import U
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAMS='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
NF445='51b8e0850c678085580940b3ab9afeff8277f446d4407c0200fb75754970db32'
NF446='3cfd2a71adf0c7fa0d9e314a8a0c7bf9cde732d60fad4c7a2346a286f0fb150a'
PRIMES=(2,3,4,5,7,8,9)
H=F(1,10**12)
CUTS=(H,F(1,1000),F(1,20),F(1),4*B)
def read(p):
 b=Path(p).read_bytes();return json.loads(b),hashlib.sha256(b).hexdigest()
def A(v):return arb(str(v))
def C(v):return acb(A(v))
def enclosure(z,digits=75):
 mid,rad,e=z.mid_rad_10exp(digits)
 v=F(10)**int(e)
 return F(int(mid)-int(rad))*v,F(int(mid)+int(rad))*v
def interp(a,b):return a[0]<=b[1] and b[0]<=a[1]
def save(p,data):
 path=Path(p);path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(data,indent=2)+'\n')
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 p.add_argument('--principal',default='notes/data/provisional/NF407_original_prime_jump_log_power_exact.json')
 p.add_argument('--nf413',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 p.add_argument('--nf445',required=True)
 p.add_argument('--nf446',default='notes/data/provisional/NF446_original_joint_compact_kernel_J7_J8_custody_index.json')
 p.add_argument('--precision',type=int,default=1024)
 p.add_argument('--eval-limit',type=int,default=5000)
 p.add_argument('--abs-tol',default='1e-16')
 p.add_argument('--output',required=True)
 args=p.parse_args()
 ctx.prec=args.precision
 src,sh=read(args.source);seams,ks=read(args.seams)
 principal,ps=read(args.principal);curv,cs=read(args.nf413)
 nf445,ns=read(args.nf445);nf446,fs=read(args.nf446)
 assert sh==SRC and ks==SEAMS and ns==NF445
 assert nf446['pass']=='NF446' and nf446['source_sha256']==SRC
 assert nf446['original_nf445_native_json_sha256']==ns
 assert nf446['original_entire_extension_outside_B_needed_in_FINAL_joint_integral'] is False
 assert nf446['original_B_endpoint_all_joint_integrands_removable']
 assert curv['original_nf407_full_native_source_sha256']==SRC
 assert curv['original_true_full_u4_second_derivative_L2_upper_integer']=='256'
 assert nf445['original_nf407_source_sha256']==SRC
 assert src['original_dimension']==242
 assert len(src['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert len(src['original_source_critical_sine_frequencies'])==32
 assert all(k['W_ODD_NEG']==k['RH']=='OPEN' for k in (src,seams,principal,curv,nf445))
 assert args.precision>=768 and args.eval_limit>=100
 assert F(args.abs_tol)>0
 original=U(src)
 source_rad=original.err
 assert 0<source_rad<F(1,10**700)
 v=original.at(C(B)).real
 vball=enclosure(v)
 native_v=tuple(map(F,nf445['original_source_v_analytic_carrier_interval']))
 assert interp(vball,native_v)
 dv=tuple(map(F,nf445['original_source_derivative_intervals_at_B']['1']))
 assert max(map(abs,dv))+10**12*source_rad<F(1,10**6)
 assert vball[1]<0 and vball[0]>-1
 original_source_charge=100*source_rad
 # True source NF413 and real endpoint derivative bound:
 # |U'(B-s)|<=|U'(B)|+256 sqrt(s), s in [0,h/2].
 # |U(B)-U(B-t/2)|/2<=t/4(1e-6+256 sqrt(h/2)).
 # sqrt(h/2)<1e-6, K(t)<1/t+1 for t>0.
 collar=H/F(4)*(F(1,10**6)+256*F(1,10**6))*(1+H)
 assert collar<F(13,10**17) # 1.3e-16
 # The original compact source v, U(B-t/2) remain inside [-B,B].
 # For t>=h, original source-rad contribution to the combined
 # integrand is <=S0*K(t), and ∫_h^(4B)K< log(4B/h)+4B<50.
 assert 4*B<5 and H<F(1,10**10)
 result={
   'pass':'NF447',
   'standing':'ORIGINAL TRUE +B SOURCE COMPACT INTEGRATION PROBE; POINT ACCEPTED ONLY IF FULL ACB ENCLOSURE RESOLVES; J7/J8 SIGN OPEN',
   'original_nf407_source_sha256':sh,'original_nf406_seams_sha256':ks,
   'original_nf407_principal_json_sha256':ps,
   'original_nf413_curvature_json_sha256':cs,
   'original_nf445_native_json_sha256':ns,
   'original_nf446_compact_custody_json_sha256':fs,
   'original_selected_plus_critical_source_count':246,
   'original_source_frequency_order_groups':len(original.terms),
   'original_true_original_source_physical_B':'11/10',
   'original_true_endpoint_x':'11/10',
   'original_endpoint_J8_closure':True,
   'original_native_precision_bits':args.precision,
   'original_small_t_collar_exact':str(H),
   'original_true_collar_uncomputed_absolute_charge_exact':str(collar),
   'original_source_radius_charge_exact':str(original_source_charge),
   'original_original_physical_regular_minus_primes':[2,3,4,5,7,8,9],
   'original_original_physical_plus_primes':[],
   'original_NF407_principal_jumps_at_B_minus':[2,3,4,5,7,8,9],
   'original_source_uB_arb_native_interval':list(map(str,vball)),
   'original_analytic_J_B_integral_formula':'1/2 int_0^(4B) K(t)*(U(B)-U(B-t/2))dt',
   'original_regularized_scalar_at_B':'u4(B)*(psi(1/4)-log(pi)+1/2*[log(4/B)+pi/2+H(2B)])',
   'original_K_analytic':'K(t)=exp(-t/4)/(1-exp(-t))',
   'original_complete_joint_true_source_integral_fully_resolved':False,
   'original_pointwise_J8_endpoint_z_source_certified':False,
   'original_true_J7_signed_D_certified':False,
   'original_true_J8_signed_D_certified':False,
   'original_full_NF410_NF404_signed_scalar_decided':False,
   'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 def kernel(t,analytic):
  # This is the actual source-correlated combined kernel, with no
  # exterior source and no split image, not a sampled Gauss mesh.
  tt=acb(t)
  k=(-tt/4).exp()/(1-(-tt).exp())
  return (k/2)*(C(v)-original.at(C(B)-tt/2))
 integral_lo=F(0);integral_hi=F(0)
 parts=[]
 for i,(low,high) in enumerate(zip(CUTS[:-1],CUTS[1:]),1):
  print('NF447 original +B compact Arb integral piece',i,'[',float(low),float(high),']',flush=True)
  rec={'part':i,'lower':str(low),'upper':str(high),'status':'UNDECIDED'}
  try:
   z=acb.integral(kernel,C(low),C(high),abs_tol=A(args.abs_tol),
       rel_tol=A('1e-20'),deg_limit=64,eval_limit=args.eval_limit,
       depth_limit=600)
   rec['native_acb_ball']=str(z)[:400]
   if z.is_finite() and z.imag.contains(0):
    lo,hi=enclosure(z.real)
    rec['interval']=[str(lo),str(hi)]
    rec['width']=str(hi-lo)
    if hi-lo<F(1,10**6):
     rec['status']='ACCEPTED_FULL_ANALYTIC_ACB_INTERVAL'
     integral_lo+=lo;integral_hi+=hi
    else:rec['status']='METHOD_STOP_FINITE_ACB_INTERVAL_TOO_WIDE'
   else:rec['status']='METHOD_STOP_NONFINITE_OR_IMAG_NOT_ZERO'
  except Exception as e:
   rec['status']='METHOD_STOP_ACB_NO_RESOLVED_INTEGRAL'
   rec['exception']=repr(e)[:240]
  parts.append(rec)
  print('NF447 original compact piece',i,rec['status'],rec.get('width',''),flush=True)
  if not rec['status'].startswith('ACCEPTED'):break
 result['original_acb_compact_joint_integral_pieces']=parts
 result['original_all_four_native_pieces_source_certified']=len(parts)==4 and all(t['status'].startswith('ACCEPTED') for t in parts)
 if result['original_all_four_native_pieces_source_certified']:
  # Add uncomputed collar and original 4096bit source radii.
  exact_lo=integral_lo-collar-original_source_charge
  exact_hi=integral_hi+collar+original_source_charge
  assert exact_lo<=exact_hi
  result['original_true_joint_kernel_integral_interval']=[str(exact_lo),str(exact_hi)]
  result['original_true_joint_kernel_integral_width']=str(exact_hi-exact_lo)
  pival=arb.pi()
  y=(-A(B)).exp()
  H2=((1+y)/(1-y)).log()+2*y.atan()
  c0=A(F(1,4)).digamma()-pival.log()
  scalar=v*(c0+((A(4)/A(B)).log()+pival/2+H2)/2)
  q0,q1=enclosure(scalar)
  xx=A(B);shift_sum=arb(0)
  log_seams={int(t['n']):t for t in seams['original_prime_power_log_shifts']}
  for n in PRIMES:
   assert n in log_seams
   weight=A(n).log()/A(n).sqrt() if n not in (4,8,9) else A({4:2,8:2,9:3}[n]).log()/A(n).sqrt()
   shift_sum+=weight*(original.at(C(B)-C(A(n).log())).real+v)
  # IMPORTANT: for prime powers n=4/8/9 use von Mangoldt Λ(n)=log prime,
  # not log n: n=8 Λ=log2, n=9 Λ=log3.
  center=F(6677356497477490213,4611686018427387904)
  zknown=scalar-shift_sum-A(center)*(xx/2).sinh()
  zl,zh=enclosure(zknown)
  # seven source translated evaluations + endpoint v each, 2S0
  zlo=exact_lo+zl-50*source_rad
  zhi=exact_hi+zh+50*source_rad
  result['original_true_J8_B_scalar_and_shift_interval']=[str(zl),str(zh)]
  result['original_true_B_arch_J_interval']=[str(exact_lo+q0),str(exact_hi+q1)]
  result['original_true_complete_J8_B_z_interval']=[str(zlo),str(zhi)]
  result['original_true_complete_J8_B_z_width']=str(zhi-zlo)
  if zhi-zlo<F(1,10**8):
   result['original_complete_joint_true_source_integral_fully_resolved']=True
   result['original_pointwise_J8_endpoint_z_source_certified']=True
   result['standing']='SOURCE-CERTIFIED TRUE ORIGINAL COMPACT JOINT J8 B-ENDPOINT Z INTERVAL; FULL D7 D8 SIGN OPEN'
  else:result['standing']='METHOD STOP JOINT COMPACT ENDPOINT FINITE INTERVAL TOO WIDE FOR SOURCE-CERTIFIED POINT'
 save(args.output,result)
 print('NF447 source-native endpoint status:',result['standing'],flush=True)
 print('NF447 true J7 J8 pz/z² integrals and RH OPEN',flush=True)
if __name__=='__main__':main()
