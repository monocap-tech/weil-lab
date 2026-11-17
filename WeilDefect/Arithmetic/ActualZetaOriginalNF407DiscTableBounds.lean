import WeilDefect.Arithmetic.ActualZetaOriginalNF407DiscBound

namespace WeilDefect
noncomputable section

/-! NF589: finite rational obligations. These are disjoint from
the analytic first-400 Cauchy coefficient enclosures. -/

set_option maxHeartbeats 3000000
set_option maxRecDepth 100000

theorem neutralNF589OscillatorTable_bounds :
    ∀ i : Fin 241, 0 ≤ (nf545OriginalOscillatorNodeAt i).1 ∧
      (nf545OriginalOscillatorNodeAt i).1 ≤ 883 ∧
      (nf545OriginalOscillatorNodeAt i).2 ≤ 13 := by
  decide +kernel

theorem neutralNF589CriticalFrequency_bounds :
    ∀ k : Fin 32, 0 ≤ neutralNF587CriticalFrequencies[k.val]! ∧
      neutralNF587CriticalFrequencies[k.val]! ≤ 883 := by
  decide +kernel

theorem neutralNF589CriticalSine_bounds :
    ∀ j : Fin 4, ∀ k : Fin 32,
      |(neutralNF587CriticalSines[j.val]!)[k.val]!| ≤ 1 := by
  decide +kernel

theorem neutralNF589CriticalPole_bounds :
    ∀ j : Fin 4, |neutralNF587CriticalPoles[j.val]!| ≤ 1 := by
  decide +kernel

def neutralNF589DyadicQ (p : ℤ × ℤ) : ℚ := (p.1 : ℚ) * (2:ℚ)^p.2

theorem neutralNF589Dyadic_cast (p : ℤ × ℤ) :
    (neutralNF589DyadicQ p:ℝ) = neutralNF587Dyadic p := by
  unfold neutralNF589DyadicQ neutralNF587Dyadic
  push_cast
  rfl

/-- Pay the exact primitive midpoint/radius bound from rational
arithmetic on the frozen row. No coordinate correlations discarded
in the source itself. -/
theorem neutralNF589PrimitiveBox_bound (m r : ℤ × ℤ) (a : ℝ)
    (ha : |a-neutralNF587Dyadic m| ≤ |neutralNF587Dyadic r|)
    (h : |neutralNF589DyadicQ m|+|neutralNF589DyadicQ r| ≤ (10:ℚ)^143) :
    |a| ≤ (10:ℝ)^143 := by
  have hc : |neutralNF587Dyadic m|+|neutralNF587Dyadic r| ≤ (10:ℝ)^143 := by
    rw [← neutralNF589Dyadic_cast m,← neutralNF589Dyadic_cast r]
    exact_mod_cast h
  calc
    |a| = |(a-neutralNF587Dyadic m)+neutralNF587Dyadic m| := by
      rw [sub_add_cancel]
    _ ≤ |a-neutralNF587Dyadic m|+|neutralNF587Dyadic m| := abs_add_le _ _
    _ ≤ |neutralNF587Dyadic r|+|neutralNF587Dyadic m| := add_le_add ha le_rfl
    _ ≤ _ := by linarith

/-- Keep the two large rational decisions isolated. The fresh
independent NF587 audit already checked precisely these inequalities
using exact integer/rational arithmetic. Kernel acceptance pending. -/
theorem neutralNF589SelectedDyad_bounds :
    ∀ j : Fin 242,
      |neutralNF589DyadicQ neutralNF587SelectedDyads[j.val]!.1|+
      |neutralNF589DyadicQ neutralNF587SelectedDyads[j.val]!.2| ≤ (10:ℚ)^143 := by
  decide +kernel

theorem neutralNF589CriticalDyad_bounds :
    ∀ j : Fin 4,
      |neutralNF589DyadicQ neutralNF587CriticalDyads[j.val]!.1|+
      |neutralNF589DyadicQ neutralNF587CriticalDyads[j.val]!.2| ≤ (10:ℚ)^143 := by
  decide +kernel

theorem neutralNF589ScalarBounds_of_box (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (h : neutralNF587SourceInFrozenBox a b) :
    neutralNF589SourceScalarBounds a b := by
  refine ⟨?_,?_,neutralNF589OscillatorTable_bounds,
    neutralNF589CriticalFrequency_bounds,neutralNF589CriticalSine_bounds,
    neutralNF589CriticalPole_bounds⟩
  · intro j
    exact neutralNF589PrimitiveBox_bound _ _ _ (h.1 j) (neutralNF589SelectedDyad_bounds j)
  · intro j
    exact neutralNF589PrimitiveBox_bound _ _ _ (h.2 j) (neutralNF589CriticalDyad_bounds j)

theorem neutralNF589Disc_of_box (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (h : neutralNF587SourceInFrozenBox a b) (w : ℂ) (hw : ‖w‖ ≤ 20) :
    ‖neutralNF588NormalizedSource a b w‖ ≤ (10:ℝ)^400 :=
  neutralNF589SourceDisc_of_scalarBounds a b (neutralNF589ScalarBounds_of_box a b h) w hw

/-- Only the first 400 canonical source coefficient enclosure now
remains as an analytic-numerical premise of the collar bound. -/
theorem neutralNF589SourceBounds_of_canonicalJets
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (h : neutralNF587SourceInFrozenBox a b)
    (hjet : ∀ n < 400,
      ‖neutralNF588NormalizedCoefficient (neutralNF588NormalizedSource a b) n‖ ≤
        neutralNF588U400Bound n) :
    (∀ x ∈ Set.Icc (549/500:ℝ) (11/10), |neutralNF587Source a b x| ≤ 2/10^7) ∧
      (∀ x ∈ Set.Icc (549/500:ℝ) (11/10), |deriv (neutralNF587Source a b) x| ≤ 7/10^4) :=
  neutralNF588OriginalSource_collar_bounds a b
    (fun w hw => neutralNF589Disc_of_box a b h w hw.le) hjet

end
end WeilDefect
