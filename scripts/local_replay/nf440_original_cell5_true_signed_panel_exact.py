#!/usr/bin/env python3
"""NF440 original TRUE J5 three unchanged-source physical panel signed integral.

Original source-certified 512 modes per panel, 2048 common images, exact
sourcewise real response tail, 512 native p and 1023 raw dx moments;
all parents SHA256 pinned. Exact Fraction Chebyshev product-to-sum.
No false r jump at rational integration cuts 31/50 or 73/100.
Full-cell principal NF410 p0 control follows in separate final 3-panel job.
RH and global NF410/NF404 unchanged OPEN.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SOURCE="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAMS="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
PINS={
 1:{"low":"ac3d579ea10fe25009eafeddc174d0d88c78ff20f4ed447a9b41e4adc5c6e59e",
    "high":"f6cd1f6d777bd9227bd1763bf98762b7867e7aa7686c38c26951461e906c7274",
    "control":"f50809db74f325f305a975b2cdb6a5770c2c2276356556eb89cac8934f647e95",
    "tail":"7620671f67532897b8426f04afeec99c823e3e01fb971fc080693a0e1e7254e3",
    "moments":"33f17b7c777206fa021663ff0dfa031620c75a3a8ae2a97bab1c9b10a6e57df7"},
 2:{"low":"0655c8900521b31f17ccf0ab8c3b98bf950ab0a8bb6f2a0872dec88ac07f286b",
    "high":"b6194bd6af39ff7095f6a2220334383ea74967119c05acf08c73044c2ddf1378",
    "control":"0dc99e2f469d3e07a836405ae82c076b64e808fa566363ad12f8dfdcd3255cbd",
    "tail":"bb11b50a7ad20442e08e47786933f626baae34e3f523aca09810ad669abbaa6a",
    "moments":"3bd968b4e8cc95f5948a139650ab56dfc56fca9dd4d241bd17bdc3d7a1a09a84"},
 3:{"low":"c2ea899bf3a958b4e039efcad6cad68ada942b76c11dd11d2f904c444195c413",
    "high":"e27b1021b2d279e3d611997eca81dbb2280bf2329a0483b7dc1be16284668263",
    "control":"797b8edd5911a86fdc2b043c4bb417caf160119dbb76c233189ed2a158ce6220",
    "tail":"69384c2c0bcaaa82058c3db1c6cb34d742748366fc34306bc7ca14a35de6e969",
    "moments":"16e6ac10c0174ceb04e16c4bda51f829ff662fd65ea8c3d94a61012872b8ef3a"}}
def read(path,sha):
 b=Path(path).read_bytes()
 digest=hashlib.sha256(b).hexdigest()
 assert digest==sha,(str(path),digest,sha)
 return json.loads(b)
def ball(v):
 a,b=map(F,v);assert a<=b;return a,b
def add(x,y):return x[0]+y[0],x[1]+y[1]
def scale(c,x):return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def widen(x,e):assert e>=0;return x[0]-e,x[1]+e
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--panel',type=int,choices=(1,2,3),required=True)
 for tag in ('low','high','control','tail','moments'):
  ap.add_argument('--'+tag,required=True)
 ap.add_argument('--output',required=True)
 args=ap.parse_args();panel=args.panel
 d={key:read(getattr(args,key),sha) for key,sha in PINS[panel].items()}
 lo,hi,ctrl,tail,mom=(d[key] for key in ('low','high','control','tail','moments'))
 assert all(x['pass']=='NF440' for x in d.values())
 assert all(x['source_sha256']==SOURCE and x['seams_sha256']==SEAMS for x in (lo,hi,ctrl))
 assert tail['NF407_original_source_sha256']==mom['original_nf407_source_sha256']==SOURCE
 assert tail['NF406_original_seams_sha256']==mom['original_nf406_seams_sha256']==SEAMS
 assert all(x['original_panel_number']==panel for x in d.values())
 assert all(x['original_true_cell5']=='(log(5)-11/10,log(7)-11/10)' for x in d.values())
 assert lo['original_panel_true_piece_exact_bounds']==hi['original_panel_true_piece_exact_bounds']==ctrl['original_panel_true_piece_exact_bounds']==tail['original_panel_true_piece_exact_bounds']
 assert lo['original_minus_translate_primes']==hi['original_minus_translate_primes']==ctrl['original_minus_translate_primes']==[2,3,4,5]
 assert lo['original_plus_translate_primes']==hi['original_plus_translate_primes']==ctrl['original_plus_translate_primes']==[]
 assert lo['original_neither_prime_branches']==hi['original_neither_prime_branches']==[7,8,9]
 assert all(x['original_independent_direct_source_n2_n3_n4_n5_minus_only_prime_overlap_pass'] for x in (lo,hi,ctrl))
 assert all(x['original_independent_direct_source_endpoint_overlap_pass'] for x in (lo,hi,ctrl))
 assert all(x['common_endpoint_image_indices']==2048 for x in (lo,hi,ctrl))
 assert lo['original_exact_NF404_dyadic_center']==hi['original_exact_NF404_dyadic_center']==mom['original_NF404_dyadic_center']
 assert lo['analytic_Chebyshev_center']==hi['analytic_Chebyshev_center']==tail['original_Chebyshev_center']==mom['original_panel_center']
 assert lo['analytic_Chebyshev_halfwidth']==hi['analytic_Chebyshev_halfwidth']==tail['original_Chebyshev_halfwidth']==mom['original_panel_halfwidth']
 assert lo['original_rational_panel_cuts_are_not_prime_seams'] and hi['original_rational_panel_cuts_are_not_prime_seams']
 assert mom['original_active_minus_prime_powers']==mom['original_principal_jump_weights_active']==tail['original_minus_translate_active']==[2,3,4,5]
 assert mom['original_active_plus_prime_powers']==tail['original_plus_translate_active']==[]
 assert mom['original_principal_jump_weights_inactive']==[7,8,9]
 assert mom['original_regular_z_four_minus_and_principal_four_jump_terms_on_all_panels']
 assert mom['original_nf410_full_true_cell5_p0_overlap_requires_all_three_panels']
 assert mom['original_internal_rational_cuts_not_original_seams']==['31/50','73/100']
 assert tail['original_rational_integration_cuts_not_prime_seams']==['31/50','73/100']
 assert tail['sourcewise_cheb_tail_starts_at_mode']==tail['original_Chebyshev_accepted_prefix_count_required']==512
 assert tail['required_each_native_coefficient_interval_width_strict_less_than']=='1e-44'
 assert F(tail['original_all_512_native_coefficient_interval_charge'])==512*F(5,10**45)
 assert (lo['mode_start_inclusive'],lo['mode_stop_exclusive'])==(0,256)
 assert (hi['mode_start_inclusive'],hi['mode_stop_exclusive'])==(256,512)
 assert (ctrl['mode_start_inclusive'],ctrl['mode_stop_exclusive'])==(0,8)
 coeff=lo['coefficients']+hi['coefficients']
 assert len(coeff)==512 and [x['n'] for x in coeff]==list(range(512))
 assert len(ctrl['coefficients'])==8
 key='true_original_cell5_fixed_branch_coefficient_outward_interval'
 midpoint=[];maxwidth=F(0)
 for j,x in enumerate(coeff):
  a,b=ball(x[key]);assert b-a<F(1,10**44)
  maxwidth=max(maxwidth,b-a);midpoint.append((a+b)/2)
  if j<8:
   u,v=ball(ctrl['coefficients'][j][key])
   assert a<=v and u<=b,('independent low-index padding overlap',panel,j)
 supP=sum(map(abs,midpoint),F(0))
 p=[ball(v) for v in mom['original_source_signed_p_cheb_moments_n0_to_n511']]
 dx=[ball(v) for v in mom['original_cell5_raw_dx_cheb_moments_n0_to_n1022']]
 assert len(p)==512 and len(dx)==1023
 assert p[0][1]<0 and F(0)<dx[0][0]<dx[0][1]<F(1,8)
 poly_pz=F(0),F(0)
 for v,pm in zip(midpoint,p):poly_pz=add(poly_pz,scale(v,pm))
 sq=[F(0)]*1023
 for i in range(512):
  vi=midpoint[i]
  for j in range(i,512):
   x=vi*midpoint[j]
   if i==j:sq[0]+=x/2;sq[2*i]+=x/2
   else:sq[j-i]+=x;sq[i+j]+=x
 poly_z2=F(0),F(0)
 for v,raw in zip(sq,dx):poly_z2=add(poly_z2,scale(v,raw))
 eps=F(tail['original_true_cell5_z_minus_any_accepted_P511_uniform_error_exact_upper'])
 assert 0<eps<F(1,10**30)
 fee_pz=eps*(-p[0][0])
 fee_z2=dx[0][1]*(2*eps*supP+eps*eps)
 pz=widen(poly_pz,fee_pz)
 z2=widen(poly_z2,fee_z2)
 D=add(scale(F(4),pz),scale(F(2),z2))
 assert D[0]<=D[1] and D[1]-D[0]<F(1,10**28)
 assert z2[1]>0
 sign='negative' if D[1]<0 else 'positive' if D[0]>0 else 'undecided'
 out={
  'pass':'NF440',
  'standing':'TRUE ORIGINAL J5 SINGLE PANEL CONTINUOUS SIGNED 4pz+2z2 ACCEPTED; WHOLE J5 REQUIRES AGGREGATE P0 AND 3 PANEL INTEGRAL',
  'original_panel_number':panel,'original_true_cell5':'(log(5)-11/10,log(7)-11/10)',
  'source_sha256':SOURCE,'seams_sha256':SEAMS,
  'source_parent_original_JSON_SHA256':PINS[panel],
  'original_panel_physical_piece_rational_bound_enclosures':lo['original_panel_true_piece_exact_bounds'],
  'original_internal_cuts_are_not_original_support_seams':['31/50','73/100'],
  'original_NF404_dyadic_center':mom['original_NF404_dyadic_center'],
  'original_regular_minus_and_principal_jump_active':[2,3,4,5],
  'original_regular_plus':[],'original_principal_jump_inactive':[7,8,9],
  'original_source_native_coefficient_count':512,
  'original_independent_short_padding_overlap_n0to7':True,
  'original_max_source_native_interval_width_exact':str(maxwidth),
  'original_NF410_full_p0_aggregate_still_required':True,
  'original_source_midpoint_P511_sup_bound':str(supP),
  'original_true_z_minus_P511_epsilon':str(eps),
  'original_true_principal_p0_interval':list(map(str,p[0])),
  'original_true_dx_length_interval':list(map(str,dx[0])),
  'original_signed_pz_poly_interval':list(map(str,poly_pz)),
  'original_signed_z2_poly_interval':list(map(str,poly_z2)),
  'original_signed_pz_true_tail_fee':str(fee_pz),
  'original_signed_z2_true_tail_fee':str(fee_z2),
  'original_signed_pz_complete_interval':list(map(str,pz)),
  'original_signed_z2_complete_interval':list(map(str,z2)),
  'original_true_signed_D_piece_interval':list(map(str,D)),
  'original_true_signed_D_piece_sign':sign,
  'full_original_true_cell5_signed_decided':False,
  'original_global_NF410_NF404_signed_decided':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 dst=Path(args.output);dst.parent.mkdir(parents=True,exist_ok=True)
 dst.write_text(json.dumps(out,indent=2)+'\n')
 print('NF440 original true J5 piece',panel,'pz',float(pz[0]),float(pz[1]),'z2',float(z2[0]),float(z2[1]))
 print('NF440 original true J5 piece signed D',panel,sign,float(D[0]),float(D[1]),'tail fee',float(4*fee_pz+2*fee_z2))
 print('NF410 full original cell5 p0 three-piece summation and full D aggregate OPEN')
if __name__=='__main__':main()
