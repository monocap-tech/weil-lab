import WeilDefect.Morphology.NeutralWeilSourceWindowAttachment

namespace WeilDefect

noncomputable section

open scoped BigOperators SchwartzMap FourierTransform

/--
Equality-threshold prime powers: those retained by the strict-right `≤`
operator but absent from the pinned source's strict `<` compact-window sum.
-/
def rightLimitThresholdFinset (a : ℝ) : Finset ℕ :=
  rightLimitPrimePowerFinset a \ activePrimePowerFinset a

@[simp]
theorem mem_rightLimitThresholdFinset
    (a : ℝ) (n : ℕ) :
    n ∈ rightLimitThresholdFinset a ↔
      IsPrimePow n ∧ Real.log (n : ℝ) = 2 * a := by
  rw [rightLimitThresholdFinset, Finset.mem_sdiff,
    mem_rightLimitPrimePowerFinset]
  constructor
  · rintro ⟨⟨hnpp, hnle⟩, hnactive⟩
    have hnlt : ¬ Real.log (n : ℝ) < 2 * a := by
      intro hlt
      exact hnactive ((mem_activePrimePowerFinset a n).2 ⟨hnpp, hlt⟩)
    exact ⟨hnpp, le_antisymm hnle (le_of_not_gt hnlt)⟩
  · rintro ⟨hnpp, hneq⟩
    refine ⟨⟨hnpp, hneq.le⟩, ?_⟩
    intro hnactive
    have hlt := ((mem_activePrimePowerFinset a n).1 hnactive).2
    rw [hneq] at hlt
    exact (lt_irrefl (2 * a)) hlt

/-- The equality-threshold Finset contains at most one prime power. -/
theorem rightLimitThresholdFinset_subsingleton (a : ℝ) :
    (↑(rightLimitThresholdFinset a) : Set ℕ).Subsingleton := by
  intro m hm n hn
  apply primePowerThreshold_subsingleton a
  · exact (mem_rightLimitThresholdFinset a m).1 hm
  · exact (mem_rightLimitThresholdFinset a n).1 hn

/-- Every strict-source prime is retained by the right-limit prime set. -/
theorem activePrimePowerFinset_subset_rightLimit (a : ℝ) :
    activePrimePowerFinset a ⊆ rightLimitPrimePowerFinset a := by
  intro n hn
  exact active_mem_rightLimitPrimePowerFinset hn

/-- Pinned-source strict prime trigonometric sum in source frequency. -/
def strictSourcePrimeSymbol (a t : ℝ) : ℝ :=
  ∑ n ∈ activePrimePowerFinset a,
    compactWindowPrimeCoefficient n *
      Real.cos (t * Real.log (n : ℝ))

/-- Pinned-source strict compact-window scalar symbol in source frequency. -/
def strictSourceCompactWeilSymbol (a t : ℝ) : ℝ :=
  compactWindowArchimedeanSymbol t - strictSourcePrimeSymbol a t

/-- Pinned-source strict compact-window scalar symbol in mathlib frequency. -/
def strictSourceCompactWeilSymbolMathlib (a ξ : ℝ) : ℝ :=
  strictSourceCompactWeilSymbol a (2 * Real.pi * ξ)

/-- Equality-threshold correction in mathlib frequency. -/
def rightLimitThresholdPrimeSymbolMathlib (a ξ : ℝ) : ℝ :=
  ∑ n ∈ rightLimitThresholdFinset a,
    compactWindowPrimeCoefficient n *
      Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ))

/--
The threshold correction is exactly the difference between the right-limit
prime sum and the pinned source's strict prime sum.
-/
theorem rightLimitThresholdPrimeSymbolMathlib_eq
    (a ξ : ℝ) :
    rightLimitThresholdPrimeSymbolMathlib a ξ =
      (∑ n ∈ rightLimitPrimePowerFinset a,
        compactWindowPrimeCoefficient n *
          Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ)))
      -
      (∑ n ∈ activePrimePowerFinset a,
        compactWindowPrimeCoefficient n *
          Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ))) := by
  unfold rightLimitThresholdPrimeSymbolMathlib rightLimitThresholdFinset
  rw [Finset.sum_sdiff_eq_sub
    (activePrimePowerFinset_subset_rightLimit a)]

/--
Exact source/right-limit symbol conversion.

