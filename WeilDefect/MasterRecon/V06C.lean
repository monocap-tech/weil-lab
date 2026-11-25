import WeilDefect.MasterRecon.V06B
import Mathlib.Analysis.Analytic.IsolatedZeros
import Mathlib.Analysis.Normed.Module.Connected

/-! V06C: analytic uniqueness for bounded observations of the local
solution orbit. The real negative-axis vanishing is explicit. -/
namespace WeilDefect.MasterRecon.V06C

open Set
open scoped Topology

variable {H F : Type*}
variable [NormedAddCommGroup H] [NormedSpace ℂ H]
variable [NormedAddCommGroup F] [NormedSpace ℂ F]

/-- A vector-valued analytic function on a disk is identically zero if
it vanishes on the negative real radius. -/
theorem negative_radius_identity (f : ℂ → F) (r : ℝ) (hr : 0 < r)
    (hf : AnalyticOnNhd ℂ f (Metric.ball 0 r))
    (hz : ∀ a : ℝ, -r < a → a < 0 → f (a : ℂ) = 0) :
    ∀ z ∈ Metric.ball (0 : ℂ) r, f z = 0 := by
  have hc : (0 : ℂ) ∈ closure ({z | f z = 0} \ ({0} : Set ℂ)) := by
    apply Metric.mem_closure_iff.mpr
    intro ε hε
    let a : ℝ := -(min r ε / 2)
    have hm : 0 < min r ε := lt_min hr hε
    have ha : a < 0 := by dsimp [a]; linarith
    have har : -r < a := by
      dsimp [a]
      have hle := min_le_left r ε
      linarith
    have hae : -a < ε := by
      dsimp [a]
      have hle := min_le_right r ε
      linarith
    refine ⟨(a : ℂ), ?_, ?_⟩
    · refine ⟨hz a har ha, ?_⟩
      simp only [mem_singleton_iff]
      exact_mod_cast (ne_of_lt ha)
    · rw [dist_comm, dist_zero_right, Complex.norm_real, Real.norm_eq_abs,
        abs_of_neg ha]
      exact hae
  have he := hf.eqOn_zero_of_preconnected_of_mem_closure
    isPreconnected_ball (Metric.mem_ball_self hr) hc
  intro z hz'
  exact he hz'

/-- Vanishing of a bounded linear observation on one real radius
propagates throughout the complex disk. -/
theorem observed_orbit_identity (U : ℂ → H) (J : H →L[ℂ] F)
    (r : ℝ) (hr : 0 < r)
    (hU : AnalyticOnNhd ℂ U (Metric.ball 0 r))
    (hz : ∀ a : ℝ, -r < a → a < 0 → J (U (a : ℂ)) = 0) :
    ∀ z ∈ Metric.ball (0 : ℂ) r, J (U z) = 0 :=
  negative_radius_identity (fun z => J (U z)) r hr
    (J.comp_analyticOnNhd hU) hz

/-- In particular, every positive real translation strictly inside the
disk has zero observation. The physical restriction map is an input. -/
theorem positive_radius_observation (U : ℂ → H) (J : H →L[ℂ] F)
    (r : ℝ) (hr : 0 < r)
    (hU : AnalyticOnNhd ℂ U (Metric.ball 0 r))
    (hz : ∀ a : ℝ, -r < a → a < 0 → J (U (a : ℂ)) = 0)
    (s : ℝ) (hs : 0 < s) (hsr : s < r) :
    J (U (s : ℂ)) = 0 := by
  apply observed_orbit_identity U J r hr hU hz
  rw [Metric.mem_ball, dist_zero_right, Complex.norm_real, Real.norm_eq_abs,
    abs_of_pos hs]
  exact hsr

end WeilDefect.MasterRecon.V06C

#print axioms WeilDefect.MasterRecon.V06C.negative_radius_identity
#print axioms WeilDefect.MasterRecon.V06C.observed_orbit_identity
#print axioms WeilDefect.MasterRecon.V06C.positive_radius_observation
