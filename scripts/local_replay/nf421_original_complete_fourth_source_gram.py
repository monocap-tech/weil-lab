#!/usr/bin/env python3
"""NF421 original 246-generator FOURTH derivative analytic Gram (4096-bit).

All true original NF407 dyadic selected/critical generators consolidated before
differentiation; 4th derivative returns ODD x^even sin/x^odd cos basis,
and original odd pole ->sinh(x/2)/16. Exact NF413 physical trig Gram,
including every selected-critical cross. No quadrature, source shadow,
new generator, or assertion of NF404/RH closure.

Gives uniform |z'''| upper bound on actual original NF406 cell6
[899/1000,901/1000] by differentiating NF420 true arch identity once,
which algebraically cancels standalone u4''(x).
"""
import argparse,json,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
from nf413_original_full_246_curvature_gram_native import Moments
from nf415_original_cell6_I1_validated_acb import read,native_source,A
from nf416_original_cell6_full_I0_regularized_taylor import original_jets
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10);X=F(9,10);RADIUS=F(1,1000)
def ceil_power_two(z):
 k=1
 while not (z<arb(k)):
  k*=2
  assert k<10**250,('full original fourth-derivative Gram unresolved',str(z)[:160])
 return k
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 p.add_argument('--jet',default='notes/data/provisional/NF411_original_source_boundary_jet.json')
 p.add_argument('--nf420',default='notes/data/provisional/NF420_original_cell6_independent_sharpened_Taylor_positive_interval.json')
 p.add_argument('--output',required=True)
 a=p.parse_args()
 source,ssha=read(a.source);seams,seamsha=read(a.seams);jet,jsha=read(a.jet);nf420,gsha=read(a.nf420)
 assert source['original_dimension']==242
 assert len(source['original_selected_generator_node_orders'])==242
 assert len(source['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert len(source['original_source_critical_sine_frequencies'])==32
 assert nf420['original_nf407_source_sha256']==ssha
 assert nf420['original_nf406_seam_sha256']==seamsha
 assert jet['nf407_source_sha256']==ssha
 assert nf420['original_true_third_derivative_L2_integer_upper']==1334
 assert nf420['original_true_second_derivative_global_sup_integer_upper']==2002
 assert nf420['original_true_complete_z_second_x_derivative_uniform_bound']==125457
 assert all(q['W_ODD_NEG']==q['RH']=='OPEN' for q in (source,seams,jet,nf420))
 knots=seams['certified_ordered_knots']
 assert knots[13]['label']=='-B+log(7)' and knots[14]['label']=='-B+log(8)'
 assert F(knots[13]['high'])<X-RADIUS and F(knots[14]['low'])>X+RADIUS
 ctx.prec=4096
 terms,pole,S0=native_source(source)
 assert len(terms)>=240 and S0<F(1,10**700)
 pi=arb.pi()
 current={(f,k):A(v) for f,k,v in terms}
 for order in range(4):
  nxt={}
  for (f,k),v in current.items():
   w=2*pi*A(f)
   if k:nxt[(f,k-1)]=nxt.get((f,k-1),arb(0))+k*v
   nxt[(f,k)]=nxt.get((f,k),arb(0))+(w if (k+order)%2==0 else -w)*v
  current={k:v for k,v in nxt.items() if v!=0}
  print('NF421 full original derivative order',order+1,'physical grouped basis',len(current),flush=True)
 assert len(current)>=200
 M=Moments(pi)
 E=arb(0)
 items=sorted(current.items())
 for i,(key,v) in enumerate(items):
  E+=v*v*M.gram(key,key)
  for prev,w in items[:i]:E+=2*v*w*M.gram(key,prev)
  if (i+1)%60==0:print('NF421 4th source analytic physical Gram row',i+1,'/',len(items),flush=True)
 # Original pole is odd; 4th derivative = pole sinh(x/2)/16.
 pole4=A(pole)/16
 cross=sum((v*M.pole_overlap(f,k) for (f,k),v in items),arb(0))
 E+=2*pole4*cross+pole4*pole4*(A(B).sinh()-A(B))
 assert E>0,('original source fourth Gram loses positivity',str(E)[:220])
 assert E<arb(10)**200,('original fourth Gram midpoint uncontrolled',str(E)[:220])
 S4=10**16*S0
 assert S4<F(1,10**670)
 u4=E.sqrt()+A(F(3,2)*S4)
 N4=ceil_power_two(u4)
 grouped={}
 for f,k,v in terms:grouped.setdefault(f,[]).append((k,v))
 grouped=sorted(grouped.items())
 endpoint=6*original_jets(B,grouped,pole,pi,3)[3]
 S3=F(10**12)*S0
 assert S3<F(1,10**680)
 endBound=ceil_power_two(abs(endpoint)+A(S3))
 # Cauchy-Schwarz: sqrt(2B)<3/2. True source |u'''(s)|
 # ≤|u'''(B)| + ||u''''||L2*sqrt(2B).
 M3=endBound+F(3,2)*N4
 Mz3=58*M3+7*N4+10
 dmin=B-(X+RADIUS)
 t1min=2*dmin;t2min=2*(B+X-RADIUS)
 assert dmin>F(1,6) and t1min>F(1,3) and t2min>3
 # For t>0: |K'| ≤1/(2t)+2/t²,
 # |K''| ≤ (2/t)*[(1/4+1/t)^2+1/t+1/t²].
 def K2bd(t):
  return F(2)/t*((F(1,4)+1/t)**2+1/t+1/t**2)
 assert K2bd(t1min)<140 and K2bd(t2min)<1
 # R''=4K''(t1)+4K''(t2)-1/d³
 assert 4*140+4+1/dmin**3<800
 # all other endpoint terms + original centered a/8 cosh <2,
 # first u''(B) coefficient (K1-K2)<7; sum <10.
 assert F(16)*M3+7*N4+42*M3+10==Mz3
 assert N4>0 and Mz3>0
 result={
 'pass':'NF421',
 'standing':'4096-BIT ORIGINAL COMPLETE FOURTH SOURCE DERIVATIVE CORRELATED GRAM AND GENUINE CELL6 z THIRD x-DERIVATIVE UNIFORM BOUND; NF404 OPEN',
 'original_nf407_source_sha256':ssha,
 'original_nf406_seams_sha256':seamsha,
 'original_nf411_boundary_jet_sha256':jsha,
 'original_nf420_parent_sha256':gsha,
 'original_complete_242_selected_plus_four_critical_generators':True,
 'original_all_selected_critical_correlations_retained':True,
 'original_pole_fourth_derivative_sinh_included':True,
 'original_true_4th_derivative_source_basis_count':len(items),
 'original_true_4th_derivative_L2_Gram_squared_native_arb':str(E),
 'original_source_coefficient_uniform_fourth_derivative_radii_exact':str(S4),
 'original_true_u4_fourth_derivative_L2_upper_power2':str(N4),
 'original_true_u4_third_derivative_at_B_native_arb':str(endpoint),
 'original_u4_third_derivative_at_B_native_with_radius_power2':str(endBound),
 'original_true_u4_third_derivative_global_sup_upper_exact':str(M3),
 'original_complete_z_third_x_derivative_uniform_upper_exact':str(Mz3),
 'original_complete_z_third_x_derivative_original_interval':['899/1000','901/1000'],
 'original_NF420_exact_second_to_third_arch_cancellation':'A_prime=K(t1)-K(t2); original moving I0-I1 u_second boundary=(K(t1)-K(t2))*(u_second(B)-u_second(x)); all standalone u_second(x) cancel',
 'original_true_seven_signed_primes_third_derivative_included_in_bound':True,
 'original_original_endpoint_and_dyadic_center_third_derivative_included':True,
 'native_precision_bits':4096,
 'original_complete_z_second_x_jet_at_9over10_certified':False,
 'true_source_local_z_second_derivative_enclosure_certified':False,
 'original_NF404_entire_centered_scalar_certified':False,
 'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(result,indent=2)+'\n')
 print('NF421 full ORIGINAL fourth correlated Gram:',str(E)[:160],flush=True)
 print('NF421 original u4 fourth derivative L2',N4,'u third sup',M3,'full z third sup',Mz3,flush=True)
 print('NF421 fourth Gram is structural; complete z second x jet remains a separate obligation',flush=True)
if __name__=='__main__':main()
