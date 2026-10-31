#!/usr/bin/env python3
"""NF406: exact original physical endpoint logarithm and its L2 norm.

Analytic theorem (source-specific, inherited m(D) strong realization):
For u odd, C^2 on [-B,B], zero extended, with nonzero u(B)=v,
A u(x)=(v/2) sign(x)*log(B/(B-|x|))+h_arch(x), with bounded
h_arch near +/-B. Finite prime translations are piecewise bounded.
The exact subtracted q has ||q||_I^2=B*v^2.
This script certifies the original u4 endpoint and q power from actual
SHA-pinned NF405 original source intervals, and original NF404 selected
pole-centered power. It does NOT integrate the regular part or cross.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)

B=F(11,10)
N401='644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515'
N374='a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559'
N375='03c709571046d3f09307614aaded9749f5a15ba1'

def read(p):
 b=Path(p).read_bytes()
 return json.loads(b),hashlib.sha256(b).hexdigest()
def span(v):
 assert len(v)==2
 a,b=map(F,v)
 assert a<=b
 return a,b

def main():
 p=argparse.ArgumentParser()
 p.add_argument('--nf405-endpoint',default='notes/data/provisional/NF405_original_endpoint_extracted_tail_exact.json')
 p.add_argument('--nf405-physical',default='notes/data/provisional/NF405_original_compact_physical_kernel_exact.json')
 p.add_argument('--nf404-center',default='notes/data/provisional/NF404_original_selected_pole_shear_exact.json')
 p.add_argument('--nf374',default='notes/data/provisional/NF374_original_correlated_curvature_native.json')
 p.add_argument('--nf401',default='notes/data/provisional/NF401_original_242D_selected_column_source_native.json')
 p.add_argument('--output',required=True)
 a=p.parse_args()
 endpoint,esha=read(a.nf405_endpoint)
 physical,psha=read(a.nf405_physical)
 center,csha=read(a.nf404_center)
 nf374,nsha=read(a.nf374)
 nf401,sha401=read(a.nf401)
 assert sha401==center['original_nf401_selected_native_sha256']==N401
 assert nsha==endpoint['nf374_native_sha256']==N374
 assert endpoint['nf404_centering_sha256']==csha
 assert physical['nf405_original_endpoint_extracted_source_sha256']==esha
 assert physical['nf404_original_pole_shear_source_sha256']==csha
 assert physical['nf401_original_selected_source_sha256']==sha401
 assert physical['original_compact_translation_integral_upper']=='22/5'
 assert physical['actual_original_prime_power_shifts']==[2,3,4,5,7,8,9]
 assert nf374['working_precision_bits']==4096
 assert endpoint['original_source_exact_half_budget_with_endpoint_extraction_pass'] is True
 assert center['actual_original_full_supported_centered_scalar_integrated'] is False
 assert all(x['W_ODD_NEG']==x['RH']=='OPEN' for x in (endpoint,physical,center,nf374,nf401))

 v_lo,v_hi=span(endpoint['original_actual_matched_u4_endpoint_interval'])
 assert v_lo<v_hi<0
 # Original true signed endpoint, not an absolute-value proxy:
 # q(x) = v/2 sign(x) log[B/(B-|x|)] for |x|<B.
 # Two sides; integral_0^B log^2[B/(B-x)] dx=2 B.
 # Therefore ||q||²= B v² EXACTLY (no quadrature approximation).
 q_lo=B*v_hi*v_hi
 q_hi=B*v_lo*v_lo
 assert F(150,10**24) < q_lo < q_hi < F(151,10**24)
 E_lo=F(center['original_selected_after_pole_shear_power_lower_exact'])
 E_hi=F(center['original_selected_after_pole_shear_power_upper_exact'])
 gamma2=F(center['exact_source_original_full_complement_power_budget'])
 full_cap=F(center['exact_sufficient_new_full_supported_centered_scalar_power_upper_target'])
 assert full_cap==E_lo+gamma2
 assert E_lo>F(33,10**12)**2 # ||g||>=||P_J g||>3.3e-11
 assert q_hi<F(123,10**13)**2 # ||q||<1.23e-11
 regular_lower=F(207,10**13)  # ||g-q||>2.07e-11
 assert E_lo>(regular_lower+F(123,10**13))**2
 assert F(0)<q_lo<q_hi<full_cap
 # Source output MUST not quietly identify singular q with the physical
 # entire arch response or use it as a positive power component.
 out={
  'pass':'NF406',
  'standing':'SOURCE-CERTIFIED ORIGINAL NONZERO PHYSICAL DIGAMMA LOG ENDPOINT; REGULAR RESPONSE AND CROSS OPEN',
  'original_nf401_native_sha256':sha401,
  'original_nf374_native_sha256':nsha,
  'original_nf405_endpoint_exact_sha256':esha,
  'original_nf405_compact_physical_exact_sha256':psha,
  'original_nf404_pole_shear_exact_sha256':csha,
  'original_support_half_width':str(B),
  'original_u4_endpoint_outward':[str(v_lo),str(v_hi)],
  'strict_original_u4_endpoint_nonzero':True,
  'original_signed_log_coefficient_outward':[str(v_lo/2),str(v_hi/2)],
  'original_true_physical_log_model':'q(x)=u4(B)/2*sign(x)*log(B/(B-|x|)), |x|<B',
  'original_arch_action_boundary_asymptotic':'A u4(B-d)=u4(B)/2*log(B/d)+O(1) as d->0+, prime translation terms bounded piecewise',
  'original_exact_log_model_squared_norm_identity':'||q||^2=B*u4(B)^2',
  'original_exact_log_model_squared_norm_lower':str(q_lo),
  'original_exact_log_model_squared_norm_upper':str(q_hi),
  'strict_source_log_power_bracket':'150/10^24 < ||q||^2 < 151/10^24',
  'original_selected_centered_power_lower':str(E_lo),
  'original_selected_centered_power_upper':str(E_hi),
  'actual_centered_full_power_sufficient_upper_target':str(full_cap),
  'original_exterior_power_budget':str(gamma2),
  'strict_actual_regular_part_norm_lower':str(regular_lower),
  'actual_regular_part_norm_lower_reason':'||g-q||>=||g||-||q||>=||P_Jg||-||q||>2.07e-11',
  'actual_complete_centered_physical_scalar_identity':'||g||^2=||g-q||^2+2<g-q,q>+||q||^2, g=1_I(m(D)u4-a*sinh(x/2))',
  'source_original_prime_translation_seams':'x=+/-B -/+ log(n), n in 2,3,4,5,7,8,9',
  'source_original_arch_translation_seams':'t=2(B +/- x)',
  'physical_endpoint_log_subtraction_required':True,
  'original_complete_regular_part_and_cross_integrated':False,
  'original_full_supported_centered_scalar_upper_computed':False,
  'original_lowband_J242_perp_upper_computed':False,
  'original_domain_general_audit':'OPEN',
  'new_signed_kernel_cells':0,
  'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF406 original actual u4(B) nonzero exact source PASS')
 print('NF406 original physical logarithm q squared norm in (1.50e-22,1.51e-22): PASS')
 print('NF406 original regular physical component norm >2.07e-11: PASS')
 print('NF406 positive centered full supported scalar STILL UNMEASURED')
if __name__=='__main__':main()
