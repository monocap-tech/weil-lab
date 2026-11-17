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
  simp [neutralNF575OriginalEndpoint, neutralNF575OriginalEndpointHalf,hp,hn]

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
