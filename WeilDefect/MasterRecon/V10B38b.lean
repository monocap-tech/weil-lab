import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic

/-! V10B38b: uniqueness on the uniform closure of a finite-span basis.
The approximation and vanishing pairings are explicit hypotheses. This
does not assume general L2 completeness or identify a literal load. -/
namespace WeilDefect.MasterRecon.V10B38b
open MeasureTheory Set
open scoped BigOperators

theorem finite_pairing_zero (r : ℝ → ℝ) (p : ℕ → ℝ → ℝ)
    (hr : Continuous r) (hp : ∀ j, Continuous (p j))
    (hz : ∀ j, (∫ x in (0:ℝ)..1, r x*p j x)=0)
    (n : ℕ) (a : ℕ → ℝ) :
    (∫ x in (0:ℝ)..1, r x*(∑ j ∈ Finset.range n, a j*p j x))=0 := by
  have he : (fun x : ℝ => r x*(∑ j ∈ Finset.range n, a j*p j x)) =
      fun x => ∑ j ∈ Finset.range n, a j*(r x*p j x) := by
    funext x
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro j _
    ring
  rw [he,intervalIntegral.integral_finsetSum]
  · simp only [intervalIntegral.integral_const_mul,hz,mul_zero,Finset.sum_const_zero]
  · intro j _
    exact (continuous_const.mul (hr.mul (hp j))).intervalIntegrable 0 1

theorem approx_energy_bound (r g : ℝ → ℝ) (hr : Continuous r)
    (hg : Continuous g) (hz : (∫ x in (0:ℝ)..1, r x*g x)=0)
    (ε : ℝ) (he : ∀ x ∈ Icc (0:ℝ) 1, |r x-g x| ≤ ε) :
    (∫ x in (0:ℝ)..1, r x*r x) ≤ ε*(∫ x in (0:ℝ)..1, |r x|) := by
  have hfun : (fun x : ℝ => r x*(r x-g x)) =
      fun x => r x*r x-r x*g x := by funext x; ring
  have hi : (∫ x in (0:ℝ)..1, r x*(r x-g x)) =
      ∫ x in (0:ℝ)..1, r x*r x := by
    rw [hfun,intervalIntegral.integral_sub ((hr.mul hr).intervalIntegrable 0 1)
      ((hr.mul hg).intervalIntegrable 0 1),hz,sub_zero]
  rw [← hi,← intervalIntegral.integral_const_mul]
  apply intervalIntegral.integral_mono_on (by norm_num)
    ((hr.mul (hr.sub hg)).intervalIntegrable 0 1)
    ((continuous_const.mul hr.abs).intervalIntegrable 0 1)
  intro x hx
  calc
    _ ≤ |r x*(r x-g x)| := le_abs_self _
    _ = |r x-g x|*|r x| := by rw [abs_mul,mul_comm]
    _ ≤ _ := mul_le_mul_of_nonneg_right (he x hx) (abs_nonneg _)

theorem uniform_span_unique (r : ℝ → ℝ) (p : ℕ → ℝ → ℝ)
    (hr : Continuous r) (hp : ∀ j, Continuous (p j))
    (hz : ∀ j, (∫ x in (0:ℝ)..1, r x*p j x)=0)
    (ha : ∀ ε : ℝ, 0 < ε → ∃ n : ℕ, ∃ a : ℕ → ℝ,
      ∀ x ∈ Icc (0:ℝ) 1, |r x-∑ j ∈ Finset.range n, a j*p j x| ≤ ε) :
    ∀ x ∈ Icc (0:ℝ) 1, r x=0 := by
  intro x hx
  by_contra hn
  let I : ℝ := ∫ x in (0:ℝ)..1, r x*r x
  let M : ℝ := ∫ x in (0:ℝ)..1, |r x|
  have hI : 0 < I := by
    apply intervalIntegral.integral_pos (by norm_num)
      (hr.mul hr).continuousOn
    · intro t _
      exact mul_self_nonneg _
    · exact ⟨x,hx,mul_self_pos.mpr hn⟩
  have hM : 0 ≤ M := intervalIntegral.integral_nonneg (by norm_num) (fun _ _ => abs_nonneg _)
  let ε : ℝ := I/(M+1)
  have hε : 0 < ε := div_pos hI (by linarith)
  obtain ⟨n,a,hclose⟩ := ha ε hε
  let g : ℝ → ℝ := fun x => ∑ j ∈ Finset.range n, a j*p j x
  have hg : Continuous g := by
    unfold g
    fun_prop
  have hgzero : (∫ x in (0:ℝ)..1, r x*g x)=0 :=
    finite_pairing_zero r p hr hp hz n a
  have hb := approx_energy_bound r g hr hg hgzero ε hclose
  change I ≤ ε*M at hb
  have heq : ε*(M+1)=I := by
    dsimp [ε]
    field_simp [show M+1 ≠ 0 by linarith]
  nlinarith only [hb,heq,hε]

end WeilDefect.MasterRecon.V10B38b

#print axioms WeilDefect.MasterRecon.V10B38b.finite_pairing_zero
#print axioms WeilDefect.MasterRecon.V10B38b.approx_energy_bound
#print axioms WeilDefect.MasterRecon.V10B38b.uniform_span_unique
