import WeilDefect.Arithmetic.ActualZetaIV106E18SControlledPrimitive

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric
open scoped SchwartzMap ContDiff

/-- Normalize a single supported Schwartz bump, using its actual integral.
Existence of a nonzero-mass bump is kept separate from the correction. -/
theorem neutralIV106E18TNormalize (p : 𝓢(ℝ,ℂ)) (A B : ℝ)
    (hout : ∀ x, x ≤ A ∨ B ≤ x → p x = 0)
    (hm : (∫ x in A..B, p x) ≠ 0) :
    ∃ ρ : 𝓢(ℝ,ℂ), (∀ x, x ≤ A ∨ B ≤ x → ρ x = 0) ∧
      (∫ x in A..B, ρ x) = 1 := by
  let m : ℂ := ∫ x in A..B, p x
  let ρ : 𝓢(ℝ,ℂ) := m⁻¹ • p
  refine ⟨ρ, ?_, ?_⟩
  · intro x hx
    change m⁻¹ * p x = 0
    rw [hout x hx, mul_zero]
  · change (∫ x in A..B, m⁻¹ * p x) = 1
    rw [intervalIntegral.integral_const_mul]
    exact inv_mul_cancel₀ hm

/-- Exact mass correction with a fixed normalized bump. The loss is
linear in the raw uniform error, independent of the approximation index. -/
theorem neutralIV106E18TMass_correct
    (df : ℝ → ℂ) (hdf : Continuous df) (A B : ℝ) (hAB : A < B)
    (hm : (∫ x in A..B, df x) = 0)
    (q ρ : 𝓢(ℝ,ℂ))
    (hqout : ∀ x, x ≤ A ∨ B ≤ x → q x = 0)
    (hρout : ∀ x, x ≤ A ∨ B ≤ x → ρ x = 0)
    (hρmass : (∫ x in A..B, ρ x) = 1)
    (M η : ℝ) (hM : 0 ≤ M) (hη : 0 ≤ η)
    (hρbound : ∀ x, ‖ρ x‖ ≤ M)
    (hclose : ∀ x, ‖q x-df x‖ ≤ η) :
    ∃ g : 𝓢(ℝ,ℂ), (∀ x, x ≤ A ∨ B ≤ x → g x = 0) ∧
      (∫ x in A..B, g x) = 0 ∧
      (∀ x, ‖g x-df x‖ ≤ η*(1+(B-A)*M)) := by
  let m : ℂ := ∫ x in A..B, q x
  let g : 𝓢(ℝ,ℂ) := q - m • ρ
  have hmass : ‖m‖ ≤ η*(B-A) := by
    have he : (∫ x in A..B, q x-df x) = m := by
      rw [intervalIntegral.integral_sub (q.continuous.intervalIntegrable A B)
        (hdf.intervalIntegrable A B), hm, sub_zero]
    rw [← he]
    have hb : ‖∫ x in A..B, q x-df x‖ ≤ η*|B-A| :=
      intervalIntegral.norm_integral_le_of_norm_le_const (fun x _ => hclose x)
    simpa only [abs_of_nonneg (sub_nonneg.mpr hAB.le)] using hb
  refine ⟨g, ?_, ?_, ?_⟩
  · intro x hx
    change q x-m*ρ x = 0
    rw [hqout x hx, hρout x hx, mul_zero, sub_zero]
  · change (∫ x in A..B, q x-m*ρ x) = 0
    have hi : IntervalIntegrable (fun x : ℝ => m * ρ x) volume A B := by
      exact (continuous_const.mul ρ.continuous).intervalIntegrable A B
    have he := intervalIntegral.integral_sub (q.continuous.intervalIntegrable A B) hi
    change (∫ x in A..B, q x - m * ρ x) =
      (∫ x in A..B, q x) - (∫ x in A..B, m * ρ x) at he
    rw [he, intervalIntegral.integral_const_mul, hρmass, mul_one]
    exact sub_self m
  · intro x
    change ‖q x-m*ρ x-df x‖ ≤ _
    rw [show q x-m*ρ x-df x = (q x-df x)-m*ρ x by ring]
    calc
      _ ≤ ‖q x-df x‖ + ‖m*ρ x‖ := norm_sub_le _ _
      _ ≤ η+(η*(B-A))*M := by
        rw [norm_mul]
        exact add_le_add (hclose x)
          (mul_le_mul hmass (hρbound x) (norm_nonneg _) (mul_nonneg hη (sub_nonneg.mpr hAB.le)))
      _ = _ := by ring

