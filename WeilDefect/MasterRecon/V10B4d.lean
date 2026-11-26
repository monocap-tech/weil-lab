import WeilDefect.MasterRecon.V10B4c
import Mathlib.Analysis.Calculus.BumpFunction.FiniteDimension
import Mathlib.Analysis.Calculus.Deriv.Support
import Mathlib.Analysis.Calculus.ContDiff.Deriv

/-! V10B4d: actual compactly supported exponential-moment multipliers.
Uniform L¹ estimates follow from compact parameter/physical rectangles,
using joint smoothness of the partial derivatives. -/
namespace WeilDefect.MasterRecon.V10B4d

open Set MeasureTheory
open scoped ContDiff

noncomputable def cutoff (t : ℝ) (ht : 0 ≤ t) : ContDiffBump (0 : ℝ) :=
  ⟨t+1, t+2, by linarith, by linarith⟩

noncomputable def multiplier (t : ℝ) (ht : 0 ≤ t) (j : ℕ)
    (z : ℝ × ℝ) : ℂ :=
  (cutoff t ht z.2 : ℂ) * (z.2 : ℂ)^j * Complex.exp ((z.1*z.2 : ℝ) : ℂ)

theorem multiplier_on_support (t : ℝ) (ht : 0 ≤ t) (j : ℕ)
    (s x : ℝ) (hx : x ∈ Icc (-t) t) :
    multiplier t ht j (s,x) = (x : ℂ)^j * Complex.exp ((s*x : ℝ) : ℂ) := by
  have h : x ∈ Metric.closedBall (0 : ℝ) (cutoff t ht).rIn := by
    rw [Metric.mem_closedBall, Real.dist_eq, sub_zero, abs_le]
    change -(t+1) ≤ x ∧ x ≤ t+1
    exact ⟨by linarith [hx.1], by linarith [hx.2]⟩
  unfold multiplier
  rw [(cutoff t ht).one_of_mem_closedBall h]
  simp

theorem multiplier_smooth (t : ℝ) (ht : 0 ≤ t) (j : ℕ) :
    ContDiff ℝ ∞ (multiplier t ht j) := by
  unfold multiplier
  have hc : ContDiff ℝ ∞ (fun x : ℝ => (cutoff t ht x : ℂ)) :=
    Complex.ofRealCLM.contDiff.comp (cutoff t ht).contDiff
  exact ((hc.comp contDiff_snd).mul (by fun_prop)).mul (by fun_prop)

theorem multiplier_support (t : ℝ) (ht : 0 ≤ t) (j : ℕ) (s : ℝ) :
    tsupport (fun x => multiplier t ht j (s,x)) ⊆
      Metric.closedBall (0 : ℝ) (t+2) := by
  apply closure_minimal _ Metric.isClosed_closedBall
  intro x hx
  apply Metric.ball_subset_closedBall
  have hne : cutoff t ht x ≠ 0 := by
    intro h
    exact hx (by simp [multiplier, h])
  have hmem : x ∈ Function.support (cutoff t ht : ℝ → ℝ) := hne
  rw [(cutoff t ht).support_eq] at hmem
  exact hmem

noncomputable def partialY (P : ℝ × ℝ → ℂ) (z : ℝ × ℝ) : ℂ :=
  fderiv ℝ P z (0,1)

theorem partialY_smooth (P : ℝ × ℝ → ℂ) (hP : ContDiff ℝ ∞ P) :
    ContDiff ℝ ∞ (partialY P) := by
  unfold partialY
  have h := hP.fderiv_right (m := ∞) (by simp)
  exact h.clm_apply contDiff_const

theorem partialY_deriv (P : ℝ × ℝ → ℂ) (hP : ContDiff ℝ ∞ P)
    (s x : ℝ) :
    deriv (fun y => P (s,y)) x = partialY P (s,x) := by
  have hpath : HasDerivAt (fun y : ℝ => (s,y)) (0,1) x :=
    (hasDerivAt_const x s).prodMk (hasDerivAt_id x)
  have h := ((hP.differentiable (by simp) (s,x)).hasFDerivAt).comp_hasDerivAt x hpath
  exact h.deriv

