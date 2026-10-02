import WeilDefect.Morphology.NeutralDigammaStepDecay
import Mathlib.Analysis.Normed.Group.InfiniteSum
import Mathlib.Topology.Algebra.InfiniteSum.Order

namespace WeilDefect

noncomputable section

open Filter
open scoped BigOperators Topology

/-- Fixed finite mass of the shift-index cubic majorant. -/
def neutralCenteredDigammaCubicMass : ℝ := ∑' n : ℕ, 1 / ((n : ℝ)+1)^3

theorem neutralCenteredDigammaCubic_summable :
    Summable (fun n : ℕ => 1 / ((n : ℝ)+1)^3) := by
  simpa only [Nat.cast_add, Nat.cast_one] using
    (summable_nat_add_iff (f := fun n : ℕ => 1 / (n : ℝ)^3) 1).mpr
      (Real.summable_one_div_nat_pow.mpr (by norm_num : 1 < (3 : ℕ)))

/-- The actual centered increments, as a complex absolutely convergent series. -/
theorem neutralCenteredDigammaSymbol_step_summable (ξ : ℝ) :
    Summable (fun n : ℕ => neutralCenteredDigammaSymbol (n+1) ξ -
      neutralCenteredDigammaSymbol n ξ) :=
  (neutralCenteredDigammaSymbol_step_norm_summable ξ).of_norm

theorem neutralCenteredDigammaSymbol_telescoping (N : ℕ) (ξ : ℝ) :
    (∑ n ∈ Finset.range N, (neutralCenteredDigammaSymbol (n+1) ξ -
      neutralCenteredDigammaSymbol n ξ)) =
      neutralCenteredDigammaSymbol N ξ - neutralCenteredDigammaSymbol 0 ξ := by
  induction N with
  | zero => simp
  | succ N ih => rw [Finset.sum_range_succ, ih]; ring

/-- Actual pointwise residual: initial centered digamma value plus the
absolutely convergent series of its actual increments. No zero claim. -/
def neutralCenteredDigammaLimit (ξ : ℝ) : ℂ :=
  neutralCenteredDigammaSymbol 0 ξ + ∑' n : ℕ,
    (neutralCenteredDigammaSymbol (n+1) ξ - neutralCenteredDigammaSymbol n ξ)

theorem neutralCenteredDigammaSymbol_tendsto (ξ : ℝ) :
    Tendsto (fun N : ℕ => neutralCenteredDigammaSymbol N ξ) atTop
      (𝓝 (neutralCenteredDigammaLimit ξ)) := by
  have h0 : Tendsto (fun _ : ℕ => neutralCenteredDigammaSymbol 0 ξ) atTop
      (𝓝 (neutralCenteredDigammaSymbol 0 ξ)) := tendsto_const_nhds
  have h := h0.add
    (neutralCenteredDigammaSymbol_step_summable ξ).hasSum.tendsto_sum_nat
  change Tendsto _ atTop (𝓝 (neutralCenteredDigammaSymbol 0 ξ + ∑' n : ℕ,
    (neutralCenteredDigammaSymbol (n+1) ξ - neutralCenteredDigammaSymbol n ξ)))
  convert h using 1
  funext N
  rw [neutralCenteredDigammaSymbol_telescoping]
  ring

/-- Explicit reciprocal-series representation of the actual residual.
This is not an assumed Gauss formula and does not assert cancellation. -/
theorem neutralCenteredDigammaLimit_eq_reciprocal_series (ξ : ℝ) :
    neutralCenteredDigammaLimit ξ = neutralCenteredDigammaSymbol 0 ξ +
      ∑' n : ℕ, ((neutralGaussReciprocal n (2*Real.pi*ξ) -
        neutralGaussReciprocal n 0 : ℝ) : ℂ) := by
  unfold neutralCenteredDigammaLimit
  simp_rw [neutralCenteredDigammaSymbol_step]

/-- Uniform-in-shift frequency envelope for the actual centered displacement. -/
theorem neutralCenteredDigammaSymbol_uniform_displacement_bound (N : ℕ) (ξ : ℝ) :
    ‖neutralCenteredDigammaSymbol N ξ - neutralCenteredDigammaSymbol 0 ξ‖ ≤
      64*(Real.pi*ξ)^2 * neutralCenteredDigammaCubicMass := by
  have hg : Summable (fun n : ℕ => 64*(Real.pi*ξ)^2 / ((n : ℝ)+1)^3) := by
    simpa only [mul_one_div] using
      neutralCenteredDigammaCubic_summable.mul_left (64*(Real.pi*ξ)^2)
  rw [← neutralCenteredDigammaSymbol_telescoping]
  calc
    ‖∑ n ∈ Finset.range N, (neutralCenteredDigammaSymbol (n+1) ξ -
        neutralCenteredDigammaSymbol n ξ)‖ ≤
      ∑ n ∈ Finset.range N, ‖neutralCenteredDigammaSymbol (n+1) ξ -
        neutralCenteredDigammaSymbol n ξ‖ := norm_sum_le _ _
    _ ≤ ∑ n ∈ Finset.range N, 64*(Real.pi*ξ)^2 / ((n : ℝ)+1)^3 :=
      Finset.sum_le_sum (fun n _ => neutralCenteredDigammaSymbol_step_norm_bound n ξ)
    _ ≤ ∑' n : ℕ, 64*(Real.pi*ξ)^2 / ((n : ℝ)+1)^3 :=
      hg.sum_le_tsum (Finset.range N) (fun n _ => by positivity)
    _ = 64*(Real.pi*ξ)^2 * neutralCenteredDigammaCubicMass := by
      simp only [neutralCenteredDigammaCubicMass, div_eq_mul_inv, one_mul,
        tsum_mul_left]

theorem neutralCenteredDigammaSymbol_uniform_norm_bound (N : ℕ) (ξ : ℝ) :
    ‖neutralCenteredDigammaSymbol N ξ‖ ≤ ‖neutralCenteredDigammaSymbol 0 ξ‖ +
      64*(Real.pi*ξ)^2 * neutralCenteredDigammaCubicMass := by
  have h := norm_add_le (neutralCenteredDigammaSymbol N ξ -
    neutralCenteredDigammaSymbol 0 ξ) (neutralCenteredDigammaSymbol 0 ξ)
  rw [sub_add_cancel] at h
  linarith [neutralCenteredDigammaSymbol_uniform_displacement_bound N ξ]

/-- The zero-tail question is exactly cancellation of this actual residual. -/
theorem neutralCenteredDigammaSymbol_zero_limit_iff (ξ : ℝ) :
    Tendsto (fun N : ℕ => neutralCenteredDigammaSymbol N ξ) atTop (𝓝 0) ↔
      neutralCenteredDigammaLimit ξ = 0 := by
  constructor
  · intro h
    exact tendsto_nhds_unique (neutralCenteredDigammaSymbol_tendsto ξ) h
  · intro h
    rw [← h]
    exact neutralCenteredDigammaSymbol_tendsto ξ

end

end WeilDefect
