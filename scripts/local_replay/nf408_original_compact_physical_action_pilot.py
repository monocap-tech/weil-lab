#!/usr/bin/env python3
"""NF408: original u4 true physical m(D) action pilot at ONE interior point.

High precision mpmath, signed source correlated FIRST, original arch compact
difference integral and all seven translated primes. This is an EXPLORATORY
midpoint quadrature, *NOT* an Arb/interval-certified action or L2 scalar.
"""
import argparse,hashlib,json,sys,time
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
SOURCE_SHAS={
 'original_parent_NF374':'a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559',
 'original_parent_NF401':'644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515'
}
N7={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
B=F(11,10)
def read(p):
 z=Path(p).read_bytes();return json.loads(z),hashlib.sha256(z).hexdigest()
def rat(z):
 x=F(z)
 return mp.mpf(x.numerator)/x.denominator
def dyad_ball_mid(z):
 mid,rad=z
 return mp.ldexp(mp.mpf(mid[0]),int(mid[1]))
class Source:
 def __init__(self,s):
  self.pi=mp.pi
  # Collect same freq in one original source physical family:
  # x^even*sin and x^odd*cos have an explicit original initial
  # polynomial prefix. Actual original 242+4 sources all retained.
  groups={}
  for node,bal in zip(s['original_selected_generator_node_orders'],s['original_exact_native_raw_selected_coefficients_mid_radius']):
   c,k=node;v=-dyad_ball_mid(bal)
   if c=='pole':
    groups.setdefault('pole',[]).append((0,v))
   else:
    c=F(c);groups.setdefault(c,[]).append((k,v))
  for v,probe in zip(s['original_exact_native_original_four_critical_coefficients_mid_radius'],s['original_source_critical_sines_and_pole_coefficients']):
   alpha=dyad_ball_mid(v)
   for freq,coeff in zip(s['original_source_critical_sine_frequencies'],probe['sine_coefficients']):
    c=F(freq)
    groups.setdefault(c,[]).append((0,alpha*rat(coeff)))
   groups.setdefault('pole',[]).append((0,alpha*rat(probe['sinh_coefficient'])))
  self.pole=sum((v for k,v in groups.pop('pole')),mp.mpf(0))
  self.groups=[]
  for c,vals in groups.items():
   self.groups.append((2*self.pi*rat(c), sorted(vals)))
  self.B=rat(B)
 def at(self,x):
  if abs(x)>self.B:return mp.mpf(0)
  if x==0:return mp.mpf(0)
  # entire physical true source u4(x) is formed from the single
  # original correlated 242+4 carrier before multiplier action.
  result=self.pole*mp.sinh(x/2)
  for omega,vals in self.groups:
   sn=mp.sin(omega*x);co=mp.cos(omega*x)
   total=mp.mpf(0)
   last=0;power=mp.mpf(1)
   for k,v in vals:
    power*=x**(k-last);last=k
    total+=v*power*(sn if k%2==0 else co)
   result+=total
  return result
def kernel(t):
 return mp.exp(-t/4)/(-mp.expm1(-t))
def arch_tail(t):
 z=mp.exp(-t/4)
 return 2*(mp.atanh(z)+mp.atan(z))
def gauss_integral(fn,left,right,step,n):
 if right<=left:return mp.mpf(0),0
 import numpy as np
 # x_j and weights are double nodes (approximate, not certified);
 # evaluate them with high precision and compare independent n settings.
 from numpy.polynomial.legendre import leggauss
 nodes,weights=leggauss(n)
 X=[mp.mpf(repr(z)) for z in nodes]
 W=[mp.mpf(repr(z)) for z in weights]
 segments=max(1,int(mp.ceil((right-left)/step)))
 acc=mp.mpf(0)
 for k in range(segments):
  a=left+(right-left)*k/segments
  b=left+(right-left)*(k+1)/segments
  mid=(a+b)/2;half=(b-a)/2
  for t,w in zip(X,W):
   acc+=half*w*fn(mid+half*t)
 return acc,segments*n
def evaluate(sample,s,step,n,lower_t):
 B=s.B;x=rat(sample)
 ux=s.at(x)
 uB=s.at(B)
 rho=rat(F(6677356497477490213,4611686018427387904))
 t1=2*(B-x);tmax=2*(B+x)
 def fn(t):
  yp=x+t/2;ym=x-t/2
  return kernel(t)*(ux-(s.at(yp) if yp<B else mp.mpf(0))/2-
                       (s.at(ym) if ym>-B else mp.mpf(0))/2)
 # The omitted 0<t<lower_t source-specific term is NOT CERTIFIED:
 # on smooth interior the true difference has O(t²) numerator.
 # Its omission is monitored as a pilot convergence dimension.
 part0,n0=gauss_integral(fn,lower_t,t1,step,n)
 part1,n1=gauss_integral(fn,t1,tmax,step,n)
 arch=(mp.digamma(mp.mpf(1)/4)-mp.log(mp.pi)+arch_tail(tmax))*ux+part0+part1
 primes=mp.mpf(0)
 for k,base in N7.items():
  lag=mp.log(k);weight=mp.log(base)/mp.sqrt(k)
  primes-=weight*(s.at(x+lag)+s.at(x-lag))
 full=arch+primes
 g=full-rho*mp.sinh(x/2)
 q=uB/2*mp.log(B/(B-x))
 r=uB*sum((mp.log(base)/mp.sqrt(n) for n,base in N7.items() if x>abs(B-mp.log(n))),mp.mpf(0))
 z=g-q-r
 return {
  'original_u4_x':mp.nstr(ux,45),
  'original_u4_B':mp.nstr(uB,45),
  'original_arch_action_x':mp.nstr(arch,45),
  'original_7_prime_action_x':mp.nstr(primes,45),
  'original_complete_multiplier_action_x':mp.nstr(full,45),
  'original_centered_g_x':mp.nstr(g,45),
  'original_log_q_x':mp.nstr(q,45),
  'original_prime_jump_r_x':mp.nstr(r,45),
  'original_continuous_z_x':mp.nstr(z,45),
  'signed_reconstruction_error_g_minus_q_r_z':mp.nstr(g-q-r-z,20),
  'quadrature_count':n0+n1,
 }
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--boundary',default='notes/data/provisional/NF406_original_physical_endpoint_log_exact.json')
 p.add_argument('--center',default='notes/data/provisional/NF404_original_selected_pole_shear_exact.json')
 p.add_argument('--dps',type=int,default=205)
 p.add_argument('--x',default='11/20')
 p.add_argument('--step',default='1/50')
 p.add_argument('--nodes',type=int,default=16)
 p.add_argument('--min-t',default='1/100000000')
 p.add_argument('--output',required=True)
 args=p.parse_args()
 source,ssha=read(args.source)
 boundary,bsha=read(args.boundary)
 center,csha=read(args.center)
 assert source['original_dimension']==242
 assert source['original_nf374_native_sha256']==SOURCE_SHAS['original_parent_NF374']
 assert center['original_nf401_selected_native_sha256']==SOURCE_SHAS['original_parent_NF401']
 assert source['original_exported_coefficients_are_4096bit_arb_not_float'] is True
 assert source['original_u4_endpoint_matches_nf405_exact_signed_bounds'] is True
 assert len(source['original_exact_native_raw_selected_coefficients_mid_radius'])==242
 assert len(source['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert source['W_ODD_NEG']==source['RH']==boundary['W_ODD_NEG']==boundary['RH']==center['W_ODD_NEG']==center['RH']=='OPEN'
 assert args.dps>=190 and args.nodes>=12 and F(0)<F(args.min_t)<F(1,10**6)
 mp.mp.dps=args.dps
 t=time.monotonic()
 s=Source(source)
 x=rat(args.x)
 assert 0<x<s.B
 val=evaluate(args.x,s,rat(args.step),args.nodes,rat(args.min_t))
 # Check the true original source is at native original 8 point.
 native=next((z for z in source['source_rational_samples']
              if F(z['x_over_B'])*B==F(args.x)),None)
 if native is not None:
  yy=mp.mpf(val['original_u4_x'])
  a,b=map(rat,native['original_true_u4_value_outward'])
  assert a-mp.mpf('1e-35')<=yy<=b+mp.mpf('1e-35')
  val['original_true_source_4096bit_sample_overlap_with_rounded_display']=True
 # The midpoint quadrature absolute error is NOT bounded.
 result={
  'pass':'NF408',
  'standing':'ORIGINAL MIDPOINT-COEFFICIENT PHYSICAL ACTION SINGLE-POINT GAUSS PILOT; NO RIGOROUS QUADRATURE ERROR OR L2 NORM',
  'original_nf407_coeff_native_sha256':ssha,
  'original_nf406_endpoint_log_sha256':bsha,
  'original_nf404_center_sha256':csha,
  'sample_physical_x':args.x,
  'working_decimal_digits':args.dps,
  'gauss_segment_max_width':args.step,
  'approximate_gauss_nodes_per_segment':args.nodes,
  'small_t_omitted_positive_piece_lower_bound':args.min_t,
  'double_approximated_legendre_nodes_and_weights_NOT_CERTIFIED':True,
  'source_export_native_arb_centers_USED_source_native_radii_NOT_PROPAGATED':True,
  'original_unmeasured_true_source_multipler_point_error':True,
  'sample':val,
  'original_continuous_regularized_z_interval_certified':False,
  'original_original_full_centered_physical_scalar_upper_computed':False,
  'original_lowband_complement_upper_computed':False,
  'new_signed_kernel_cells':0,
  'W_ODD_NEG':'OPEN','RH':'OPEN',
  'elapsed_seconds':round(time.monotonic()-t,1)
 }
 target=Path(args.output);target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps(result,indent=2)+'\n')
 print('NF408 original physical point PILOT (NOT certified):')
 print('x=',args.x,'source u=',val['original_u4_x'],'g=',val['original_centered_g_x'],'z=',val['original_continuous_z_x'])
 print('source true residual original physical L2 still UNMEASURED')
if __name__=='__main__':main()
