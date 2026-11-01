#!/usr/bin/env python3
"""NF441 conditional original J1/J2 P511 source tails, not true certificates."""
import argparse,hashlib,json,sys,math
from pathlib import Path
from fractions import Fraction as F
from nf425_original_cell6_chebyshev_existence_exact import source
from nf433_original_cell3_cell7_branch_ellipse_router_exact import cheb_source_tail
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10);N=512
SOURCE='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAMS='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
P={1:[(F(7,10000),F(8,10000))],
   2:[(F(55,1000),F(55,1000)),(F(148,1000),F(58,1000)),(F(243,1000),F(53,1000))]}
def read(p):
 b=Path(p).read_bytes();return json.loads(b),hashlib.sha256(b).hexdigest()
def main():
 a=argparse.ArgumentParser()
 a.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 a.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 a.add_argument('--output',required=True)
 x=a.parse_args()
 s,sh=read(x.source);k,kh=read(x.seams)
 assert sh==SOURCE and kh==SEAMS
 assert s['original_dimension']==242 and len(s['original_source_critical_sine_frequencies'])==32
 assert s['W_ODD_NEG']==s['RH']==k['W_ODD_NEG']==k['RH']=='OPEN'
 assert k['certified_ordered_knots'][9]['label']=='B-log(3)'
 c,pole,S0=source(s)
 assert len(c)==273 and S0<F(1,10**700)
 raw=sum((abs(v)*B**j for (f,j),v in c.items()),abs(pole))
 assert raw<10**160
 assert 2*F(7,10)*F(5,7)+2*F(11,10)*F(3,5)<3
 out={'pass':'NF441','standing':'ORIGINAL SOURCE EXACT CONDITIONAL 512 MODE ERRORS; NATIVE ALL512 NOT YET CERTIFIED',
 'original_source_sha256':sh,'original_seams_sha256':kh,
 'original_J1_J2_512_native_source_coefficients_complete':False,
 'cells':{},'W_ODD_NEG':'OPEN','RH':'OPEN'}
 for cell,panels in P.items():
  vals=[]
  for i,(C,H) in enumerate(panels,1):
   right=C+H*F(13,5);left=C-H*F(13,5);d=B-right
   assert -B<left<right<B and d>F(11,20)
   assert 1+2*d+2*d*d>3
   tri=F(0);counts={str(r):0 for r in (2,3,4,5)}
   for (f,j),v in c.items():
    z,r=min((cheb_source_tail(f,j,v,r,H),r) for r in (F(2),F(3),F(4),F(5)))
    tri+=z;counts[str(r)]+=1
   assert sum(counts.values())==273
   image=F(36,2000)*10**160*F(1,3)**2048
   pole_tail=F(4*10**7)*(abs(pole)+2)/5**N
   log_tail=raw*F(1,5)**N/(N*(1-F(1,5)))
   sr=(10**12+20)*S0
   midpoint=512*F(5,10**45)
   eps=tri+image+pole_tail+log_tail+sr+midpoint
   assert eps<F(1,10**38)
   vals.append({'panel':i,'source_512_generator_tail':str(tri),
   'original_2048_image_remainder':str(image),
   'original_joint_pole_tail':str(pole_tail),
   'original_endpoint_log_tail':str(log_tail),
   'original_4096bit_source_radius_charge':str(sr),
   'original_512_midpoint_fee_conditional':str(midpoint),
   'original_uniform_z_P511_conditional_bound':str(eps),
   'original_native_512_accepted':False,
   'best_rho_counts':counts,
   'fixed_source_analytic_ellipse_real_bounds':[str(left),str(right)]})
   print('NF441',cell,'panel',i,'conditional original response error',float(eps),flush=True)
  out['cells'][str(cell)]=vals
 p=Path(x.output);p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