/-- Compactness supplies one L¹ mass bound for a jointly continuous
family with common compact support. -/
theorem uniform_integral_norm (P : ℝ × ℝ → ℂ) (hP : Continuous P)
    (R : ℝ) (hzero : ∀ s x, s ∈ Icc (-(1/2):ℝ) (1/2) →
      x ∉ Metric.closedBall (0:ℝ) R → P (s,x) = 0) :
    ∃ A : ℝ, 0 ≤ A ∧ ∀ s ∈ Icc (-(1/2):ℝ) (1/2),
      Integrable (fun x => P (s,x)) ∧ (∫ x, ‖P (s,x)‖) ≤ A := by
  let S : Set ℝ := Icc (-(1/2):ℝ) (1/2)
  let D : Set ℝ := Metric.closedBall (0:ℝ) R
  have hD : IsCompact D := isCompact_closedBall _ _
  have hSD : IsCompact (S ×ˢ D) := isCompact_Icc.prod hD
  obtain ⟨B, hB⟩ := hSD.bddAbove_image hP.norm.continuousOn
  let C : ℝ := max B 0
  let g : ℝ → ℝ := D.indicator (fun _ => C)
  have hg : Integrable g := by
    unfold g
    rw [integrable_indicator_iff hD.isClosed.measurableSet]
    exact integrableOn_const hD.measure_lt_top.ne
  have hgn : ∀ x, 0 ≤ g x := by
    intro x
    by_cases hx : x ∈ D
    · simp [g, hx, C]
    · simp [g, hx]
  refine ⟨∫ x, g x, integral_nonneg hgn, ?_⟩
  intro s hs
  have hbound : ∀ x, ‖P (s,x)‖ ≤ g x := by
    intro x
    by_cases hx : x ∈ D
    · have hh := hB (show ‖P (s,x)‖ ∈ (fun z => ‖P z‖) '' (S ×ˢ D) from
        ⟨(s,x), ⟨hs,hx⟩, rfl⟩)
      simpa [g, hx] using hh.trans (le_max_left B 0)
    · simp [g, hx, hzero s x hs hx]
  have hi : Integrable (fun x => P (s,x)) :=
    hg.mono' (hP.comp (continuous_const.prodMk continuous_id)).aestronglyMeasurable
      (ae_of_all _ hbound)
  exact ⟨hi, integral_mono hi.norm hg hbound⟩

theorem multiplier_uniform_L1 (t : ℝ) (ht : 0 ≤ t) (j : ℕ) :
    ∃ A : ℝ, 0 ≤ A ∧ ∀ s ∈ Icc (-(1/2):ℝ) (1/2),
      Integrable (fun x => multiplier t ht j (s,x)) ∧
      (∫ x, ‖multiplier t ht j (s,x)‖) ≤ A := by
  apply uniform_integral_norm _ (multiplier_smooth t ht j).continuous (t+2)
  intro s x _ hx
  by_contra hn
  exact hx (multiplier_support t ht j s (subset_closure hn))

theorem multiplier_uniform_second_L1 (t : ℝ) (ht : 0 ≤ t) (j : ℕ) :
    ∃ B : ℝ, 0 ≤ B ∧ ∀ s ∈ Icc (-(1/2):ℝ) (1/2),
      Integrable (deriv (deriv (fun x => multiplier t ht j (s,x)))) ∧
      (∫ x, ‖deriv (deriv (fun x => multiplier t ht j (s,x))) x‖) ≤ B := by
  let P := multiplier t ht j
  have hp : ContDiff ℝ ∞ P := multiplier_smooth t ht j
  have he (s : ℝ) : deriv (deriv (fun x => P (s,x))) =
      fun x => partialY (partialY P) (s,x) := by
    have h1 : deriv (fun x => P (s,x)) = fun x => partialY P (s,x) :=
      funext (partialY_deriv P hp s)
    rw [h1]
    exact funext (partialY_deriv (partialY P) (partialY_smooth P hp) s)
  have hz : ∀ s x, s ∈ Icc (-(1/2):ℝ) (1/2) →
      x ∉ Metric.closedBall (0:ℝ) (t+2) → partialY (partialY P) (s,x) = 0 := by
    intro s x _ hx
    rw [← congrFun (he s) x]
    by_contra hn
    apply hx
    exact multiplier_support t ht j s
      (tsupport_deriv_subset (tsupport_deriv_subset (subset_closure hn)))
  obtain ⟨B,hB,hall⟩ := uniform_integral_norm _ 
    (partialY_smooth _ (partialY_smooth P hp)).continuous (t+2) hz
  refine ⟨B,hB,fun s hs => ?_⟩
  change Integrable (deriv (deriv (fun x => P (s,x)))) ∧ _
  rw [he s]
  exact hall s hs

end WeilDefect.MasterRecon.V10B4d

#print axioms WeilDefect.MasterRecon.V10B4d.multiplier_on_support
#print axioms WeilDefect.MasterRecon.V10B4d.multiplier_smooth
#print axioms WeilDefect.MasterRecon.V10B4d.multiplier_support
#print axioms WeilDefect.MasterRecon.V10B4d.partialY_smooth
#print axioms WeilDefect.MasterRecon.V10B4d.partialY_deriv
#print axioms WeilDefect.MasterRecon.V10B4d.uniform_integral_norm
#print axioms WeilDefect.MasterRecon.V10B4d.multiplier_uniform_L1
#print axioms WeilDefect.MasterRecon.V10B4d.multiplier_uniform_second_L1
