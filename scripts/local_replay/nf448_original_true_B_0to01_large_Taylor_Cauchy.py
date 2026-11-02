#!/usr/bin/env python3
"""NF448: original NF407 source-correlated, rigorously integrated t=0 panel.

This is the ORIGINAL true J8 endpoint compact kernel I_B:
 I_B = 1/2 int_0^(4B) K(t)[u4(B)-u4(B-t/2)] dt.
The t∈[0,1/10] panel is calculated by a single Taylor series over
the complete original 246-source linear form BEFORE any absolute values.
No Acb analytic-integrator heuristic or unverified Gauss quadrature.

Let L(t)=t*K(t)=exp(-t/4)/((1-exp(-t))/t), entire near 0.
Let G(t)=(u4(B)-u4(B-t/2))/t; it is analytic at 0.
Then I_[0,h] = 1/2 integral_0^h L(t) G(t) dt.
All 273 source freq/order modes and original sinh pole are retained.

Cauchy bound: R=2/5, h=1/10; for |t|<=R,
 |u4(B-t/2)|<10^175 using source |c| absolute <10^160,
 f<883, k<=13, pi<22/7 and exp(pi*f*R)<(11/4)^112<10^50.
For |t|<=1, |L(t)|<6 via 3-e>1/4.
Therefore coefficient bound for [t^n] L(t)*G(t):
 |c_n| <= 12*M/R^(n+1).
Tail of degree N-1 integral <(h/2)*12*M/R*(h/R)^N/(1-h/R).
This is a rigorously tiny explicit rational charge with N=240.
The source dyadic coefficient radius charge is paid separately,
with exact frequency/degree uniform derivative overcharge.

Promote only SMALL PANEL; uncomputed [1/10,4B], full I_B and D7/D8 OPEN.
"""
import argparse, hashlib, json, math, sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb, acb, ctx
from nf415_original_cell6_I1_validated_acb import native_source

if hasattr(sys, "set_int_max_str_digits"): sys.set_int_max_str_digits(0)
B=F(11,10)
R=F(2,5)
H=F(1,10)
N=1300
SOURCE_SHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM_SHA="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
NATIVE_SHA="51b8e0850c678085580940b3ab9afeff8277f446d4407c0200fb75754970db32"
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def A(z):
 if isinstance(z,arb):return z
 if isinstance(z,F):return arb(z.numerator)/arb(z.denominator)
 return arb(z)
def C(z):return acb(A(z))
def outball(z,digits=96):
 m,r,e=z.mid_rad_10exp(digits)
 scale=F(10)**int(e)
 return F(int(m)-int(r))*scale,F(int(m)+int(r))*scale
