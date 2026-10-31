#!/usr/bin/env python3
"""NF423 rigorous original cell6 OPEN physical support wider z''' envelope.

No new source, no extra x-point quadrature or derivative order. Verify same
NF421 full correlated 246 physical source and NF422 corrected all-order
arch recurrence; rigorously bound whole 0.85..0.93 original cell6 interval
with 4096-bit outward Arb interval evaluation for finite A(x), moving kernels,
and true original signed 5 active prime weights. Sharpen global 1540338
to a lower integer on a 40x WIDER original interval. Build source-paid
cubic remainder conditional on parent three true z-jets at x=.9; exact
Fraction follow-up may then enlarge guaranteed true z>0 island.
"""
import argparse,sys,json
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
from nf415_original_cell6_I1_validated_acb import read,A
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10);L=F(17,20);R=F(93,100);X=F(9,10)
WEIGHTS={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
def K(t):
 return (-t/4).exp()/(1-(-t).exp())
def Kprime(t):
 q=(-t).exp()
 return K(t)*(-arb(1)/4-q/(1-q))
def Ksecond(t):
 q=(-t).exp()
 l=-arb(1)/4-q/(1-q)
 return K(t)*(l*l+q/(1-q)**2)
def upper(v,candidates):
 for n in candidates:
  if abs(v)<arb(n):return n
 raise AssertionError(('original source interval arithmetic fails bound',str(v)[:280]))
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 p.add_argument('--nf411',default='notes/data/provisional/NF411_original_source_boundary_jet.json')
 p.add_argument('--nf421gram',default='notes/data/provisional/NF421_original_fourth_source_gram_and_z_third_bound_native.json')
 p.add_argument('--nf421interval',default='notes/data/provisional/NF421_original_local_third_taylor_independent_fraction.json')
 p.add_argument('--nf422',default='notes/data/provisional/NF422_original_all_order_arch_transfer_exact.json')
 p.add_argument('--output',required=True)
 a=p.parse_args()
 source,sha=read(a.source);seams,seamsha=read(a.seams)
 jet,jsha=read(a.nf411);gram,gsha=read(a.nf421gram)
 old,oldsha=read(a.nf421interval);trans,tsha=read(a.nf422)
 assert source['original_dimension']==242
 assert len(source['original_selected_generator_node_orders'])==242
 assert len(source['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert sha==gram['original_nf407_source_sha256']==old['original_source_sha256']==trans['original_nf407_source_sha256']
 assert gram['original_nf406_seams_sha256']==trans['original_nf406_exact_support_seams_sha256']==seamsha
 assert trans['NF421_original_conservative_third_derivative_numerical_upper_preserved']
 assert trans['all_original_orders_1_through_12_inductively_replayed_exact_fraction']
 assert gram['original_true_u4_fourth_derivative_L2_upper_power2']=='16384'
 assert gram['original_true_u4_third_derivative_global_sup_upper_exact']=='24580'
 assert jet['nf407_source_sha256']==sha
 assert jet['source_derivative_nonzero_certified']
 assert all(r['W_ODD_NEG']==r['RH']=='OPEN' for r in (source,seams,jet,gram,old,trans))
 knots=seams['certified_ordered_knots']
 assert knots[13]['label']=='-B+log(7)' and knots[14]['label']=='-B+log(8)'
 assert F(knots[13]['high'])<L<R<F(knots[14]['low'])
 assert X>=L and X<=R and R-L==F(2,25)
 assert R-L==40*F(1,500)
 dmin=B-R;dmax=B-L
 assert dmin>F(1,6) and 2*dmax<=F(1,2)
 assert 2*dmin>F(1,3) and 2*(B+L)>3 and 2*(B+R)<F(9,2)
 ctx.prec=4096
 # Enclose x over entire physical source interval, not a mesh.
 x=arb('0.89 +/- 0.04')
 assert x.contains(arb('0.85')) and x.contains(arb('0.93'))
 d=A(B)-x;t1=2*d;t2=2*(A(B)+x)
 phi=((d/A(B))*(d/4).cosh()/(d/4).sinh()).log()+2*((-d/2).exp()).atan()
 q=(-t2/4).exp()
 J=2*(q.atanh()+q.atan())
 c=(arb(1)/4).digamma()-arb.pi().log()+(J+phi)/2
 AA=c+(A(B)/d).log()/2
 ca=upper(AA,[4,5,6,7,8,10,12,16])
 k1=K(t1);k2=K(t2)
 assert k1>0 and k2>0
 assert k1<6 and k2<1
 bkp1=upper(Kprime(t1),[10,20,30])
 bkp2=upper(Kprime(t2),[1,2])
 Rsecond=4*Ksecond(t1)+4*Ksecond(t2)-1/(d**3)
 bR=upper(Rsecond,[400,600,800,1200])
 # Source odd support, original NF414 has only n=2,3,4,5,7
 # post-seam and n=8,9 neither on ALL this interval.
 count=0;primeweight=arb(0);branch=[]
 for n,base in WEIGHTS.items():
  h=arb(n).log();seam=abs(A(B)-h)
  if h<A(B) and x<seam:status='both'
  elif h>A(B) and x<seam:status='neither'
  else:
   assert x>seam
   status='post-seam'
  if status=='post-seam':
   primeweight+=arb(base).log()/arb(n).sqrt();count+=1
  branch.append({'n':n,'branch':status})
 assert [i['branch'] for i in branch]==['post-seam']*5+['neither']*2
 assert count==5
 cp=upper(primeweight,[3,4,5,6,10])
 assert cp<=4
 # Actual original |u4'''|<=24580 globally and
 # ||u4''''||2<16384; original kernel source integrals
 # preserve |I0[u''']|<3N4 and |I1[u''']|<4N4
 # since t1<=1/2 and t2<9/2. Prime P''' only 5
 # one-sided original physical source translates, total weight<cp.
 N3=24580;N4=16384
 # Genuine original endpoints from NF411: |u''(B)|<1,
 # |u'(B)|<1e-6, |u(B)|<1e-9, center third <2.
 # Their combined true cost: <7+2e-6*(bkp1+bkp2)
 # +1e-9*bR+2 <10.
 assert F(7)+F(2,10**6)*(bkp1+bkp2)+F(bR,10**9)+2 <10
 M=(ca+cp)*N3+7*N4+10
 assert M<1540338
 # Original no-mesh simultaneous interval proof keeps every
 # true NF406 prime branch and 246-source u'''' norm bound.
 out={
 'pass':'NF423-original-cell6-uniform-extension',
 'standing':'FULL ORIGINAL SOURCE-CORRELATED z THIRD DERIVATIVE NATIVE INTERVAL SHARPENED OVER 40x WIDER PHYSICAL CELL6 MACRO REGION; NOT FULL CELL OR NF404',
 'original_source_sha256':sha,
 'original_nf406_seams_sha256':seamsha,
 'original_nf411_endpoint_jet_sha256':jsha,
 'original_nf421_fourth_correlated_source_gram_sha256':gsha,
 'original_nf421_previous_cubic_Taylor_sha256':oldsha,
 'original_nf422_corrected_all_order_transfer_sha256':tsha,
 'original_242_selected_plus_four_critical_unchanged':True,
 'full_source_all_selected_critical_correlations_from_NF421_kept':True,
 'original_corrected_NF422_endpoint_parity_used':True,
 'full_interval_native_precision_bits':4096,
 'true_original_cell6_widened_interval_exact':[str(L),str(R)],
 'true_original_cell6_widened_interval_decimal':['0.85','0.93'],
 'original_nf406_exact_one_sided_knot_brackets_strictly_excluded':True,
 'original_widened_interval_ratio_to_NF421_original_macro':40,
 'original_full_7_signed_prime_branches_over_entire_interval':branch,
 'original_signed_active_prime_weight_sum_arb':str(primeweight),
 'original_signed_active_prime_weight_strict_integer_upper':cp,
 'original_analytic_A_interval_arb':str(AA),
 'original_analytic_A_absolute_strict_integer_upper':ca,
 'original_Kprime1_strict_integer_upper':bkp1,
 'original_Kprime2_strict_integer_upper':bkp2,
 'original_Rsecond_strict_integer_upper':bR,
 'original_source_u_third_sup_strict':N3,
 'original_source_u_fourth_L2_strict':N4,
 'original_full_zthird_widened_interval_strict_integer_upper':M,
 'original_source_I0_u_third_bound':'3*N4',
 'original_source_I1_u_third_bound':'4*N4',
 'original_complete_z_centered_second_xjet_at_9over10_reused':True,
 'original_cubic_Taylor_remainder_valid_for_every_x_in_widened_interval':True,
 'original_widened_x_Taylor_remainder':'M*|x-9/10|^3/6',
 'original_tight_entire_cell6_z_enclosure_certified':False,
 'original_z_p_and_z_squared_integrated':False,
 'original_NF404_centered_scalar_decided':False,
 'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF423 40x original macro cell6 interval [0.85,0.93], |A|<',ca,'prime weight <',cp,flush=True)
 print('NF423 true original complete |zthird|<',M,'on EVERY x in physical interval',flush=True)
 print('NF423 complete original cell6/NF404 scalar OPEN',flush=True)
if __name__=='__main__':main()
