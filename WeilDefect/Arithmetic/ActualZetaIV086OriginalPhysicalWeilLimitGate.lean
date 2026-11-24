import WeilDefect.Arithmetic.ActualZetaIV083CompactC2OriginalGammaLimitGate
import WeilDefect.Arithmetic.ActualZetaIV084OriginalPolePhysicalGate
import WeilDefect.Arithmetic.ActualZetaIV085OriginalPrimeFiniteGate
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Filter
open scoped Topology

/-!
IV086 — assemble the literal original signed Weil RHS from the
physical poles, finite original signed prime contribution and the
original NF599 physical Gamma approximants. No positivity theorem,
carrier identification, or RH claim. Component source copies are
unchanged; pending upstream gates are not counted as certified.
-/

/-- The exact physical approximation with a fixed arithmetic cutoff M
and a variable original NF599 Gamma truncation N. -/
def neutralIV086PhysicalWeilFinite (M N : ℕ) (k : ℝ → ℂ) : ℂ :=
  (∫ u : ℝ, k u *
    (Complex.exp (-(u : ℂ) / 2) + Complex.exp ((u : ℂ) / 2))) -
  (∑ n ∈ Finset.range M, neutralIV085PrimeSummand k n) +
  neutralIV078FiniteSpatial N k

/-- The finite physical approximation equals the actual original
poles and finite prime term plus the literal finite Gamma spectral
pairing. This equality has no infinite-limit premise. -/
theorem neutralIV086PhysicalWeilFinite_eq_spectral
    (M N : ℕ) (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k)
    {L : ℝ} (hL : 0 ≤ L)
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ L) :
    neutralIV086PhysicalWeilFinite M N k =
      Zeta23.paperFT k (Complex.I / 2) +
      Zeta23.paperFT k (-Complex.I / 2) -
      (∑ n ∈ Finset.range M, neutralIV085PrimeSummand k n) +
      (1 / (2 * Real.pi) : ℂ) *
        (∫ r : ℝ, Zeta23.paperFT k (r : ℂ) *
          (neutralIV071GammaFinite N r : ℂ)) := by
  unfold neutralIV086PhysicalWeilFinite
  rw [← neutralIV084PoleSum_physical k hk.continuous hsupp,
      ← neutralIV083FiniteGamma_pairing_compactC2 N k hk hL hsupp]

/-- At any sufficient arithmetic cutoff, the entire physical
approximation converges to the literal original literature RHS.
No additional weighted or ordinary Fourier-L¹ hypothesis. -/
theorem neutralIV086PhysicalWeilFinite_tendsto_original
    (M : ℕ) (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k)
    {L : ℝ} (hL : 0 ≤ L)
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ L)
    (hM : Real.exp L < (M : ℝ)) :
    Tendsto (fun N : ℕ => neutralIV086PhysicalWeilFinite M N k)
      atTop (𝓝 (Zeta23.EF.literatureRHS k)) := by
  rw [neutralIV085LiteratureRHS_finitePrime k hsupp M hM,
      neutralIV084PoleSum_physical k hk.continuous hsupp]
  unfold neutralIV086PhysicalWeilFinite
  exact tendsto_const_nhds.add
    (neutralIV083FiniteSpatial_tendsto_compactC2 k hk hL hsupp)

/-- A finite arithmetic cutoff always exists; no arithmetic-density
or zero-location condition is imposed on the original test. -/
theorem neutralIV086ExistsPhysicalWeilLimit
    (k : ℝ → ℂ) (hk : ContDiff ℝ 2 k)
    {L : ℝ} (hL : 0 ≤ L)
    (hsupp : ∀ u : ℝ, k u ≠ 0 → |u| ≤ L) :
    ∃ M : ℕ, Real.exp L < (M : ℝ) ∧
      Tendsto (fun N : ℕ => neutralIV086PhysicalWeilFinite M N k)
        atTop (𝓝 (Zeta23.EF.literatureRHS k)) := by
  obtain ⟨M, hM⟩ := exists_nat_gt (Real.exp L)
  exact ⟨M, hM, neutralIV086PhysicalWeilFinite_tendsto_original M k hk hL hsupp hM⟩

#print axioms neutralIV086PhysicalWeilFinite_eq_spectral
#print axioms neutralIV086PhysicalWeilFinite_tendsto_original
#print axioms neutralIV086ExistsPhysicalWeilLimit

end
end WeilDefect
