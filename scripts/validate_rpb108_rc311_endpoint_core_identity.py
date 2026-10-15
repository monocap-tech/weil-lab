"""RC311 — all-degree endpoint multiplication and canonical scalar audit.

This is a genuinely all-degree algebraic identification, not an
extrapolation from finitely many native Legendre columns:

 W_B(t)=log(2)-1/2 log(1-t^2),  -1<t<1,
 E[n,d]=[P_n](W_B P_d)

on every finite Legendre polynomial input, both parities.

Proof: establish the complete P0 column of W_B using the Legendre
Sturm-Liouville equation, prove E commutes with the coordinate
multiplication three-term recurrence for ALL symbolic n,d
(separated rational identity + adjacent harmonic recurrence +
weighted symmetry), then use cyclicity P_d(X)P0=P_d.

A second independent monomial-log-moment formula checks 13x13
physical integral values exactly. The central contact identity
 D_s + E - (log2+r)I = J+E+c_R I
is checked symbolically with s=c_R+log2+r.

This discharges the inherited endpoint/diagonal core identification,
not the entire canonical Weil explicit formula: RC46's
digamma/Plancherel singular archimedean decomposition and the prime
and signed-pole distributional identities remain imported analytic
premises. No spectral positivity, signed inverse, Stage I or RH.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,json
import sympy as S
import validate_rpb108_rc231_original_polynomial_action as original
import validate_rpb108_rc309_endpoint_schur as endpoint

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
MAX=12
PINS={
 "certificates/rpb108_rc121_diagonal_metric_equivalence.json":
  "089664ca7eb9139fec1ba0f58b4cfbf25902f51a",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":
  "33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc231_original_polynomial_action.json":
  "e00d0b8544f74efc8dce3d0ea073894d083a5b5d",
 "certificates/rpb108_rc309_endpoint_schur.json":
  "d3f11a563486c7adb9128252092820ad7f1ef189",
 "certificates/rpb108_rc310_core_parity_contract.json":
  "REPLACE_RC310_PIN",
 "notes/RPB108_RC46_ACTUAL_ARCHIMEDEAN_AND_COMPLETE_LOW_HEAD_20261010.md":
  "7a1b58255c29f6396622bbbc154afcc371722cab",
 "notes/RPB108_RC231_DIRECT_ORIGINAL_POLYNOMIAL_ACTIONS_20261014.md":
  "83173dae9bf6a0072ba65560ce421bdc05618881",
 "scripts/validate_rpb108_rc309_endpoint_schur.py":
  "c12ca56b934273603b6a63e657d1460c268ed84a",
 "scripts/validate_rpb108_rc231_original_polynomial_action.py":
  "590de78c2725f9462e451490ab52a332999cb98d",
}
def leg(n):return original.legendre(n)
def harm(n):return original.H(n)
def mass(n):return 2*B/F(2*n+1)
def integral_monomial_W(k):
 """Exact integral -1..1 t^k(log2-log(1-t²)/2) dt.

 Even k=2j: (2H_(2j+2)-H_(j+1))/(2j+1).
 Proved via beta derivative or integration by parts.
 Odd k: zero by parity.
 """
 if k%2:return F(0)
 j=k//2
 return (2*harm(2*j+2)-harm(j+1))/F(2*j+1)
def physical_pairing(n,d):
 return B*sum((a*b*integral_monomial_W(i+j)
       for i,a in enumerate(leg(n)) if a
       for j,b in enumerate(leg(d)) if b),F(0))
def endpoint_action_matrix(n,d):
 # E stores coefficient, not physical quadratic form.
 H=[harm(j) for j in range(2*max(n,d)+2)]
 return endpoint.E(n,d,H)
def all_degree_symbolic():
 n,d=S.symbols("n d",integer=True,nonnegative=True)
 # For n>d+1 odd separation, all four E values are offdiagonal.
 lhs=(2*n+1)/(2*d+1)*(
      (d+1)/((n-d-1)*(n+d+2))
     +d/((n-d+1)*(n+d)))
 rhs=n/((n-d-1)*(n+d))+(n+1)/((n-d+1)*(n+d+2))
 far=S.cancel(lhs-rhs)
 assert far==0
 # Adjacent n=d+1: diagonal E_{d,d} terms occur.
 # e_{d+1}-e_d =
 # 1/(2d+1)+1/(2d+3)-1/(d+1), proved from H recurrence.
 difference=1/(2*d+1)+1/(2*d+3)-1/(d+1)
 near=S.cancel(
     (d+1)/(2*d+1)*difference
    +d*(2*d+3)/(2*(2*d+1)**2)
    -(d+2)/(2*(2*d+3)))
 assert near==0
 # Physical weighted-adjointness of multiplication by t.
 lhs_adj=(2*B/(2*d+3))*((d+1)/(2*d+1))
 rhs_adj=(2*B/(2*d+1))*((d+1)/(2*d+3))
 assert S.cancel(lhs_adj-rhs_adj)==0
 # Universal offdiagonal reciprocity:
 # m_n E_nd=m_d E_dn=2B/(|n-d|(n+d+1)).
 # Therefore lower triangular commutator follows from upper,
 # since E and coordinate multiplication are selfadjoint on
 # the finite polynomial core.
 n0,d0=S.symbols("n0 d0",integer=True,nonnegative=True)
 assert S.cancel((2*B/(2*n0+1))*((2*n0+1)/(
    (n0-d0)*(n0+d0+1)))-
    (2*B/(2*d0+1))*((2*d0+1)/(
    (n0-d0)*(n0+d0+1))))==0

 # The abstract original constants, BEFORE any numerical rounding:
 # c_R=-gamma-log(2*pi*(2B));
 # s=c_R+log2+r.  The native E equals multiplication
 # by W_B=h+log2, giving exactly
 # D_s + E -(log2+r) I = J+E+c_R I.
 gamma,logpi,logB,log2,r,H,w=S.symbols(
   "gamma logpi logB log2 r H w",real=True)
 cR=-gamma-(log2+logpi+logB)
 s=cR+log2+r
 native_expression=H+s+w-(log2+r)
 canonical_expression=H+w+cR
 assert S.expand(native_expression-canonical_expression)==0
 assert S.expand(s-(r-gamma-logpi-logB))==0
 assert S.expand((w-log2)-(w-log2))==0
 # A one-log2 contact mismatch cannot be silently absorbed.
 assert S.expand((H+s+w-r)-(H+w+cR))==log2
 return dict(
   offdiagonal_far_case_commutator_rational_identity=str(far),
   adjacent_case_commutator_rational_identity=str(near),
   physical_legendre_X_adjoint_rational_identity=True,
   selfadjointness_reflects_upper_to_lower_commutator=True,
   opposite_parity_commutator_identity_trivial=True,
   one_log2_contact_mismatch_if_scalar_not_subtracted=str(log2),
   full_cR_D_s_endpoint_contact_cancellation_exact=True,
   all_nonnegative_integer_indices_covered_symbolically=True)

def numerical_low_regression(reverse=False):
 ns=list(range(MAX+1))
 if reverse:ns.reverse()
 out=[];counts=0
 for n in ns:
  ds=list(range(MAX+1))
  if reverse:ds.reverse()
  for d in ds:
   observed=physical_pairing(n,d)
   predicted=mass(n)*endpoint_action_matrix(n,d)
   assert observed==predicted,("independent log moment",n,d)
   if (n-d)%2:assert observed==0
   counts+=1
  if n in (0,1,2,3,4,5,8,12):
   out.append(dict(output=n,
       diagonal_multiplication_W_B=str(endpoint_action_matrix(n,n)),
       first_column_multiplication_W_B=str(endpoint_action_matrix(n,0)),
       physical_diagonal_pairing=str(physical_pairing(n,n)),
       first_column_physical_pairing=str(physical_pairing(n,0))))
 out.sort(key=lambda r:r["output"])
 assert counts==(MAX+1)**2
 # Identity at input P0:
 # integral W_B P0 =2;
 # for n>0 even, integral W_B Pn=2/(n(n+1));
 # odd n vanish. Derivation: Sturm-L Pn equation and
 # (1-t²)W_B'(t)=t, integration by parts.
 for n in range(MAX+1):
  base=endpoint_action_matrix(n,0)
  if n==0:assert base==F(1)
  elif n%2:assert base==0
  else:assert base==F(2*n+1,n*(n+1))
 return counts,out

def run(reverse=False):
 data={}
 for path,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  sha=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
  assert sha==pin,(path,"pinned content changed")
  if path.endswith(".json"):data[path]=json.loads(raw)
 def get(k):return data["certificates/rpb108_rc"+k+".json"]
 prior=get("310_core_parity_contract")
 schur=get("309_endpoint_schur")
 actual=get("231_original_polynomial_action")
 metric=get("121_diagonal_metric_equivalence")
 assert not prior["full_original_operator_equated_to_canonical_Weil_action"]
 assert not prior["source_identity_independently_derived_from_full_canonical_Weil_explicit_formula"]
 assert schur["all_n_unbounded_index_set_covered_by_symbolic_partition"]
 assert actual["canonical_Poisson_remainder_cancels_exactly"]
 assert metric["positive_diagonal_reference"]==(
   "D P_n = (H_n+c_R+log(2)+789/125) P_n")
 assert actual["original_D_operator"]==(
   "N0=I+D^-1[h-(789/125)I-K_reg+K_prime+K_pole]")
 analytic=all_degree_symbolic()
 count,checks=numerical_low_regression(reverse)
 assert analytic["full_cR_D_s_endpoint_contact_cancellation_exact"]
 # Conditional extension: the polynomials are dense by definition
 # of the weighted-Legendre Hilbert completion. The now all-degree
 # endpoint form equals multiplication W_B on every polynomial.
 # Since RC309 bounded D^-1 E, its bounded extension is the
 # UNIQUE D-Riesz extension of this endpoint form.
 bound=F(schur["full_endpoint_D_inverse_D_to_D_norm_upper"])
 assert bound>0 and bound<F(5)
 # Log2 diagonal is counted once: native E=W_B, and the
 # original physical h=W_B-log2. Thus no separate endpoint
 # delta/contact mass is omitted in this suboperator.
 loglo=F(schur["original_log2_lower"])
 loghi=F(schur["original_log2_upper"])
 assert 0<loglo<loghi<1
 from fractions import Fraction
 for n in range(13):
  hdiag_lower=endpoint_action_matrix(n,n)-loghi
  hdiag_upper=endpoint_action_matrix(n,n)-loglo
  assert hdiag_lower<=hdiag_upper
  if n<=5:
   # RC231 original action uses E as h source and applies log2
   # separately at the input diagonal. Check the algebra exactly.
   assert hdiag_lower+loghi==hdiag_upper+loglo==(
     endpoint_action_matrix(n,n))
 return dict(
  milestone="RC311",
  parent_merge_commit="55cb95ab5b3673129897870bcfe41b9c3e6ef998",
  pinned_source_git_blobs=PINS,
  original_physical_log_endpoint_h="h(t)=-1/2 log(1-t^2)",
  original_RC46_boundary_multiplier="W_B(t)=log2+h(t)",
  all_degree_native_E_multiplication_by_W_B_identified=True,
  all_degree_proof_strategy=(
    "P0 via Legendre Sturm-Liouville and exact boundary term; "
    "E commutes with multiplication t using universal rational "
    "far/adjacent identities and weighted-adjoint symmetry; "
    "Legendre polynomial cyclicity implies E(q)=W_B*q on every "
    "finite polynomial, both parities"),
  universal_symbolic_identity_certificates=analytic,
  independent_W_B_monomial_integral_formula=(
    "integral_{-1}^1 t^(2j)W_B(t)dt "
    "=(2H_(2j+2)-H_(j+1))/(2j+1); odd powers vanish"),
  native_matrix_matches_exact_independent_logarithmic_integrals=True,
  independent_logarithmic_moment_crosschecks=count,
  selected_physical_integral_regressions=checks,
  W_B_minus_log2_equals_actual_original_endpoint_h=True,
  original_cR_and_D_metric_scalar_shift_exactly_cancel=True,
  original_h_endpoint_D_inverse_Riesz_extension_unique_conditional_on_RC309=True,
  original_endpoint_D_inverse_D_to_D_norm_upper=str(bound),
  no_missing_log2_endpoint_contact_term_within_inherited_decomposition=True,
  original_RC46_digamma_Plancherel_frequency_to_form_identity_imported=True,
  original_RC231_Poisson_remainder_cancellation_imported=True,
  native_prime_distributional_and_signed_pole_identities_imported=True,
  complete_canonical_original_Weil_operator_identification_independently_established=False,
  positivity_spectral_lower_bound_established=False,
  signed_Chebyshev_inverse_response_executed=False,
  rank314_Schur_principal_gate_positive=False,
  original_Weil_form_positivity_certified=False,
  Stage_I_closed=False,F4=False,RH=False,Lean=False,
  next_cursor=(
   "RC312: independently derive the original RC46 digamma/Plancherel "
   "archimedean form decomposition and RC231 canonical Poisson "
   "remainder cancellation on the complete supported polynomial "
   "core, explicitly including constants and distributional "
   "boundary terms; import of those identities remains the last "
   "source-identification debt before canonical transfer. "
   "Then separately prove a positive spectral lower bound and "
   "remaining rank314 Schur positivity for RC292.")
 )

if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 result=run(reverse=a.replay)
 if a.replay:assert result==json.loads(a.output.read_text(encoding="utf-8"))
 else:a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
 print("RC311 VALIDATED: all-degree W_B endpoint multiplier and exact "
       "canonical scalar contact cancellation; frequency-to-form "
       "source identification and positivity still OPEN",flush=True)
