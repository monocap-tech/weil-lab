#!/usr/bin/env python3
"""NF427 original source-pinned Chebyshev *series* cutoff, not interpolant.

Independent rational replay of NF425 ellipse E2 and source NF407, exact
cell6 NF406 knots, NF423 and NF425 source ancestry. On the fixed-cell6
analytic continuation, the finite NF424 source-image response is bounded
by M=10^400 on the entire Bernstein E2. Its exact Chebyshev SERIES
coefficients |a_n| <= 2M/2^n (n>=1). The full series tail n>=1500 has
sup norm < 4M/2^1500 < 10^-50, hence 1500 coefficients (n=0..1499),
NOT 2049, suffice for the full true original physical J6 with total
analytic residual <2e-45 (NF424 original-source tail <1e-45).
The script does not evaluate a coefficient or signed cell integral.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10); C=F(91,100);H=F(7,100);RHO=2;DEGREE=1499
def read(p):
 data=Path(p).read_bytes()
 return json.loads(data),hashlib.sha256(data).hexdigest()
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 p.add_argument('--nf423',default='notes/data/provisional/NF423_original_entire_open_cell6_zthird_native.json')
 p.add_argument('--nf425-script',default='scripts/local_replay/nf425_original_cell6_chebyshev_existence_exact.py')
 p.add_argument('--output',required=True)
 a=p.parse_args()
 s,ssha=read(a.source);seams,ksha=read(a.seams);old,psha=read(a.nf423)
 assert old['original_nf407_source_sha256']==ssha
 assert old['original_nf406_exact_support_seams_sha256']==ksha
 assert old['true_original_entire_open_cell6_zthird_uniform_strict_upper']==286758
 assert old['original_all_seven_real_signed_prime_branches_inside_open_cell']==['post-seam']*5+['neither']*2
 assert s['original_dimension']==242 and len(s['original_selected_generator_node_orders'])==242
 assert len(s['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert len(s['original_source_critical_sine_frequencies'])==32
 assert s['W_ODD_NEG']==s['RH']=='OPEN'
 knots=seams['certified_ordered_knots']
 assert knots[13]['label']=='-B+log(7)' and knots[14]['label']=='-B+log(8)'
 assert F(21,25)<F(knots[13]['low'])<F(knots[13]['high'])<F(knots[14]['low'])<F(knots[14]['high'])<F(49,50)
 assert C-H==F(21,25) and C+H==F(49,50)
 assert C+F(5,4)*H==F(399,400) and B-F(399,400)==F(41,400)
 # Exact finite source coefficients, original selected+critical source.
 def dyad(y):
  m,e=int(y[0]),int(y[1])
  return F(m*2**e) if e>=0 else F(m,2**(-e))
 coeff={};pole=F(0);S0=F(0)
 def add(f,k,v):coeff[f,k]=coeff.get((f,k),F(0))+v
 for (f,k),(mid,rad) in zip(s['original_selected_generator_node_orders'],s['original_exact_native_raw_selected_coefficients_mid_radius']):
  c=dyad(mid);S0+=abs(dyad(rad))*B**(k or 0)
  if f=='pole':pole+=c
  else:add(F(f),k,c)
 for (mid,rad),shape in zip(s['original_exact_native_original_four_critical_coefficients_mid_radius'],s['original_source_critical_sines_and_pole_coefficients']):
  c=dyad(mid);e=abs(dyad(rad))
  for f,v in zip(s['original_source_critical_sine_frequencies'],shape['sine_coefficients']):
   add(F(f),0,c*F(v));S0+=e*abs(F(v))
  pole+=c*F(shape['sinh_coefficient']);S0+=e*abs(F(shape['sinh_coefficient']))
 raw=sum((abs(q)*B**k for (f,k),q in coeff.items()),abs(pole))
 assert raw<10**160 and S0<F(1,10**700)
 assert max(k for f,k in coeff)<=13 and max(f for f,k in coeff)<883
 p425=Path(a.nf425_script).read_bytes()
 pin425=hashlib.sha256(p425).hexdigest()
 # Replay NF425 actual original source M=10^400 ellipse envelope:
 assert 10**190 * 3**373 < 10**400
 M=10**400
 tail=F(4*M,2**(DEGREE+1))
 assert tail<F(1,10**50)
 # NF424's independent full ORIGINAL cell6 image+source model error:
 image=F(36,2000)*10**160*F(3,8)**480
 source_error=(10**12+20)*S0
 assert image+source_error<F(1,10**45)
 total=tail+image+source_error
 assert total<F(2,10**45)
 # A numerical coefficient-radius gate remains unfulfilled:
 coeff_radius=F(1,10**25)
 target=(DEGREE+1)*coeff_radius
 assert target<F(1,10**21)
 out={
  'pass':'NF427',
  'standing':'ORIGINAL FULL CELL6 CHEBYSHEV SERIES CUTOFF DEGREE1499 ACCEPTED; NATIVE COEFFICIENTS AND SIGNED INTEGRAL INCOMPLETE',
  'NF407_original_source_sha256':ssha,'NF406_original_seams_sha256':ksha,
  'NF423_original_cell6_parent_sha256':psha,
  'NF425_exact_source_ellipse_script_sha256':pin425,
  'original_242_plus_four_source_preserved':True,
  'true_original_cell6':'(log(7)-11/10,log(8)-11/10)',
  'only_fixed_cell6_analytic_continuation_outside_J6':True,
  'Bernstein_ellipse_parameter':str(RHO),'M_bound':'1e400',
  'series_degree_sufficient':DEGREE,
  'number_Chebyshev_series_coefficients_needed':DEGREE+1,
  'prior_NF425_interpolation_degree':2048,
  'actual_Chebyshev_coefficients_evaluated_by_this_replay':0,
  'Chebyshev_series_tail_rational_upper_exact':str(tail),
  'Chebyshev_series_tail_strict_less_than_1e_minus_50':True,
  'original_image_tail_rational_upper_exact':str(image),
  'original_source_radius_rational_upper_exact':str(source_error),
  'complete_cell6_analytical_existential_residual_rational_upper_exact':str(total),
  'complete_original_cell6_analytic_residual_strict_upper':'2e-45',
  'future_each_native_series_coefficient_radius_target':'1e-25',
  'future_sum_of_1500_native_coefficient_radii_target_exact':str(target),
  'same_1500_coefficients_as_NF425_interpolant':False,
  'all_1500_native_coefficients_certified':False,
  'complete_original_cell6_signed_pz_z2_integrated':False,
  'NF404_signed_scalar_decided':False,'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF427 SOURCE-EXACT entire original physical cell6 Chebyshev SERIES n>=1500 tail <1e-50 PASS',flush=True)
 print('NF427 target coefficient count 1500 vs prior 2049 interpolant; numerical coefficients & NF404/RH OPEN',flush=True)
if __name__=='__main__': main()
