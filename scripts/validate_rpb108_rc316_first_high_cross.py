"""RC316: first rigorous NONZERO original signed high-cross entries.

For u_n = sqrt((2n+1)/(2B)) P_n(x/B), B=11/10, n=232 or 244,
and u_0, compute sqrt(2n+1)*Q(u_n,u_0), where Q is the original
CC27 Weil mixed form identified in RC313, NOT the augmented proxy.

The off-diagonal J and scalar contributions vanish; endpoint is
(2n+1)/(n(n+1)), prime is a seven-prime Legendre boundary sum;
RC46 regular polynomial vanishes for n>193 and only its uniform
kernel remainder is paid. The exponentially small even pole is paid
by Taylor orthogonality and an explicit upper bound.

This does NOT compute C^-1T, a signed high response Y, a Gram, or a
positive Schur complement. In particular it does not close Stage I.
"""
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
GRID=10**35
OUTPUT=10**18
PRIMES=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
PINS={
 "certificates/rpb108_rc46_native_archimedean_head.json":
 "be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc313_prime_pole_distributions.json":
 "954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc314_fredholm_schur.json":
 "6496be8d20176f173c0ff8b6e393b0ccd7c6ff5b",
 "certificates/rpb108_rc315_low_mode_sign.json":
 "a8cd974c8218e18943dda0082f48cca36a3350a8",
}

