import WeilDefect.Arithmetic.ActualZetaIV093OriginalRestrictedCoercivityTransferGate
import WeilDefect.Arithmetic.ActualZetaOriginalCollarCoercivity
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped ComplexConjugate SchwartzMap Topology

/-- The actual compact window diagonal has a real nonnegative paper transform
at every real frequency, with no RH assumption. -/
theorem neutralIV094WindowDiagonal_paperFT (a : ℝ) (f : RealComplexL2) (r : ℝ) :
    Zeta23.paperFT (neutralWindowCorrelation a f f) (r : ℂ) =
      ((‖neutralWindowEvaluation a (r : ℂ) f‖^2 : ℝ) : ℂ) := by
  rw [← neutralRawTransform_eq_paperFT, neutralWindowCorrelation_rawTransform,
    Complex.conj_ofReal]
  simpa only [Complex.ofReal_pow] using Complex.conj_mul' (neutralWindowEvaluation a (r : ℂ) f)

/-- The inverse representative of the original Green diagonal has the very
same pointwise real-frequency transform, by the actual raw-transform bridge. -/
theorem neutralIV094GreenDiagonal_paperFT
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients) (r : ℝ) :
    Zeta23.paperFT (neutralActualZetaGreenCorrelationInverse a v v) (r : ℂ) =
      ((‖neutralWindowEvaluation a (r : ℂ) (neutralActualZetaGreenSynthesis a v)‖^2 : ℝ) : ℂ) := by
  rw [← neutralRawTransform_eq_paperFT,
    neutralActualZetaGreenCorrelationInverse_rawTransform a ha v v,
    neutralRawTransform_eq_paperFT]
  exact neutralIV094WindowDiagonal_paperFT a _ r

/-- The omitted Gamma contribution has nonnegative real part on any
actual admissible kernel with nonnegative real paper transform.
No second-moment premise is needed for this one-sided conclusion. -/
theorem neutralIV094WeilFinite_real_le
    (M N : ℕ) (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k)
    {L : ℝ} (hL : 0 ≤ L) (hs : ∀ u, k u ≠ 0 → |u| ≤ L)
    (hM : Real.exp L < (M : ℝ))
    (hp : ∀ r : ℝ, 0 ≤ (Zeta23.paperFT k (r : ℂ)).re) :
    (neutralIV086PhysicalWeilFinite M N k).re ≤ (Zeta23.EF.literatureRHS k).re := by
  have hi := neutralIV090GammaProduct_integrable_compactC2 k hk hL hs
  have hf := neutralIV078Finite_spectral_integrable N k
    (neutralIV082Fourier_integrable_compactC2 k hk hL hs)
  have he : Integrable (neutralIV090GammaErrorIntegrand N k) := by
    apply (hi.sub hf).congr
    filter_upwards [] with r
    simp only [neutralIV090GammaErrorIntegrand, Complex.ofReal_sub, Pi.sub_apply]
    ring
  have hr : 0 ≤ (∫ r : ℝ, neutralIV090GammaErrorIntegrand N k r).re := by
    have hh := integral_re he
    change (∫ r : ℝ, (neutralIV090GammaErrorIntegrand N k r).re) =
      (∫ r : ℝ, neutralIV090GammaErrorIntegrand N k r).re at hh
    rw [← hh]
    apply integral_nonneg
    intro r
    simp only [neutralIV090GammaErrorIntegrand, Complex.mul_re,
      Complex.ofReal_re, Complex.ofReal_im, mul_zero, sub_zero]
    exact mul_nonneg (hp r) (neutralIV089GammaRemainder_bound N r).1
  have hd := congrArg Complex.re (neutralIV090WeilError_eq_integral M N k hk hL hs hM)
  have hc : ((1 / (2 * Real.pi) : ℝ) : ℂ) = (1 / (2 * Real.pi) : ℂ) := by
    push_cast <;> rfl
  rw [← hc] at hd
  simp only [Complex.sub_re, Complex.mul_re, Complex.ofReal_re,
    Complex.ofReal_im, zero_mul, sub_zero] at hd
  apply sub_nonneg.mp
  rw [hd]
  exact mul_nonneg (by positivity) hr

