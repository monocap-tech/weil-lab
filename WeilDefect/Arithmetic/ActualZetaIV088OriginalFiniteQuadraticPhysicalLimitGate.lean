import WeilDefect.Arithmetic.ActualZetaIV087OriginalMixedPhysicalLimitGate
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSchwartzPolarization
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Filter
open scoped SchwartzMap Topology ComplexConjugate BigOperators

/-!
IV088: transport the certified IV087 entrywise physical limit through
arbitrary finite complex quadratic combinations on the original
Schwartz family. One fixed sufficient arithmetic cutoff is used for
every entry. No positivity assumption or conclusion, no RH claim.
-/

/-- Finite quadratic combination of the actual IV086 approximants,
with exactly the IV007 coefficient orientation. -/
def neutralIV088PhysicalMixedEnergy {n : ℕ}
    (a : ℝ) (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (M N : ℕ) : ℂ :=
  ∑ i : Fin n, ∑ j : Fin n,
    conj (u i) * neutralIV086PhysicalWeilFinite M N
      (neutralWindowCorrelation a ((s i).toLp 2 volume)
        ((s j).toLp 2 volume)) * u j

private theorem finiteSum_tendsto {ι : Type*}
    (t : Finset ι) (F : ι → ℕ → ℂ) (v : ι → ℂ)
    (h : ∀ i, Tendsto (F i) atTop (𝓝 (v i))) :
    Tendsto (fun N : ℕ => ∑ i ∈ t, F i N) atTop
      (𝓝 (∑ i ∈ t, v i)) := by
  classical
  induction t using Finset.induction_on with
  | empty =>
    simpa only [Finset.sum_empty] using
      (tendsto_const_nhds : Tendsto (fun _ : ℕ => (0 : ℂ)) atTop (𝓝 0))
  | @insert i t hi ih =>
    simp only [Finset.sum_insert hi]
    exact (h i).add ih

/-- Original finite mixed arithmetic quadratic energy is the limit
of the complete signed physical approximants. -/
theorem neutralIV088PhysicalMixedEnergy_tendsto_original
    {n : ℕ} (a : ℝ) (ha : 0 ≤ a) (s : Fin n → 𝓢(ℝ, ℂ))
    (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (M : ℕ) (hM : Real.exp (2 * a) < (M : ℝ)) :
    Tendsto (fun N : ℕ => neutralIV088PhysicalMixedEnergy a s u M N)
      atTop (𝓝 (neutralIV007OriginalMixedEnergy a s u)) := by
  unfold neutralIV088PhysicalMixedEnergy neutralIV007OriginalMixedEnergy
  apply finiteSum_tendsto
  intro i
  apply finiteSum_tendsto
  intro j
  exact (tendsto_const_nhds.mul
    (neutralIV087OriginalMixedEntry_physicalLimit a ha s hs M hM i j)).mul
      tendsto_const_nhds

/-- The same finite quadratic limit receives the actual original
full-divisor entries, with the existing partner-frequency orientation. -/
theorem neutralIV088PhysicalMixedEnergy_tendsto_divisor
    {n : ℕ} (a : ℝ) (ha : 0 ≤ a) (s : Fin n → 𝓢(ℝ, ℂ))
    (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (M : ℕ) (hM : Real.exp (2 * a) < (M : ℝ)) :
    Tendsto (fun N : ℕ => neutralIV088PhysicalMixedEnergy a s u M N)
      atTop (𝓝 (∑ i : Fin n, ∑ j : Fin n,
        conj (u i) * neutralIV007OriginalDivisorEntry a s i j * u j)) := by
  simp_rw [neutralIV008OriginalMixedEntry_eq_divisor a s hs]
  exact neutralIV088PhysicalMixedEnergy_tendsto_original a ha s u hs M hM

/-- The finite family limit is the literal signed arithmetic diagonal
of the actual physical Schwartz superposition, using IV009. -/
theorem neutralIV088PhysicalMixedEnergy_tendsto_diagonal
    {n : ℕ} (a : ℝ) (ha : 0 ≤ a) (s : Fin n → 𝓢(ℝ, ℂ))
    (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (M : ℕ) (hM : Real.exp (2 * a) < (M : ℝ)) :
    Tendsto (fun N : ℕ => neutralIV088PhysicalMixedEnergy a s u M N)
      atTop (𝓝 (Zeta23.EF.literatureRHS
        (neutralWindowCorrelation a
          ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume)
          ((neutralIV009PhysicalSchwartzSum s u).toLp 2 volume)))) := by
  rw [← neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal a s u hs]
  exact neutralIV088PhysicalMixedEnergy_tendsto_original a ha s u hs M hM

/-- The imaginary part tends to zero by the existing Hermitian
identity of the original mixed energy, not by a positivity claim. -/
theorem neutralIV088PhysicalMixedEnergy_im_tendsto_zero
    {n : ℕ} (a : ℝ) (ha : 0 ≤ a) (s : Fin n → 𝓢(ℝ, ℂ))
    (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (M : ℕ) (hM : Real.exp (2 * a) < (M : ℝ)) :
    Tendsto (fun N : ℕ => (neutralIV088PhysicalMixedEnergy a s u M N).im)
      atTop (𝓝 (0 : ℝ)) := by
  have h := (Complex.continuous_im.tendsto
    (neutralIV007OriginalMixedEnergy a s u)).comp
      (neutralIV088PhysicalMixedEnergy_tendsto_original a ha s u hs M hM)
  simpa only [Function.comp_apply, neutralIV008OriginalMixedEnergy_im_zero a s hs u]
    using h

#print axioms neutralIV088PhysicalMixedEnergy_tendsto_original
#print axioms neutralIV088PhysicalMixedEnergy_tendsto_divisor
#print axioms neutralIV088PhysicalMixedEnergy_tendsto_diagonal
#print axioms neutralIV088PhysicalMixedEnergy_im_tendsto_zero

end
end WeilDefect
