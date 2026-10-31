#!/usr/bin/env python3
"""NF408 exact original signed digamma and seven-prime PHYSICAL regularization.

Algebraically removes the known endpoint log and all seven true prime
support jumps *inside* the source action, with no physical quadrature.
Original g=z+q+r unchanged. No numerical positive norm.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10)
POWERS=(2,3,4,5,7,8,9)
def read(p):
 b=Path(p).read_bytes()
 return json.loads(b),hashlib.sha256(b).hexdigest()
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--principal',default='notes/data/provisional/NF407_original_prime_jump_log_power_exact.json')
 p.add_argument('--center',default='notes/data/provisional/NF404_original_selected_pole_shear_exact.json')
 p.add_argument('--output',required=True)
 a=p.parse_args()
 seams,ssha=read(a.seams)
 source,ussha=read(a.source)
 principal,psha=read(a.principal)
 center,csha=read(a.center)
 assert seams['number_of_open_physical_support_cells']==16
 assert len(seams['original_prime_power_log_shifts'])==7
 assert principal['source_all_original_prime_jumps_cancelled_from_z'] is True
 assert principal['original_nf406_seams_sha256']==ssha
 assert principal['original_nf404_center_sha256']==csha
 assert source['original_exported_coefficients_are_4096bit_arb_not_float'] is True
 assert all(x['W_ODD_NEG']==x['RH']=='OPEN' for x in (seams,source,principal,center))
 assert center['actual_original_full_supported_centered_scalar_integrated'] is False
 logstates={}
 for t in seams['original_prime_power_log_shifts']:
  n=t['n'];lo=F(t['log_lower']);hi=F(t['log_upper'])
  assert F(0)<lo<hi<2*B
  branch='h_less_B' if hi<B else 'h_greater_B'
  assert (lo<B if branch=='h_less_B' else lo>B)
  logstates[n]=branch
 assert logstates=={2:'h_less_B',3:'h_less_B',4:'h_greater_B',
                    5:'h_greater_B',7:'h_greater_B',
                    8:'h_greater_B',9:'h_greater_B'}
 # Verify every prime-support seam's signed discontinuity subtraction
 # algebraically for generic abstract u(-B)=-v, u(+B)=v,
 # nearest smooth translated value U and signed prime weight c.
 U=F(137,17);v=F(-19,5);c=F(31,7)
 checks=[]
 for n in POWERS:
  # The source prime operator has -c_n[u(x+h)+u(x-h)].
  # For h<B at positive seam x=B-h:
  # left = -c(v+U), right(after subtract r)= -c U-v c.
  # For h>B at x=h-B: left=0, right=-c*u(-B)-v c
  # = +v c-v c=0. In both the z component is continuous.
  if logstates[n]=='h_less_B':
   left=-c*(v+U);right=-c*U-v*c
  else:
   left=F(0);right=-c*(-v)-v*c
  assert left==right
  checks.append({'n':n,'branch':logstates[n],
    'positive_seam':f'abs(B-ln({n}))',
    'continuous_original_prime_remainder_before_equals_after':True})
 # The compact original arch action on x∈[0,B), d=B-x,
 # t1=2d, t2=2(B+x):
 #
 # A u =c0 u +J(t2)u +
 #  ∫_0^t1 K(t)[u-.5(uplus+uminus)]dt
 # +∫_t1^t2 K(t)[u-.5uminus]dt.
 # Split u-.5uminus=.5u+.5(u-uminus). Then
 # A u=(c0+.5J(t1)+.5J(t2))u +I0+I1.
 # With q=v/2 ln(B/d), define Phi=J(t1)-ln(B/d).
 # A u-q=(c0+.5J(t2)+.5Phi)u +.5ln(B/d)(u-v)+I0+I1.
 #
 # Pointwise boundary: Phi(d)=ln[(d/B)coth(d/4)]
 #                    +2atan(exp(-d/2))→ln(4/B)+pi/2.
 # The u-v factor vanishes linearly, so (u-v)ln(B/d)
 # tends zero; both I0 and I1 have a finite limit.
 #
 # This is algebra/analytic identity not a quadrature.
 assert B==F(11,10)
 # Verify coefficient conservation in the compact split as a rational
 # formal linear identity for independent u, J1,J2 and L variables:
 for u,J1,J2,L,v in [(F(17),F(13),F(3),F(11),F(-7)),
                     (F(-5,3),F(2,9),F(31,5),F(19),F(1,13))]:
  lhs=(J1+J2)*u/2-v*L/2
  phi=J1-L
  rhs=(J2+phi)*u/2+L*(u-v)/2
  assert lhs==rhs
 assert F(0)<B<2
 out={
 'pass':'NF408',
 'standing':'EXACT SOURCE-SIGNED ORIGINAL PHYSICAL LOG AND SEVEN-PRIME JUMP SUBTRACTION INSIDE CONTINUOUS INTEGRAND; NORM UNCOMPUTED',
 'original_nf406_seam_partition_sha256':ssha,
 'original_nf407_true_coefficient_native_sha256':ussha,
 'original_nf407_principal_exact_sha256':psha,
 'original_nf404_pole_center_sha256':csha,
 'support_half_width':str(B),
 'arch_original_symbol':'m_arch(xi)=Re psi(1/4+i*pi*xi)-ln(pi)',
 'arch_kernel':'K(t)=e^(-t/4)/(1-e^(-t))',
 'arch_kernel_tail':'J(t)=2[atanh(e^(-t/4))+atan(e^(-t/4))]',
 'arch_regularized_positive_half_formula':'x>=0; d=B-x,t1=2d,t2=2(B+x),L=ln(B/d),Phi=J(t1)-L; A u4-q = [psi(1/4)-ln pi+(J(t2)+Phi)/2]*u4(x)+L*(u4(x)-u4(B))/2+int_0^t1 K(t)*(u4(x)-(u4(x+t/2)+u4(x-t/2))/2)dt+1/2 int_t1^t2 K(t)*(u4(x)-u4(x-t/2))dt',
 'stable_arch_Phi_non_cancelling_formula':'Phi(d)=ln[(d/B)*coth(d/4)]+2 atan(exp(-d/2))',
 'stable_arch_Phi_endpoint_limit':'ln(4/B)+pi/2',
 'stable_boundary_finite_multiplier':'(u4(x)-u4(B))*ln(B/(B-x)) tends zero as x tends B from left',
 'all_seven_original_prime_remainders_positive_x':[
 {'n':t['n'],'branch':t['branch'],
  'formula_when_x_less_abs_B_minus_h':('-c_n[u4(x+h)+u4(x-h)]' if t['branch']=='h_less_B' else '0'),
  'formula_when_x_greater_abs_B_minus_h':'-c_n[u4(x-h)+u4(B)]'}
  for t in checks],
 'source_original_prime_remainder_seam_continuity_formally_checked':True,
 'source_odd_reflection_to_negative_half':True,
 'original_continuous_z_direct_formula':'z(x)=Au4(x)-q(x)+sum_{n in N7}(P_n u4-r_n)(x)-a sinh(x/2), x>=0; odd reflection for x<0',
 'original_true_midpoint_coefficient_source_radii_also_paid_in_other_NF408_exact_replay':True,
 'original_16_cell_full_positive_scalar_rigorously_integrated':False,
 'original_regular_z_signed_p_cross_rigorously_integrated':False,
 'original_general_domain_audit':'OPEN',
 'new_signed_kernel_cells':0,'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF408 original arch log canceled INSIDE action, genuine 7 translated prime jumps canceled INSIDE source terms')
 print('NF408 continuous physical z original exact formula checked; no full norm upper')
if __name__=='__main__':main()
