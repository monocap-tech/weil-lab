import WeilDefect.Arithmetic.ActualZetaIV106D4CellEnergy

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped BigOperators

/-- Null endpoints remove the distinction between closed cells and oriented integrals. -/
theorem neutralIV106D5Closed_cell (v : ℝ → ℂ) (l r : ℝ) (hlr : l ≤ r)
    (hm : (∫ t in Set.Icc l r, v t) = 0) :
    (∫ t in l..r, v t) = 0 := by
  rw [intervalIntegral.integral_of_le hlr, ← integral_Icc_eq_integral_Ioc]
  exact hm

/-- Integrate the actual pointwise primitive bound on a single cell. -/
theorem neutralIV106D5Cell_energy (v V : ℝ → ℂ)
    (hv : Continuous v) (hV : Continuous V) (l r : ℝ) (hlr : l < r)
    (hm : (∫ t in l..r, v t) = 0)
    (hp : ∀ x ∈ Set.Icc l r, V x = ∫ t in l..x, v t) :
    (∫ x in l..r, ‖V x‖^2) ≤ (r-l)^2/6 * (∫ x in l..r, ‖v x‖^2) := by
  let E : ℝ := ∫ x in l..r, ‖v x‖^2
  have hf : Continuous (fun x => ‖V x‖^2) := hV.norm.pow 2
  have hg : Continuous (fun x : ℝ => ((x-l)*(r-x)/(r-l))*E) :=
    ((((continuous_id.sub continuous_const).mul
      (continuous_const.sub continuous_id)).div_const _).mul continuous_const)
  calc
    _ ≤ ∫ x in l..r, ((x-l)*(r-x)/(r-l))*E := by
      apply intervalIntegral.integral_mono_on hlr.le
        (hf.intervalIntegrable (μ := volume) l r)
        (hg.intervalIntegrable (μ := volume) l r)
      intro x hx
      rw [hp x hx]
      exact neutralIV106D4Point v hv l r x hlr hx.1 hx.2 hm
    _ = _ := by
      rw [intervalIntegral.integral_mul_const, neutralIV106D4Envelope l r hlr]

/-- Assemble equal-width local energy estimates into the whole window. -/
theorem neutralIV106D5Partition_energy (v V : ℝ → ℂ)
    (hv : Continuous v) (hV : Continuous V)
    (p : ℕ → ℝ) (N : ℕ) (h : ℝ) (hh : 0 < h)
    (hw : ∀ j < N, p (j+1)-p j = h)
    (hm : ∀ j < N, (∫ x in p j..p (j+1), v x) = 0)
    (hp : ∀ j < N, ∀ x ∈ Set.Icc (p j) (p (j+1)),
      V x = ∫ t in p j..x, v t) :
    (∫ x in p 0..p N, ‖V x‖^2) ≤ h^2/6 * (∫ x in p 0..p N, ‖v x‖^2) := by
  have hvi : ∀ j < N, IntervalIntegrable (fun x => ‖v x‖^2) volume (p j) (p (j+1)) :=
    fun j _ => (hv.norm.pow 2).intervalIntegrable _ _
  have hVi : ∀ j < N, IntervalIntegrable (fun x => ‖V x‖^2) volume (p j) (p (j+1)) :=
    fun j _ => (hV.norm.pow 2).intervalIntegrable _ _
  rw [← intervalIntegral.sum_integral_adjacent_intervals hVi,
    ← intervalIntegral.sum_integral_adjacent_intervals hvi, Finset.mul_sum]
  apply Finset.sum_le_sum
  intro j hj
  have hjN := Finset.mem_range.mp hj
  have hjp : p j < p (j+1) := sub_pos.mp (by rw [hw j hjN]; exact hh)
  have hc := neutralIV106D5Cell_energy v V hv hV (p j) (p (j+1)) hjp
    (hm j hjN) (hp j hjN)
  rwa [hw j hjN] at hc

#print axioms neutralIV106D5Closed_cell
#print axioms neutralIV106D5Cell_energy
#print axioms neutralIV106D5Partition_energy
end
end WeilDefect