/-- Simultaneous uniform approximation of the actual trial and its
actual physical derivative on a fixed buffered interval. A normalized
bump and its fixed sup bound are explicit inputs, not hidden assumptions. -/
theorem neutralIV106E18TTrial_approx
    (l h ε : ℝ) (hh : 0 < h) (hε : 0 < ε)
    (ρ : 𝓢(ℝ,ℂ))
    (hρout : ∀ x, x ≤ l-ε ∨ l+h+ε ≤ x → ρ x = 0)
    (hρmass : (∫ x in (l-ε)..(l+h+ε), ρ x) = 1)
    (M η : ℝ) (hM : 0 ≤ M) (hη : 0 < η)
    (hρbound : ∀ x, ‖ρ x‖ ≤ M) :
    ∃ s : 𝓢(ℝ,ℂ), (∀ x ∉ Icc (l-ε) (l+h+ε), s x = 0) ∧
      (∀ x, ‖s x-neutralIV106E18ITrial l h x‖ ≤
        (η*(1+(l+h+ε-(l-ε))*M))*(l+h+ε-(l-ε))) ∧
      (∀ x, ‖SchwartzMap.derivCLM ℂ ℂ s x-neutralIV106E18SDTrial l h x‖ ≤
        η*(1+(l+h+ε-(l-ε))*M)) := by
  have hAB : l-ε < l+h+ε := by linarith
  have hdout : ∀ x ∉ closedBall (l+h/2) (h/2), neutralIV106E18SDTrial l h x = 0 := by
    intro x hx
    apply neutralIV106E18SDTrial_outside l h hh x
    intro hx'
    apply hx
    rw [mem_closedBall, Real.dist_eq, abs_le]
    constructor <;> linarith [hx'.1,hx'.2]
  obtain ⟨q,hqout,hqclose⟩ := neutralIV106E18ISmooth_local
    (neutralIV106E18SDTrial l h) (neutralIV106E18SDTrial_continuous l h)
    (l+h/2) (h/2) (h/2+ε/2) (by positivity) (by linarith) hdout η hη
  have hqout' : ∀ x, x ≤ l-ε ∨ l+h+ε ≤ x → q x = 0 := by
    intro x hx
    apply hqout x
    intro hb
    rw [mem_closedBall, Real.dist_eq, abs_le] at hb
    rcases hx with hl | hr <;> linarith [hb.1,hb.2]
  obtain ⟨g,hgout,hgm,hgclose⟩ := neutralIV106E18TMass_correct
    (neutralIV106E18SDTrial l h) (neutralIV106E18SDTrial_continuous l h)
    (l-ε) (l+h+ε) hAB
    (neutralIV106E18STrial_derivative_mass l h (l-ε) (l+h+ε) hh (by linarith) (by linarith))
    q ρ hqout' hρout hρmass M η hM hη.le hρbound (fun x => (hqclose x).le)
  exact neutralIV106E18SPrimitive_error
    (neutralIV106E18ITrial l h) (neutralIV106E18SDTrial l h)
    (neutralIV106E18SDTrial_continuous l h) (neutralIV106E18STrial_derivative l h hh)
    (l-ε) (l+h+ε) hAB
    (neutralIV106E18ITrial_outside l h hh _ (by intro hx; linarith [hx.1]))
    (fun x hx => neutralIV106E18ITrial_outside l h hh x
      (fun hi => hx ⟨by linarith [hi.1], by linarith [hi.2]⟩))
    g hgout hgm _ (mul_nonneg hη.le (by positivity)) hgclose

#print axioms neutralIV106E18TNormalize
#print axioms neutralIV106E18TMass_correct
#print axioms neutralIV106E18TTrial_approx
end
end WeilDefect
