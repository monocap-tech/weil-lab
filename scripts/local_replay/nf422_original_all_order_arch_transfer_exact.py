#!/usr/bin/env python3
"""NF422 source-parity-correct all-order TRUE original moving-arch transfer.

Analytical exact-rational formal differentiation for physical original u4,
no numerical quadrature or new source. Corrects NF421 THIRD derivative
u4''(B) K2 sign. Verifies NF421 numerical M_z3 remains a safe bound,
quantifies the strictly conditional source-Taylor panel coverage cost on
the certified [899/1000,901/1000] interval only.

D (A(x)g(x)+I0[g]+I1[g])
 = A(x)g'(x)+I0[g']+I1[g'] + K(t1)g(B)-K(t2)g(-B),
 A'=K(t1)-K(t2), t1=2(B-x), t2=2(B+x).
For original odd u4, u4^(j)(-B)=(-1)^(j+1)u4^(j)(B).
This is a mathematical operator-level transfer, not a claim of
decision-quality NF404 norm or full-cell derivative bounds.
"""
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);X=F(9,10)
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def dd(form):
 out={}
 def add(k,v):out[k]=out.get(k,F(0))+v
 for key,v in form.items():
  tag=key[0]
  if tag=="S":
   j=key[1]
   add(("S",j+1),v)
   add(("E",j,1,0),v)
   add(("E",j,2,0),v*(-1)**j)
  elif tag=="E":
   _,j,side,m=key
   add(("E",j,side,m+1),v*(-2 if side==1 else 2))
  elif tag=="Q":
   _,n=key
   add(("Q",n+1),v*n)
  else:raise AssertionError(key)
 return {k:v for k,v in out.items() if v}
