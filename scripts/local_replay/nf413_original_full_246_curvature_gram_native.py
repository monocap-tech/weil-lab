#!/usr/bin/env python3
"""NF413: FULL original 242 selected + 4 critical correlated physical u4'' Gram.

Exact dyadic aggregation of all selected x^k sin/cos and all four critical
32-sine/pole source functions, with all mixed correlations retained.
4096-bit outward Arb analytic full physical Gram; no x quadrature.

DOES NOT evaluate the remaining arch t integral, continuous z, or full scalar.
"""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);MAXDEG=32
def read(p):
 raw=Path(p).read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def dyad(v):
 n,e=int(v[0]),int(v[1])
 return F(n*2**e) if e>=0 else F(n,2**(-e))
def A(v):return arb(str(v))
def ceil_bound(z):
 b=1
 while not (z<arb(b)):
  b*=2
  assert b<10**300,("source curvature bound exceeds practical interval capacity",str(z)[:160])
 return b
class Moments:
 def __init__(self,pi):
  self.pi=pi;self.cache={};self.pole={}
 def get(self,f,n,kind):
  assert 0<=n<=MAXDEG
  assert (n%2==0 if kind=="c" else n%2==1)
  if f==0:
   return A(F(2)*B**(n+1)/F(n+1)) if kind=="c" else arb(0)
  if f not in self.cache:
   sn,co=A(2*f*B).sin_cos_pi()
   omega=2*self.pi*A(f)
   self.cache[f]=([2*sn/omega],[],sn,co,omega)
  cs,ss,sn,co,om=self.cache[f]
  while (len(cs)-1)*2<n if kind=="c" else len(ss)*2-1<n:
   # Build alternating S_(2k+1),C_(2k+2) from C_(2k).
   k=len(ss)
   j=2*k+1
   sj=(-2*A(B**j)*co+j*cs[k])/om
   ss.append(sj)
   j+=1
   cj=(2*A(B**j)*sn-j*sj)/om
   cs.append(cj)
  return cs[n//2] if kind=="c" else ss[(n-1)//2]
 def pole_overlap(self,f,m):
  key=(f,m)
  if key in self.pole:return self.pole[key]
  # ∫ phi(x)sinh(x/2) dx = ∫ phi(x)exp(x/2)dx
  # because phi is odd, over [-B,B]. Valid for x^m sin(m even)
  # or x^m cos(m odd).
  z=acb(A(F(1,2)),2*self.pi*A(f))
  bz=A(B); ep=(z*bz).exp(); en=(-z*bz).exp()
  prev=(ep-en)/z
  for k in range(1,m+1):
   prev=(A(B**k)*ep-A((-B)**k)*en-k*prev)/z
  res=prev.imag if m%2==0 else prev.real
  self.pole[key]=res
  return res
 def gram(self,a,b):
  fa,ma=a; fb,mb=b;n=ma+mb
  if ma%2==0 and mb%2==0:
   return (self.get(fa-fb,n,"c")-self.get(fa+fb,n,"c"))/2
  if ma%2==1 and mb%2==1:
   return (self.get(fa-fb,n,"c")+self.get(fa+fb,n,"c"))/2
  if ma%2==0:
   return (self.get(fa+fb,n,"s")+self.get(fa-fb,n,"s"))/2
  return (self.get(fa+fb,n,"s")+self.get(fb-fa,n,"s"))/2
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
 p.add_argument("--radius",default="notes/data/provisional/NF408_original_source_midpoint_action_error_exact.json")
 p.add_argument("--jet",default="notes/data/provisional/NF411_original_source_boundary_jet.json")
 p.add_argument("--parent",default="notes/data/provisional/NF412_original_full_source_triangle_stop.json")
 p.add_argument("--output",required=True)
 args=p.parse_args()
 source,source_sha=read(args.source)
 radius,radius_sha=read(args.radius)
 jet,jet_sha=read(args.jet)
 parent,parent_sha=read(args.parent)
 assert source["original_dimension"]==242
 assert len(source["original_selected_generator_node_orders"])==242
 assert len(source["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
 assert len(source["original_source_critical_sine_frequencies"])==32
 assert radius["original_nf407_coefficient_native_sha256"]==source_sha
 assert jet["nf407_source_sha256"]==source_sha
 assert jet["source_derivative_nonzero_certified"]
 assert parent["original_nf407_original_full_source_sha256"]==source_sha
 assert parent["selected_source_generators_included"]==242
 assert all(v["W_ODD_NEG"]==v["RH"]=="OPEN" for v in (source,radius,jet,parent))
 ctx.prec=4096;pi=arb.pi()
 # ORIGINAL unrounded full physical source: aggregate all 242 selected and
 # 4 critical exact dyadic midpoints at common physical generator keys.
 original={}; pole=F(0);S2=F(0)
 def add(f,k,a):
  key=(f,k);original[key]=original.get(key,F(0))+a
 def curvweight(f,k):
  w=7*abs(f)
  return ((k*(k-1)*B**(k-2) if k>=2 else 0)
          +(2*k*w*B**(k-1) if k else 0)+w*w*B**k)
 for (freq,k),(mid,rad) in zip(source["original_selected_generator_node_orders"],
                              source["original_exact_native_raw_selected_coefficients_mid_radius"]):
  val=dyad(mid);err=abs(dyad(rad))
  if freq=="pole":
   pole+=val;S2+=err/4
  else:
   ff=F(freq)
   assert k is not None and k>=0 and k<=13
   add(ff,k,val)
   S2+=err*curvweight(ff,k)
 for (mid,rad),shape in zip(source["original_exact_native_original_four_critical_coefficients_mid_radius"],
                           source["original_source_critical_sines_and_pole_coefficients"]):
  alpha=dyad(mid);err=abs(dyad(rad))
  for freq,coeff in zip(source["original_source_critical_sine_frequencies"],shape["sine_coefficients"]):
   ff=F(freq);q=F(coeff)
   add(ff,0,alpha*q)
   S2+=err*abs(q)*curvweight(ff,0)
  q=F(shape["sinh_coefficient"])
  pole+=alpha*q;S2+=err*abs(q)/4
 assert S2<F(1,10**735),("original second derivative source uncertainty too large",str(S2)[:130])
 assert len(original)>=67 and all(k>=0 for f,k in original)
 # Original source value/derivative at B independent NF411 check.
 x=A(B);ub=A(pole)*(x/2).sinh();db=A(pole)*(x/2).cosh()/2
 for (f,k),v in sorted(original.items()):
  if not v:continue
  sn,co=A(2*f*B).sin_cos_pi()
  wt=2*pi*A(f);coeff=A(v);power=A(B**k)
  if k%2==0:
   ub+=coeff*power*sn
   db+=coeff*(A(k*B**(k-1))*sn if k else arb(0))
   db+=coeff*power*wt*co
  else:
   ub+=coeff*power*co
   db+=coeff*(A(k*B**(k-1))*co-co*0)  # zero term retains odd parity
   db-=coeff*power*wt*sn
 v_source=arb(jet["original_original_source_value_at_B_arb"])
 d_source=arb(jet["original_original_source_derivative_at_B_arb"])
 # Independent identical source formulas must OVERLAP native endpoint balls.
 assert not (ub<v_source or ub>v_source),("NF411 endpoint value mismatch",str(ub)[:150])
 assert not (db<d_source or db>d_source),("NF411 endpoint slope mismatch",str(db)[:150])
 # Second derivative amplitudes: original odd basis x^even sin, x^odd cos.
 # Aggregate all 246 first, including common frequency cancels, then
 # derivatives and all exact physical cross terms.
 derived={}
 def dadd(key,v):derived[key]=derived.get(key,arb(0))+v
 for (f,k),q in sorted(original.items()):
  if not q:continue
  C=A(q);w=2*pi*A(f)
  if k>=2:dadd((f,k-2),C*k*(k-1))
  if k>=1:
   dadd((f,k-1),C*2*k*w*(1 if k%2==0 else -1))
  dadd((f,k),-C*w*w)
 terms=[(key,z) for key,z in sorted(derived.items()) if z!=0]
 assert len(terms)>=200
 M=Moments(pi)
 E=arb(0)
 for i,(u,coef) in enumerate(terms):
  E+=coef*coef*M.gram(u,u)
  for v,cj in terms[:i]:
   E+=2*coef*cj*M.gram(u,v)
 pole2=A(pole)/4
 cross=arb(0)
 for (f,k),coef in terms:
  cross+=coef*M.pole_overlap(f,k)
 E+=2*pole2*cross+pole2*pole2*(A(B).sinh()-A(B))
 assert E>0,("correlated full original source curvature Gram unresolved",str(E)[:200])
 assert E<arb(10)**200,("still large full source Gram",str(E)[:200])
 true_curv=E.sqrt()+A(F(3,2)*S2)
 u2_bound=ceil_bound(true_curv)
 # Compare parent full 246-term triangle bound, to ensure entire source
 # correlation is preserved and the rigorous new upper is indeed stronger.
 orig_tri=F(parent["true_original_full_source_second_derivative_L2_triangle_upper_exact"])
 assert true_curv<A(orig_tri)
 small=[]
 for h in (F(1,10**10),F(1,10**12),F(1,10**14)):
  positive=F(u2_bound)*h*h/8
  full=F(3,2)*positive # sqrt(2)<3/2, both odd halves
  small.append({"h_exact":str(h),"positive_half_I0_L2_upper_exact":str(positive),
        "whole_odd_I0_L2_upper_exact":str(full),
        "whole_odd_I0_under_eps_over_8":full<F(9,8*10**17)})
 out={
 "pass":"NF413",
 "standing":"4096-BIT OUTWARD FULL ORIGINAL 242+4 PHYSICAL SOURCE u4 SECOND DERIVATIVE GRAM; NEAR-t I0 CERTIFIED ONLY, ORIGINAL z UNINTEGRATED",
 "original_nf407_full_native_source_sha256":source_sha,
 "original_nf408_first_order_radius_parent_sha256":radius_sha,
 "original_nf411_independent_jet_sha256":jet_sha,
 "original_nf412_triangle_parent_sha256":parent_sha,
 "original_selected_generators":242,
 "original_critical_generator_blocks":4,
 "original_critical_sine_frequencies":32,
 "same_original_physical_terms_after_exact_rational_consolidation":len(original),
 "original_nonzero_physical_second_derivative_basis_terms":len(terms),
 "all_246_original_selected_selected_selected_critical_critical_critical_cross_preserved":True,
 "entire_original_pole_and_poly_sine_cos_included":True,
 "source_native_4096bit_midpoint_correlated_original_second_derivative_L2_squared_Arb":str(E),
 "native_second_derivative_source_coefficient_radii_uniform_exact":str(S2),
 "native_second_derivative_error_paid_in_L2_by_3S2_over_2":True,
 "original_true_full_u4_second_derivative_L2_upper_integer":str(u2_bound),
 "independent_NF411_original_endpoint_value_overlap":True,
 "independent_NF411_original_endpoint_derivative_overlap":True,
 "original_small_t_I0_physical_enclosures":small,
 "other_arch_t_integrals_rigorously_integrated":False,
 "original_continuous_z_cells_6_3_7_certified":False,
 "complete_original_centered_norm_certified":False,
 "NF404_cap_decided":False,
 "W_ODD_NEG":"OPEN","RH":"OPEN"
 }
 target=Path(args.output);target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(json.dumps(out,indent=2)+"\n")
 print("NF413 FULL original physical u4'' L2² interval",str(E)[:100],flush=True)
 print("NF413 original full curvature strict integer upper",u2_bound,flush=True)
 print("NF413 full original near-t fees",[(i["h_exact"],i["whole_odd_I0_under_eps_over_8"]) for i in small],flush=True)
 print("NF413 original continuous z, full centered scalar, RH OPEN",flush=True)
if __name__=="__main__":main()
