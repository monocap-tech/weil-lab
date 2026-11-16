import WeilDefect.Arithmetic.ActualZetaOriginalCollar242Correction
import WeilDefect.Arithmetic.ActualZetaOriginalCollar242GraphCorrection
import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.LinearAlgebra.StdBasis
import Mathlib.LinearAlgebra.Basis.Defs

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-!
NF544: eliminate NF543's *abstract* right-inverse R by constructing
it from an explicitly indexed 242-column Schwartz bump family
and the actual physical 242-moment map M.

The essential remaining source-specific hypothesis is the positive
definiteness of the associated 242×242 Gram endomorphism for the
original NF523 analytic generators j_i with its genuine χ cutoff.
No surrogate polynomial control, Green span, or finite zero table
is used to prove that source-specific nondegeneracy.
-/

/-- Exact finite-rank Schwartz synthesis of 242 explicit columns. -/
def neutralNF544BumpSynthesis (b : Fin 242 → 𝓢(ℝ, ℂ)) :
    (Fin 242 → ℂ) →ₗ[ℂ] 𝓢(ℝ, ℂ) :=
  (Pi.basisFun ℂ (Fin 242)).constr ℂ b

/-- The actual 242×242 moment/column Gram endomorphism.
Its entries are the TRUE original physical moments applied to the
TRUE compact-smooth correction functions (when b is instantiated
with the NF523 weighted j_i). -/
def neutralNF544PhysicalGram
    (M : NeutralNF543Moments) (b : Fin 242 → 𝓢(ℝ, ℂ)) :
    Module.End ℂ (Fin 242 → ℂ) :=
  M.comp ((SchwartzMap.toLpCLM ℂ ℂ 2 volume).toLinearMap.comp
    (neutralNF544BumpSynthesis b))

/-- A positive-definite (complex Hermitian) original moment Gram
has zero kernel. This is the only point where the original analytic
independence and weighted cutoff positivity must be supplied. -/
theorem neutralNF544PhysicalGram_injective_of_pos
    (M : NeutralNF543Moments) (b : Fin 242 → 𝓢(ℝ, ℂ))
    (hpos : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) * (neutralNF544PhysicalGram M b d) i).re) :
    Function.Injective (neutralNF544PhysicalGram M b) := by
  intro x y hxy
  by_contra hne
  have hd : x - y ≠ 0 := sub_ne_zero.mpr hne
  have hzero : neutralNF544PhysicalGram M b (x - y) = 0 := by
    rw [map_sub, hxy, sub_self]
  have hpositive := hpos (x - y) hd
  simp [hzero] at hpositive

/-- The inverse Gram is mathematically canonical once the TRUE
original physical Gram has been shown nonsingular. -/
def neutralNF544GramEquiv
    (M : NeutralNF543Moments) (b : Fin 242 → 𝓢(ℝ, ℂ))
    (hG : Function.Injective (neutralNF544PhysicalGram M b)) :
    (Fin 242 → ℂ) ≃ₗ[ℂ] (Fin 242 → ℂ) :=
  LinearEquiv.ofBijective (neutralNF544PhysicalGram M b)
    ⟨hG, (LinearMap.injective_iff_surjective).mp hG⟩

/-- CONSTRUCT the 242-direction correction from the original columns
and inverse Gram. No independent right-inverse is assumed. -/
def neutralNF544GramRightInverse
    (M : NeutralNF543Moments) (b : Fin 242 → 𝓢(ℝ, ℂ))
    (hG : Function.Injective (neutralNF544PhysicalGram M b)) :
    NeutralNF543RightInverse :=
  (neutralNF544BumpSynthesis b).comp
    (neutralNF544GramEquiv M b hG).symm.toLinearMap

