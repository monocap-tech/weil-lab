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
#print axioms CP011CanonicalRoster.pinned_external_positive_root_is_member
