import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSchwartzPolarization
import WeilDefect.Arithmetic.ActualZetaPhaseIVHermitianTwoBlockPSD
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
IV010: EXACT ONE-NEW-SUPPORT extension of the authentic mixed Weil EF.

Old Schwartz family s lives inside [-a,a], new test t inside [-b,b],
a ≤ b. IV009 attaches the old finite mixed quadratic energy to the
diagonal physical Schwartz sum. IV006/IV007 transport that OLD block
without changing its entries. The new cross row, cross column and
new diagonal are literal ORIGINAL Zeta23.EF.literatureRHS mixed terms.

We do NOT assume that the new mixed zeta estimate is true. We expose
precisely the necessary additional source inequality and prove it is
sufficient for positive semidefiniteness of this one-site extension.
The condition is a quantified cross-support Schur/Cauchy bound; no
global Weil positivity or RH is concluded.
-/

/-- The same authentic two-argument zeta arithmetic mixed functional,
with original physical L² correlation and all EF terms retained. -/
def neutralIV010Mixed (b : ℝ) (f g : 𝓢(ℝ, ℂ)) : ℂ :=
  Zeta23.EF.literatureRHS
    (neutralWindowCorrelation b (f.toLp 2 volume) (g.toLp 2 volume))

/-- The literal original signed arithmetic diagonal at a window. -/
def neutralIV010Diagonal (b : ℝ) (f : 𝓢(ℝ, ℂ)) : ℂ :=
  neutralIV010Mixed b f f

/-- Source-specific two-function family, with indices 0 and 1. -/
def neutralIV010TwoTests (f g : 𝓢(ℝ, ℂ)) : Fin 2 → 𝓢(ℝ, ℂ) :=
  fun i => if i = 0 then f else g

/-- Coefficients 1 and v, so the actual physical sum is f+v•g. -/
def neutralIV010TwoCoeffs (v : ℂ) : Fin 2 → ℂ :=
  fun i => if i = 0 then 1 else v

/-- Both source family members really fit the same original window. -/
theorem neutralIV010TwoTests_supported
    (b : ℝ) (f g : 𝓢(ℝ, ℂ))
    (hf : ∀ x : ℝ, x ∉ Set.Icc (-b) b → f x = 0)
    (hg : ∀ x : ℝ, x ∉ Set.Icc (-b) b → g x = 0) :
    ∀ i : Fin 2, ∀ x : ℝ,
      x ∉ Set.Icc (-b) b → neutralIV010TwoTests f g i x = 0 := by
  intro i x hx
  fin_cases i
  · simpa [neutralIV010TwoTests] using hf x hx
  · simpa [neutralIV010TwoTests] using hg x hx

/-- The two-function finite Schwartz combination is the actual sum. -/
theorem neutralIV010TwoTests_physicalSum
    (f g : 𝓢(ℝ, ℂ)) (v : ℂ) :
    neutralIV009PhysicalSchwartzSum
        (neutralIV010TwoTests f g) (neutralIV010TwoCoeffs v) =
      f + v • g := by
  simp [neutralIV009PhysicalSchwartzSum,
    neutralIV010TwoTests, neutralIV010TwoCoeffs, Fin.sum_univ_two]

/-- Physical polarization for ONE genuinely new test. The four terms
are literal original arithmetic zeta EF entries, not a surrogate
abstract Hermitian matrix. This uses IV009's genuine full-divisor
finite-Schwartz polarization theorem. -/
theorem neutralIV010TwoSource_literalBlock
    (b : ℝ) (f g : 𝓢(ℝ, ℂ))
    (hf : ∀ x : ℝ, x ∉ Set.Icc (-b) b → f x = 0)
    (hg : ∀ x : ℝ, x ∉ Set.Icc (-b) b → g x = 0)
    (v : ℂ) :
    neutralIV010Diagonal b (f + v • g) =
      neutralIV010Mixed b f f +
        neutralIV010Mixed b f g * v +
        conj v * neutralIV010Mixed b g f +
        conj v * neutralIV010Mixed b g g * v := by
  have hpol := neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal
    b (neutralIV010TwoTests f g) (neutralIV010TwoCoeffs v)
    (neutralIV010TwoTests_supported b f g hf hg)
  rw [neutralIV010TwoTests_physicalSum] at hpol
  change neutralIV007OriginalMixedEnergy b
      (neutralIV010TwoTests f g) (neutralIV010TwoCoeffs v) =
    neutralIV010Diagonal b (f + v • g) at hpol
  rw [← hpol]
  simp [neutralIV007OriginalMixedEnergy, neutralIV007OriginalMixedEntry,
    neutralIV010Mixed, neutralIV010TwoTests, neutralIV010TwoCoeffs,
    Fin.sum_univ_two]
  ring

