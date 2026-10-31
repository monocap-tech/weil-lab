#!/usr/bin/env python3
"""NF416 independent Fraction replay of full original I0 error ledger and exact z recomposition.

Reads preexisting native files; no Arb integrator or Gauss nodes.
Checks original SHA custody, exact rational original source and H/K
analytic tails, and exact signed NF414 finite + NF415 I1 + NF416 I0.
Does NOT certify cellwide norm or RH.
"""
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def dyad(v):
 n,e=int(v[0]),int(v[1])
 return F(n*2**e) if e>=0 else F(n,2**(-e))
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
 ap.add_argument("--nf413",default="notes/data/provisional/NF413_original_full_246_source_curvature_native.json")
 ap.add_argument("--nf414",default="notes/data/provisional/NF414_original_hotspot_finite_continuous_native.json")
 ap.add_argument("--nf415",default="notes/data/provisional/NF415_original_cell6_I1_correlated_taylor_native.json")
 ap.add_argument("--nf416",default="notes/data/provisional/NF416_original_cell6_full_I0_and_z_point_native.json")
 ap.add_argument("--output",required=True)
 a=ap.parse_args()
 s,ssha=read(a.source);g,gsha=read(a.nf413)
 f,fsha=read(a.nf414);j,jsha=read(a.nf415);v,vsha=read(a.nf416)
 assert ssha==g['original_nf407_full_native_source_sha256']==f['original_nf407_source_sha256']
 assert ssha==j['original_nf407_source_sha256']==v['original_nf407_source_sha256']
 assert [v['original_nf413_native_full_curvature_sha256'],v['original_nf414_original_finite_seven_primes_sha256'],
         v['original_nf415_full_I1_sha256']]==[gsha,fsha,jsha]
 assert len(s['original_selected_generator_node_orders'])==242
 assert len(s['original_source_critical_sine_frequencies'])==32
 assert len(s['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert v['original_I0_t_interval']==['0','2/5']
 assert v['original_physical_cell']==6 and v['original_physical_x']=='9/10'
 assert v['original_zero_singularity_removed_by_H_t_equals_tK_t']
 assert v['entire_original_source_symmetric_plus_and_minus_translation_preserved']
 assert v['tiny_t_source_Taylor_degree']==530
 assert v['tiny_t_analytic_H_Taylor_degree']==60
 assert v['source_taylor_degree_large']==300
 assert v['kernel_taylor_degree_large']==160
 assert v['large_panel_count']==38
 fmax=max([F(x[0]) for x in s['original_selected_generator_node_orders'] if x[0]!='pole']+
          [F(x) for x in s['original_source_critical_sine_frequencies']])
 assert F(v['original_source_all_selected_frequencies_max_exact'])==fmax
 assert F(882)<fmax<F(883)
 U=F(j['analytic_exact_source_raw_abs_U_exact'])
 # Full source exact Uraw from same original 242+4 grouped by frequency:
 nodes={}
 pole=F(0)
 def add(x,k,q):nodes[(x,k)]=nodes.get((x,k),F(0))+q
 for (freq,k),(mid,rad) in zip(s['original_selected_generator_node_orders'],
                                s['original_exact_native_raw_selected_coefficients_mid_radius']):
  if freq=='pole':pole+=dyad(mid)
  else:add(F(freq),k,dyad(mid))
 for (mid,rad),shape in zip(s['original_exact_native_original_four_critical_coefficients_mid_radius'],
                           s['original_source_critical_sines_and_pole_coefficients']):
  alpha=dyad(mid)
  for freq,coef in zip(s['original_source_critical_sine_frequencies'],shape['sine_coefficients']):
   add(F(freq),0,alpha*F(coef))
  pole+=alpha*F(shape['sinh_coefficient'])
 original_U=sum((abs(q)*F(11,10)**k for (freq,k),q in nodes.items()),abs(pole))
 assert U==original_U and U<10**160
 Rsmall=F(8*3**62)*U*F(62)**518/math.factorial(518)
 RH=F(6)*F(1,50)**61/(1-F(1,50))
 E_small=F(6)*Rsmall/531+F(1,50)*F(6)*RH
 Rlarge=F(3**16)*U*F(16)**288/math.factorial(288)
 RK=F(81)*F(2,5)**161/F(3,5)
 E_large=(F(2,5)-F(1,50))*(100*Rlarge+RK*(F(1030)+Rlarge))
 S2=F(g['native_second_derivative_source_coefficient_radii_uniform_exact'])
 E_native=S2*F(2,5)**2/8
 assert S2<F(1,10**735)
 for name,check in [
 ("original_tiny_t_source_remainder_upper_exact",Rsmall),
 ("original_tiny_t_H_remainder_upper_exact",RH),
 ("original_tiny_t_integrated_truncation_upper_exact",E_small),
 ("original_large_t_source_taylor_remainder_upper_exact",Rlarge),
 ("original_large_t_kernel_taylor_remainder_upper_exact",RK),
 ("original_large_t_integrated_truncation_upper_exact",E_large),
 ("original_I0_native_source_error_paid_exact",E_native),
 ("original_I0_total_truncation_and_source_error_upper_exact",E_small+E_large+E_native)]:
  assert F(v[name])==check,(name,"mismatched exact source error contract")
 i0=[F(x) for x in v['original_I0_full_0_to_2over5_rational_outward_interval']]
 fi=[F(x) for x in f['hotspot_points'][1]['original_z_finite_known_part_source_paid_rational_interval']]
 i1=[F(x) for x in j['true_original_cell6_I1_rational_outward_interval']]
 z=[fi[i]+i1[i]+i0[i] for i in (0,1)]
 assert z==[F(x) for x in v['original_true_full_z_cell6_at_x9over10_outward_interval']]
 assert z[0]<z[1] and z[0]>0
 assert i0[1]-i0[0]==F(v['original_I0_interval_width_exact'])
 assert z[1]-z[0]==F(v['original_true_full_z_cell6_pointwise_width_exact'])
 assert z[1]-z[0]<F(1,10**55)
 assert v['complete_original_z_pointwise_certified']
 assert not v['complete_original_z_on_full_cell6_certified']
 assert not v['original_complete_centered_scalar_certified']
 assert not v['NF404_acceptance_gate_decided']
 assert v['W_ODD_NEG']==v['RH']=='OPEN'
 report=dict(pass_="NF416-independent",standing="INDEPENDENT EXACT RATIONAL SOURCE-RECONSTRUCTED ERROR LEDGER AND ORIGINAL FULL POINTWISE z RECOMPOSITION PASS",
 original_source_sha256=ssha,nf413_sha256=gsha,nf414_sha256=fsha,
 nf415_sha256=jsha,nf416_sha256=vsha,
 original_source_generators=246,
 original_source_max_frequency_exact=str(fmax),
 original_Uraw_exact_recomputed=True,
 tiny_t_source_analytic_tail_replayed=True,
 regular_t_source_and_K_analytic_tails_replayed=True,
 true_source_second_derivative_coefficient_radius_replayed=True,
 original_full_I0_outward_interval_recomposed_with_original_NF414_NF415=True,
 original_complete_z_at_x9over10_pointwise_positive_certified=True,
 original_complete_z_pointwise_width_under_1e55=True,
 original_entire_cellwise_z_certified=False,
 original_NF404_full_scalar_certified=False,
 W_ODD_NEG="OPEN",RH="OPEN")
 report["pass"]=report.pop("pass_")
 dst=Path(a.output);dst.parent.mkdir(parents=True,exist_ok=True)
 dst.write_text(json.dumps(report,indent=2)+"\n")
 print("NF416 independent exact source replay PASS, complete original z(9/10) positive pointwise")
 print("NF416 cellwide NF404 W-ODD-NEG RH OPEN")
if __name__=="__main__":main()
