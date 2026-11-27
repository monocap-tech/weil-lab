import WeilDefect.MasterRecon.V10B40a

/-! V10B40d: exact finite odd deflation of a known basis expansion.
This is a finite identity, with no appeal to infinite completeness. -/
namespace WeilDefect.MasterRecon.V10B40d
open MeasureTheory Set
open scoped BigOperators
open WeilDefect.MasterRecon.V10B39b
open WeilDefect.MasterRecon.V10B40a

noncomputable def parity (j : ℕ) : ℝ := (1-(-1:ℝ)^j)/2

theorem odd_expansion (p : ℕ → ℝ → ℝ)
    (hr : ∀ j x, p j (1-x)=(-1:ℝ)^j*p j x)
    (m : ℕ) (a : ℕ → ℝ) (x : ℝ) :
    oddPart (fun t => ∑ j ∈ Finset.range m, a j*p j t) x =
      ∑ j ∈ Finset.range m, (parity j*a j)*p j x := by
  unfold oddPart
  rw [← Finset.sum_sub_distrib, Finset.sum_div]
  apply Finset.sum_congr rfl
  intro j _
  rw [hr]
  unfold parity
  ring

theorem project_prefix (p : ℕ → ℝ → ℝ) (d : ℕ → ℝ)
    (hp : ∀ j, Continuous (p j)) (hd : ∀ j, d j ≠ 0)
    (ho : ∀ i j, (∫ t in (0:ℝ)..1, p i t*p j t)=
      if i=j then (d j)⁻¹ else 0)
    (n m : ℕ) (hnm : n ≤ m) (a : ℕ → ℝ) (x : ℝ) :
    project p d n (fun t => ∑ j ∈ Finset.range m, a j*p j t) x =
      ∑ j ∈ Finset.range n, a j*p j x := by
  unfold project
  apply Finset.sum_congr rfl
  intro j hj
  have hjm : j ∈ Finset.range m :=
    Finset.mem_range.mpr ((Finset.mem_range.mp hj).trans_le hnm)
  rw [finite_pair p d hp hd ho m j hjm a]
  field_simp [hd j]

theorem deflate_expansion (p : ℕ → ℝ → ℝ) (d : ℕ → ℝ)
    (hp : ∀ j, Continuous (p j)) (hd : ∀ j, d j ≠ 0)
    (ho : ∀ i j, (∫ t in (0:ℝ)..1, p i t*p j t)=
      if i=j then (d j)⁻¹ else 0)
    (hr : ∀ j x, p j (1-x)=(-1:ℝ)^j*p j x)
    (n m : ℕ) (hnm : n ≤ m) (a : ℕ → ℝ) (x : ℝ) :
    deflate p d n (fun t => ∑ j ∈ Finset.range m, a j*p j t) x =
      (∑ j ∈ Finset.range m, (parity j*a j)*p j x)-
      (∑ j ∈ Finset.range n, (parity j*a j)*p j x) := by
  have he : oddPart (fun t => ∑ j ∈ Finset.range m, a j*p j t) =
      fun t => ∑ j ∈ Finset.range m, (parity j*a j)*p j t := by
    funext t
    exact odd_expansion p hr m a t
  unfold deflate
  rw [he,project_prefix p d hp hd ho n m hnm]

end WeilDefect.MasterRecon.V10B40d

#print axioms WeilDefect.MasterRecon.V10B40d.odd_expansion
#print axioms WeilDefect.MasterRecon.V10B40d.project_prefix
#print axioms WeilDefect.MasterRecon.V10B40d.deflate_expansion
