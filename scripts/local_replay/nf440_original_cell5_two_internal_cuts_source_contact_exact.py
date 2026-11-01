#!/usr/bin/env python3
"""NF440 independent contact across artificial J5 integration cuts.

Check full original 512 native midpoint source-polynomials on BOTH sides
at x=31/50 and x=73/100, charging independent sourcewise true z tails.
The cuts are internal integration devices; no prime jump at either.
Exact Fraction Chebyshev recursion, independent of signed integrations.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SOURCE="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAMS="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
PINS={
 1:("ac3d579ea10fe25009eafeddc174d0d88c78ff20f4ed447a9b41e4adc5c6e59e",
    "f6cd1f6d777bd9227bd1763bf98762b7867e7aa7686c38c26951461e906c7274",
    "7620671f67532897b8426f04afeec99c823e3e01fb971fc080693a0e1e7254e3"),
 2:("0655c8900521b31f17ccf0ab8c3b98bf950ab0a8bb6f2a0872dec88ac07f286b",
    "b6194bd6af39ff7095f6a2220334383ea74967119c05acf08c73044c2ddf1378",
    "bb11b50a7ad20442e08e47786933f626baae34e3f523aca09810ad669abbaa6a"),
 3:("c2ea899bf3a958b4e039efcad6cad68ada942b76c11dd11d2f904c444195c413",
    "e27b1021b2d279e3d611997eca81dbb2280bf2329a0483b7dc1be16284668263",
    "69384c2c0bcaaa82058c3db1c6cb34d742748366fc34306bc7ca14a35de6e969")}
CENTERS=(F(565,1000),F(677,1000),F(789,1000))
H=F(63,1000)
def read(path,pin):
 raw=Path(path).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==pin,path
 return json.loads(raw)
def poly(coeff,t):
 T0=F(1);T1=t
 ret=coeff[0]*T0+coeff[1]*T1
 for n in range(2,512):
  T2=2*t*T1-T0
  ret+=coeff[n]*T2
  T0,T1=T1,T2
 return ret
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--input-root',required=True)
 ap.add_argument('--output',required=True)
 a=ap.parse_args()
 root=Path(a.input_root);c={};eps={}
 for i in (1,2,3):
  L=read(root/f'p{i}/low/NF440_original_J5_panel{i}_n0to256.json',PINS[i][0])
  R=read(root/f'p{i}/high/NF440_original_J5_panel{i}_n256to512.json',PINS[i][1])
  tail=read(root/f'p{i}/tail/NF440_J5_panel{i}_sourcewise_true_tail.json',PINS[i][2])
  assert L['pass']==R['pass']==tail['pass']=='NF440'
  assert L['source_sha256']==R['source_sha256']==tail['NF407_original_source_sha256']==SOURCE
  assert L['seams_sha256']==R['seams_sha256']==tail['NF406_original_seams_sha256']==SEAMS
  assert L['original_panel_number']==R['original_panel_number']==tail['original_panel_number']==i
  assert L['original_true_cell5']==R['original_true_cell5']==tail['original_true_cell5']=='(log(5)-11/10,log(7)-11/10)'
  assert L['original_minus_translate_primes']==R['original_minus_translate_primes']==tail['original_minus_translate_active']==[2,3,4,5]
  assert L['original_plus_translate_primes']==R['original_plus_translate_primes']==tail['original_plus_translate_active']==[]
  assert L['original_rational_panel_cuts_are_not_prime_seams']
  assert F(L['analytic_Chebyshev_center'])==F(R['analytic_Chebyshev_center'])==F(tail['original_Chebyshev_center'])==CENTERS[i-1]
  assert F(L['analytic_Chebyshev_halfwidth'])==F(R['analytic_Chebyshev_halfwidth'])==F(tail['original_Chebyshev_halfwidth'])==H
  x=L['coefficients']+R['coefficients']
  assert [v['n'] for v in x]==list(range(512))
  c[i]=[]
  for v in x:
   lo,hi=map(F,v['true_original_cell5_fixed_branch_coefficient_outward_interval'])
   assert lo<=hi and hi-lo<F(1,10**44)
   c[i].append((lo+hi)/2)
  eps[i]=F(tail['original_true_cell5_z_minus_any_accepted_P511_uniform_error_exact_upper'])
  assert 0<eps[i]<F(1,10**30)
 contacts=[]
 for x,left,right in ((F(31,50),1,2),(F(73,100),2,3)):
  pl=poly(c[left],(x-CENTERS[left-1])/H)
  pr=poly(c[right],(x-CENTERS[right-1])/H)
  delta=abs(pl-pr)
  bound=eps[left]+eps[right]
  assert delta < bound
  # Strong secondary source agreement, far below the generous
  # 2.4e-35 function tail. This is NOT an exact equality assertion.
  assert delta<F(1,10**59)
  contacts.append({
   'cut':str(x),'left_panel':left,'right_panel':right,
   'left_original_midpoint_P511':str(pl),'right_original_midpoint_P511':str(pr),
   'absolute_midpoint_P511_difference':str(delta),
   'two_full_source_tail_sum':str(bound),
   'true_z_intervals_at_cut_overlap':True,
   'difference_strict_below_1e_minus59':True})
  print('NF440 original same-source internal contact at',float(x),'delta',float(delta),'source tails',float(bound))
 out={'pass':'NF440',
  'standing':'INDEPENDENT ORIGINAL TRUE J5 MIDPOINT SOURCE-POLYNOMIAL CONTACT AT BOTH NONPHYSICAL CUTS; SIGNED J5 ALREADY SEPARATELY CERTIFIED',
  'original_source_sha256':SOURCE,'original_seams_sha256':SEAMS,
  'original_true_cell5':'(log(5)-11/10,log(7)-11/10)',
  'original_rational_cuts_not_prime_jumps':['31/50','73/100'],
  'panels_all_share_original_regular_minus_n2_n3_n4_n5':True,
  'original_independently_accepted_source_512_modes_per_panel':512,
  'original_contact_checks':contacts,
  'original_global_NF410_NF404_signed_decided':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF440 ACCEPTED two exact rational same-original-source polynomial contacts; no extra physical seams')
if __name__=='__main__':main()
