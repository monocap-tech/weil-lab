import WeilDefect.Arithmetic.ActualZetaIV106E18STrialDerivative
import Mathlib.Analysis.Calculus.ContDiff.Deriv
import Mathlib.Analysis.Calculus.BumpFunction.Normed

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric
open scoped SchwartzMap ContDiff

/-- A zero-integral smooth derivative supported strictly inside [A,B]
has a compact smooth primitive with precisely that derivative. -/
theorem neutralIV106E18SPrimitive (g : 𝓢(ℝ,ℂ)) (A B : ℝ) (hAB : A < B)
    (hout : ∀ x, x ≤ A ∨ B ≤ x → g x = 0)
    (hm : (∫ x in A..B, g x) = 0) :
    ∃ s : 𝓢(ℝ,ℂ), (∀ x ∉ Icc A B, s x = 0) ∧
      (∀ x, s x = ∫ t in A..x, g t) ∧
      SchwartzMap.derivCLM ℂ ℂ s = g := by
  let F : ℝ → ℂ := fun x => ∫ t in A..x, g t
  have hc := g.continuous
  have hd (x : ℝ) : HasDerivAt F (g x) x :=
    intervalIntegral.integral_hasDerivAt_right (hc.intervalIntegrable _ _)
      hc.aestronglyMeasurable.stronglyMeasurableAtFilter hc.continuousAt
  have hF : ContDiff ℝ ∞ F := by
    apply contDiff_infty_iff_deriv.mpr
    refine ⟨fun x => (hd x).differentiableAt,?_⟩
    rw [show deriv F = (g:ℝ→ℂ) from funext fun x => (hd x).deriv]
    exact g.smooth ⊤
  have hzeroL (x : ℝ) (hx : x ≤ A) : F x = 0 := by
    dsimp [F]
    rw [show (∫ t in A..x,g t) = ∫ t in A..x,(0:ℂ) by
      apply intervalIntegral.integral_congr
      intro t ht
      rw [uIcc_of_ge hx] at ht
      exact hout t (Or.inl ht.2)]
    simp
  have hzeroR (x : ℝ) (hx : B ≤ x) : F x = 0 := by
    have he : (∫ t in B..x,g t) = 0 := by
      rw [show (∫ t in B..x,g t) = ∫ t in B..x,(0:ℂ) by
        apply intervalIntegral.integral_congr
        intro t ht
        rw [uIcc_of_le hx] at ht
        exact hout t (Or.inr ht.1)]
      simp
    dsimp [F]
    rw [← intervalIntegral.integral_add_adjacent_intervals
      (hc.intervalIntegrable A B) (hc.intervalIntegrable B x),hm,he,add_zero]
  have hFout : ∀ x ∉ Icc A B, F x = 0 := by
    intro x hx
    by_cases h : x ≤ A
    · exact hzeroL x h
    · exact hzeroR x (by
        by_contra! hh
        exact hx ⟨le_of_not_ge h,hh.le⟩)
  have hcomp : HasCompactSupport F :=
    HasCompactSupport.intro (K := Icc A B) isCompact_Icc hFout
  let s := hcomp.toSchwartzMap hF
  refine ⟨s,hFout,fun _ => rfl,?_⟩
  ext x
  exact (hd x).deriv

/-- Uniform control of a primitive follows from uniform control of the
derivative, on a single fixed interval. No log norm is estimated from
physical L2 approximation alone. -/
theorem neutralIV106E18SPrimitive_error (f df : ℝ → ℂ)
    (hdf : Continuous df) (hd : ∀ x, HasDerivAt f (df x) x)
    (A B : ℝ) (hAB : A < B) (hfA : f A = 0)
    (hfout : ∀ x ∉ Icc A B, f x = 0)
    (g : 𝓢(ℝ,ℂ)) (hout : ∀ x, x ≤ A ∨ B ≤ x → g x = 0)
    (hm : (∫ x in A..B, g x) = 0) (η : ℝ) (hη : 0 ≤ η)
    (hclose : ∀ x, ‖g x-df x‖ ≤ η) :
    ∃ s : 𝓢(ℝ,ℂ), (∀ x ∉ Icc A B, s x = 0) ∧
      (∀ x, ‖s x-f x‖ ≤ η*(B-A)) ∧
      (∀ x, ‖SchwartzMap.derivCLM ℂ ℂ s x-df x‖ ≤ η) := by
  obtain ⟨s,hs,hprim,hderiv⟩ := neutralIV106E18SPrimitive g A B hAB hout hm
  refine ⟨s,hs,?_,?_⟩
  · intro x
    by_cases hx : x ∈ Icc A B
    · rw [hprim]
      have hf : (∫ t in A..x, df t) = f x := by
        rw [intervalIntegral.integral_eq_sub_of_hasDerivAt (fun t _ => hd t)
          (hdf.intervalIntegrable A x),hfA,sub_zero]
      rw [← hf,← intervalIntegral.integral_sub
        (g.continuous.intervalIntegrable A x) (hdf.intervalIntegrable A x)]
      calc
        _ ≤ η*|x-A| := intervalIntegral.norm_integral_le_of_norm_le_const
          (fun t _ => hclose t)
        _ ≤ _ := by
          rw [abs_of_nonneg (sub_nonneg.mpr hx.1)]
          exact mul_le_mul_of_nonneg_left (sub_le_sub_right hx.2 A) hη
    · rw [hs x hx,hfout x hx,sub_zero,norm_zero]
      exact mul_nonneg hη (sub_nonneg.mpr hAB.le)
  · intro x
    rw [hderiv]
    exact hclose x

/-- Actual derivative zero-integral identity: the compact trial returns
to the same zero boundary value. -/
theorem neutralIV106E18STrial_derivative_mass (l h A B : ℝ) (hh : 0 < h)
    (hA : A < l) (hB : l+h < B) :
    (∫ x in A..B, neutralIV106E18SDTrial l h x) = 0 := by
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt
    (fun x _ => neutralIV106E18STrial_derivative l h hh x)
    ((neutralIV106E18SDTrial_continuous l h).intervalIntegrable A B)]
  rw [neutralIV106E18ITrial_outside l h hh A (by intro hx; linarith [hx.1]),
    neutralIV106E18ITrial_outside l h hh B (by intro hx; linarith [hx.2]),sub_zero]

#print axioms neutralIV106E18SPrimitive
#print axioms neutralIV106E18SPrimitive_error
#print axioms neutralIV106E18STrial_derivative_mass
end
end WeilDefect
