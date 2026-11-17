import WeilDefect.Arithmetic.ActualZetaOriginalStripLogCarrier
import WeilDefect.Arithmetic.ActualZetaOriginalCollar242Correction

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped ComplexConjugate

/-!
NF575: retain the exact historical NF498/NF523/NF528 endpoint
formula. Its argument U must be attached to the frozen NF494
U400 analytic source (SHA in the note); this file does not
replace U by midpoints of 400 coefficient intervals.
-/

def neutralNF575OriginalEndpointHalf (U : ℝ → ℝ) (x : ℝ) : ℝ :=
  if x ∈ Set.Ioo ((11/10:ℝ)-1/500) (11/10:ℝ) then
    (U x / 2) * Real.log ((11/10:ℝ) / ((11/10:ℝ)-x))
  else 0

def neutralNF575OriginalEndpoint (U : ℝ → ℝ) (x : ℝ) : ℂ :=
  (neutralNF575OriginalEndpointHalf U x -
    neutralNF575OriginalEndpointHalf U (-x) : ℝ)

theorem neutralNF575OriginalEndpoint_odd (U : ℝ → ℝ) (x : ℝ) :
    neutralNF575OriginalEndpoint U (-x) =
      -neutralNF575OriginalEndpoint U x := by
  unfold neutralNF575OriginalEndpoint
  rw [neg_neg]
  push_cast
  ring

theorem neutralNF575OriginalEndpoint_real (U : ℝ → ℝ) (x : ℝ) :
    conj (neutralNF575OriginalEndpoint U x) =
      neutralNF575OriginalEndpoint U x := by
  simp [neutralNF575OriginalEndpoint]

theorem neutralNF575OriginalEndpoint_supported (U : ℝ → ℝ) (x : ℝ)
    (hx : x ∉ neutralNF543OriginalCollars) :
    neutralNF575OriginalEndpoint U x = 0 := by
  have hp : x ∉ Set.Ioo ((11/10:ℝ)-1/500) (11/10:ℝ) := by
    intro h
    exact hx (Or.inr h)
  have hn : -x ∉ Set.Ioo ((11/10:ℝ)-1/500) (11/10:ℝ) := by
    intro h
    apply hx
    left
    exact ⟨by linarith [h.2], by linarith [h.1]⟩
  unfold neutralNF575OriginalEndpoint neutralNF575OriginalEndpointHalf
  rw [if_neg hp, if_neg hn]
  norm_num

