import WeilDefect.MasterRecon.V10B7b
import WeilDefect.MasterRecon.V10B7c
import WeilDefect.MasterRecon.V10B6h

/-! V10B7d: the local zero-count theorem with no external arithmetic
hypotheses. Native certification of the imported modules is required. -/
namespace WeilDefect.MasterRecon.V10B7d

theorem elementary_bound : V10B7b.ElementaryZetaBound :=
  V10B7c.elementary_growth

theorem halfPlane_growth : V10B7a.HalfPlaneGrowth :=
  V10B7b.growth_of_elementary_bound elementary_bound

theorem local_count :
    ∃ A : ℝ, 1 ≤ A ∧ ∀ t : ℝ,
      (V09D.count t (t+1) : ℝ) ≤ A*Real.log (|t|+3) :=
  V10B7b.local_count_of_elementary_bound elementary_bound
    V10B6h.strip_reflection_closed V10B6h.strip_reflection_mult

theorem integer_local_count :
    ∃ A : ℝ, 0 ≤ A ∧ ∀ n : ℤ,
      (V09D.count (n:ℝ) ((n:ℝ)+1) : ℝ) ≤ A*Real.log (|(n:ℝ)|+3) := by
  obtain ⟨A,hA,h⟩ := local_count
  exact ⟨A,by linarith,fun n => h (n:ℝ)⟩

end WeilDefect.MasterRecon.V10B7d

#print axioms WeilDefect.MasterRecon.V10B7d.elementary_bound
#print axioms WeilDefect.MasterRecon.V10B7d.halfPlane_growth
#print axioms WeilDefect.MasterRecon.V10B7d.local_count
#print axioms WeilDefect.MasterRecon.V10B7d.integer_local_count
