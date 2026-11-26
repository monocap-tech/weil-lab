import WeilDefect.Arithmetic.ActualZetaIV107OriginalPackedResponseExtension
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

/-- Individual row payments retain the physical mass of each original
generator and its actual signed arithmetic interaction with the residual. -/
def neutralIV108RowBudget (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ)) : ℝ :=
  ∑ i : Fin k, (5/2:ℝ) * ‖neutralIV106CrossRHS k hk v i‖^2 /
    neutralIV104Mass k hk i

theorem neutralIV108Young (m x y : ℝ) (hm : 0 < m) :
    2*x*y ≤ (2/5:ℝ)*m*x^2 + (5/2:ℝ)*y^2/m := by
  have h : (2*x*y - (2/5:ℝ)*m*x^2)*m ≤ (5/2:ℝ)*y^2 := by
    nlinarith only [sq_nonneg ((2/5:ℝ)*m*x-y)]
  have hh := (le_div_iff₀ hm).2 h
  linarith

theorem neutralIV108Row_payment (m : ℝ) (hm : 0 < m) (d b : ℂ) :
    2*(conj d*b).re ≤ (2/5:ℝ)*m*‖d‖^2 + (5/2:ℝ)*‖b‖^2/m := by
  have h : (conj d*b).re ≤ ‖d‖*‖b‖ := by
    simpa only [norm_mul, Complex.norm_conj] using Complex.re_le_norm (conj d*b)
  linarith only [h, neutralIV108Young m ‖d‖ ‖b‖ hm]

/-- The solved response pays exactly its own original signed quadratic energy. -/
theorem neutralIV108Response_energy (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ)) :
    neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk (neutralIV106Response k hk v)) =
      ∑ i : Fin k, (conj (neutralIV106Response k hk v i) *
        neutralIV106CrossRHS k hk v i).re := by
  have h := (neutralIV106Gram_energy k hk (neutralIV106Response k hk v)).symm
  rw [neutralIV106Response_solves] at h
  simpa only [Complex.re_sum] using h

/-- Upper bound on the response energy, with each cross row kept separate.
No uniform mixed operator norm or complementary positivity is presumed. -/
theorem neutralIV108Response_le_rowBudget (k : ℕ) (hk : 0 < k) (v : 𝓢(ℝ,ℂ)) :
    neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk (neutralIV106Response k hk v)) ≤
      neutralIV108RowBudget k hk v := by
  let d := neutralIV106Response k hk v
  let b := neutralIV106CrossRHS k hk v
  have hm := neutralIV101Packed_full_margin k hk d
  have hmass : ‖(neutralIV100Packed k hk d).toLp 2 volume‖^2 =
      ∑ i : Fin k, ‖d i‖^2 * neutralIV104Mass k hk i := by
    exact neutralIV099Sector_mass Finset.univ (neutralIV100Carrier k hk) d
      (neutralIV100Carrier_disjoint k hk)
  have hpay : (∑ i : Fin k, 2*(conj (d i)*b i).re) ≤
      ∑ i : Fin k, ((2/5:ℝ)*neutralIV104Mass k hk i*‖d i‖^2 +
        (5/2:ℝ)*‖b i‖^2/neutralIV104Mass k hk i) := by
    apply Finset.sum_le_sum
    intro i hi
    exact neutralIV108Row_payment _ (neutralIV100Carrier_mass_pos k hk i) _ _
  have henergy : neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk d) =
      ∑ i : Fin k, (conj (d i)*b i).re := neutralIV108Response_energy k hk v
  have hsum : (∑ i : Fin k, (2/5:ℝ)*neutralIV104Mass k hk i*‖d i‖^2) =
      (2/5:ℝ)*‖(neutralIV100Packed k hk d).toLp 2 volume‖^2 := by
    rw [hmass, Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro i hi
    ring
  rw [← Finset.mul_sum, ← henergy, Finset.sum_add_distrib, hsum] at hpay
  change _ ≤ (2/5:ℝ)*‖(neutralIV100Packed k hk d).toLp 2 volume‖^2 +
    neutralIV108RowBudget k hk v at hpay
  change neutralIV101Q (11/10:ℝ) (neutralIV100Packed k hk d) ≤ _
  linarith only [hpay, hm]

/-- Directional row-budget sufficient test for the exact Schur remainder. -/
theorem neutralIV108Schur_nonneg_of_rowBudget (k : ℕ) (hk : 0 < k)
    (v : 𝓢(ℝ,ℂ)) (h : neutralIV108RowBudget k hk v ≤ neutralIV101Q (11/10:ℝ) v) :
    0 ≤ neutralIV107SchurEnergy k hk v := by
  unfold neutralIV107SchurEnergy
  exact sub_nonneg.mpr (le_trans (neutralIV108Response_le_rowBudget k hk v) h)

#print axioms neutralIV108Young
#print axioms neutralIV108Row_payment
#print axioms neutralIV108Response_energy
#print axioms neutralIV108Response_le_rowBudget
#print axioms neutralIV108Schur_nonneg_of_rowBudget

end
end WeilDefect
