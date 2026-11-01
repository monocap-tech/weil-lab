#!/usr/bin/env python3
"""NF439 exact original TRUE continuous physical cell4 signed integral.

Original NF434/435/436 512 source-native interval balls and NF436
exact rational true z-P511 uniform tail, SHA-pinned. Independent NF439
original true signed p and raw dx Cheb moments from exact NF406
log4-B/B-log2 seam. Source interval coefficient MIDPOINTS used for P511:
all midpoint selection error already in accepted uniform tail epsilon.
No sampled quadrature. Product-to-sum in exact Fraction, no sign assumed.
"""
from __future__ import annotations
import argparse,hashlib,json,sys,zipfile
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
PINS={
 "low":"ab98174c259d36df3b34f30486c3231f1d95bc90910938aab05c72d7ff4c9cc2",
 "mid":"289d8087a58d455ca20d6f5ce573bc5df612d38f648811b65f7f867fe3648de8",
 "high":"d561a19960b8d69c571a72a71b571de2479d5d615024f7fde3a275975e297cf8",
 "tail":"f8abd0ae4a8ec03d8ea14c4ace4e41210b039d9a72844989f9ba636076760ef9",
}
SOURCE_SHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM_SHA="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
N=512
def read(path,pin):
 p=Path(path);raw=p.read_bytes()
 if zipfile.is_zipfile(p):
  with zipfile.ZipFile(p) as z:
   names=[x for x in z.namelist() if x.endswith(".json")]
   assert len(names)==1
   raw=z.read(names[0])
 sha=hashlib.sha256(raw).hexdigest()
 assert sha==pin,(str(path),sha,pin)
 return json.loads(raw)