The project right-limit symbol equals the pinned strict source symbol minus the
at-most-one equality-threshold prime contribution.
-/
theorem rightLimitCompactWeilSymbolMathlib_eq_strictSource_sub_threshold
    (a ξ : ℝ) :
    rightLimitCompactWeilSymbolMathlib a ξ =
      strictSourceCompactWeilSymbolMathlib a ξ -
        rightLimitThresholdPrimeSymbolMathlib a ξ := by
  rw [rightLimitCompactWeilSymbolMathlib_eq,
    rightLimitThresholdPrimeSymbolMathlib_eq]
  unfold strictSourceCompactWeilSymbolMathlib
    strictSourceCompactWeilSymbol strictSourcePrimeSymbol
  ring

/-- Away from an equality threshold the source and right-limit symbols agree. -/
theorem rightLimitCompactWeilSymbolMathlib_eq_strictSource_of_no_threshold
    {a : ℝ}
    (hthreshold : rightLimitThresholdFinset a = ∅)
    (ξ : ℝ) :
    rightLimitCompactWeilSymbolMathlib a ξ =
      strictSourceCompactWeilSymbolMathlib a ξ := by
  rw [rightLimitCompactWeilSymbolMathlib_eq_strictSource_sub_threshold]
  simp [rightLimitThresholdPrimeSymbolMathlib, hthreshold]

/--
The threshold correction is a temperate multiplier.  It is finite and
trigonometric; no extra source asymptotic is needed.
-/
theorem rightLimitThresholdPrimeSymbolMathlib_hasTemperateGrowth
    (a : ℝ) :
    Function.HasTemperateGrowth
      (fun ξ : ℝ => (rightLimitThresholdPrimeSymbolMathlib a ξ : ℂ)) := by
  unfold rightLimitThresholdPrimeSymbolMathlib
  fun_prop

/--
The strict source symbol inherits temperate growth from the certified
right-limit symbol plus the explicit finite threshold correction.
-/
theorem strictSourceCompactWeilSymbolMathlib_hasTemperateGrowth
    (a : ℝ)
    (hRight : RightLimitWeilSymbolTemperatePremise a) :
    Function.HasTemperateGrowth
      (fun ξ : ℝ => (strictSourceCompactWeilSymbolMathlib a ξ : ℂ)) := by
  have hthreshold :=
    rightLimitThresholdPrimeSymbolMathlib_hasTemperateGrowth a
  have heq :
      (fun ξ : ℝ => (strictSourceCompactWeilSymbolMathlib a ξ : ℂ)) =
        (fun ξ : ℝ => (rightLimitCompactWeilSymbolMathlib a ξ : ℂ)) +
          (fun ξ : ℝ => (rightLimitThresholdPrimeSymbolMathlib a ξ : ℂ)) := by
    funext ξ
    simp only [Pi.add_apply]
    have hreal :
        strictSourceCompactWeilSymbolMathlib a ξ =
          rightLimitCompactWeilSymbolMathlib a ξ +
            rightLimitThresholdPrimeSymbolMathlib a ξ := by
      have h :=
        rightLimitCompactWeilSymbolMathlib_eq_strictSource_sub_threshold a ξ
      linarith
    exact_mod_cast hreal
  rw [heq]
  exact hRight.hasTemperateGrowth.add hthreshold

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

/-- Strict-source multiplier core, using the source's literal prime cutoff `log n < 2a`. -/
noncomputable def strictSourceWeilMultiplierCore
    (a : ℝ) (hRight : RightLimitWeilSymbolTemperatePremise a)
    (f : RealComplexTempered) : RealComplexTempered :=
  TemperedDistribution.fourierMultiplierCLM ℂ
    (fun ξ : ℝ => (strictSourceCompactWeilSymbolMathlib a ξ : ℂ)) f

/-- Strict-source compact action: strict source multiplier plus the named pole. -/
def strictSourceCompactAction
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hRight : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) (_hu : HasCompactSupport u) : ℂ :=
  strictSourceWeilMultiplierCore a hRight carrier.temperedMode u +
    ∫ x : ℝ, u x * neutralWeilSourcePole carrier x ∂volume

/-- Physical translation correction contributed by equality-threshold prime powers. -/
def rightLimitThresholdPrimePhysical
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a x : ℝ) : ℂ :=
  ∑ n ∈ rightLimitThresholdFinset a,
    ((compactWindowPrimeCoefficient n / 2 : ℝ) : ℂ) *
      (carrier.h (x - Real.log (n : ℝ)) +
        carrier.h (x + Real.log (n : ℝ)))