/-- The authentic original zeta mixed EF is Hermitian for two
arbitrary complex Schwartz tests supported in the same window. -/
theorem neutralIV010Mixed_hermitian
    (b : ℝ) (f g : 𝓢(ℝ, ℂ))
    (hf : ∀ x : ℝ, x ∉ Set.Icc (-b) b → f x = 0)
    (hg : ∀ x : ℝ, x ∉ Set.Icc (-b) b → g x = 0) :
    conj (neutralIV010Mixed b f g) =
      neutralIV010Mixed b g f := by
  simpa [neutralIV010Mixed, neutralIV007OriginalMixedEntry,
    neutralIV010TwoTests] using
    (neutralIV008OriginalMixedEntry_hermitian
      b (neutralIV010TwoTests f g)
      (neutralIV010TwoTests_supported b f g hf hg)
      (0 : Fin 2) (1 : Fin 2))

/-- The genuine original one-test signed EF diagonal is real. -/
theorem neutralIV010Diagonal_im_zero
    (b : ℝ) (g : 𝓢(ℝ, ℂ))
    (hg : ∀ x : ℝ, x ∉ Set.Icc (-b) b → g x = 0) :
    (neutralIV010Diagonal b g).im = 0 := by
  have h : conj (neutralIV010Mixed b g g) =
      neutralIV010Mixed b g g :=
    neutralIV010Mixed_hermitian b g g hg hg
  have hi := congrArg Complex.im h
  simp only [Complex.conj_im] at hi
  dsimp [neutralIV010Diagonal]
  linarith

/-- EXACT new row/column block decomposition. The old finite family
is supported in [-a,a], the one newly admitted Schwartz test in
[-b,b]. Only the old block is transported from a to b.

No inequality for the NEW cross term or diagonal is smuggled in. -/
theorem neutralIV010OldPlusNew_exactBlock
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (t : 𝓢(ℝ, ℂ))
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (v : ℂ) :
    neutralIV010Diagonal b (neutralIV009PhysicalSchwartzSum s u + v • t) =
      neutralIV007OriginalMixedEnergy a s u +
        neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t * v +
        conj v * neutralIV010Mixed b t (neutralIV009PhysicalSchwartzSum s u) +
        conj v * neutralIV010Diagonal b t * v := by
  let S := neutralIV009PhysicalSchwartzSum s u
  have hSa : ∀ x : ℝ, x ∉ Set.Icc (-a) a → S x = 0 :=
    neutralIV009PhysicalSchwartzSum_supported a s u hs
  have hSb : ∀ x : ℝ, x ∉ Set.Icc (-b) b → S x = 0 :=
    neutralIV006Schwartz_support_expand a b hab S hSa
  have hfamily : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-b) b → s i x = 0 := by
    intro i
    exact neutralIV006Schwartz_support_expand a b hab (s i) (hs i)
  have hpol := neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal
    b s u hfamily
  have hnat := neutralIV007OriginalMixedEnergy_natural a b hab s hs u
  have hold :
      neutralIV010Mixed b S S = neutralIV007OriginalMixedEnergy a s u :=
    (hpol.symm).trans hnat.symm
  calc
    neutralIV010Diagonal b (S + v • t) =
      neutralIV010Mixed b S S + neutralIV010Mixed b S t * v +
      conj v * neutralIV010Mixed b t S +
      conj v * neutralIV010Mixed b t t * v :=
        neutralIV010TwoSource_literalBlock b S t hSb ht v
    _ = _ := by
      rw [hold]
      rfl

