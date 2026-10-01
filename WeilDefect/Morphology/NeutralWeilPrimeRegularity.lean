import WeilDefect.Morphology.NeutralWeilSourceDiagonal

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped BigOperators ComplexConjugate

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- The actual finite prime translations, for any retained cutoff set. -/
def neutralFinitePrimePhysical
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (S : Finset ℕ) (x : ℝ) : ℂ :=
  ∑ n ∈ S, ((compactWindowPrimeCoefficient n / 2 : ℝ) : ℂ) *
    (carrier.h (x - Real.log (n : ℝ)) + carrier.h (x + Real.log (n : ℝ)))

/-- Finite prime translations of the rough carrier are globally L1. -/
theorem neutralFinitePrimePhysical_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (S : Finset ℕ) :
    Integrable (neutralFinitePrimePhysical carrier S) volume := by
  unfold neutralFinitePrimePhysical
  apply integrable_finsetSum
  intro n hn
  exact ((neutralPhysicalRepresentative_integrable carrier).comp_sub_right
    (Real.log (n : ℝ))).add
    ((neutralPhysicalRepresentative_integrable carrier).comp_add_right
      (Real.log (n : ℝ))) |>.const_mul _

/-- Local regularity of the finite prime part needs no bounded carrier. -/
theorem neutralFinitePrimePhysical_locallyIntegrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (S : Finset ℕ) :
    LocallyIntegrable (neutralFinitePrimePhysical carrier S) volume :=
  (neutralFinitePrimePhysical_integrable carrier S).locallyIntegrable

/-- The finite prime part has an explicit compact support enclosure. -/
theorem neutralFinitePrimePhysical_zero_outside
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (S : Finset ℕ) (L : ℝ)
    (hL : ∀ n ∈ S, |Real.log (n : ℝ)| ≤ L)
    {x : ℝ} (hx : x ∉ Set.Icc (-(c + L)) (c + L)) :
    neutralFinitePrimePhysical carrier S x = 0 := by
  unfold neutralFinitePrimePhysical
  apply Finset.sum_eq_zero
  intro n hn
  have hm : carrier.h (x - Real.log (n : ℝ)) = 0 :=
    carrier.representative_eq_zero_of_not_mem (by
      intro hmem
      apply hx
      have := (abs_le.mp (hL n hn))
      constructor <;> linarith [hmem.1, hmem.2])
  have hp : carrier.h (x + Real.log (n : ℝ)) = 0 :=
    carrier.representative_eq_zero_of_not_mem (by
      intro hmem
      apply hx
      have := (abs_le.mp (hL n hn))
      constructor <;> linarith [hmem.1, hmem.2])
  rw [hm, hp, zero_add, mul_zero]

/-- Any fixed exponential weight is integrable against the finite prime norm.
This is an integral growth statement, not a pointwise exponential bound. -/
theorem neutralFinitePrimePhysical_weightedNorm_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (S : Finset ℕ) (L κ : ℝ)
    (hL : ∀ n ∈ S, |Real.log (n : ℝ)| ≤ L) :
    Integrable (fun x => ‖neutralFinitePrimePhysical carrier S x‖ *
      Real.exp (κ * |x|)) volume := by
  have hOn : IntegrableOn (fun x => ‖neutralFinitePrimePhysical carrier S x‖)
      (Set.Icc (-(c + L)) (c + L)) volume :=
    (neutralFinitePrimePhysical_integrable carrier S).norm.integrableOn
  have hCont : Continuous (fun x : ℝ => Real.exp (κ * |x|)) := by fun_prop
  exact (hOn.mul_continuousOn hCont.continuousOn isCompact_Icc).integrable_of_forall_notMem_eq_zero (fun x hx => by
      rw [neutralFinitePrimePhysical_zero_outside carrier S L hL hx,
        norm_zero, zero_mul])

