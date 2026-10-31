#!/usr/bin/env python3
"""NF409 two-form numerical identity test for TRUE original physical action.

Reconstruct source from authenticated NF407 4096-bit coefficients, compute
the original NF408 full compact physical m(D) action independently and
the NF408 analytically regularized continuous z directly (without forming
q or r in its individual arch/prime terms). Compare both at x=.55 and 1.09.

IMPORTANT: approximately represented Gauss nodes, inner quadrature
truncation, coefficient midpoints and evaluated real transcendental
functions are NOT rigorous interval enclosures. No original norm proof.
"""
import argparse,json,time
from pathlib import Path
from fractions import Fraction as F
import mpmath as mp
from nf408_original_compact_physical_action_pilot import Source,evaluate,read,rat,gauss_integral,kernel,arch_tail,N7

def stable(x,s,step,n,lower_t):
 B=s.B;d=B-x;t1=2*d;t2=2*(B+x)
 assert 0<x<B
 u=s.at(x);v=s.at(B)
 L=mp.log(B/d)
 J2=arch_tail(t2)
 phi=mp.log((d/B)*mp.coth(d/4))+2*mp.atan(mp.exp(-d/2))
 c0=mp.digamma(mp.mpf(1)/4)-mp.log(mp.pi)
 def kern0(t):
  yp=s.at(x+t/2);ym=s.at(x-t/2)
  return kernel(t)*(u-(yp+ym)/2)
 def kern1(t):
  ym=s.at(x-t/2)
  return kernel(t)*(u-ym)/2
 i0,nn0=gauss_integral(kern0,lower_t,t1,step,n)
 i1,nn1=gauss_integral(kern1,t1,t2,step,n)
 arch_minus_q=(c0+(J2+phi)/2)*u+(L/2)*(u-v)+i0+i1
 prime_minus_r=mp.mpf(0)
 parts=[]
 for k,base in N7.items():
  lag=mp.log(k);w=mp.log(base)/mp.sqrt(k);xk=abs(B-lag)
  if x<xk and lag<B:
   contribution=-w*(s.at(x+lag)+s.at(x-lag))
   branch="both-shifts"
  elif x<xk and lag>B:
   contribution=mp.mpf(0)
   branch="neither-shift"
  else:
   contribution=-w*(s.at(x-lag)+v)
   branch="continuous-post-seam"
  prime_minus_r+=contribution
  parts.append({'n':k,'branch':branch,'value':mp.nstr(contribution,48)})
 a=rat(F(6677356497477490213,4611686018427387904))
 z=arch_minus_q+prime_minus_r-a*mp.sinh(x/2)
 q=v/2*L
 r=v*sum((mp.log(base)/mp.sqrt(k) for k,base in N7.items()
           if x>abs(B-mp.log(k))),mp.mpf(0))
 return {'arch_minus_q':mp.nstr(arch_minus_q,60),
         'prime_minus_r':mp.nstr(prime_minus_r,60),
         'z_direct_continuous':mp.nstr(z,60),
         'q':mp.nstr(q,60),'r':mp.nstr(r,60),
         'direct_reconstructed_g':mp.nstr(z+q+r,60),
         'stable_Phi':mp.nstr(phi,50),
         'original_source_u':mp.nstr(u,50),
         'original_endpoint_v':mp.nstr(v,50),
         'integrand_quadrature_evaluations':nn0+nn1,
         'all_seven_original_signed_prime_branches':parts}

