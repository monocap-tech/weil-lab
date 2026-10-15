"""RC314: finite Morse index and exact residual-corrected Schur positivity gate.

The original CC27 signed form is identified with a bounded selfadjoint
D-Riesz representative in RC313. Write in the D-normalized physical
Legendre basis

 N0 = I + D^-1/2 h D^-1/2
           + D^-1/2 (P-R+Pole-r I) D^-1/2,
 h(t) = -1/2 log(1-t^2) >= 0, r=789/125.

D_n=H_n+s tends to infinity; D^-1/2 is compact. The second,
sign-indefinite term is therefore compact. The first term is bounded
and nonnegative via RC309. Weyl's theorem implies the ESSENTIAL
spectrum lies in [1,infinity), though finitely many negative/null
eigenvalues can remain. RC283's independent parity-specific
coercive high complements bound their total dimension by 301.

A new rank301 exact Feshbach/Schur test is derived:
 for N=[[B,T*],[T,C]], C>=mu I on high complement,
 any approximate Y and residual R=T-CY,
 S=B-T*Y-Y*T+Y*CY-R*C^-1 R
   >= B-T*Y-Y*T+Y*CY - R*R/mu.
N positive iff S positive. This is a conditional test, not
a computed signed inverse or positivity certificate.

Independently, the sharpened RC313 prime bound and sign-specific
pole norm produce a coarser, *standalone* explicit finite-index
bound (usually worse than RC283), illustrating where the true
remaining difficulty lives without importing the stronger lambda.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import argparse,hashlib,json

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
GRID=10**30
r=F(789,125)
PINS={
 "certificates/rpb108_rc121_diagonal_metric_equivalence.json":
 "089664ca7eb9139fec1ba0f58b4cfbf25902f51a",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":
 "33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc283_reduced_reference.json":
 "1dc4bba375af6bfd7a274fccc07638e0eead56e6",
 "certificates/rpb108_rc292_signed_inverse_action_contract.json":
 "a4e19528ab5b12d9651a29dbeb478d7844e05470",
 "certificates/rpb108_rc308_bounded_arch_pole.json":
 "2461485678ec998ed7449e8a6141a3b71e083f35",
 "certificates/rpb108_rc309_endpoint_schur.json":
 "d3f11a563486c7adb9128252092820ad7f1ef189",
 "certificates/rpb108_rc311_endpoint_core_identity.json":
 "f32be168d91a100c96710c484677648a54b3799d",
 "certificates/rpb108_rc313_prime_pole_distributions.json":
 "954b4892cf3b4e999e65476d7ce341021528d9e8",
}

def up(x):
 assert x>=0
 return F((x.numerator*GRID+x.denominator-1)//x.denominator,GRID)
def down(x):
 assert x>=0
 return F(x.numerator*GRID//x.denominator,GRID)
def M(x,y):
 return [[sum(x[i][k]*y[k][j] for k in range(len(y)))
          for j in range(len(y[0]))] for i in range(len(x))]
def add(x,y,sign=1):
 return [[x[i][j]+sign*y[i][j] for j in range(len(x[0]))]
         for i in range(len(x))]
def tr(x):return [list(a) for a in zip(*x)]
def inv2(x):
 a,b=x[0]; c,d=x[1]; den=a*d-b*c
 assert den>0
 return [[d/den,-b/den],[-c/den,a/den]]
def psd2(x,strict=False):
 assert x[0][1]==x[1][0]
 if strict:return x[0][0]>0 and x[0][0]*x[1][1]-x[0][1]**2>0
 return x[0][0]>=0 and x[1][1]>=0 and x[0][0]*x[1][1]-x[0][1]**2>=0

def feshbach_regression():
 # All blocks are exact rational and genuinely non-diagonal.
 C=[[F(3),F(1,4)],[F(1,4),F(5,2)]]
 mu=F(2)
 assert psd2(add(C,[[mu,F(0)],[F(0),mu]],-1),strict=True)
 BB=[[F(2),F(1,5)],[F(1,5),F(2)]]
 T=[[F(1,3),F(-1,5)],[F(1,4),F(1,6)]]
 Y=[[F(1,10),F(0)],[F(0),F(1,11)]]
 residual=add(T,M(C,Y),-1)
 # S_true = B-T* C^-1 T
 true=add(BB,M(M(tr(T),inv2(C)),T),-1)
 # S_trial = B-T*Y-Y*T+Y*CY
 trial=add(add(add(BB,M(tr(T),Y),-1),
               M(tr(Y),T),-1),
           M(M(tr(Y),C),Y))
 correction=M(M(tr(residual),inv2(C)),residual)
 assert true==add(trial,correction,-1)
 paid=M(tr(residual),residual)
 paid=[[v/mu for v in row] for row in paid]
 assert psd2(add(paid,correction,-1))
 lower=add(trial,paid,-1)
 assert psd2(add(true,lower,-1))
 assert psd2(true,strict=True) and psd2(lower,strict=True)
 # Choosing Y=0 preserves exact correction and catches a common
 # incorrect PLUS-sign residual Schur correction.
 zero=[[F(0)]*2 for _ in range(2)]
 wrong=add(BB,M(M(tr(T),inv2(C)),T),+1)
 assert wrong!=true
 assert add(trial,correction,-1)==true
 return dict(
  positive_high_block_C=[[str(v) for v in row] for row in C],
  block_floor_mu=str(mu),
  nonzero_residual=[[str(v) for v in row] for row in residual],
  exact_schur=[[str(v) for v in row] for row in true],
  paid_lower_schur=[[str(v) for v in row] for row in lower],
  exact_residual_correction_is_SUBTRACTED=True,
  exact_nontrivial_rational_Loewner_identity=True,
  residual_bound_by_mu_strictly_valid=True,
  sufficient_lower_schur_SPD_in_example=True)

def standalone_bounds(sl,arch,prime):
 Cp=F(prime["original_prime_finite_chain_L2_norm_upper"])
 Cr=F(arch["regular_original_physical_L2_operator_norm_upper"])
 sinhB=F(arch["certified_sinh_B_upper"])
 assert sinhB>B
 oddpole=2*(sinhB-B)
 even_lambda=r+Cp+Cr
 odd_lambda=even_lambda+oddpole
 assert F(11)<even_lambda<odd_lambda<F(13)
 # Harmonic rational GRIDS avoid 2500-degree unreduced denominators.
 # Low/upper are truly outward because each 1/k is separately paid.
 Hlo=F(0); Hhi=F(0); found={}
 for k in range(1,10001):
  t=F(1,k)
  Hlo+=down(t)
  Hhi+=up(t)
  parity="even" if k%2==0 else "odd"
  lam=even_lambda if parity=="even" else odd_lambda
  if parity not in found and Hlo+sl>lam:
   rank=(k+1)//2 if parity=="odd" else k//2
   assert Hlo+sl>lam and Hhi>=Hlo
   found[parity]=dict(
    first_strict_high_degree=k,low_parity_dimension=rank,
    actual_harmonic_H_N_lower=str(Hlo),
    actual_harmonic_H_N_upper=str(Hhi),
    sign_aware_physical_lower_perturbation_lambda=str(lam),
    certified_high_complement_D_coercivity_floor_lower=str(
      down(1-lam/(Hlo+sl))))
  if len(found)==2:break
 assert len(found)==2
 assert found["even"]["first_strict_high_degree"]%2==0
 assert found["odd"]["first_strict_high_degree"]%2==1
 return found,dict(
  seven_prime_nominal_physical_L2_upper=str(Cp),
  regular_convolution_physical_L2_upper=str(Cr),
  even_positive_pole_ignored_in_lower_bound=True,
  odd_signed_negative_pole_L2_upper=str(oddpole),
  even_lower_negative_perturbation_upper=str(even_lambda),
  odd_lower_negative_perturbation_upper=str(odd_lambda))

def run(reverse=False):
 data={}
 for path,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  got=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
  assert got==sha,(path,"pinned source mutated")
  data[path]=json.loads(raw)
 def get(s):return data["certificates/rpb108_rc"+s+".json"]
 can=get("313_prime_pole_distributions")
 assert can["original_CC27_Weil_polynomial_form_matches_native_model_on_all_degrees"]
 assert can["original_CC27_Weil_bounded_D_Riesz_extension_unique_under_RC121_equivalence"]
 assert not can["positive_spectral_lower_bound_proved"]
 epi=get("311_endpoint_core_identity")
 assert epi["W_B_minus_log2_equals_actual_original_endpoint_h"]
 assert epi["all_degree_native_E_multiplication_by_W_B_identified"]
 sch=get("309_endpoint_schur")
 assert F(sch["full_endpoint_D_inverse_D_to_D_norm_upper"])>0
 rc121=get("121_diagonal_metric_equivalence")
 assert rc121["positive_diagonal_reference"]==(
   "D P_n = (H_n+c_R+log(2)+789/125) P_n")
 ref=get("283_reduced_reference")
 assert ref["proposed_buffered_reference_rank"]==317
 assert ref["minimal_positive_reference_rank"]==301
 rc292=get("292_signed_inverse_action_contract")
 assert not rc292["either_signed_projection_test_executed"]
 actual=get("129_four_vector_joint_moment")
 sl=F(actual["actual_D_Gram_entry_lower"][0][0])/(2*B)
 sh=F(actual["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert F(3)<sl<=sh<F(5)
 arch=get("308_bounded_arch_pole")

 # Compactness: D^-1/2 is compact on physical orthonormal Legendre
 # coordinates because its n-th diagonal tends to zero as H_n→∞.
 # Q=D^-1/2 h D^-1/2 >=0 is bounded by RC309/311; the
 # indefinite part K=D^-1/2(P-R+Pole-rI)D^-1/2 is compact.
 # Weyl => sigma_essential(N0=I+Q+K) subset [1,infinity).
 # This says NOTHING about finite negative or zero eigenvalues.
 rough,terms=standalone_bounds(sl,arch,can)

 choices=[]
 for j,info in enumerate(ref["reduced_reference_options"]):
  parity=info["parity"];first=0 if parity=="even" else 1
  assert j==first
  lam=F(info["parameter_lambda"])
  for option in info["reduced_reference_options"]:
   m=option["first_discarded_matching_degree"]
   rank=option["new_low_reference_rank"]
   floor=F(option["certified_D_reference_floor_lower"])
   assert m==2*rank+j
   assert floor>0
   Hm=sum((F(1,k) for k in range(1,m+1)),F(0))
   exact=1-lam/(Hm+sl)
   assert exact>=floor>0
   choices.append(dict(
    parity=parity,reference_rank=rank,
    first_discarded_degree=m,
    high_complement_D_floor_lower=str(floor),
    exact_reference_high_lower_coercivity_value=str(exact),
    parity_minimal_choice=option["protected_high_mass_floor_target"]=="0"))
 choices.sort(key=lambda x:(x["parity"],x["reference_rank"]))
 even=next(x for x in choices if x["parity"]=="even" and x["parity_minimal_choice"])
 odd=next(x for x in choices if x["parity"]=="odd" and x["parity_minimal_choice"])
 rank=even["reference_rank"]+odd["reference_rank"]
 assert rank==301 and even["first_discarded_degree"]==232
 assert odd["first_discarded_degree"]==371
 mu=min(F(even["high_complement_D_floor_lower"]),
        F(odd["high_complement_D_floor_lower"]))
 assert mu>0
 rank317even=next(x for x in choices if x["parity"]=="even" and x["reference_rank"]==122)
 rank317odd=next(x for x in choices if x["parity"]=="odd" and x["reference_rank"]==195)
 mu317=min(F(rank317even["high_complement_D_floor_lower"]),
           F(rank317odd["high_complement_D_floor_lower"]))
 assert mu317>mu
 assert rank < rank317even["reference_rank"]+rank317odd["reference_rank"]
 assert mu317/mu>F(10)

 # Cross-rest residual corrector:
 # Schur_{301}= B-T*Y-Y*T+Y*CY-R*C^-1R,
 # R=T-CY, C>=mu I. Hence a positive finite lower witness
 # B-T*Y-Y*T+Y*CY -R*R/mu is SUFFICIENT for full positivity,
 # and not assumed to be realized by existing RC280 trials.
 toy=feshbach_regression()
 assert toy["exact_residual_correction_is_SUBTRACTED"]

 oldupper=F(rc292["global_even_reference_D_upper"])
 newupper=F(can["original_augmented_model_D_to_D_norm_upper"])
 # New RC313 crude all-component upper bound is worse than
 # the sharper inherited RC292 upper. Do not overwrite it.
 assert newupper>oldupper
 assert rough["even"]["low_parity_dimension"]+rough["odd"]["low_parity_dimension"]>301
 return dict(
  milestone="RC314",
  parent_merge_commit="f89fef4ae8a53c37015d9efc0ecc8ad5a05cd643",
  pinned_source_git_blobs=PINS,
  complete_original_CC27_D_Riesz_identification_imported_from_RC313=True,
  operator_selfadjoint_in_physical_D_energy=True,
  identity_plus_positive_endpoint_plus_compact_signed_perturbation=True,
  positive_endpoint_piece="D^-1/2 h D^-1/2 with h=-1/2 log(1-t²)>=0",
  indefinite_compact_piece="D^-1/2 (Prime-Regular+Pole-789/125 I) D^-1/2",
  compactness_reason="D_n=H_n+s diverges, so D^-1/2 compact on physical L2",
  Weyl_essential_spectrum_lower_ge_one=True,
  original_operator_is_selfadjoint_Fredholm_index_zero=True,
  nonpositive_spectral_subspace_is_finite_dimensional=True,
  independent_sign_aware_original_lower_bound_components=terms,
  independent_sign_aware_crude_low_reference=rough,
  inherited_stronger_RC283_all_reference_choices=choices,
  original_nonpositive_Morse_index_upper=rank,
  original_nonpositive_multiplicity_upper_even=even["reference_rank"],
  original_nonpositive_multiplicity_upper_odd=odd["reference_rank"],
  rank301_high_complement_positive_in_both_parities=True,
  selected_rank301_high_complement_D_floor_lower=str(mu),
  buffered_rank317_high_complement_D_floor_lower=str(mu317),
  buffered_rank317_has_stronger_reference_conditioning=True,
  exact_feshbach_conditional_contract=(
   "N=[[B,T*],[T,C]], C>=mu I, R=T-CY; "
   "Schur=B-T*Y-Y*T+Y*CY-R*C^-1R "
   ">=B-T*Y-Y*T+Y*CY-R*R/mu"),
  rank301_feshbach_positivity_equivalent_to_full_positivity=True,
  rank301_signed_residual_positivity_sufficient_condition=True,
  exact_feshbach_residual_sign_regression=toy,
  rank301_approximate_Schur_blocks_actually_evaluated=False,
  RC292_preexisting_tighter_reference_upper=str(oldupper),
  RC313_augmented_model_operator_upper=str(newupper),
  new_RC313_crude_operator_upper_DID_NOT_improve_RC292_reference_upper=True,
  positive_spectral_lower_bound_certified=False,
  full_301_or_317_Schur_principal_positive=False,
  signed_inverse_response_certified=False,
  Stage_I_closed=False,F4=False,RH=False,Lean=False,
  next_cursor=(
    "RC315: compute a NEW SIGNED high-complement response Y and "
    "its rigorously paid full D residual for the rank301 or better "
    "conditioned rank317 Feshbach block; insert into the MINUS-sign "
    "Schur certificate. The compactness/Fredholm theorem locates "
    "all possible nonpositive spectrum but does NOT prove it absent.")
 )
if __name__=="__main__":
 ap=argparse.ArgumentParser()
 ap.add_argument("--output",type=Path,required=True)
 ap.add_argument("--replay",action="store_true")
 a=ap.parse_args()
 v=run(reverse=a.replay)
 if a.replay:assert v==json.loads(a.output.read_text(encoding="utf-8"))
 else:a.output.write_text(json.dumps(v,sort_keys=True,indent=2)+"\n",encoding="utf-8")
 print("RC314 VALIDATED: full signed operator Fredholm, nonpositive "
       "index<=301, exact residual-corrected rank301 Schur contract; "
       "positivity and Stage I OPEN",flush=True)