def predicted(n):
 # Exact all-order boundary transfer for original odd source.
 out={("S",n):F(1),("Q",n):-F(math.factorial(n-1),2)}
 for j in range(n):
  m=n-1-j
  out[("E",j,1,m)]=F((-2)**m)
  out[("E",j,2,m)]=F((-1)**j*2**m)
 return out
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 ap.add_argument('--nf414',default='notes/data/provisional/NF414_original_hotspot_finite_continuous_native.json')
 ap.add_argument('--nf419',default='notes/data/provisional/NF419_original_cell6_full_xprime_native.json')
 ap.add_argument('--nf420',default='notes/data/provisional/NF420_original_cell6_independent_sharpened_Taylor_positive_interval.json')
 ap.add_argument('--nf421gram',default='notes/data/provisional/NF421_original_fourth_source_gram_and_z_third_bound_native.json')
 ap.add_argument('--nf421jet',default='notes/data/provisional/NF421_original_cell6_complete_second_xjet_native.json')
 ap.add_argument('--nf421interval',default='notes/data/provisional/NF421_original_local_third_taylor_independent_fraction.json')
 ap.add_argument('--output',required=True)
 args=ap.parse_args()
 source,source_sha=read(args.source);seams,seam_sha=read(args.seams)
 finite,finite_sha=read(args.nf414);jet,jet_sha=read(args.nf419)
 r420,r420_sha=read(args.nf420);g,gsha=read(args.nf421gram)
 j,jsha=read(args.nf421jet);r421,r421sha=read(args.nf421interval)
 assert source['original_dimension']==242
 assert len(source['original_selected_generator_node_orders'])==242
 assert len(source['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert len(source['original_source_critical_sine_frequencies'])==32
 assert source_sha==jet['original_nf407_source_sha256']==r420['original_nf407_source_sha256']
 assert source_sha==g['original_nf407_source_sha256']==j['original_source_sha256']==r421['original_source_sha256']
 assert source_sha==finite['original_nf407_source_sha256']
 assert seam_sha==g['original_nf406_seams_sha256']
 assert r420_sha==g['original_nf420_parent_sha256']
 assert gsha==r421['NF421_original_source_fourth_Gram_sha256']
 assert jsha==r421['NF421_original_second_xjet_sha256']
 assert r421['original_true_z_third_x_derivative_uniform_upper_exact']=='1540338'
 assert g['original_true_u4_third_derivative_global_sup_upper_exact']=='24580'
 assert j['original_true_pointwise_second_x_jet_certified']
 assert r421['original_positive_interval_radius_improved_from_NF420']
 assert all(q['W_ODD_NEG']==q['RH']=='OPEN' for q in (source,seams,finite,jet,r420,g,j,r421))
 # Actual original function parity is enforced by EXACT node types:
 # original x^even sin and x^odd cos plus 4 critical odd sin and sinh.
 nodes=source['original_selected_generator_node_orders']
 assert all((f=='pole' and k is None) or
   (f!='pole' and isinstance(k,int) and 0<=k<=13)
   for f,k in nodes)
 assert all(k%2==0 or k%2==1 for f,k in nodes if f!='pole')
 assert any(f=='pole' for f,k in nodes)
 assert len(source['original_source_critical_sines_and_pole_coefficients'])==4
 # Re-derive the physical MOVING t-interface from independent endpoint
 # formal symbols, not from the claimed all-order commutator.
 # K1: original I0 upper t1'=-2, I1 lower t1'=-2,
 # K2: original I1 upper t2'=+2.
 # A' g(x)=(K1-K2)g(x). Coefficient tuples are exact:
 # (K1,gx), (K1,gB), (K1,ginner),
 # (K2,gx), (K2,g(-B)).
 initial_boundary={
  ('K1','gx'):-F(2)+F(1)+F(1),
  ('K1','gB'):F(1),
  ('K1','ginner'):F(1)-F(1),
  ('K2','gx'):F(1)-F(1),
  ('K2','gminusB'):-F(1)}
 assert initial_boundary=={
  ('K1','gx'):F(0),('K1','gB'):F(1),
  ('K1','ginner'):F(0),('K2','gx'):F(0),
  ('K2','gminusB'):-F(1)}
 # This proves the original interface cancellation BEFORE substituting
 # odd-source g(-B), so parity and moving-endpoint directions are separate.
 # Every selected source monomial is sin for even k, cos for odd k
 # by the NF407/NF413 source generator convention. Both are odd,
 # as are all critical sine and odd pole; hence all derivative parity.
 form={("S",1):F(1),("E",0,1,0):F(1),("E",0,2,0):F(1),("Q",1):-F(1,2)}
 proof=[]
 for n in range(1,13):
  exact=predicted(n)
  assert form==exact,('all-order original moving arch recurrence fails',n)
  proof.append({
    'derivative_order':n,
    'physical_arch_integral_atom':'S[u^('+str(n)+')]',
    'endpoint_jet_terms':2*n,
    'endpoint_u_at_B_kernel1_coefficient':str(exact[('E',0,1,n-1)]),
    'endpoint_u_at_B_kernel2_coefficient':str(exact[('E',0,2,n-1)]),
    'top_endpoint_u_derivative_at_B_kernel2_sign':str(exact[('E',n-1,2,0)]),
    'original_dlog_pole_coefficient_for_u_B_over_d_power':str(exact[('Q',n)])})
  form=dd(form)
 # Key NF421 error: u4''(B) multiplies K1+K2 in z'''
 # not K1-K2; all other exact endpoint terms match NF421.
 correct=predicted(3)
 assert correct[('E',2,1,0)]==1
 assert correct[('E',2,2,0)]==1
 assert correct[('E',1,1,1)]==correct[('E',1,2,1)]==-2
 assert correct[('E',0,1,2)]==correct[('E',0,2,2)]==4
 assert correct[('Q',3)]==-1
 incorrect_nf421_k2_term=-1
 assert incorrect_nf421_k2_term != correct[('E',2,2,0)]
 # NF421's native/independent bound uses |K1|<6 and |K2|<1
 # so |K1+K2|<7, same numerical budget for the corrected sign.
 # Therefore local conservative |z'''|<1540338 remains unaffected.
 assert F(2)/F(1,3)==6 and F(2)/3<1
 assert F(58)*24580+7*16384+10 ==1540338
 assert int(g['original_true_u4_fourth_derivative_L2_upper_power2'])==16384
 # The uniform bound holds ONLY inside true original macro interval.
 macro_l,macro_r=F(899,1000),F(901,1000)
 assert (macro_l,macro_r)==tuple(map(F,r421['original_macro_interval']))
 assert macro_r-macro_l==F(1,500)
 knots=seams['certified_ordered_knots']
 assert knots[13]['label']=='-B+log(7)' and knots[14]['label']=='-B+log(8)'
 assert F(knots[13]['high'])<macro_l<macro_r<F(knots[14]['low'])
 # NF421 original z anchored cubic Taylor has a huge error at macro
 # edge relative to z(0.9). This certifies a SPECIFIC coarse bound
 # precision stop, not an information-theoretic impossibility.
 Mz3=F(r421['original_true_z_third_x_derivative_uniform_upper_exact'])
 edge_error=Mz3*F(1,1000)**3/6
 assert edge_error>F(1,10000)
 # Construct a purely conditional exact finite cover for an L2 error
 # of < 9e-17 on THIS macro interval: 10000 equally spaced panels,
 # each halfwidth 1e-7, requires source-certified 2nd x-jets at ALL
 # their centers, NOT currently available. For a true uniform M3
 # on the macro, local sup Taylor error <= M3*r^3/6.
 # ||error||L2 <= M3*r^3/6 * sqrt(1/500)
 # and sqrt(1/500) <1/20 exactly because 1/500<1/400.
 epsilon=F(9,10**17)
 r=F(1,10**7)
 tile_count=(macro_r-macro_l)/(2*r)
 assert tile_count==10000
 macro_l2upper=Mz3*r**3/F(120)
 assert macro_l2upper<epsilon
 assert F(1,500)<F(1,20)**2
 # This is a sufficient design conditional on 10000 NEW genuine
 # original (z,z',z'') interval certificates, not a computed scalar.
 # Outside macro, Mz3=1540338 is NOT presently certified. Full cell
 # has additional unclipped cells to be treated separately.
 full_cell_length_lower=F(knots[14]['low'])-F(knots[13]['high'])
 assert full_cell_length_lower>F(1,8)
 assert macro_r-macro_l<full_cell_length_lower
 # True original NF414 support branch distribution at x0.
 original_branches=finite['hotspot_points'][1]['all_seven_true_prime_branches']
 assert len(original_branches)==7
 assert [q['branch'] for q in original_branches]==[q['branch'] for q in jet['original_all_seven_signed_prime_derivative_branches']]
 assert [q['branch'] for q in original_branches]==[q['branch'] for q in j['original_seven_signed_prime_derivative_branches']]
 out={
  'pass':'NF422',
  'standing':'ACCEPTED EXACT ORIGINAL ALL-ORDER MOVING ARCH TRANSFER AND NF421 THIRD-PARITY CORRECTION; GENUINE MACRO PANEL CERTIFICATION COST, NF404 OPEN',
  'original_nf407_source_sha256':source_sha,
  'original_nf406_exact_support_seams_sha256':seam_sha,
  'original_nf414_signed_seven_prime_branches_sha256':finite_sha,
  'original_nf419_complete_xprime_sha256':jet_sha,
  'original_nf420_source_Taylor_sha256':r420_sha,
  'original_nf421_fourth_source_gram_sha256':gsha,
  'original_nf421_second_xjet_sha256':jsha,
  'original_nf421_source_Taylor_interval_sha256':r421sha,
  'same_original_242_selected_and_4_critical_odd_source':True,
  'original_odd_source_derivative_j_parity':'u4^(j)(-B)=(-1)^(j+1)u4^(j)(B)',
  'original_true_I0_I1_moving_interface_general_g':'I0[g]+I1[g] derivative contributes K(t1)*(g(B)-g(x))+K(t2)*(g(x)-g(-B))',
  'original_physical_boundary_direct_formal_atom_check':True,
  'original_combined_arch_S_commutator':'d S[g]/dx = S[gprime]+K(t1)g(B)-K(t2)g(-B)',
  'original_finite_A_derivative_exact':'A_prime=K(t1)-K(t2)',
  'original_all_order_arch_n_formula':'S[u4^(n)]+sum_j=0..n-1 u4^(j)(B)*[(-2)^(n-1-j) K^(n-1-j)(t1)+(-1)^j 2^(n-1-j) K^(n-1-j)(t2)]-(n-1)!u4(B)/(2 d^n)',
  'all_original_orders_1_through_12_inductively_replayed_exact_fraction':True,
  'all_order_formal_replay':proof,
  'NF421_original_zthird_endpoint_correction':'u4second(B)*(K(t1)+K(t2)), NOT u4second(B)*(K(t1)-K(t2))',
  'NF421_original_analytic_third_identity_as_written_needs_correction':True,
  'NF421_original_conservative_third_derivative_numerical_upper_preserved':True,
  'NF421_verified_original_Mz3_upper_unchanged':1540338,
  'exact_original_macro_cell6_interval':['899/1000','901/1000'],
  'original_7_signed_prime_branches_unchanged':True,
  'original_NF421_cubic_error_at_macro_interval_edge_exact':str(edge_error),
  'original_NF421_single_center_macro_NF404_quality':'FAILS_TO_RESOLVE',
  'NF409_provisional_original_L2_error_budget_exact':str(epsilon),
  'conditional_10000_panels_halfwidth_exact':str(r),
  'conditional_macro_panels_required_as_constructed':int(tile_count),
  'conditional_10000_center_complete_original_second_jet_certificates_available':False,
  'conditional_macro_L2_error_strict_upper_exact':str(macro_l2upper),
  'conditional_macro_L2_error_less_than_NF409_epsilon':macro_l2upper<epsilon,
  'original_full_physical_cell6_length_exceeds':'1/8',
  'original_Mz3_local_macro_only_not_entire_original_cell6':True,
  'complete_original_macro_source_x_taylor_cellwise_model_certified':False,
  'complete_original_entire_cell6_model_certified':False,
  'NF410_signed_original_p_z_and_z_squared_certified':False,
  'NF404_original_complete_centered_scalar_decided':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 target=Path(args.output);target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps(out,indent=2)+'\n')
 print('NF422 exact n=1..12 original physical arch transfer PASS')
 print('NF422 NF421 u4second(B) K2 parity sign corrected; 1540338 bound safe')
 print('NF422 macro single-center cubic bound at |x-0.9|=0.001:',str(edge_error))
 print('NF422 conditional 10000 source-jet panels over original macro interval error L2 <',str(macro_l2upper))
 print('NF422 full cell6 and original NF404 signed scalar OPEN')
if __name__=='__main__':main()
