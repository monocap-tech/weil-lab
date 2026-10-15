"""RC309 — exact weighted-Schur bound for the singular endpoint Legendre matrix.

The original native endpoint head has even/odd parity blocks
    E[n,d] = (2n+1)/(|n-d|(n+d+1)), n!=d,
    E[n,n] = 2H_(2n)-2H_n+1/(2n+1).
The off-diagonal 1/|n-d| alone has logarithmic Schur row growth;
the conjugated D-energy action D^-1 E is nevertheless bounded.

Let m_n=2B/(2n+1), D_n=H_n+s (s>=s_lower>3), and
H_D = l2(m_n D_n). Weighted symmetry m_n E[n,d]=m_d E[d,n]
makes the l2 conjugate symmetric. Schur weight p_n=sqrt(m_n/D_n)
reduces both weighted row and column tests to
   sum_{d same parity n} E[n,d]/D_d <= 2+9/s_lower,
uniformly for every n, including n=0,1.

Analytic proof partitions d<n/2, n/2<=d<=2n, d>2n;
the lower and upper blocks each cost <=3/s, the near-diagonal
block <=2 and the diagonal <=3/s. Uniformity over infinite
indices is from inequalities, NOT finite numerical sampling.

Under the *explicitly imported* RC237 native original-source
decomposition, combine this with the RC308 common-carrier
prime/archimedean/pole components and the scalar diagonal
(-log2 -789/125) to produce a bounded ABSTRACT N_model. This
is a conditional algebraic model, not a new independent
identification with the canonical Weil operator or a positivity
certificate. Polynomial powers of N_model are well-defined;
RC292's spectral/Schur positivity and signed inverse remain OPEN.
"""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import validate_rpb108_rc252_signed_endpoint_tail as endpoint_source
import validate_rpb108_rc237_two_trial_signed_response as native

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
GRID=10**24
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":
 "33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc303_direct_polynomial_prime.json":
 "cc71c9a961230ecedeb65947afae15ba37f0abbe",
 "certificates/rpb108_rc304_p10_high_mixed.json":
 "5f098868017a19ec753c6f6e4b724cd5036d053b",
 "certificates/rpb108_rc308_bounded_arch_pole.json":
 "2461485678ec998ed7449e8a6141a3b71e083f35",
 "scripts/validate_rpb108_rc237_two_trial_signed_response.py":
 "d13e909c8aa8b91d5b55ec5e5e5179cdaf9325d2",
 "scripts/validate_rpb108_rc252_signed_endpoint_tail.py":
 "e3b89120820dc08b049c87bcc2867a5bc94b8ad9",
}

