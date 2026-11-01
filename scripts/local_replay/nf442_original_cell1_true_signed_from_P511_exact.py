#!/usr/bin/env python3
"""NF442 exact original true continuous physical J1 signed D1.

Immutable original NF441 low a0..63 and conditional source tail; NF442
indexed native source a64..511, distinct padding overlap a56..71,
and independent NF442 original NF407 principal p=q (r=0) 512
moments, true raw dx1023. Original NF404 midpoint Cheb exact
Fraction convolution and complete uniform z-P511 fee charged.
No global NF410/NF404 W-ODD-NEG or RH promotion.
"""
import argparse,hashlib,json,sys,zipfile
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
SOURCE='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAMS='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
PINS={
 'low':'895432f34bcd132752ba0d74fd2a7e5b0e81cf99b6e00216a16a1a5a1b35fac2',
 'mid':'cefb041af7c8a4d11c75371d471169747170f42aa68474edd32f113ee68d8e6d',
 'high':'0296e040d0915b4a7f19445d6f123d50d6f60d4fa8cb720c53f9f27c2a3aa794',
 'control':'4ec8e6ba4236c73fafd9a867e4f20afb703e6309dcdb14640af629c0faef5f3c',
 'tail':'b8c3fba2e15f29e5906729ea79de8008b6b96570ae94b70486c705f31dfdea22',
 'moments':'73e9f9d55dc7330e1fc35113812a3219fa8c989ad2e8fc2ba66fba80dfa49cdd',
}
N=512;J1='(0,11/10-log(3))'
def read(path,key):
 path=Path(path);b=path.read_bytes()
 if zipfile.is_zipfile(path):
  with zipfile.ZipFile(path) as z:
   names=[n for n in z.namelist() if n.endswith('.json')]
   assert len(names)==1
   b=z.read(names[0])
 digest=hashlib.sha256(b).hexdigest()
 assert digest==PINS[key],('original source SHA custody mismatch',key,digest)
 return json.loads(b)
