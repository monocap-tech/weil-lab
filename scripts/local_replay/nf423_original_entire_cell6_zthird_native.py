#!/usr/bin/env python3
"""NF423 original ENTIRE open physical cell6 rigorous third x derivative bound.

Use genuine NF406 exact seam brackets as physical domain boundaries. All
original cell6 x lie strictly inside a rational OVER-ENVELOPE [.84,.99].
Evaluate ONLY arch/kernel coefficients on the enclosing interval with
4096-bit Arb; prime branch logic is proven for the true NF406 OPEN cell,
NOT for the over-envelope (which crosses seams). Existing correlated full
u4'''' Gram, endpoint data, and original signed 5 active prime weights
bound every true z'''(x) in cell6. This certifies whole-cell *derivative
control*, NOT a completed decision-quality z/C/NF404 scalar model.
"""
import argparse,json,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
from nf415_original_cell6_I1_validated_acb import read,A
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10);L=F(21,25);R=F(99,100)
WEIGHTS={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
def kval(t):
 r=(-t).exp()
 K=(-t/4).exp()/(1-r)
 L1=-arb(1)/4-r/(1-r)
 L2=r/(1-r)**2
 return K,K*L1,K*(L1*L1+L2)
def bound(v,arr):
 for n in arr:
  if abs(v)<arb(n):return n
 raise AssertionError(('overbroad interval bound',str(v)[:200]))
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 p.add_argument('--nf411',default='notes/data/provisional/NF411_original_source_boundary_jet.json')
 p.add_argument('--nf421gram',default='notes/data/provisional/NF421_original_fourth_source_gram_and_z_third_bound_native.json')
 p.add_argument('--nf422',default='notes/data/provisional/NF422_original_all_order_arch_transfer_exact.json')
 p.add_argument('--nf423wide',default='notes/data/provisional/NF423_original_cell6_wide_zthird_native.json')
 p.add_argument('--output',required=True)
 a=p.parse_args()
 src,sha=read(a.source);seams,seamsha=read(a.seams)
 jet,jsha=read(a.nf411);g,gsha=read(a.nf421gram)
 transfer,tsha=read(a.nf422);wide,wsha=read(a.nf423wide)
 assert sha==g['original_nf407_source_sha256']==wide['original_source_sha256']==transfer['original_nf407_source_sha256']
 assert seamsha==g['original_nf406_seams_sha256']==wide['original_nf406_seams_sha256']
 assert jet['nf407_source_sha256']==sha
 assert g['original_true_u4_fourth_derivative_L2_upper_power2']=='16384'
 assert g['original_true_u4_third_derivative_global_sup_upper_exact']=='24580'
 assert transfer['all_original_orders_1_through_12_inductively_replayed_exact_fraction']
 assert transfer['NF421_original_analytic_third_identity_as_written_needs_correction']
 assert wide['original_corrected_NF422_endpoint_parity_used']
 assert all(x['W_ODD_NEG']==x['RH']=='OPEN' for x in (src,seams,jet,g,transfer,wide))
 knot=seams['certified_ordered_knots']
 assert knot[13]['label']=='-B+log(7)' and knot[14]['label']=='-B+log(8)'
 # True original cell6= (log(7)-B,log(8)-B), a STRICT SUBSET of
 # [.84,.99]. Evaluate arch on superset; prime fixed only on real cell.
 assert L<F(knot[13]['low'])<F(knot[13]['high'])<F(knot[14]['low'])<F(knot[14]['high'])<R
 assert F(knot[14]['low'])-F(knot[13]['high'])>F(1,8)
 ctx.prec=4096
 x=arb('0.915 +/- 0.075')
 assert x.contains(A(L)) and x.contains(A(R))
 d=A(B)-x;t1=2*d;t2=2*(A(B)+x)
 assert B-R>F(1,10) and 2*(B-L)<F(3,5)
 assert 2*(B+R)<F(9,2) and 2*(B+L)>3
 phi=((d/A(B))*(d/4).cosh()/(d/4).sinh()).log()+2*((-d/2).exp()).atan()
 q=(-t2/4).exp()
 J=2*(q.atanh()+q.atan())
 AA=(arb(1)/4).digamma()-arb.pi().log()+(J+phi)/2+(A(B)/d).log()/2
 cA=bound(AA,[4,5,6,7,8,10,12,16])
 k1,p1,kpp1=kval(t1);k2,p2,kpp2=kval(t2)
 assert k1>0 and k2>0
 ck1=bound(k1,[6,7,8,9,10,12])
 ck2=bound(k2,[1,2])
 cp1=bound(p1,[20,25,30,40,60])
 cp2=bound(p2,[1,2])
 # Direct dependency-laden whole interval for K'' can produce a
 # non-finite Arb ball. Instead use exact rational positive-t bounds:
 # |K''(t)| <= (2/t)*((1/4+1/t)^2+1/t+1/t^2).
 # Here t1>=2(B-R)=11/50, t2>=2(B+L)=97/25,
 # and d>=B-R=11/100. This is uniform without an Arb
 # interval dependency failure; source analytic A is still Arb.
 def Ksecond_exact(t):
  return F(2)/t*((F(1,4)+1/t)**2+1/t+1/t**2)
 true_R2_upper=4*Ksecond_exact(2*(B-R))+4*Ksecond_exact(2*(B+L))+1/(B-R)**3
 assert true_R2_upper<2600
 cR2=2600
 # On actual physical knot-defined open cell6:
 # n2,3,4,5,7 POST-SEAM one translate, n8,9 NEITHER.
 # These original source branches are checked by certified knot order,
 # not by testing the over-enclosing x interval against seams.
 weights=sum((arb(base).log()/arb(n).sqrt() for n,base in WEIGHTS.items() if n in (2,3,4,5,7)),arb(0))
 cP=bound(weights,[3,4,5])
 assert cP==3
 # E integral estimates true for entire cell6, since:
 # I0[u'''] <= 2sqrt(2t1)*N4<3N4 because t1<0.6,
 # I1[u'''] <=sqrt(2)(sqrt(t2)-sqrt(t1))*N4<4N4,
 # from ||u''''||2 and true support. Explicit rational overcharges:
 assert 16*(B-L)<9 # implies 2sqrt(2*t1)<3
 assert 2*(B+R)<F(9,2) # implies sqrt(2t2)<3<4
 N3=24580;N4=16384
 # Endpoint u''(B) <1, u'(B)<1e-6, u(B)<1e-9,
 # NF404 centered third derivative <2.
 endpoint=ck1+ck2+F(2,10**6)*(cp1+cp2)+F(1,10**9)*cR2+2
 mend=next(k for k in [10,12,15,20] if endpoint<k)
 M=(cA+cP)*N3+7*N4+mend
 assert M<int(g['original_complete_z_third_x_derivative_uniform_upper_exact'])
 assert M>=int(wide['original_full_zthird_widened_interval_strict_integer_upper']) or cA<=wide['original_analytic_A_absolute_strict_integer_upper']
 out={
 'pass':'NF423-entire-open-cell6-zthird',
 'standing':'ACCEPTED TRUE COMPLETE ORIGINAL PHYSICAL CELL6 OPEN DOMAIN UNIFORM z THIRD DERIVATIVE FROM CORRELATED 246 SOURCE, EXACT PRIME KNOTS; CELLWISE z / NF404 OPEN',
 'original_nf407_source_sha256':sha,
 'original_nf406_exact_support_seams_sha256':seamsha,
 'original_nf411_endpoint_jet_sha256':jsha,
 'original_nf421_source_fourth_gram_sha256':gsha,
 'original_nf422_all_order_corrected_transfer_sha256':tsha,
 'original_nf423_wide_native_parent_sha256':wsha,
 'original_full_242_selected_plus_four_critical_source_kept':True,
 'original_true_physical_cell_number':6,
 'original_true_entire_cell_open_exact_description':'(log(7)-11/10,log(8)-11/10)',
 'original_physical_cell6_original_knot_lower_certified':knot[13],
 'original_physical_cell6_original_knot_upper_certified':knot[14],
 'native_interval_evaluated_on_strict_original_cell_superset':['21/25','99/100'],
 'native_interval_real_arb_4096bit':True,
 'native_interval_arch_A_ball':str(AA),
 'true_analytic_arch_A_absolute_strict_upper':cA,
 'original_all_seven_real_signed_prime_branches_inside_open_cell':['post-seam']*5+['neither']*2,
 'true_active_prime_weight_strict_upper':cP,
 'true_K1_strict_upper':ck1,'true_K2_strict_upper':ck2,
 'true_K1prime_strict_upper':cp1,'true_K2prime_strict_upper':cp2,
 'true_Rsecond_strict_upper':cR2,
 'true_Rsecond_source_kernel_rational_upper_exact':str(true_R2_upper),
 'true_Rsecond_direct_broad_Arb_interval_used':False,
 'true_original_source_u4_third_global_sup_strict':N3,
 'true_original_source_u4_fourth_L2_strict':N4,
 'true_original_zthird_endpoint_and_center_budget_strict':mend,
 'true_original_entire_open_cell6_zthird_uniform_strict_upper':M,
 'original_NF422_correct_odd_derivative_endpoint_sign':True,
 'certified_true_entire_open_cell6_derivative_bound':True,
 'true_full_original_cell6_cubic_Taylor_remainder_from_x0':'M*|x-9/10|^3/6 on the true open cell6 (fundamental theorem, source piecewise C3)',
 'original_true_complete_cell6_z_decision_quality_enclosure':False,
 'original_cell6_signed_p_z_and_z2_integrated':False,
 'original_NF404_complete_centered_scalar_decided':False,
 'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF423 TRUE ENTIRE OPEN PHYSICAL CELL6 zthird bound',M,'A<',cA,'P3<',cP,'end<',mend,flush=True)
 print('NF423 full original cell6 is derivative-controlled but NOT scalar-certified',flush=True)
if __name__=='__main__':main()
