import WeilDefect.Arithmetic.ActualZetaOriginalJ242FiniteRootBudget
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF566 — translate a finite LIST of distinct weighted real roots
into the Mathlib Finset root-multiplicity degree obstruction.

This is the final generic combinatorial gate before attaching
the EXACT original 67 oscillator square nodes and the genuine
negative sinh node. The proof uses a genuine finite set of
distinct nodes and retains the multiplicities from each list
entry, with NO duplicate-counting assumption.

No original source independence assumption is introduced.
-/

/-- The total multiplicity of a list of pairwise distinct real
root nodes cannot exceed a nonzero polynomial's natural degree.
Unlike a list sum without a nodup premise, this certificate
cannot count a repeated node twice. -/
theorem neutralNF566WeightedNodeListDegreeStop
    (p : Polynomial ℝ) (l : List (ℝ × ℕ))
    (hDistinct : (l.map Prod.fst).Nodup)
    (hRoots : ∀ q ∈ l, q.2 ≤ rootMultiplicity q.1 p)
    (hBudget : p.natDegree < (l.map Prod.snd).sum) :
    p = 0 := by
  classical
  have hList : l.Nodup := hDistinct.of_map
  let s : Finset (ℝ × ℕ) := l.toFinset
  let t : Finset ℝ := s.image Prod.fst
  have hInj : Set.InjOn (fun q : ℝ × ℕ => q.1) (s : Set (ℝ × ℕ)) := by
    intro q hq r hr hqr
    have hq' : q ∈ l := by simpa only [s, List.mem_toFinset] using hq
    have hr' : r ∈ l := by simpa only [s, List.mem_toFinset] using hr
    exact (List.nodup_map_iff_inj_on hList).mp hDistinct q hq' r hr' hqr
  let m : ℝ → ℕ := fun x =>
    if h : ∃ q : ℝ × ℕ, q ∈ s ∧ q.1 = x then
      (Classical.choose h).2
    else 0
  have hm (q : ℝ × ℕ) (hq : q ∈ s) : m q.1 = q.2 := by
    dsimp [m]
    split_ifs with h
    · have hc := Classical.choose_spec h
      have hSame : Classical.choose h = q :=
        hInj hc.1 hq hc.2
      exact congrArg Prod.snd hSame
    · exact False.elim (h ⟨q, hq, rfl⟩)
  have hBound : ∀ x ∈ t, m x ≤ rootMultiplicity x p := by
    intro x hx
    obtain ⟨q, hq, hqx⟩ := Finset.mem_image.mp hx
    subst x
    rw [hm q hq]
    apply hRoots q
    simpa only [s, List.mem_toFinset] using hq
  have hSum : (∑ x ∈ t, m x) = (l.map Prod.snd).sum := by
    calc
      (∑ x ∈ t, m x) = ∑ q ∈ s, m q.1 := by
        exact Finset.sum_image hInj
      _ = ∑ q ∈ s, q.2 := by
        apply Finset.sum_congr rfl
        intro q hq
        exact hm q hq
      _ = (l.map Prod.snd).sum := by
        simpa only [List.sum_map] using
          (List.sum_toFinset (fun q : ℝ × ℕ => q.2) hList).symm
  exact neutralNF565FiniteDistinctRootMultiplicityDegreeStop
    p t m hBound (by rw [hSum]; exact hBudget)

end
end WeilDefect
