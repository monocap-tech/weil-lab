module

public import CP016MonotoneAttach
public import Mathlib.Analysis.Calculus.Deriv.MeanValue
public import Mathlib.Analysis.Calculus.MeanValue

/-!
CP017: a RATIONAL SUFFICIENCY CERTIFICATE for original Hardy-Z
monotonicity on the entire source-to-narrow-zero interval.

The following two analytic premises are NOT YET PROVED and are NOT
obtainable from floating-point samples:
  (A) 12/5 <= deriv Zeta.hardyZ (149.5)
  (B) |Z'(t)-Z'(149.5)| <= 4 * (t-149.5)
      for EVERY t in [149.5,150.05353].

They imply Z'(t) >= 4647/25000 = 0.18588 > 0, and hence strict
monotonicity and (CONDITIONALLY on the actual new root proof) numerical
identity with the original source-defined 53rd zero.

A more primitive differentiable-derivative/curvature sufficient condition:
  DifferentiableOn ℝ (deriv Zeta.hardyZ) [a,b] and
  ||derivWithin (deriv Zeta.hardyZ) [a,b] x|| <= 4 for x in [a,b).
This implies (B) by the genuine original Mathlib mean value theorem.
None of these analytic bounds has a kernel receipt, and the source
modules are candidates until a REAL original Lean 4.35 compiler pass.
-/

@[expose] public section

open Set

namespace CP017CurvatureBudget

private abbrev a : ℝ := (149500 : ℝ) / 1000
private abbrev b : ℝ := (15005353 : ℝ) / 100000

/-- Exact, no floating-point rounding: requested curvature budget
sacrifices 4·0.55353 = 2.21412 derivative units, leaving 0.18588. -/
theorem exact_positive_derivative_margin :
    (0 : ℝ) < (12 : ℝ) / 5 - 4 * (b - a) := by
  norm_num [a, b]

/-- A single derivative anchor and a source-independent Lipschitz
variation guarantee a STRICT positive derivative throughout the
whole window, with exact rational lower margin 4647/25000.
These are explicit analytic hypotheses, not a point-sample check. -/
theorem uniform_derivative_margin_of_rational_budget
    (hanchor : (12 : ℝ) / 5 ≤ deriv Zeta.hardyZ a)
    (hvariation :
      ∀ t ∈ Icc a b,
        |deriv Zeta.hardyZ t - deriv Zeta.hardyZ a|
          ≤ 4 * (t - a)) :
    ∀ t ∈ Icc a b, (4647 : ℝ) / 25000 ≤ deriv Zeta.hardyZ t := by
  intro t ht
  have hdif := (abs_le.mp (hvariation t ht)).1
  have hwidth : t - a ≤ b - a := by
    have := ht.2
    linarith
  have hmargin :
      (4647 : ℝ) / 25000 =
        (12 : ℝ) / 5 - 4 * (b - a) := by
    norm_num [a, b]
  rw [hmargin]
  linarith

/-- Exact rational analytic budget A+B implies original source Hardy-Z
strict monotonicity. Source Hardy-Z continuity and original Mathlib
derivative-to-monotonicity theorem are reused. -/
theorem strictMonoOn_original_hardyZ_of_rational_budget
    (hanchor : (12 : ℝ) / 5 ≤ deriv Zeta.hardyZ a)
    (hvariation :
      ∀ t ∈ Icc a b,
        |deriv Zeta.hardyZ t - deriv Zeta.hardyZ a|
          ≤ 4 * (t - a)) :
    StrictMonoOn Zeta.hardyZ (Icc a b) := by
  have hcontinuous : ContinuousOn Zeta.hardyZ (Icc a b) :=
    continuousOn_hardyZ.mono (by
      intro t ht
      exact (show (0 : ℝ) ≤ t from
        (by norm_num [a] : (0 : ℝ) ≤ a).trans ht.1))
  apply strictMonoOn_of_deriv_pos (convex_Icc a b) hcontinuous
  intro t ht
  have hwithin : t ∈ Icc a b := interior_subset ht
  have hbound :=
    uniform_derivative_margin_of_rational_budget hanchor hvariation t hwithin
  have hmargin : (0 : ℝ) < (4647 : ℝ) / 25000 := by norm_num
  linarith

