"""RC306: replace exponential monomial prime error with polynomial Markov bound.

For an arbitrary signed even Legendre polynomial q of degree <=D,
||q||_infty <= sqrt(S_D)||q||_2, S_D=sum_{even d<=D}1/m_d.
Classical Markov: ||q'||_infty <= D^2/B ||q||_infty
on the physical support [-B,B]. This produces a direct uniform
L2 bound for parameter uncertainty in all seven *signed translated,
compactly supported* prime sources. It is NOT the old exponentially
large monomial coefficient majorant.

For endpoint output n>=N(D)=max(2050,2D+2), the RC252 moment formula
admits every signed coefficient vector. Its parity-tail D-energy is
bounded by a UNIVERSAL constant over all finite even input degrees,
provided N increases with D. Thus a dimension-free bound is obtained
for the *adaptive omitted endpoint suboperator*, NOT for a fixed
output truncation, nor for the complete Weil operator.

Classical Legendre ||P_d||_infty<=1 and Markov inequality are analytic
inputs (not newly proved by Actions). Full prime/regular/pole/endpoint
operator action and Chebyshev recursion remain open.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,json

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
SCALE=10**24
BASE=2050
DEGREES=(10,20,32,64,128,256,512,1024,1536,2048,4096,8192)
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":
  "33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc43_native_prime_head.json":
  "b4893953109e6fdc55d52b505c2bcfbf0d38281e",
 "certificates/rpb108_rc303_direct_polynomial_prime.json":
  "cc71c9a961230ecedeb65947afae15ba37f0abbe",
 "certificates/rpb108_rc304_p10_high_mixed.json":
  "5f098868017a19ec753c6f6e4b724cd5036d053b",
 "certificates/rpb108_rc305_signed_uniform_tail.json":
  "ec72d1eee5b610607806d191b9a4b8bb569b7349",
}

def sqrt_up(x):
 assert x>=0
 if x==0:return F(0)
 return F(isqrt(x.numerator*SCALE*SCALE//x.denominator)+1,SCALE)

def sqrt_down(x):
 assert x>=0
 if x==0:return F(0)
 return F(isqrt(x.numerator*SCALE*SCALE//x.denominator),SCALE)

def legendre_mass(d):
 return 2*B/F(2*d+1)

def S(D):
 assert isinstance(D,int) and D>=0 and D%2==0
 k=D//2
 return F((k+1)*(2*k+1),1)/(2*B)

def f(n):
 return F(1,n*n)-F(1,(n+1)*(n+1))

def rows(prime):
 ret=[]
 for row in prime["active_prime_powers"]:
  elllo,ellhi=F(row["translation_lower"]),F(row["translation_upper"])
  clo,chi=F(row["coefficient_lower"]),F(row["coefficient_upper"])
  assert 0<elllo<=ellhi and 0<clo<=chi
  ret.append((F(ellhi-elllo,2),F(chi-clo,2),chi))
 assert len(ret)==7
 assert all(dl>0 and dc>0 for dl,dc,ch in ret)
 return ret

def prime_bound(D,pr):
 # Compactly supported translations are controlled separately
 # on the symmetric-difference strips (length <=2 delta_ell)
 # and on the common overlap (length <=2B). The original
 # RC237 factors of 2 are retained, now with a sup-norm and
 # physical derivative (classical Markov), not monomial l1.
 s=S(D)
 L2=s*F(D**4,1)/(B*B)
 terms=[2*(dc+ch*sqrt_up(2*dl*s+2*B*dl*dl*L2))
        for dl,dc,ch in pr]
 return sum(terms,F(0))

def adaptive_endpoint(D,Hbase,sl):
 assert D%2==0 and D>=0
 N=max(BASE,2*D+2)
 assert N%2==0 and N>D
 gap=1-F(D*(D+1),N*(N+1))
 assert F(3,4)<gap<=1
 # Since H_N>=H_2050, using the *fixed Hbase* in the
 # denominator gives a valid but slightly conservative bound.
 W=(F(1,N*N)+f(N))/2
 assert 0<W<F(1,N*N)
 E2=2*B*S(D)*W/((Hbase+sl)*gap*gap)
 return N,gap,W,E2

def check_structure_all_degrees(D):
 N=max(BASE,2*D+2)
 assert 4*D*(D+1) < N*(N+1)
 assert 2*B*S(D)/F(N*N)<=F(1,4)
 assert F(1,2)*(F(1,N*N)+f(N))<=F(1,N*N)
 # General polynomial identity for N0=2(D+1):
 # N0(N0+1)-4D(D+1) = 6(D+1)>0.
 N0=2*(D+1)
 assert N0*(N0+1)-4*D*(D+1)==6*(D+1)
 assert 2*B*S(D)/F(N0*N0)==F(D+2,8*(D+1))

def main(reverse=False):
 data={}
 for path,sha in sorted(PINS.items(),reverse=reverse):
  b=(ROOT/path).read_bytes()
  h=hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
  assert h==sha,(path,"source blob changed")
  data[path]=json.loads(b)
 def get(s):return data["certificates/rpb108_rc"+s+".json"]
 old=get("305_signed_uniform_tail")
 oldprime={x["max_even_input_degree"]:x
           for x in old["universal_all_signed_coefficients_prime_parameter_bound_by_degree"]}
 oldend={x["max_even_input_degree"]:x
         for x in old["universal_all_signed_coefficients_endpoint_tail_bound_by_degree"]}
 assert sorted(oldprime)==[10,20,32,64]
 assert old["prime_arithmetic_suboperator_uniform_on_every_reported_finite_degree_cap"]
 assert old["uniform_endpoint_bound_avoids_RC252_positive_signed_moment_assumption"]
 assert get("304_p10_high_mixed")["input_even_legendre_degrees_supported"]==[0,2,4,6,8,10]
 original=get("303_direct_polynomial_prime")
 assert original["direct_native_prime_translation_available_for_signed_polynomials"]
 m=get("129_four_vector_joint_moment")
 sl=F(m["actual_D_Gram_entry_lower"][0][0])/(2*B)
 sh=F(m["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert 0<sl<=sh
 pr=rows(get("43_native_prime_head"))
 H=F(0)
 for n in range(1,BASE+1):H+=F(1,n)
 assert H>F(8) and H<F(9)
 global_E2=F(4,9)/(H+sl)
 global_E=sqrt_up(global_E2)
 assert global_E< F(1,4)
 # Proof works for arbitrary even D, not only sampled D values:
 # N>=2D+2, S_D<=N^2/(8B), W_N<1/N^2,
 # 1-D(D+1)/(N(N+1))>3/4, and H_N>=Hbase.
 records=[]
 for D in (reversed(DEGREES) if reverse else DEGREES):
  check_structure_all_degrees(D)
  N,gap,W,E2=adaptive_endpoint(D,H,sl)
  E=sqrt_up(E2)
  assert E<global_E and E2<global_E2
  Cp=prime_bound(D,pr)
  assert Cp>0
  inv=sqrt_up(Cp*Cp/sl)
  # For fixed D, sup-norm L2->Linf constant sqrt(S_D),
  # Markov derivative constant D^2/B in physical coordinates.
  #
  # D-uniform prime bound is polynomial-growing, NOT bounded
  # uniformly in D. The exact formula is sufficient to evaluate
  # any given integer input-degree cap without basis expansion.
  row=dict(
   even_input_maximum_degree=D,
   first_adaptively_omitted_even_output_degree=N,
   signed_endpoint_geometric_gap_exact=str(gap),
   parity_telescoping_weight_upper_exact=str(W),
   signed_endpoint_tail_D_energy_per_input_L2_squared_upper=str(E2),
   signed_endpoint_tail_D_norm_per_input_L2_upper=str(E),
   prime_supnorm_embedding_squared_exact=str(S(D)),
   physical_Markov_derivative_factor_exact=str(F(D*D,1)/B),
   physical_Markov_derivative_embedding_squared_exact=str(
      F(D**4,1)*S(D)/(B*B)),
   all_seven_signed_prime_translation_L2_error_per_input_L2_upper=str(Cp),
   all_seven_signed_prime_D_inverse_error_per_input_L2_upper=str(inv),
   source_coefficients_may_have_arbitrary_signs=True,
   source_positive_signed_moment_unnecessary=True,
   dimension_free_for_adaptive_endpoint_tail_only=True)
  if D in oldprime:
   prior=F(oldprime[D]["full_prime_parameter_L2_error_per_input_L2_upper"])
   assert Cp<prior,("new prime bound not better",D)
   row["RC305_monomial_prime_error_bound"]=str(prior)
   row["verified_sharp_prime_bound_improvement_factor_lower"]=str(
      F(prior.numerator*Cp.denominator//(prior.denominator*Cp.numerator)))
  if D in oldend:
   priorE2=F(oldend[D][
      "uniform_endpoint_tail_D_energy_per_input_L2_squared_upper_exact"])
   if N==BASE:
    assert E2==priorE2,("fixed-cutoff endpoint regression",D)
   else:
    assert E2<priorE2,("adaptive tail did not improve",D)
   row["RC305_fixed_cutoff_endpoint_D_energy_per_input_L2_squared_upper"]=str(priorE2)
  records.append(row)
 records.sort(key=lambda z:z["even_input_maximum_degree"])
 assert records[0]["even_input_maximum_degree"]==10
 assert records[-1]["even_input_maximum_degree"]==8192

 # Explicit compact-support translated polynomial consistency:
 # legacy direct signed P4-P6/2+P8/3-P10/5 source norm,
 # with nontrivial coefficients and all seven active primes.
 mix={4:F(1),6:F(-1,2),8:F(1,3),10:F(-1,5)}
 norm2=sum((c*c*legendre_mass(d) for d,c in mix.items()),F(0))
 actual=original["mixed_signed_even_polynomial_action"][
     "directly_evaluated_prime_source"]
 assert norm2==F(actual["direct_polynomial_mass_squared"])
 # This new analytic bound is an independently derived upper bound
 # for the TRUE parameter perturbation, NOT necessarily for the
 # numerically much looser inherited RC303 upper estimate.
 # Do NOT assert RC303's old *bound* lies below this new one.
 cap10=F(records[0][
     "all_seven_signed_prime_translation_L2_error_per_input_L2_upper"])
 mix_delta=cap10*sqrt_up(norm2)
 assert mix_delta>0 and mix_delta< F(1,10**15)

 # Sanity on true basis embedding using P0,P2,P4:
 # |P_d(x)|<=1 and Markov's inequality are standard imported
 # analytic facts, not empirical deductions from sample points.
 # Test exact endpoint equalities P_d(1)=1, P'_d(1)=d(d+1)/2.
 import validate_rpb108_rc237_two_trial_signed_response as legacy
 for d in [0,2,4,10,20,32]:
  if d>32:continue
  L=legacy.orig.legendre(d)
  assert sum(L,F(0))==1
  assert sum((k*L[k] for k in range(len(L))),F(0))==F(d*(d+1),2)

 return dict(
  milestone="RC306",
  starting_commit="540e46d0bde48589bbcee25c6f291e02b08b16cd",
  input_git_blob_pins=PINS,
  method="physical_supnorm_and_classical_Markov_instead_of_monomial_l1",
  all_even_polynomial_degrees_covered_by_symbolic_closed_form=True,
  signed_prime_translation_interval_error_uniform_for_each_finite_degree_cap=True,
  prime_error_dimension_free_for_unbounded_degree=False,
  adaptive_output_cutoff_formula="max(2050, 2*D+2) (D even)",
  full_adaptive_endpoint_tail_dimension_free_D_norm_per_input_L2_upper=str(global_E),
  full_adaptive_endpoint_tail_dimension_free_D_energy_per_input_L2_squared_upper=str(global_E2),
  source_sign_or_positive_signed_moment_assumption=False,
  degree_independent_endpoint_tail_with_moving_output_cutoff_certified=True,
  degree_independent_endpoint_tail_with_fixed_output_cutoff_certified=False,
  all_degree_sampling_replay_records=records,
  direct_mixed_P10_input_physical_L2_squared=str(norm2),
  derived_mixed_input_prime_parameter_L2_error_upper=str(mix_delta),
  inherited_previous_monomial_estimate_may_exceed_sharp_new_upper=True,
  standard_legendre_unit_supnorm_imported_not_fully_formalized=True,
  classical_Markov_inequality_imported_not_fully_formalized=True,
  signed_translation_support_perturbation_L2_geometry_imported_from_RC237=True,
  full_original_prime_source_L2_operator_bound_certified=False,
  full_original_Weil_action_uniform_for_all_input_degrees=False,
  full_infinite_input_action_certified=False,
  repeatable_Chebyshev_inverse_operator_action_certified=False,
  remaining_314_principal_Schur_positive=False,
  original_Weil_form_positivity_certified=False,
  Stage_I_closed=False,RH=False,F4=False,Lean=False,
  next_cursor=(
    "RC307: integrate the polynomially growing signed-prime source "
    "parameter error and universally bounded degree-adaptive "
    "endpoint tail with a corresponding degree-adaptive direct "
    "prime projection and complete archimedean/pole errors. "
    "The resulting full operator must be bounded on a common "
    "completion before repeated Chebyshev actions are claimed.")
 )
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 args=p.parse_args()
 x=main(reverse=args.replay)
 if args.replay: assert x==json.loads(args.output.read_text(encoding="utf-8"))
 else: args.output.write_text(json.dumps(x,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print("RC306 VALIDATED: signed prime Markov bound and all-degree "
       "adaptive endpoint tail; Stage I OPEN",flush=True)
