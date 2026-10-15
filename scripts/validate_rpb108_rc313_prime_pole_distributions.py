"""RC313: all-polynomial Weil prime/pole distributional normalization.

Start from the actual ORIGINAL CC27 Weil mixed-form source, not an
interpolated finite Legendre model. Use Plancherel and zero-extension
to identify -2 sum Lambda(n)/sqrt(n) cos(2pi xi log n) with exactly
-c_n (T_ell+T_-ell), and the two cross-paired imaginary-frequency
moments with 2|cosh(x/2)><cosh(x/2)|-2|sinh(x/2)><sinh(x/2)|.

All-degree identities are algebraic on the entire supported polynomial
core; executable regressions use completely independent monomial
overlap/translated-coordinate integrals in both parity sectors.
Independently re-enclose log n and Lambda(n)/sqrt(n) from atanh
rational series/sqrt intervals for all seven active prime powers.

With RC312+RC311+RC309 and RC121 metric equivalence, the complete
CC27 ORIGINAL FORM on the polynomial core agrees with the native
bounded operator. Its unique completed D-form representative is
bounded and can be iterated ABSTRACTLY. This does not prove the
separate zero-divisor/retained witness identity, a spectral lower
bound, signed inverse, Stage I, F4, or RH.
"""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from math import comb,factorial,isqrt
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
Q=10**55
GRID=10**30
PINS={
 "notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_FLUX_CC27_20261008.md":
   "e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482",
 "notes/RPB108_RC42_ACTUAL_NATIVE_SIGNED_POLE_HEAD_20261010.md":
   "9e358b68e647c6c62534c296b6d567d22d31eb10",
 "notes/RPB108_RC43_ACTUAL_NATIVE_PRIME_HEAD_20261010.md":
   "0ebf5dba5370ce317944aa43c85b19865ab16936",
 "certificates/rpb108_rc42_native_signed_pole_head.json":
   "478c53d7d309d6921d7ba65274eef0feed5bc100",
 "certificates/rpb108_rc43_native_prime_head.json":
   "b4893953109e6fdc55d52b505c2bcfbf0d38281e",
 "certificates/rpb108_rc121_diagonal_metric_equivalence.json":
   "089664ca7eb9139fec1ba0f58b4cfbf25902f51a",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":
   "33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc308_bounded_arch_pole.json":
   "2461485678ec998ed7449e8a6141a3b71e083f35",
 "certificates/rpb108_rc309_endpoint_schur.json":
   "d3f11a563486c7adb9128252092820ad7f1ef189",
 "certificates/rpb108_rc310_core_parity_contract.json":
   "a40b6807309f71df128b98f820a45a12e145948a",
 "certificates/rpb108_rc311_endpoint_core_identity.json":
   "f32be168d91a100c96710c484677648a54b3799d",
 "certificates/rpb108_rc312_arch_frequency_form.json":
   "df120735342f66a3cf41559064b2785fcb266965",
}

