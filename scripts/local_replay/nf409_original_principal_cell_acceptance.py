#!/usr/bin/env python3
"""NF409 source-exact signed principal P=q+r cell integrals and an acceptance
contract for rigorous future continuous-z interval boxes.

All original prime seams enclosed with exact rational logarithms.
No claim of original z(x) boxes or centered physical norm certificate.
"""
import argparse,json,hashlib,sys
from fractions import Fraction as F
from pathlib import Path
from nf407_original_prime_jump_log_power_exact import I,ilog,compact
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)
R=F(332,10**13)
EPS=F(9,10**17)
def read(p):
 z=Path(p).read_bytes();return json.loads(z),hashlib.sha256(z).hexdigest()
def mx(a,b):return I(max(a.l,b.l),max(a.u,b.u))
def overlap(a,b,x):
 lo=max(F(0),b.l-max(a.u,x.u))
 hi=max(F(0),b.u-max(a.l,x.l))
 return I(lo,hi)
def hval(d):
 # H(d)=d(1+log(B/d)), monotone d∈[0,B].
 if d==0:return I(0)
 assert 0<d<=B
 z=ilog(I(B/d))
 return compact(d*(1+z),55)
def Hinterval(d):
 return I(hval(d.l).l,hval(d.u).u)
def qintegral(a,b,v):
 # q=v/2 log(B/(B-x)) on x>0.
 # Integral =v/2 [H(B-a)-H(B-b)].
 return compact(v*(Hinterval(I(B)-a)-Hinterval(I(B)-b))/2,55)