/-- Every finite prime set supplies its own shift bound. No analytic growth
premise is needed for exponential-weighted norm integrability. -/
theorem neutralFinitePrimePhysical_weightedNorm_integrable_all
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (S : Finset ℕ) (κ : ℝ) :
    Integrable (fun x => ‖neutralFinitePrimePhysical carrier S x‖ *
      Real.exp (κ * |x|)) volume := by
  apply neutralFinitePrimePhysical_weightedNorm_integrable carrier S
    (∑ n ∈ S, |Real.log (n : ℝ)|) κ
  intro n hn
  exact Finset.single_le_sum (fun (m : ℕ) hm => abs_nonneg (Real.log (m : ℝ))) hn

/-- Support-gap pairing estimate for an L1 residual piece. No pointwise bound
on q is needed; the exterior test bound carries the Gaussian decay. -/
theorem integrable_pairing_of_L1_gap
    (q g : ℝ → ℂ) (a B : ℝ)
    (hq : Integrable q volume) (hg : AEStronglyMeasurable g volume)
    (hzero : ∀ x ∈ Set.Ioo (-a) a, q x = 0)
    (hB : 0 ≤ B)
    (hbound : ∀ x, x ∉ Set.Ioo (-a) a → ‖g x‖ ≤ B) :
    Integrable (fun x => conj (g x) * q x) volume ∧
      ‖∫ x, conj (g x) * q x‖ ≤ B * ∫ x, ‖q x‖ := by
  have hdom : ∀ x, ‖conj (g x) * q x‖ ≤ B * ‖q x‖ := by
    intro x
    by_cases hx : x ∈ Set.Ioo (-a) a
    · simp only [hzero x hx, mul_zero, norm_zero, le_refl]
    · rw [norm_mul, Complex.norm_conj]
      exact mul_le_mul_of_nonneg_right (hbound x hx) (norm_nonneg _)
  have hi : Integrable (fun x => conj (g x) * q x) volume :=
    (hq.norm.const_mul B).mono'
      ((Complex.continuous_conj.comp_aestronglyMeasurable hg).mul hq.aestronglyMeasurable)
      (Filter.Eventually.of_forall hdom)
  refine ⟨hi, ?_⟩
  calc
    ‖∫ x, conj (g x) * q x‖ ≤ ∫ x, ‖conj (g x) * q x‖ :=
      norm_integral_le_integral_norm _
    _ ≤ ∫ x, B * ‖q x‖ :=
      integral_mono hi.norm (hq.norm.const_mul B) hdom
    _ = B * ∫ x, ‖q x‖ := integral_const_mul _ _

/-- The already represented physical prime shell is an actual L1 function. -/
theorem frozenWeilPrimeShellPhysical_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) (a b : ℝ) :
    Integrable (frozenWeilPrimeShellPhysical carrier a b) volume :=
  neutralFinitePrimePhysical_integrable carrier (frozenWeilPrimeShell a b)

/-- Prime-shell support-gap pairing uses its actual L1 mass and no extra
regularity assumption on the carrier representative. -/
theorem frozenWeilPrimeShellPhysical_L1_gap
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a b B : ℝ) (hca : c ≤ a) (g : ℝ → ℂ)
    (hg : AEStronglyMeasurable g volume) (hB : 0 ≤ B)
    (hbound : ∀ x, x ∉ Set.Ioo (-a) a → ‖g x‖ ≤ B) :
    Integrable (fun x => conj (g x) * frozenWeilPrimeShellPhysical carrier a b x)
      volume ∧
    ‖∫ x, conj (g x) * frozenWeilPrimeShellPhysical carrier a b x‖ ≤
      B * ∫ x, ‖frozenWeilPrimeShellPhysical carrier a b x‖ := by
  exact integrable_pairing_of_L1_gap _ g a B
    (frozenWeilPrimeShellPhysical_integrable carrier a b) hg
    (fun x hx => frozenWeilPrimeShellPhysical_zero_on_window carrier hca hx)
    hB hbound

end

end WeilDefect
