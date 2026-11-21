module

public import Zeta.Zeros.RiemannHypothesisUpTo.Basic
public import CP013Seam

/-!
CP014: formal bridge from an exhaustive COMPLETED finite-height count
and a source-separated finite root partition to an EXACT zero-count
at the Euler/RS seam c = 149500/1000.

This module deliberately keeps the missing root-to-finset coverage
as an EXPLICIT premise, not as an unproved consequence of a raw SHA,
individual BatchSpec witness, or source-prefix count alone.

Actual proof-source candidate only; requires real Lean v4.35 compile,
standard-axiom and .olean audit before any kernel PASS.
-/

@[expose] public section

open Set Zeta.Certificates

namespace CP014FiniteCut

/-- A finite root roster is exhausted by two disjoint witnesses when their
total cardinality equals that of the roster. This is a general set theorem:
it is NOT itself a zero-count certificate. -/
theorem exhausted_by_two_disjoint_parts {α : Type} [DecidableEq α]
    (S E R : Finset α)
    (hsubset : E ∪ R ⊆ S)
    (hdisjoint : Disjoint E R)
    (hcount : S.card = E.card + R.card) :
    S = E ∪ R := by
  have hcard : (E ∪ R).card = S.card := by
    rw [Finset.card_union_of_disjoint hdisjoint]
    omega
  exact (Finset.eq_of_subset_of_card_le hsubset (by omega)).symm

/-- The initial portion of an EXACT exhaustive finite two-method root
partition contains exactly the Euler-side roots. No zero can hide at the
cut: every source root lies strictly on one side. -/
theorem exact_low_partition (S E R : Finset ℂ) (c : ℝ)
    (hsubset : E ∪ R ⊆ S)
    (hdisjoint : Disjoint E R)
    (hcount : S.card = E.card + R.card)
    (hEuler : ∀ z ∈ E, z.im < c)
    (hRS : ∀ z ∈ R, c < z.im) :
    (S.filter (fun z : ℂ => z.im < c)).card = E.card := by
  have hpart := exhausted_by_two_disjoint_parts S E R hsubset hdisjoint hcount
  have hfilter : S.filter (fun z : ℂ => z.im < c) = E := by
    ext z
    constructor
    · intro hz
      have hzmem : z ∈ S := (Finset.mem_filter.mp hz).1
      have hzlt : z.im < c := (Finset.mem_filter.mp hz).2
      rw [hpart] at hzmem
      rcases Finset.mem_union.mp hzmem with hE | hR
      · exact hE
      · exact False.elim ((not_lt_of_ge (le_of_lt (hRS z hR))) hzlt)
    · intro hE
      exact Finset.mem_filter.mpr
        ⟨hsubset (Finset.mem_union.mpr (Or.inl hE)), hEuler z hE⟩
  rw [hfilter]

/-- Numerical source counts are specializations of the generic exact
partition. The MISSING antecedent is that the real finite set S of all
positive-height zeta zeros below g is covered by authentic kernel-root
witness sets E and R of the specified counts. -/
theorem original_seam_root_cardinality
    (S E R : Finset ℂ)
    (hsubset : E ∪ R ⊆ S)
    (hdisjoint : Disjoint E R)
    (hEcount : E.card = 52)
    (hRcount : R.card = 1747950)
    (hScount : S.card = 1748002)
    (hEuler : ∀ z ∈ E, z.im < (149500 : ℝ) / 1000)
    (hRS : ∀ z ∈ R, (149500 : ℝ) / 1000 < z.im) :
    (S.filter (fun z : ℂ => z.im < (149500 : ℝ) / 1000)).card = 52 := by
  have htotal : S.card = E.card + R.card := by
    omega
  rw [exact_low_partition S E R ((149500 : ℝ) / 1000)
      hsubset hdisjoint htotal hEuler hRS]
  exact hEcount

end CP014FiniteCut

#print axioms CP014FiniteCut.exhausted_by_two_disjoint_parts
#print axioms CP014FiniteCut.exact_low_partition
#print axioms CP014FiniteCut.original_seam_root_cardinality