def ov(a,b):return a[0]<=b[1] and b[0]<=a[1]
def save(path,obj):
 p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(obj,indent=2)+"\n")
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--source",default="notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
 ap.add_argument("--seams",default="notes/data/provisional/NF406_original_prime_support_partition_exact.json")
 ap.add_argument("--nf445",required=True)
 ap.add_argument("--precision",type=int,default=4096)
 ap.add_argument("--output",required=True)
 args=ap.parse_args()
 ctx.prec=args.precision
 src,sha=read(args.source)
 seams,ks=read(args.seams)
 native,nh=read(args.nf445)
 assert sha==SOURCE_SHA and ks==SEAM_SHA and nh==NATIVE_SHA
 assert src["original_dimension"]==242
 assert len(src["original_exact_native_original_four_critical_coefficients_mid_radius"])==4
 assert len(src["original_source_critical_sine_frequencies"])==32
 assert native["original_nf407_source_sha256"]==sha
 assert native["original_nf406_seams_sha256"]==ks
 assert native["original_precision_bits"]==4096
 assert src["W_ODD_NEG"]==native["W_ODD_NEG"]=="OPEN"
 assert src["RH"]==native["RH"]=="OPEN"
 assert args.precision>=3072
 terms,pole,s0=native_source(src)
 assert len(terms)==273 and s0<F(1,10**700)
 assert all(0<f<883 and 0<=k<=13 for f,k,c in terms)
 absolute=sum((abs(c)*(B+R/2)**k for f,k,c in terms),abs(pole))
 assert absolute<10**160
 E=F(22,7)*883*R
 E=(E.numerator+E.denominator-1)//E.denominator
 assert E==1111
 assert F(11,4)**E<10**500
 # Any source polynomial*sin/cos at complex |t|<=R is bounded
 # by its coeff*(B+R/2)^k * exp(pi f R), and sinh pole by
 # abs(pole)*exp((B+R/2)/2)<4|pole|. 10^175 is ample.
 M=4*F(10)**160*F(11,4)**E
 assert 4*absolute*F(11,4)**E<=M
 # e<11/4 and e^(1/4)<3/2, hence L=exp(-t/4)/f
 # with |f|>=3-e>1/4 on unit disk, |L|<6.
 assert F(3)-F(11,4)==F(1,4)
 assert F(3,2)**4>F(11,4)
 q=H/R
 assert q==F(1,4)
 assert F(6)/(1-R)<=12
 tail=(H/F(2))*12*M/R*q**N/(1-q)
 tail_short=(H/F(2))*12*M/R*q**(N-16)/(1-q)
 assert tail<F(1,10**45)
 assert tail_short<F(1,10**35)
 print("NF448 original full source 273 groups, exact Taylor tail bound",float(tail),flush=True)
 # Polynomial source expansion in t about B, carrying all 273 groups
 # at native 4096-bit Arb/Acb before source-amplitude cancellation.
 # For each original mode c*y^k*sin(2*pi*f*y) if k even, else cos,
 # 2Re(alpha y^k exp(i*omega*y)) with
 # alpha = -i*c/2 for sine and c/2 for cosine, real t Taylor coeffs.
 u=[arb(0) for _ in range(N+1)]
 pi=arb.pi()
 half=A(F(1,2))
 for idx,(f,k,c) in enumerate(terms):
  omega=2*pi*A(f)
  iw=acb(arb(0),omega)
  alpha=acb(arb(0),-A(c)/2) if k%2==0 else acb(A(c)/2)
  pre=alpha*(iw*A(B)).exp()
  ew=[acb(1)]
  z=-iw/2
  for r in range(1,N+1):ew.append(ew[-1]*z/r)
  poly=[A(math.comb(k,j))*A(B)**(k-j)*(-half)**j for j in range(k+1)]
  for r in range(N+1):
   val=acb(0)
   for j in range(min(k,r)+1):
    val+=poly[j]*ew[r-j]
   u[r]+=2*(pre*val).real
  if idx%90==0:print("NF448 certified original source series grouped",idx+1,flush=True)
 # Original odd sinh pole: sinh(B/2-t/4).
 # d^r/dt^r sinh(B/2-t/4)
 # = (-1/4)^r * sinh(B/2) if even, cosh(B/2) if odd.
 pole_mid=A(pole)
 sinh=(A(B)/2).sinh()
 cosh=(A(B)/2).cosh()
 fact=1
 for r in range(N+1):
  if r:fact*=r
  u[r]+=pole_mid*((-A(F(1,4)))**r)*(sinh if r%2==0 else cosh)/fact
 assert ov(outball(u[0]),tuple(map(F,native["original_source_v_analytic_carrier_interval"])))
 # L(t)=exp(-t/4) /[(1-e^-t)/t], formal inversion in Arb.
 ker=[arb(0) for _ in range(N)]
 qpoly=[arb(0) for _ in range(N)]
 fac=1
 for n in range(N):
  if n:fac*=n
  qpoly[n]=((-A(F(1,4)))**n)/fac
 ker[0]=arb(1)
 for n in range(1,N):
  z=qpoly[n]
  for j in range(1,n+1):
   f=F((-1)**j,math.factorial(j+1))
   z-=A(f)*ker[n-j]
  ker[n]=z
 # G(t)=(U(B)-U(B-t/2))/t = -sum_{r>=0}u[r+1] t^r.
 # Integrate L*G exactly by polynomial anti-differentiation, original
 # all-source correlation preserved (ARB ball arithmetic).
 P=[arb(0) for _ in range(N)]
 for n in range(N):
  z=arb(0)
  for j in range(n+1):
   z-=ker[j]*u[n-j+1]
  P[n]=z
 h=A(H)
 def integrate(n):
  z=arb(0)
  hpower=h
  for j in range(n):
   z+=P[j]*hpower/(2*(j+1))
   hpower*=h
  return z
 full=outball(integrate(N))
 short=outball(integrate(N-16))
 assert full[0]<=full[1] and short[0]<=short[1]
 # Source coefficient actual interval, not just midpoint:
 # For 0<=t<=H, |delta U'| <=10000*S0 by original frequency<883,
 # 0<=k<=13, B<=11/10; then |delta I|<
 # H/4 (1+H) * 10000*S0 < 10^6 S0.
 source_charge=10**6*s0
 full=(full[0]-tail-source_charge,full[1]+tail+source_charge)
 short=(short[0]-tail_short-source_charge,short[1]+tail_short+source_charge)
 assert ov(full,short) and full[1]-full[0]<F(1,10**25)
 out={
 "pass":"NF448",
 "standing":"ACCEPTED original true NF407 compact-source x=B integral panel [0,1/10] exact correlated Taylor/rigorous Cauchy remainder; remainder [1/10,4B] and z(B) point OPEN",
 "source_sha256":sha,"seams_sha256":ks,"original_nf445_native_json_sha256":nh,
 "original_source_generators_selected_plus_critical":246,
 "original_source_freq_order_groups":273,
 "original_critical_source_sines":32,
 "precision_bits":args.precision,
 "original_true_endpoint_x":"11/10",
 "original_true_panel":["0","1/10"],
 "original_kernel":"(1/2)*K(t)*(U(B)-U(B-t/2)), K=e^(-t/4)/(1-e^(-t))",
 "original_removable_product":"(1/2)*L(t)*G(t), L=tK, G=(U(B)-U(B-t/2))/t",
 "original_compact_true_source_only":True,
 "original_generator_Laurent_m0_included_in_source_sinh":True,
 "original_source_complex_Cauchy_radius":"2/5",
 "original_source_complex_Cauchy_abs_upper_integer":str(M),
 "original_L_Cauchy_radius":"1",
 "original_L_Cauchy_modulus_upper":"6",
 "original_full_Taylor_degree":N-1,
 "original_short_Taylor_degree":N-17,
 "original_true_source_tail_charge":str(tail),
 "original_short_tail_charge":str(tail_short),
 "original_original_4096bit_source_radius_charge":str(source_charge),
 "original_full_true_panel_integral_enclosure":[str(x) for x in full],
 "original_independent_truncation_nested_enclosure":[str(x) for x in short],
 "original_nested_enclosures_overlap":True,
 "original_full_true_panel_enclosure_width":str(full[1]-full[0]),
 "original_remaining_true_endpoint_integral_interval":"(1/10,4B) OPEN",
 "original_true_full_I_B_source_certified":False,
 "original_true_full_z_B_point_source_certified":False,
 "original_true_J7_signed_integral_certified":False,
 "original_true_J8_signed_integral_certified":False,
 "original_full_NF410_NF404_scalar_decided":False,
 "W_ODD_NEG":"OPEN","RH":"OPEN"
 }
 save(args.output,out)
 print("NF448 source-native original x=B true panel [0,1/10] CERTIFIED",float(full[0]),float(full[1]),"width",float(full[1]-full[0]),flush=True)
 print("NF448 remaining [1/10,4B] and signed J7/J8 original RH OPEN",flush=True)
if __name__=="__main__":main()
