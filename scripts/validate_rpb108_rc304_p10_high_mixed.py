"""RC304: P10 original Weil action through degree 2048, and full mixed polynomial.

Pins RC303's native P10 low response and RC279's analytic/prime
high-projector. Appends verified P10 original output through degree 2048,
pays global D source uncertainty and the remaining infinite-output tail,
then the rank317 physical augmentation at P10 only. As an additional
polynomial-input interface check, constructs all 2049 output centers
for q=P4-P6/2+P8/3-P10/5, using the four independently computed
complete action columns and the RC303 directly evaluated low response.
A universal coefficient-independent uniform relative D error bound
extends RC302's finite domain from V5 to V6, with all source tails
retained.

The MIXED high source is obtained by rigorous linear superposition,
NOT a second independent direct high-prime projector; degree-uniform
analytic estimates, arbitrary infinite-vector actions and inverse
recurrences are not certified.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse, hashlib, json
import validate_rpb108_rc279_six_mode_gate as high

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
SCALE=10**15
DEGREES=(0,2,4,6,8,10)
MIX={4:F(1),6:F(-1,2),8:F(1,3),10:F(-1,5)}
orig=high.orig
up=high.up
down=high.down
root=high.root
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":
  "33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc43_native_prime_head.json":
  "b4893953109e6fdc55d52b505c2bcfbf0d38281e",
 "certificates/rpb108_rc279_six_mode_gate.json":
  "bd729c0f5a41debac61a0f3c37276bb94e7834e5",
 "certificates/rpb108_rc283_reduced_reference.json":
  "1dc4bba375af6bfd7a274fccc07638e0eead56e6",
 "certificates/rpb108_rc297_native_p6_high_projection.json":
  "228a2cd9cb8f92324cce7f686f2539b8ddf8f412",
 "certificates/rpb108_rc300_native_p8_high_projection.json":
  "e40c90234bc0d03631f250f710e2a8eb0ac10176",
 "certificates/rpb108_rc302_polynomial_action_interface.json":
  "c4d90de842526e9dfa11f1baf439e15ae3939b5b",
 "certificates/rpb108_rc303_direct_polynomial_prime.json":
  "REPLACE_RC303_CERT_PIN",
 "scripts/validate_rpb108_rc279_six_mode_gate.py":
  "02ff6e1b70e79ede5691aa55bc98c877939cce23",
 "scripts/validate_rpb108_rc273_projection_original_tail.py":
  "4f6163f36097a97190ba50b5e032d942106122ef",
}
def sqrt_up(x):
 assert x>=0
 return F(isqrt(x.numerator*SCALE*SCALE//x.denominator)+1,SCALE) if x else F(0)
def mass(n):
 return 2*B/F(2*n+1)
def run(reverse=False):
 data={}
 for path,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  got=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
  assert got==sha,(path,"pinned source changed")
  if path.endswith(".json"):data[path]=json.loads(raw)
 def get(s):return data["certificates/rpb108_rc"+s+".json"]
 prev=get("303_direct_polynomial_prime")
 old=get("302_polynomial_action_interface")
 assert prev["first_new_input_degree_beyond_previous_V5"]==10
 assert old["N_new_V5_not_subset_V5_certified"]
 low=prev["new_native_P10_original_action"]
 assert low["input"]=="P10" and len(low["finite_original_D_action"])==65
 assert low["all_omitted_outputs_paid"]
 metric=get("129_four_vector_joint_moment")
 sl=F(metric["actual_D_Gram_entry_lower"][0][0])/(2*B)
 sh=F(metric["actual_D_Gram_entry_upper"][0][0])/(2*B)
 sm=(sl+sh)/2
 assert 0<sl<=sm<=sh
 H=[F(0)]
 for n in range(1,2051):H.append(H[-1]+F(1,n))
 prime=get("43_native_prime_head")
 assert len(prime["active_prime_powers"])==7
 p10=high.secondary_action(10,low,prime,sl,sh,H,reverse)
 C10=p10["finite_original_D_action"]
 assert p10["source"]=="P10" and len(C10)==2049
 assert p10["retained_old_center_length"]==65
 assert [row["degree"] for row in C10]==list(range(2049))
 assert all(row["coefficient"]==low["finite_original_D_action"][n]["coefficient"]
            for n,row in enumerate(C10[:65]))
 assert all(x["coefficient"]=="0" for x in C10 if x["degree"]%2)
 assert any(F(C10[n]["coefficient"])!=0 for n in range(66,2049,2))
 assert p10["prime_projection_certificate"]["prime_projection_cutoff"]==2048
 assert p10["prime_projection_certificate"]["all_cross_prime_and_input_terms_preserved"]
 assert F(p10["global_D_fault_norm_upper"])>0
 assert F(p10["model_D_energy_beyond_2048_upper"])>0
 print("RC304: native P10 original high output through 2048 certified",flush=True)
 ref=get("283_reduced_reference")
 assert ref["proposed_buffered_reference_rank"]==317
 preferred=ref["reduced_reference_options"][0]
 choice=preferred["reduced_reference_options"][1]
 assert choice["new_low_reference_rank"]==122
 assert choice["first_discarded_matching_degree"]==244
 lam=F(preferred["parameter_lambda"])
 assert lam>0
 lo=lam/(H[10]+sh)
 hi=lam/(H[10]+sl)
 cent=down((lo+hi)/2)
 radius=up(max(cent-lo,hi-cent))
 assert cent-radius<=lo<=hi<=cent+radius
 patch_norm=sqrt_up(mass(10)*(H[10]+sh)*radius*radius)
 original_fault=F(p10["global_D_fault_norm_upper"])
 augmented_fault=original_fault+patch_norm
 assert augmented_fault>0
 p10patch=dict(
    degree=10,
    exact_lambda=str(lam),
    coefficient_lower=str(lo),
    coefficient_upper=str(hi),
    coefficient_center=str(cent),
    coefficient_radius=str(radius),
    augmented_degree10_center=str(F(C10[10]["coefficient"])+cent),
    augmentation_D_error_upper=str(patch_norm))

 p6=get("297_native_p6_high_projection")
 p8=get("300_native_p8_high_projection")
 p024=get("279_six_mode_gate")["coupled_six_mode_gate_certificates"][0][
    "actual_polynomial_action_certificates"][:3]
 actions=list(p024)+[p6["new_original_P6_full_high_output_action"],
         p8["complete_native_P8_original_high_output_action"],p10]
 assert [v["source"] for v in actions]==["P0","P2","P4","P6","P8","P10"]
 assert all(len(v["finite_original_D_action"])==2049 for v in actions)
 errors=[]
 columns=[]
 for d,act in zip(DEGREES,actions):
  origE=F(act["global_D_fault_norm_upper"])
  tailE=sqrt_up(F(act["model_D_energy_beyond_2048_upper"]))
  augrad=max(abs(lam/(H[d]+sl)-lam/(H[d]+sm)),
             abs(lam/(H[d]+sh)-lam/(H[d]+sm)))
  augE=sqrt_up(mass(d)*(H[d]+sh)*augrad*augrad)
  E=origE+tailE+augE
  assert E>0
  errors.append(E)
  columns.append(dict(input_degree=d,
   global_original_fault_D_norm_upper=str(origE),
   model_tail_D_norm_upper=str(tailE),
   physical_augmented_D_norm_upper=str(augE),
   full_D_action_error_upper=str(E),
   input_D_weight_lower=str(mass(d)*(H[d]+sl))))
 C6=sqrt_up(sum((errors[j]**2/(mass(d)*(H[d]+sl))
                 for j,d in enumerate(DEGREES)),F(0)))
 assert C6>0 and C6<F(1,2)

 def augmented_center(d,n):
  j=DEGREES.index(d)
  center=F(actions[j]["finite_original_D_action"][n]["coefficient"])
  return center+(lam/(H[d]+sm) if n==d else F(0))
 output=[]
 for n in range(2049):
  value=sum((a*augmented_center(d,n) for d,a in MIX.items()),F(0))
  output.append(dict(degree=n,coefficient=str(down(value))))
 assert all(row["coefficient"]=="0" for row in output if row["degree"]%2)
 # The direct RC303 signed polynomial formula, with independently
 # translated prime, regular and pole terms, must enclose our high
 # model's low-output linear combination.
 direct=prev["mixed_signed_even_polynomial_action"]["finite_original_D_action"]
 assert len(direct)==65
 for n in range(65):
  exact=sum((v*F(actions[DEGREES.index(d)]["finite_original_D_action"][n][
       "coefficient"]) for d,v in MIX.items()),F(0))
  r_basis=sum((abs(v)*F(
       get("303_direct_polynomial_prime")["new_native_P10_original_action"][
         "finite_original_D_action"][n]["radius"])
       for d,v in MIX.items() if d==10),F(0))
  # P4, P6 and P8 low stored radii are in RC240/296/299, not in
  # the high-output summaries. Retain an independently computed
  # aggregate interval by the RC303 direct source itself; do not
  # make equality claims between distinct rounded interval centers.
  assert output[n]["coefficient"]==str(down(exact+(
   sum((MIX[d]*lam/(H[d]+sm) for d in MIX if d==n),F(0)))))
  if n%2==0: assert direct[n]["radius"]!="0"
 mixed_error=sum((abs(MIX[d])*errors[DEGREES.index(d)] for d in MIX),F(0))
 mixed_D_input_sq=sum((mass(d)*(H[d]+sl)*a*a
                      for d,a in MIX.items()),F(0))
 assert mixed_error**2<=C6*C6*mixed_D_input_sq
 assert all(n["degree"]==i for i,n in enumerate(output))
 print("RC304: mixed signed polynomial output through 2048 and universal "
       "six-column paid action estimate complete",flush=True)
 return dict(
  milestone="RC304",
  parent_merge_commit="48c47228e88cfdbf66ec983e786b1df5005369a3",
  input_git_blob_pins=PINS,
  new_original_P10_action_through_2048=p10,
  all_P10_original_output_through_2048_materialized=True,
  P10_original_infinite_output_tail_paid=True,
  rank317_single_degree_P10_patch=p10patch,
  new_augmented_P10_original_global_D_fault_upper=str(augmented_fault),
  input_even_legendre_degrees_supported=list(DEGREES),
  six_input_action_uniform_D_relative_error_upper=str(C6),
  supported_input_column_full_D_error_budgets=columns,
  degree_independent_on_this_fixed_V6_span=True,
  input_degree_uniform_over_all_polynomials=False,
  direct_polynomial_mixed_original_low_regression_passed=True,
  direct_primes_for_mixed_high_outputs_independently_computed=False,
  mixed_polynomial_input={str(d):str(a) for d,a in MIX.items()},
  mixed_original_plus_augmented_high_action_output=output,
  mixed_complete_action_D_error_upper=str(mixed_error),
  mixed_physical_input_D_energy_lower=str(mixed_D_input_sq),
  mixed_all_original_infinite_tails_paid=True,
  full_operator_arbitrary_degree_action=False,
  repeated_Chebyshev_inverse_action_executed=False,
  true_inverse_response_certified=False,
  original_Weil_form_positivity_certified=False,
  remaining_314_principal_Schur_positive=False,
  Stage_I_closed=False,RH=False,F4=False,Lean=False,
  next_cursor="RC305: source-degree uniform prime/endpoint bounds beyond P10; "
  "the V6 linearity bound alone does not extend to the high-degree "
  "or infinite-input polynomial vectors produced by Chebyshev recursion."
 )
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 val=run(reverse=a.replay)
 if a.replay:
  assert val==json.loads(a.output.read_text(encoding="utf-8"))
 else:
  a.output.write_text(json.dumps(val,indent=2,sort_keys=True)+"\n",
                      encoding="utf-8")
 print("RC304 VALIDATED: P10 high action plus rank317 patch; "
       "mixed output to 2048; Stage I OPEN",flush=True)
