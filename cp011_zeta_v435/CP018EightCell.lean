module

public import CP017CurvatureBudget
public import Mathlib.Analysis.Calculus.MeanValue

/-!
CP018: a FINITE CERTIFICATE of Hardy-Z curvature from eight *rational*
midpoint second-derivative enclosures and a uniform third-derivative bound.

a = 149.5, b = 150.05353, and for j = 0..7:
  c_j = a + (2j+1)(b-a)/16.

GENUINE missing analytic inputs, never supplied here by floating-point:
  (1) Z'(a) >= 12/5.
  (2) for all 8 rational centers, |Z''(c_j)| <= 7/2.
  (3) Z'' is differentiable on [a,b].
  (4) for all t in [a,b], |Z'''(t)| <= 12.
  (5) Z' differentiable on [a,b].
  (6) a true critical-line zeta zero in (150.05352,150.05353).

Then every t∈[a,b] is within Δ/16 of a center, so
  |Z''(t)| <= 7/2 + 12Δ/16
            = 1566059/400000 = 3.9151475 < 4.
CP017's rational curvature budget gives Z'(t)>=4647/25000>0.
CP016's exact ordinal source bridge then ATTACHES the refined zero
to canonical first RS root #53. ALL source math beyond this sufficient
implication remains UNCOMPILED until real external Lean v4.35 audit.

Unlike a derivative of the original HardyZ VALUE-error inequality,
this is mathematically sound, since the derivative data and smoothness
are stated explicitly rather than inferred from an absolute value bound.
-/

@[expose] public section

open Set

namespace CP018EightCell

private abbrev a : ℝ := (149500 : ℝ) / 1000
private abbrev b : ℝ := (15005353 : ℝ) / 100000
private abbrev width : ℝ := b - a

/-- Exact-rational 8-cell midpoint locations. -/
def center (j : Fin 8) : ℝ :=
  a + ((2 * j.val + 1 : ℕ) : ℝ) * width / 16

/-- Exact-rational jth left boundary. -/
private def left (j : Fin 8) : ℝ :=
  a + (j.val : ℝ) * width / 8

/-- Exact-rational jth right boundary. -/
private def right (j : Fin 8) : ℝ :=
  a + ((j.val + 1 : ℕ) : ℝ) * width / 8

/-- The jth center sits inside its own eighth of the interval. -/
theorem center_mem_interval (j : Fin 8) : center j ∈ Icc a b := by
  have hj : j.val < 8 := j.isLt
  dsimp [center, a, b, width]
  constructor <;> norm_num at * <;> nlinarith

/-- Exact rational half-cell radius. All variables are real and j ranges
over the finite eight original source cells. -/
private theorem distance_to_center_of_cell
    (j : Fin 8) (t : ℝ)
    (hlo : left j ≤ t) (hhi : t ≤ right j) :
    |t - center j| ≤ width / 16 := by
  rw [abs_le]
  constructor
  · dsimp [left, right, center, width] at *
    push_cast at *
    nlinarith [hlo]
  · dsimp [left, right, center, width] at *
    push_cast at *
    nlinarith [hhi]

/-- Every point in the ENTIRE closed target interval is within
the exact half-width Δ/16 of ONE of the EIGHT rational midpoints.
This is a finite rational coverage statement, not a HardyZ estimate. -/
theorem eight_center_cover (t : ℝ) (ht : t ∈ Icc a b) :
    ∃ j : Fin 8, |t - center j| ≤ width / 16 := by
  by_cases h0 : t ≤ a + width / 8
  · refine ⟨⟨0, by decide⟩, distance_to_center_of_cell ⟨0, by decide⟩ t ?_ ?_⟩
    · dsimp [left]
      simpa using ht.1
    · dsimp [right]
      simpa using h0
  · by_cases h1 : t ≤ a + 2 * width / 8
    · refine ⟨⟨1, by decide⟩, distance_to_center_of_cell ⟨1, by decide⟩ t ?_ ?_⟩
      · dsimp [left]
        nlinarith [not_le.mp h0]
      · dsimp [right]
        nlinarith [h1]
    · by_cases h2 : t ≤ a + 3 * width / 8
      · refine ⟨⟨2, by decide⟩, distance_to_center_of_cell ⟨2, by decide⟩ t ?_ ?_⟩
        · dsimp [left]
          nlinarith [not_le.mp h1]
        · dsimp [right]
          nlinarith [h2]
      · by_cases h3 : t ≤ a + 4 * width / 8
        · refine ⟨⟨3, by decide⟩, distance_to_center_of_cell ⟨3, by decide⟩ t ?_ ?_⟩
          · dsimp [left]
            nlinarith [not_le.mp h2]
          · dsimp [right]
            nlinarith [h3]
        · by_cases h4 : t ≤ a + 5 * width / 8
          · refine ⟨⟨4, by decide⟩, distance_to_center_of_cell ⟨4, by decide⟩ t ?_ ?_⟩
            · dsimp [left]
              nlinarith [not_le.mp h3]
            · dsimp [right]
              nlinarith [h4]
          · by_cases h5 : t ≤ a + 6 * width / 8
            · refine ⟨⟨5, by decide⟩, distance_to_center_of_cell ⟨5, by decide⟩ t ?_ ?_⟩
              · dsimp [left]
                nlinarith [not_le.mp h4]
              · dsimp [right]
                nlinarith [h5]
            · by_cases h6 : t ≤ a + 7 * width / 8
              · refine ⟨⟨6, by decide⟩, distance_to_center_of_cell ⟨6, by decide⟩ t ?_ ?_⟩
                · dsimp [left]
                  nlinarith [not_le.mp h5]
                · dsimp [right]
                  nlinarith [h6]
              · refine ⟨⟨7, by decide⟩, distance_to_center_of_cell ⟨7, by decide⟩ t ?_ ?_⟩
                · dsimp [left]
                  nlinarith [not_le.mp h6]
                · dsimp [right, width]
                  nlinarith [ht.2]

/-- Exact rational worst-case curvature after eight center checks and
a global THIRD-derivative bound 12. Real arithmetic, no zeta data. -/
theorem exact_eight_cell_curvature_margin :
    (7 : ℝ) / 2 + 12 * width / 16 =
      (1566059 : ℝ) / 400000 ∧
    (1566059 : ℝ) / 400000 < 4 := by
  constructor <;> norm_num [a, b, width]

/-- Completely generic real function theorem: EIGHT finite midpoint
second-derivative checks and a genuine global third-derivative bound
imply the UNIFORM original curvature cap 4 on [a,b].
All analytic estimates remain explicit proof-bearing hypotheses. -/
theorem eight_midpoints_and_third_derivative_imply_curvature
    (f : ℝ → ℝ)
    (hD2diff : ∀ t ∈ Icc a b,
      DifferentiableAt ℝ (deriv (deriv f)) t)
    (hD3 : ∀ t ∈ Icc a b,
      ‖deriv (deriv (deriv f)) t‖ ≤ 12)
    (hcenters : ∀ j : Fin 8,
      |deriv (deriv f) (center j)| ≤ (7 : ℝ) / 2) :
    ∀ t ∈ Icc a b,
      |deriv (deriv f) t| ≤ 4 := by
  intro t ht
  obtain ⟨j, hjdist⟩ := eight_center_cover t ht
  have hc : center j ∈ Icc a b := center_mem_interval j
  have hlip := (convex_Icc a b).norm_image_sub_le_of_norm_deriv_le
    hD2diff hD3 hc ht
  have hdiff :
      |deriv (deriv f) t - deriv (deriv f) (center j)|
        ≤ 12 * |t - center j| := by
    simpa only [Real.norm_eq_abs] using hlip
  have hcenter := hcenters j
  have htriangle :
      |deriv (deriv f) t| ≤
        |deriv (deriv f) t - deriv (deriv f) (center j)| +
          |deriv (deriv f) (center j)| := by
    convert abs_add_le
      (deriv (deriv f) t - deriv (deriv f) (center j))
      (deriv (deriv f) (center j)) using 1 <;> ring
  have hbudget := exact_eight_cell_curvature_margin
  have hw : 0 ≤ width := by norm_num [a, b, width]
  nlinarith [htriangle, hcenter, hdiff, hjdist, hbudget.1, hbudget.2]

/-- The finite eight-center certificate transfers directly into the
ORIGINAL Hardy-Z strict monotonicity target used by CP016, without
using a black-box derivative of the published value-error inequality. -/
theorem original_hardyZ_strictMono_of_eight_midpoint_certificate
    (hanchor : (12 : ℝ) / 5 ≤ deriv Zeta.hardyZ a)
    (hD1diff : ∀ t ∈ Icc a b,
      DifferentiableAt ℝ (deriv Zeta.hardyZ) t)
    (hD2diff : ∀ t ∈ Icc a b,
      DifferentiableAt ℝ (deriv (deriv Zeta.hardyZ)) t)
    (hD3 : ∀ t ∈ Icc a b,
      ‖deriv (deriv (deriv Zeta.hardyZ)) t‖ ≤ 12)
    (hcenters : ∀ j : Fin 8,
      |deriv (deriv Zeta.hardyZ) (center j)| ≤ (7 : ℝ) / 2) :
    StrictMonoOn Zeta.hardyZ (Icc a b) := by
  have hsecond := eight_midpoints_and_third_derivative_imply_curvature
    Zeta.hardyZ hD2diff hD3 hcenters
  have hvariation :
      ∀ t ∈ Icc a b,
        |deriv Zeta.hardyZ t - deriv Zeta.hardyZ a| ≤
          4 * (t - a) := by
    intro t ht
    have ha : a ∈ Icc a b := by
      constructor
      · exact le_refl _
      · norm_num [a, b]
    have hlip :=
      (convex_Icc a b).norm_image_sub_le_of_norm_deriv_le
        hD1diff (by
          intro u hu
          simpa [Real.norm_eq_abs] using hsecond u hu)
        ha ht
    have hta : 0 ≤ t - a := sub_nonneg.mpr ht.1
    simpa only [Real.norm_eq_abs, abs_of_nonneg hta] using hlip
  exact CP017CurvatureBudget.strictMonoOn_original_hardyZ_of_rational_budget
    hanchor hvariation

end CP018EightCell

#print axioms CP018EightCell.center_mem_interval
#print axioms CP018EightCell.eight_center_cover
#print axioms CP018EightCell.exact_eight_cell_curvature_margin
#print axioms CP018EightCell.eight_midpoints_and_third_derivative_imply_curvature
#print axioms CP018EightCell.original_hardyZ_strictMono_of_eight_midpoint_certificate
