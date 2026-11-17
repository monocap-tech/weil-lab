import WeilDefect.Arithmetic.ActualZetaOriginalEndpointOddSequence
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalStripFullGraph

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped SchwartzMap ComplexConjugate

/-! NF596: generalize the certified NF583 proof verbatim except for the amplitude bound. No numerical smallness assumption is necessary for graph convergence. -/

private theorem neutralNF596Raw_cast (h : ℝ → ℝ) (z : ℂ) :
    neutralRawTransform (fun x => (h x:ℂ)) z =
      neutralNF579RawTransform h z := by
  unfold neutralRawTransform neutralNF579RawTransform
  apply integral_congr_ae
  filter_upwards [] with x
  rw [show Complex.I*z*(x:ℂ) = Complex.I*(z*(x:ℂ)) by ring]
  

theorem neutralNF596OriginalEndpoint_actualSeedGraph_bounded
    (U : ℝ → ℝ) (hm : Measurable U) (A : ℝ) (hA : 0 ≤ A)
    (hU : ∀ x ∈ Set.Ioo ((11/10:ℝ)-1/500) (11/10:ℝ),
      |U x| ≤ A)
    (hi : Integrable (neutralNF575OriginalEndpointHalf U) volume)
    (C : ℝ) (hC : 0 ≤ C)
    (hb : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralNF579RawTransform (neutralNF575OriginalEndpointHalf U) z‖ ≤
        C*neutralNF575StripEnvelope z.re) :
    ∃ (g : ℕ → 𝓢(ℝ,ℂ))
      (K : NeutralActualZetaSourceDomain (11/10:ℝ))
      (G : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ)),
      (∀ n x, g n x = (neutralNF583Odd
        (neutralNF582HalfSequence (neutralNF575OriginalEndpointHalf U) n) x:ℂ)) ∧
      (∀ n x, conj (g n x) = g n x) ∧
      (∀ n x, g n (-x) = -g n x) ∧
      (∀ n x, x ∉ neutralNF543OriginalCollars → g n x = 0) ∧
      neutralLogPhysical (neutralActualZetaSourcePhysical (11/10:ℝ) K).val =
        (neutralNF575OriginalEndpoint_memLp U hm A hA hU).toLp (neutralNF575OriginalEndpoint U) ∧
      (∀ n, neutralLogPhysical (neutralActualZetaSourcePhysical (11/10:ℝ) (G n)).val =
        (g n).toLp 2 volume) ∧ Tendsto G atTop (nhds K) := by
  let h := neutralNF575OriginalEndpointHalf U
  have hh : ∀ x, x ∉ neutralNF578PositiveCollar → h x = 0 := by
    intro x hx
    have he : x ∉ Set.Ioo ((11/10:ℝ)-1/500) (11/10:ℝ) := by
      intro hp
      apply hx
      change (549/500:ℝ) < x ∧ x < 11/10
      constructor <;> linarith [hp.1,hp.2]
    exact if_neg he
  choose g hge hgr hgo hgs using
    fun n : ℕ => neutralNF583OddSequence_existsSchwartz h hi hh n
  have hw (n : ℕ) (x : ℝ) (hx : x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ)) :
      g n x = 0 := by
    apply hgs n x
    intro he
    apply hx
    rcases he with hl | hr
    · exact ⟨hl.1.le, by linarith [hl.2]⟩
    · exact ⟨by linarith [hr.1], hr.2.le⟩
  let f := (neutralNF575OriginalEndpoint_memLp U hm A hA hU).toLp (neutralNF575OriginalEndpoint U)
  let v := fun n => (g n).toLp 2 volume
  have hf : ∀ᵐ x ∂volume, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → f x = 0 :=
    (neutralNF575OriginalEndpoint_L2_properties U
      (neutralNF575OriginalEndpoint_memLp U hm A hA hU)).1
  have hgt (n : ℕ) : ∀ᵐ x ∂volume,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → v n x = 0 := by
    exact neutralNF581Raw_toLp_supported (11/10) (g n)
      ((g n).memLp 2 volume) (hw n)
  have htarget (z : ℂ) : neutralWindowEvaluation (11/10:ℝ) z f =
      neutralNF579RawTransform (neutralNF583Odd h) z := by
    dsimp only [f]
    rw [← neutralNF581RawTransform_toLp_window (11/10:ℝ)
      (neutralNF575OriginalEndpoint U)
      (neutralNF575OriginalEndpoint_memLp U hm A hA hU)
      (fun x hx => neutralNF575OriginalEndpoint_supported U x (by
        intro he
        apply hx
        rcases he with hl | hr
        · exact ⟨hl.1.le, by linarith [hl.2]⟩
        · exact ⟨by linarith [hr.1], hr.2.le⟩))]
    exact neutralNF596Raw_cast _ z
  have hsample (n : ℕ) (z : ℂ) : neutralWindowEvaluation (11/10:ℝ) z (v n) =
      neutralNF579RawTransform (neutralNF583Odd (neutralNF582HalfSequence h n)) z := by
    change neutralWindowEvaluation (11/10:ℝ) z (((g n).memLp 2 volume).toLp (g n)) = _
    rw [← neutralNF581RawTransform_toLp_window (11/10:ℝ)
      (g n) ((g n).memLp 2 volume) (hw n)]
    have he : (g n : ℝ → ℂ) =
        fun x => (neutralNF583Odd (neutralNF582HalfSequence h n) x:ℂ) :=
      funext (hge n)
    rw [he, neutralNF596Raw_cast]
  have hp (ξ : ℝ) : Tendsto
      (fun n => neutralWindowEvaluation (11/10:ℝ) ((-2*Real.pi*ξ:ℝ):ℂ) (v n))
      atTop (nhds (neutralWindowEvaluation (11/10:ℝ) ((-2*Real.pi*ξ:ℝ):ℂ) f)) := by
    simpa only [htarget,hsample] using
      neutralNF583OddSequence_sampleLimit h hi hh (-2*Real.pi*ξ)
  let M := 2*(Real.exp 1*C)
  have hM : 0 ≤ M := by dsimp [M]; positivity
  have hft (z : ℂ) (hz : |z.im| ≤ 1/2) :
      ‖neutralWindowEvaluation (11/10:ℝ) z f‖ ≤ M*neutralNF575StripEnvelope z.re := by
    rw [htarget]
    apply (neutralNF583Odd_strip h hi hh C hb z hz).trans
    have he : 1 ≤ Real.exp 1 := by simpa using Real.exp_le_exp.mpr (show (0:ℝ) ≤ 1 by norm_num)
    have hE : 0 ≤ neutralNF575StripEnvelope z.re := by
      unfold neutralNF575StripEnvelope
      have hl := Real.log_nonneg (show 1 ≤ 2+|z.re| by linarith [abs_nonneg z.re])
      positivity
    apply mul_le_mul_of_nonneg_right _ hE
    dsimp [M]
    nlinarith [mul_le_mul_of_nonneg_right he hC]
  have hvt (n : ℕ) (z : ℂ) (hz : |z.im| ≤ 1/2) :
      ‖neutralWindowEvaluation (11/10:ℝ) z (v n)‖ ≤ M*neutralNF575StripEnvelope z.re := by
    rw [hsample]
    exact neutralNF583OddSequence_strip h hi hh C hC hb n z hz
  obtain ⟨K,G,hK,hG,hlim⟩ :=
    neutralNF579OriginalPhysicalSequence_fullGraph_of_stripSamples f v hf hgt hp M hM hft hvt
  exact ⟨g,K,G,hge,hgr,hgo,hgs,hK,hG,hlim⟩

end
end WeilDefect