/-- The logarithmic singularity itself is square integrable at
the actual endpoint. The half-source amplitude is the supplied
U(B-d)/2, not a smooth surrogate. Bounded measurable U on the
true collar suffices; this needs no first Fourier derivative. -/
theorem neutralNF581OriginalHalfAndEndpoint_memLp
    (U : ℝ → ℝ) (hm : Measurable U) (M : ℝ) (hM : 0 ≤ M)
    (hU : ∀ x ∈ Set.Ioo ((11/10:ℝ)-1/500) (11/10:ℝ), |U x| ≤ M) :
    MemLp (fun x => (neutralNF575OriginalEndpointHalf U x : ℂ)) 2 volume ∧
      MemLp (neutralNF575OriginalEndpoint U) 2 volume := by
  let B : ℝ := 11/10
  let δ : ℝ := 1/500
  let H : ℝ → ℂ := (Set.Ioo (0:ℝ) δ).indicator
    (fun d => ((U (B-d)/2)*Real.log (B/d) : ℝ))
  have hmH : Measurable H := by
    apply Measurable.indicator _ measurableSet_Ioo
    fun_prop
  have hg : IntegrableOn (fun d : ℝ => d^(-(1/2):ℝ))
      (Set.Ioo 0 δ) volume :=
    (intervalIntegral.integrableOn_Ioo_rpow_iff (by norm_num : 0 < δ)).mpr
      (by norm_num)
  have hi : Integrable (fun d => ‖H d‖^2) volume := by
    let c : ℝ := 4*M^2*B^(1/2:ℝ)
    have hmajor : Integrable ((Set.Ioo (0:ℝ) δ).indicator
        (fun d : ℝ => c*d^(-(1/2):ℝ))) volume :=
      (integrable_indicator_iff measurableSet_Ioo).mpr (hg.const_mul c)
    apply hmajor.mono' (hmH.aestronglyMeasurable.norm.pow 2)
    filter_upwards [] with d
    by_cases hd : d ∈ Set.Ioo (0:ℝ) δ
    · have hd0 : 0 < d := hd.1
      have hdB : d < B := by
        have h := hd.2
        dsimp [δ,B] at *
        linarith
      have harg : 1 ≤ B/d := (le_div_iff₀ hd0).mpr (by simpa using hdB.le)
      have hl0 : 0 ≤ Real.log (B/d) := Real.log_nonneg harg
      have hl : Real.log (B/d) ≤ 4*(B/d)^(1/4:ℝ) := by
        have h := Real.log_le_rpow_div (by positivity : 0 ≤ B/d)
          (by norm_num : 0 < (1/4:ℝ))
        linarith only [h]
      have hb : |U (B-d)| ≤ M :=
        hU (B-d) ⟨by dsimp [B] at *; linarith [hd.2],
          by dsimp [B] at *; linarith⟩
      have hnorm : ‖H d‖ ≤ (M/2)*(4*(B/d)^(1/4:ℝ)) := by
        simp only [H,Set.indicator_of_mem hd,Complex.norm_real,
          Real.norm_eq_abs,abs_mul,abs_div,abs_of_nonneg hl0,
          abs_of_nonneg (by norm_num : (0:ℝ)≤2)]
        exact mul_le_mul (div_le_div_of_nonneg_right hb (by norm_num)) hl
          hl0 (by positivity)
      have hsq := pow_le_pow_left₀ (norm_nonneg (H d)) hnorm 2
      rw [Real.norm_eq_abs,abs_of_nonneg (sq_nonneg ‖H d‖),
        Set.indicator_of_mem hd]
      calc
        _ ≤ ((M/2)*(4*(B/d)^(1/4:ℝ)))^2 := hsq
        _ = c*d^(-(1/2):ℝ) := by
          have hp : ((B/d)^(1/4:ℝ))^2 = (B/d)^(1/2:ℝ) := by
            rw [← Real.rpow_mul_natCast (by positivity : 0 ≤ B/d)]
            norm_num
          rw [mul_pow,mul_pow,hp,Real.div_rpow (by positivity : 0 ≤ B) hd0.le]
          unfold c
          rw [Real.rpow_neg hd0.le]
          ring
    · simp [H,hd]
  let h : ℝ → ℂ := fun x => (neutralNF575OriginalEndpointHalf U x : ℂ)
  have hright : h = fun x => H (B-x) := by
    funext x
    have heq : B-x ∈ Set.Ioo (0:ℝ) δ ↔
        x ∈ Set.Ioo ((11/10:ℝ)-1/500) (11/10:ℝ) := by
      simp only [Set.mem_Ioo]
      dsimp [B,δ]
      constructor <;> intro hh <;> constructor <;> linarith [hh.1,hh.2]
    by_cases hx : x ∈ Set.Ioo ((11/10:ℝ)-1/500) (11/10:ℝ)
    · dsimp only [h, H, neutralNF575OriginalEndpointHalf]
      rw [if_pos hx, Set.indicator_of_mem (heq.mpr hx), sub_sub_cancel]
      rfl
    · have hn : B-x ∉ Set.Ioo (0:ℝ) δ := fun hh => hx (heq.mp hh)
      dsimp only [h, H, neutralNF575OriginalEndpointHalf]
      rw [if_neg hx, Set.indicator_of_notMem hn]
      norm_num
  have hmright : Measurable h := by
    rw [hright]
    exact hmH.comp (measurable_const.sub measurable_id)
  have hir : Integrable (fun x => ‖h x‖^2) volume := by
    rw [hright]
    exact (integrable_comp_sub_left (fun d => ‖H d‖^2) B).mpr hi
  have hil : Integrable (fun x : ℝ => ‖h (-x)‖^2) volume := by
    simpa only [zero_sub] using
      (integrable_comp_sub_left (fun d => ‖h d‖^2) 0).mpr hir
  have hr : MemLp h 2 volume :=
    (memLp_two_iff_integrable_sq_norm hmright.aestronglyMeasurable).mpr hir
  have hh : MemLp (fun x : ℝ => h (-x)) 2 volume :=
    (memLp_two_iff_integrable_sq_norm
      (hmright.comp measurable_neg).aestronglyMeasurable).mpr hil
  have he : neutralNF575OriginalEndpoint U = fun x => h x-h (-x) := by
    funext x
    simp [neutralNF575OriginalEndpoint,h]
  refine ⟨hr, ?_⟩
  rw [he]
  exact hr.sub hh