/-- RIGOROUS derivative variation follows from a uniform curvature
enclosure on [a,b) and differentiability on [a,b]. This is exactly
the source Mathlib mean value theorem, not sampling. -/
theorem derivative_variation_of_curvature_bound
    (hdiff : DifferentiableOn ℝ (deriv Zeta.hardyZ) (Icc a b))
    (hcurvature : ∀ t ∈ Ico a b,
      ‖derivWithin (deriv Zeta.hardyZ) (Icc a b) t‖ ≤ (4 : ℝ)) :
    ∀ t ∈ Icc a b,
      |deriv Zeta.hardyZ t - deriv Zeta.hardyZ a|
        ≤ 4 * (t - a) := by
  intro t ht
  have h := norm_image_sub_le_of_norm_deriv_le_segment
    hdiff hcurvature t ht
  simpa only [Real.norm_eq_abs] using h

/-- Exact analytic checklist: one endpoint derivative lower enclosure
and ONE uniform bound on the second derivative of Hardy-Z (in the
derivWithin sense) suffice for monotonicity. -/
theorem strictMonoOn_original_hardyZ_of_curvature_bound
    (hanchor : (12 : ℝ) / 5 ≤ deriv Zeta.hardyZ a)
    (hdiff : DifferentiableOn ℝ (deriv Zeta.hardyZ) (Icc a b))
    (hcurvature : ∀ t ∈ Ico a b,
      ‖derivWithin (deriv Zeta.hardyZ) (Icc a b) t‖ ≤ (4 : ℝ)) :
    StrictMonoOn Zeta.hardyZ (Icc a b) :=
  strictMonoOn_original_hardyZ_of_rational_budget
    hanchor (derivative_variation_of_curvature_bound hdiff hcurvature)

/-- If a new critical-line zero in CP010's narrow candidate interval
has been independently kernel-certified, then rational budget A+B
IDENTIFIES it with source-defined ordinal 53.

No new root existence or either analytic bound is proved here.
The original source first RS numerical row remains unavailable. -/
theorem refined_narrow_root_is_source_53rd_of_rational_budget
    {t : ℝ}
    (hnarrow : t ∈ Ioo ((15005352 : ℝ) / 100000)
      ((15005353 : ℝ) / 100000))
    (hzero : riemannZeta (1 / 2 + Complex.I * (t : ℂ)) = 0)
    (hanchor : (12 : ℝ) / 5 ≤ deriv Zeta.hardyZ a)
    (hvariation : ∀ u ∈ Icc a b,
      |deriv Zeta.hardyZ u - deriv Zeta.hardyZ a|
        ≤ 4 * (u - a))
    (hb : b < gramPoint certifiedZeroCount.minIdx) :
    ∃ z : ℂ, z ∈ CP015SourceWitnesses.rsRoots ∧
      riemannZeta.N z.im = 52 ∧
      z = 1 / 2 + Complex.I * (t : ℂ) := by
  have ht : t ∈ Ioo a b := by
    constructor
    · calc
        a < (15005352 : ℝ) / 100000 := by norm_num [a]
        _ < t := hnarrow.1
    · exact hnarrow.2
  exact CP016MonotoneAttach.refined_root_equals_original_53rd_of_hardy_monotone
    ht hb
    (strictMonoOn_original_hardyZ_of_rational_budget hanchor hvariation)
    hzero

end CP017CurvatureBudget

#print axioms CP017CurvatureBudget.exact_positive_derivative_margin
#print axioms CP017CurvatureBudget.uniform_derivative_margin_of_rational_budget
#print axioms CP017CurvatureBudget.strictMonoOn_original_hardyZ_of_rational_budget
#print axioms CP017CurvatureBudget.derivative_variation_of_curvature_bound
#print axioms CP017CurvatureBudget.strictMonoOn_original_hardyZ_of_curvature_bound
#print axioms CP017CurvatureBudget.refined_narrow_root_is_source_53rd_of_rational_budget
