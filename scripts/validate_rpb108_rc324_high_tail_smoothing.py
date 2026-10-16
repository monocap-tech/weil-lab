"""RC324 — genuine mode-sensitive original high coercivity interfaces.

This checkpoint is the first rigorous 278-coordinate high-D *diagonal*
profile for the original CC27 signed Weil operator, and a much
stronger COERCIVITY theorem for its far-even tail n>=800.

Key technical improvement: the regular RC46 absolute-distance
convolution has tiny high/high norm, due to two integrations by parts
against the zero-boundary primitive of a high Legendre expansion.
Its derivative kernel consists of -k''(|x-y|) and a diagonal atom
-2*k'(0) delta(x-y). The high primitive norm is <=2B/(2N-1).
Pay the RC46 uniform polynomial remainder separately.

The original even high C_244,244 has a rigorously positive lower
and upper native interval, using the exact diagonal logarithmic
endpoint. A NEW nonzero one-mode high Ritz trial is constructed for
RC323's witness using its signed n=244 coupling, and an improved
original-native upper bound on C_244,244. This gives a true strict
Schur UPPER contraction, not a positive lower Schur bound.

The far tail C_[800,infty) has a certified uniform positive lower
floor much better than the older global even floor for n>=244.
The finite 278-dimensional head still couples to that far tail:
the two floors C>=mu_244 and D_far>=mu_800 CANNOT be combined into
a block-diagonal lower operator without paying their cross action.
Stage I and the full 3x3 Schur positivity remain open.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import validate_rpb108_rc315_low_mode_sign as rc315
import validate_rpb108_rc318_p0_signed_schur as rc318

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
r=F(789,125)
OUT=10**30
GRID=10**42
FIRST=244
TAIL_START=800
PINS={
 "certificates/rpb108_rc46_native_archimedean_head.json":
  "be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":
  "33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc313_prime_pole_distributions.json":
  "954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc314_fredholm_schur.json":
  "6496be8d20176f173c0ff8b6e393b0ccd7c6ff5b",
 "certificates/rpb108_rc322_low_3d_gram.json":
  "ba344b44436c5c2d392a9feb5c6dc0c9892dfe88",
 "certificates/rpb108_rc323_coercivity_nogo.json":
  "51b5f627eaaa3c380b54cc53a886ad5bac9f05ad",
}
def lo(x,g=OUT):return F(x.numerator*g//x.denominator,g)
def hi(x,g=OUT):return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def sqrtlo(x,g=GRID):
 assert x>0
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2
 return F(k,g)
def sqrthi(x,g=GRID):
 assert x>=0
 if not x:return F(0)
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2
 return F(k+1,g)
def gitblob(raw):
 return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def analytic_smoothing(coef,eps,N):
 assert N>=2
 assert len(coef)==193 and coef[0]==F(1,4) and coef[1]==-F(1,48)
 # k(r)=sum_0^192 coef[j] r^j; polynomial valid r in [0,2B].
 # k'(0)=coef[1]. The constant coef[0] vanishes on all
 # zero-mean high functions, but the derivative proof handles
 # it without any special cases.
 derivative2_sup=sum((
   abs(coef[j])*j*(j-1)*R**(j-2)
   for j in range(2,len(coef))),F(0))
 # Let f be any L2-normalized combination of physical
 # Legendre u_n with n>=N. Its primitive vanishes at both
 # endpoints since all n>=1, and its coefficients on
 # adjacent Legendre modes have absolute sum <=2B/(2N-1).
 primitive_operator_up=2*B/F(2*N-1)
 # Two IBPs and distributional mixed derivative:
 # d_x d_y k(|x-y|)=-k''(|x-y|)-2*k'(0)*delta(x-y).
 # Kernel sup bound and the delta term are charged in L2.
 bound=(2*abs(coef[1])+R*derivative2_sup) * primitive_operator_up**2 + R*eps
 assert bound>0
 return dict(derivative2_sup=derivative2_sup,
   primitive_norm_upper=primitive_operator_up,
   high_regular_quadratic_operator_norm_upper=hi(bound,GRID))

def scalar_original(gamma):
 a,b=map(F,gamma)
 assert F(577,1000)<a<=b<F(578,1000)
 pi=rc315.pi_iv()
 log=rc315.log_i(2*pi*R)
 return -b-log.hi,-a-log.lo

def Htable(N):
 h=F(0)
 out={0:h}
 for k in range(1,2*N+1):
  h+=F(1,k)
  if k in (FIRST,TAIL_START) or (FIRST<=k<TAIL_START and k%2==0):
   out[k]=h
 return out

def sinh_up(z,terms=40):
 from math import factorial
 v=sum((z**(2*k+1)/factorial(2*k+1) for k in range(terms)),F(0))
 rem=z**(2*terms+1)/factorial(2*terms+1)/(1-z*z/F((2*terms+2)*(2*terms+3)))
 return hi(v+rem,GRID)

def run(reverse=False):
 data={}
 for p,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/p).read_bytes()
  assert gitblob(raw)==pin,("pinned upstream blob changed",p)
  data[p]=json.loads(raw)
 def src(s):return data["certificates/rpb108_rc"+s+".json"]
 assert src("323_coercivity_nogo")["global_C_floor_only_3D_Loewner_Schur_method_impossible"]
 assert src("314_fredholm_schur")["identity_plus_positive_endpoint_plus_compact_signed_perturbation"]
 assert src("313_prime_pole_distributions")[
   "full_CC27_prime_pole_distributional_source_identity_on_all_polynomials"]
 coef=list(map(F,src("46_native_archimedean_head")["regular_kernel_coefficients"]))
 eps=F(src("46_native_archimedean_head")["regular_kernel_uniform_error_upper"])
 assert eps>0 and eps<F(1,10**22)
 met=src("129_four_vector_joint_moment")
 slo=F(met["actual_D_Gram_entry_lower"][0][0])/R
 shi=F(met["actual_D_Gram_entry_upper"][0][0])/R
 assert F(3)<slo<=shi<F(5)
 gamma=src("322_low_3d_gram")["refined_Euler_Maclaurin_gamma"]
 cLo,cHi=scalar_original(gamma)
 assert F(-4)<cLo<=cHi<F(-3)
 prime=F(src("313_prime_pole_distributions")[
  "original_prime_finite_chain_L2_norm_upper"])
 assert F(4)<prime<F(5)
 globalEven=next(x for x in src("314_fredholm_schur")[
   "inherited_stronger_RC283_all_reference_choices"]
   if x["parity"]=="even" and x["first_discarded_degree"]==FIRST)
 muOld=F(globalEven["high_complement_D_floor_lower"])
 assert muOld>0
 smooth244=analytic_smoothing(coef,eps,FIRST)
 smooth800=analytic_smoothing(coef,eps,TAIL_START)
 norm244=smooth244["high_regular_quadratic_operator_norm_upper"]
 norm800=smooth800["high_regular_quadratic_operator_norm_upper"]
 assert 0<norm800<norm244<F(1,1000)
 # RC314 exact decomposition:
 # N0=I + D^-1/2 h D^-1/2 +
 #    D^-1/2 (P-Kreg+Kpole-r I) D^-1/2,
 # with h>=0 and Kpole>=0 on the even subspace.
 # For ANY even high f supported at n>=800, the native
 # prime form is >=-prime||f||² and regular >=-norm800||f||².
 h=Htable(TAIL_START)
 Dfloor=h[TAIL_START]+slo
 muFar=1-(r+prime+norm800)/Dfloor
 assert muFar>F(1,20) and muFar>9*muOld
 # At a SINGLE even high mode n>=244 we may exploit the
 # *diagonal* Wnn of the original endpoint; this does NOT
 # give the same operator Loewner bound on combinations.
 moments=[]
 minBound=None
 for n in range(FIRST,TAIL_START,2):
  Hn=h[n]
  extra=2*(h[2*n]-Hn)+F(1,2*n+1)
  reg=analytic_smoothing(coef,eps,n)[
    "high_regular_quadratic_operator_norm_upper"]
  low=(Hn+extra+cLo-prime-reg)/(Hn+shi)
  # pole diagonal upper: cosh(Bt/2) orthogonal to Pn's
  # degree < n Taylor polynomial. Uniform tail <=5 Z^n
  # for Z=B/2<1. Therefore
  # Kpole(u_n,u_n)=2 |<u_n,cosh>|² <=100B Z^(2n).
  poleUp=100*B*(B/2)**(2*n)
  upper=(Hn+extra+cHi+prime+reg+poleUp)/(Hn+slo)
  assert 0<low<=upper<2
  if minBound is None or low<minBound:minBound=low
  if n in (244,246,256,400,600,798):
   moments.append(dict(n=n,
     original_CC27_N0_high_diagonal_lower=str(lo(low)),
     original_CC27_N0_high_diagonal_upper=str(hi(upper)),
     regular_high_compression_norm_up=str(reg),
     endpoint_diagonal_exact=str(extra)))
 assert len(moments)==6 and len(range(FIRST,TAIL_START,2))==278
 assert minBound>3*muOld
 mode244=moments[0]
 C244_L=F(mode244["original_CC27_N0_high_diagonal_lower"])
 C244_U=F(mode244["original_CC27_N0_high_diagonal_upper"])
 assert 0<C244_L<C244_U
 # Construct an actual finite-support high Ritz response for
 # RC323's signed low witness, not an "inverse" of C.
 # The native original scaled signed high cross is pinned as
 # a full interval for degree244, independent of this proof.
 s244=next(x for x in src("323_coercivity_nogo")["signed_high_mode_samples"]
    if x["degree"]==FIRST)
 Alo,Ahi=map(F,s244["original_signed_combined_amplitude_interval"])
 assert 0<Alo<=Ahi<F(1,100)
 # True b=<v244,N0 x>=A/sqrt((2n+1)*(Hn+s)),
 # plus the rigorous WHOLE physical source perturbation norm
 # inherited from RC323, which bounds this one coordinate.
 srcError=F(src("323_coercivity_nogo")[
   "complete_original_high_source_error_upper"])
 denMin=sqrtlo((2*FIRST+1)*(h[FIRST]+slo))
 denMax=sqrthi((2*FIRST+1)*(h[FIRST]+shi))
 bLow=Alo/denMax-srcError
 bHigh=Ahi/denMin+srcError
 assert 0<bLow<bHigh
 alpha=bLow/C244_U
 strictReduction=bLow*bLow/C244_U
 assert 0<alpha and 0<strictReduction
 # For Yx=alpha*v244,
 # Bxx -2alpha*b+alpha²*C244 <=Bxx-bLow²/C244_U.
 # This is a Schur UPPER contract, NOT a positive Schur
 # lower witness, since the entire high inverse is still
 # uncomputed.
 Bxx=F(src("323_coercivity_nogo")["original_low_quadratic_B_upper"])
 improvedSchurUpper=Bxx-strictReduction
 assert improvedSchurUpper<Bxx
 return dict(
  milestone="RC324",
  parent_merge="15665091da594ffa73cdfa63f62bcc133939c779",
  input_git_blob_pins=PINS,
  original_CC27_signed_Weil_operator=True,
  regular_kernel_polynomial_degree=192,
  regular_kernel_derivative_at_zero_exact=str(coef[1]),
  regular_kernel_second_derivative_sup_upper=str(
     hi(smooth244["derivative2_sup"],GRID)),
  zero_boundary_primitive_two_ended_IBP_identity_valid=True,
  original_high_regular_operator_norm_bound_244plus=str(norm244),
  original_high_regular_operator_norm_bound_800plus=str(norm800),
  original_prime_physical_L2_operator_norm_upper=str(prime),
  original_even_far_high_cut_degree=TAIL_START,
  original_even_far_high_D_floor_strict_positive=True,
  original_even_far_high_D_floor_lower=str(lo(muFar)),
  inherited_even_244plus_global_floor=str(muOld),
  original_even_far_floor_improvement_factor_lower=str(
     lo(muFar/muOld)),
  original_high_even_diagonal_count_evaluated=278,
  original_high_even_diagonal_min_lower=str(lo(minBound)),
  selected_original_high_even_diagonal_enclosures=moments,
  original_mode244_high_C_diagonal_bounded_positive=True,
  original_mode244_C_lower=str(C244_L),
  original_mode244_C_upper=str(C244_U),
  original_R323_low_witness_rational_coordinates=[
   "3/25","-23/8","1"],
  original_mode244_cross_to_witness_lower=str(lo(bLow)),
  original_mode244_cross_to_witness_upper=str(hi(bHigh)),
  nonzero_one_coordinate_original_high_Ritz_coefficient=str(alpha),
  strict_one_mode_actual_Schur_upper_reduction_lower=str(lo(strictReduction)),
  witness_original_signed_Schur_upper_after_one_high_trial=str(hi(improvedSchurUpper)),
  positive_full_three_mode_original_Schur_proved=False,
  first_278_mode_high_head_to_far_tail_cross_operator_computed=False,
  inverse_weighted_actual_full_high_covariance_computed=False,
  two_complement_floors_NOT_claimed_as_block_diagonal_Loewner_bound=True,
  full_rank317_Schur_positive=False,
  Stage_I_closed=False,F4=False,Lean=False,RH=False,
  next_cursor=(
   "RC325: use the certified C_[800,infty) tail lower bound and "
   "explicit original 278-mode C_head and cross-to-tail action "
   "to build a genuinely mode-sensitive high inverse trial Y "
   "with paid R=T-CY. Merely knowing high mode diagonal "
   "intervals does not give positivity of the finite high block; "
   "two floors cannot be combined without paying coupling."
  )
 )
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 v=run(reverse=a.replay)
 if a.replay:
  assert v==json.loads(a.output.read_text(encoding="utf-8"))
 else:
  a.output.write_text(json.dumps(v,sort_keys=True,indent=2)+"\n",encoding="utf-8")
 print("RC324: first native high-mode diagonal profile, far high coercivity, nonzero Ritz; full 3D Schur Stage I OPEN")