def ball(v):
 lo,hi=map(F,v);assert lo<=hi
 return lo,hi
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def scale(q,x):return (q*x[0],q*x[1]) if q>=0 else (q*x[1],q*x[0])
def widen(x,e):assert e>=0;return x[0]-e,x[1]+e
def main():
 ap=argparse.ArgumentParser()
 for key in ('low','mid','high','tail','moments'):
  ap.add_argument('--'+key,required=True)
 ap.add_argument('--moments-sha256',required=True)
 ap.add_argument('--output',required=True)
 a=ap.parse_args()
 d={key:read(getattr(a,key),PINS[key]) for key in PINS}
 d['moments']=read(a.moments,a.moments_sha256)
 low,mid,high,t,m=(d[k] for k in ('low','mid','high','tail','moments'))
 assert [low['pass'],mid['pass'],high['pass'],t['pass'],m['pass']]==['NF438','NF439','NF439','NF439','NF439']
 assert t['NF407_original_source_sha256']==m['original_nf407_source_sha256']==SOURCE_SHA
 assert t['NF406_original_seams_sha256']==m['original_nf406_seams_sha256']==SEAM_SHA
 for parent in (low,mid,high):
  assert parent['source_sha256']==SOURCE_SHA and parent['seams_sha256']==SEAM_SHA
  assert parent['original_true_cell4']==m['original_true_cell4']==t['original_true_cell4']=='(11/10-log(2),log(5)-11/10)'
  assert parent['original_minus_translate_primes']==m['original_active_minus_prime_powers']==[2,3,4]
  assert parent['original_plus_translate_primes']==m['original_active_plus_prime_powers']==[]
  assert parent['original_neither_prime_branches']==m['original_inactive_prime_powers']==[5,7,8,9]
  assert parent['original_exact_NF404_dyadic_center']==m['original_NF404_dyadic_center']
  assert parent['original_independent_direct_source_n2_n3_n4_minus_only_prime_overlap_pass']
  assert parent['original_independent_direct_source_endpoint_overlap_pass']
  assert parent['common_endpoint_image_indices']==2048
 assert m['original_principal_jump_weights_active']==[2,3,4]
 assert m['original_principal_jump_weights_inactive']==[5,7,8,9]
 assert m['original_principal_jump_weight_multiplicities']=={'2':1,'3':1,'4':1}
 assert m['original_regular_z_has_only_n2_minus_translate_and_p_has_n2_jump']
 assert m['original_nf410_independent_true_cell4_signed_p0_overlap']
 assert m['number_original_signed_p_moments']==N
 assert m['number_original_raw_dx_moments']==2*N-1
 assert t['original_Chebyshev_accepted_prefix_count_required']==N
 assert t['sourcewise_cheb_tail_starts_at_mode']==N
 assert t['required_each_native_coefficient_interval_width_strict_less_than']=='1e-44'
 assert not t['original_true_cell4_signed_pz_z2_integrated']
 assert all(z['W_ODD_NEG']==z['RH']=='OPEN' for z in d.values())
 coefficients=low['coefficients']+mid['coefficients']+high['coefficients']
 assert len(coefficients)==N
 assert [x['n'] for x in coefficients]==list(range(N))
 # Choose exact rational MIDPOINTS of genuinely accepted source balls,
 # not intervals again: the NF436 true-z uniform error already contains
 # 5e-45 midpoint choice for EACH coefficient. No double count.
 ca=[]
 for z in coefficients:
  lo,hi=ball(z['true_original_cell4_fixed_branch_coefficient_outward_interval'])
  assert hi-lo<F(1,10**44)
  ca.append((lo+hi)/2)
 supP=sum(map(abs,ca),F(0))
 pm=[ball(x) for x in m['original_source_signed_p_cheb_moments_n0_to_n511']]
 jm=[ball(x) for x in m['original_cell4_raw_dx_cheb_moments_n0_to_n1022']]
 assert pm[0][1]<0
 assert len(pm)==N and len(jm)==2*N-1
 pz=(F(0),F(0))
 for ci,pi in zip(ca,pm):pz=add(pz,scale(ci,pi))
 # Exact Cheb polynomial square coefficients, NOT a Gauss rule:
 # T_i*T_j = (T_{i+j}+T_|i-j|)/2; 2 on i<j.
 sq=[F(0)]*(2*N-1)
 for i in range(N):
  ci=ca[i]
  for j in range(i,N):
   cj=ca[j]
   v=ci*cj
   if i==j:
    sq[0]+=v/2
    sq[2*i]+=v/2
   else:
    sq[j-i]+=v
    sq[j+i]+=v
 assert len(sq)==2*N-1
 z2=(F(0),F(0))
 for bi,ji in zip(sq,jm):z2=add(z2,scale(bi,ji))
 length=jm[0]
 assert 0<length[0]<length[1]<F(1,8)
 eps=F(t['original_true_cell4_z_minus_any_accepted_P511_uniform_error_exact_upper'])
 assert 0<eps<F(1,10**38)
 # True z=P511+r, uniform |r|<eps. Since original p=v*(W+log/2)<0
 # on this TRUE cell, ∫|p|= -∫p = -pm[0].
 fee_pz=eps*(-pm[0][0])
 fee_z2=length[1]*(2*eps*supP+eps**2)
 fullpz=widen(pz,fee_pz)
 fullz2=widen(z2,fee_z2)
 signed=add(scale(F(4),fullpz),scale(F(2),fullz2))
 assert fullz2[1]>=0
 assert signed[0]<=signed[1]
 assert signed[1]-signed[0]<F(1,10**20),('original true cell4 sign enclosure unresolved',str(float(signed[1]-signed[0])))
 sign=('negative' if signed[1]<0 else 'positive' if signed[0]>0 else 'undecided')
 result={
  'pass':'NF439',
  'standing':'COMPLETE ORIGINAL TRUE CELL4 SIGNED pz/z² AND 4pz+2z² CONTINUOUS INTEGRAL SOURCE-CERTIFIED; NF410/NF404 AND RH OPEN',
  'original_nf407_source_sha256':SOURCE_SHA,
  'original_nf406_seams_sha256':SEAM_SHA,
  'original_source_parent_json_sha256':dict(PINS,moments=a.moments_sha256),
  'original_true_cell4':'(log(4)-11/10,11/10-log(2))',
  'original_active_minus_prime_powers':[2,3,4],
  'original_active_plus_prime_powers':[],
  'original_regular_response_n2_translate_multiplicity':1,
  'original_principal_p_n2_jump_multiplicity':1,
  'original_principal_p_jump_active':[2,3,4],
  'original_NF404_dyadic_center':m['original_NF404_dyadic_center'],
  'original_cell4_cheb_coefficient_balls':N,
  'original_exact_P511_midpoints_used':True,
  'original_complete_cell4_raw_dx_moments_used':2*N-1,
  'original_complete_cell4_signed_p_moments_used':N,
  'original_true_z_minus_original_midpoint_P511_uniform_error':str(eps),
  'original_cell4_P511_sup_bound_from_sum_absolute_coefficients':str(supP),
  'original_true_cell4_length_outward':list(map(str,length)),
  'original_true_cell4_signed_p0_outward':list(map(str,pm[0])),
  'original_P511_pz_outward_interval':list(map(str,pz)),
  'original_P511_squared_outward_interval':list(map(str,z2)),
  'original_complete_true_cell4_pz_tail_fee':str(fee_pz),
  'original_complete_true_cell4_z2_tail_fee':str(fee_z2),
  'original_true_cell4_pz_outward_interval':list(map(str,fullpz)),
  'original_true_cell4_z2_outward_interval':list(map(str,fullz2)),
  'original_true_cell4_signed_4pz_plus_2z2_outward_interval':list(map(str,signed)),
  'original_true_cell4_nonprincipal_signed_contribution_sign':sign,
  'original_true_cell4_signed_integral_decision_quality':True,
  'original_remaining_six_other_positive_cell_integrals_complete':False,
  'original_NF410_NF404_global_scalar_decided':False,
  'original_fourth_J242_exterior_upper_closed':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(result,indent=2)+'\n')
 print('NF439 ORIGINAL TRUE CELL4 COMPLETE CONTINUOUS SOURCE SIGNED pz,z2,4pz+2z2 accepted',sign,flush=True)
 print('pz',float(fullpz[0]),float(fullpz[1]),'z2',float(fullz2[0]),float(fullz2[1]),flush=True)
 print('SIGNED original J4',float(signed[0]),float(signed[1]),'total fee',float(4*fee_pz+2*fee_z2),flush=True)
 print('Original global NF410/NF404 W-ODD-NEG RH OPEN',flush=True)
if __name__=='__main__':main()
