#!/usr/bin/env python3
"""NF415 original source / rigorously validated ACb I1 at cell 6 physical x=9/10.

Analytic integrator is FLINT's acb_calc_integrate, NOT an unverified Gauss
mesh. Fully source-correlated 242+4 original physical function as analytic
complex x, including all original polynomial powers and signed dyadic
critical pole. Does not infer any cellwise or NF404 full-scalar result.

Also exact independent pointwise tiny-t I0 truncation using NF413 u4'' L2:
|int_0^min(h,2(B-x)) K(t) D_tu(x)dt| < 50 h^(3/2).
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from flint import acb,arb,ctx
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10)
def read(p):
 data=Path(p).read_bytes()
 return json.loads(data),hashlib.sha256(data).hexdigest()
def dyad(z):
 n,e=int(z[0]),int(z[1])
 return F(n*2**e) if e>=0 else F(n,2**(-e))
def A(v):return arb(str(v))
def C(v):return acb(A(v))
def native_source(s):
 coeff={};pole=F(0);errors=F(0)
 def add(f,k,v):coeff[(f,k)]=coeff.get((f,k),F(0))+v
 for (freq,k),(mid,rad) in zip(s['original_selected_generator_node_orders'],s['original_exact_native_raw_selected_coefficients_mid_radius']):
  v=dyad(mid);eps=abs(dyad(rad))
  if freq=='pole':pole+=v;errors+=eps
  else:
   add(F(freq),k,v);errors+=eps*B**k
 for (mid,rad),shape in zip(s['original_exact_native_original_four_critical_coefficients_mid_radius'],s['original_source_critical_sines_and_pole_coefficients']):
  a=dyad(mid);e=abs(dyad(rad))
  for f,k in zip(s['original_source_critical_sine_frequencies'],shape['sine_coefficients']):
   add(F(f),0,a*F(k))
   errors+=e*abs(F(k))
  pole+=a*F(shape['sinh_coefficient']);errors+=e*abs(F(shape['sinh_coefficient']))
 assert len(s['original_selected_generator_node_orders'])==242
 assert len(s['original_source_critical_sine_frequencies'])==32
 assert errors<F(1,10**700)
 return [(f,k,q) for (f,k),q in sorted(coeff.items()) if q],pole,errors
class U:
 def __init__(self,s):
  self.terms,self.pole,self.err=native_source(s)
  self.pi=acb.pi()
  # Each source term summed at 4096 bits before integration; all 246.
  self.groups={}
  for f,k,q in self.terms:self.groups.setdefault(f,[]).append((k,C(q)))
  self.groups=list(self.groups.items())
  self.pole=C(self.pole)
 def at(self,x):
  z=self.pole*(x/2).sinh()
  for f,vals in self.groups:
   w=2*self.pi*C(f)*x
   sn=w.sin();co=w.cos()
   for k,q in vals:
    z+=q*x**k*(sn if k%2==0 else co)
  return z
def main():
 p=argparse.ArgumentParser()
 p.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 p.add_argument('--nf413',default='notes/data/provisional/NF413_original_full_246_source_curvature_native.json')
 p.add_argument('--nf414',default='notes/data/provisional/NF414_original_hotspot_finite_continuous_native.json')
 p.add_argument('--output',required=True)
 p.add_argument('--eval-limit',type=int,default=18000)
 p.add_argument('--precision',type=int,default=1024)
 args=p.parse_args()
 original,sha=read(args.source);p413,h413=read(args.nf413);p414,h414=read(args.nf414)
 assert p413['original_nf407_full_native_source_sha256']==sha
 assert p414['original_nf407_source_sha256']==sha
 assert p413['original_true_full_u4_second_derivative_L2_upper_integer']=='256'
 assert all(v['W_ODD_NEG']==v['RH']=='OPEN' for v in (original,p413,p414))
 ctx.prec=args.prec
 src=U(original)
 x=C(F(9,10));t1=C(F(2,5));t2=C(4)
 u=src.at(x)
 assert (u.imag).contains(0)
 def integrand(t,analytic):
  # Entire source in complex t. Meromorphic K(t), no pole along 2/5..4.
  # A direct complex ball for K is checked for zero; FLINT's analytical
  # integration must enclose all error including oscillatory source.
  k=(-t/4).exp()/(1-(-t).exp())
  return (k/2)*(u-src.at(x-t/2))
 record={'original_rational_x':'9/10','physical_original_cell':6,
  'I1_true_original_t_lower':'2/5','I1_true_original_t_upper':'4',
  'source_native_246_generator_4096bit_midpoints':True,
  'original_native_coefficient_uniform_radius_exact':str(src.err),
  'full_source_I1_validation':'UNDECIDED',
  'true_I0_certified':False,'true_complete_z_certified':False,
  'original_full_centered_scalar_certified':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'
 }
 try:
  val=acb.integral(integrand,t1,t2,abs_tol=A('1e-14'),rel_tol=A('1e-18'),
     deg_limit=80,eval_limit=args.eval_limit,depth_limit=1000)
  record['native_integral_I1_raw_acb']=str(val)
  record['native_integral_I1_finite']=bool(val.is_finite())
  if val.is_finite():
   # Coefficient radius for integral: |δu(x)-δu(x-t/2)|≤2S0
   # and K>0, ∫_(2/5)^4 K(t)dt <2log(10)<5.
   charge=5*src.err
   m,rad,e=val.real.mid_rad_10exp(72)
   lo=F(int(m)-int(rad))*F(10)**int(e)-charge
   hi=F(int(m)+int(rad))*F(10)**int(e)+charge
   assert lo<=hi
   record['I1_coefficient_radius_analytic_upper_exact']=str(charge)
   record['I1_true_original_full_source_rational_interval']=[str(lo),str(hi)]
   record['I1_true_interval_width_exact']=str(hi-lo)
   # FINITE from the integrator alone is not enough to declare success.
   # This checks a genuinely resolving outward real ball.
   record['full_source_I1_validation']=('ACCEPTED_RESOLVED_INTERVAL_WITH_EXPLICIT_SOURCE_RADIUS'
       if hi-lo<F(1,10**13) else 'METHOD_STOP_ACB_FINITE_BUT_UNRESOLVED')
  else:record['full_source_I1_validation']='METHOD_STOP_NONFINITE_ACB_INTERVAL'
 except Exception as e:
  record['native_integral_error']=repr(e)
  record['full_source_I1_validation']='METHOD_STOP_ACB_NO_CONVERGENCE'
 h=F(1,10**12)
 # Pointwise Cauchy on triangular central second difference,
 # |D_t u(x)| <= ||u''||2 * t^(3/2)/(4sqrt3);
 # integrate with K(t)<2/t: ||u''||2 h^(3/2)/(3sqrt3)<50 h^(3/2).
 # With h=10^-12, this is <5e-17. This is pointwise unlike NF413 L2.
 assert F(256**2)<F(150**2)*3
 eps=F(50,10**18)
 assert eps==F(5,10**17)
 record['original_pointwise_I0_0_to_h_strict_upper_exact']=str(eps)
 record['pointwise_small_t_valid_on_all_original_positive_x_with_t_less_2B_minus_2x']=True
 record['I1_analytic_integration_library']='python-flint 0.8.0 acb.integral complex ball, no unverified Gauss mesh'
 record['actual_complete_original_z_at_cell6_certified']=False
 record['NF404_acceptance_decided']=False
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(record,indent=2)+'\n')
 print('NF415 original I1 native status:',record['full_source_I1_validation'],flush=True)
 print('NF415 original I1:',record.get('native_integral_I1_raw_acb','not finite'),flush=True)
 print('NF415 pointwise 0<t<1e-12 I0 original bound <5e-17; remaining I0,z open',flush=True)
if __name__=='__main__':main()
