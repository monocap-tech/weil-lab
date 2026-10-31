#!/usr/bin/env python3
"""NF405 original fourth-source analytic high-tail horizon.
Source-pinned exact Fraction; actual supported lowband integral OPEN.
"""
import argparse,json,hashlib,sys
from pathlib import Path
from fractions import Fraction as F
from nf375_cutoff_reduction import calc,CAP_A,CAP_D,CAP_K
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
N401='644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515'
N398='bae006e4fb542c4b0c6d184ae8cfbc2e7c924d45c89092ebda89cf0c6057c877'
NF375_BLOB='03c709571046d3f09307614aaded9749f5a15ba1'
NF374_SHA='a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559'
def read(p):
 b=Path(p).read_bytes();return json.loads(b),hashlib.sha256(b).hexdigest(),hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def run(p):
 center,csha,_=read(p.center);nf375,hsha,gh=read(p.nf375)
 nf398,sha398,_=read(p.nf398);nf401,sha401,_=read(p.nf401)
 nf403,sha403,_=read(p.nf403)
 assert gh==NF375_BLOB
 assert nf375['native_report_sha256']==NF374_SHA
 assert sha401==center['original_nf401_selected_native_sha256']==N401
 assert sha398==nf403['original_nf398_highband_native_sha256']==N398
 assert nf403['original_nf401_accepted_242D_native_sha256']==N401
 assert center['actual_original_full_supported_centered_scalar_integrated'] is False
 assert nf375['measured_original_lowband'] is False
 assert all(x['W_ODD_NEG']==x['RH']=='OPEN' for x in (center,nf375,nf398,nf401,nf403))
 d=nf375['directions'][3];assert d['direction']==4
 a1,a3,b=[F(d[k]) for k in ('signed_original_first_sine_moment','original_sine_absolute_cubic_moment','original_sinh_coefficient')]
 original_H=F(nf398['original_NF375_fourth_highband_action_norm_upper'])
 assert calc(24,a1,a3,b,CAP_A[3],CAP_D[3],CAP_K[3])[0]==original_H
 E0=F(center['original_selected_after_pole_shear_power_lower_exact'])
 E1=F(center['original_selected_after_pole_shear_power_upper_exact'])
 gamma2=F(center['exact_source_original_full_complement_power_budget'])
 assert F(0)<E0<E1 and E1-E0<F(1,10**100)
 assert E1<F(332,10**13)**2
 delta=gamma2/2
 R=F(332,10**13)
 assert E1+delta<R*R
 rows=[];first=None
 for k in range(24,49):
  h,parts,_=calc(k,a1,a3,b,CAP_A[3],CAP_D[3],CAP_K[3])
  fee=delta+2*R*h+h*h+E1-E0
  passed=fee<gamma2
  rows.append({'k':k,'cutoff':str(2**k),'original_highband_H':str(h),
               'source_sine':str(parts[0]),'source_sinh':str(parts[1]),
               'matched_exterior':str(parts[2]),
               'cross_term_fee':str(2*R*h+h*h),
               'half_budget_conditional_gate':passed})
  if first is None and passed:first=k
 assert first is not None and first>24
 assert all(row['half_budget_conditional_gate']==(row['k']>=first) for row in rows)
 out={
  'pass':'NF405','standing':'SOURCE-EXACT ORIGINAL HIGHBAND HORIZON; CENTERED PHYSICAL LOWBAND INTEGRAL UNMEASURED',
  'original_nf401_native_sha256':sha401,'original_nf398_native_sha256':sha398,
  'original_nf375_blob_sha1':gh,'original_nf375_sha256':hsha,
  'original_nf374_native_source_sha256':NF374_SHA,
  'original_nf404_pole_shear_sha256':csha,'original_nf403_source_sha256':sha403,
  'original_selected_centered_power_lower':str(E0),
  'original_selected_centered_power_upper':str(E1),
  'original_half_budget_delta':str(delta),
  'original_exterior_power_budget_gamma2':str(gamma2),
  'future_original_supported_lowband_scalar_cap':str(E1+delta),
  'source_strict_sqrt_upper_R':str(R),
  'first_feasible_log2_cutoff_under_half_budget':first,
  'first_feasible_cutoff':str(2**first),
  'accepted_original_k24_H_reproduced':True,'horizons':rows,
  'conditional_inequality':'If a separately certified original supported lowband centered energy <= E1+delta, then complete centered power <= E0+gamma2 by original analytic Hk and positive triangle.',
  'actual_original_supported_lowband_centered_energy_measured':False,
  'actual_original_full_supported_centered_power_upper':False,
  'original_full_lowband_upper':False,'new_signed_kernel_cells':0,
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(p.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF405 original exact 50% lowband slack cutoff k=',first,', Lambda=',2**first)
 print('NF405 original positive physical integral still UNMEASURED')
 return out
if __name__=='__main__':
 p=argparse.ArgumentParser()
 for name,default in [('center','NF404_original_selected_pole_shear_exact.json'),('nf375','NF375_reduced_cutoff_exact.json'),('nf398','NF398_original_j387_selected_signed_native.json'),('nf401','NF401_original_242D_selected_column_source_native.json'),('nf403','NF403_original_joint_complement_power_exact.json')]:
  p.add_argument('--'+name,default='notes/data/provisional/'+default)
 p.add_argument('--output',required=True)
 run(p.parse_args())