/-- Preserve the earlier endpoint-admission interface. -/
theorem neutralNF575OriginalEndpoint_memLp
    (U : ℝ → ℝ) (hm : Measurable U) (M : ℝ) (hM : 0 ≤ M)
    (hU : ∀ x ∈ Set.Ioo ((11/10:ℝ)-1/500) (11/10:ℝ), |U x| ≤ M) :
    MemLp (neutralNF575OriginalEndpoint U) 2 volume :=
  (neutralNF581OriginalHalfAndEndpoint_memLp U hm M hM hU).2

/-- If the historical endpoint has finite physical L² norm, its
actual L² realization is supported and real a.e. No claim that an
arbitrary U (or a truncated U400 polynomial) has this membership. -/
theorem neutralNF575OriginalEndpoint_L2_properties (U : ℝ → ℝ)
    (hU : MemLp (neutralNF575OriginalEndpoint U) 2 volume) :
    (∀ᵐ x ∂volume, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
      hU.toLp (neutralNF575OriginalEndpoint U) x = 0) ∧
    (∀ᵐ x ∂volume,
      conj (hU.toLp (neutralNF575OriginalEndpoint U) x) =
        hU.toLp (neutralNF575OriginalEndpoint U) x) := by
  constructor
  · filter_upwards [hU.coeFn_toLp] with x hx houtside
    rw [hx]
    apply neutralNF575OriginalEndpoint_supported
    intro hE
    apply houtside
    rcases hE with h | h
    · exact ⟨h.1.le, by linarith [h.2]⟩
    · exact ⟨by linarith [h.1], h.2.le⟩
  · filter_upwards [hU.coeFn_toLp] with x hx
    rw [hx]
    exact neutralNF575OriginalEndpoint_real U x

/-- The SAME NF528 collar compression and mollifier margin.
With center c=B-δ/2, compressed support radius sδ/2 and
mollifier radius (1-s)δ/4, the enlarged interval is strictly
inside the authentic positive collar. -/
theorem neutralNF575OriginalCompressionMargin
    (s : ℝ) (hs : 1/2 ≤ s) (hs' : s < 1) :
    let B : ℝ := 11/10
    let δ : ℝ := 1/500
    let c := B-δ/2
    let ε := (1-s)*δ/4
    0 < ε ∧ B-δ < c-s*δ/2-ε ∧ c+s*δ/2+ε < B := by
  dsimp
  constructor
  · linarith
  constructor <;> linarith

/-- Dilation does not spend an extra logarithmic tail factor:
the actual NF528 affine compression scalar s times envelope(st)
is at most envelope(t), uniformly for 0<s≤1. -/
theorem neutralNF575StripEnvelope_dilation_le
    (s t : ℝ) (hs : 0 < s) (hs' : s ≤ 1) :
    s * neutralNF575StripEnvelope (s*t) ≤ neutralNF575StripEnvelope t := by
  have habs : |s*t| = s*|t| := by rw [abs_mul,abs_of_pos hs]
  have hlow : 0 ≤ s*|t| := by positivity
  have hle : s*|t| ≤ |t| := by nlinarith [abs_nonneg t]
  have hlog := Real.log_le_log (by positivity : 0 < 2+s*|t|)
    (by linarith : 2+s*|t| ≤ 2+|t|)
  have hnum : 0 ≤ 1+Real.log (2+|t|) := by
    have hh := Real.log_nonneg (show 1 ≤ 2+|t| by linarith [abs_nonneg t])
    linarith
  unfold neutralNF575StripEnvelope
  rw [habs]
  calc
    _ ≤ s*((1+Real.log (2+|t|))/(1+s*|t|)) :=
      mul_le_mul_of_nonneg_left (div_le_div_of_nonneg_right (by linarith only [hlog])
        (by positivity)) hs.le
    _ ≤ _ := by
      rw [← mul_div_assoc]
      apply (div_le_div_iff₀ (by positivity) (by positivity)).mpr
      have hh : s*(1+|t|) ≤ 1+s*|t| := by linarith
      nlinarith only [mul_le_mul_of_nonneg_left hh hnum]

end
end WeilDefect
