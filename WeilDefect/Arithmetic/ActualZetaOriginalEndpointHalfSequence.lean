import WeilDefect.Arithmetic.ActualZetaOriginalEndpointSeedTransform
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointScalarLimits
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointScaleSequence
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointLogGeometry

namespace WeilDefect
noncomputable section
open MeasureTheory Filter

/-!
NF582: apply the actual twist-integrability and affine/convolution
identities to the literal one-collar source, then prove a uniform
strip estimate and the fixed-frequency limit for the explicit
contraction sequence. No physical L² approximation premise.
-/

theorem neutralNF582Compressed_supported (h : ℝ → ℝ)
    (s : ℝ) (hs : 0 < s) (hs' : s < 1)
    (hh : ∀ x, x ∉ neutralNF578PositiveCollar → h x = 0)
    (x : ℝ) (hx : x ∉ neutralNF578PositiveCollar) :
    neutralNF578CompressedHalf h s x = 0 := by
  apply hh
  intro ha
  apply hx
  have hy : |(0:ℝ)| ≤ neutralNF578Epsilon s := by
    unfold neutralNF578Epsilon
    rw [abs_zero]
    linarith
  apply neutralNF578Convolution_geometry s x 0 hs hs' hy
  simpa only [sub_zero] using ha

private theorem neutralNF582Collar_abs (x : ℝ)
    (hx : x ∈ neutralNF578PositiveCollar) : |x| ≤ (11/10:ℝ) := by
  change (549/500:ℝ) < x ∧ x < 11/10 at hx
  exact abs_le.mpr ⟨by linarith [hx.1], hx.2.le⟩

theorem neutralNF582ActualHalf_transform
    (h : ℝ → ℝ) (hi : Integrable h volume)
    (hh : ∀ x, x ∉ neutralNF578PositiveCollar → h x = 0)
    (s : ℝ) (hs : 0 < s) (hs' : s < 1) (z : ℂ) :
    neutralNF579RawTransform
      (neutralNF578ConvolvedHalf h (neutralNF579Mollifier s hs') s) z =
      neutralNF579RawTransform (neutralNF579Mollifier s hs') z *
        ((s:ℂ) * Complex.exp
          (Complex.I * (z * (((1-s)*neutralNF578Center:ℝ):ℂ))) *
          neutralNF579RawTransform h ((s:ℂ)*z)) := by
  have he : 0 ≤ neutralNF578Epsilon s := by
    unfold neutralNF578Epsilon
    linarith
  have hρ := neutralNF580Twisted_integrable
    (neutralNF579Mollifier s hs') (neutralNF579Mollifier_integrable s hs')
    (neutralNF578Epsilon s) he (neutralNF579Mollifier_supported s hs') z
  have hf := neutralNF580Twisted_integrable
    (neutralNF578CompressedHalf h s) (neutralNF579CompressedHalf_integrable h hi s hs)
    (11/10) (by norm_num) (fun x hx =>
      neutralNF582Compressed_supported h s hs hs' hh x
        (fun hx' => (not_le_of_gt hx) (neutralNF582Collar_abs x hx'))) z
  rw [neutralNF579ConvolvedHalf_transform h (neutralNF579Mollifier s hs') s z hρ hf,
    neutralNF579CompressedHalf_transform h s hs z]

/-- A uniform strip majorant travels through the exact compressed
convolution. The deliberately relaxed exp(1) loss suffices for
the Hilbert/graph dominated-convergence theorem. -/
theorem neutralNF582ActualHalf_strip
    (h : ℝ → ℝ) (hi : Integrable h volume)
    (hh : ∀ x, x ∉ neutralNF578PositiveCollar → h x = 0)
    (C : ℝ) (hC : 0 ≤ C)
    (hb : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralNF579RawTransform h z‖ ≤ C * neutralNF575StripEnvelope z.re)
    (s : ℝ) (hs : 1/2 ≤ s) (hs' : s < 1)
    (z : ℂ) (hz : |z.im| ≤ 1/2) :
    ‖neutralNF579RawTransform
      (neutralNF578ConvolvedHalf h (neutralNF579Mollifier s hs') s) z‖ ≤
      (Real.exp 1 * C) * neutralNF575StripEnvelope z.re := by
  have hs0 : 0 < s := by linarith
  have hsim : ((s:ℂ)*z).im = s*z.im := by simp [Complex.mul_im]
  have hsre : ((s:ℂ)*z).re = s*z.re := by simp [Complex.mul_re]
  have hsz : |((s:ℂ)*z).im| ≤ 1/2 := by
    rw [hsim, abs_mul, abs_of_pos hs0]
    calc
      _ ≤ 1 * |z.im| := mul_le_mul_of_nonneg_right hs'.le (abs_nonneg _)
      _ ≤ _ := by simpa using hz
  have hphase :
      ‖Complex.exp (Complex.I * (z * (((1-s)*neutralNF578Center:ℝ):ℂ)))‖ ≤
        Real.exp ((1-s)*neutralNF578Center/2) := by
    rw [Complex.norm_exp]
    apply Real.exp_le_exp.mpr
    have hc : 0 ≤ (1-s)*neutralNF578Center := by
      unfold neutralNF578Center
      positivity
    have hr : (Complex.I * (z * (((1-s)*neutralNF578Center:ℝ):ℂ))).re =
        -z.im * ((1-s)*neutralNF578Center) := by
      simp [Complex.mul_re,Complex.mul_im]
      ring
    rw [hr]
    have hm := mul_le_mul_of_nonneg_right
      ((neg_le_abs z.im).trans hz) hc
    linarith
  have hm := neutralNF579Mollifier_strip s hs' z hz
  have hseed := hb ((s:ℂ)*z) hsz
  rw [hsre] at hseed
  have hscale := neutralNF575StripEnvelope_dilation_le s z.re hs0 hs'.le
  have hE : 0 ≤ neutralNF575StripEnvelope z.re := by
    unfold neutralNF575StripEnvelope
    have hl := Real.log_nonneg (show 1 ≤ 2+|z.re| by linarith [abs_nonneg z.re])
    positivity
  have hphaseSum : neutralNF578Epsilon s/2 + (1-s)*neutralNF578Center/2 ≤ 1 := by
    unfold neutralNF578Epsilon neutralNF578Center
    linarith
  rw [neutralNF582ActualHalf_transform h hi hh s hs0 hs' z,
    norm_mul,norm_mul,norm_mul,Complex.norm_real,Real.norm_eq_abs,abs_of_pos hs0]
  calc
    _ ≤ (Real.exp (neutralNF578Epsilon s/2) *
        (s * Real.exp ((1-s)*neutralNF578Center/2))) *
          (C * neutralNF575StripEnvelope (s*z.re)) := by
      gcongr
    _ = Real.exp (neutralNF578Epsilon s/2+(1-s)*neutralNF578Center/2) *
        C * (s*neutralNF575StripEnvelope (s*z.re)) := by
      rw [Real.exp_add]
      ring
    _ ≤ (Real.exp 1*C)*neutralNF575StripEnvelope z.re := by
      have hP := Real.exp_le_exp.mpr hphaseSum
      have hsc : 0 ≤ s*neutralNF575StripEnvelope (s*z.re) := by
        unfold neutralNF575StripEnvelope
        have hl := Real.log_nonneg (show 1 ≤ 2+|s*z.re| by linarith [abs_nonneg (s*z.re)])
        positivity
      exact mul_le_mul (mul_le_mul_of_nonneg_right hP hC) hscale hsc
        (mul_nonneg (Real.exp_pos _).le hC)

def neutralNF582HalfSequence (h : ℝ → ℝ) (n : ℕ) : ℝ → ℝ :=
  neutralNF578ConvolvedHalf h
    (neutralNF579Mollifier (neutralNF582Scale n) (neutralNF582Scale_lt_one n))
    (neutralNF582Scale n)

/-- Fixed real sample convergence for the actual historical
one-collar affine/mollifier sequence. -/
theorem neutralNF582ActualHalf_sampleLimit
    (h : ℝ → ℝ) (hi : Integrable h volume)
    (hh : ∀ x, x ∉ neutralNF578PositiveCollar → h x = 0) (t : ℝ) :
    Tendsto (fun n => neutralNF579RawTransform (neutralNF582HalfSequence h n) (t:ℂ))
      atTop (nhds (neutralNF579RawTransform h (t:ℂ))) := by
  let S := neutralNF582Scale
  let φ := fun n : ℕ => neutralNF579Bump (S n) (neutralNF582Scale_lt_one n)
  have hS : Tendsto S atTop (nhds 1) := neutralNF582Scale_tendsto
  have hrad : Tendsto (fun n => (φ n).rOut) atTop (nhds 0) := by
    have ho : Tendsto (fun _ : ℕ => (1:ℝ)) atTop (nhds 1) := tendsto_const_nhds
    have hd : Tendsto (fun _ : ℕ => (2000:ℝ)) atTop (nhds 2000) := tendsto_const_nhds
    simpa [φ,neutralNF579Bump,neutralNF578Epsilon] using
      (ho.sub hS).div hd (by norm_num)
  have hρ := neutralNF580NormalizedBump_sampleLimit φ hrad t
  have ht : Tendsto (fun n => S n*t) atTop (nhds t) := by
    have hc : Tendsto (fun _ : ℕ => t) atTop (nhds t) := tendsto_const_nhds
    simpa using hS.mul hc
  have hH := neutralNF580RealTransform_sampleLimit h hi (fun n => S n*t) t ht
  have hc : Continuous (fun s : ℝ => (s:ℂ) * Complex.exp
      (Complex.I * ((t:ℂ) * (((1-s)*neutralNF578Center:ℝ):ℂ)))) := by fun_prop
  have hp : Tendsto (fun n => (S n:ℂ) * Complex.exp
      (Complex.I * ((t:ℂ) * (((1-S n)*neutralNF578Center:ℝ):ℂ))))
      atTop (nhds (1:ℂ)) := by
    simpa using hc.continuousAt.tendsto.comp hS
  have hlim := hρ.mul (hp.mul hH)
  have he (n : ℕ) :
      neutralNF579RawTransform (neutralNF582HalfSequence h n) (t:ℂ) =
        neutralNF579RawTransform (neutralNF579Mollifier (S n)
          (neutralNF582Scale_lt_one n)) (t:ℂ) *
          ((S n:ℂ) * Complex.exp
            (Complex.I * ((t:ℂ) * (((1-S n)*neutralNF578Center:ℝ):ℂ))) *
            neutralNF579RawTransform h ((S n*t:ℝ):ℂ)) := by
    unfold neutralNF582HalfSequence
    rw [neutralNF582ActualHalf_transform h hi hh (S n)
      (neutralNF582Scale_pos n) (neutralNF582Scale_lt_one n)]
    push_cast
    rfl
  simpa [he,neutralNF579RawTransform,neutralNF579Mollifier,φ] using hlim

end
end WeilDefect
