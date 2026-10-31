#!/usr/bin/env python3
"""NF417 independent pure Fraction reconstruction of original 246 source error ledgers.
No numeric Arb, no Gauss. Both original NF417 cell3 and cell7 native
point receipts must exist. Rebuild complete signed source raw triangle
and original coefficient radii from the exact NF407 dyadic export.
Recompute all positive exact analytic remainder charges and z recomposition.
"""
import argparse, hashlib, json, math, sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def dyad(x):
 n,e=int(x[0]),int(x[1]);return F(n*2**e) if e>=0 else F(n,2**(-e))
def source_contract(s):
 src={};pole=F(0);S0=F(0)
 def add(f,k,q):src[(f,k)]=src.get((f,k),F(0))+q
 for (f,k),(m,r) in zip(s['original_selected_generator_node_orders'],s['original_exact_native_raw_selected_coefficients_mid_radius']):
  if f=='pole':pole+=dyad(m);S0+=abs(dyad(r))
  else:
   add(F(f),k,dyad(m));S0+=abs(dyad(r))*B**k
 for (m,r),shape in zip(s['original_exact_native_original_four_critical_coefficients_mid_radius'],s['original_source_critical_sines_and_pole_coefficients']):
  val=dyad(m);rad=abs(dyad(r))
  for f,coef in zip(s['original_source_critical_sine_frequencies'],shape['sine_coefficients']):
   q=F(coef);add(F(f),0,val*q);S0+=rad*abs(q)
  q=F(shape['sinh_coefficient']);pole+=val*q;S0+=rad*abs(q)
 assert len(s['original_selected_generator_node_orders'])==242
 assert len(s['original_source_critical_sines_and_pole_coefficients'])==4
 assert len(s['original_source_critical_sine_frequencies'])==32
 freqs=[f for f,k in src]
 assert F(882)<max(freqs)<F(883)
 U=sum((abs(q)*B**k for (f,k),q in src.items()),abs(pole))
 assert U<F(10)**160 and S0<F(1,10**700)
 return U,S0,max(freqs)
