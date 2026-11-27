import WeilDefect.MasterRecon.V10B8d
import WeilDefect.MasterRecon.V08G

/-! V10B21b: zero-extension translation regularity, including the
endpoint jumps. No boundary vanishing assumption is imposed. -/
namespace WeilDefect.MasterRecon.V10B21b

open MeasureTheory Set Filter
open scoped InnerProduct
open V08I (FullL2)

noncomputable def supported (a b : ℝ) (p : ℝ → ℂ) : ℝ → ℂ :=
  (Icc a b).indicator p

noncomputable def majorant (a b B K r : ℝ) (x : ℝ) : ℝ :=
  (Icc a b).indicator (fun _ => K^2*r^2) x +
  (Icc (a-r) a).indicator (fun _ => B^2) x +
  (Icc (b-r) b).indicator (fun _ => B^2) x

theorem pointwise_translation (a b B K r : ℝ) (hr : 0 ≤ r)
    (hB : 0 ≤ B) (hK : 0 ≤ K) (p : ℝ → ℂ)
    (hb : ∀ x ∈ Icc a b, ‖p x‖ ≤ B)
    (hl : ∀ x ∈ Icc a b, ∀ y ∈ Icc a b, ‖p x-p y‖ ≤ K*|x-y|)
    (x : ℝ) :
    ‖supported a b p (x+r)-supported a b p x‖^2 ≤ majorant a b B K r x := by
  have hi (S : Set ℝ) (c : ℝ) (hc : 0 ≤ c) :
      0 ≤ S.indicator (fun _ : ℝ => c) x := by
    by_cases h : x ∈ S <;> simp [Set.indicator_of_mem,Set.indicator_of_notMem,h,hc]
  have h₁ := hi (Icc a b) (K^2*r^2) (by positivity)
  have h₂ := hi (Icc (a-r) a) (B^2) (by positivity)
  have h₃ := hi (Icc (b-r) b) (B^2) (by positivity)
  unfold supported majorant
  by_cases hx : x ∈ Icc a b <;> by_cases hy : x+r ∈ Icc a b
  · rw [indicator_of_mem hx,indicator_of_mem hy,indicator_of_mem hx]
    have h := hl (x+r) hy x hx
    rw [show x+r-x=r by ring,abs_of_nonneg hr] at h
    have hh := (sq_le_sq₀ (norm_nonneg _) (mul_nonneg hK hr)).mpr h
    rw [mul_pow] at hh
    linarith
  · rw [indicator_of_notMem hy,indicator_of_mem hx,zero_sub,norm_neg]
    have hx' : x ∈ Icc (b-r) b := by
      refine ⟨?_,hx.2⟩
      by_contra! h
      apply hy
      exact ⟨by linarith [hx.1],by linarith⟩
    rw [indicator_of_mem hx']
    have hh := (sq_le_sq₀ (norm_nonneg _) hB).mpr (hb x hx)
    linarith
  · rw [indicator_of_mem hy,indicator_of_notMem hx,sub_zero]
    have hx' : x ∈ Icc (a-r) a := by
      refine ⟨by linarith [hy.1],?_⟩
      by_contra! h
      apply hx
      exact ⟨h.le,by linarith [hy.2]⟩
    rw [indicator_of_mem hx']
    have hh := (sq_le_sq₀ (norm_nonneg _) hB).mpr (hb (x+r) hy)
    linarith
  · rw [indicator_of_notMem hx,indicator_of_notMem hy,sub_self,norm_zero,zero_pow (by decide)]
    linarith

theorem interval_indicator_integrable (a b c : ℝ) :
    Integrable ((Icc a b).indicator (fun _ : ℝ => c)) := by
  rw [integrable_indicator_iff measurableSet_Icc]
  exact integrableOn_const (measure_Icc_lt_top.ne)

theorem majorant_integral (a b B K r : ℝ) (hab : a ≤ b) (hr : 0 ≤ r) :
    (∫ x, majorant a b B K r x) = (b-a)*K^2*r^2+2*r*B^2 := by
  unfold majorant
  let F := (Icc a b).indicator (fun _ : ℝ => K^2*r^2)
  let G := (Icc (a-r) a).indicator (fun _ : ℝ => B^2)
  let H := (Icc (b-r) b).indicator (fun _ : ℝ => B^2)
  have hF : Integrable F := interval_indicator_integrable a b _
  have hG : Integrable G := interval_indicator_integrable (a-r) a _
  have hH : Integrable H := interval_indicator_integrable (b-r) b _
  change (∫ x, (F+G) x+H x) = _
  rw [integral_add (hF.add hG) hH]
  change (∫ x, F x+G x)+(∫ x,H x) = _
  rw [integral_add hF hG]
  dsimp only [F,G,H]
  simp only [integral_indicator_const _ measurableSet_Icc,Measure.real,Real.volume_Icc,
    ENNReal.toReal_ofReal (sub_nonneg.mpr hab),smul_eq_mul]
  rw [show a-(a-r)=r by ring,show b-(b-r)=r by ring,ENNReal.toReal_ofReal hr]
  ring

theorem translation_sq (a b B K r : ℝ) (hab : a ≤ b) (hr : 0 ≤ r)
    (hB : 0 ≤ B) (hK : 0 ≤ K) (p : ℝ → ℂ)
    (hb : ∀ x ∈ Icc a b, ‖p x‖ ≤ B)
    (hl : ∀ x ∈ Icc a b, ∀ y ∈ Icc a b, ‖p x-p y‖ ≤ K*|x-y|)
    (f : FullL2) (hf : (f : ℝ → ℂ) =ᵐ[volume] supported a b p) :
    ‖V10B8d.shift r f-f‖^2 ≤ (b-a)*K^2*r^2+2*r*B^2 := by
  let d := V10B8d.shift r f-f
  have hi : Integrable (fun x : ℝ => ‖d x‖^2) :=
    (memLp_two_iff_integrable_sq_norm (Lp.aestronglyMeasurable d)).mp (Lp.memLp d)
  have hm : Integrable (majorant a b B K r) :=
    ((interval_indicator_integrable a b _).add
      (interval_indicator_integrable (a-r) a _)).add (interval_indicator_integrable (b-r) b _)
  have hh : ∀ᵐ x ∂volume, ‖d x‖^2 ≤ majorant a b B K r x := by
    filter_upwards [Lp.coeFn_sub (V10B8d.shift r f) f,V10B8d.shift_ae r f,hf,
      V06D.ae_translate hf r] with x h1 h2 h3 h4
    change ‖d x‖^2 ≤ _
    change ‖((V10B8d.shift r f-f : FullL2) : ℝ → ℂ) x‖^2 ≤ _
    rw [h1]
    change ‖V10B8d.shift r f x-f x‖^2 ≤ _
    rw [h2,h3,h4]
    exact pointwise_translation a b B K r hr hB hK p hb hl x
  rw [V08G.l2_norm_sq_integral]
  exact (integral_mono_ae hi hm hh).trans_eq (majorant_integral a b B K r hab hr)

theorem translation_sqrt (a b B K r : ℝ) (hab : a ≤ b) (hr : 0 ≤ r) (hr1 : r ≤ 1)
    (hB : 0 ≤ B) (hK : 0 ≤ K) (p : ℝ → ℂ)
    (hb : ∀ x ∈ Icc a b, ‖p x‖ ≤ B)
    (hl : ∀ x ∈ Icc a b, ∀ y ∈ Icc a b, ‖p x-p y‖ ≤ K*|x-y|)
    (f : FullL2) (hf : (f : ℝ → ℂ) =ᵐ[volume] supported a b p) :
    ‖V10B8d.shift r f-f‖ ≤ Real.sqrt ((b-a)*K^2+2*B^2)*Real.sqrt r := by
  have h := translation_sq a b B K r hab hr hB hK p hb hl f hf
  have hrr : r^2 ≤ r := by nlinarith [mul_nonneg hr (sub_nonneg.mpr hr1)]
  have hh := mul_le_mul_of_nonneg_left hrr (mul_nonneg (sub_nonneg.mpr hab) (sq_nonneg K))
  apply (sq_le_sq₀ (norm_nonneg _) (by positivity)).mp
  rw [mul_pow,Real.sq_sqrt (by positivity),Real.sq_sqrt hr]
  nlinarith only [h,hh]

end WeilDefect.MasterRecon.V10B21b

#print axioms WeilDefect.MasterRecon.V10B21b.pointwise_translation
#print axioms WeilDefect.MasterRecon.V10B21b.interval_indicator_integrable
#print axioms WeilDefect.MasterRecon.V10B21b.majorant_integral
#print axioms WeilDefect.MasterRecon.V10B21b.translation_sq
#print axioms WeilDefect.MasterRecon.V10B21b.translation_sqrt