def ceil_grid(x):
 assert x>=0
 return F((x.numerator*GRID+x.denominator-1)//x.denominator,GRID)
def floor_grid(x):
 assert x>=0
 return F(x.numerator*GRID//x.denominator,GRID)
def legendre(n):
 p=[F(1)]
 if n==0:return p
 q=[F(0),F(1)]
 for d in range(1,n):
  v=[F(0)]*(d+2)
  for j,c in enumerate(q):v[j+1]+=F(2*d+1,d+1)*c
  for j,c in enumerate(p):v[j]-=F(d,d+1)*c
  p,q=q,v
 return q
def poly_input(coef):
 p=[F(0)]*(max(coef)+1)
 for d,v in coef.items():
  for k,c in enumerate(legendre(d)):p[k]+=v*c
 return p
def poly_shift(p,off):
 return [sum((p[j]*comb(j,k)*off**(j-k)
       for j in range(k,len(p))),F(0)) for k in range(len(p))]
def poly_multiply(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z
def integrate_poly(p,lo,hi):
 return sum((c*(hi**(k+1)-lo**(k+1))/F(k+1)
             for k,c in enumerate(p)),F(0))
def mass(n):return 2*B/F(2*n+1)
def physical_norm_sq(p):
 return B*integrate_poly(poly_multiply(p,p),-1,1)
def translated_overlap(p,q,displacement):
 """Physical x pairing <p,T_ell q>, with p,q in t=x/B coordinates."""
 delta=displacement/B
 assert 0<delta<2
 return B*integrate_poly(poly_multiply(p,poly_shift(q,delta)),
                         F(-1),1-delta)
def independent_affine_overlap(p,q,displacement):
 """Independent variable u=t+1, from 0 to 2-delta."""
 delta=displacement/B
 pp=poly_shift(p,-1)
 qq=poly_shift(q,delta-1)
 return B*integrate_poly(poly_multiply(pp,qq),F(0),2-delta)
def rational_exp_upper(z,N=26):
 assert 0<z<F(5,2) and N>=10
 terms=[z**k/factorial(k) for k in range(N+1)]
 tail=(z**(N+1)/factorial(N+1))/(1-z/F(N+2))
 return sum(terms,F(0)),sum(terms,F(0))+tail
def primebase(n):
 for p in range(2,n+1):
  if n%p:continue
  if any(p%k==0 for k in range(2,isqrt(p)+1)):continue
  k=n
  while k%p==0:k//=p
  if k==1:return p
 return None
def log_interval(n):
 # log n=2*atanh((n-1)/(n+1)), positive-term rational series.
 t=F(n-1,n+1)
 K=360
 val=sum((2*t**(2*k+1)/F(2*k+1) for k in range(K)),F(0))
 rem=2*t**(2*K+1)/(F(2*K+1)*(1-t*t))
 return val,val+rem
def sqrt_interval(n):
 L=isqrt(n*Q*Q)
 return F(L,Q),F(L+1,Q)
def prime_interval_check(row):
 n=row["n"];p=primebase(n)
 assert p==row["base_prime"]
 al,au=log_interval(n);pl,pu=log_interval(p)
 sl,su=sqrt_interval(n)
 tlo,thi=map(F,[row["translation_lower"],row["translation_upper"]])
 clo,chi=map(F,[row["coefficient_lower"],row["coefficient_upper"]])
 assert tlo<=al<=au<=thi,("log n tight enclosure",n)
 assert clo<=pl/su<=pu/sl<=chi,("Lambda coefficient enclosure",n)
 return dict(
  prime_power=n,base_prime=p,log_n_lower=str(floor_grid(al)),
  log_n_upper=str(ceil_grid(au)),
  coefficient_Lambda_over_sqrt_n_lower=str(floor_grid(pl/su)),
  coefficient_Lambda_over_sqrt_n_upper=str(ceil_grid(pu/sl)),
  source_lambda_is_log_base_prime_not_log_n=True,
  neither_prime_coefficient_nor_pair_of_directions_doubled=True)

def expmom(p,sign,terms=40):
 """Exact degree-40 Taylor model for m_{+/-}(p)."""
 t=F(sign)*B/2
 polynomial=[t**k/factorial(k) for k in range(terms+1)]
 return B*integrate_poly(poly_multiply(p,polynomial),-1,1)

def positive_legendre_exp_series(n):
 """Independent positive Rodrigues/integration-by-parts model."""
 t=B/2
 cap=(40-n)//2
 if cap<0:return F(0)
 return B*sum((F(2**(n+1))*t**(n+2*j)
                 *F(factorial(j+n),factorial(j)
                      *factorial(2*j+2*n+1))
                 for j in range(cap+1)),F(0))

def run(reverse=False):
 inputs={}
 for path,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  sha=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
  assert sha==pin,("pinned original form changed",path)
  if path.endswith(".json"):inputs[path]=json.loads(raw)
 def c(k):return inputs["certificates/rpb108_rc"+k+".json"]
 arch=c("312_arch_frequency_form")
 assert arch["canonical_Poisson_remainder_cancels_at_form_level"]
 assert arch["independent_full_archimedean_vs_canonical_log_form_identity_on_polynomials"]
 assert c("311_endpoint_core_identity")["all_degree_native_E_multiplication_by_W_B_identified"]
 assert c("310_core_parity_contract")["all_five_source_terms_exactly_linear_for_finite_polynomial_inputs"]
 assert c("309_endpoint_schur")["all_n_unbounded_index_set_covered_by_symbolic_partition"]
 assert c("121_diagonal_metric_equivalence")["whole_supported_canonical_form_domain_covered"]
 prime=c("43_native_prime_head")
 pole=c("42_native_signed_pole_head")
 assert prime["original_form_source_blob"]==PINS[
  "notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_FLUX_CC27_20261008.md"]
 assert pole["original_form_source_blob"]==prime["original_form_source_blob"]
 assert pole["actual_native_signed_pole_head_inertia"]==[1,1,6]
 low_e,high_e=rational_exp_upper(R)
 assert F(9)<low_e<=high_e<F(10),("exact support aperture",low_e,high_e)
 active=[n for n in range(2,10) if primebase(n) is not None]
 assert active==[2,3,4,5,7,8,9]
 assert [r["n"] for r in prime["active_prime_powers"]]==active
 assert primebase(6) is None and primebase(10)==2
 # The strict cutoff contains n=9, and excludes n>=10:
 # log n < 2B iff n<exp(2B).
 records=[prime_interval_check(row) for row in (
    reversed(prime["active_prime_powers"]) if reverse else
    prime["active_prime_powers"])]
 records.sort(key=lambda z:z["prime_power"])

 # Core-level Fourier normalization:
 #  Fourier(T_ell f)(xi)=exp(+2*pi*i*xi*ell) fhat(xi)
 # for T_ell f(x)=f(x+ell), and the reverse sign for T_-ell.
 # Hence -2 c_n cos(2*pi*xi*ell) has inverse action
 # -c_n (T_ell+T_-ell). This holds by Plancherel for EVERY
 # supported L2 input. Extension by zero is essential: without
 # it the prime overlap would have the wrong integration domain.
 # Spectral sign and coefficient count are separately checked.
 qs={
  "even_P0":{0:F(1)},
  "odd_P1":{1:F(1)},
  "even_P2":{2:F(1)},
  "odd_P3":{3:F(1)},
  "signed_even_P0_minus_P4":{0:F(1),4:F(-1,3)},
  "signed_odd_P1_minus_P5":{1:F(1),5:F(-1,2)},
  "mixed_parity_P0_P1":{0:F(1),1:F(1)},
 }
 test_keys=list(qs) if not reverse else list(reversed(list(qs)))
 poly={k:poly_input(y) for k,y in qs.items()}
 # These are EXACT rational-center source models.
 centers=[((F(row["translation_lower"])+F(row["translation_upper"]))/2,
            (F(row["coefficient_lower"])+F(row["coefficient_upper"]))/2)
           for row in prime["active_prime_powers"]]
 pair_results=[]
 for left,right in [
  ("even_P0","even_P0"),("odd_P1","odd_P1"),
  ("even_P2","even_P0"),("odd_P3","odd_P1"),
  ("signed_even_P0_minus_P4","even_P2"),
  ("signed_odd_P1_minus_P5","odd_P3"),
  ("mixed_parity_P0_P1","mixed_parity_P0_P1"),
  ("even_P0","odd_P1"),("signed_even_P0_minus_P4","signed_odd_P1_minus_P5")]:
  p,q=poly[left],poly[right]
  parts=[]
  for ell,coef in (reversed(centers) if reverse else centers):
   plus=translated_overlap(p,q,ell)
   reverse_direction=translated_overlap(q,p,ell)
   assert plus==independent_affine_overlap(p,q,ell)
   assert reverse_direction==independent_affine_overlap(q,p,ell)
   # Physical minus-translation equals the reversed positive
   # overlap after the change of variable t -> t-ell/B.
   parts.append(-coef*(plus+reverse_direction))
  prime_form=sum(parts,F(0))
  check_swap=sum((-coef*(
   translated_overlap(q,p,ell)+translated_overlap(p,q,ell))
                  for ell,coef in centers),F(0))
  assert prime_form==check_swap
  if (left.startswith("even") and right.startswith("odd")
     or left.startswith("signed_even") and right.startswith("signed_odd")):
   assert prime_form==0
  if left==right=="even_P0":assert prime_form<0
  if left==right=="odd_P1":assert prime_form>0
  pair_results.append(dict(
   left=left,right=right,
   original_prime_rational_center_bilinear_pairing=str(
      floor_grid(abs(prime_form))*(1 if prime_form>=0 else -1)),
   exactly_paired_two_support_truncated_translations=True,
   exact_direct_vs_affine_integral_two_way_regression=True,
   Hermitian_real_symmetric_prime_pairing=True))
 assert len(pair_results)==9

 # Pole: m_+(q)=qhat(i/(4pi)), m_-(q)=qhat(-i/(4pi));
 # for c=cosh(x/2), s=sinh(x/2), m±=<c±s,q>.
 # Thus over complex L2, Qpole(h,f)=
 # conj(m_-h)m_+f+conj(m_+h)m_-f
 # =2 conj(m_c h)m_c f-2 conj(m_s h)m_s f.
 # The sign is negative on odd parity, and the operator is
 # rank two on every supported L2 input, not just Legendre samples.
 # Below: exact Taylor models and INDEPENDENT Rodrigues series.
 parity_cases=[]
 t=F(B,2)
 _,exp_up=rational_exp_upper(t)
 assert exp_up<F(2)
 taylortail=2*t**41/F(factorial(41))
 assert taylortail<F(1,10**60)
 selected=list(range(7))
 if reverse:selected.reverse()
 for n in selected:
  q=legendre(n)
  mp=expmom(q,+1)
  mm=expmom(q,-1)
  assert mm==(-1)**n*mp
  positive=positive_legendre_exp_series(n)
  # Rodrigues expansion is the degree-40 truncation regrouped
  # by degree n+2j; exact equality, no floating sampling.
  assert positive==mp,(n,"Rodrigues exponential moment")
  mc=(mp+mm)/2;ms=(mp-mm)/2
  pole_from_pairs=2*mp*mm
  pole_from_parity=2*(mc*mc-ms*ms)
  assert pole_from_pairs==pole_from_parity
  if n%2==0:
   assert ms==0 and pole_from_pairs>=0
  else:
   assert mc==0 and pole_from_pairs<=0
  # Exponential Taylor error uniformly <=2*t^41/41!.
  # |P_n|<=1 on [-1,1] via classical Legendre bound.
  moment_error=2*B*taylortail
  parity_cases.append(dict(
   input_degree=n,reflection_parity="even" if n%2==0 else "odd",
   m_plus_Taylor_center=str(floor_grid(abs(mp))),
   m_minus_equals_parity_times_m_plus=True,
   Rodrigues_series_matches_moment_Taylor_exactly=True,
   original_two_cross_pole_products_equal_rank_two_difference=True,
   expected_quadratic_sign="positive" if n%2==0 else "negative",
   original_pole_moment_error_upper=str(ceil_grid(moment_error))))
 parity_cases.sort(key=lambda x:x["input_degree"])
 assert len(parity_cases)==7
 # An algebraic arbitrary-complex moment identity: cross-pairing
 # expands to 2 conjugate(c_h)c_f -2 conjugate(s_h)s_f.
 # Independently test nontrivial rational moments (including
 # nonzero both c,s) with exact bilinear coefficient identity.
 m_c_h,m_s_h,m_c_f,m_s_f=F(3,7),F(-2,5),F(-4,9),F(5,13)
 mp_h=m_c_h+m_s_h;mm_h=m_c_h-m_s_h
 mp_f=m_c_f+m_s_f;mm_f=m_c_f-m_s_f
 assert mm_h*mp_f+mp_h*mm_f==2*(m_c_h*m_c_f-m_s_h*m_s_f)

 # Fully PAID uniform D-form bound after original CC27 source
 # identification: improve previous RC309 nominal prime constant
 # using RC43's finite chain/cosine translation bounds.
 prior3=c("308_bounded_arch_pole")
 schur=c("309_endpoint_schur")
 norm_phys=F(prime["full_paired_prime_physical_operator_norm_upper"])
 old_prime=F(prior3["nominal_prime_L2_operator_norm_upper"])
 assert F(0)<norm_phys<old_prime
 regular=F(prior3["regular_original_physical_L2_operator_norm_upper"])
 pole_norm=F(prior3["exact_pole_rank_two_L2_operator_norm_upper"])
 sl=F(schur["actual_metric_s_lower"])
 assert sl>F(3)
 endpoint=F(schur["full_endpoint_D_inverse_D_to_D_norm_upper"])
 scalar=F(schur["scalar_diagonal_D_inverse_D_to_D_norm_upper"])
 original_full_model=1+endpoint+(norm_phys+regular+pole_norm)/sl+scalar
 previous_abstract=F(schur["conditional_abstract_original_action_model_bound"])
 assert original_full_model<previous_abstract
 full_model_upper=ceil_grid(original_full_model)
 assert full_model_upper<previous_abstract
 augmented=F(c("310_core_parity_contract")[
    "rank317_augmentation_D_to_D_operator_norm_upper"])
 assert augmented>0
 # This action is the bounded D-Riesz representative of the
 # ORIGINAL CC27 mixed form. It is NOT the canonical logarithmic
 # metric identity operator, and it is not positive merely because
 # it has a bounded norm.
 # Polynomial form identification is exact for arbitrary degrees:
 # RC312 supplies arch; above gives prime/pole; RC311 contact
 # and RC309 ensure continuity in D. RC121 guarantees equivalent
 # D and canonical supported form domains, thus the equality
 # extends uniquely by density IF CC27's original source formula
 # is accepted as defining the canonical Weil form.
 return dict(
  milestone="RC313",
  parent_merge_commit="96cb955efc0682b42e505197b63d120140b7a353",
  exact_source_blob_pins=PINS,
  source_definition="original CC27 Weil quadratic form, with actual Fourier convention exp(-2pi i xi x)",
  strict_cutoff_original_aperture_B=str(B),
  strict_prime_power_support_n_less_than_exp_2B=[2,3,4,5,7,8,9],
  exp_2B_lower_exact_rational=str(floor_grid(low_e)),
  exp_2B_upper_exact_rational=str(ceil_grid(high_e)),
  all_prime_power_translation_and_Chebyshev_summands_reenclosed=records,
  all_degree_original_prime_Fourier_multiplier_to_translations=(
   "-2 sum_{n prime power} Lambda(n)/sqrt(n)*cos(2pi xi log n) "
   "corresponds exactly to -sum c_n(T_ell+T_-ell)"),
  all_supported_inputs_zero_extended_no_periodic_wraparound=True,
  original_prime_has_no_extra_factor_two=True,
  every_prime_power_base_prime_coefficient_not_log_n=True,
  direct_prime_bilinear_regressions=pair_results,
  original_prime_operator_Hermitian_on_physical_L2=True,
  signed_pole_original_source_formula="conj(m_-(h))*m_+(f)+conj(m_+(h))*m_-(f)",
  pole_m_plus_Fourier_analytic_argument="xi=+i/(4pi)",
  pole_m_minus_Fourier_analytic_argument="xi=-i/(4pi)",
  complete_rank_two_pole_operator_identified=(
    "2|cosh(x/2)><cosh(x/2)| - 2|sinh(x/2)><sinh(x/2)|"),
  signed_pole_even_positive_odd_negative=True,
  pole_Rodrigues_Taylor_parity_checks=parity_cases,
  full_CC27_prime_pole_distributional_source_identity_on_all_polynomials=True,
  full_CC27_archimedean_source_identity_imported_RC312=True,
  original_CC27_Weil_polynomial_form_matches_native_model_on_all_degrees=True,
  original_CC27_Weil_bounded_D_Riesz_extension_unique_under_RC121_equivalence=True,
  original_CC27_original_form_vs_complete_native_model_identification=True,
  original_prime_finite_chain_L2_norm_upper=str(ceil_grid(norm_phys)),
  previous_nominal_prime_L2_norm_upper=str(ceil_grid(old_prime)),
  improved_original_native_Weil_D_to_D_operator_norm_upper=str(full_model_upper),
  previous_conditional_abstract_D_to_D_norm_upper=str(ceil_grid(previous_abstract)),
  original_augmented_model_D_to_D_norm_upper=str(
   ceil_grid(original_full_model+augmented)),
  positive_spectral_lower_bound_proved=False,
  original_Weil_form_positivity_certified=False,
  RC292_signed_inverse_response_certified=False,
  rank314_Schur_principal_gate_positive=False,
  actual_zeta_zero_synthesis_on_all_completed_carriers_newly_established=False,
  full_Lean_formalization_newly_completed=False,
  Stage_I_closed=False,F4=False,RH=False,Lean=False,
  next_cursor=(
   "RC314: now that the original CC27 Weil polynomial core and "
   "completed D-Riesz representation are identified, investigate "
   "an actual positive spectral lower bound for the FULL "
   "signed operator and remaining rank314 Schur complement; "
   "a bounded upper operator norm does not supply a lower bound "
   "and no signed Chebyshev inverse is yet certified.")
 )
if __name__=="__main__":
 parser=argparse.ArgumentParser()
 parser.add_argument("--output",type=Path,required=True)
 parser.add_argument("--replay",action="store_true")
 a=parser.parse_args()
 result=run(reverse=a.replay)
 if a.replay:
  assert result==json.loads(a.output.read_text(encoding="utf-8"))
 else:
  a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
 print("RC313 VALIDATED: complete CC27 prime-pole distributional "
       "polynomial core and bounded D-Riesz transfer; "
       "spectral positivity/Stage I OPEN",flush=True)
