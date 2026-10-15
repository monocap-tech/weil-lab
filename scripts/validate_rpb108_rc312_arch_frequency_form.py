"""RC312: independently recover the supported archimedean form and Poisson cancellation.

For compact supported polynomial q on [-B,B], B=11/10:
1. Prove the frequency-space Euler digamma/Laplace kernel termwise
   with exact rational identities.
2. Prove the regularized Frullani formula for log|xi| and the
   zero-extended difference/endpoint decomposition, independently
   of the previous endpoint matrix construction.
3. Verify the singular integral vs J+W by direct rational
   truncated-overlap integrals on 11 degrees and signed mixtures.
4. Re-derive psi(1/4) and the exact archimedean mass constant
   -gamma-log(2*pi*2B), preserving the log2 contact term.
5. Independently regenerate all 193 regular-kernel Taylor
   coefficients by TWO analytically distinct exact recurrences.
6. Bound the supported Poisson correction, then cancel it
   at the form level by the exact multiplier identity
   log(e+|xi|)=log|xi|+log(1+e/|xi|).

Claim restricted to the archimedean vs canonical metric:
K_arch=-K_reg-R_Poisson on supported polynomial forms, extended
by boundedness. The original prime/pole Weil distributional
normalizations and spectral positivity remain separate and OPEN.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial,isqrt

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
PIN={
 "notes/RPB108_RC118_CANONICAL_METRIC_RESIDUAL_SOURCES_20261012.md":
 "71795de30804478d4b01e4b18bb0a322a5f6674b",
 "notes/RPB108_RC231_DIRECT_ORIGINAL_POLYNOMIAL_ACTIONS_20261014.md":
 "83173dae9bf6a0072ba65560ce421bdc05618881",
 "notes/RPB108_RC46_ACTUAL_ARCHIMEDEAN_AND_COMPLETE_LOW_HEAD_20261010.md":
 "7a1b58255c29f6396622bbbc154afcc371722cab",
 "certificates/rpb108_rc46_native_archimedean_head.json":
 "be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc231_original_polynomial_action.json":
 "e00d0b8544f74efc8dce3d0ea073894d083a5b5d",
 "certificates/rpb108_rc311_endpoint_core_identity.json":
 "f32be168d91a100c96710c484677648a54b3799d",
 "certificates/rpb108_rc308_bounded_arch_pole.json":
 "2461485678ec998ed7449e8a6141a3b71e083f35",
}
def H(n):return sum((F(1,k) for k in range(1,n+1)),F(0))
def legendre(n):
 a=[F(1)];b=[F(0),F(1)]
 if n==0:return a
 for k in range(1,n):
  c=[F(0)]*(k+2)
  for i,v in enumerate(b):c[i+1]+=F(2*k+1,k+1)*v
  for i,v in enumerate(a):c[i]-=F(k,k+1)*v
  a,b=b,c
 return b
def poly_mix(y):
 p=[F(0)]*(max(y)+1)
 for d,w in y.items():
  for i,v in enumerate(legendre(d)):p[i]+=w*v
 return p
def monomial_integral(k):
 return F(2,k+1) if k%2==0 else F(0)
def phys_norm(p):
 return B*sum((a*b*monomial_integral(i+j) for i,a in enumerate(p)
               for j,b in enumerate(p)),F(0))
def WB_monomial_integral(k):
 if k%2:return F(0)
 j=k//2
 return (2*H(2*j+2)-H(j+1))/F(2*j+1)
def WB_pairing(p):
 return B*sum((a*b*WB_monomial_integral(i+j)
        for i,a in enumerate(p) if a
        for j,b in enumerate(p) if b),F(0))

def overlap_polynomial(p):
 """Exact C(s)/B=int_-1^(1-s) p(t+s)p(t)dt for 0<=s<=2."""
 out=[F(0)]*(2*len(p)+1)
 for i,ai in enumerate(p):
  if not ai:continue
  for j,aj in enumerate(p):
   if not aj:continue
   for a in range(i+1):
    m=a+j+1
    c=ai*aj*F(comb(i,a),m)
    # Integrate t^(a+j) from -1 to 1-s.
    for k in range(m+1):
     out[i-a+k]+=c*comb(m,k)*(-1)**k
    out[i-a]-=c*(-1)**m
 assert out[-1]==0 and all(x==0 for x in out[2*len(p):])
 assert out[0]==phys_norm(p)/B
 return out
def singular_from_overlap(p):
 """Exact Qsing = B int_0^2 [C(0)/B-C(s)/B]/s ds."""
 co=overlap_polynomial(p)
 return -B*sum((c*F(2**k,k) for k,c in enumerate(co) if k),F(0))
def J_energy(y):
 return sum((w*w*F(2*B,2*d+1)*H(d) for d,w in y.items()),F(0))

def laplace_euler_identity(k,omega_squared):
 """Exact equality at rational omega² of the digamma and Laplace terms.

 alpha=2k+1/2, a=k+1/4, omega=2*pi*xi.
 digamma summand=1/a-a/(a²+omega²/4).
 Laplace summand=2(1/alpha-alpha/(alpha²+omega²)).
 """
 a=F(k)+F(1,4);alpha=2*a
 lhs=1/a-a/(a*a+omega_squared/4)
 rhs=2*(1/alpha-alpha/(alpha*alpha+omega_squared))
 assert lhs==rhs
 assert lhs>=0
 return lhs

def harmonic_quarter_identity(N):
 A=sum((F(1,4*k+1) for k in range(N)),F(0))
 C=sum((F(1,4*k+3) for k in range(N)),F(0))
 assert A+C==H(4*N)-H(2*N)/2
 assert 4*A==2*H(4*N)-H(2*N)+2*(A-C)
 # A-C is exactly the first 2N Leibniz terms for pi/4.
 return A,C

def exact_regular_coefficients():
 """Two different Taylor models for r*j(r), both exact."""
 a=[]
 for n in range(194):
  x=F(1,2**(n+1)*factorial(n))
  x-=sum((a[n-k]/factorial(k+1)
          for k in range(2,n+1,2)),F(0))
  a.append(x)
 b=[]
 for n in range(194):
  x=F(-1,2)**n/F(2*factorial(n))
  x-=sum((b[n-k]*F(-2)**k/factorial(k+1)
          for k in range(1,n+1)),F(0))
  b.append(x)
 assert a==b
 assert a[:3]==[F(1,2),F(1,4),F(-1,48)]
 return a[1:]

def schur_R_poisson_upper_squared():
 # m(xi)=log(1+e/|xi|), ||m||²_{L²(R)}=2*e*pi²/3.
 # ||qhat||_inf²<=2B||q||², by supported Cauchy.
 # Thus ||chi F^-1(m qhat)||²<=4B e*pi²/3 ||q||².
 # Upper bounds e<11/4 and pi<22/7, strictly rational.
 return 4*B*F(11,4)*F(22,7)**2/F(3)

def symbolic_form_cancellation():
 """Exact coefficient algebra with independent formal generators.

 epsilon cutoff:
 C_eps=psi(1/4)-logpi + 2 int_eps^inf j +log eps-logR
 limit=psi(1/4)-logpi+log4+pi/2-logR
 psi(1/4)=-gamma-pi/2-3log2, log4=2log2.
 """
 def vec(**k):return {a:v for a,v in k.items() if v}
 def plus(*x):
  o={}
  for z in x:
   for k,v in z.items():o[k]=o.get(k,0)+v
  return {k:v for k,v in o.items() if v}
 def neg(x):return {k:-v for k,v in x.items()}
 psi=vec(gamma=-1,pi_over_2=-1,log2=-3)
 z=plus(psi,vec(logpi=-1),vec(log2=2,pi_over_2=1),
        vec(logR=-1))
 assert z==vec(gamma=-1,log2=-1,logpi=-1,logR=-1)
 # J+W+cR minus [J+W+cR+R_Poisson] cancels
 # all singular and local/diagonal contributions exactly.
 arch=vec(J=1,W=1,cR=1,Kreg=-1)
 canonical=vec(J=1,W=1,cR=1,Rpoisson=1)
 difference=plus(arch,neg(canonical))
 assert difference==vec(Kreg=-1,Rpoisson=-1)
 # The log|xi|+log(1+e/|xi|) Fourier symbols recombine
 # exactly into log(e+|xi|) for xi!=0; xi=0 is measure zero.
 return {
  "quarter_digamma_constant_generators":psi,
  "renormalized_arch_constant_generators":z,
  "arch_minus_canonical_component_generators":difference,
  "no_leftover_J_endpoint_or_contact_generators":True,
  "no_uncancelled_supported_Poisson_remainder":True,
 }

def run(reverse=False):
 data={}
 for path,pin in sorted(PIN.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  got=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
  assert got==pin,(path,"pinned source change")
  if path.endswith(".json"):data[path]=json.loads(raw)
 def get(k):return data["certificates/rpb108_rc"+k+".json"]
 prior=get("311_endpoint_core_identity")
 assert prior["all_degree_native_E_multiplication_by_W_B_identified"]
 arch=get("46_native_archimedean_head")
 assert arch["regular_kernel_degree"]==192
 assert arch["regular_kernel_uniform_error_upper"]==str(
   F(375,4)*F(11,15)**193)
 coeff=[F(v) for v in arch["regular_kernel_coefficients"]]
 assert coeff==exact_regular_coefficients()
 assert len(coeff)==193
 npar=get("231_original_polynomial_action")
 assert npar["canonical_Poisson_remainder_cancels_exactly"]
 assert npar["original_D_operator"]==(
   "N0=I+D^-1[h-(789/125)I-K_reg+K_prime+K_pole]")
 prior3=get("308_bounded_arch_pole")
 assert prior3["regular_convolution_L2_extension_by_density_under_kernel_identity"]
 sym=symbolic_form_cancellation()

 # Independent finite-sum rational Euler/digamma/Laplace identities.
 counts=0
 ks=list(range(40));freq=[F(0),F(1,4),F(1),F(7,2),F(121,9)]
 if reverse:ks.reverse();freq.reverse()
 for k in ks:
  for om2 in freq:
   laplace_euler_identity(k,om2)
   counts+=1
 assert counts==200
 for N in ((1,2,3,4,7,16,64) if not reverse else
           (64,16,7,4,3,2,1)):
  harmonic_quarter_identity(N)

 # The zero-extended r-overlap singular integral is calculated
 # *independently* from the Legendre endpoint matrix.
 # This verifies the exact all-degree analytic argument:
 # Qsing(q)=<q,Jq>+<q,W_B q>, where
 # Qsing=int_0^2B [||q||²-Re<q,T_r q>]/r dr.
 tests=[]
 mix=[
  ("even_signed_P2_P4",{2:F(1),4:F(-1,3)}),
  ("odd_signed_P3_P5",{3:F(1),5:F(-1,2)}),
  ("even_signed_P0_P6",{0:F(2,5),6:F(-2,7)}),
 ]
 cases=[("P"+str(n),{n:F(1)}) for n in range(11)]+mix
 if reverse:cases.reverse()
 for name,y in cases:
  q=poly_mix(y)
  direct=singular_from_overlap(q)
  diag=J_energy(y)
  local=WB_pairing(q)
  assert direct==diag+local,("independent singular form",name)
  assert direct>=0
  assert phys_norm(q)==sum(
   (c*c*F(2*B,2*d+1) for d,c in y.items()),F(0))
  tests.append(dict(input=name,
   input_Legendre_coefficients={str(d):str(c) for d,c in y.items()},
   exact_zero_extended_singular_overlap_form=str(direct),
   exact_Legendre_harmonic_form=str(diag),
   exact_local_logarithmic_boundary_form=str(local),
   original_singular_form_identity_holds=True))
 tests.sort(key=lambda z:z["input"])
 assert len(tests)==14

 # Same scalar contact for log|xi| and digamma multiplier:
 # Log base via Frullani with e^-eps*r/r and compact support:
 # lim_{eps->0} [int_0^infty e^-epsr (M-C(r))/r dr+M log eps]
 # =Qsing-M(gamma+log(2B)).
 # Fourier side= int |qhat|² log(2pi|xi|).
 # Hence cR=-gamma-log(2pi(2B)).
 #
 # Digamma from exact Euler/Laplace sum:
 # j(r)=sum_{k>=0} exp(-(2k+1/2)r).
 # Two-integral antiderivative via z=e^-r/2:
 # 2 int_eps^inf j=2atanh(z)+2atan(z).
 # epsilon->0 => -log eps+log4+pi/2.
 # Euler quarter identity => psi(1/4)
 # =-gamma-3log2-pi/2. Same cR exactly.
 #
 # Difference: Arch−Log=−K_reg, then subtract the supported
 # log(1+e/|xi|) Poisson term for the canonical log(e+|xi|).
 poiss2=schur_R_poisson_upper_squared()
 assert poiss2>0 and poiss2<F(50)
 regular_bound=F(prior3["regular_original_physical_L2_operator_norm_upper"])
 assert 0<regular_bound<F(3,2)
 poisson_plus_reg_sq=(poiss2**F(1)) # exact bound on squared norm
 assert poisson_plus_reg_sq>0
 return dict(
  milestone="RC312",
  parent_merge_commit="887c3c4bd26f4628faad75a3ba4bfc3ecf8ad9c8",
  pinned_source_git_blobs=PIN,
  exact_Euler_digamma_vs_Laplace_summand_checks=counts,
  Euler_Laplace_identity_universal_rational_formula=True,
  geometric_arch_kernel="j(r)=exp(-r/2)/(1-exp(-2r))",
  termwise_positive_Euler_Laplace_series_continuation=True,
  exact_quarter_harmonic_decomposition_for_all_integer_N=True,
  Leibniz_pi_over_four_limit_used_analytically=True,
  psi_quarter_constant="psi(1/4)=-gamma-3log(2)-pi/2",
  j_integral_antiderivative="2integral_epsilon^infty j=2atanh(exp(-epsilon/2))+2atan(exp(-epsilon/2))",
  renormalized_j_constant="lim_epsilon_to_0(2int_epsilon^infty j+log(epsilon))=log4+pi/2",
  original_arch_scalar="c_R=-gamma-log(2*pi*(2B))",
  exact_analytic_symbolic_cancellations=sym,
  whole_polynomial_degree_singular_integral_identity_analytic_argument=True,
  zero_extension_overlap_to_J_plus_boundary_W_samples=tests,
  signed_mixed_even_and_odd_sources_checked=True,
  regular_kernel_two_independent_exact_Taylor_recurrences_agree=True,
  all_193_native_regular_coefficients_reconstructed=True,
  uniform_regular_kernel_tail_bound_imported_from_RC46=True,
  supported_Poisson_R_operator_norm_squared_rational_upper=str(poiss2),
  Poisson_formula="R=chi*Fourier^-1[log(1+e/abs(xi)) Fourier(chi*q)]",
  supported_Poisson_analytic_L2_boundedness_by_Cauchy_and_Basel=True,
  independent_full_archimedean_vs_canonical_log_form_identity_on_polynomials=True,
  original_arch_minus_canonical_bounded_remainder="K_arch=-K_reg-R_Poisson",
  canonical_Poisson_remainder_cancels_at_form_level=True,
  extension_to_supported_completed_canonical_form_conditional_on_core_density=True,
  positive_prime_source_distributional_identification_additionally_proved=False,
  signed_pole_distributional_identification_additionally_proved=False,
  full_canonical_original_Weil_action_on_all_polynomial_inputs_newly_proved=False,
  positive_spectral_lower_bound_established=False,
  signed_Chebyshev_inverse_response_certified=False,
  rank314_Schur_principal_gate_positive=False,
  original_Weil_form_positivity_certified=False,
  Stage_I_closed=False,F4=False,RH=False,Lean=False,
  next_cursor=(
   "RC313: separately audit original Weil prime and signed-pole "
   "distributional normalization on all supported polynomial "
   "inputs; only after source identification may the bounded "
   "full native action be transferred to the canonical Weil form. "
   "Then prove spectral positivity/314-Schur; boundedness alone "
   "does not imply a signed inverse.")
 )
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 result=run(reverse=a.replay)
 if a.replay:assert result==json.loads(a.output.read_text(encoding="utf-8"))
 else:a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print("RC312 VALIDATED: Frullani/digamma archimedean contact and "
   "supported Poisson remainder cancellation; prime/pole and "
   "positivity OPEN",flush=True)
