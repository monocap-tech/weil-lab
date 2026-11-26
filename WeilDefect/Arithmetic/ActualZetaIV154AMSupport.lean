import WeilDefect.Arithmetic.ActualZetaIV152AMPhysicalEnvelope
import Mathlib.MeasureTheory.Function.Floor

namespace WeilDefect
noncomputable section
open MeasureTheory

/-- The physical weight is a measurable step function, without any
assumption on the native row bank. -/
theorem neutralIV154Measurable_weight : Measurable neutralIV152PhysicalWeight := by
  have h : Measurable (fun x : ℝ => (x+2)*4096) := by fun_prop
  exact (measurable_of_countable (fun i : ℤ => (neutralIV146Value i : ℝ))).comp h.floor

/-- Every point in the half-open physical window has a valid cell index. -/
theorem neutralIV154Window_index (x : ℝ) (hl : -2 ≤ x) (hu : x < 2) :
    ∃ i : ℕ, i < 16384 ∧ Int.floor ((x+2)*4096) = (i:ℤ) := by
  have h₀ : (0:ℤ) ≤ Int.floor ((x+2)*4096) := Int.le_floor.mpr (by push_cast; linarith)
  have h₁ : Int.floor ((x+2)*4096) < (16384:ℤ) := Int.floor_lt.mpr (by push_cast; linarith)
  let i := (Int.floor ((x+2)*4096)).toNat
  have hi : (i:ℤ) = Int.floor ((x+2)*4096) := Int.toNat_of_nonneg h₀
  exact ⟨i, by omega, hi.symm⟩

/-- Positivity on the entire half-open window conditional only on
the integer positivity bank. The right endpoint is deliberately excluded. -/
theorem neutralIV154Window_pos
    (hbank : ∀ i : ℕ, i < 16384 → 0 < neutralIV146Value (i:ℤ))
    (x : ℝ) (hl : -2 ≤ x) (hu : x < 2) :
    0 < neutralIV152PhysicalWeight x := by
  obtain ⟨i,hi,he⟩ := neutralIV154Window_index x hl hu
  unfold neutralIV152PhysicalWeight
  rw [he]
  exact_mod_cast hbank i hi

/-- A test function supported in the half-open window vanishes at
every zero of the physical weight, conditional on the integer bank. -/
theorem neutralIV154Zero_compatible (f : ℝ → ℝ)
    (hbank : ∀ i : ℕ, i < 16384 → 0 < neutralIV146Value (i:ℤ))
    (hf : ∀ x, x ∉ Set.Ico (-2:ℝ) 2 → f x = 0)
    (x : ℝ) (hx : neutralIV152PhysicalWeight x = 0) : f x = 0 := by
  apply hf
  intro h
  have hp := neutralIV154Window_pos hbank x h.1 h.2
  linarith

#print axioms neutralIV154Measurable_weight
#print axioms neutralIV154Window_index
#print axioms neutralIV154Window_pos
#print axioms neutralIV154Zero_compatible

end
end WeilDefect
