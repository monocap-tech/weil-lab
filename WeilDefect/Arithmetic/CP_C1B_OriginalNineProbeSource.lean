import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSchwartzPolarization
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
CP-C1(B) — genuine original signed Weil two-probe source bridge.

This intentionally IMPORTS the kernel-passed IV009 Schwartz polarization,
NOT the separately failing IV010 source module, and does not import an
independent spectral comparison. The original arithmetic functional is
literally Zeta23.EF.literatureRHS on the physical window correlation.
The target is conjugate-linear FIRST and linear SECOND.

No frozen bump implementation, independent explicit-formula comparison,
interval enclosure, zero census, positivity or RH is asserted here.
All declarations are new Lean proof CANDIDATES until built and audited.
-/

/-- Authentic original mixed arithmetic Weil value, not a Gram proxy. -/
def neutralCPC1BOriginalMixed (a : ℝ)
    (f g : 𝓢(ℝ, ℂ)) : ℂ :=
  Zeta23.EF.literatureRHS
    (neutralWindowCorrelation a (f.toLp 2 volume) (g.toLp 2 volume))

/-- True original physical diagonal, with no positive sign assumed. -/
def neutralCPC1BOriginalDiagonal (a : ℝ)
    (f : 𝓢(ℝ, ℂ)) : ℂ :=
  neutralCPC1BOriginalMixed a f f

private def pair (f g : 𝓢(ℝ, ℂ)) : Fin 2 → 𝓢(ℝ, ℂ) :=
  fun i => if i = 0 then f else g

private def pairCoeff (v : ℂ) : Fin 2 → ℂ :=
  fun i => if i = 0 then 1 else v

private theorem pair_supported
    (a : ℝ) (f g : 𝓢(ℝ, ℂ))
    (hf : ∀ x : ℝ, x ∉ Set.Icc (-a) a → f x = 0)
    (hg : ∀ x : ℝ, x ∉ Set.Icc (-a) a → g x = 0) :
    ∀ i : Fin 2, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → pair f g i x = 0 := by
  intro i x hx
  fin_cases i
  · simpa [pair] using hf x hx
  · simpa [pair] using hg x hx

private theorem pair_physicalSum
    (f g : 𝓢(ℝ, ℂ)) (v : ℂ) :
    neutralIV009PhysicalSchwartzSum (pair f g) (pairCoeff v) =
      f + v • g := by
  simp [neutralIV009PhysicalSchwartzSum, pair, pairCoeff,
    Fin.sum_univ_two]

/-- Source-level finite-pair identity using ONLY accepted IV009
polarization and the unchanged original all-divisor EF functional. -/
theorem neutralCPC1BOriginal_exactTwoProbe
    (a : ℝ) (f g : 𝓢(ℝ, ℂ))
    (hf : ∀ x : ℝ, x ∉ Set.Icc (-a) a → f x = 0)
    (hg : ∀ x : ℝ, x ∉ Set.Icc (-a) a → g x = 0)
    (v : ℂ) :
    neutralCPC1BOriginalDiagonal a (f + v • g) =
      neutralCPC1BOriginalMixed a f f +
        neutralCPC1BOriginalMixed a f g * v +
        conj v * neutralCPC1BOriginalMixed a g f +
        conj v * neutralCPC1BOriginalMixed a g g * v := by
  have hpol := neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal
    a (pair f g) (pairCoeff v) (pair_supported a f g hf hg)
  rw [pair_physicalSum] at hpol
  change neutralIV007OriginalMixedEnergy a (pair f g) (pairCoeff v) =
    neutralCPC1BOriginalDiagonal a (f + v • g) at hpol
  rw [← hpol]
  simp [neutralIV007OriginalMixedEnergy, neutralIV007OriginalMixedEntry,
    neutralCPC1BOriginalMixed, neutralCPC1BOriginalDiagonal,
    pair, pairCoeff, Fin.sum_univ_two]
  ring

/-- Original full arithmetic mixed entries are Hermitian on supported
complex Schwartz tests: no imaginary-sign convention is substituted. -/
theorem neutralCPC1BOriginal_hermitian
    (a : ℝ) (f g : 𝓢(ℝ, ℂ))
    (hf : ∀ x : ℝ, x ∉ Set.Icc (-a) a → f x = 0)
    (hg : ∀ x : ℝ, x ∉ Set.Icc (-a) a → g x = 0) :
    conj (neutralCPC1BOriginalMixed a f g) =
      neutralCPC1BOriginalMixed a g f := by
  simpa [neutralCPC1BOriginalMixed,
    neutralIV007OriginalMixedEntry, pair] using
    (neutralIV008OriginalMixedEntry_hermitian
      a (pair f g) (pair_supported a f g hf hg)
      (0 : Fin 2) (1 : Fin 2))

