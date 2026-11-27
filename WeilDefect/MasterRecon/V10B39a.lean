import WeilDefect.MasterRecon.V10B33a
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.Algebra.Polynomial.Degree.Operations

/-! V10B39a: finite polynomial span from a degree-graded family.
The proof cancels the highest coefficient; no completeness is assumed. -/
namespace WeilDefect.MasterRecon.V10B39a
open Polynomial
open scoped BigOperators

theorem graded_top_nonzero (p : ℝ[X]) (n : ℕ)
    (h : p.degree = n) : p.coeff n ≠ 0 := by
  have hn : p.natDegree = n := natDegree_eq_of_degree_eq_some h
  have hp : p ≠ 0 := by
    intro hz
    simp [hz] at h
  rw [← hn,coeff_natDegree]
  exact leadingCoeff_ne_zero.mpr hp

theorem graded_cancel (p q : ℝ[X]) (n : ℕ)
    (hp : p.degree < (n+1:ℕ)) (hq : q.degree = n) :
    (p-C (p.coeff n/q.coeff n)*q).degree < n := by
  apply (degree_lt_iff_coeff_zero _ n).mpr
  intro k hk
  rw [coeff_sub,coeff_C_mul]
  by_cases he : k=n
  · subst k
    have hn := graded_top_nonzero q n hq
    field_simp [hn]
  · have hk' : n+1 ≤ k := by omega
    have hz := (degree_lt_iff_coeff_zero p (n+1)).mp hp k hk'
    have hz' := (degree_lt_iff_coeff_zero q (n+1)).mp
      (show q.degree < (n+1:ℕ) by rw [hq]; exact_mod_cast Nat.lt_succ_self n) k hk'
    rw [hz,hz',mul_zero,sub_zero]

theorem graded_span (q : ℕ → ℝ[X]) (hq : ∀ j, (q j).degree = j) :
    ∀ n (p : ℝ[X]), p.degree < n →
      ∃ a : ℕ → ℝ, p = ∑ j ∈ Finset.range n, C (a j)*q j := by
  intro n
  induction n with
  | zero =>
    intro p hp
    have hz : p=0 := by
      ext k
      rw [coeff_zero]
      exact (degree_lt_iff_coeff_zero p 0).mp hp k (Nat.zero_le k)
    exact ⟨fun _ => 0,by simp [hz]⟩
  | succ n ih =>
    intro p hp
    let c := p.coeff n/(q n).coeff n
    let r := p-C c*q n
    have hr : r.degree < n := graded_cancel p (q n) n hp (hq n)
    obtain ⟨a,ha⟩ := ih r hr
    let b : ℕ → ℝ := fun j => if j=n then c else a j
    refine ⟨b,?_⟩
    rw [Finset.sum_range_succ]
    have hs : (∑ j ∈ Finset.range n, C (b j)*q j) =
        ∑ j ∈ Finset.range n, C (a j)*q j := by
      apply Finset.sum_congr rfl
      intro j hj
      have hne : j ≠ n := Nat.ne_of_lt (Finset.mem_range.mp hj)
      simp [b,hne]
    rw [hs,← ha]
    simp only [b,if_pos rfl]
    dsimp [r]
    ring

noncomputable def shiftedReal (j : ℕ) : ℝ[X] :=
  (shiftedLegendre j).map (Int.castRingHom ℝ)

theorem shiftedReal_degree (j : ℕ) : (shiftedReal j).degree = j := by
  unfold shiftedReal
  have hi : Function.Injective (Int.castRingHom ℝ) := by
    intro a b h
    exact_mod_cast h
  rw [Polynomial.degree_map_eq_of_injective hi,degree_shiftedLegendre]

theorem shiftedReal_span (n : ℕ) (p : ℝ[X]) (hp : p.degree < n) :
    ∃ a : ℕ → ℝ, p = ∑ j ∈ Finset.range n, C (a j)*shiftedReal j :=
  graded_span shiftedReal shiftedReal_degree n p hp

end WeilDefect.MasterRecon.V10B39a

#print axioms WeilDefect.MasterRecon.V10B39a.graded_top_nonzero
#print axioms WeilDefect.MasterRecon.V10B39a.graded_cancel
#print axioms WeilDefect.MasterRecon.V10B39a.graded_span
#print axioms WeilDefect.MasterRecon.V10B39a.shiftedReal_degree
#print axioms WeilDefect.MasterRecon.V10B39a.shiftedReal_span
