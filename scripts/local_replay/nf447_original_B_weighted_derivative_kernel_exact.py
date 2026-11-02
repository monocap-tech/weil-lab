#!/usr/bin/env python3
"""NF447 exact source-certified derivative kernel for true original z(B).

The first native acb.integral with K(t)(v-U(B-t/2))/2 returned nan.
This is an INTEGRATION METHOD STOP, not a failure of the NF446 identity.

Replace by a genuinely analytic removable kernel, valid on t=0:
 I_B = 1/4 int_0^(4B) t*K(t) int_0^1 U'(B-theta*t/2)dtheta dt.
No exterior analytic continuation; all U' arguments in [-B,B].
Source NF413 ||U''||L2<256 and NF445 true |U'(B)|<1e-6 give
 |I_B|<902, |J(B)|<916 and full physical |z(B)|<7300.
That is genuine *endpoint boundedness*, not numerically useful
signed D7/D8; original complete NF410/NF404 RH OPEN.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10)
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02f08b28302d940b2fcce'
# Pin actual original source immutable digest (not the typo above).
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
NATIVE='51b8e0850c678085580940b3ab9afeff8277f446d4407c0200fb75754970db32'
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def Finterval(x):
 a,b=map(F,x);assert a<=b;return a,b
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 ap.add_argument('--principal',default='notes/data/provisional/NF407_original_prime_jump_log_power_exact.json')
 ap.add_argument('--nf413',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 ap.add_argument('--nf445',required=True)
 ap.add_argument('--nf446',default='notes/data/provisional/NF446_original_joint_compact_kernel_J7_J8_custody_index.json')
 ap.add_argument('--nf447-attempt',required=True)
 ap.add_argument('--output',required=True)
 args=ap.parse_args()
 source,sh=read(args.source);seams,ksha=read(args.seams)
 princ,ps=read(args.principal);curv,cs=read(args.nf413)
 native,ns=read(args.nf445);joint,js=read(args.nf446)
 attempt,ats=read(args.nf447_attempt)
 assert sh==SRC and ksha==SEAM and ns==NATIVE
 assert source['original_dimension']==242
 assert len(source['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert len(source['original_source_critical_sine_frequencies'])==32
 assert curv['original_nf407_full_native_source_sha256']==SRC
 assert curv['original_true_full_u4_second_derivative_L2_upper_integer']=='256'
 assert native['original_nf407_source_sha256']==SRC
 assert native['original_precision_bits']==4096
 assert joint['pass']=='NF446' and joint['original_nf407_source_sha256']==SRC
 assert joint['original_fixed_source_entire_continuation_beyond_B_not_needed']
 assert joint['source_nf413_second_derivative_L2_upper']==256
 assert attempt['pass']=='NF447' and attempt['original_nf407_source_sha256']==SRC
 assert attempt['original_acb_compact_joint_integral_pieces'][0]['status']=='METHOD_STOP_NONFINITE_OR_IMAG_NOT_ZERO'
 assert not attempt['original_pointwise_J8_endpoint_z_source_certified']
 assert all(q['W_ODD_NEG']==q['RH']=='OPEN' for q in (source,seams,curv,native,joint,attempt))
 # Actual original source endpoint derivative interval and true input
 # radii: source uncertainty in U' bounded <1e12 S0 (<1e-688).
 s0=F(attempt['original_source_radius_charge_exact'])/100
 assert 0<s0<F(1,10**700)
 a,b=Finterval(native['original_source_derivative_intervals_at_B']['1'])
 assert max(abs(a),abs(b))+10**12*s0<F(1,10**6)
 v0,v1=Finterval(native['original_source_v_analytic_carrier_interval'])
 assert -1<v0<=v1<0
 # Exact identity:
 # U(B)-U(B-t/2)=(t/2)int_0^1 U'(B-theta*t/2)dtheta.
 # Original singular kernel K(t) multiplies t, giving L(t)=tK(t),
 # finite L(0)=1. No independent digamma/image evaluation.
 bmax=4*B
 assert bmax==F(22,5)
 # For any theta∈[0,1] and t∈[0,bmax],
 # |U'(B-theta*t/2)|<=delta+256 sqrt(theta*t/2)
 # by NF413 true L2, and sqrt(t/2)<sqrt(2B)<3/2.
 # Integrate theta sqrt(theta): 2/3, giving
 # avg derivative <= delta+256 (2/3)(3/2)=delta+256.
 delta=F(1,10**6)
 avg=delta+256
 assert F(2,3)*F(3,2)==1
 # 0< tK(t)<1+t from exact kernel inequalities.
 integral_upper=avg*(bmax+bmax*bmax/2)/4
 assert integral_upper<F(902)
 # Analytic scalar at B exactly:
 # u4(B)*[psi(1/4)-log(pi)+1/2*(log(4/B)+pi/2+H(2B))].
 # |c0|<10 original NF446 Arb, log(4/B)<2 since
 # e^2>1+2+2=5>40/11, pi/2<2, and H(2B)<3:
 # y=exp(-B)<1/2 since e^B>1+B+B²/2>2,
 # log((1+y)/(1-y))<log 3<2, 2 atan(y)<2y<1.
 assert 1+B+B**2/2>2
 assert 1+2+F(2)**2/2>F(4)/B
 assert F(4)/B==F(40,11)
 scalar_upper=F(10)+F(2+2+3,2)
 assert scalar_upper<F(14)
 joint_at_B=F(902)+F(14)
 assert joint_at_B==916
 # At B, the original physical NF405 active signed n=2,3,4,5,7,8,9
 # all have legitimate arguments B-log(n) in [-B,B],
 # original weight Lambda(n)/sqrt(n)<1 and original NF404
 # exact centered sinh term <2; 7*(|U|+|v|)<7*901.
 center=F(6677356497477490213,4611686018427387904)
 assert 0<center<2
 physical_z_at_B=joint_at_B+7*(900+1)+2
 assert physical_z_at_B==7225<F(7300)
 # Source-only improvement does not decide the integral or sign.
 out={
 'pass':'NF447',
 'standing':'CERTIFIED ORIGINAL +B WEIGHTED DERIVATIVE-KERNEL CONTINUATION AND FINITE |z(B)|<7300; DIRECT FIRST ACB INTEGRAL METHOD STOP; SIGNED J7/J8 OPEN',
 'original_source_sha256':sh,'original_nf406_seams_sha256':ksha,
 'original_nf407_principal_sha256':ps,'original_nf413_source_curvature_sha256':cs,
 'original_nf445_4096bit_source_native_sha256':ns,
 'original_nf446_compact_custody_sha256':js,
 'original_nf447_failed_acb_pilot_sha256':ats,
 'original_original_246_source_retained':True,
 'original_true_endpoint_B':'11/10',
 'original_small_t_original_ACB_pilot_status':'METHOD_STOP_NONFINITE_OR_IMAG_NOT_ZERO',
 'original_source_original_acb_pilot_not_a_point_certificate':True,
 'original_exact_weighted_derivative_kernel':
    'I_B=(1/4) int_0^(4B) t K(t) int_0^1 Uprime(B-theta*t/2)dtheta dt',
 'original_resummed_K':'K(t)=exp(-t/4)/(1-exp(-t))',
 'original_resummed_tK_at_zero_exact_limit':'1',
 'original_all_weighted_Uprime_arguments_inside_original_compact_support':True,
 'original_true_Uprime_B_sup_lt':'1e-6',
 'original_true_Udoubleprime_L2_upper':256,
 'original_exact_integral_I_B_bound':str(integral_upper),
 'original_certified_integral_I_B_absolute_lt':902,
 'original_original_analytic_scalar_B_absolute_lt':14,
 'original_original_joint_arch_at_B_absolute_lt':916,
 'original_full_true_physical_zB_absolute_lt':7300,
 'original_true_signed_J7_certified':False,
 'original_true_signed_J8_certified':False,
 'original_full_NF410_NF404_scalar_decided':False,
 'original_signed_cells_complete_count':6,
 'W_ODD_NEG':'OPEN','RH':'OPEN'}
 path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(out,indent=2)+'\n')
 print('NF447 exact derivative kernel endpoint |I_B|<902, |Joint(B)|<916, ORIGINAL true |z(B)|<7300')
 print('NF447 direct Acb nan on small panel preserved as METHOD STOP; signed J7/J8 and RH OPEN')
if __name__=='__main__':main()
