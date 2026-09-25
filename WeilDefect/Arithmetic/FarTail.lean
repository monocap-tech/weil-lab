import WeilDefect.RationalResponse
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics

namespace WeilDefect

open Filter Set MeasureTheory
open scoped Topology BigOperators

/-- Continuous majorant used for the WD-T31 logarithmic shell tail. -/
noncomputable def logarithmicTailKernel (x : ℝ) : ℝ :=
  (1 + Real.log x) / x ^ 2

private theorem hasDerivAt_logarithmicTailKernel
    {x : ℝ} (hx : x ≠ 0) :
    HasDerivAt logarithmicTailKernel
      ((-1 - 2 * Real.log x) / x ^ 3) x := by
  unfold logarithmicTailKernel
  have hnum :
      HasDerivAt (fun y : ℝ => 1 + Real.log y) x⁻¹ x :=
    (Real.hasDerivAt_log hx).const_add 1
  have hden := (hasDerivAt_id x).pow 2
  convert hnum.div hden (by simp [hx]) using 1
  field_simp [hx]
  ring

/-- The logarithmic tail kernel is nonnegative on [1,∞). -/
theorem logarithmicTailKernel_nonneg
    {x : ℝ} (hx : 1 ≤ x) :
    0 ≤ logarithmicTailKernel x := by
  unfold logarithmicTailKernel
  have hx0 : 0 < x := lt_of_lt_of_le zero_lt_one hx
  have hlog : 0 ≤ Real.log x := Real.log_nonneg hx
  positivity

/-- The logarithmic tail kernel is decreasing on [1,∞). -/
theorem logarithmicTailKernel_antitoneOn :
    AntitoneOn logarithmicTailKernel (Ici (1 : ℝ)) := by
  apply antitoneOn_of_deriv_nonpos (convex_Ici (1 : ℝ))
  · intro x hx
    have hx0 : x ≠ 0 := by
      have : 0 < x := lt_of_lt_of_le zero_lt_one hx
      exact this.ne'
    exact (hasDerivAt_logarithmicTailKernel hx0).continuousAt.continuousWithinAt
  · intro x hx
    have hx1 : 1 < x := by
      simpa only [interior_Ici, mem_Ioi] using hx
    have hx0 : x ≠ 0 := (lt_trans zero_lt_one hx1).ne'
    exact (hasDerivAt_logarithmicTailKernel hx0).differentiableAt.differentiableWithinAt
  · intro x hx
    have hx1 : 1 < x := by
      simpa only [interior_Ici, mem_Ioi] using hx
    have hx0 : x ≠ 0 := (lt_trans zero_lt_one hx1).ne'
    rw [(hasDerivAt_logarithmicTailKernel hx0).deriv]
    have hlog : 0 ≤ Real.log x := Real.log_nonneg hx1.le
    have hden : 0 ≤ x ^ 3 := by positivity
    exact div_nonpos_of_nonpos_of_nonneg (by linarith) hden

private theorem hasDerivAt_logarithmicTailAntideriv
    {x : ℝ} (hx : x ≠ 0) :
    HasDerivAt
      (fun y : ℝ => -(Real.log y + 2) / y)
      (logarithmicTailKernel x) x := by
  have hnum :
      HasDerivAt (fun y : ℝ => Real.log y + 2) x⁻¹ x :=
    (Real.hasDerivAt_log hx).add_const 2
  have hquot :=
    hnum.div (hasDerivAt_id x) hx
  convert hquot.neg using 1
  · ext y
    simp [neg_div]
  · unfold logarithmicTailKernel
    simp only [id_eq]
    field_simp [hx]
    ring

private theorem tendsto_logarithmicTailAntideriv :
    Tendsto (fun x : ℝ => -(Real.log x + 2) / x) atTop (𝓝 0) := by
  have hlog :
      Tendsto (fun x : ℝ => Real.log x / x) atTop (𝓝 0) := by
    simpa [Real.rpow_one] using
      (isLittleO_log_rpow_atTop (r := (1 : ℝ)) zero_lt_one).tendsto_div_nhds_zero
  have hconst :
      Tendsto (fun x : ℝ => (2 : ℝ) / x) atTop (𝓝 0) := by
    exact tendsto_const_nhds.div_atTop tendsto_id
  have hadd := hlog.add hconst
  simpa [add_div, add_comm, neg_div] using hadd.neg

/-- The kernel is integrable on every positive tail starting at c>=1. -/
theorem logarithmicTailKernel_integrableOn_Ioi
    {c : ℝ} (hc : 1 ≤ c) :
    IntegrableOn logarithmicTailKernel (Ioi c) := by
  apply integrableOn_Ioi_deriv_of_nonneg'
    (g := fun x : ℝ => -(Real.log x + 2) / x)
    (l := 0)
  · intro x hx
    have hx0 : x ≠ 0 := by
      have : 0 < x := lt_of_lt_of_le zero_lt_one (hc.trans hx)
      exact this.ne'
    exact hasDerivAt_logarithmicTailAntideriv hx0
  · intro x hx
    exact logarithmicTailKernel_nonneg (hc.trans hx.le)
  · exact tendsto_logarithmicTailAntideriv

/-- Exact improper integral of the logarithmic tail kernel. -/
theorem integral_logarithmicTailKernel_Ioi
    {c : ℝ} (hc : 1 ≤ c) :
    ∫ x in Ioi c, logarithmicTailKernel x =
      (Real.log c + 2) / c := by
  have h :=
    integral_Ioi_of_hasDerivAt_of_nonneg'
      (a := c)
      (g := fun x : ℝ => -(Real.log x + 2) / x)
      (g' := logarithmicTailKernel)
      (l := 0)
      (fun x hx => by
        have hx0 : x ≠ 0 := by
          have : 0 < x := lt_of_lt_of_le zero_lt_one (hc.trans hx)
          exact this.ne'
        exact hasDerivAt_logarithmicTailAntideriv hx0)
      (fun x hx => logarithmicTailKernel_nonneg (hc.trans hx.le))
      tendsto_logarithmicTailAntideriv
  convert h using 1 <;> ring

/--
Discrete logarithmic tail estimate.  This is the analytic summation step in
WD-T31: the unit-shell majorant has an explicit O((log R)/R) tail.
-/
theorem logarithmicTail_tsum_le
    (R : ℕ) (hR : 1 ≤ R) :
    (∑' k : ℕ, logarithmicTailKernel (k + R + 1 : ℕ))
      ≤ (Real.log R + 2) / R := by
  have hanti :
      AntitoneOn logarithmicTailKernel (Ici (R : ℝ)) :=
    logarithmicTailKernel_antitoneOn.mono (by
      intro x hx
      have hRreal : (1 : ℝ) ≤ (R : ℝ) := by exact_mod_cast hR
      have hxR : (R : ℝ) ≤ x := hx
      exact hRreal.trans hxR)
  have hint :
      IntegrableOn logarithmicTailKernel (Ioi (R : ℝ)) :=
    logarithmicTailKernel_integrableOn_Ioi (by exact_mod_cast hR)
  have hnonneg :
      ∀ x ∈ Ioi (R : ℝ), 0 ≤ logarithmicTailKernel x := by
    intro x hx
    exact logarithmicTailKernel_nonneg
      (le_trans (by exact_mod_cast hR) hx.le)
  have hbound :=
    hanti.tsum_comp_add_le_integral R hint hnonneg
  rw [integral_logarithmicTailKernel_Ioi (by exact_mod_cast hR)] at hbound
  simpa [Nat.cast_add, Nat.cast_one] using hbound

end WeilDefect