def replay(j,cell,parents,contract):
 U,S0,fmax=contract;srcsha,gsha,fsha=parents['shas']
 assert j['pass']=='NF417' and j['cell']==cell
 assert j['x']=={3:'7/20',7:'26/25'}[cell]
 assert j['nf407_original_source_sha256']==srcsha
 assert j['nf413_curvature_sha256']==gsha
 assert j['nf414_seven_signed_prime_finite_sha256']==fsha
 x=F(j['x']);t1=2*(B-x);t2=2*(B+x);tau=F(1,50);step=F(1,100)
 assert j['original_I0_true_t_interval']==['0',str(t1)]
 assert j['original_I1_true_t_interval']==[str(t1),str(t2)]
 assert j['I0_regular_panels']==int((t1-tau)/step)
 assert j['I1_panels']==int((t2-t1)/step)
 assert F(j['original_raw_source_triangle_U'])==U
 assert F(j['original_coefficient_source_S0'])==S0
 assert F(j['exact_original_max_frequency'])==fmax
 g=parents['g'];f=parents['f']
 S2=F(g['native_second_derivative_source_coefficient_radii_uniform_exact'])
 assert S2==F(j['original_coefficient_source_second_derivative_S2'])
 Rs=F(8*3**62)*U*F(62)**518/math.factorial(518)
 RH=F(6)*tau**61/(1-tau)
 E0small=6*Rs/531+tau*6*RH
 Rsource=F(3**16)*U*F(16)**288/math.factorial(288)
 RK0=F(81)*F(2,5)**161/F(3,5)
 E0large=(t1-tau)*(100*Rsource+RK0*(F(1030)+Rsource))
 E0coeff=S2*t1*t1/8
 eta=F(1,100)/t1
 RK1=81*eta**49/(1-eta)
 E1=(t2-t1)*(F(2)/t1*Rsource+RK1*(520+Rsource))
 E1coeff=2*(t2/t1-1)*S0
 items={
 'I0_tiny_source_tail':Rs,'I0_tiny_H_tail':RH,
 'I0_tiny_integrated_error':E0small,
 'I0_regular_source_tail':Rsource,
 'I0_regular_kernel_tail':RK0,
 'I0_regular_integrated_error':E0large,
 'I0_source_native_coefficient_error':E0coeff,
 'I0_total_error':E0small+E0large+E0coeff,
 'I1_kernel_complex_disk_ratio':eta,'I1_kernel_tail':RK1,
 'I1_source_tail':Rsource,'I1_integrated_error':E1,
 'I1_source_native_coefficient_error':E1coeff}
 for name,v in items.items():assert F(j[name])==v,('RATIONAL ERROR REPLAY FAILURE',cell,name)
 i0=[F(z) for z in j['original_true_I0_outward_rational_interval']]
 i1=[F(z) for z in j['original_true_I1_outward_rational_interval']]
 exact_finite=[F(z) for z in f['hotspot_points'][[3,6,7].index(cell)]['original_z_finite_known_part_source_paid_rational_interval']]
 assert exact_finite==[F(z) for z in j['original_NF414_finite_z_known_outward_rational_interval']]
 complete=[exact_finite[k]+i0[k]+i1[k] for k in (0,1)]
 assert complete==[F(z) for z in j['original_true_complete_z_pointwise_rational_interval']]
 assert complete[0]<complete[1]
 assert F(j['original_true_I0_width_exact'])==i0[1]-i0[0]
 assert F(j['original_true_I1_width_exact'])==i1[1]-i1[0]
 assert F(j['original_true_complete_z_pointwise_width_exact'])==complete[1]-complete[0]
 assert complete[1]-complete[0]<F(1,10**38)
 assert j['true_original_complete_z_pointwise_certified']
 assert not j['entire_original_cell_z_certified']
 assert not j['original_NF404_whole_scalar_certified']
 assert j['W_ODD_NEG']==j['RH']=='OPEN'
 return {'cell':cell,'x':str(x),'I0_panels':j['I0_regular_panels'],
         'I1_panels':j['I1_panels'],
         'source_246_exact_coefficient_radii_paid':True,
         'complete_analytic_source_and_kernel_tails_exactly_recomputed':True,
         'true_z_source_original_NF414_I0_I1_exactly_recomposed':True,
         'pointwise_z_sign':('strictly-positive' if complete[0]>0 else 'strictly-negative' if complete[1]<0 else 'unresolved'),
         'complete_original_z_pointwise_certified':True,
         'original_full_cell_L2_certified':False}
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--nf413',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 ap.add_argument('--nf414',default='notes/data/provisional/NF414_original_hotspot_finite_continuous_native.json')
 ap.add_argument('--receipt3',default='notes/data/provisional/NF417_original_cell3_full_z_pointwise_native.json')
 ap.add_argument('--receipt7',default='notes/data/provisional/NF417_original_cell7_full_z_pointwise_native.json')
 ap.add_argument('--output',required=True)
 a=ap.parse_args()
 s,ssha=read(a.source);g,gsha=read(a.nf413);f,fsha=read(a.nf414)
 assert ssha==g['original_nf407_full_native_source_sha256']==f['original_nf407_source_sha256']
 contract=source_contract(s)
 p={'g':g,'f':f,'shas':(ssha,gsha,fsha)}
 reports=[]
 parent_sha={}
 for cell,path in [(3,a.receipt3),(7,a.receipt7)]:
  obj,sha=read(path);parent_sha[cell]=sha
  reports.append(replay(obj,cell,p,contract))
 out={'pass':'NF417-independent','standing':'FULL 246-source two-hotspot Fraction exact analytic error and signed z replay PASS',
      'nf407_source_sha256':ssha,'nf413_sha256':gsha,'nf414_sha256':fsha,
      'original_true_source_246_generator_count':246,
      'original_NF417_cell3_receipt_sha256':parent_sha[3],
      'original_NF417_cell7_receipt_sha256':parent_sha[7],
      'hotspot_independent_reports':reports,
      'no_Arb_or_Gauss_used_in_independent_error_replay':True,
      'whole_original_z_cellwise_certified':False,
      'NF404_full_centered_scalar_certified':False,
      'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF417 independent source 246 exact rational error and original cell3/7 z interval replay PASS')
if __name__=='__main__':main()
