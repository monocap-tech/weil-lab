import WeilDefect.Morphology.NeutralWeilFrozenExtension

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped BigOperators SchwartzMap FourierTransform Real

/-- Inverse Fourier translation, with the pinned mathlib sign and 2*pi convention. -/
theorem inverseFourier_sub_const (f : ℝ → ℂ) (s ξ : ℝ) :
    𝓕⁻ (fun x : ℝ => f (x - s)) ξ =
      (Real.fourierChar (s * ξ) : ℂ) * 𝓕⁻ f ξ := by
  change VectorFourier.fourierIntegral Real.fourierChar volume (-innerₗ ℝ)
    (f ∘ fun x : ℝ => x + (-s)) ξ = _
  rw [VectorFourier.fourierIntegral_comp_add_right]
  change Real.fourierChar (-(ξ * (-s))) • 𝓕⁻ f ξ = _
  rw [show -(ξ * (-s)) = s * ξ by ring]
  simp only [Circle.smul_def, smul_eq_mul]

/-- The same translation identity on the existing Schwartz-space inverse Fourier map. -/
theorem schwartz_inverseFourier_sub_const (u : SchwartzMap ℝ ℂ) (s ξ : ℝ) :
    𝓕⁻ (u.compSubConstCLM ℂ s) ξ =
      (Real.fourierChar (s * ξ) : ℂ) * 𝓕⁻ u ξ := by
  rw [SchwartzMap.fourierInv_coe]
  change 𝓕⁻ (fun x : ℝ => u (x - s)) ξ = _
  rw [inverseFourier_sub_const]
  rw [SchwartzMap.fourierInv_coe]

/-- The cosine coefficient is exactly the average of the two opposite Fourier phases. -/
theorem cosine_eq_fourierChar_pair (s ξ : ℝ) :
    (Real.cos ((2 * Real.pi * ξ) * s) : ℂ) =
      (1 / 2 : ℂ) *
        ((Real.fourierChar (s * ξ) : ℂ) +
          (Real.fourierChar ((-s) * ξ) : ℂ)) := by
  rw [← Complex.ofReal_cos]
  simp only [Complex.cos, Real.fourierChar_apply]
  push_cast
  ring_nf

/-- The transposed cosine multiplier on a Schwartz test is the symmetric translation average. -/
theorem schwartz_cosineMultiplier_transpose
    (s : ℝ) (u : SchwartzMap ℝ ℂ) :
    𝓕 (SchwartzMap.smulLeftCLM ℂ
      (fun ξ : ℝ => (Real.cos ((2 * Real.pi * ξ) * s) : ℂ)) (𝓕⁻ u)) =
      (1 / 2 : ℂ) •
        (u.compSubConstCLM ℂ s + u.compSubConstCLM ℂ (-s)) := by
  have hcos : Function.HasTemperateGrowth
      (fun ξ : ℝ => (Real.cos ((2 * Real.pi * ξ) * s) : ℂ)) := by fun_prop
  have h : SchwartzMap.smulLeftCLM ℂ
      (fun ξ : ℝ => (Real.cos ((2 * Real.pi * ξ) * s) : ℂ)) (𝓕⁻ u) =
      𝓕⁻ ((1 / 2 : ℂ) •
        (u.compSubConstCLM ℂ s + u.compSubConstCLM ℂ (-s))) := by
    ext ξ
    rw [SchwartzMap.smulLeftCLM_apply_apply hcos]
    simp only [FourierTransform.fourierInv_smul, FourierTransform.fourierInv_add,
      smul_apply, add_apply, smul_eq_mul]
    rw [schwartz_inverseFourier_sub_const, schwartz_inverseFourier_sub_const,
      cosine_eq_fourierChar_pair]
    ring
  rw [h, FourierTransform.fourier_fourierInv_eq]

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Evaluation of the L2 distribution uses the actual chosen physical representative. -/
theorem neutralPhysical_temperedMode_apply
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (u : SchwartzMap ℝ ℂ) :
    carrier.temperedMode u = ∫ x : ℝ, u x * carrier.h x ∂volume := by
  change MeasureTheory.Lp.toTemperedDistribution (carrier.h_memLp.toLp carrier.h) u = _
  rw [MeasureTheory.Lp.toTemperedDistribution_apply]
  apply integral_congr_ae
  filter_upwards [carrier.h_memLp.coeFn_toLp] with x hx
  rw [hx]
  rfl

