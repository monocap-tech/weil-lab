#!/usr/bin/env python3
"""NF447 genuine original J8 B-endpoint source known part native (NOT signed).

The original NF446/NF447 exact joint derivative integral is still uncomputed;
its true abs <902 has source NF413/NF445 rigorous custody. This script
independently evaluates all other true original +B terms with 2048-bit
Arb and full 246-source coefficient/radius, seven genuine prime powers
with CORRECT von Mangoldt log(prime) and original exact NF404 center.
It gives a rigorous source-native broad enclosure for z(B) but cannot
decide sign of z(B), J7/J8 continuous integral, or RH.
"""
from __future__ import annotations
import argparse,json,hashlib,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
from nf415_original_cell6_I1_validated_acb import U
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
NATIVE='51b8e0850c678085580940b3ab9afeff8277f446d4407c0200fb75754970db32'
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def A(x):return x if isinstance(x,arb) else arb(str(x))
def C(x):return acb(A(x))
def bounds(v,digits=70):
 m,r,e=v.mid_rad_10exp(digits);q=F(10)**int(e)
 return F(int(m)-int(r))*q,F(int(m)+int(r))*q
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--nf445',required=True)
 ap.add_argument('--nf447-derivative',required=True)
 ap.add_argument('--precision',type=int,default=2048)
 ap.add_argument('--output',required=True)
 args=ap.parse_args()
 ctx.prec=args.precision
 src,sha=read(args.source);native,nh=read(args.nf445);deriv,dh=read(args.nf447_derivative)
 assert sha==SRC and nh==NATIVE and args.precision>=2048
 assert native['original_nf407_source_sha256']==sha
 assert deriv['pass']=='NF447' and deriv['original_source_sha256']==sha
 assert deriv['original_certified_integral_I_B_absolute_lt']==902
 assert deriv['original_source_original_acb_pilot_not_a_point_certificate']
 assert not deriv['original_true_signed_J8_certified']
 assert all(z['W_ODD_NEG']==z['RH']=='OPEN' for z in (src,native,deriv))
 u=U(src)
 assert len(u.terms)==273 and u.err<F(1,10**700)
 v=u.at(C(B)).real
 v0,v1=bounds(v)
 orig=tuple(map(F,native['original_source_u4_B_independent_native_interval']))
 assert v0<=orig[1] and orig[0]<=v1 and v1<0
 y=(-A(B)).exp()
 h2=((1+y)/(1-y)).log()+2*y.atan()
 scalar=v*(A(F(1,4)).digamma()-arb.pi().log()
   +((A(4)/A(B)).log()+arb.pi()/2+h2)/2)
 terms=[]
 weighted=arb(0)
 for n,prime in ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)):
  w=A(prime).log()/A(n).sqrt()
  point=A(B)-A(n).log()
  assert point>=-A(B) and point<=A(B)
  original_compact=u.at(C(point)).real
  weighted+=w*(original_compact+v)
  terms.append({'n':n,'original_von_mangoldt_prime':prime,
    'original_true_shifted_compact_u_interval':list(map(str,bounds(original_compact))),
    'original_endpoint_minus_log_n_abscissa_ball_str':str(point)[:150]})
 center=F(6677356497477490213,4611686018427387904)
 known=scalar-weighted-A(center)*(A(B)/2).sinh()
 lo,hi=bounds(known)
 # Original true each source coefficient radius on compact support
 # <S0. Seven shifted U and seven v plus scalar coefficient<14:
 # full total <28 S0, overcharge 50S0.
 charge=50*u.err
 integral_bound=F(902)
 full_lo=lo-integral_bound-charge
 full_hi=hi+integral_bound+charge
 assert full_lo<=full_hi
 assert hi-lo<F(1,10**25)
 out={'pass':'NF447','standing':'SOURCE-NATIVE ORIGINAL J8 B-ENDPOINT ALL NONINTEGRAL TERMS CERTIFIED; UNSIGNED TRUE z(B) ENCLOSURE WITH NF413 I_BOUND; DIRECT ACB INTEGRAL METHOD STOP',
  'original_nf407_source_sha256':sha,'original_nf445_full_native_json_sha256':nh,
  'original_nf447_true_derivative_certificate_sha256':dh,
  'original_original_source_246_selected_critical':246,
  'original_source_273_frequency_order':273,
  'original_arb_precision_bits':args.precision,
  'original_active_regular_minus_prime_powers':[2,3,4,5,7,8,9],
  'original_active_regular_plus_prime_powers':[],
  'original_shifted_source_von_mangoldt_weight_typed':True,
  'original_source_shift_terms':terms,
  'original_all_known_joint_arch_scalar_prime_and_center_interval':list(map(str,(lo,hi))),
  'original_source_uncertainty_charge_exact':str(charge),
  'original_unevaluated_compact_derivative_integral_abs_lt':902,
  'original_true_J8_B_z_conservative_interval':list(map(str,(full_lo,full_hi))),
  'original_true_J8_B_z_interval_width':str(full_hi-full_lo),
  'original_numerical_true_J8_B_integral_value_resolved':False,
  'original_true_J8_signed_continuous_integral_decided':False,
  'original_true_J7_signed_continuous_integral_decided':False,
  'original_global_NF410_NF404_scalar_decided':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(out,indent=2)+'\n')
 print('NF447 original true compact B known term certified',float(known.mid()),'interval',float(lo),float(hi),flush=True)
 print('NF447 genuine full true z(B) interval with exact absolute I_B<902:',float(full_lo),float(full_hi),flush=True)
 print('NF447 J7 J8 signed and RH remain OPEN',flush=True)
if __name__=='__main__':main()
