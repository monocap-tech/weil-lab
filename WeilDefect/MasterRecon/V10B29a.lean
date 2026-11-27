import WeilDefect.MasterRecon.V10B28d
import WeilDefect.MasterRecon.V08J
import Mathlib.MeasureTheory.Function.LpSeminorm.Indicator

/-! V10B29a: realize endpoint-inclusive trials in the log carrier.
The stronger Archimedean multiplier domain is obtained from the physical
action, not assumed in the carrier lift. SeriesSupply and residual
bound remain explicit until their independent attachments are certified. -/
namespace WeilDefect.MasterRecon.V10B29a

open MeasureTheory Set Filter Complex
open scoped ENNReal FourierTransform InnerProduct ComplexConjugate
open V08I (FullL2 logWeight logCarrier physicalInclusion)
open V10B28c (trial)
open V10B23b (SeriesSupply archAction)
open V10B21c (actionTerm)

theorem trial_indicator (t : ℝ) (p : ℝ → ℂ) :
    trial t p = (Icc (-t) t).indicator (fun x => p (x+t)) := by
  funext x
  have hm : x+t ∈ Icc 0 (2*t) ↔ x ∈ Icc (-t) t := by
    simp only [mem_Icc]
    constructor <;> intro hx <;> constructor <;> linarith [hx.1,hx.2]
  unfold trial V10B24b.zeroExtend
  by_cases hx : x ∈ Icc (-t) t
  · rw [indicator_of_mem (hm.mpr hx),indicator_of_mem hx]
  · rw [indicator_of_notMem (fun h => hx (hm.mp h)),indicator_of_notMem hx]