/-- Translating a Schwartz test against an L2 carrier gives a genuine integrable product. -/
theorem neutralPhysical_shift_pairing_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (u : SchwartzMap ℝ ℂ) (s : ℝ) :
    Integrable (fun x : ℝ => u x * carrier.h (x + s)) volume := by
  have h : Integrable (fun x : ℝ => u (x - s) * carrier.h x) volume :=
    ((u.compSubConstCLM ℂ s).memLp 2 volume).integrable_mul carrier.h_memLp
  simpa only [add_sub_cancel_right] using h.comp_add_right s

/-- Change of variables transfers the test translation to the physical carrier. -/
theorem neutralPhysical_shift_pairing
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (u : SchwartzMap ℝ ℂ) (s : ℝ) :
    (∫ x : ℝ, u (x - s) * carrier.h x ∂volume) =
      ∫ x : ℝ, u x * carrier.h (x + s) ∂volume := by
  simpa only [add_sub_cancel_right] using
    (integral_add_right_eq_self (fun x : ℝ => u (x - s) * carrier.h x) s).symm

/-- Exact cosine/translation correspondence on the actual rough carrier, in weak form. -/
theorem cosineFourierMultiplier_physical_pairing
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (s : ℝ) (u : SchwartzMap ℝ ℂ) :
    TemperedDistribution.fourierMultiplierCLM ℂ
        (fun ξ : ℝ => (Real.cos ((2 * Real.pi * ξ) * s) : ℂ))
        carrier.temperedMode u =
      (1 / 2 : ℂ) *
        ((∫ x : ℝ, u x * carrier.h (x + s) ∂volume) +
          (∫ x : ℝ, u x * carrier.h (x - s) ∂volume)) := by
  rw [TemperedDistribution.fourierMultiplierCLM_apply_apply,
    schwartz_cosineMultiplier_transpose]
  simp only [map_smul, map_add, smul_eq_mul]
  rw [neutralPhysical_temperedMode_apply, neutralPhysical_temperedMode_apply]
  simp only [SchwartzMap.compSubConstCLM_apply]
  rw [neutralPhysical_shift_pairing carrier u s,
    neutralPhysical_shift_pairing carrier u (-s)]
  simp only [add_neg_eq_sub]

/-- Integrability of every weighted physical shell term against any Schwartz test. -/
theorem frozenWeilPrimeShell_term_pairing_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (u : SchwartzMap ℝ ℂ) (n : ℕ) :
    Integrable (fun x : ℝ => u x *
      ((compactWindowPrimeCoefficient n / 2 : ℝ) : ℂ) *
      (carrier.h (x - Real.log (n : ℝ)) + carrier.h (x + Real.log (n : ℝ)))) volume := by
  have hm := neutralPhysical_shift_pairing_integrable carrier u (-Real.log (n : ℝ))
  have hp := neutralPhysical_shift_pairing_integrable carrier u (Real.log (n : ℝ))
  convert (hm.add hp).const_mul ((compactWindowPrimeCoefficient n / 2 : ℝ) : ℂ) using 1
  ext x
  simp only [add_neg_eq_sub]
  ring

