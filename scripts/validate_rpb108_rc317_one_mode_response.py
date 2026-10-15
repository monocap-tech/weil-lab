"""RC317: first NONZERO one-coordinate signed high-response trial.

For the ORIGINAL CC27 signed Weil D-Riesz representative N0 (RC313),
use RC315 P0 diagonal and RC316 P0--P244 signed cross to construct an
explicit nonzero high-complement response Y v0 = alpha v244, where
v_n = u_n/sqrt(H_n+s) and u_n are physical-L2 orthonormal Legendre.

The augmented RC292 positive reference provides an UPPER form bound
N0 <= nu I (not an absolute-norm bound). RC313 independently provides
||N0|| <= M. RC283/314 provide a positive even high complement floor
C>=mu_even I. Consequently

  alpha = b_lower/nu >0, b=<v244,N0 v0>,
  <v0-alpha*v244,N0(v0-alpha*v244)>
      <= B0 - b_lower^2/nu < B0.
  S00 = inf_y <v0-y,N0(v0-y)> <= that upper bound.

The full high residual R=T-CY is bounded, VERY COARSELY, by
||R v0|| <= M*(1+alpha). This is a rigorous full-D-norm bound,
NOT an evaluated residual Gram or a passed positivity Schur witness.
The 2x2 original signed principal block is positive even with
high coupling because mu_even*B0_lower > b_upper^2.

We do not certify full original signed positivity, Stage I, F4 or RH.
"""
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
GRID=10**30
OUT=10**20
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc292_signed_inverse_action_contract.json":"a4e19528ab5b12d9651a29dbeb478d7844e05470",
 "certificates/rpb108_rc313_prime_pole_distributions.json":"954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc314_fredholm_schur.json":"6496be8d20176f173c0ff8b6e393b0ccd7c6ff5b",
 "certificates/rpb108_rc315_low_mode_sign.json":"a8cd974c8218e18943dda0082f48cca36a3350a8",
 "certificates/rpb108_rc316_first_high_cross.json":"89f3ad09f2a63c0033c631c788dbe78c67e92e68",
}

