import WeilDefect.Arithmetic.ActualZetaOriginalEndpointHalfSequence
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointSeedSchwartz

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped SchwartzMap ComplexConjugate

/-! NF583: transport the literal half sequence to the actual odd
physical endpoint. The full strip bound remains a hypothesis on
the original half, not an assumed bound on the approximants. -/

def neutralNF583Odd (h : ℝ → ℝ) : ℝ → ℝ :=
  fun x => h x - h (-x)

theorem neutralNF583Odd_transform (h : ℝ → ℝ)
    (hi : Integrable h volume)
    (hh : ∀ x, x ∉ neutralNF578PositiveCollar → h x = 0)
    (z : ℂ) :
    neutralNF579RawTransform (neutralNF583Odd h) z =
      neutralNF579RawTransform h z - neutralNF579RawTransform h (-z) := by
  have hs (x : ℝ) (hx : (11/10:ℝ) < |x|) : h x = 0 := by
    apply hh
    intro hp
    change (549/500:ℝ) < x ∧ x < 11/10 at hp
    have ha : |x| ≤ (11/10:ℝ) := abs_le.mpr ⟨by linarith [hp.1], hp.2.le⟩
    exact (not_le_of_gt hx) ha
  have h1 := neutralNF580Twisted_integrable h hi (11/10) (by norm_num) hs z
  have h2 := neutralNF580Twisted_integrable h hi (11/10) (by norm_num) hs (-z)
  let G : ℝ → ℂ := fun x => (h x:ℂ)*Complex.exp (Complex.I*((-z)*(x:ℂ)))
  have he : (fun x : ℝ => (h (-x):ℂ)*Complex.exp (Complex.I*(z*(x:ℂ)))) =
      fun x => G (-x) := by
    funext x
    dsimp [G]
    push_cast
    congr 2
    ring
  have hr : Integrable (fun x : ℝ =>
      (h (-x):ℂ)*Complex.exp (Complex.I*(z*(x:ℂ)))) volume := by
    rw [he]
    simpa only [zero_sub] using (integrable_comp_sub_left G 0).mpr h2
  unfold neutralNF579RawTransform neutralNF583Odd
  simp only [Complex.ofReal_sub,sub_mul]
  rw [integral_sub h1 hr, he]
  have hneg : (∫ x : ℝ, G (-x)) = ∫ x : ℝ, G x := by
    simpa only [zero_sub] using integral_sub_left_eq_self G volume (0:ℝ)
  rw [hneg]

theorem neutralNF583Odd_strip (h : ℝ → ℝ)
    (hi : Integrable h volume)
    (hh : ∀ x, x ∉ neutralNF578PositiveCollar → h x = 0)
    (C : ℝ)
    (hb : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralNF579RawTransform h z‖ ≤ C * neutralNF575StripEnvelope z.re)
    (z : ℂ) (hz : |z.im| ≤ 1/2) :
    ‖neutralNF579RawTransform (neutralNF583Odd h) z‖ ≤
      (2*C)*neutralNF575StripEnvelope z.re := by
  have hn : |(-z).im| ≤ 1/2 := by simpa only [Complex.neg_im,abs_neg] using hz
  have hE : neutralNF575StripEnvelope (-z).re = neutralNF575StripEnvelope z.re := by
    simp only [neutralNF575StripEnvelope,Complex.neg_re,abs_neg]
  rw [neutralNF583Odd_transform h hi hh z]
  calc
    _ ≤ ‖neutralNF579RawTransform h z‖ + ‖neutralNF579RawTransform h (-z)‖ :=
      norm_sub_le _ _
    _ ≤ C*neutralNF575StripEnvelope z.re+C*neutralNF575StripEnvelope z.re := by
      have h := hb (-z) hn
      rw [hE] at h
      exact add_le_add (hb z hz) h
    _ = _ := by ring

theorem neutralNF583HalfSequence_supported (h : ℝ → ℝ)
    (hh : ∀ x, x ∉ neutralNF578PositiveCollar → h x = 0)
    (n : ℕ) (x : ℝ) (hx : x ∉ neutralNF578PositiveCollar) :
    neutralNF582HalfSequence h n x = 0 :=
  neutralNF578ConvolvedHalf_supported h
    (neutralNF579Mollifier (neutralNF582Scale n) (neutralNF582Scale_lt_one n))
    (neutralNF582Scale n) x (neutralNF582Scale_pos n)
    (neutralNF582Scale_lt_one n) hh
    (neutralNF579Mollifier_supported (neutralNF582Scale n)
      (neutralNF582Scale_lt_one n)) hx

