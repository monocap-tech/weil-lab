"""RC305: signed-uniform analytic *suboperator* bounds by polynomial degree.

The inherited RC252 endpoint tail gate requires a strictly positive
signed moment bracket. That property is NOT stable under arbitrary
signed polynomial inputs. Replace it with a rigorous Cauchy/geometric
bound valid for every even Legendre polynomial of degree <=D, with
endpoint output modes n>=first>D.

Separately bound the inherited signed-prime interval-parameter defect
for all coefficients in each input degree cap, using exact Legendre
monomial l1 and derivative majorants and physical L2 Cauchy. These are
bounds on SUBTERMS, not the complete Weil action or its iterates.

No global/infinite-input operator bound, original Weil-form positivity,
Stage I, F4 or RH proof is claimed. All numbers are exact Fraction
arithmetic with rational outward square-root grids.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

import validate_rpb108_rc237_two_trial_signed_response as legacy
import validate_rpb108_rc252_signed_endpoint_tail as signed

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
G=10**18
orig=legacy.orig
END=2048
FIRST=2050
DEGREES=(10,20,32,64,128,256,512,1024,1536,2048)
PRIME_DEGREES=(10,20,32,64)
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":
  "33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc43_native_prime_head.json":
  "b4893953109e6fdc55d52b505c2bcfbf0d38281e",
 "certificates/rpb108_rc303_direct_polynomial_prime.json":
  "cc71c9a961230ecedeb65947afae15ba37f0abbe",
 "certificates/rpb108_rc304_p10_high_mixed.json":
  "5f098868017a19ec753c6f6e4b724cd5036d053b",
 "scripts/validate_rpb108_rc237_two_trial_signed_response.py":
  "d13e909c8aa8b91d5b55ec5e5e5179cdaf9325d2",
 "scripts/validate_rpb108_rc252_signed_endpoint_tail.py":
  "e3b89120820dc08b049c87bcc2867a5bc94b8ad9",
}

def sqrt_up(x):
 assert x>=0
 if x==0:return F(0)
 return F(isqrt(x.numerator*G*G//x.denominator)+1,G)

def sqrt_down(x):
 assert x>=0
 if x==0:return F(0)
 return F(isqrt(x.numerator*G*G//x.denominator),G)

def m(d):
 return 2*B/F(2*d+1)

def add(a,b):
 z=[F(0)]*max(len(a),len(b))
 for j,v in enumerate(a):z[j]+=v
 for j,v in enumerate(b):z[j]+=v
 return z

def qpoly(coeff):
 p=[F(0)]
 for d,v in coeff.items():
  p=add(p,[v*x for x in orig.legendre(d)])
 return p

def norm2(coeff):
 return sum((a*a*m(d) for d,a in coeff.items()),F(0))

def parameter_rows(prime):
 res=[]
 for row in prime["active_prime_powers"]:
  el,eh=map(F,[row["translation_lower"],row["translation_upper"]])
  cl,ch=map(F,[row["coefficient_lower"],row["coefficient_upper"]])
  assert 0<=el<=eh and 0<=cl<=ch
  res.append((F(eh-el,2),F(ch-cl,2),ch))
 assert len(res)==7
 return res

def main(reverse=False):
 data={}
 for path,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  got=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
  assert got==sha,(path,"pinned source changed")
  if path.endswith(".json"):data[path]=json.loads(raw)
 def get(k):return data["certificates/rpb108_rc"+k+".json"]
 metric=get("129_four_vector_joint_moment")
 sl=F(metric["actual_D_Gram_entry_lower"][0][0])/(2*B)
 sh=F(metric["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert 0<sl<=sh
 prime=get("43_native_prime_head")
 rows=parameter_rows(prime)
 old=get("303_direct_polynomial_prime")
 prev=get("304_p10_high_mixed")
 assert old["first_new_input_degree_beyond_previous_V5"]==10
 assert prev["input_even_legendre_degrees_supported"]==[0,2,4,6,8,10]
 assert not prev["input_degree_uniform_over_all_polynomials"]

 H=[F(0)]
 for n in range(1,FIRST+1):H.append(H[-1]+F(1,n))
 f=lambda n:F(1,n*n)-F(1,(n+1)**2)
 parity_weight=(F(1,FIRST*FIRST)+f(FIRST))/2
 assert parity_weight>0 and f(FIRST)>0
 # This is an upper bound for the same-parity positive series of f(n)
 # by the alternating decreasing sequence comparison.
 x=F(FIRST*(FIRST+1))
 endpoint=[]
 for D in (reversed(DEGREES) if reverse else DEGREES):
  assert D%2==0 and D<FIRST and D>=10
  k=D//2
  # Sum_{j=0}^k 1/m_{2j}; an exact closed form, valid on the
  # orthogonal physical interval [-B,B].
  norm_dual_sq=sum((1/m(d) for d in range(0,D+1,2)),F(0))
  assert norm_dual_sq==F((k+1)*(2*k+1),2*B)
  spectral_tmax=F(D*(D+1))
  gap=1-spectral_tmax/x
  assert gap>0
  # For every even a supported on d<=D, signed cancellations allowed:
  # M_n = sum_d a_d / (1-t_d/x_n), |M_n| <=
  # sqrt(norm_dual_sq)*||a||_L2 /gap. No positive-moment hypothesis.
  endC2=2*B*norm_dual_sq*parity_weight/(
      (H[FIRST]+sl)*gap*gap)
  endC=sqrt_up(endC2)
  assert endC*endC>=endC2 and endC>0
  endpoint.append(dict(
   max_even_input_degree=D,
   endpoint_first_omitted_even_output=FIRST,
   endpoint_output_geometric_gap_exact=str(gap),
   input_Legendre_l1_dual_norm_squared_exact=str(norm_dual_sq),
   signed_parity_tail_weight_upper_exact=str(parity_weight),
   uniform_endpoint_tail_D_energy_per_input_L2_squared_upper_exact=str(endC2),
   uniform_endpoint_tail_D_norm_per_input_L2_upper=str(endC),
   every_real_signed_coefficient_choice_covered=True,
   positivity_of_signed_moments_not_required=True))
 endpoint.sort(key=lambda v:v["max_even_input_degree"])
 assert endpoint[0]["max_even_input_degree"]==10
 assert endpoint[-1]["max_even_input_degree"]==2048

 # Every even input polynomial in span(P0,P2,...,PD) has
 # q(x)=sum a_d P_d(x), ||q||_L2^2=sum m_d a_d^2.
 # For q=sum_k b_k x^k, the original RC237 primitive bounds
 # A(q)=sum|b_k| and T(q)=sum k|b_k|/B.
 # By triangle and weighted Cauchy:
 # A(q)^2 <= (sum A(P_d)^2/m_d) * ||q||_L2^2,
 # T(q)^2 <= (sum T(P_d)^2/m_d) * ||q||_L2^2.
 # This is an actual whole-input-space estimate, not a sample grid.
 A2=F(0);T2=F(0)
 prime_rows=[]
 for d in range(0,max(PRIME_DEGREES)+1,2):
  pol=orig.legendre(d)
  assert len(pol)==d+1
  assert all(pol[k]==0 for k in range(1,d+1,2))
  A=sum(map(abs,pol),F(0))
  T=sum((k*abs(a) for k,a in enumerate(pol)),F(0))/B
  A2+=A*A/m(d)
  T2+=T*T/m(d)
  if d not in PRIME_DEGREES:continue
  # RC237 parameter fault:
  # 2 Sum_j [delta_c_j ||q||_L2
  #    + c_j sqrt(2 delta_ell_j A(q)^2
  #       +2B delta_ell_j^2 T(q)^2)].
  const=2*sum((dc+ch*sqrt_up(2*de*A2+2*B*de*de*T2)
               for de,dc,ch in rows),F(0))
  Dconst=sqrt_up(const*const/sl)
  assert const>0 and Dconst>0
  prime_rows.append(dict(
   max_even_input_degree=d,
   input_monomial_l1_operator_norm_squared_exact=str(A2),
   input_monomial_derivative_l1_operator_norm_squared_exact=str(T2),
   full_prime_parameter_L2_error_per_input_L2_upper=str(const),
   D_inverse_normalized_prime_parameter_error_per_input_L2_upper=str(Dconst),
   all_seven_prime_parameter_errors_charged=True,
   all_real_signed_input_coefficients_covered=True))
 assert [v["max_even_input_degree"] for v in prime_rows]==list(PRIME_DEGREES)

 # Check against the independently evaluated RC303 direct translated
 # prime polynomial, which includes signed coefficients and P10.
 mix={4:F(1),6:F(-1,2),8:F(1,3),10:F(-1,5)}
 q=qpoly(mix)
 A=sum(map(abs,q),F(0))
 T=sum((k*abs(a) for k,a in enumerate(q)),F(0))/B
 norm=norm2(mix)
 assert norm>0
 idx=prime_rows[0]
 assert A*A<=F(idx["input_monomial_l1_operator_norm_squared_exact"])*norm
 assert T*T<=F(idx["input_monomial_derivative_l1_operator_norm_squared_exact"])*norm
 prior_direct=old["mixed_signed_even_polynomial_action"][
    "directly_evaluated_prime_source"]
 assert F(prior_direct["direct_polynomial_mass_squared"])==norm
 actual_fault=F(prior_direct["direct_prime_arithmetic_fault_upper"])
 assert actual_fault*actual_fault<=(
   F(idx["full_prime_parameter_L2_error_per_input_L2_upper"])**2
   *norm)

 # Signed endpoint tests include vectors with zero zeroth moment.
 # RC252's positive signed-moment bracket cannot accept all of them.
 # They must nevertheless obey the new absolute source-energy bound.
 endpoint_examples=[]
 for label,a in (
   ("mixed_P4_P6_P8_P10",mix),
   ("cancellation_P0_minus_P2",{0:F(1),2:F(-1)}),
   ("second_difference",{0:F(1),2:F(-2),4:F(1)})
 ):
  aa=[a.get(d,F(0)) for d in range(max(a)+1)]
  assert all(not v for d,v in enumerate(aa) if d%2)
  signed_sum=sum(aa,F(0))
  Q2=norm2(a)
  envelope=F(endpoint[0][
     "uniform_endpoint_tail_D_norm_per_input_L2_upper"])
  assert envelope>0
  controls=[]
  for n in [FIRST,FIRST+2]:
   v,rad=signed.native.endpoint(aa,n,F(0),F(0))
   assert rad==0
   xx=F(n*(n+1))
   direct=(2*n+1)*sum((coeff/(xx-d*(d+1))
                     for d,coeff in enumerate(aa) if coeff),F(0))
   assert v==direct,("signed analytic endpoint identity",label,n)
   # Signed polynomial moment need not be positive; endpoint bound
   # controls magnitude rather than assuming M_n>0.
   lower=F(n*(n+1)-10*11,n*(n+1))
   assert lower>0
   assert abs(xx*v/F(2*n+1))**2 <= (
      F(endpoint[0][
         "input_Legendre_l1_dual_norm_squared_exact"])*Q2/(lower*lower))
   controls.append(dict(degree=n,exact_signed_endpoint_coefficient=str(v)))
  endpoint_examples.append(dict(
   name=label,
   signed_zeroth_moment=str(signed_sum),
   original_input_physical_L2_squared=str(Q2),
   two_high_endpoint_coefficients_exact=controls,
   source_degree_ten_uniform_absolute_endpoint_bound_passed=True))
 assert any(v["signed_zeroth_moment"]=="0" for v in endpoint_examples)
 assert sum(mix.values(),F(0))!=0

 # Guardrail: original finite-output d=10 source uses cutoff64 with
 # 65>3*d+1. That guard fails starting at even d=22.
 valid=[d for d in range(4,65,2) if 65>3*d+1]
 assert valid==list(range(4,21,2))
 assert not (65>3*22+1)
 assert not (1-F(2050*2051,x))>0

 return dict(
  milestone="RC305",
  starting_commit="93f2a120d09181735c5720b2a86f340d8c27d917",
  input_git_blob_pins=PINS,
  universal_all_signed_coefficients_endpoint_tail_bound_by_degree=endpoint,
  universal_all_signed_coefficients_prime_parameter_bound_by_degree=prime_rows,
  signed_polynomial_prime_parameter_mixed_P10_crosscheck=True,
  direct_signed_endpoint_identity_and_uniform_bound_examples=endpoint_examples,
  uniform_endpoint_bound_avoids_RC252_positive_signed_moment_assumption=True,
  original_low_output_cutoff_64_max_even_input_degree_with_3d_guard=20,
  original_low_output_cutoff_64_d22_fails_3d_guard=True,
  original_high_output_cutoff_2048_even_endpoint_first_omitted=FIRST,
  source_degree_2050_not_admissible_for_fixed_tail_cutoff=True,
  prime_arithmetic_suboperator_uniform_on_every_reported_finite_degree_cap=True,
  endpoint_tail_suboperator_uniform_on_every_reported_finite_degree_cap=True,
  analytic_endpoint_formula_imported_from_prior_native_source=True,
  original_signed_prime_parameter_error_formula_imported=True,
  entire_original_Weil_action_uniform_on_all_input_degrees=False,
  arbitrary_infinite_vector_action_certified=False,
  recurrence_composition_certified=False,
  entire_remaining_314_principal_Schur_positive=False,
  original_Weil_form_positivity_certified=False,
  Stage_I_closed=False,RH=False,F4=False,Lean=False,
  next_cursor=(
   "RC306: integrate these sign-robust tail/prime-error operator "
   "constants with degree-adaptive output cutoffs and a certified "
   "full original action on the growing polynomial space; "
   "the unbounded-degree and infinite-input recurrence interface "
   "is NOT yet established."))
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 result=main(reverse=a.replay)
 if a.replay:
  assert result==json.loads(a.output.read_text(encoding="utf-8"))
 else:
  a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",
                      encoding="utf-8")
 print("RC305 VALIDATED: signed-uniform endpoint and prime parameter "
       "suboperator bounds by degree; Stage I OPEN",flush=True)