theorem trial_mem (t B : ℝ) (p : ℝ → ℂ) (hp : Measurable p)
    (hb : ∀ x ∈ Icc 0 (2*t), ‖p x‖ ≤ B) :
    MemLp (trial t p) 2 volume := by
  rw [trial_indicator,memLp_indicator_iff_restrict measurableSet_Icc]
  letI : IsFiniteMeasure (volume.restrict (Icc (-t) t)) :=
    ⟨by rw [Measure.restrict_apply MeasurableSet.univ,univ_inter]; exact measure_Icc_lt_top⟩
  apply MemLp.of_bound (hp.comp (by fun_prop : Measurable (fun x : ℝ => x+t))).aestronglyMeasurable B
  rw [ae_restrict_iff' measurableSet_Icc]
  exact Eventually.of_forall fun x hx => hb (x+t) ⟨by linarith [hx.1],by linarith [hx.2]⟩

noncomputable def physicalTrial (t B : ℝ) (p : ℝ → ℂ) (hp : Measurable p)
    (hb : ∀ x ∈ Icc 0 (2*t), ‖p x‖ ≤ B) : FullL2 :=
  (trial_mem t B p hp hb).toLp (trial t p)

theorem physicalTrial_ae (t B : ℝ) (p : ℝ → ℂ) (hp : Measurable p)
    (hb : ∀ x ∈ Icc 0 (2*t), ‖p x‖ ≤ B) :
    (physicalTrial t B p hp hb : ℝ → ℂ) =ᵐ[volume] trial t p :=
  MemLp.coeFn_toLp (trial_mem t B p hp hb)

theorem physicalTrial_support (t B : ℝ) (p : ℝ → ℂ) (hp : Measurable p)
    (hb : ∀ x ∈ Icc 0 (2*t), ‖p x‖ ≤ B) :
    ∀ᵐ x ∂volume, x ∉ Icc (-t) t → physicalTrial t B p hp hb x = 0 := by
  filter_upwards [physicalTrial_ae t B p hp hb] with x hx
  intro hout
  rw [hx,trial_indicator,indicator_of_notMem hout]

theorem trial_action_integrable (t B K : ℝ) (ht : 0 ≤ t) (hB : 0 ≤ B) (hK : 0 ≤ K)
    (p : ℝ → ℂ) (hp : Measurable p)
    (hb : ∀ x ∈ Icc 0 (2*t), ‖p x‖ ≤ B)
    (hl : ∀ x ∈ Icc 0 (2*t), ∀ y ∈ Icc 0 (2*t), ‖p x-p y‖ ≤ K*|x-y|) :
    IntegrableOn (actionTerm (physicalTrial t B p hp hb)) (Ioi 0) := by
  apply V10B22a.supported_action_integrable (-t) t B K (by linarith) hB hK
    (fun x => p (x+t))
  · intro x hx
    exact hb _ ⟨by linarith [hx.1],by linarith [hx.2]⟩
  · intro x hx y hy
    have h := hl (x+t) ⟨by linarith [hx.1],by linarith [hx.2]⟩
      (y+t) ⟨by linarith [hy.1],by linarith [hy.2]⟩
    simpa only [show x+t-(y+t)=x-y by ring] using h
  · rw [V10B21b.supported,← trial_indicator]
    exact physicalTrial_ae t B p hp hb

theorem weight_form_integrable (f : FullL2) (hf : Integrable (fun x : ℝ => f x))
    (hD : IntegrableOn (actionTerm f) (Ioi 0)) (hS : SeriesSupply)
    (C : ℝ) (hC : ∀ u, |V10B8e.residual u| ≤ C) :
    Integrable (fun u => logWeight u * ‖(𝓕 f : FullL2) u‖^2) := by
  let F : FullL2 := 𝓕 f
  let A : FullL2 := V10B22b.U (archAction f)
  have ha : (A : ℝ → ℂ) =ᵐ[volume] fun u => (V10B8e.gammaSymbol u:ℂ)*F u :=
    V10B23b.arch_multiplier_ae f hf hD hS
  have hF : Integrable (fun u => ‖F u‖^2) :=
    (memLp_two_iff_integrable_sq_norm (Lp.aestronglyMeasurable F)).mp (Lp.memLp F)
  have hpair := (L2.integrable_inner (𝕜 := ℂ) A F).norm
  have hdom := hpair.add (hF.const_mul C)
  apply hdom.mono' (V08I.logWeight_continuous.measurable.aestronglyMeasurable.mul
    ((Lp.aestronglyMeasurable F).norm.pow 2))
  filter_upwards [ha] with u hu
  change ‖logWeight u * ‖F u‖^2‖ ≤ ‖inner ℂ (A u) (F u)‖+C*‖F u‖^2
  rw [Real.norm_eq_abs,abs_of_nonneg (mul_nonneg (V08I.logWeight_pos u).le (sq_nonneg _)),
    hu,RCLike.inner_apply',norm_mul,norm_mul,Complex.norm_conj,Complex.norm_real,Real.norm_eq_abs]
  have hr := hC u
  have hw : logWeight u ≤ |V10B8e.gammaSymbol u|+C := by
    unfold V10B8e.residual at hr
    linarith [neg_abs_le (V10B8e.gammaSymbol u-logWeight u),le_abs_self (V10B8e.gammaSymbol u)]
  have hm := mul_le_mul_of_nonneg_right hw (sq_nonneg ‖F u‖)
  nlinarith only [hm]

theorem trial_carrier_exists (t B K : ℝ) (ht : 0 ≤ t) (hB : 0 ≤ B) (hK : 0 ≤ K)
    (p : ℝ → ℂ) (hp : Measurable p)
    (hb : ∀ x ∈ Icc 0 (2*t), ‖p x‖ ≤ B)
    (hl : ∀ x ∈ Icc 0 (2*t), ∀ y ∈ Icc 0 (2*t), ‖p x-p y‖ ≤ K*|x-y|)
    (hS : SeriesSupply) (C : ℝ) (hC : ∀ u, |V10B8e.residual u| ≤ C) :
    ∃ g : logCarrier t, physicalInclusion t g = physicalTrial t B p hp hb := by
  let f := physicalTrial t B p hp hb
  have hs := physicalTrial_support t B p hp hb
  have hD := trial_action_integrable t B K ht hB hK p hp hb hl
  have hf : Integrable (fun x : ℝ => f x) := V08K.supported_integrable t f hs
  exact (V08J.physicalInclusion_range_iff t f).mpr
    ⟨hs,weight_form_integrable f hf hD hS C hC⟩

end WeilDefect.MasterRecon.V10B29a

#print axioms WeilDefect.MasterRecon.V10B29a.trial_indicator
#print axioms WeilDefect.MasterRecon.V10B29a.trial_mem
#print axioms WeilDefect.MasterRecon.V10B29a.physicalTrial_ae
#print axioms WeilDefect.MasterRecon.V10B29a.physicalTrial_support
#print axioms WeilDefect.MasterRecon.V10B29a.trial_action_integrable
#print axioms WeilDefect.MasterRecon.V10B29a.weight_form_integrable
#print axioms WeilDefect.MasterRecon.V10B29a.trial_carrier_exists