def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 p.add_argument('--prior',default='notes/data/provisional/NF408_original_continuous_action_exact.json')
 p.add_argument('--dps',type=int,default=205)
 p.add_argument('--nodes',type=int,default=16)
 p.add_argument('--step',default='1/40')
 p.add_argument('--min-t',default='1/10000000000')
 p.add_argument('--output',required=True)
 a=p.parse_args();t=time.monotonic()
 source,ssha=read(a.source);seams,seamsha=read(a.seams);prior,psha=read(a.prior)
 assert source['original_dimension']==242
 assert prior['original_nf407_true_coefficient_native_sha256']==ssha
 assert prior['original_nf406_seam_partition_sha256']==seamsha
 assert seams['number_of_open_physical_support_cells']==16
 assert all(v['W_ODD_NEG']==v['RH']=='OPEN' for v in (source,seams,prior))
 assert a.dps>=205 and a.nodes>=12
 mp.mp.dps=a.dps
 s=Source(source)
 reports=[]
 for x in ['11/20','109/100']:
  original=evaluate(x,s,rat(a.step),a.nodes,rat(a.min_t))
  stableval=stable(rat(x),s,rat(a.step),a.nodes,rat(a.min_t))
  d=abs(mp.mpf(original['original_continuous_z_x'])-mp.mpf(stableval['z_direct_continuous']))
  gdiff=abs(mp.mpf(original['original_centered_g_x'])-mp.mpf(stableval['direct_reconstructed_g']))
  # Old quadrature integrates +u*K/2 on [t1,t2]; stable exact algebra
  # evaluates that whole term as u*(J(t1)-J(t2))/2. Calibrate Gauss
  # quadrature's actual error on the known kernel, not source.
  xx=rat(x);t1=2*(s.B-xx);t2=2*(s.B+xx)
  Kq,_=gauss_integral(kernel,t1,t2,rat(a.step),a.nodes)
  Kexact=arch_tail(t1)-arch_tail(t2)
  calibration=s.at(xx)*(Kq-Kexact)/2
  residual=(mp.mpf(original['original_continuous_z_x'])-
            mp.mpf(stableval['z_direct_continuous']))-calibration
  # Original result is displayed to 45 significant figures.
  assert abs(residual)<mp.mpf('1e-38'), 'two-form difference not explained by known Gauss K quadrature error'
  assert len(stableval['all_seven_original_signed_prime_branches'])==7
  reports.append({'x':x,'original_old_direct_g':original['original_centered_g_x'],
        'original_old_subtraction_z':original['original_continuous_z_x'],
        'original_new_continuous_z':stableval['z_direct_continuous'],
        'original_new_reconstructed_g':stableval['direct_reconstructed_g'],
        'difference_z_two_form':mp.nstr(d,50),
        'difference_g_two_form':mp.nstr(gdiff,50),
        'known_K_Gauss_kernel_error_calibration':mp.nstr(calibration,50),
        'difference_minus_K_Gauss_kernel_error':mp.nstr(residual,50),
        'source_original_u':stableval['original_source_u'],
        'stable_source_Phi':stableval['stable_Phi'],
        'source_original_all_prime_branches':stableval['all_seven_original_signed_prime_branches'],
        'original_new_arch_minus_q':stableval['arch_minus_q'],
        'original_new_prime_minus_r':stableval['prime_minus_r']})
  print('NF409 original two-form x=',x,'z=',stableval['z_direct_continuous'],'delta=',mp.nstr(d,7),flush=True)
 out={'pass':'NF409',
  'standing':'ORIGINAL TRUE PHYSICAL CONTINUOUS z TWO-FORM 205-DIGIT GAUSS EQUIVALENCE, NOT RIGOROUS QUADRATURE CERTIFICATE',
  'original_nf407_source_coeff_sha256':ssha,
  'original_nf406_seam_sha256':seamsha,
  'original_nf408_analytic_continuous_action_sha256':psha,
  'source_true_original_242plus4_native_coefficient_midpoints':True,
  'original_complete_real_seven_prime_source_restored':True,
  'original_analytic_plus_numeric_different_forms_compared':True,
  'difference_calibrated_against_unbounded_K_Gauss_quadrature_error':True,
  'original_two_form_samples':reports,
  'gauss_nested_t_integrals_numerically_approximated':True,
  'arbitrary_transcendental_roundoff_certified':False,
  'original_pointwise_error_enclosure_certified':False,
  'original_x_integral_and_complete_centered_norm_certified':False,
  'original_domain_general_audit':'OPEN',
  'new_signed_kernel_cells':0,'W_ODD_NEG':'OPEN','RH':'OPEN',
  'elapsed_seconds':round(time.monotonic()-t,2)}
 dst=Path(a.output);dst.parent.mkdir(parents=True,exist_ok=True)
 dst.write_text(json.dumps(out,indent=2)+'\n')
 print('NF409 ORIGINAL PHYSICAL stable action two-form pilot PASS; no physical L2 certificate')
if __name__=='__main__':main()
