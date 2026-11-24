import WeilDefect.Arithmetic.ActualZetaIV086OriginalPhysicalWeilLimitGate
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalMixedHermitian
import WeilDefect.Arithmetic.ActualZetaSmoothCorrelationRegularity
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Filter
open scoped SchwartzMap Topology ComplexConjugate

/-!
IV087: specialize the certified original signed physical limit to the
existing original finite-family mixed Schwartz carrier. The actual
window is unchanged; the correlation radius is twice its radius.
No positivity, global complement estimate or RH claim.
-/

/-- A genuine window correlation is supported in the doubled window. -/
theorem neutralIV087WindowCorrelation_support_abs
    (a : ℝ) (f g : RealComplexL2) :
    ∀ u : ℝ, neutralWindowCorrelation a f g u ≠ 0 → |u| ≤ 2 * a := by
  intro u hu
  apply abs_le.mpr
  by_contra h
  exact hu (neutralWindowCorrelation_supported a f g u
    (fun hmem => h ⟨hmem.1, hmem.2⟩))

/-- The original mixed Schwartz entry uses a compact C² correlation,
not an abstract replacement kernel. -/
theorem neutralIV087OriginalMixedCorrelation_contDiff
    {n : ℕ} (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (i j : Fin n) :
    ContDiff ℝ 2 (neutralWindowCorrelation a
      ((s i).toLp 2 volume) ((s j).toLp 2 volume)) :=
  neutralWindowCorrelation_contDiff_of_ae_smoothSecond
    a ((s i).toLp 2 volume) ((s j).toLp 2 volume)
    (fun x : ℝ => (s j) x) ((s j).smooth 2)
    (neutralIV008SchwartzWindow_hasCompactSupport a (s j) (hs j))
    (neutralIV006Schwartz_window_ae a (s j) (hs j))

/-- The original physical limit receives the actual mixed arithmetic
entry with a single cutoff M strictly above exp(2a). -/
theorem neutralIV087OriginalMixedEntry_physicalLimit
    {n : ℕ} (a : ℝ) (ha : 0 ≤ a) (s : Fin n → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (M : ℕ) (hM : Real.exp (2 * a) < (M : ℝ))
    (i j : Fin n) :
    Tendsto (fun N : ℕ => neutralIV086PhysicalWeilFinite M N
      (neutralWindowCorrelation a ((s i).toLp 2 volume) ((s j).toLp 2 volume)))
      atTop (𝓝 (neutralIV007OriginalMixedEntry a s i j)) := by
  unfold neutralIV007OriginalMixedEntry
  exact neutralIV086PhysicalWeilFinite_tendsto_original M _
    (neutralIV087OriginalMixedCorrelation_contDiff a s hs i j)
    (show 0 ≤ 2 * a by positivity)
    (neutralIV087WindowCorrelation_support_abs a _ _) hM

/-- Transport the same limit to the full original divisor entry,
retaining the actual multiplicity-copy and partner-zero pairing. -/
theorem neutralIV087OriginalDivisorEntry_physicalLimit
    {n : ℕ} (a : ℝ) (ha : 0 ≤ a) (s : Fin n → 𝓢(ℝ, ℂ))
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (M : ℕ) (hM : Real.exp (2 * a) < (M : ℝ))
    (i j : Fin n) :
    Tendsto (fun N : ℕ => neutralIV086PhysicalWeilFinite M N
      (neutralWindowCorrelation a ((s i).toLp 2 volume) ((s j).toLp 2 volume)))
      atTop (𝓝 (neutralIV007OriginalDivisorEntry a s i j)) := by
  rw [neutralIV008OriginalMixedEntry_eq_divisor a s hs i j]
  exact neutralIV087OriginalMixedEntry_physicalLimit a ha s hs M hM i j

#print axioms neutralIV087WindowCorrelation_support_abs
#print axioms neutralIV087OriginalMixedCorrelation_contDiff
#print axioms neutralIV087OriginalMixedEntry_physicalLimit
#print axioms neutralIV087OriginalDivisorEntry_physicalLimit

end
end WeilDefect
