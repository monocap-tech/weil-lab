module

public import Zeta.Main

/-!
CP011: canonical positive-zero roster EXHAUSTION via the actual upstream
Turing count + independent no-duplicate original certified interval witnesses.

This is a Lean SOURCE PROOF CANDIDATE under isolated Zeta 4.35.
Compiling a source candidate and auditing the real .olean are still OPEN.
No numerical zero refinement or original Weil arithmetic equality is claimed.

The proof adapts the upstream proof of
  riemannZeta.ne_zero_of_re_ne_half_upto
in Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean, but handles ALL zeros on
the positive-height domain, not just off-critical-line zeros.
-/

@[expose] public section

open Set Zeta.Certificates

namespace CP011CanonicalRoster

/-- Every genuine nontrivial zeta zero with ordinate in the positive certified
Gram window occurs in the original canonical interval witness list.
Nothing is added to the axiom set: a hypothetical missing root would yield
N(g) >= n+1, while the real upstream Turing count says N(g)=n. -/
theorem every_positive_zero_is_original_witness
    (Z : CertifiedZeroCount) {s : ℂ}
    (hs : s.im ∈ Ioo 0 (gramPoint Z.minIdx))
    (hz : riemannZeta s = 0) : s ∈ Z.zeros := by
  by_contra hnot
  let extra : List ℂ := s :: Z.zeros
  have hbound := riemannZeta.le_N_of_zeros
    (T := gramPoint Z.minIdx) extra
    (by
      simp only [List.mem_cons, forall_eq_or_imp, extra]
      refine ⟨⟨hs, hz⟩, fun a ha ↦ ?_⟩
      exact ⟨Ioo_subset_Ioo le_rfl Z.below (Z.zeros_im ha),
        (Z.zeros_spec a ha).2⟩)
    (by simp [extra, hnot, Z.zeros_nodup])
  have hN : riemannZeta.N (gramPoint Z.minIdx) =
      Z.intervals.length :=
    riemannZeta.N_gramPoint_eq Z
  have hfalse : (((Z.intervals.length + 1 : ℕ) : ℝ) ≤
      (Z.intervals.length : ℝ)) := by
    simpa [extra, Z.zeros_length, hN] using hbound
  have hstrict : ((Z.intervals.length : ℕ) : ℝ) <
      (((Z.intervals.length + 1 : ℕ) : ℝ)) := by
    exact_mod_cast Nat.lt_succ_self Z.intervals.length
  exact (not_lt_of_ge hfalse) hstrict

/-- Distinct source slots are separated in their physical zero-ordinate
coordinate, using the upstream CertifiedZeroIntervals.pairwise theorem. -/
private theorem original_slots_separated (Z : CertifiedZeroCount)
    {A B : NonemptyInterval ℝ} (hA : A ∈ Z.intervals)
    (hB : B ∈ Z.intervals) (hne : A ≠ B) :
    A.snd ≤ B.fst ∨ B.snd ≤ A.fst := by
  have hpg := List.pairwise_iff_getElem.mp Z.pairwise
  obtain ⟨i, hi, rfl⟩ := List.mem_iff_getElem.mp hA
  obtain ⟨j, hj, rfl⟩ := List.mem_iff_getElem.mp hB
  rcases lt_trichotomy i j with h | h | h
  · exact Or.inl (hpg i j hi hj h)
  · subst j; exact absurd rfl hne
  · exact Or.inr (hpg j i hj hi h)

