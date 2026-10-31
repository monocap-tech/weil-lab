#!/usr/bin/env python3
"""NF412: source-correlated physical Gram for the original critical source f4''.

All 4 original critical source coefficients are combined in exact Fraction
BEFORE any absolute bound. The 32 sine features + odd pole are then contracted
against their analytic full physical second-derivative Gram at 4096-bit Arb.

Does NOT control true u4 curvature: essential 242 selected terms are absent from Gram.
nested integral or the complete continuous z.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10)
def read(path):
 raw=Path(path).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def dyad(x):
 n,e=int(x[0]),int(x[1])
 return F(n*(2**e)) if e>=0 else F(n,2**(-e))
def A(x):return arb(str(x))
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
 p.add_argument("--curvature",default="notes/data/provisional/NF374_original_correlated_curvature_native.json")
 p.add_argument("--radius",default="notes/data/provisional/NF408_original_source_midpoint_action_error_exact.json")
 p.add_argument("--center",default="notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
 p.add_argument("--output",required=True)
 a=p.parse_args()
 source,ssha=read(a.source);curv,csha=read(a.curvature)
 radius,rsha=read(a.radius);center,centsha=read(a.center)
 assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
 assert len(source["original_source_critical_sines_and_pole_coefficients"])==4
 assert len(source["original_source_critical_sine_frequencies"])==32
 assert radius["original_nf407_coefficient_native_sha256"]==ssha
 assert curv["working_precision_bits"]==4096
 assert source["original_dimension"]==242
 assert all(d["W_ODD_NEG"]==d["RH"]=="OPEN" for d in (source,curv,radius,center))
 ctx.prec=4096
 freqs=[F(t) for t in source["original_source_critical_sine_frequencies"]]
 critical_coeff=[]
 pole=F(0)
 for midrad,shape in zip(source["original_exact_native_original_four_critical_coefficients_mid_radius"],source["original_source_critical_sines_and_pole_coefficients"]):
  alpha=dyad(midrad[0])
  critical_coeff.append([alpha*F(t) for t in shape["sine_coefficients"]])
  pole+=alpha*F(shape["sinh_coefficient"])
 combined=[sum((v[j] for v in critical_coeff),F(0)) for j in range(32)]
 # The original physical critical f4 = sum_j combined_j sin(2*pi*freq_j*x)
 # +pole*sinh(x/2). Its second derivative has these exact source coefficients.
 pi=arb.pi()
 s2=[-A(combined[j])*(2*pi*A(freqs[j]))**2 for j in range(32)]
 pp=A(pole)/4
 def sine_overlap(fi,fj):
  # Integral[-B,B] sin(2pi fi x) sin(2pi fj x)dx
  # =S(fi-fj)-S(fi+fj), S(w)=sin(2pi w B)/(2pi w), S(0)=B
  def S(w):
   if w==0:return A(B)
   sn,_=(A(2*w*B)).sin_cos_pi()
   return sn/(2*pi*A(w))
  return S(fi-fj)-S(fi+fj)
 def sine_sinh(fi):
  # Integral[-B,B] sin(k x) sinh(x/2) dx
  k=2*pi*A(fi)
  sn,cs=(A(2*fi*B)).sin_cos_pi()
  a0=A(F(1,2))
  return 2*(a0*(A(B)/2).cosh()*sn-k*(A(B)/2).sinh()*cs)/(a0*a0+k*k)
 # Pairwise physical Gram is evaluated *after* exact source correlation.
 ss=arb(0)
 for i in range(32):
  ss+=s2[i]*s2[i]*sine_overlap(freqs[i],freqs[i])
  for j in range(i):
   ss+=2*s2[i]*s2[j]*sine_overlap(freqs[i],freqs[j])
 cross=sum((s2[i]*sine_sinh(freqs[i]) for i in range(32)),arb(0))
 pole_power=(A(B).sinh()-A(B))
 full=ss+2*pp*cross+pp*pp*pole_power
 # Can fail if precision insufficient for the original 1e92 cancellation;
 # never widen a potentially negative computed square to an invented positive bound.
 assert full>=arb(0),("original critical second derivative Gram did not resolve",str(full)[:300])
 # Accepted NF374 true original exterior w4'' L2 squared is <9e-12.
 w4=arb(curv["nf374_curvature"][3]["whole_interval_second_derivative_L2_squared"][0])
 assert w4>0 and w4<arb("9e-12")
 assert F(radius["original_native_coefficient_derivative_error_uniform_D"])<F(1,10**750)
 # Source-native u4 is f4-w4; use the validated original 4th exterior curvature.
 ctrue=full.sqrt()+arb("3e-6")
 # Pay a fresh *second*-derivative source-native radius in exact rationals.
 # Use 2*pi*|freq|<7*|freq|, |sinh(x/2)|<1, all x in [-B,B].
 S2=F(0)
 for (freq,k),(mid,rad) in zip(source["original_selected_generator_node_orders"],
                              source["original_exact_native_raw_selected_coefficients_mid_radius"]):
  rr=abs(dyad(rad))
  if freq=="pole":
   assert k is None
   S2+=rr/F(4)
  else:
   omega=7*abs(F(freq))
   S2+=rr*((k*(k-1)*B**(k-2) if k>=2 else 0)
       +(2*k*omega*B**(k-1) if k else 0)+omega*omega*B**k)
 for (mid,rad),shape in zip(source["original_exact_native_original_four_critical_coefficients_mid_radius"],
                            source["original_source_critical_sines_and_pole_coefficients"]):
  rr=abs(dyad(rad))
  S2+=rr*(sum((abs(F(v))*(7*abs(w))**2 for v,w in
                 zip(shape["sine_coefficients"],freqs)),F(0))
          +abs(F(shape["sinh_coefficient"]))/4)
 assert S2<F(1,10**735),("source second derivative uncertainty large",str(S2)[:120])
 ctrue+=A(F(3,2)*S2)
 bound=1
 while not (ctrue<arb(bound)):
  bound*=2
  assert bound<10**300
 h=F(1,10**10)
 small=F(bound)*h*h/8
 # K(t)=exp(-t/4)/(1-exp(-t)) < 2/t for 0<t<=h.
 # 1/2 sym difference <= t²/8 |u''| in L2 over valid interior x.
 # Thus ||int_0^min(h,2(B-x)) K(t)*(u-(u_++u_-)/2) dt||_L2(0,B)
 # <= h²/8 * ||u''||_L2(-B,B).
 eps=F(9,10**17)
 out={
 "pass":"NF412",
 "standing":"FOUR-CRITICAL ONLY GRAM DIAGNOSTIC; MISSING ORIGINAL 242 SELECTED CROSS AND NO TRUE SMALL-t SOURCE BUDGET",
 "original_nf407_native_source_sha256":ssha,
 "original_nf374_fourth_exterior_curvature_sha256":csha,
 "original_nf408_source_first_derivative_radius_sha256":rsha,
 "original_nf404_center_sha256":centsha,
 "critical_source_dimension":4,"critical_sine_count":32,
 "all_four_original_critical_coefficients_combined_exactly_before_gram":True,
 "original_midpoint_critical_f4_second_derivative_squared_L2_arb":str(full),
 "original_original_exterior_w4_second_derivative_L2_squared_under":"9e-12",
 "original_native_second_derivative_radius_sup_S2_exact":str(S2),
 "original_true_second_derivative_source_radius_paid":True,
 "missing_242_selected_critical_cross_covariance":True,
 "former_true_u4_curvature_interpretation_invalid":True,
 "original_midpoint_u4_second_derivative_L2_upper_integer":str(bound),
 "original_small_t_cutoff_h_exact":str(h),
 "original_midpoint_near_t_zero_arch_I0_L2_upper":str(small),
 "conditional_midpoint_near_t_bound_below_eps_quarter":small<eps/4,
 "original_native_source_second_derivative_radius_paid":True,
 "original_true_u4_second_derivative_L2_bound_certified":False,
 "original_true_near_t_L2_bound_certified":False,
 "original_remaining_arch_t_quadrature_certified":False,
 "original_z_cell_6_3_7_interval_certified":False,
 "original_full_centered_scalar_certified":False,
 "NF404_gate_decided":False,
 "W_ODD_NEG":"OPEN","RH":"OPEN"
 }
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+"\n")
 print("NF412 midpoint-correlated critical curvature squared:",str(full)[:85])
 print("NF412 INVALID critical-only surrogate upper",bound,"small-t kernel charge",float(small))
 print("NF412 242+4 source correlation missing: true tiny-t arch, z and scalar UNDECIDED")
if __name__=="__main__":main()