/-- No sign of the real diagonal is assumed or proved. -/
theorem neutralCPC1BOriginal_diagonal_im_zero
    (a : ℝ) (g : 𝓢(ℝ, ℂ))
    (hg : ∀ x : ℝ, x ∉ Set.Icc (-a) a → g x = 0) :
    (neutralCPC1BOriginalDiagonal a g).im = 0 := by
  have h : conj (neutralCPC1BOriginalMixed a g g) =
      neutralCPC1BOriginalMixed a g g :=
    neutralCPC1BOriginal_hermitian a g g hg hg
  have hi := congrArg Complex.im h
  simp only [Complex.conj_im] at hi
  dsimp [neutralCPC1BOriginalDiagonal]
  linarith

/-- True original real diagonal response to an arbitrary COMPLEX
relative phase, derived directly from IV009 (not from IV010). -/
theorem neutralCPC1BOriginal_phaseResponse
    (a : ℝ) (f g : 𝓢(ℝ, ℂ))
    (hf : ∀ x : ℝ, x ∉ Set.Icc (-a) a → f x = 0)
    (hg : ∀ x : ℝ, x ∉ Set.Icc (-a) a → g x = 0)
    (v : ℂ) :
    (neutralCPC1BOriginalDiagonal a (f + v • g)).re =
      (neutralCPC1BOriginalDiagonal a f).re +
      2 * (neutralCPC1BOriginalMixed a f g * v).re +
      (neutralCPC1BOriginalDiagonal a g).re * (v.re^2 + v.im^2) := by
  have hherm : neutralCPC1BOriginalMixed a g f =
      conj (neutralCPC1BOriginalMixed a f g) :=
    (neutralCPC1BOriginal_hermitian a f g hf hg).symm
  have hdiag := neutralCPC1BOriginal_diagonal_im_zero a g hg
  rw [neutralCPC1BOriginal_exactTwoProbe a f g hf hg v]
  rw [hherm]
  -- Include the imaginary-product expansion, so the real diagonal's
  -- imaginary part occurs literally in the goal before rewriting.
  -- Do NOT unfold the diagonal alias in hdiag: the goal uses that alias.
  simp only [Complex.add_re, Complex.mul_re, Complex.mul_im,
    Complex.conj_re, Complex.conj_im]
  -- Actual compiler diagnostic: the GOAL already unfolds the diagonal
  -- alias; expose the identical original mixed expression in hdiag.
  dsimp only [neutralCPC1BOriginalDiagonal] at hdiag ⊢
  rw [hdiag]
  ring

/-- The REAL component of the actual mixed original Weil entry is
recovered from three original diagonal source evaluations. -/
theorem neutralCPC1BOriginal_re_from_three_probes
    (a : ℝ) (f g : 𝓢(ℝ, ℂ))
    (hf : ∀ x : ℝ, x ∉ Set.Icc (-a) a → f x = 0)
    (hg : ∀ x : ℝ, x ∉ Set.Icc (-a) a → g x = 0) :
    (neutralCPC1BOriginalMixed a f g).re =
      ((neutralCPC1BOriginalDiagonal a (f + g)).re -
        (neutralCPC1BOriginalDiagonal a f).re -
        (neutralCPC1BOriginalDiagonal a g).re) / 2 := by
  have h := neutralCPC1BOriginal_phaseResponse a f g hf hg (1 : ℂ)
  simp only [one_smul, mul_one, Complex.one_re, Complex.one_im,
    one_pow, zero_pow, add_zero, mul_one] at h
  linarith

/-- The IMAGINARY component requires an i-relative-phase probe.
This negative sign is forced by the source's first-slot conjugation. -/
theorem neutralCPC1BOriginal_im_from_three_probes
    (a : ℝ) (f g : 𝓢(ℝ, ℂ))
    (hf : ∀ x : ℝ, x ∉ Set.Icc (-a) a → f x = 0)
    (hg : ∀ x : ℝ, x ∉ Set.Icc (-a) a → g x = 0) :
    (neutralCPC1BOriginalMixed a f g).im =
      -((neutralCPC1BOriginalDiagonal a (f + Complex.I • g)).re -
        (neutralCPC1BOriginalDiagonal a f).re -
        (neutralCPC1BOriginalDiagonal a g).re) / 2 := by
  have h := neutralCPC1BOriginal_phaseResponse a f g hf hg Complex.I
  simp only [Complex.mul_re, Complex.I_re, Complex.I_im,
    zero_mul, mul_zero, mul_one, sub_zero, zero_sub,
    zero_pow, one_pow, zero_add, add_zero, one_mul] at h
  linarith

#print axioms neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal
#print axioms neutralIV008OriginalMixedEntry_hermitian
#print axioms neutralCPC1BOriginal_exactTwoProbe
#print axioms neutralCPC1BOriginal_hermitian
#print axioms neutralCPC1BOriginal_diagonal_im_zero
#print axioms neutralCPC1BOriginal_phaseResponse
#print axioms neutralCPC1BOriginal_re_from_three_probes
#print axioms neutralCPC1BOriginal_im_from_three_probes

end
end WeilDefect
