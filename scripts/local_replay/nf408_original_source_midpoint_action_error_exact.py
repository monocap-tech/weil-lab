#!/usr/bin/env python3
"""NF408 source-native EXACT 4096-bit interval-COEFFICIENT action error bound.

For original supported odd u4, native NF407 coefficient enclosure -> exact
dyadic midpoint uhat, pointwise value/derivative errors S,D. Uses the
original accepted signed highband |m(xi)|<=17+ln |xi| (|xi|>=1).
The lowband |m|<=800 follows the quarter-digamma integral, seven
original prime powers, and elementary bounds. Plancherel plus physical
IBP gives ||m(D)(u4-uhat)||_L2(I) <3000(S+D).
This is ONLY a source-input uncertainty certificate, NOT quadrature.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)
NF374='a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559'
NF401='644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515'
def load(path):
 b=Path(path).read_bytes()
 return json.loads(b),hashlib.sha256(b).hexdigest()
def dyad(t):
 n,e=int(t[0]),int(t[1])
 return F(n*2**e) if e>=0 else F(n,2**(-e))
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--native',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--nf405',default='notes/data/provisional/NF405_original_compact_physical_kernel_exact.json')
 p.add_argument('--output',required=True)
 a=p.parse_args()
 n,nsha=load(a.native)
 prev,prevsha=load(a.nf405)
 assert n['original_nf374_native_sha256']==NF374
 assert prev['nf401_original_selected_source_sha256']==NF401
 assert n['original_dimension']==242
 assert len(n['original_exact_native_raw_selected_coefficients_mid_radius'])==242
 assert len(n['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert n['original_exported_coefficients_are_4096bit_arb_not_float'] is True
 assert n['original_u4_endpoint_matches_nf405_exact_signed_bounds'] is True
 assert all(x['W_ODD_NEG']==x['RH']=='OPEN' for x in (n,prev))
 S=D=F(0)
 for (c,k),coeff in zip(n['original_selected_generator_node_orders'],n['original_exact_native_raw_selected_coefficients_mid_radius']):
  radius=abs(dyad(coeff[1]))
  if c=='pole':
   assert k is None
   S+=radius;D+=radius  # sinh(.55)<1, cosh(.55)/2<1
  else:
   assert k>=0
   freq=abs(F(c))
   S+=radius*B**k
   D+=radius*((k*B**(k-1) if k else 0)+7*freq*B**k)
 for probe,coeff in zip(n['original_source_critical_sines_and_pole_coefficients'],n['original_exact_native_original_four_critical_coefficients_mid_radius']):
  rad=abs(dyad(coeff[1]))
  sine=sum((abs(F(x)) for x in probe['sine_coefficients']),F(0))
  dx=sum((7*abs(F(x))*abs(F(c)) for x,c in zip(probe['sine_coefficients'],n['original_source_critical_sine_frequencies'])),F(0))
  pole=abs(F(probe['sinh_coefficient']))
  S+=rad*(sine+pole)
  D+=rad*(dx+pole)
 assert 0<S<F(1,10**750)
 assert 0<D<F(1,10**750)
 # Verified elementary lowband m bound:
 # psi(1/4)=-EulerGamma-pi/2-3 log2, and abs(psi(1/4)-ln pi)<10
 # K(t)=sum_{j>=0} exp(-(j+1/4)t). For |xi|<=1,
 # 1-cos(pi xi t) <=pi²t²/2 and
 # int K(t)t²dt=2sum_j(j+1/4)^-3 <=144.
 # Thus arch diff <= pi² sum_j <=10*(64+8)=720.
 # all seven prime cos sum absolute <=2*7*3=42.
 # Entire original |m(xi)| <10+720+42=772<800.
 assert F(10)+F(10)*(64+8)+F(2*7*3)<800
 # For |xi|<=1, |hat du|<=2B*S, m<800; Parseval L2 low:
 # sqrt(2)*800*2B*S<2500*S.
 assert F(2)*(800*2*B)**2 <2500**2
 # For |xi|>=1, |hat du| <= (2S+2B D)/(2*pi*|xi|),
 # 2*pi>6. Signed original |m(xi)|<=17+ln xi.
 # int_1^infty (17+ln xi)^2/xi² dx=17²+34+2=325,
 # both signs high norm <=sqrt(650)/6 * (2S+2B D)
 # <5*(2S+2B D)<11(S+D).
 assert 650<F(5*6)**2
 assert 5*2*B==11
 physical_action_error_upper=3000*(S+D)
 assert 2500*S+11*(S+D)<physical_action_error_upper
 assert physical_action_error_upper<F(1,10**745)
 out={
   'pass':'NF408',
   'standing':'EXACT SOURCE-NATIVE COEFFICIENT-UNCERTAINTY ORIGINAL FULL m(D) ACTION L2 UPPER ONLY; QUADRATURE UNBOUNDED',
   'original_nf407_coefficient_native_sha256':nsha,
   'original_nf405_compact_kernel_exact_sha256':prevsha,
   'original_native_coefficient_value_error_uniform_S':str(S),
   'original_native_coefficient_derivative_error_uniform_D':str(D),
   'original_supported_true_source_minus_native_midpoint_uniform_bound':str(S),
   'original_supported_true_source_derivative_minus_native_midpoint_uniform_bound':str(D),
   'original_complete_original_signed_lowband_m_symbol_upper_strict':800,
   'original_complete_original_signed_highband_bound':'|m(xi)| <=17+ln|xi| for |xi|>=1, original NF375 inherited SM41',
   'original_fourier_tail_primitive_integral_exact':'int_1^infty (17+ln x)^2/x^2 dx=325',
   'original_source_native_radius_full_physical_m_action_L2_error_upper':str(physical_action_error_upper),
   'strict_source_native_radius_full_action_error_below':'1e-745',
   'original_centered_physical_quadrature_error_enclosed':False,
   'original_double_gauss_pilot_input_rounding_error_enclosed':False,
   'original_full_supported_centered_scalar_upper_computed':False,
   'original_regularized_z_and_signed_cross_integrated':False,
   'new_signed_kernel_cells':0,
   'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 target=Path(a.output);target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps(out,indent=2)+'\n')
 print('NF408 source-native original physical action L2 midpoint COEFFICIENT uncertainty <1e-745 PASS')
 print('NF408 physical arch integral/outer L2 quadrature error NOT bounded')
if __name__=='__main__':main()