/-- Exact original cross-support REAL quadratic block formula.
The new row remains the actual literal Zeta23.EF.literatureRHS
mixed term, with its first-antilinear/second-linear sign. -/
theorem neutralIV010OldPlusNew_realBlock
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (t : 𝓢(ℝ, ℂ))
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (v : ℂ) :
    (neutralIV010Diagonal b (neutralIV009PhysicalSchwartzSum s u + v • t)).re =
      (neutralIV007OriginalMixedEnergy a s u).re +
      2 * (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t * v).re +
      (neutralIV010Diagonal b t).re * (v.re^2 + v.im^2) := by
  let S := neutralIV009PhysicalSchwartzSum s u
  have hSa : ∀ x : ℝ, x ∉ Set.Icc (-a) a → S x = 0 :=
    neutralIV009PhysicalSchwartzSum_supported a s u hs
  have hSb : ∀ x : ℝ, x ∉ Set.Icc (-b) b → S x = 0 :=
    neutralIV006Schwartz_support_expand a b hab S hSa
  have hherm : neutralIV010Mixed b t S =
      conj (neutralIV010Mixed b S t) :=
    (neutralIV010Mixed_hermitian b S t hSb ht).symm
  have hdiag : (neutralIV010Diagonal b t).im = 0 :=
    neutralIV010Diagonal_im_zero b t ht
  rw [neutralIV010OldPlusNew_exactBlock a b hab s u hs t ht v]
  rw [hherm]
  simp only [Complex.add_re, Complex.mul_re, Complex.conj_re, Complex.conj_im]
  dsimp [neutralIV010Diagonal] at hdiag
  rw [hdiag]
  ring

/-- Sharp COMPLEX two-source Schur/Cauchy support criterion.
This is algebra only, reusing the NF740 genuine complex Hermitian
two-block PSD theorem. In particular the cross magnitude cannot be
omitted or replaced by a pairwise real-only estimate. -/
theorem neutralIV010HermitianTwoBlock_nonnegative
    (A D : ℝ) (B v : ℂ)
    (hA : 0 ≤ A) (hD : 0 ≤ D)
    (hcross : B.re^2 + B.im^2 ≤ A * D) :
    0 ≤ A + 2 * (B * v).re + D * (v.re^2 + v.im^2) := by
  have h := neutralNF740HermitianTwoBlockPSD
    A D B.re (-B.im) hA hD
    (by nlinarith only [hcross]) 1 0 v.re v.im
  change 0 ≤ A * (1^2 + 0^2) +
    2 * (B.re * (1*v.re + 0*v.im) +
      (-B.im) * (1*v.im - 0*v.re)) +
      D * (v.re^2 + v.im^2) at h
  simpa only [one_pow, zero_pow, one_mul, zero_mul,
    add_zero, zero_add, sub_zero, mul_one, neg_mul,
    Complex.mul_re] using h

/-- Actual original arithmetic support-EXTENSION sufficiency gate.

For one old finite Schwartz span and one newly admitted test:
old-block nonnegativity, new diagonal nonnegativity and a
source-specific complex mixed determinant bound together imply
nonnegativity of every physical two-source superposition.

NO part of this theorem asserts the missing mixed bound holds for
zeta outside the original frozen support; it is an explicit premise.
-/
theorem neutralIV010OriginalOneNewSource_nonnegative_of_crossBound
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (t : 𝓢(ℝ, ℂ))
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (hOld : 0 ≤ (neutralIV007OriginalMixedEnergy a s u).re)
    (hNew : 0 ≤ (neutralIV010Diagonal b t).re)
    (hCross :
      (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t).re^2 +
      (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t).im^2 ≤
        (neutralIV007OriginalMixedEnergy a s u).re *
          (neutralIV010Diagonal b t).re)
    (v : ℂ) :
    0 ≤ (neutralIV010Diagonal b
      (neutralIV009PhysicalSchwartzSum s u + v • t)).re := by
  rw [neutralIV010OldPlusNew_realBlock a b hab s u hs t ht v]
  exact neutralIV010HermitianTwoBlock_nonnegative
    (neutralIV007OriginalMixedEnergy a s u).re
    (neutralIV010Diagonal b t).re
    (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t)
    v hOld hNew hCross

#print axioms neutralNF740HermitianTwoBlockPSD
#print axioms neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal
#print axioms neutralIV008OriginalMixedEntry_hermitian
#print axioms neutralIV007OriginalMixedEnergy_natural
#print axioms neutralIV010TwoTests_supported
#print axioms neutralIV010TwoTests_physicalSum
#print axioms neutralIV010TwoSource_literalBlock
#print axioms neutralIV010Mixed_hermitian
#print axioms neutralIV010Diagonal_im_zero
#print axioms neutralIV010OldPlusNew_exactBlock
#print axioms neutralIV010OldPlusNew_realBlock
#print axioms neutralIV010HermitianTwoBlock_nonnegative
#print axioms neutralIV010OriginalOneNewSource_nonnegative_of_crossBound

end
end WeilDefect
