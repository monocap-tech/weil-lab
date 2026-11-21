module

public import CP011CanonicalRoster

/-!
CP012 — original certified Zeta slot ↔ proposed rational interval: explicit
MISSING kernel proof contract. Upstream BatchSpec n an ad bn bd publishes
only (length, first-left, last-right), NOT every index's endpoints.

The main theorem is CONDITIONAL on hslot : IndexedSlotContains Z k a b.
No arbitrary published source file hash can discharge hslot. Its proof must
come from a genuine original kernel certificate whose public statement
exposes the indexed zero interval or a sufficient ordinal containment fact.

The CP011 zero uniqueness theorem is itself only a source CANDIDATE until
the isolated actual v4.35 compiler/axiom audit reports acceptance.
-/

@[expose] public section

open Set Zeta.Certificates

namespace CP012RowReceipt

/-- Minimal new source-to-kernel bridge: the k-th ORIGINAL CERTIFIED
interval contains the two proposed bounds a<=b. This is weaker than
asserting byte-for-byte original source endpoints, but is exactly sufficient
to attach a rigorously proved refined root to the original zero ordinal. -/
structure IndexedSlotContains (Z : CertifiedZeroCount)
    (k : Fin Z.intervals.length) (a b : ℝ) : Prop where
  left_le : (Z.intervals.get k).fst ≤ a
  right_le : b ≤ (Z.intervals.get k).snd

/-- A stronger, optionally obtainable certificate: actual original
source row endpoints at the same source-indexed certified slot.
Source hashes and BatchSpec alone DO NOT prove this statement. -/
structure ExactSourceRowAt (Z : CertifiedZeroCount)
    (k : Fin Z.intervals.length) (a b : ℝ) : Prop where
  left_eq : (Z.intervals.get k).fst = a
  right_eq : (Z.intervals.get k).snd = b

theorem ExactSourceRowAt.implies_containment
    {Z : CertifiedZeroCount} {k : Fin Z.intervals.length}
    {a b : ℝ} (h : ExactSourceRowAt Z k a b) :
    IndexedSlotContains Z k a b :=
  ⟨h.left_eq.le, h.right_eq.ge⟩

/-- Actual ZERO identity transport from a kernel-certified refined root
(s, its exact ordinate interval, and ζ(s)=0) to the kth original source
slot. The NEW hslot hypothesis is explicit; it is not supplied by a
Git source-row hash or external BatchSpec boundary/length statement. -/
theorem refined_root_equals_canonical_at_index
    (Z : CertifiedZeroCount) (k : Fin Z.intervals.length)
    {a b : ℝ} (hslot : IndexedSlotContains Z k a b)
    {s : ℂ} (hs : s.im ∈ Ioo a b)
    (hz : riemannZeta s = 0) :
    ∃ t : ℝ,
      t ∈ Ioo (Z.intervals.get k).fst (Z.intervals.get k).snd ∧
      riemannZeta (1 / 2 + Complex.I * (t : ℂ)) = 0 ∧
      s = 1 / 2 + Complex.I * (t : ℂ) := by
  have hs_source :
      s.im ∈ Ioo (Z.intervals.get k).fst (Z.intervals.get k).snd :=
    ⟨lt_of_le_of_lt hslot.left_le hs.1,
      lt_of_lt_of_le hs.2 hslot.right_le⟩
  exact CP011CanonicalRoster.refined_root_identifies_original_slot
    Z k hs_source hz

/-- A byte-level exact-source-row certificate is *sufficient*, but the
weaker indexed interval-containment theorem above is all the downstream
arithmetic/spectral root identification really requires. -/
theorem refined_root_of_exact_source_row
    (Z : CertifiedZeroCount) (k : Fin Z.intervals.length)
    {a b : ℝ} (hsource : ExactSourceRowAt Z k a b)
    {s : ℂ} (hs : s.im ∈ Ioo a b)
    (hz : riemannZeta s = 0) :
    ∃ t : ℝ,
      t ∈ Ioo (Z.intervals.get k).fst (Z.intervals.get k).snd ∧
      riemannZeta (1 / 2 + Complex.I * (t : ℂ)) = 0 ∧
      s = 1 / 2 + Complex.I * (t : ℂ) :=
  refined_root_equals_canonical_at_index Z k
    hsource.implies_containment hs hz

end CP012RowReceipt

#print axioms CP012RowReceipt.ExactSourceRowAt.implies_containment
#print axioms CP012RowReceipt.refined_root_equals_canonical_at_index
#print axioms CP012RowReceipt.refined_root_of_exact_source_row
