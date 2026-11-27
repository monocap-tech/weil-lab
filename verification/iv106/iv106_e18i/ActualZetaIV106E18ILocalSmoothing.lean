import WeilDefect.Arithmetic.ActualZetaIV106E18HRoughResponse
import Mathlib.Analysis.Calculus.BumpFunction.SmoothApprox

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric InnerProductSpace
open scoped SchwartzMap ContDiff ComplexConjugate

/-- The E18A unit-cell polynomial, in factored derivative coordinates. -/
def neutralIV106E18IPoly (h t : ℝ) : ℝ :=
  60*t^2*(1-t)^5 - 300*t^3*(1-t)^4 +
  300*t^4*(1-t)^3 - 60*t^5*(1-t)^2 -
  h^2/4 * (5*t^4*(1-t)^4*(1-2*t))

theorem neutralIV106E18IPoly_endpoints (h : ℝ) :
    neutralIV106E18IPoly h 0 = 0 ∧ neutralIV106E18IPoly h 1 = 0 := by
  constructor <;> simp [neutralIV106E18IPoly]

/-- Clipping the affine coordinate gives exactly the zero extension because
both endpoint values vanish. No discontinuous indicator is needed. -/
def neutralIV106E18ITrial (l h : ℝ) (x : ℝ) : ℂ :=
  (neutralIV106E18IPoly h (max 0 (min 1 ((x-l)/h))) : ℂ)

theorem neutralIV106E18ITrial_continuous (l h : ℝ) :
    Continuous (neutralIV106E18ITrial l h) := by
  unfold neutralIV106E18ITrial neutralIV106E18IPoly
  fun_prop

theorem neutralIV106E18ITrial_inside (l h : ℝ) (hh : 0 < h)
    (x : ℝ) (hx : x ∈ Set.Icc l (l+h)) :
    neutralIV106E18ITrial l h x =
      (neutralIV106E18IPoly h ((x-l)/h) : ℂ) := by
  have h0 : 0 ≤ (x-l)/h := div_nonneg (sub_nonneg.mpr hx.1) hh.le
  have h1 : (x-l)/h ≤ 1 := (div_le_iff₀ hh).mpr (by linarith [hx.2])
  simp [neutralIV106E18ITrial, min_eq_right h1, max_eq_right h0]

theorem neutralIV106E18ITrial_outside (l h : ℝ) (hh : 0 < h)
    (x : ℝ) (hx : x ∉ Set.Icc l (l+h)) :
    neutralIV106E18ITrial l h x = 0 := by
  by_cases hl : x < l
  · have h0 : (x-l)/h ≤ 0 := div_nonpos_of_nonpos_of_nonneg (by linarith) hh.le
    have h1 : (x-l)/h ≤ 1 := by linarith
    simp [neutralIV106E18ITrial, min_eq_right h1, max_eq_left h0,
      (neutralIV106E18IPoly_endpoints h).1]
  · have hr : l+h < x := by
      by_contra! hbad
      exact hx ⟨le_of_not_gt hl,hbad⟩
    have h1 : 1 ≤ (x-l)/h := (le_div_iff₀ hh).mpr (by linarith)
    simp [neutralIV106E18ITrial, min_eq_left h1,
      (neutralIV106E18IPoly_endpoints h).2]

theorem neutralIV106E18ITrial_compact (l h : ℝ) (hh : 0 < h) :
    HasCompactSupport (neutralIV106E18ITrial l h) :=
  HasCompactSupport.intro (K := Set.Icc l (l+h)) isCompact_Icc
    (neutralIV106E18ITrial_outside l h hh)

/-- Smooth uniform approximation with a fixed, slightly enlarged ball.
The cutoff is one on the original support and bounded between zero and one.
This does not require the rough input itself to have a Schwartz derivative. -/
theorem neutralIV106E18ISmooth_local (f : ℝ → ℂ) (hf : Continuous f)
    (c r R : ℝ) (hr : 0 < r) (hR : r < R)
    (hs : ∀ x ∉ closedBall c r, f x = 0)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ s : 𝓢(ℝ,ℂ), (∀ x ∉ closedBall c R, s x = 0) ∧
      ∀ x, ‖s x-f x‖ < ε := by
  have hcompact : HasCompactSupport f :=
    HasCompactSupport.intro (K := closedBall c r) (isCompact_closedBall _ _) hs
  obtain ⟨g,hg,hclose⟩ :=
    (hcompact.uniformContinuous_of_continuous hf).exists_contDiff_dist_le hε
  let φ : ContDiffBump c := ⟨r,R,hr,hR⟩
  let w : ℝ → ℂ := fun x => φ x • g x
  have hw : ContDiff ℝ ∞ w := φ.contDiff.smul hg
  have hwout : ∀ x ∉ closedBall c R, w x = 0 := by
    intro x hx
    have hz : φ x = 0 := by
      by_contra hn
      have hm : x ∈ Function.support φ := hn
      rw [φ.support_eq] at hm
      exact hx (ball_subset_closedBall hm)
    simp [w,hz]
  have hwc : HasCompactSupport w :=
    HasCompactSupport.intro (K := closedBall c R) (isCompact_closedBall _ _) hwout
  refine ⟨hwc.toSchwartzMap hw, hwout, ?_⟩
  intro x
  change ‖w x-f x‖ < ε
  have hdist : ‖g x-f x‖ < ε := by simpa [dist_eq_norm] using hclose x
  by_cases hx : x ∈ closedBall c r
  · have hφ : φ x = 1 := φ.one_of_mem_closedBall hx
    simpa [w,hφ] using hdist
  · have hzero : f x = 0 := hs x hx
    rw [hzero] at hdist ⊢
    simp only [w, sub_zero, norm_smul, Real.norm_eq_abs,
      abs_of_nonneg φ.nonneg]
    exact (mul_le_of_le_one_left (norm_nonneg _) φ.le_one).trans_lt (by simpa only [sub_zero] using hdist)

/-- The window indicator provides one fixed L2 majorant for all uniform
approximants; no Fourier regularity appears in this bound. -/
theorem neutralIV106E18IL2_error (f : ℝ → ℂ)
    (hf : MemLp f 2 volume) (s : 𝓢(ℝ,ℂ))
    (B : RealComplexL2) (ε : ℝ)
    (h : ∀ᵐ x ∂volume, ‖s x-f x‖ ≤ ε*‖B x‖) :
    ‖s.toLp 2 volume-hf.toLp f‖ ≤ ε*‖B‖ := by
  apply Lp.norm_le_mul_norm_of_ae_le_mul
  filter_upwards [h,s.coeFn_toLp 2 volume,hf.coeFn_toLp,
    Lp.coeFn_sub (s.toLp 2 volume) (hf.toLp f)] with x hx hs hf' hd
  rw [hd, Pi.sub_apply, hs, hf']
  exact hx

#print axioms neutralIV106E18IPoly_endpoints
#print axioms neutralIV106E18ITrial_continuous
#print axioms neutralIV106E18ITrial_inside
#print axioms neutralIV106E18ITrial_outside
#print axioms neutralIV106E18ITrial_compact
#print axioms neutralIV106E18ISmooth_local
#print axioms neutralIV106E18IL2_error
end
end WeilDefect
