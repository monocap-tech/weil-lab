import WeilDefect.Morphology.NeutralWeilResidualCarrier
import Mathlib.Tactic

namespace WeilDefect

noncomputable section

/--
Physical Gaussian envelope centered on the compact support interval [-c,c].

This is the modulus profile that appears after the moving-frequency Gaussian
filter is transferred to physical space.  RPB-88 isolates only the support-gap
geometry and pointwise domination; the later tail integral is not included
here.
-/
def gaussianSupportEnvelope (R c x : ℝ) : ℝ :=
  Real.exp (-R * (|x| - c) ^ 2 / 4)

/--
Outside the strict interval (-a,a), the absolute value is at least a whenever
a is nonnegative.
-/
theorem radius_le_abs_of_not_mem_Ioo
    {a x : ℝ}
    (ha : 0 ≤ a)
    (hx : x ∉ Set.Ioo (-a) a) :
    a ≤ |x| := by
  have hx' : x ≤ -a ∨ a ≤ x := by
    by_cases hleft : x ≤ -a
    · exact Or.inl hleft
    · right
      have hleft' : -a < x := lt_of_not_ge hleft
      by_contra hright
      have hright' : x < a := lt_of_not_ge hright
      exact hx ⟨hleft', hright'⟩
  rcases hx' with hleft | hright
  · have hx0 : x ≤ 0 :=
      hleft.trans (neg_nonpos.mpr ha)
    rw [abs_of_nonpos hx0]
    linarith
  · have hx0 : 0 ≤ x :=
      ha.trans hright
    rw [abs_of_nonneg hx0]
    exact hright

/--
Strict support-gap geometry: if 0 ≤ c < a and x lies outside (-a,a), then
the distance proxy |x|-c is at least the collar width a-c.
-/
theorem supportGap_le_abs_sub
    {c a x : ℝ}
    (hc : 0 ≤ c)
    (hca : c < a)
    (hx : x ∉ Set.Ioo (-a) a) :
    a - c ≤ |x| - c := by
  have ha : 0 ≤ a :=
    hc.trans (le_of_lt hca)
  exact sub_le_sub_right
    (radius_le_abs_of_not_mem_Ioo ha hx) c

/--
Squared version of the support-gap inequality, used by the Gaussian exponent.
-/
theorem supportGap_sq_le_abs_sub_sq
    {c a x : ℝ}
    (hc : 0 ≤ c)
    (hca : c < a)
    (hx : x ∉ Set.Ioo (-a) a) :
    (a - c) ^ 2 ≤ (|x| - c) ^ 2 := by
  have hgap := supportGap_le_abs_sub hc hca hx
  have hgap0 : 0 ≤ a - c :=
    sub_nonneg.mpr (le_of_lt hca)
  have hxgap0 : 0 ≤ |x| - c :=
    hgap0.trans hgap
  nlinarith

/--
The physical Gaussian envelope on the exterior is bounded by the value forced
by the positive support gap.
-/
theorem gaussianSupportEnvelope_le_gap
    {R c a x : ℝ}
    (hR : 0 ≤ R)
    (hc : 0 ≤ c)
    (hca : c < a)
    (hx : x ∉ Set.Ioo (-a) a) :
    gaussianSupportEnvelope R c x
      ≤ Real.exp (-R * (a - c) ^ 2 / 4) := by
  unfold gaussianSupportEnvelope
  apply Real.exp_le_exp.mpr
  have hsquare :=
    supportGap_sq_le_abs_sub_sq hc hca hx
  have hmul :
      R * (a - c) ^ 2 ≤
        R * (|x| - c) ^ 2 :=
    mul_le_mul_of_nonneg_left hsquare hR
  nlinarith

/--
Pointwise product domination before using the support gap.

The hypothesis on g is exactly the physical Gaussian-filter envelope that the
next F-3 subpass must derive from the actual Gaussian convolution kernel and
the compact support of the F-1 mode.
-/
theorem residual_mul_gaussianEnvelope_bound
    {c R A : ℝ}
    (residual : NeutralExponentialResidualCarrier c)
    (g : ℝ → ℂ)
    (hA : 0 ≤ A)
    (hg :
      ∀ x : ℝ,
        ‖g x‖
          ≤ A * Real.sqrt R
              * gaussianSupportEnvelope R c x)
    (x : ℝ) :
    ‖residual.q x * g x‖
      ≤
      residual.growthConstant
        * Real.exp (residual.growthRate * |x|)
        * (A * Real.sqrt R
            * gaussianSupportEnvelope R c x) := by
  rw [norm_mul]
  exact mul_le_mul
    (residual.growth_bound x)
    (hg x)
    (norm_nonneg _)
    (mul_nonneg
      residual.growthConstant_nonneg
      (Real.exp_nonneg _))

/--
Exterior pointwise domination after inserting the positive support gap.

This is the first load-bearing F-3 estimate.  It still retains the residual's
fixed exponential growth in |x|; the next pass must integrate/complete the
square against the remaining Gaussian tail.
-/
theorem residual_mul_gaussianExterior_bound
    {c R A x : ℝ}
    (residual : NeutralExponentialResidualCarrier c)
    (hc : 0 ≤ c)
    (hR : 0 ≤ R)
    (hA : 0 ≤ A)
    (g : ℝ → ℂ)
    (hg :
      ∀ y : ℝ,
        ‖g y‖
          ≤ A * Real.sqrt R
              * gaussianSupportEnvelope R c y)
    (hx : x ∉ Set.Ioo (-residual.a) residual.a) :
    ‖residual.q x * g x‖
      ≤
      residual.growthConstant
        * Real.exp (residual.growthRate * |x|)
        * (A * Real.sqrt R
            * Real.exp
                (-R * (residual.a - c) ^ 2 / 4)) := by
  have henv :
      gaussianSupportEnvelope R c x
        ≤ Real.exp
            (-R * (residual.a - c) ^ 2 / 4) :=
    gaussianSupportEnvelope_le_gap
      hR hc residual.strict hx
  calc
    ‖residual.q x * g x‖
        ≤ residual.growthConstant
            * Real.exp (residual.growthRate * |x|)
            * (A * Real.sqrt R
                * gaussianSupportEnvelope R c x) :=
      residual_mul_gaussianEnvelope_bound
        residual g hA hg x
    _ ≤ residual.growthConstant
            * Real.exp (residual.growthRate * |x|)
            * (A * Real.sqrt R
                * Real.exp
                    (-R * (residual.a - c) ^ 2 / 4)) := by
      apply mul_le_mul_of_nonneg_left
      · apply mul_le_mul_of_nonneg_left henv
        exact mul_nonneg hA (Real.sqrt_nonneg R)
      · exact mul_nonneg
          residual.growthConstant_nonneg
          (Real.exp_nonneg _)

end

end WeilDefect
