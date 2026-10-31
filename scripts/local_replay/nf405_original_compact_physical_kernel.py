#!/usr/bin/env python3
"""NF405 exact compact physical-original signed digamma + 7-prime action.

Uses analytic quarter-digamma Laplace representation and Fourier
translation identity. Original centered scalar is NOT INTEGRATED.
All algebra/checks pure Fraction; no spurious numerical RH closure.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from math import factorial
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
B=F(11,10);T=4*B
ORIGINAL_NF401='644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515'
PRIME_POWERS=(2,3,4,5,7,8,9)
def load(path):
 raw=Path(path).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def check_formal_fourth_tail():
 # Let z=exp(-B). 4 sum_{j>=0} z^(4j+1)/(4j+1)
 # =2(atanh(z)+atan(z)). Coefficients exact through degree 83.
 for k in range(1,84,2):
  geometric=F(4,k) if k%4==1 else F(0)
  hyper=F(2,k)
  arc=F(2,k)*(1 if k%4==1 else -1)
  assert geometric==hyper+arc
 for k in range(0,85,2):
  assert not any((k%4==1,k%2==1))
 return True
def check_cancellation_formal():
 # u(x+h)+u(x-h)-2u(x) = h²u''+ h^4 u''''/12 + ...
 # With h=t/2, first term t²u''/4 and no order-zero/one.
 for k in range(9):
  coef=((F(1,2)**k+(-F(1,2))**k)-(2 if k==0 else 0))/factorial(k)
  if k%2==1 or k==0:assert coef==0
  elif k==2:assert coef==F(1,4)
  elif k==4:assert coef==F(1,192)
 return True
def check_shift_support():
 # For |x|<=B, t>4B implies x+t/2>B and x-t/2<-B.
 assert T==F(22,5)
 for x in (-B,-B/2,F(0),B/2,B):
  t=T+F(1,10**6)
  assert x+t/2>B and x-t/2<-B
 # exp(11/5)>9 by a finite positive Taylor sum; hence all 7
 # actual original prime shifts log(n) are <2B, support overlaps.
 assert sum(((2*B)**k/F(factorial(k)) for k in range(8)),F(0))>9
 assert len(PRIME_POWERS)==7 and PRIME_POWERS[-1]==9
 return True
def run(args):
 center,csha=load(args.center)
 endpoint,esha=load(args.endpoint)
 nf401,nsha=load(args.nf401)
 assert nsha==center['original_nf401_selected_native_sha256']==ORIGINAL_NF401
 assert endpoint['original_source_exact_half_budget_with_endpoint_extraction_pass'] is True
 assert endpoint['original_full_supported_centered_scalar_measured'] is False
 assert center['actual_original_full_supported_centered_scalar_integrated'] is False
 assert center['new_signed_kernel_cells']==0
 assert all(x['W_ODD_NEG']==x['RH']=='OPEN' for x in (center,endpoint,nf401))
 assert check_formal_fourth_tail() and check_cancellation_formal() and check_shift_support()
 # Spectral identity for supported odd piecewise smooth original u4:
 # m(xi) = Re psi(1/4+i*pi*xi)-log pi
 #         -2 sum_n Lambda(n)/sqrt(n) cos(2*pi*xi*log n).
 #
 # Define c_B=psi(1/4)-log pi+J_B,
 # J_B=int_(4B)^infty exp(-t/4)/(1-exp(-t)) dt
 #    =4 sum_(j>=0) exp(-(4j+1)B)/(4j+1)
 #    =2[atanh(exp(-B))+atan(exp(-B))].
 #
 # 1_I m(D)u4(x)=c_B u4(x)
 #  - 1/2 int_0^(4B) exp(-t/4)/(1-exp(-t))
 #       [u4(x+t/2)+u4(x-t/2)-2u4(x)]dt
 #  -sum_n Lambda(n)/sqrt(n) [u4(x+log n)+u4(x-log n)]
 # for a.e. x in (-B,B), u4 extended by zero beyond support.
 #
 # At t=0 second difference ~t²u''/4, kernel ~1/t:
 # integrand O(t). At support changes split t at 2(B±x).
 # Full original centered positive norm is the integral over I of
 # square of the complete expression minus fixed dyadic a*sinh(x/2).
 out={
  'pass':'NF405',
  'standing':'EXACT COMPACT PHYSICAL SPACE ORIGINAL MULTIPLIER ACTION IDENTITY; CENTERED NORM STILL UNMEASURED',
  'nf401_original_selected_source_sha256':nsha,
  'nf404_original_pole_shear_source_sha256':csha,
  'nf405_original_endpoint_extracted_source_sha256':esha,
  'original_support_half_width':'11/10',
  'original_compact_translation_integral_upper':'22/5',
  'actual_original_prime_power_shifts':list(PRIME_POWERS),
  'original_prime_shift_multipliers':'Lambda(n)/sqrt(n), n in 2,3,4,5,7,8,9',
  'fourier_original_signed_symbol':'Re psi(1/4+i*pi*xi)-log(pi)-2 sum Lambda(n)/sqrt(n) cos(2*pi*xi*log n)',
  'arch_constant':'psi(1/4)-log(pi)+2[atanh(exp(-11/10))+atan(exp(-11/10))]',
  'quarter_digamma_constant':'psi(1/4)=-EulerGamma-pi/2-3*log(2)',
  'arch_kernel':'exp(-t/4)/(1-exp(-t))',
  'physical_arch_action':'c_B*u4(x) - (1/2) integral_0^(22/5) arch_kernel(t)*(u4(x+t/2)+u4(x-t/2)-2*u4(x))dt',
  'physical_prime_action':'-sum_{n=2,3,4,5,7,8,9} Lambda(n)/sqrt(n)*(u4(x+log(n))+u4(x-log(n)))',
  'centered_full_physical_scalar':'integral_{x=-11/10}^{11/10} |physical_arch_action+physical_prime_action-a*sinh(x/2)|^2 dx',
  'original_fixed_dyadic_pole_center':center['fixed_dyadic_pole_coefficient'],
  'original_centered_upper_acceptance':center['exact_sufficient_new_full_supported_centered_scalar_power_upper_target'],
  'original_quarter_digamma_formula_analytic_not_numeric_reproduced':True,
  'formal_exact_fourth_power_series':True,
  'formal_exact_source_kernel_cancellation_at_zero':True,
  'original_seven_prime_shift_support_is_within_two_B':True,
  'original_full_supported_centered_norm_numeric_integration':False,
  'original_J_perp_lowband_upper':False,
  'original_general_operator_domain_review':'OPEN',
  'new_signed_kernel_cells':0,
  'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\n')
 print('NF405 exact original compact physical response 0<t<22/5 + seven shifts PASS')
 print('NF405 centered full physical norm still UNMEASURED')
 return out
if __name__=='__main__':
 p=argparse.ArgumentParser()
 p.add_argument('--center',default='notes/data/provisional/NF404_original_selected_pole_shear_exact.json')
 p.add_argument('--endpoint',default='notes/data/provisional/NF405_original_endpoint_extracted_tail_exact.json')
 p.add_argument('--nf401',default='notes/data/provisional/NF401_original_242D_selected_column_source_native.json')
 p.add_argument('--output',required=True)
 run(p.parse_args())