def floor(x):return F(x.numerator*OUT//x.denominator,OUT)
def ceil(x):return F((x.numerator*OUT+x.denominator-1)//x.denominator,OUT)
def sqrt_bounds(x):
 assert x>0
 a=isqrt(x.numerator*GRID*GRID//x.denominator)
 low,hi=F(a,GRID),F(a+1,GRID)
 assert low*low<=x<=hi*hi
 return low,hi
def gitblob(raw):
 return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def run(reverse=False):
 inp={}
 for path,sha in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  assert gitblob(raw)==sha,("source pin changed",path)
  inp[path]=json.loads(raw)
 def src(s):return inp["certificates/rpb108_rc"+s+".json"]
 metric=src("129_four_vector_joint_moment")
 s_lower=F(metric["actual_D_Gram_entry_lower"][0][0])/(2*B)
 s_upper=F(metric["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert 3<s_lower<=s_upper<5
 n=244
 H=sum((F(1,k) for k in range(1,n+1)),F(0))
 assert H>6
 low=src("315_low_mode_sign")
 high=src("316_first_high_cross")
 assert low["normalized_low_block_positive_2_by_2"]
 assert high["rank317_high_mode_first_even_cross_nonzero"]
 assert high["original_CC27_signed_source"]
 signed=next(x for x in high["rigorous_high_crosses"]
             if x["first_omitted_even_degree"]==n)
 slo=F(signed["original_scaled_cross_lower"])
 shi=F(signed["original_scaled_cross_upper"])
 assert 0<slo<=shi<1
 # The original signed Q(u_n,u0), scaled by sqrt(2n+1),
 # converts into the D-normalized Riesz b exactly as follows:
 # b = signed / sqrt((2n+1)*s*(H_n+s)).
 Dlow=(2*n+1)*s_lower*(H+s_lower)
 Dhigh=(2*n+1)*s_upper*(H+s_upper)
 _,denhi=sqrt_bounds(Dhigh)
 denlo,_=sqrt_bounds(Dlow)
 b_lower=slo/denhi
 b_upper=shi/denlo
 assert 0<b_lower<=b_upper<F(1,100)
 p0=next(x for x in low["original_low_diagonals"] if x["n"]==0)
 phys0lo,phys0hi=map(F,p0["physically_normalized_original_Weil_diagonal_interval"])
 B_lower=phys0lo/s_upper
 B_upper=phys0hi/s_lower
 assert B_lower>0 and B_lower<=B_upper
 ref=src("314_fredholm_schur")
 matches=[x for x in ref["inherited_stronger_RC283_all_reference_choices"]
          if x["parity"]=="even" and x["reference_rank"]==122 and
             x["first_discarded_degree"]==244]
 assert len(matches)==1
 mu_even=F(matches[0]["high_complement_D_floor_lower"])
 mu_global=F(ref["buffered_rank317_high_complement_D_floor_lower"])
 assert 0<mu_global<=mu_even
 rc292=src("292_signed_inverse_action_contract")
 nu=F(rc292["global_even_reference_D_upper"])
 assert nu>0 and rc292["reference_rank"]==317
 assert not rc292["either_signed_projection_test_executed"]
 # Careful: N0 <= G_aug <= nu in the even sector; nu is
 # an upper FORM bound only, NOT ||N0||.
 M=F(src("313_prime_pole_distributions")[
  "improved_original_native_Weil_D_to_D_operator_norm_upper"])
 assert M>nu
 assert ref["rank301_feshbach_positivity_equivalent_to_full_positivity"]
 # Positive 2x2 principal even though signed low-high coupling is nonzero.
 # C_244,244 >= mu_even; determinant >= B_lower*mu_even-b_upper^2.
 det_lower=B_lower*mu_even-b_upper*b_upper
 assert det_lower>0
 # Choose an explicit nonzero trial response on the P0 column.
 # In the full high space this is Y v0 = alpha v244,
 # with alpha>=0 rational, no use of an unproved inverse.
 alpha=b_lower/nu
 assert alpha>0
 strict_gap=b_lower*b_lower/nu
 assert strict_gap>0 and strict_gap<B_lower
 trial_upper=B_upper-strict_gap
 # Projected residual at mode 244: b-alpha*a244,
 # with mu_even <= a244 <= nu. Use two-sided rational bounds.
 projected_R_lo=b_lower-alpha*nu
 projected_R_hi=b_upper-alpha*mu_even
 assert projected_R_lo>=0 and projected_R_hi>=projected_R_lo
 # Complete high residual in actual D Hilbert space:
 # ||T v0|| <= M and ||C Y v0|| <= M*alpha.
 # This is an explicit full, but extremely weak, error payment.
 residual_full_bound=M*(1+alpha)
 residual_gram_bound=residual_full_bound**2
 # RC314 rigorous lower Schur gate pays residual by mu_global;
 # this coarse bound does NOT pass it.
 residual_correction_upper=residual_gram_bound/mu_global
 assert residual_correction_upper>B_lower
 return dict(
  milestone="RC317",
  parent_route_head="eb58711cc46bb1df6d15d219cd5e033150a091de",
  input_git_blob_pins=PINS,
  object="Original CC27 signed Weil D-Riesz action, even P0 and P244",
  rank317_first_high_even_degree=n,
  original_signed_cross_is_strictly_positive=True,
  metric_s_lower=str(s_lower),
  metric_s_upper=str(s_upper),
  harmonic_H244_exact=str(H),
  original_normalized_cross_b_interval=[str(floor(b_lower)),str(ceil(b_upper))],
  original_normalized_P0_B_interval=[str(floor(B_lower)),str(ceil(B_upper))],
  high_even_floor_mu=str(mu_even),
  high_whole_rank317_floor_mu=str(mu_global),
  upper_even_form_bound_nu=str(nu),
  original_full_D_operator_absolute_norm_upper_M=str(M),
  two_by_two_original_signed_P0_P244_positive=True,
  two_by_two_determinant_lower=str(floor(det_lower)),
  one_column_high_response_Y_coeff_alpha=str(alpha),
  Y_is_nonzero_and_supported_only_at_high_degree_244=True,
  one_mode_trial_S00_upper=str(ceil(trial_upper)),
  strict_S00_reduction_below_original_B_lower=str(floor(strict_gap)),
  projected_signed_residual_mode_244_interval=[
   str(floor(projected_R_lo)),str(ceil(projected_R_hi))],
  full_D_residual_norm_upper=str(ceil(residual_full_bound)),
  full_D_residual_gram_upper=str(ceil(residual_gram_bound)),
  minus_sign_residual_correction_upper=str(ceil(residual_correction_upper)),
  full_residual_bound_is_coarse_global_norm_not_native_source_action=True,
  no_full_high_response_computed=True,
  original_rank317_Schur_positivity_certified=False,
  Stage_I_closed=False,F4=False,RH=False,Lean=False,
  next_cursor=(
   "RC318: replace coarse global ||T-CY|| bound with genuine "
   "source-action/Parseval tail and paid cross-correlation residual "
   "for multiple high modes. The rank-317 full Schur lower test "
   "remains open. Do not infer positivity from a small positive "
   "two-mode principal block or the strict upper Schur contraction."
  ),
 )
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 result=run(reverse=a.replay)
 if a.replay:assert result==json.loads(a.output.read_text(encoding="utf-8"))
 else:a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
 print("RC317: nonzero one-mode signed high trial; full residual paid coarsely. Schur positivity and Stage I OPEN",flush=True)
