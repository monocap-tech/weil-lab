#!/usr/bin/env python3
"""NF441 true original p0 moments for J1 J2 and singular-endpoint J8.

Authentic NF407 v=u4(B)<0, q(x)=v/2 log(B/(B-x)),
r(x)=v sum_{original jump active n} Lambda(n)/sqrt(n).
The endpoint log is integrable on J8: primitive B at x=B is its
rigorous limit, with NO arbitrary endpoint cutoff or source migration.
Independent original NF410 zeroth moment must overlap on each cell.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
from flint import arb,ctx
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10);BASE={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
CONFIG={1:(8,9,()),2:(9,10,(3,)),8:(15,16,(2,3,4,5,7,8,9))}
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
def A(x):return arb(str(x))
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def bounds(z,d=75):
 m,r,e=z.mid_rad_10exp(d);q=F(10)**int(e)
 return F(int(m)-int(r))*q,F(int(m)+int(r))*q
def prim(x):
 # F'=log[B/(B-x)], F(B)=B via t log(t)->0.
 if x is None:return A(B)
 z=A(B)-x
 assert z>0
 return x+z*(z/A(B)).log()
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 ap.add_argument('--principal',default='notes/data/provisional/NF407_original_prime_jump_log_power_exact.json')
 ap.add_argument('--nf410',default='notes/data/provisional/NF410_original_signed_taylor_moments.json')
 ap.add_argument('--precision',type=int,default=2048)
 ap.add_argument('--output',required=True)
 a=ap.parse_args();ctx.prec=a.precision
 s,sha=read(a.source);seams,ksha=read(a.seams)
 principal,psha=read(a.principal);nf410,nsha=read(a.nf410)
 assert sha==SRC and ksha==SEAM and a.precision>=2048
 assert principal['original_nf406_seams_sha256']==ksha
 assert nf410['original_nf406_source_sha256']==ksha and nf410['original_nf407_source_sha256']==psha
 assert s['original_dimension']==242 and len(s['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert all(j['W_ODD_NEG']==j['RH']=='OPEN' for j in (s,seams,principal,nf410))
 v0,v1=map(F,principal['original_source_u4_endpoint_interval'])
 assert v0<v1<0
 mid=(v0+v1)/2;radius=(v1-v0)/2
 knots=seams['certified_ordered_knots']
 result={'pass':'NF441','standing':'ORIGINAL TRUE J1 J2 J8 PRINCIPAL p0 INDEPENDENT NF410 NATIVE; J8 LOG ENDPOINT INTEGRAL BY LIMIT NOT REGULAR z',
  'original_source_sha256':sha,'original_seams_sha256':ksha,'original_principal_sha256':psha,
  'nf410_parent_sha256':nsha,'original_precision_bits':a.precision,
  'original_v_endpoint_interval':[str(v0),str(v1)],'cells':{},
  'original_true_J1_J2_J8_signed_pz_z2_integrated':False,'W_ODD_NEG':'OPEN','RH':'OPEN'}
 for cell,(i,j,active) in CONFIG.items():
  L,R=knots[i],knots[j]
  old=nf410['original_positive_original_physical_cells'][cell-1]
  assert old['cell']==cell and old['left_label']==L['label'] and old['right_label']==R['label']
  lv={'0':lambda:A(0),'B-log(3)':lambda:A(B)-A(3).log(),
      '-B+log(9)':lambda:A(9).log()-A(B)}[L['label']]()
  rv=None if R['label']=='+B' else {'B-log(3)':lambda:A(B)-A(3).log(),
      '-B+log(4)':lambda:A(4).log()-A(B)}[R['label']]()
  assert lv>=0 and (rv is None or lv<rv<A(B))
  length=(A(B) if rv is None else rv)-lv
  W=sum((A(BASE[n]).log()/A(n).sqrt() for n in active),arb(0))
  assert W>=0 and W<A(5)
  val=A(mid)*(W*length+(prim(rv)-prim(lv))/2)
  lo,hi=bounds(val)
  # Original jump weights <5, length<B, log primitive integrated < B
  # on (0,B). Therefore midpoint-v uncertainty <(5B+B/2)*rad<7rad.
  fee=7*radius
  lo-=fee;hi+=fee
  prior=tuple(map(F,old['signed_original_p_moments_by_degree_0_to_3'][0]))
  assert lo<=prior[1] and prior[0]<=hi,('original NF410 signed p0 disagreement',cell,float(lo),float(prior[0]))
  assert lo<=hi<0 and hi-lo<F(1,10**30)
  result['cells'][str(cell)]={'true_left':L['label'],'true_right':R['label'],
    'original_r_jump_active':list(active),
    'original_q_log_endpoint_integrated_by_limit':rv is None,
    'source_original_p0_interval':[str(lo),str(hi)],
    'independent_NF410_original_p0_interval':list(map(str,prior)),
    'independent_NF410_p0_overlap':True,
    'signed_p0_strict_negative':True,'complete_true_signed_J_integral':False}
  print('NF441 ORIGINAL p0 true cell',cell,'=',float(lo),'independent NF410 overlap PASS',flush=True)
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