/-- The concrete original witness list has AT MOST ONE chosen zero whose
ordinate belongs to the open interior of a single certified original slot.
This uses genuine source zero-to-slot proof lineage, not a numerical guess. -/
private theorem witness_members_same_slot_eq (Z : CertifiedZeroCount)
    {A : NonemptyInterval ℝ} (hA : A ∈ Z.intervals)
    {s t : ℂ} (hs : s ∈ Z.zeros) (ht : t ∈ Z.zeros)
    (hsA : s.im ∈ Ioo A.fst A.snd)
    (htA : t.im ∈ Ioo A.fst A.snd) : s = t := by
  simp only [CertifiedZeroIntervals.zeros, List.mem_map] at hs ht
  rcases hs with ⟨u, hu, rfl⟩
  rcases ht with ⟨v, hv, rfl⟩
  simp only [one_div, List.mem_pmap] at hu hv
  obtain ⟨J, hJ, rfl⟩ := hu
  obtain ⟨K, hK, rfl⟩ := hv
  have hJroot := (Z.has_zero J hJ).choose_spec.1
  have hKroot := (Z.has_zero K hK).choose_spec.1
  have hJI : (Z.has_zero J hJ).choose ∈ Ioo A.fst A.snd := by
    simpa using hsA
  have hKI : (Z.has_zero K hK).choose ∈ Ioo A.fst A.snd := by
    simpa using htA
  have heqJ : J = A := by
    by_contra hne
    rcases original_slots_separated Z hJ hA hne with h | h
    · exact absurd (lt_of_lt_of_le hJroot.2 h |>.trans hJI.1)
        (not_lt.mpr le_rfl)
    · exact absurd (lt_of_lt_of_le hJI.2 h |>.trans hJroot.1)
        (not_lt.mpr le_rfl)
  have heqK : K = A := by
    by_contra hne
    rcases original_slots_separated Z hK hA hne with h | h
    · exact absurd (lt_of_lt_of_le hKroot.2 h |>.trans hKI.1)
        (not_lt.mpr le_rfl)
    · exact absurd (lt_of_lt_of_le hKI.2 h |>.trans hKroot.1)
        (not_lt.mpr le_rfl)
  subst J
  subst K
  rfl

/-- Any two zeros whose ordinates lie INSIDE THE SAME original certified
interval are EQUAL, without assuming uniqueness separately. The upstream
Turing count enforces exhaustivity and the original disjoint slots enforce
the source index. It applies to a new Euler or RS refined candidate once
that candidate has its actual Hardy-Z kernel certificate and source nesting. -/
theorem unique_zero_in_original_slot (Z : CertifiedZeroCount)
    {A : NonemptyInterval ℝ} (hA : A ∈ Z.intervals)
    {s t : ℂ}
    (hsA : s.im ∈ Ioo A.fst A.snd)
    (htA : t.im ∈ Ioo A.fst A.snd)
    (hzs : riemannZeta s = 0)
    (hzt : riemannZeta t = 0) : s = t := by
  have hsG : s.im ∈ Ioo 0 (gramPoint Z.minIdx) :=
    ⟨(Z.fst_nonneg A hA).trans_lt hsA.1,
      hsA.2.trans_le ((Z.le_height hA).trans Z.below)⟩
  have htG : t.im ∈ Ioo 0 (gramPoint Z.minIdx) :=
    ⟨(Z.fst_nonneg A hA).trans_lt htA.1,
      htA.2.trans_le ((Z.le_height hA).trans Z.below)⟩
  exact witness_members_same_slot_eq Z hA
    (every_positive_zero_is_original_witness Z hsG hzs)
    (every_positive_zero_is_original_witness Z htG hzt) hsA htA

/-- Concrete pinned 1,748,002-root Turing-certificate specialization.
This gives exact membership of every positive zero below the source Gram point,
not a numerical ordinate enclosure or a new RH claim. -/
theorem pinned_external_positive_root_is_member {s : ℂ}
    (hs : s.im ∈ Ioo 0
       (gramPoint certifiedZeroCount.minIdx))
    (hz : riemannZeta s = 0) :
    s ∈ certifiedZeroCount.zeros :=
  every_positive_zero_is_original_witness certifiedZeroCount hs hz

end CP011CanonicalRoster

#print axioms CP011CanonicalRoster.every_positive_zero_is_original_witness
#print axioms CP011CanonicalRoster.unique_zero_in_original_slot
#print axioms CP011CanonicalRoster.pinned_external_positive_root_is_member
