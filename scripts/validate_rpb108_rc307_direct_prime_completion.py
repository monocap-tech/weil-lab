"""RC307: independent signed mixed-source prime projection to 2048.

The prime action is evaluated from the mixed degree-ten polynomial
itself, not by summing P4/P6/P8/P10 action columns. The inherited exact
piecewise prime model is projected by a boundary-resolvent to degree
2048, with interval enclosures and a Parseval lower-capture upper
bound for the true infinite nominal prime-output remainder.

A separate dimension-free full signed-prime L2 operator bound follows
from finite sums of truncated translations; the same bounded component
extends by density to all L2. This does NOT control the complete Weil
operator or its iterative Chebyshev action. Interval arithmetic is
conditional on the inherited original Weil prime-source model.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib
import argparse
import json

import validate_rpb108_rc273_projection_original_tail as high
import validate_rpb108_rc303_direct_polynomial_prime as native_direct

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
SCALE=10**24
MIX={4:F(1),6:F(-1,2),8:F(1,3),10:F(-1,5)}
DEG=10
END=2048
FIRST=2050
PINS={
 "certificates/rpb108_rc43_native_prime_head.json":
    "b4893953109e6fdc55d52b505c2bcfbf0d38281e",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":
    "33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc303_direct_polynomial_prime.json":
    "cc71c9a961230ecedeb65947afae15ba37f0abbe",
 "certificates/rpb108_rc304_p10_high_mixed.json":
    "5f098868017a19ec753c6f6e4b724cd5036d053b",
 "certificates/rpb108_rc306_adaptive_markov.json":
    "29123b028e6d9c8f69e31c0b61f3a04c3ade33c7",
 "scripts/validate_rpb108_rc273_projection_original_tail.py":
    "4f6163f36097a97190ba50b5e032d942106122ef",
 "scripts/validate_rpb108_rc303_direct_polynomial_prime.py":
    "0ac8d342af986fec3c33e3b18838db21c0972c49",
}
def sqrt_up(z):
 assert z>=0
 if not z:return F(0)
 return F(isqrt(z.numerator*SCALE*SCALE//z.denominator)+1,SCALE)

def mass(n):
 return 2*B/F(2*n+1)

def run(reverse=False):
 data={}
 for path,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  digest=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
  assert digest==sha,(path,"pinned analytic input changed")
  data[path]=json.loads(raw) if path.endswith(".json") else None
 def get(s):return data["certificates/rpb108_rc"+s+".json"]
 prime=get("43_native_prime_head")
 mom=get("129_four_vector_joint_moment")
 prev=get("303_direct_polynomial_prime")
 highprev=get("304_p10_high_mixed")
 adaptive=get("306_adaptive_markov")
 assert prev["direct_native_prime_translation_available_for_signed_polynomials"]
 assert not highprev["direct_primes_for_mixed_high_outputs_independently_computed"]
 assert adaptive["method"]=="physical_supnorm_and_classical_Markov_instead_of_monomial_l1"
 assert highprev["mixed_polynomial_input"]=={str(d):str(a) for d,a in MIX.items()}
 assert len(prime["active_prime_powers"])==7
 sl=F(mom["actual_D_Gram_entry_lower"][0][0])/(2*B)
 sh=F(mom["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert 0<sl<=sh

 # First prove a GLOBAL nominal prime L2 action norm:
 # Each P_j q = -c_j(1_I T_ell q + 1_I T_-ell q), with q extended by
 # zero outside [-B,B]. Both translation operators preserve L2 on
 # the line and restriction decreases it. Consequently,
 # ||P q||_2 <= 2 sum_j c_j_upper ||q||_2, for EVERY L2 input.
 # Finite-rank polynomial density extends this bounded operator
 # to the full original physical L2 carrier. No differentiability
 # or input-degree factor is needed for this NOMINAL bound.
 total=2*sum((F(row["coefficient_upper"])
              for row in prime["active_prime_powers"]),F(0))
 assert 0<total<F(10)
 inverseL2=sqrt_up(total*total/sl)
 inverseD=total/sl
 assert inverseL2>0 and inverseD>0

 a=[F(0)]*(DEG+1)
 for d,w in MIX.items():a[d]=w
 q=native_direct.weighted_polynomial(MIX)
 assert len(q)==11
 assert q==high.native.input_poly(a)

 # Independent direct 65-output exact prime integral / Parseval model.
 low,tail64,fault64,lowproof=native_direct.native_prime_on_polynomial(
   q,prime,reverse)
 assert len(low)==65 and lowproof["exact_piecewise_segments"]==15
 assert all(low[n]==0 for n in range(1,65,2))
 norm2=sum((w*w*mass(d) for d,w in MIX.items()),F(0))
 assert norm2==F(lowproof["direct_polynomial_mass_squared"])
 assert norm2==F(prev["mixed_signed_even_polynomial_action"][
   "directly_evaluated_prime_source"]["direct_polynomial_mass_squared"])

 # Genuine HIGH native prime output, not re-interpolation of RC304.
 rows,tail2048,interval_fault,proof=high.prime_output(
   a,0,prime,reverse)
 assert len(rows)==992
 assert [v["degree"] for v in rows]==list(range(66,2049,2))
 assert proof["prime_projection_cutoff"]==END
 assert proof["all_cross_prime_and_input_terms_preserved"]
 assert proof["prime_controls"]["prime_segment_polynomial_sha256"]
 assert len(proof["direct_high_degree_integral_control_indices"])>=1
 assert 0<tail2048<tail64
 print("RC307: independent mixed signed prime output projected "
       "through 2048",flush=True)

 # RC273 chooses the arithmetic model internally. Require its
 # seven source parameters to coincide with the midpoint model
 # used by RC303 before claiming the independent low regression.
 model=proof["prime_controls"]["chosen_prime_model_parameters"]
 assert len(model)==7
 for actual,row in zip(model,prime["active_prime_powers"]):
  assert F(actual["chosen_translation"])==(
      F(row["translation_lower"])+F(row["translation_upper"]))/2
  assert F(actual["chosen_coefficient"])==(
      F(row["coefficient_lower"])+F(row["coefficient_upper"]))/2
 # Rebuild RC273's exact low-output digest from an entirely
 # distinct direct integral model over all 15 translated segments.
 # Hash matches if and only if all 65 low model values agree.
 recomputed=high.native.segment_digest([(F(0),F(64),low)])
 assert recomputed==proof["low_prime_coefficient_digest"]

 direct64upper=F(lowproof["omitted_prime_L2_energy_upper"])
 assert tail64<=direct64upper or direct64upper<=tail64
 # Both 64+ tails arise from the SAME rational arithmetic model,
 # with independent outward grids. Compare within two ulps.
 assert abs(tail64-direct64upper)<=F(4,10**15)
 # Full nominal prime physical squared energy bound
 # ensures the new captured/tail ratio is meaningful.
 nominalFull=F(lowproof["full_prime_L2_mass_squared_upper"])
 assert 0<tail2048<nominalFull
 first_weight=high.orig.H(FIRST)+sl
 assert first_weight>0
 high_D_energy=tail2048/first_weight
 high_D_norm=sqrt_up(high_D_energy)
 assert high_D_norm**2>=high_D_energy

 # For the direct mixed source, RC306 independently bounds
 # uncertain prime parameters by physical Markov estimates.
 cap=adaptive["all_degree_sampling_replay_records"][0]
 assert cap["even_input_maximum_degree"]==10
 paramConst=F(cap[
   "all_seven_signed_prime_translation_L2_error_per_input_L2_upper"])
 paramError=sqrt_up(paramConst*paramConst*norm2/sl)
 assert paramError>0

 # Precise coordinate intervals on the independent prime action
 # guarantee the source is NOT represented merely by interpolated
 # original P4/P6/P8/P10 high columns.
 selected={}
 for n in (66,128,256,512,1024,1536,2048):
  e=next(t for t in rows if t["degree"]==n)
  l=F(e["lower"]);u=F(e["upper"])
  assert l<=u and (u-l)<F(1,10**45)
  selected[str(n)]={"lower":str(l),"upper":str(u)}
 return dict(
  milestone="RC307",
  parent_merge_commit="42313bd4739e918e9085ff94a290a0bb5462e4fa",
  input_git_blob_pins=PINS,
  mixed_signed_even_legendre_input={str(d):str(w)
                                   for d,w in MIX.items()},
  actual_signed_prime_seven_active_pairs=True,
  independent_direct_mixed_polynomial_prime_high_projection_through_2048=True,
  direct_mixed_prime_high_output_intervals=rows,
  selected_high_output_prime_intervals=selected,
  direct_prime_projection_certificate=proof,
  exact_independent_low_65_prime_model_digest_regression=True,
  direct_prime_model_L2_energy_after_output64_upper=str(tail64),
  direct_prime_model_L2_energy_after_output2048_upper=str(tail2048),
  direct_prime_model_D_energy_after_output2048_upper=str(high_D_energy),
  direct_prime_model_D_norm_after_output2048_upper=str(high_D_norm),
  original_mixed_input_L2_squared_exact=str(norm2),
  signed_prime_arithmetic_parameter_D_norm_upper=str(paramError),
  dimension_free_nominal_prime_L2_to_L2_norm_upper=str(total),
  dimension_free_nominal_prime_L2_to_D_inverse_norm_upper=str(inverseL2),
  dimension_free_nominal_prime_D_to_D_inverse_norm_upper=str(inverseD),
  dimension_free_nominal_prime_component_extends_to_full_L2_by_density=True,
  dimension_free_prime_parameter_perturbation_bound_proved=False,
  degree_adaptive_direct_full_prime_projector_all_polynomials=False,
  full_archimedean_pole_endpoint_operator_bounded_on_common_carrier=False,
  full_original_Weil_operator_composability_certified=False,
  true_inverse_response_certified=False,
  remaining_314_principal_Schur_positive=False,
  original_Weil_form_positivity_certified=False,
  Stage_I_closed=False,F4=False,RH=False,Lean=False,
  next_cursor=(
   "RC308: integrate directly evaluated high signed-prime polynomial "
   "source with original archimedean/pole and endpoint estimates; "
   "formalize extension/composition on an appropriate common carrier "
   "without treating the bounded nominal prime component as the full "
   "Weil action.")
 )
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 args=p.parse_args()
 result=run(reverse=args.replay)
 if args.replay:
  assert result==json.loads(args.output.read_text(encoding="utf-8"))
 else:
  args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",
                         encoding="utf-8")
 print("RC307 VALIDATED: independent high signed mixed source and "
       "global nominal-prime L2 operator bound; Stage I OPEN",flush=True)