/-- Explicit 242×242 Gram inversion DISCHARGES the NF543 right
inverse obligation, without knowing or guessing any matrix entry. -/
theorem neutralNF544GramRightInverse_correct
    (M : NeutralNF543Moments) (b : Fin 242 → 𝓢(ℝ, ℂ))
    (hG : Function.Injective (neutralNF544PhysicalGram M b))
    (d : Fin 242 → ℂ) :
    M (((neutralNF544GramRightInverse M b hG) d).toLp 2 volume) = d := by
  change neutralNF544PhysicalGram M b
      ((neutralNF544GramEquiv M b hG).symm d) = d
  exact (neutralNF544GramEquiv M b hG).apply_symm_apply d

/-- A finite Schwartz synthesis remains supported in the ORIGINAL
two collars whenever each of its 242 columns is supported there. -/
theorem neutralNF544BumpSynthesis_supported
    (b : Fin 242 → 𝓢(ℝ, ℂ))
    (hb : ∀ (j : Fin 242) (x : ℝ),
      x ∉ neutralNF543OriginalCollars → (b j) x = 0)
    (d : Fin 242 → ℂ) (x : ℝ)
    (hx : x ∉ neutralNF543OriginalCollars) :
    (neutralNF544BumpSynthesis b d) x = 0 := by
  simp only [neutralNF544BumpSynthesis, Basis.constr_apply_fintype,
    Pi.basisFun_repr]
  simp [hb _ x hx]

/-- Exact-geometry support of the constructed Gram inverse. This
is NOT an extra right-inverse hypothesis: its support follows
from the explicit 242 source correction columns. -/
theorem neutralNF544GramRightInverse_supported
    (M : NeutralNF543Moments) (b : Fin 242 → 𝓢(ℝ, ℂ))
    (hG : Function.Injective (neutralNF544PhysicalGram M b))
    (hb : ∀ (j : Fin 242) (x : ℝ),
      x ∉ neutralNF543OriginalCollars → (b j) x = 0)
    (d : Fin 242 → ℂ) (x : ℝ)
    (hx : x ∉ neutralNF543OriginalCollars) :
    ((neutralNF544GramRightInverse M b hG) d) x = 0 := by
  exact neutralNF544BumpSynthesis_supported b hb
    ((neutralNF544GramEquiv M b hG).symm d) x hx

/-- Positivity of the TRUE 242-dimensional Gram plus the 242 real
source-supported Schwartz correction columns is sufficient for
simultaneous SAME-SOURCE logarithmic-domain admission, strict
original support and ALL 242 exact original moments. No separately
assumed R occurs anywhere in this theorem. -/
theorem neutralNF544OriginalGram_correctedSmoothLogCarrier
    (M : NeutralNF543Moments)
    (b : Fin 242 → 𝓢(ℝ, ℂ))
    (hGram : ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) * (neutralNF544PhysicalGram M b d) i).re)
    (hb : ∀ (j : Fin 242) (x : ℝ),
      x ∉ neutralNF543OriginalCollars → (b j) x = 0)
    (ell : RealComplexL2) (g : 𝓢(ℝ, ℂ))
    (hg : ∀ x : ℝ, x ∉ neutralNF543OriginalCollars → g x = 0) :
    ∃ k : NeutralLogHilbertCarrier (11 / 10 : ℝ),
      neutralLogPhysical k.val =
          (neutralNF543Correct M
            (neutralNF544GramRightInverse M b
              (neutralNF544PhysicalGram_injective_of_pos M b hGram))
            ell g).toLp 2 volume ∧
        M ((neutralNF543Correct M
            (neutralNF544GramRightInverse M b
              (neutralNF544PhysicalGram_injective_of_pos M b hGram))
            ell g).toLp 2 volume) = M ell := by
  let hG := neutralNF544PhysicalGram_injective_of_pos M b hGram
  exact neutralNF543Correct_hasOriginalLogCarrierAnd242Moments
    M (neutralNF544GramRightInverse M b hG)
    (neutralNF544GramRightInverse_correct M b hG)
    ell g hg
    (neutralNF544GramRightInverse_supported M b hG hb)

end
end WeilDefect