def interval(x):
 a,b=map(F,x)
 assert a<=b
 return a,b
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def scale(v,x):return (v*x[0],v*x[1]) if v>=0 else (v*x[1],v*x[0])
def overlap(x,y):return x[0]<=y[1] and y[0]<=x[1]
def main():
 ap=argparse.ArgumentParser()
 for key in PINS:ap.add_argument('--'+key,required=True)
 ap.add_argument('--output',required=True)
 args=ap.parse_args()
 d={k:read(getattr(args,k),k) for k in PINS}
 low,mid,high,ctl,tail,m=(d[k] for k in PINS)
 assert [low['pass'],mid['pass'],high['pass'],ctl['pass'],tail['pass'],m['pass']]==['NF441','NF442','NF442','NF442','NF441','NF442']
 assert tail['original_source_sha256']==m['original_nf407_source_sha256']==SOURCE
 assert tail['original_seams_sha256']==m['original_nf406_seams_sha256']==SEAMS
 assert m['original_true_cell1']==J1
 assert m['original_native_precision_bits']==2048
 assert m['original_NF404_dyadic_center']=='6677356497477490213/4611686018427387904'
 assert m['original_active_minus_prime_powers']==[2,3]
 assert m['original_active_plus_prime_powers']==[2,3]
 assert m['original_inactive_prime_powers']==[4,5,7,8,9]
 assert m['original_principal_jump_weights_active']==[]
 assert m['original_principal_jump_weights_inactive']==[2,3,4,5,7,8,9]
 assert m['original_principal_jump_weight_multiplicities']=={}
 assert m['original_regular_z_has_both_n2_n3_signed_translates_but_principal_jumps_none']
 assert m['original_nf410_independent_true_cell1_signed_p0_overlap']
 assert m['number_original_signed_p_moments']==N
 assert m['number_original_raw_dx_moments']==2*N-1
 for key in ('low','mid','high','control'):
  x=d[key]
  assert x['source_sha256']==SOURCE and x['seams_sha256']==SEAMS
  assert x['original_true_cell1']==J1
  assert x['original_minus_translate_primes']==[2,3] and x['original_plus_translate_primes']==[2,3]
  assert x['original_neither_prime_branches']==[4,5,7,8,9]
  assert x['original_signed_prime_translate_terms']==4
  assert x['original_independent_direct_source_both_n2_and_n3_prime_overlap_pass']
  assert x['original_independent_direct_source_endpoint_overlap_pass']
  assert x['common_endpoint_image_indices']==2048
  assert x['original_exact_NF404_dyadic_center']==m['original_NF404_dyadic_center']
  assert x['original_native_precision_bits']==2048
  assert x['analytic_Chebyshev_center']=='7/10000' and x['analytic_Chebyshev_halfwidth']=='1/1250'
 for key,a,b in [('low',0,64),('mid',64,320),('high',320,512),('control',56,72)]:
  xs=d[key]['coefficients']
  assert [x['n'] for x in xs]==list(range(a,b))
  assert all(interval(x['true_original_cell1_fixed_branch_coefficient_outward_interval'])[1]-interval(x['true_original_cell1_fixed_branch_coefficient_outward_interval'])[0]<F(1,10**44) for x in xs)
 for n in range(56,64):
  assert overlap(interval(low['coefficients'][n]['true_original_cell1_fixed_branch_coefficient_outward_interval']),
                 interval(ctl['coefficients'][n-56]['true_original_cell1_fixed_branch_coefficient_outward_interval']))
 for n in range(64,72):
  assert overlap(interval(mid['coefficients'][n-64]['true_original_cell1_fixed_branch_coefficient_outward_interval']),
                 interval(ctl['coefficients'][n-56]['true_original_cell1_fixed_branch_coefficient_outward_interval']))
 assert not tail['original_J1_J2_512_native_source_coefficients_complete']
 t=tail['cells']['1']
 assert len(t)==1 and t[0]['panel']==1
 assert not t[0]['original_native_512_accepted'] # parent was conditional, now discharged by above
 assert sum(t[0]['best_rho_counts'].values())==273
 assert F(t[0]['original_512_midpoint_fee_conditional'])==512*F(5,10**45)
 eps=F(t[0]['original_uniform_z_P511_conditional_bound'])
 assert 0<eps<F(1,10**38)
 vals=low['coefficients']+mid['coefficients']+high['coefficients']
 assert len(vals)==N and [x['n'] for x in vals]==list(range(N))
 a=[sum(interval(x['true_original_cell1_fixed_branch_coefficient_outward_interval']))/2 for x in vals]
 sup=sum(map(abs,a),F(0))
 p=[interval(v) for v in m['original_source_signed_p_cheb_moments_n0_to_n511']]
 J=[interval(v) for v in m['original_cell1_raw_dx_cheb_moments_n0_to_n1022']]
 assert len(p)==N and len(J)==2*N-1
 assert p[0][1]<0 and J[0][0]>=0
 assert J[0][1]<F(1,500)
 pz=(F(0),F(0))
 for x,y in zip(a,p):pz=add(pz,scale(x,y))
 # T_i*T_j = (T_(i+j)+T_|i-j|)/2, full exact polynomial.
 sq=[F(0)]*(2*N-1)
 for i in range(N):
  for j in range(i,N):
   v=a[i]*a[j]
   if i==j:
    sq[0]+=v/2;sq[2*i]+=v/2
   else:
    sq[j-i]+=v;sq[j+i]+=v
 z2=(F(0),F(0))
 for x,y in zip(sq,J):z2=add(z2,scale(x,y))
 # True z=P511+r. p=v/2*log[B/(B-x)]<0 on (0,B).
 # No principal jump on J1: ∫|p| = -∫p = -p0.
 fee_pz=eps*(-p[0][0])
 fee_z2=J[0][1]*(2*eps*sup+eps**2)
 true_pz=(pz[0]-fee_pz,pz[1]+fee_pz)
 true_z2=(z2[0]-fee_z2,z2[1]+fee_z2)
 D=add(scale(F(4),true_pz),scale(F(2),true_z2))
 assert D[0]<=D[1] and D[1]-D[0]<F(1,10**20)
 sign=('positive' if D[0]>0 else 'negative' if D[1]<0 else 'undecided')
 result={
  'pass':'NF442',
  'standing':'SOURCE-CERTIFIED TRUE ORIGINAL CONTINUOUS J1 FULL SIGNED D1; GLOBAL NF410 NF404 RH OPEN' if sign!='undecided' else 'TRUE J1 SIGNED INTERVAL UNDECIDED',
  'original_source_sha256':SOURCE,'original_seams_sha256':SEAMS,
  'original_immutable_input_json_sha256':PINS,
  'original_true_cell1':J1,
  'original_NF404_dyadic_center':m['original_NF404_dyadic_center'],
  'original_active_regular_minus':[2,3],'original_active_regular_plus':[2,3],
  'original_active_principal_jumps':[],'original_principal_jump_multiplicities':{},
  'original_source_native_512_coefficient_balls':512,
  'original_independent_source_overlap_modes_56_to_71':True,
  'original_signed_p_moments_used':512,'original_raw_dx_moments_used':1023,
  'original_original_nf410_p0_overlap':True,
  'original_true_z_minus_midpoint_P511_uniform_error_exact':str(eps),
  'original_P511_sum_abs_coefficients':str(sup),
  'original_true_J1_length_interval':list(map(str,J[0])),
  'original_true_J1_p0_interval':list(map(str,p[0])),
  'original_true_J1_pz_interval':list(map(str,true_pz)),
  'original_true_J1_z2_interval':list(map(str,true_z2)),
  'original_true_J1_signed_4pz_plus_2z2_interval':list(map(str,D)),
  'original_true_J1_signed_interval_width':str(D[1]-D[0]),
  'original_true_J1_signed_sign':sign,
  'original_pz_uniform_tail_fee':str(fee_pz),
  'original_z2_uniform_tail_fee':str(fee_z2),
  'original_original_global_NF410_NF404_scalar_decided':False,
  'original_fourth_J242_exterior_upper_closed':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(result,indent=2)+'\n')
 print('NF442 ORIGINAL TRUE J1',sign,'D1 [',float(D[0]),',',float(D[1]),'] width',float(D[1]-D[0]),'epsilon',float(eps))
 print('NF442 original full global W-ODD-NEG RH OPEN')
if __name__=='__main__':main()