theorem neutralNF583HalfSequence_integrable (h : ℝ → ℝ)
    (hi : Integrable h volume) (n : ℕ) :
    Integrable (neutralNF582HalfSequence h n) volume := by
  let s := neutralNF582Scale n
  let ρ := neutralNF579Mollifier s (neutralNF582Scale_lt_one n)
  change Integrable (MeasureTheory.convolution ρ
    (neutralNF578CompressedHalf h s) (ContinuousLinearMap.mul ℝ ℝ) volume) volume
  exact (neutralNF579Mollifier_integrable s (neutralNF582Scale_lt_one n)).integrable_convolution
    (ContinuousLinearMap.mul ℝ ℝ)
    (neutralNF579CompressedHalf_integrable h hi s (neutralNF582Scale_pos n))

/-- Complete odd transform convergence, with no independent physical
or logarithmic norm approximation premise. -/
theorem neutralNF583OddSequence_sampleLimit
    (h : ℝ → ℝ) (hi : Integrable h volume)
    (hh : ∀ x, x ∉ neutralNF578PositiveCollar → h x = 0) (t : ℝ) :
    Tendsto (fun n => neutralNF579RawTransform
      (neutralNF583Odd (neutralNF582HalfSequence h n)) (t:ℂ))
      atTop (nhds (neutralNF579RawTransform (neutralNF583Odd h) (t:ℂ))) := by
  have hp := neutralNF582ActualHalf_sampleLimit h hi hh t
  have hn := neutralNF582ActualHalf_sampleLimit h hi hh (-t)
  have he (n : ℕ) := neutralNF583Odd_transform (neutralNF582HalfSequence h n)
    (neutralNF583HalfSequence_integrable h hi n)
    (neutralNF583HalfSequence_supported h hh n) (t:ℂ)
  rw [neutralNF583Odd_transform h hi hh]
  simpa only [he,Complex.ofReal_neg] using hp.sub hn

theorem neutralNF583OddSequence_strip
    (h : ℝ → ℝ) (hi : Integrable h volume)
    (hh : ∀ x, x ∉ neutralNF578PositiveCollar → h x = 0)
    (C : ℝ) (hC : 0 ≤ C)
    (hb : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralNF579RawTransform h z‖ ≤ C*neutralNF575StripEnvelope z.re)
    (n : ℕ) (z : ℂ) (hz : |z.im| ≤ 1/2) :
    ‖neutralNF579RawTransform (neutralNF583Odd (neutralNF582HalfSequence h n)) z‖ ≤
      (2*(Real.exp 1*C))*neutralNF575StripEnvelope z.re := by
  apply neutralNF583Odd_strip _ (neutralNF583HalfSequence_integrable h hi n)
    (neutralNF583HalfSequence_supported h hh n) (Real.exp 1*C) _ z hz
  intro w hw
  exact neutralNF582ActualHalf_strip h hi hh C hC hb
    (neutralNF582Scale n) (neutralNF582Scale_half_le n)
    (neutralNF582Scale_lt_one n) w hw

/-- The actual sequence is exactly the earlier pointwise-real odd
Schwartz seed; no alternate physical approximation is selected. -/
theorem neutralNF583OddSequence_existsSchwartz
    (h : ℝ → ℝ) (hi : Integrable h volume)
    (hh : ∀ x, x ∉ neutralNF578PositiveCollar → h x = 0) (n : ℕ) :
    ∃ g : 𝓢(ℝ,ℂ),
      (∀ x, g x = (neutralNF583Odd (neutralNF582HalfSequence h n) x:ℂ)) ∧
      (∀ x, conj (g x) = g x) ∧
      (∀ x, g (-x) = -g x) ∧
      (∀ x, x ∉ neutralNF543OriginalCollars → g x = 0) :=
  neutralNF581Seed_existsSchwartz h hi (neutralNF582Scale n)
    (neutralNF582Scale_pos n) (neutralNF582Scale_lt_one n) hh

end
end WeilDefect