def l2interval(z):
 if z.l<=0<=z.u:return I(0,max(z.l*z.l,z.u*z.u))
 return I(min(z.l*z.l,z.u*z.u),max(z.l*z.l,z.u*z.u))
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 p.add_argument('--principal',default='notes/data/provisional/NF407_original_prime_jump_log_power_exact.json')
 p.add_argument('--center',default='notes/data/provisional/NF404_original_selected_pole_shear_exact.json')
 p.add_argument('--output',required=True)
 a=p.parse_args()
 seams,ssha=read(a.seams)
 principal,psha=read(a.principal)
 center,csha=read(a.center)
 assert principal['original_nf406_seams_sha256']==ssha
 assert principal['original_nf404_center_sha256']==csha
 assert seams['number_of_open_physical_support_cells']==16
 assert len(seams['certified_ordered_knots'])==17
 assert all(x['W_ODD_NEG']==x['RH']=='OPEN' for x in (seams,principal,center))
 v=I(*map(F,principal['original_source_u4_endpoint_interval']))
 assert v.u<0
 ps=principal['source_true_original_prime_jump_terms']
 assert len(ps)==7
 x={d['n']:I(*map(F,d['positive_jump_location_absolute_interval'])) for d in ps}
 c={d['n']:I(*map(F,d['signed_mangoldt_weight_positive_interval'])) for d in ps}
 assert all(z.l>0 for z in c.values())
 sorted_nodes=seams['certified_ordered_knots'][8:]
 assert sorted_nodes[0]['label']=='0' and sorted_nodes[-1]['label']=='+B'
 assert len(sorted_nodes)==9
 ptotal=I(0);cells=[]
 for j in range(8):
  na,nb=sorted_nodes[j:j+2]
  left=I(F(na['low']),F(na['high']))
  right=I(F(nb['low']),F(nb['high']))
  assert F(0)<=left.l<=left.u<right.l<=right.u<=B
  L=I(right.l-left.u,right.u-left.l)
  q=qintegral(left,right,v)
  rr=I(0)
  for n in (2,3,4,5,7,8,9):
   rr+=v*c[n]*overlap(left,right,x[n])
  rr=compact(rr,55)
  pbox=compact(q+rr,55)
  assert pbox.u<0
  ptotal+=pbox
  cells.append({'cell':j+1,'left_label':na['label'],'right_label':nb['label'],
    'left_enclosure':[str(left.l),str(left.u)],
    'right_enclosure':[str(right.l),str(right.u)],
    'width_positive_enclosure':[str(L.l),str(L.u)],
    'known_signed_q_integral_enclosure':[str(q.l),str(q.u)],
    'known_signed_r_integral_enclosure':[str(rr.l),str(rr.u)],
    'known_signed_p_integral_enclosure':[str(pbox.l),str(pbox.u)],
    'certified_original_continuous_z_range':None,
    'status':'KNOWN p INTEGRAL ONLY; TRUE z RANGE UNMEASURED'})
 # Crosscheck independently against the analytic integral over 0..B:
 # ∫_0^B q= B*v/2, ∫_0^B r= v Σ c_n(B−x_n).
 global_p=compact(B*v/2+sum((v*c[n]*(B-x[n]) for n in c),I(0)),55)
 ptotal=compact(ptotal,55)
 assert global_p.l<=ptotal.u and ptotal.l<=global_p.u
 ep=I(*map(F,principal['original_known_q_plus_all_seven_prime_jumps_power_interval']))
 C=F(center['exact_sufficient_new_full_supported_centered_scalar_power_upper_target'])
 gamma2=F(center['exact_source_original_full_complement_power_budget'])
 E=F(center['original_selected_after_pole_shear_power_lower_exact'])
 assert C==E+gamma2
 assert R*R>C and EPS>0
 fee=2*R*EPS+EPS*EPS
 assert fee<gamma2/8
 # Future optional independently source-proved continuous z bounds
 # z_i(x)∈[zlo,zhi] over EACH arbitrary rational subcell would imply:
 # E_full = E_p+2 ∑∫_cell z² + 4∑∫_cell z*p
 # with ∫ p<0 computed analytically and all odd x reflections paid.
 # This receipt reports NO z boxes and NO accepted C upper.
 out={
 'pass':'NF409',
 'standing':'SOURCE-EXACT KNOWN ORIGINAL PRINCIPAL SIGNED PHYSICAL CELL INTEGRALS AND CONDITIONAL CONTINUOUS z BOX CONTRACT; NO z BOXES OR GLOBAL NORM',
 'original_nf406_seams_sha256':ssha,
 'original_nf407_principal_source_sha256':psha,
 'original_nf404_center_source_sha256':csha,
 'original_source_principal_integral_negative_on_each_positive_cell':True,
 'original_eight_positive_source_principal_integrals':cells,
 'original_full_positive_half_known_signed_principal_integral_sum_outward':[str(ptotal.l),str(ptotal.u)],
 'original_independent_global_signed_principal_integral_outward':[str(global_p.l),str(global_p.u)],
 'original_global_principal_integral_independent_overlap':True,
 'original_p_full_squared_norm_outward':[str(ep.l),str(ep.u)],
 'original_centered_full_positive_scalar_gate_exact':str(C),
 'source_only_centered_selected_power_lower_exact':str(E),
 'original_source_exterior_allowance_gamma2_exact':str(gamma2),
 'future_rational_original_numeric_centered_norm_ceiling_R':str(R),
 'future_source_z_error_L2_tolerance_eps':str(EPS),
 'future_L2_error_energy_charge_strict_upper':str(fee),
 'source_rigorous_future_error_charge_below_one_eighth_exterior_budget':True,
 'future_original_p_continuous_z_exact_energy_identity':
  'E_full=E_p+2 sum_positive_cells integral z(x)^2 dx+4 sum_positive_cells integral z(x)*p(x) dx',
 'future_source_z_interval_box_acceptance':
  'An INDEPENDENT validated source/physical interval encloser must prove z(x) in [lo_i,hi_i] on ALL eight positive cells or their subcells. Since p(x)<0, integral z*p in [hi_i*int p, lo_i*int p]. Bound z² by range min/max, multiply certified widths, add exact E_p. The enclosing code must verify boxes, not trust handwritten values.',
 'future_piecewise_constant_source_z_acceptance':
  'If certified ||z-z_pc||_L2(I)<=eps and ||z_pc+p||<=R, then E_full<=E_pc+2R*eps+eps²; accept only if E_pc upper plus charge<=original C.',
 'original_source_native_radius_full_mD_action_error_previously_certified':'<1e-745 in NF408; not included in future eps unless validator pays explicitly',
 'true_original_continuous_z_enclosures_generated':False,
 'actual_original_continuous_z_norm_integrated':False,
 'actual_original_signed_z_p_cross_integrated':False,
 'actual_original_full_centered_supported_power_upper_computed':False,
 'new_signed_kernel_cells':0,'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 target=Path(a.output);target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps(out,indent=2)+'\n')
 print('NF409 original 8 signed p-cell integral boxes exact; independent global overlap PASS')
 print('NF409 future source z L2 envelope eps',EPS,'cost budget exact pass')
 print('NF409 no actual z boxes, full physical centered upper UNCOMPUTED')
if __name__=='__main__':main()
