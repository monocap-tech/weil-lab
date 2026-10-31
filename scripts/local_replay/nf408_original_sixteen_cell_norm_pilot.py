#!/usr/bin/env python3
"""NF408: provisional 16-cell, signed-principal-correlated original PHYSICAL L2 screen.

TRUE original source-native NF407 coefficients and all seven original prime
shifts. Original p=q+r full energy is exact accepted source; approximate
regularized z and signed <z,p> on each of EIGHT positive physical cells,
then reflect oddness. TWO outer resolutions. This is expressly NOT an
Arb/rational quadrature error certificate and cannot close W-ODD-NEG.
"""
import argparse,hashlib,json,sys,time
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp
from numpy.polynomial.legendre import leggauss
from nf408_original_compact_physical_action_pilot import Source,evaluate,read,rat
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 p.add_argument('--principal',default='notes/data/provisional/NF407_original_prime_jump_log_power_exact.json')
 p.add_argument('--center',default='notes/data/provisional/NF404_original_selected_pole_shear_exact.json')
 p.add_argument('--inner-nodes',type=int,default=14)
 p.add_argument('--inner-step',default='1/20')
 p.add_argument('--outer-a',type=int,default=2)
 p.add_argument('--outer-b',type=int,default=4)
 p.add_argument('--min-t',default='1/10000000000')
 p.add_argument('--dps',type=int,default=205)
 p.add_argument('--output',required=True)
 a=p.parse_args()
 assert a.outer_a>=2 and a.outer_b>a.outer_a
 assert a.dps>=195
 source,ssha=read(a.source)
 seams,seamsha=read(a.seams)
 principal,prsha=read(a.principal)
 center,csha=read(a.center)
 assert principal['original_nf406_seams_sha256']==seamsha
 assert principal['original_nf404_center_sha256']==csha
 assert len(source['original_exact_native_raw_selected_coefficients_mid_radius'])==242
 assert source['original_odd_physical_parity_native_reproduced'] is True
 assert source['original_exported_coefficients_are_4096bit_arb_not_float'] is True
 assert source['W_ODD_NEG']==source['RH']==seams['W_ODD_NEG']==seams['RH']==principal['W_ODD_NEG']==principal['RH']=='OPEN'
 assert seams['total_original_support_seam_knots_including_ends_and_zero']==17
 mp.mp.dps=a.dps
 s=Source(source)
 all_knots=seams['certified_ordered_knots']
 points=all_knots[8:]
 assert len(points)==9 and points[0]['label']=='0' and points[-1]['label']=='+B'
 brackets=[]
 for item in points:
  l=F(item['low']);u=F(item['high'])
  assert l<=u
  brackets.append(rat((l+u)/2))
 assert brackets[0]==0 and brackets[-1]==rat(B)
 assert all(brackets[i]<brackets[i+1] for i in range(8))
 principal_Elo,principal_Ehi=map(F,principal['original_known_q_plus_all_seven_prime_jumps_power_interval'])
 principal_E=(rat(principal_Elo)+rat(principal_Ehi))/2
 original_cap=rat(center['exact_sufficient_new_full_supported_centered_scalar_power_upper_target'])
 record=[]
 start=time.monotonic()
 for N in (a.outer_a,a.outer_b):
  xx,ww=leggauss(N)
  X=[mp.mpf(format(float(t),'.17g')) for t in xx]
  W=[mp.mpf(format(float(t),'.17g')) for t in ww]
  positive_z2=mp.mpf(0)
  positive_zp=mp.mpf(0)
  cells=[]
  for j in range(8):
   l=brackets[j];r=brackets[j+1]
   centerx=(l+r)/2;half=(r-l)/2
   z2=mp.mpf(0);zp=mp.mpf(0);samples=[]
   for node,weight in zip(X,W):
    x=centerx+half*node
    # Pass a 90-decimal original physical coordinate to parser F.
    # This is sufficient for the PROVISIONAL screen, not a rigorous
    # original seam position x interval.
    x_s=mp.nstr(x,90)
    e=evaluate(x_s,s,rat(a.inner_step),a.inner_nodes,rat(a.min_t))
    z=mp.mpf(e['original_continuous_z_x'])
    pp=mp.mpf(e['original_log_q_x'])+mp.mpf(e['original_prime_jump_r_x'])
    z2+=half*weight*z*z
    zp+=half*weight*z*pp
    samples.append({'x':mp.nstr(x,35),'z':mp.nstr(z,30),
                    'p':mp.nstr(pp,30),'original_source_u':e['original_u4_x'],
                    'regularized_g':e['original_centered_g_x']})
   positive_z2+=z2;positive_zp+=zp
   cells.append({'cell':j+1,'left':points[j]['label'],'right':points[j+1]['label'],
      'z2_positive_half_pilot':mp.nstr(z2,40),'z_p_positive_half_pilot':mp.nstr(zp,40),
      'samples':samples})
   print('NF408 ORIGINAL physical pilot resolution',N,'cell',j+1,'z2',mp.nstr(z2,10),'z p',mp.nstr(zp,10),flush=True)
  full_z2=2*positive_z2
  full_zp=2*positive_zp
  full_E=principal_E+full_z2+2*full_zp
  rec={
    'outer_nodes_per_original_positive_seam_cell':N,
    'original_physical_positive_cells':8,
    'original_physical_signed_total_cells':16,
    'original_source_full_point_evaluations':8*N,
    'original_certified_principal_p_power_midpoint_reference':mp.nstr(principal_E,45),
    'original_uncertified_z_power':mp.nstr(full_z2,45),
    'original_uncertified_signed_z_principal_cross':mp.nstr(full_zp,45),
    'original_uncertified_reconstructed_full_centered_physical_power':mp.nstr(full_E,45),
    'original_nf404_centered_sufficient_cap':mp.nstr(original_cap,45),
    'original_uncertified_full_power_over_cap_ratio':mp.nstr(full_E/original_cap,30),
    'original_uncertified_screen_above_cap':bool(full_E>original_cap),
    'cells':cells
  }
  record.append(rec)
  # Local unpublished artifacts: no claim of source certificate.
  print('NF408 physical pilot *UNCERTIFIED* outer',N,'E',mp.nstr(full_E,28),'target',mp.nstr(original_cap,28),flush=True)
 a0,b0=[mp.mpf(x['original_uncertified_reconstructed_full_centered_physical_power']) for x in record]
 out={
   'pass':'NF408',
   'standing':'UNCERTIFIED ORIGINAL FULL SUPPORTED CENTERED 16-CELL GAUSS SCREEN; SOURCE MIDPOINT TRUE, QUADRATURE ERROR NOT BOUNDED',
   'original_nf407_true_native_coefficient_sha256':ssha,
   'original_nf406_original_seam_sha256':seamsha,
   'original_nf407_exact_principal_sha256':prsha,
   'original_nf404_center_sha256':csha,
   'working_decimal_digits':a.dps,
   'inner_gauss_nodes_per_interval':a.inner_nodes,
   'inner_approximate_segment_max_width':a.inner_step,
   'inner_small_t_omitted_interval':a.min_t,
   'outer_source_positive_cells':8,
   'original_all_seven_prime_support_seams_retained':True,
   'original_source_native_arb_radius_propagated_into_quadrature':False,
   'original_outer_gauss_approximate_nodes_and_weights_UNCERTIFIED':True,
   'original_inner_gauss_approximate_nodes_and_weights_UNCERTIFIED':True,
   'pilot_resolutions':record,
   'original_two_outer_resolution_difference_absolute':mp.nstr(abs(a0-b0),45),
   'original_source_accurate_full_integral_error_enclosed':False,
   'original_complete_centered_physical_L2_upper_CERTIFIED':False,
   'original_fourth_J242_complement_lowband_upper_CLOSED':False,
   'new_signed_kernel_cells':0,'W_ODD_NEG':'OPEN','RH':'OPEN',
   'elapsed_seconds':round(time.monotonic()-start,1)
 }
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF408 both exploratory original 16-cell physical full-norm results; CERTIFICATE NOT CLAIMED',flush=True)
if __name__=='__main__':main()
