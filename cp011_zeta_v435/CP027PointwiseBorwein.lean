module

public import Zeta.EulerMaclaurin.ErrorBound
public import Mathlib.RingTheory.Polynomial.Pochhammer
public import Mathlib.NumberTheory.Bernoulli
public import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
CP027 ORIGINAL CENTER-ONLY BORWEIN GATE.

There is no CP019 Cauchy, no CP020 13-circle, no CP021 original
locally-uncompiled lean_lib, no CP026 point-bridge import here.
Only real original published Zeta@c06b4e + Mathlib4@v4.35.

For BOTH actual rational original source heights
150.05352 and 150.05353, establish the ORIGINAL
zetaRemainderBound (1/2+i*t) 6 256 <= 3/10^13.

New, sharper center-only prefactor K <= 328/27 (instead
of moving-circle 656/53). Coefficient B14=7/6, original
Pochhammer and complex-power bounds. No Cauchy premise,
no derivative and no new assumption.

These theorems are uncompiled LEAN SOURCE CANDIDATES;
the original v4.35 actual .olean and strict standard-only
#print axioms must be obtained before calling any LEAN PASS.
-/

@[expose] public section

open Finset Set

namespace CP027PointwiseBorwein

abbrev left : ℝ := (15005352 : ℝ) / 100000
abbrev right : ℝ := (15005353 : ℝ) / 100000
noncomputable def center (t : ℝ) : ℂ := (1 / 2 : ℂ) + Complex.I * (t : ℂ)
private abbrev cap : ℝ := (3 : ℝ) / (10 : ℝ) ^ 13

/-- Original source polynomial (s)_n has at most the
product of n scalar factors when ‖s‖ ≤ 151. -/
theorem original_ascending_pochhammer_norm
    (z : ℂ) (hnorm : ‖z‖ ≤ (151 : ℝ)) (n : ℕ) :
    ‖(ascPochhammer ℂ n).eval z‖ ≤
      ∏ j ∈ Finset.range n, ((151 : ℝ) + j) := by
  induction n with
  | zero => simp [ascPochhammer_zero]
  | succ n ih =>
      rw [ascPochhammer_succ_eval, norm_mul, Finset.prod_range_succ]
      have hs : ‖z + (n : ℂ)‖ ≤ (151 : ℝ) + n := by
        calc
          ‖z + (n : ℂ)‖ ≤ ‖z‖ + ‖(n : ℂ)‖ := norm_add_le _ _
          _ = ‖z‖ + (n : ℝ) := by simp
          _ ≤ 151 + n := by linarith
      exact mul_le_mul ih hs (norm_nonneg _) (by positivity)

/-- Original rational B14, recomputed from Mathlib's TRUE
Bernoulli recursion; never injected as an axiom. -/
theorem original_B14 : bernoulli 14 = (7 : ℚ) / 6 := by
  norm_num [bernoulli, bernoulli', Fin.sum_univ_eq_sum_range,
    Finset.sum_range_succ]

theorem original_B14_norm :
    ‖(((bernoulli 14 : ℝ) / ((14 : ℕ).factorial : ℝ)) : ℂ)‖
      = (7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ)) := by
  rw [original_B14]
  norm_num [Complex.norm_real, Real.norm_eq_abs, Nat.factorial]

/-- The two source centers are easier than an entire complex
Cauchy circle: Re(s_t)=1/2 and ‖s_t‖≤151. -/
theorem center_geometry (t : ℝ) (ht : t ∈ Icc left right) :
    (center t).re = (1 : ℝ) / 2 ∧ ‖center t‖ ≤ 151 := by
  have ht0 : (0 : ℝ) ≤ t := by
    have ha : (0 : ℝ) ≤ left := by norm_num [left]
    exact ha.trans ht.1
  have hnorm : ‖center t‖ ≤ (1 : ℝ) / 2 + t := by
    calc
      ‖center t‖ =
          ‖(1 / 2 : ℂ) + Complex.I * (t : ℂ)‖ := rfl
      _ ≤ ‖(1 / 2 : ℂ)‖ + ‖Complex.I * (t : ℂ)‖ :=
        norm_add_le _ _
      _ = (1 : ℝ) / 2 + t := by
        simp [norm_mul, abs_of_nonneg ht0]
  constructor
  · simp [center]
  · have hb : t ≤ right := ht.2
    dsimp [right] at hb
    linarith

/-- A sharper original Borwein prefactor for the TRUE
critical-line centers: ‖s+13‖/(Re(s)+13) ≤328/27. -/
theorem center_prefactor (z : ℂ)
    (hre : z.re = (1 : ℝ) / 2) (hn : ‖z‖ ≤ 151) :
    ‖z + (13 : ℂ)‖ / (z.re + 13) ≤ (328 : ℝ) / 27 := by
  have hup : ‖z + (13 : ℂ)‖ ≤ (164 : ℝ) := by
    calc
      ‖z + (13 : ℂ)‖ ≤ ‖z‖ + ‖(13 : ℂ)‖ := norm_add_le _ _
      _ = ‖z‖ + 13 := by simp
      _ ≤ 164 := by linarith
  rw [hre]
  apply (div_le_iff₀ (by norm_num : (0 : ℝ) < 1 / 2 + 13)).2
  nlinarith