theorem rightLimitThresholdPrime_pairing_integrable
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (u : SchwartzMap ℝ ℂ) :
    Integrable
      (fun x : ℝ => u x * rightLimitThresholdPrimePhysical carrier a x)
      volume := by
  have h := integrable_finsetSum (rightLimitThresholdFinset a)
    (fun n _ => frozenWeilPrimeShell_term_pairing_integrable carrier u n)
  simpa [rightLimitThresholdPrimePhysical, Finset.mul_sum, mul_assoc] using h

/--
The equality-threshold multiplier is exactly the corresponding physical
symmetric translation correction on every Schwartz test.
-/
theorem rightLimitThresholdPrime_fourier_physical_pairing
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (u : SchwartzMap ℝ ℂ) :
    TemperedDistribution.fourierMultiplierCLM ℂ
        (fun ξ : ℝ => (rightLimitThresholdPrimeSymbolMathlib a ξ : ℂ))
        carrier.temperedMode u =
      ∫ x : ℝ, u x * rightLimitThresholdPrimePhysical carrier a x ∂volume := by
  let g (n : ℕ) (ξ : ℝ) : ℂ :=
    (compactWindowPrimeCoefficient n : ℂ) *
      (Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ)) : ℂ)
  have hg (n : ℕ) : Function.HasTemperateGrowth (g n) := by
    dsimp [g]
    fun_prop
  have heq :
      (fun ξ : ℝ => (rightLimitThresholdPrimeSymbolMathlib a ξ : ℂ)) =
        (fun ξ : ℝ => ∑ n ∈ rightLimitThresholdFinset a, g n ξ) := by
    ext ξ
    simp [rightLimitThresholdPrimeSymbolMathlib, g]
  rw [heq, TemperedDistribution.fourierMultiplierCLM_sum ℂ
    (fun n _ => hg n)]
  simp only [sum_apply]
  have hterm (n : ℕ) :
      TemperedDistribution.fourierMultiplierCLM ℂ (g n)
          carrier.temperedMode u =
        ∫ x : ℝ,
          u x * ((compactWindowPrimeCoefficient n / 2 : ℝ) : ℂ) *
            (carrier.h (x - Real.log (n : ℝ)) +
              carrier.h (x + Real.log (n : ℝ))) ∂volume := by
    have hc : Function.HasTemperateGrowth
        (fun ξ : ℝ =>
          (Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ)) : ℂ)) := by
      fun_prop
    change TemperedDistribution.fourierMultiplierCLM ℂ
      ((compactWindowPrimeCoefficient n : ℂ) •
        (fun ξ : ℝ =>
          (Real.cos ((2 * Real.pi * ξ) * Real.log (n : ℝ)) : ℂ)))
      carrier.temperedMode u = _
    rw [TemperedDistribution.fourierMultiplierCLM_smul hc]
    simp only [smul_apply, smul_eq_mul]
    rw [cosineFourierMultiplier_physical_pairing]
    have hm :
        Integrable
          (fun x : ℝ => u x * carrier.h (x - Real.log (n : ℝ)))
          volume := by
      simpa only [sub_eq_add_neg] using
        neutralPhysical_shift_pairing_integrable
          carrier u (-Real.log (n : ℝ))
    have hp :=
      neutralPhysical_shift_pairing_integrable
        carrier u (Real.log (n : ℝ))
    have hf :
        (fun x : ℝ =>
          u x * ((compactWindowPrimeCoefficient n / 2 : ℝ) : ℂ) *
            (carrier.h (x - Real.log (n : ℝ)) +
              carrier.h (x + Real.log (n : ℝ)))) =
        (fun x : ℝ =>
          ((compactWindowPrimeCoefficient n / 2 : ℝ) : ℂ) *
            (u x * carrier.h (x - Real.log (n : ℝ)) +
              u x * carrier.h (x + Real.log (n : ℝ)))) := by
      ext x
      ring
    rw [hf, integral_const_mul, integral_add hm hp]
    push_cast
    ring
  simp_rw [hterm]
  rw [← integral_finsetSum (rightLimitThresholdFinset a)
    (fun n _ => frozenWeilPrimeShell_term_pairing_integrable carrier u n)]
  apply integral_congr_ae
  filter_upwards with x
  simp [rightLimitThresholdPrimePhysical, Finset.mul_sum, mul_assoc]