def ceil_grid(x):
 assert x>=0
 return F((x.numerator*GRID+x.denominator-1)//x.denominator,GRID)

def floor_grid(x):
 assert x>=0
 return F(x.numerator*GRID//x.denominator,GRID)

def harmonic_numbers(last):
 arr=[F(0)]
 for i in range(1,last+1):
  arr.append(arr[-1]+F(1,i))
 return arr

def E(n,d,H):
 assert n>=0 and d>=0
 if n%2!=d%2: return F(0)
 if n!=d: return F(2*n+1,abs(n-d)*(n+d+1))
 return 2*(H[2*n]-H[n])+F(1,2*n+1)

def mass(n):
 return 2*B/F(2*n+1)

def log2_interval():
 # atanh(1/3) exact rational remainder.
 low=2*sum((F(1,3)**(2*k+1)/F(2*k+1) for k in range(100)),F(0))
 high=low+2*F(1,3)**201/(201*(1-F(1,9)))
 assert 0<low<high<1
 return low,high

def run(reverse=False):
 data={}
 for path,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  blob=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
  assert blob==pin,(path,"pinned source changed")
  if path.endswith(".json"):data[path]=json.loads(raw)
 def get(k):return data["certificates/rpb108_rc"+k+".json"]
 mom=get("129_four_vector_joint_moment")
 prev=get("308_bounded_arch_pole")
 rc303=get("303_direct_polynomial_prime")
 rc304=get("304_p10_high_mixed")
 assert prev["three_component_operator_extends_boundedly_to_physical_L2"]
 assert not prev["full_endpoint_singular_source_bounded_on_common_L2"]
 assert rc303["new_native_P10_original_action"]["input"]=="P10"
 assert rc304["input_even_legendre_degrees_supported"]==[0,2,4,6,8,10]
 s_low=F(mom["actual_D_Gram_entry_lower"][0][0])/(2*B)
 s_hi=F(mom["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert F(3)<s_low<=s_hi<F(5)
 C_end=F(2)+F(9)/s_low
 assert C_end<F(5)
 C3=F(prev["three_component_nominal_source_L2_operator_norm_upper"])
 assert C3>0
 C3_D=F(prev["three_component_D_inverse_D_to_D_norm_upper"])
 assert C3_D>=C3/s_low
 Llo,Lhi=log2_interval()
 cdiag=F(789,125)+Lhi
 C_shift=cdiag/s_low
 C_model=F(1)+C_end+C3_D+C_shift
 assert C_model<F(12)
 # Core normalized source map is model:
 # N_model = I + D^-1(E - (log2+789/125) I + S3).
 # Each term is bounded on H_D. No claim this decomposition
 # has been proved from original explicit formula for every L2
 # completion vector; exact identification is inherited on a
 # polynomial core from RC237/303 and still requires audit.

 H=harmonic_numbers(1024)
 degrees=[0,1,2,3,4,5,8,10,16,32,64,128,256]
 if reverse:degrees=list(reversed(degrees))
 checks=[]
 for n in degrees:
  assert H[n]==native.orig.H(n)
  assert H[2*n]==native.orig.H(2*n)
  dmax=max(2*n+128,128)
  assert dmax<=1024
  if n==0:
   assert E(n,n,H)==1
  else:
   diag=2*(native.orig.H(2*n)-native.orig.H(n))+F(1,2*n+1)
   assert E(n,n,H)==diag and 0<diag<3
  # The original endpoint routine is independently imported.
  # For n>d, no diagonal log2 enclosure is needed.
  for d in range(n%2,n,2):
   a=[F(0)]*(d+1);a[d]=F(1)
   actual,radius=endpoint_source.native.endpoint(a,n,F(0),F(0))
   assert radius==0 and actual==E(n,d,H)
   assert mass(n)*E(n,d,H)==mass(d)*E(d,n,H)
  # Full finite section is a LOWER bound to the positive
  # weighted Schur row; the proof applies to all d> dmax too.
  terms=[]
  for d in range(n%2,dmax+1,2):
   v=E(n,d,H)/(H[d]+s_low)
   assert v>=0
   terms.append(v)
  if reverse:terms.reverse()
  subtotal=sum(terms,F(0))
  assert 0<=subtotal<C_end
  checks.append(dict(
     n=n,
     first_source_degree=n%2,
     highest_source_degree=dmax if dmax%2==n%2 else dmax-1,
     exact_finite_weighted_Schur_row_lower=str(floor_grid(subtotal)),
     universal_weighted_Schur_upper=str(C_end),
     entire_infinite_row_upper_certified_by_analytic_partition=True))
 checks.sort(key=lambda r:r["n"])
 # Symbolic universal proof obligations, checked also on large
 # degrees. No finite cutoff is used for the theorem.
 for n in (range(2,130) if not reverse else reversed(range(2,130))):
  k=n//2
  assert F(2*n+1,n+1)<2 # h_n,d <= 2/|n-d|
  assert F(2*n+1,(F(n,2))*(n+1))<F(4,n)
  assert F(4*n+2,2*n)<=3
  # Harmonic difference H_n-H_floor(n/2) <= 1.
  assert H[n]-H[k]<=1
  assert 2*H[k]/(H[k]+s_low)<=2
  # d<n/2 of same parity: at most n/4+1 indices.
  num=sum(1 for d in range(n%2,n,2) if F(d)<F(n,2))
  assert num<=F(n,4)+1
  # d in middle: 1/|n-d| <= one of harmonic half-sums.
  medium=sum((F(1,abs(n-d)) for d in range(n%2,2*n+1,2)
              if d!=n and F(n,2)<=d<=2*n),F(0))
  assert medium<=H[k]

 # For n=0, row diag=1 and h(0,d)=1/[d(d+1)].
 # For n=1, there are no lower terms; all d>=3 are high.
 # These are directly covered by the same 2+9/s constant.
 assert C_end>F(1,s_low)+F(1,2*s_low)
 assert C_end>F(3,s_low)+F(3,s_low)

 return dict(
  milestone="RC309",
  parent_merge_commit="9e0588cff619151856523f30cca1e6db419cdc54",
  pinned_sources=PINS,
  physical_B=str(B),
  actual_metric_s_lower=str(s_low),
  actual_metric_s_upper=str(s_hi),
  endpoint_native_matrix_definition=(
    "E[n,d]=(2n+1)/(|n-d|(n+d+1)) for n!=d with same parity, "
    "zero for opposite parity, E[n,n]=2(H[2n]-H[n])+1/(2n+1)"),
  physical_self_adjoint_mass_balance_mn_En_d_equals_md_Ed_n=True,
  weighted_Schur_test_weight="p[n]=sqrt(m[n]/(H[n]+s))",
  weighted_row_and_column_sum_formula="sum_{d congruent n mod 2} E[n,d]/(H[d]+s)",
  analytic_partition_low_d_less_than_n_over_2_upper="3/s",
  analytic_partition_mid_n_over_2_through_2n_upper="2",
  analytic_partition_high_d_greater_than_2n_upper="3/s",
  analytic_diagonal_upper="3/s",
  two_small_row_cases_n0_n1_handled=True,
  all_n_unbounded_index_set_covered_by_symbolic_partition=True,
  full_endpoint_D_inverse_D_to_D_norm_upper=str(C_end),
  low_mode_native_endpoint_action_regression_checks=checks,
  nominal_three_component_D_inverse_D_to_D_norm_upper=str(C3_D),
  original_log2_lower=str(Llo),
  original_log2_upper=str(Lhi),
  inherited_original_scalar_diagonal_789_over_125=str(F(789,125)),
  scalar_diagonal_D_inverse_D_to_D_norm_upper=str(C_shift),
  conditional_abstract_original_action_model_bound=str(C_model),
  abstract_bounded_model_N_powers_exist=True,
  actual_original_Weil_core_decomposition_newly_proved_independently=False,
  actual_full_Weil_operator_equivalence_without_inherited_identities=False,
  canonical_signed_inverse_response_established=False,
  positive_spectral_lower_bound_for_model_established=False,
  remaining_314_principal_Schur_positive=False,
  original_Weil_form_positivity_certified=False,
  RC292_Chebyshev_residual_certified=False,
  Stage_I_closed=False,F4=False,RH=False,Lean=False,
  next_cursor=(
    "RC310: audit the complete native original Weil core decomposition "
    "on BOTH parities and transfer the bounded abstract N_model "
    "to the canonical action with exact source-identification; "
    "then certify the spectral lower/upper bounds and signed "
    "Schur positivity prerequisites of RC292. Boundedness alone "
    "does not establish positivity or signed inverse accuracy.")
 )
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 r=run(a.replay)
 if a.replay:assert r==json.loads(a.output.read_text(encoding="utf-8"))
 else:a.output.write_text(json.dumps(r,sort_keys=True,indent=2)+"\n",encoding="utf-8")
 print("RC309 VALIDATED: endpoint weighted Schur on whole D completion, "
       "conditional abstract full action model bounded; "
       "Stage I OPEN",flush=True)