/-- The original finite Green diagonal is a lower approximation, not
merely an approximation with a symmetric error bar. -/
theorem neutralIV094GreenDiagonal_finite_le
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients)
    (M N : ℕ) (hM : Real.exp (2*a) < (M : ℝ)) :
    (neutralIV086PhysicalWeilFinite M N
      (neutralActualZetaGreenCorrelationInverse a v v)).re ≤
      (neutralActualZetaGreenZeroForm a v v).re := by
  have hs : ∀ u : ℝ, neutralActualZetaGreenCorrelationInverse a v v u ≠ 0 →
      |u| ≤ 2*a := by
    intro u hu
    apply abs_le.mpr
    by_contra h
    exact hu (neutralActualZetaGreenCorrelationInverse_supported a ha v v u
      (fun hmem => h ⟨hmem.1, hmem.2⟩))
  rw [neutralActualZetaGreenZeroForm_literature a ha v v]
  apply neutralIV094WeilFinite_real_le M N _
    (neutralActualZetaGreenCorrelationInverse_contDiff a ha v v)
    (show 0 ≤ 2*a by positivity) hs hM
  intro r
  rw [neutralIV094GreenDiagonal_paperFT a ha v r, Complex.ofReal_re]
  positivity

/-- Strict finite positivity transfers without a derivative-energy charge. -/
theorem neutralIV094GreenDiagonal_positive_of_finite
    (a : ℝ) (ha : 0 < a) (v : NeutralActualZetaGreenCoefficients)
    (M N : ℕ) (hM : Real.exp (2*a) < (M : ℝ))
    (hp : 0 < (neutralIV086PhysicalWeilFinite M N
      (neutralActualZetaGreenCorrelationInverse a v v)).re) :
    0 < (neutralActualZetaGreenZeroForm a v v).re :=
  hp.trans_le (neutralIV094GreenDiagonal_finite_le a ha v M N hM)

/-- Source-native finite coercivity on each nonzero original two-collar
smooth test eventually holds with half of the established NF600 margin.
The order may depend on the test; no uniform sector order is asserted. -/
theorem neutralIV094OriginalCollar_eventual_finite_margin
    (s : 𝓢(ℝ,ℂ)) (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0)
    (hne : s.toLp 2 volume ≠ 0) (M : ℕ)
    (hM : Real.exp (2*(11/10 : ℝ)) < (M : ℝ)) :
    ∀ᶠ N : ℕ in atTop,
      (1/5 : ℝ) * ‖s.toLp 2 volume‖^2 <
        (neutralIV086PhysicalWeilFinite M N
          (neutralWindowCorrelation (11/10 : ℝ) (s.toLp 2 volume)
            (s.toLp 2 volume))).re := by
  have hc : HasCompactSupport (fun x : ℝ => s x) := by
    apply HasCompactSupport.intro (K := Set.Icc (-(11/10 : ℝ)) (11/10 : ℝ)) isCompact_Icc
    intro x hx
    apply hs x
    intro hE
    apply hx
    rcases hE with hl | hh
    · exact ⟨hl.1.le, by linarith [hl.2]⟩
    · exact ⟨by linarith [hh.1], hh.2.le⟩
  have hk := neutralWindowCorrelation_contDiff_of_ae_smoothSecond
    (11/10 : ℝ) (s.toLp 2 volume) (s.toLp 2 volume)
    (fun x => s x) (s.smooth 2) hc (neutralNF573OriginalCollar_window_ae s hs)
  have ht := neutralIV086PhysicalWeilFinite_tendsto_original M _ hk
    (show 0 ≤ 2*(11/10 : ℝ) by norm_num)
    (neutralIV087WindowCorrelation_support_abs (11/10 : ℝ) _ _) hM
  have htr := Complex.continuous_re.continuousAt.tendsto.comp ht
  have hl := neutralNF600SmoothCollarLower s hs
  have hm : 0 < ‖s.toLp 2 volume‖^2 := sq_pos_of_pos (norm_pos_iff.mpr hne)
  have hstrict : (1/5 : ℝ) * ‖s.toLp 2 volume‖^2 < neutralNF598SmoothWeil s := by
    linarith
  exact htr.eventually (Ioi_mem_nhds hstrict)

#print axioms neutralIV094WindowDiagonal_paperFT
#print axioms neutralIV094GreenDiagonal_paperFT
#print axioms neutralIV094WeilFinite_real_le
#print axioms neutralIV094GreenDiagonal_finite_le
#print axioms neutralIV094GreenDiagonal_positive_of_finite
#print axioms neutralIV094OriginalCollar_eventual_finite_margin

end
end WeilDefect