def down(x,g=GRID):return F(x.numerator*g//x.denominator,g)
def up(x,g=GRID):
 return F((x.numerator*g+x.denominator-1)//x.denominator,g)

def logarithm_enclosure(n,K=220):
 # Exact positive atanh sum, monotonically enclosed by its geometric
 # upper tail. Grid-round BEFORE Legendre evaluation so rational
 # denominators grow only as degree*35 digits, not astronomically.
 assert 1<n<=9
 t=F(n-1,n+1)
 lo=sum((2*t**(2*k+1)/F(2*k+1) for k in range(K)),F(0))
 hi=lo+2*t**(2*K+1)/(F(2*K+1)*(1-t*t))
 a,b=down(lo),up(hi)
 assert a<=lo<=hi<=b and b-a<F(1,10**30)
 return a,b

def sqrt_enclosure(n):
 t=isqrt(n*GRID*GRID)
 assert t*t<=n*GRID*GRID<(t+1)*(t+1)
 return F(t,GRID),F(t+1,GRID)

def legendre_edge_pair(n,z):
 # Exact recurrence for P_{n-1}(z) and P_{n+1}(z).
 # No interval dependence blowup; argument uncertainty is paid
 # separately by the analytic Markov/Legendre derivative bound.
 assert n>=2 and -1<z<1
 p,q=F(1),z
 left=right=None
 for j in range(1,n+1):
  v=((2*j+1)*z*q-j*p)/F(j+1)
  p,q=q,v
  if j+1==n-1:left=q
  if j+1==n+1:right=q
 assert left is not None and right is not None
 return left,right

def signed_scaled_cross(n,arch_err,reverse=False):
 assert n in (232,244) and n>193 and n%2==0
 # Physically normalized original-source prime cross:
 # sqrt(2n+1)*Q_prime(u_n,u_0)
 # = -sum_m c_m(P_{n+1}(1-log(m)/B)-P_{n-1}(...)).
 signed_center=F(0);fault=F(0);rows=[]
 for m,p in (reversed(PRIMES) if reverse else PRIMES):
  elo,ehi=logarithm_enclosure(m)
  plo,phi=logarithm_enclosure(p)
  slo,shi=sqrt_enclosure(m)
  cl,ch=plo/shi,phi/slo
  ec=(elo+ehi)/2;cc=(cl+ch)/2
  z=1-ec/B
  left,right=legendre_edge_pair(n,z)
  delta=right-left
  # |P_k|<=1 and sup_|z|<=1 |P'_k(z)| <= k(k+1)/2.
  # Thus the difference's derivative is <=n^2+n+1.
  argument_fault=F(n*n+n+1)*(ehi-elo)/(2*B)
  # coefficient midpoint fault: width/2 * |difference| <= width.
  # Extra product term is kept as a conservative rounding reserve.
  local_fault=cc*argument_fault+(ch-cl)+(ch-cl)*argument_fault/2
  signed_center+=cc*delta
  fault+=local_fault
  rows.append(dict(prime_power=m,base_prime=p,
     signed_prime_center=str(down(-cc*delta,OUTPUT)),
     local_total_abs_fault_upper=str(up(local_fault,OUTPUT))))
 # Regular Taylor r_192(|x-y|) acting on constant u0 is
 # polynomial degree at most 193. Exact Legendre orthogonality
 # makes its nth coefficient zero for n >= 194.
 # Uniform RC46 residual ||K-K_poly||_{2->2} <= 2B*err.
 regular_err=2*B*arch_err
 # Original signed pole: even part 2|cosh(x/2)><cosh(x/2)|.
 # Replace cosh by Taylor polynomial degree n-1. Its nth
 # Legendre coefficient is zero. Bound both moments using
 # Cauchy-Schwarz, e^B<4 and Taylor remainder:
 # |Q_pole(u_n,u0)| <= 4B e^B (B/2)^n/n! <=16B(B/2)^n.
 pole_err=16*B*(B/2)**n
 assert pole_err<F(1,10**50)
 # sqrt(2n+1) <= n+1 is exact for n>=1.
 source_fault=(n+1)*(regular_err+pole_err)
 endpoint=F(2*n+1,n*(n+1))
 center=endpoint-signed_center
 lower=center-fault-source_fault
 upper=center+fault+source_fault
 assert lower<=upper
 if n==232:assert upper<-F(1,10)
 if n==244:assert lower>F(3,100)
 rows.sort(key=lambda x:x["prime_power"])
 return dict(first_omitted_even_degree=n,physical_L2_normalized_cross_scaled_by_sqrt_2n_plus_1=True,
  original_scaled_cross_lower=str(down(lower,OUTPUT)),
  original_scaled_cross_upper=str(up(upper,OUTPUT)),
  scaled_endpoint_exact=str(endpoint),
  prime_center_rational=str(-signed_center),
  prime_enclosure_fault_upper=str(up(fault,OUTPUT)),
  regular_source_physical_L2_fault_upper=str(up(regular_err,OUTPUT)),
  pole_source_physical_L2_fault_upper=str(up(pole_err,OUTPUT)),
  scaled_combined_source_fault_upper=str(up(source_fault,OUTPUT)),
  source_prime_power_components=rows,
  nonzero_cross_sign_certified="negative" if n==232 else "positive",
  actual_signed_Weil_not_augmented_reference=True)

def git_blob(raw):
 return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def run(reverse=False):
 data={}
 for path,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  assert git_blob(raw)==sha,("pinned source changed",path)
  data[path]=json.loads(raw)
 def src(k):return data["certificates/rpb108_rc"+k+".json"]
 assert src("313_prime_pole_distributions")[
   "original_CC27_Weil_polynomial_form_matches_native_model_on_all_degrees"]
 assert src("314_fredholm_schur")["original_nonpositive_Morse_index_upper"]==301
 assert src("315_low_mode_sign")["normalized_low_block_positive_2_by_2"]
 ref=src("314_fredholm_schur")
 assert any(x["first_discarded_degree"]==232 and
  x["reference_rank"]==116 for x in
  ref["inherited_stronger_RC283_all_reference_choices"])
 assert any(x["first_discarded_degree"]==244 and
  x["reference_rank"]==122 for x in
  ref["inherited_stronger_RC283_all_reference_choices"])
 arch=src("46_native_archimedean_head")
 err=F(arch["regular_kernel_uniform_error_upper"])
 assert 0<err<F(1,10**22)
 assert len(arch["regular_kernel_coefficients"])==193
 assert err==F(src("315_low_mode_sign")["tail_uniform"])
 rows=[signed_scaled_cross(n,err,reverse) for n in
       ((244,232) if reverse else (232,244))]
 rows.sort(key=lambda x:x["first_omitted_even_degree"])
 return dict(milestone="RC316",parent_route_head="43e11169dbb14759331e7db0252d7633ba67d030",
  source_blob_pins=PINS,original_CC27_signed_source=True,
  rigorous_high_crosses=rows,
  rank301_high_mode_first_even_cross_nonzero=True,
  rank317_high_mode_first_even_cross_nonzero=True,
  D_Riesz_high_cross_is_nonzero_by_positive_metric_rescaling=True,
  exact_prime_zero_extended_boundary_evaluation_used=True,
  RC46_degree192_regular_part_vanishes_for_high_cross=True,
  signed_even_pole_tail_paid=True,
  total_high_response_Y_computed=False,
  full_rank301_or_317_Schur_principal_positive=False,
  residual_Gram_computed=False,Stage_I_closed=False,F4=False,RH=False,Lean=False,
  next_cursor="RC317: construct and certify actual original high response Y to first low sources; use signed high cross and complete D residual Gram in RC314 minus-sign Schur inequality, without extrapolating from these two entries.")

if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 r=run(reverse=a.replay)
 if a.replay:assert r==json.loads(a.output.read_text(encoding="utf-8"))
 else:a.output.write_text(json.dumps(r,sort_keys=True,indent=2)+"\n",encoding="utf-8")
 print("RC316: two NONZERO original signed low-to-high crosses; Schur and Stage I OPEN",flush=True)
