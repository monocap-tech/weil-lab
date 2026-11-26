import WeilDefect.Arithmetic.ActualZetaIV105OriginalPackedSchurResponse
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

/-- The genuine complex signed Gram, not the diagonal physical mass Gram. -/
def neutralIV106Gram (k : ℕ) (hk : 0 < k) : Matrix (Fin k) (Fin k) ℂ :=
  neutralIV007OriginalMixedEntry (11/10:ℝ) (neutralIV100Carrier k hk)

theorem neutralIV106Gram_energy (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ) :
    (∑ i : Fin k, conj (c i) * (neutralIV106Gram k hk).mulVec c i).re =
      neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk c) := by
  have hs (i : Fin k) := neutralIV009OriginalCollars_supported_window _
    (neutralIV100Carrier_collars k hk i)
  have h := neutralIV009FiniteMixedEnergy_eq_literalSchwartzDiagonal
    (11/10:ℝ) (neutralIV100Carrier k hk) c hs
  have he : (∑ i : Fin k, conj (c i) * (neutralIV106Gram k hk).mulVec c i) =
      neutralIV007OriginalMixedEnergy (11/10:ℝ) (neutralIV100Carrier k hk) c := by
    unfold neutralIV007OriginalMixedEnergy
    apply Finset.sum_congr rfl
    intro i hi
    change conj (c i) * (∑ j : Fin k,
      neutralIV007OriginalMixedEntry (11/10:ℝ) (neutralIV100Carrier k hk) i j * c j) = _
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j hj
    ring
  rw [he]
  exact congrArg Complex.re h

theorem neutralIV106Gram_kernel (k : ℕ) (hk : 0 < k) (c : Fin k → ℂ)
    (hc : (neutralIV106Gram k hk).mulVec c = 0) : c = 0 := by
  have he := neutralIV106Gram_energy k hk c
  rw [hc] at he
  simp only [Pi.zero_apply, mul_zero, Finset.sum_const_zero, Complex.zero_re] at he
  have hm := neutralIV101Packed_full_margin k hk c
  have hz : ‖(neutralIV100Packed k hk c).toLp 2 volume‖^2 = 0 := by
    linarith only [hm, he, sq_nonneg ‖(neutralIV100Packed k hk c).toLp 2 volume‖]
  funext i
  exact (neutralIV100Packed_mass_zero_iff k hk c).mp hz i

theorem neutralIV106Gram_injective (k : ℕ) (hk : 0 < k) :
    Function.Injective (neutralIV106Gram k hk).mulVec := by
  intro c d hcd
  have hz : (neutralIV106Gram k hk).mulVec (c - d) = 0 := by
    funext i
    have hi := congrFun hcd i
    change (∑ j : Fin k, neutralIV106Gram k hk i j * c j) =
      ∑ j : Fin k, neutralIV106Gram k hk i j * d j at hi
    change (∑ j : Fin k, neutralIV106Gram k hk i j * (c j - d j)) = 0
    simp only [mul_sub, Finset.sum_sub_distrib, hi, sub_self]
  exact sub_eq_zero.mp (neutralIV106Gram_kernel k hk (c-d) hz)

theorem neutralIV106Gram_isUnit (k : ℕ) (hk : 0 < k) :
    IsUnit (neutralIV106Gram k hk) :=
  Matrix.mulVec_injective_iff_isUnit.mp (neutralIV106Gram_injective k hk)

theorem neutralIV106Gram_surjective (k : ℕ) (hk : 0 < k) :
    Function.Surjective (neutralIV106Gram k hk).mulVec :=
  Matrix.mulVec_surjective_iff_isUnit.mpr (neutralIV106Gram_isUnit k hk)

def neutralIV106CrossRHS (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ)) : Fin k → ℂ :=
  fun i => neutralIV101Mixed (11/10:ℝ) (neutralIV100Carrier k hk i) v

/-- Solvability of the original signed response equations on every row.
The extension from rows to arbitrary packed first arguments is separate. -/
theorem neutralIV106Response_exists (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ)) :
    ∃ d : Fin k → ℂ, (neutralIV106Gram k hk).mulVec d =
      neutralIV106CrossRHS k hk v :=
  neutralIV106Gram_surjective k hk (neutralIV106CrossRHS k hk v)

def neutralIV106Response (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ)) : Fin k → ℂ :=
  Classical.choose (neutralIV106Response_exists k hk v)

theorem neutralIV106Response_solves (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ)) :
    (neutralIV106Gram k hk).mulVec (neutralIV106Response k hk v) =
      neutralIV106CrossRHS k hk v :=
  Classical.choose_spec (neutralIV106Response_exists k hk v)

theorem neutralIV106Response_unique (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ))
    (d : Fin k → ℂ)
    (hd : (neutralIV106Gram k hk).mulVec d = neutralIV106CrossRHS k hk v) :
    d = neutralIV106Response k hk v :=
  neutralIV106Gram_injective k hk (hd.trans (neutralIV106Response_solves k hk v).symm)

#print axioms neutralIV106Gram_energy
#print axioms neutralIV106Gram_kernel
#print axioms neutralIV106Gram_injective
#print axioms neutralIV106Gram_isUnit
#print axioms neutralIV106Gram_surjective
#print axioms neutralIV106Response_exists
#print axioms neutralIV106Response_solves
#print axioms neutralIV106Response_unique

end
end WeilDefect
