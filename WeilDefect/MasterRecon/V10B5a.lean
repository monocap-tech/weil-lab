import WeilDefect.MasterRecon.V10B4f
import WeilDefect.MasterRecon.V10B2
import WeilDefect.MasterRecon.V10A2
import Mathlib.Topology.Algebra.InfiniteSum.ENNReal

/-! V10B5a: arbitrary finite sample banks grouped by right-closed
unit-height cells, then extended to the full nonnegative sum.
The per-cell count and global weighted rectangle energy budget are
explicit hypotheses, not arithmetic facts proved in this module. -/
namespace WeilDefect.MasterRecon.V10B5a

open Set MeasureTheory
open scoped ENNReal BigOperators

noncomputable def cell (y : ℝ) : ℤ := ⌈y⌉ - 1

theorem cell_mem (y : ℝ) : y ∈ Ioc (cell y : ℝ) ((cell y : ℝ)+1) := by
  unfold cell
  simp only [Int.cast_sub, Int.cast_one, mem_Ioc, sub_add_cancel]
  exact ⟨by linarith [Int.ceil_lt_add_one y], Int.le_ceil y⟩

theorem cell_unique (y : ℝ) (n : ℤ)
    (hn : y ∈ Ioc (n : ℝ) ((n : ℝ)+1)) : cell y = n := by
  have hc : ⌈y⌉ = n+1 := by
    apply Int.ceil_eq_iff.mpr
    push_cast
    constructor
    · linarith [hn.1]
    · exact hn.2
  simp [cell, hc]

theorem cell_closed (y : ℝ) : y ∈ Icc (cell y : ℝ) ((cell y : ℝ)+1) :=
  ⟨(cell_mem y).1.le, (cell_mem y).2⟩

theorem finite_grouped_sampling {ι : Type*}
    (S : Finset ι) (ordinate m v : ι → ℝ) (E C : ℤ → ℝ)
    (hm : ∀ i, 0 ≤ m i) (hE : ∀ n, 0 ≤ E n)
    (hv : ∀ i, v i ≤ 4 * E (cell (ordinate i)))
    (hcount : ∀ n : ℤ, ∑ i ∈ S.filter (fun i => cell (ordinate i) = n), m i ≤ C n) :
    ∑ i ∈ S, m i * v i ≤ 4 * ∑ n ∈ S.image (fun i => cell (ordinate i)), C n * E n := by
  classical
  let c : ι → ℤ := fun i => cell (ordinate i)
  have hmap : ∀ i ∈ S, c i ∈ S.image c :=
    fun i hi => Finset.mem_image_of_mem c hi
  calc
    (∑ i ∈ S, m i * v i) =
        ∑ n ∈ S.image c, ∑ i ∈ S.filter (fun i => c i = n), m i * v i :=
      (Finset.sum_fiberwise_of_maps_to hmap (fun i => m i * v i)).symm
    _ ≤ 4 * ∑ n ∈ S.image c, C n * E n := by
      apply V10B2.finite_weighted_rectangles
      · exact fun _ _ i _ => hm i
      · intro n _ i hi
        have he := (Finset.mem_filter.mp hi).2
        change cell (ordinate i) = n at he
        simpa only [he] using hv i
      · exact fun n _ => hE n
      · exact fun n _ => hcount n

theorem infinite_sampling_of_budget {ι : Type*}
    (ordinate m v : ι → ℝ) (E C : ℤ → ℝ) (B : ℝ)
    (hm : ∀ i, 0 ≤ m i) (hv0 : ∀ i, 0 ≤ v i)
    (hE : ∀ n, 0 ≤ E n)
    (hv : ∀ i, v i ≤ 4 * E (cell (ordinate i)))
    (hcount : ∀ (S : Finset ι) (n : ℤ),
      ∑ i ∈ S.filter (fun i => cell (ordinate i) = n), m i ≤ C n)
    (hbudget : ∀ J : Finset ℤ, ∑ n ∈ J, C n * E n ≤ B) :
    ∑' i, ENNReal.ofReal (m i * v i) ≤ ENNReal.ofReal (4 * B) := by
  classical
  rw [ENNReal.tsum_eq_iSup_sum]
  apply iSup_le
  intro S
  rw [← ENNReal.ofReal_sum_of_nonneg (fun i _ => mul_nonneg (hm i) (hv0 i))]
  apply ENNReal.ofReal_le_ofReal
  exact (finite_grouped_sampling S ordinate m v E C hm hE hv (hcount S)).trans
    (mul_le_mul_of_nonneg_left (hbudget (S.image (fun i => cell (ordinate i)))) (by norm_num))

/-- A finite weighted energy budget with the local Riemann--von Mangoldt
logarithmic shape is sufficient for the full sample sum. -/
theorem infinite_log_sampling {ι : Type*}
    (ordinate m v : ι → ℝ) (E : ℤ → ℝ) (A B : ℝ)
    (hA : 0 ≤ A) (hm : ∀ i, 0 ≤ m i) (hv0 : ∀ i, 0 ≤ v i)
    (hE : ∀ n, 0 ≤ E n)
    (hv : ∀ i, v i ≤ 4 * E (cell (ordinate i)))
    (hcount : ∀ (S : Finset ι) (n : ℤ),
      ∑ i ∈ S.filter (fun i => cell (ordinate i) = n), m i ≤
        A * Real.log (|(n : ℝ)|+3))
    (hbudget : ∀ J : Finset ℤ, ∑ n ∈ J, Real.log (|(n : ℝ)|+3) * E n ≤ B) :
    ∑' i, ENNReal.ofReal (m i * v i) ≤ ENNReal.ofReal (4 * (A*B)) := by
  apply infinite_sampling_of_budget ordinate m v E
    (fun n => A * Real.log (|(n : ℝ)|+3)) (A*B) hm hv0 hE hv hcount
  intro J
  calc
    (∑ n ∈ J, (A * Real.log (|(n : ℝ)|+3)) * E n) =
        A * ∑ n ∈ J, Real.log (|(n : ℝ)|+3) * E n := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro n _
      ring
    _ ≤ A*B := mul_le_mul_of_nonneg_left (hbudget J) hA

end WeilDefect.MasterRecon.V10B5a

#print axioms WeilDefect.MasterRecon.V10B5a.cell_mem
#print axioms WeilDefect.MasterRecon.V10B5a.cell_unique
#print axioms WeilDefect.MasterRecon.V10B5a.cell_closed
#print axioms WeilDefect.MasterRecon.V10B5a.finite_grouped_sampling
#print axioms WeilDefect.MasterRecon.V10B5a.infinite_sampling_of_budget
#print axioms WeilDefect.MasterRecon.V10B5a.infinite_log_sampling