/--
Exact action-level conversion from the pinned strict-source operator to the
project right-limit operator.

The right-limit action is the strict-source action minus the equality-threshold
physical translation correction.
-/
theorem frozenWeilCompactAction_eq_strictSource_sub_threshold
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (a : ℝ) (hRight : RightLimitWeilSymbolTemperatePremise a)
    (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u) :
    frozenWeilCompactAction carrier a hRight u hu =
      strictSourceCompactAction carrier a hRight u hu -
        ∫ x : ℝ,
          u x * rightLimitThresholdPrimePhysical carrier a x ∂volume := by
  have hstrict :=
    strictSourceCompactWeilSymbolMathlib_hasTemperateGrowth a hRight
  have hthreshold :=
    rightLimitThresholdPrimeSymbolMathlib_hasTemperateGrowth a
  have hfun :
      (fun ξ : ℝ => (rightLimitCompactWeilSymbolMathlib a ξ : ℂ)) =
        (fun ξ : ℝ => (strictSourceCompactWeilSymbolMathlib a ξ : ℂ)) -
          (fun ξ : ℝ => (rightLimitThresholdPrimeSymbolMathlib a ξ : ℂ)) := by
    funext ξ
    simp only [Pi.sub_apply]
    exact_mod_cast
      rightLimitCompactWeilSymbolMathlib_eq_strictSource_sub_threshold a ξ
  have hcore :
      rightLimitWeilMultiplierCore a hRight carrier.temperedMode =
        strictSourceWeilMultiplierCore a hRight carrier.temperedMode -
          TemperedDistribution.fourierMultiplierCLM ℂ
            (fun ξ : ℝ =>
              (rightLimitThresholdPrimeSymbolMathlib a ξ : ℂ))
            carrier.temperedMode := by
    unfold rightLimitWeilMultiplierCore strictSourceWeilMultiplierCore
    rw [hfun, temperedFourierMultiplier_sub _ _ hstrict hthreshold]
  have hcore_u := congrArg (fun T : RealComplexTempered => T u) hcore
  rw [rightLimitThresholdPrime_fourier_physical_pairing] at hcore_u
  unfold frozenWeilCompactAction strictSourceCompactAction
  simp only [ContinuousLinearMap.sub_apply] at hcore_u
  linear_combination hcore_u

/--
Source-facing finite-window premise stated with Zhu's literal strict prime
cutoff.

The explicit threshold correction converts the strict source action to the
project right-limit action, while the larger-window shell transports that
action back to the frozen base radius.
-/
structure StrictSourceCorrectedWindowPremise
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c) : Prop where
  rightSymbolAt :
    ∀ b : ℝ, residual.a ≤ b →
      RightLimitWeilSymbolTemperatePremise b
  weakIdentityOnWindow :
    ∀ (b : ℝ) (hab : residual.a ≤ b)
      (u : SchwartzMap ℝ ℂ) (hu : HasCompactSupport u),
      Function.support u ⊆ Set.Ioo (-b) b →
      (∫ x : ℝ, u x * residual.q x ∂volume) =
        strictSourceCompactAction carrier b (rightSymbolAt b hab) u hu
        - ∫ x : ℝ,
            u x * rightLimitThresholdPrimePhysical carrier b x ∂volume
        + ∫ x : ℝ,
            u x * frozenWeilPrimeShellPhysical carrier residual.a b x
            ∂volume

/--
A strict-source finite-window premise produces the shell-corrected
right-limit source-window premise consumed by the previously certified
globalization theorem.
-/
def StrictSourceCorrectedWindowPremise.toRightLimit
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs)
    (residual : NeutralExponentialResidualCarrier c)
    (hSource : StrictSourceCorrectedWindowPremise carrier residual) :
    RightLimitWeilCorrectedSourceWindowPremise carrier residual where
  symbolAt := hSource.rightSymbolAt
  weakIdentityOnWindow := by
    intro b hab u hu huWindow
    have hconvert :=
      frozenWeilCompactAction_eq_strictSource_sub_threshold
        carrier b (hSource.rightSymbolAt b hab) u hu
    have hsrc := hSource.weakIdentityOnWindow b hab u hu huWindow
    linear_combination hsrc - hconvert

end

end WeilDefect