/-- The full finite Fourier shell is the physical translation shell on every Schwartz test.
No compact support restriction on the test is needed. -/
theorem frozenWeilPrimeShell_fourier_physical_pairing
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a b : ℝ) (u : SchwartzMap ℝ ℂ) :
    TemperedDistribution.fourierMultiplierCLM ℂ
        (fun ξ : ℝ => (frozenWeilPrimeShellSymbol a b ξ : ℂ))
        carrier.temperedMode u =
      ∫ x : ℝ, u x * frozenWeilPrimeShellPhysical carrier a b x ∂volume := by
  let g (n : ℕ) (ξ : ℝ) : ℂ :=
    (compactWindowPrimeCoefficient n : ℂ) *
      (Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ)) : ℂ)
  have hg (n : ℕ) : Function.HasTemperateGrowth (g n) := by
    dsimp [g]
    fun_prop
  have heq : (fun ξ : ℝ => (frozenWeilPrimeShellSymbol a b ξ : ℂ)) =
      ∑ n ∈ frozenWeilPrimeShell a b, g n := by
    ext ξ
    simp [frozenWeilPrimeShellSymbol, g]
  rw [heq, TemperedDistribution.fourierMultiplierCLM_sum ℂ (fun n _ => hg n)]
  simp only [Finset.sum_apply]
  have hterm (n : ℕ) :
      TemperedDistribution.fourierMultiplierCLM ℂ (g n) carrier.temperedMode u =
        ∫ x : ℝ, u x * ((compactWindowPrimeCoefficient n / 2 : ℝ) : ℂ) *
          (carrier.h (x - Real.log (n : ℝ)) + carrier.h (x + Real.log (n : ℝ)))
          ∂volume := by
    have hc : Function.HasTemperateGrowth
        (fun ξ : ℝ => (Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ)) : ℂ)) := by
      fun_prop
    change TemperedDistribution.fourierMultiplierCLM ℂ
      ((compactWindowPrimeCoefficient n : ℂ) •
        (fun ξ : ℝ => (Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ)) : ℂ)))
      carrier.temperedMode u = _
    rw [TemperedDistribution.fourierMultiplierCLM_smul hc]
    simp only [smul_apply, smul_eq_mul]
    rw [cosineFourierMultiplier_physical_pairing]
    have hm : Integrable (fun x : ℝ => u x * carrier.h (x - Real.log (n : ℝ))) volume := by
      simpa only [add_neg_eq_sub] using
        neutralPhysical_shift_pairing_integrable carrier u (-Real.log (n : ℝ))
    have hp := neutralPhysical_shift_pairing_integrable carrier u (Real.log (n : ℝ))
    have hf : (fun x : ℝ => u x * ((compactWindowPrimeCoefficient n / 2 : ℝ) : ℂ) *
        (carrier.h (x - Real.log (n : ℝ)) + carrier.h (x + Real.log (n : ℝ)))) =
        (fun x : ℝ => ((compactWindowPrimeCoefficient n / 2 : ℝ) : ℂ) *
          (u x * carrier.h (x - Real.log (n : ℝ)) + u x * carrier.h (x + Real.log (n : ℝ)))) := by
      ext x
      ring
    rw [hf, integral_const_mul, integral_add hm hp]
    push_cast
    ring
  simp_rw [hterm]
  rw [← integral_finsetSum (fun n _ => frozenWeilPrimeShell_term_pairing_integrable carrier u n)]
  apply integral_congr_ae
  filter_upwards with x
  simp [frozenWeilPrimeShellPhysical, Finset.mul_sum, mul_assoc]

/-- Genuine integrability accompanies the Fourier/physical shell identification. -/
theorem frozenWeilPrimeShell_pairing_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a b : ℝ) (u : SchwartzMap ℝ ℂ) :
    Integrable (fun x : ℝ => u x * frozenWeilPrimeShellPhysical carrier a b x) volume := by
  have h := integrable_finsetSum (frozenWeilPrimeShell a b)
    (fun n _ => frozenWeilPrimeShell_term_pairing_integrable carrier u n)
  simpa [frozenWeilPrimeShellPhysical, Finset.mul_sum, mul_assoc] using h

/-- The selected frozen actions agree on the old open window, now using the
proved Fourier/physical identification rather than a formal analogy. -/
theorem frozenWeilCompactAction_compression_eq
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    {a b : ℝ} (hab : a ≤ b) (hca : c ≤ a)
    (ha : RightLimitWeilSymbolTemperatePremise a)
    (hb : RightLimitWeilSymbolTemperatePremise b)
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u)
    (huWindow : Function.support u ⊆ Set.Ioo (-a) a) :
    frozenWeilCompactAction carrier a ha u hu =
      frozenWeilCompactAction carrier b hb u hu := by
  apply sub_eq_zero.mp
  rw [frozenWeilCompactAction_radius_correction carrier hab ha hb u hu,
    frozenWeilPrimeShell_fourier_physical_pairing,
    frozenWeilPrimeShellPhysical_pairing_zero carrier hca u huWindow]

end

end WeilDefect
