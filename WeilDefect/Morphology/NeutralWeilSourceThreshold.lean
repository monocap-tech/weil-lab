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
    rw [rightLimitCompactWeilSymbolMathlib_eq_strictSource_sub_threshold]
    ring
  rw [heq]
  exact hRight.hasTemperateGrowth.add hthreshold

end

end WeilDefect