theorem original_cpow_norm (z : ℂ) (hre : z.re = (1 : ℝ) / 2) :
    ‖(256 : ℂ) ^ (-z - (13 : ℂ))‖ ≤
      1 / (256 : ℝ) ^ 13 := by
  rw [Complex.norm_cpow_eq_rpow_re_of_pos (by norm_num :
    (0 : ℝ) < 256)]
  have hs : (-z - (13 : ℂ)).re ≤ -(13 : ℝ) := by
    simp only [Complex.sub_re, Complex.neg_re, Complex.natCast_re]
    linarith
  calc
    (256 : ℝ) ^ (-z - (13 : ℂ)).re ≤
        (256 : ℝ) ^ (-(13 : ℝ)) :=
      Real.rpow_le_rpow_of_exponent_le (by norm_num) hs
    _ = 1 / (256 : ℝ) ^ 13 := by
      norm_num [Real.rpow_neg (by norm_num : (0 : ℝ) ≤ 256),
        Real.rpow_natCast]

theorem original_omitted_term (z : ℂ)
    (hre : z.re = (1 : ℝ) / 2) (hn : ‖z‖ ≤ 151) :
    ‖(((bernoulli 14 : ℝ) / ((14 : ℕ).factorial : ℝ)) : ℂ) *
      (ascPochhammer ℂ 13).eval z *
      (256 : ℂ) ^ (-z - (13 : ℂ))‖ ≤
      ((7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ))) *
        (∏ j ∈ Finset.range 13, ((151 : ℝ) + j)) /
        (256 : ℝ) ^ 13 := by
  have hcoef := original_B14_norm
  have hpoly := original_ascending_pochhammer_norm z hn 13
  have hpow := original_cpow_norm z hre
  calc
    ‖(((bernoulli 14 : ℝ) / ((14 : ℕ).factorial : ℝ)) : ℂ) *
      (ascPochhammer ℂ 13).eval z *
      (256 : ℂ) ^ (-z - (13 : ℂ))‖ =
      ((7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ))) *
        ‖(ascPochhammer ℂ 13).eval z‖ *
        ‖(256 : ℂ) ^ (-z - (13 : ℂ))‖ := by
          rw [norm_mul, norm_mul, hcoef]
    _ ≤ ((7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ))) *
        (∏ j ∈ Finset.range 13, ((151 : ℝ) + j)) *
        (1 / (256 : ℝ) ^ 13) := by
          gcongr <;> assumption
    _ = ((7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ))) *
        (∏ j ∈ Finset.range 13, ((151 : ℝ) + j)) /
        (256 : ℝ) ^ 13 := by ring

/-- The exact 13-factor RATIONAL cap at the critical-line center:
(328/27)*(7/(6*14!))*∏(151+j)/256^13
=1069402300239520471/3802951800684688204490109616128
< 3e-13. This is independently verified in Fraction arithmetic. -/
theorem exact_center_majorant :
    ((328 : ℝ) / 27) *
      (((7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ))) *
        (∏ j ∈ Finset.range 13, ((151 : ℝ) + j)) /
        (256 : ℝ) ^ 13) < cap := by
  norm_num [cap, Finset.prod_range_succ, Nat.factorial]

/-- UNCONDITIONAL SOURCE CANDIDATE of actual original Borwein
error-bound function at EVERY center in the narrow root interval,
using ONLY the point geometry, NOT a complex Cauchy circle. -/
theorem original_center_Borwein (t : ℝ) (ht : t ∈ Icc left right) :
    zetaRemainderBound (center t) 6 256 ≤ cap := by
  obtain ⟨hre, hn⟩ := center_geometry t ht
  have hK := center_prefactor (center t) hre hn
  have hT := original_omitted_term (center t) hre hn
  have hK0 : 0 ≤ ‖center t + (13 : ℂ)‖ /
      ((center t).re + 13) := by positivity
  have hprod : (0 : ℝ) ≤
      ((7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ))) *
        (∏ j ∈ Finset.range 13, ((151 : ℝ) + j)) /
        (256 : ℝ) ^ 13 := by positivity
  have hSource :
      zetaRemainderBound (center t) 6 256 =
      (‖center t + (13 : ℂ)‖ / ((center t).re + 13)) *
      ‖(((bernoulli 14 : ℝ) / ((14 : ℕ).factorial : ℝ)) : ℂ) *
        (ascPochhammer ℂ 13).eval (center t) *
        (256 : ℂ) ^ (-center t - (13 : ℂ))‖ := by
          rfl
  rw [hSource]
  calc
    _ ≤ ((328 : ℝ) / 27) *
        (((7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ))) *
        (∏ j ∈ Finset.range 13, ((151 : ℝ) + j)) /
        (256 : ℝ) ^ 13) := by
          exact mul_le_mul hK hT (norm_nonneg _) hprod
    _ ≤ cap := exact_center_majorant.le

/-- TWO precise original pointwise source obligations, without any
unpaid hypothesis. This is still an UNCOMPILED new proof candidate. -/
theorem original_center_Borwein_left :
    zetaRemainderBound (center left) 6 256 ≤ cap :=
  original_center_Borwein left (by norm_num [left, right])

theorem original_center_Borwein_right :
    zetaRemainderBound (center right) 6 256 ≤ cap :=
  original_center_Borwein right (by norm_num [left, right])

end CP027PointwiseBorwein

#print axioms CP027PointwiseBorwein.original_ascending_pochhammer_norm
#print axioms CP027PointwiseBorwein.original_B14
#print axioms CP027PointwiseBorwein.original_B14_norm
#print axioms CP027PointwiseBorwein.center_geometry
#print axioms CP027PointwiseBorwein.center_prefactor
#print axioms CP027PointwiseBorwein.original_cpow_norm
#print axioms CP027PointwiseBorwein.original_omitted_term
#print axioms CP027PointwiseBorwein.exact_center_majorant
#print axioms CP027PointwiseBorwein.original_center_Borwein
#print axioms CP027PointwiseBorwein.original_center_Borwein_left
#print axioms CP027PointwiseBorwein.original_center_Borwein_right
