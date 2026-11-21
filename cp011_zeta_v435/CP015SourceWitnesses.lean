module

public import CP013Seam
public import CP014ZetaCut

/-!
CP015: remove the six SOURCE-WITNESS HYPOTHESES from the CP014 exact
Euler/RS seam zero-count theorem, using ORIGINAL upstream genuine certified
interval witness lists. The first52 Euler and all 1,747,950 original
RS-only bundles are from CP013's imported (still new, pending compiler)
source theorem candidates.

This source theorem deliberately does not require identifying an original
private BatchSpec row's decimals with an abstract indexed interval: the
cardinality argument is invariant under choosing *different witnesses*
in different exhaustive certified bundles.

No source-row 53 enclosure or local first-RS-zero rank is proved here.
NO NEW KERNEL PASS until actual original Zeta v4.35 .olean + axiom audit.
-/

@[expose] public section

open Set Zeta.Certificates Zeta.Certificates.Gram

namespace CP015SourceWitnesses

/-- The source-certified low Euler bundle and its genuine chosen zeros. -/
private noncomputable def E : CertifiedZeroIntervals :=
  CP013Seam.first52Euler.bundle

/-- The source-certified RS-only bundle, with Euler rows excluded. -/
private noncomputable def R : CertifiedZeroIntervals :=
  CP013Seam.allRS.bundle

/-- Source-defined separate subsets of the genuine zeta zero set. -/
noncomputable def eulerRoots : Finset ℂ := by
  classical
  exact E.zeros.toFinset

noncomputable def rsRoots : Finset ℂ := by
  classical
  exact R.zeros.toFinset

/-- Exact original numbers are PROPERTIES of the authentic source
BatchSpec bundles; no numerical enumeration of the zeros is assumed. -/
theorem eulerRoots_card : eulerRoots.card = 52 := by
  classical
  calc
    eulerRoots.card = E.zeros.length := List.toFinset_card_of_nodup E.zeros_nodup
    _ = E.intervals.length := E.zeros_length
    _ = 52 := CP013Seam.first52Euler.bundle_length

theorem rsRoots_card : rsRoots.card = 1747950 := by
  classical
  calc
    rsRoots.card = R.zeros.length := List.toFinset_card_of_nodup R.zeros_nodup
    _ = R.intervals.length := R.zeros_length
    _ = 1747950 := CP013Seam.allRS.bundle_length

/-- Every original Euler witness is strictly BELOW the common boundary. -/
private theorem eulerHeightLeCut :
    E.height ≤ (149500 : ℝ) / 1000 := by
  refine E.height_le_of_getLast?_snd
    CP013Seam.first52Euler.bundle_getLast? ?_
  norm_num [Enclosure.sfrac]

theorem eulerRoots_below : ∀ z ∈ eulerRoots,
    z.im < (149500 : ℝ) / 1000 := by
  intro z hz
  have hlist : z ∈ E.zeros := List.mem_toFinset.mp hz
  exact (E.zeros_im hlist).2.trans_le eulerHeightLeCut

/-- The critical REAL-RANK observation missing from CP014:
for any genuine certified interval chain, its PUBLIC first-left endpoint
bounds all later intervals' left endpoints from below. Unlike the
intermediate exact numeric row coordinates, this inequality *is*
a valid consequence of the publicly exported BatchSpec theorem. -/
private theorem lower_bound_of_first_endpoint
    (C : CertifiedZeroIntervals) (c : ℝ)
    (hhead : C.intervals.head?.map (·.fst) = some c)
    (I : NonemptyInterval ℝ) (hI : I ∈ C.intervals) :
    c ≤ I.fst := by
  cases hl : C.intervals with
  | nil =>
      simp [hl] at hhead
  | cons J tail =>
      have hJ : J.fst = c := by
        simpa [hl] using hhead
      have hp : (J :: tail).Pairwise (fun A B => A.snd ≤ B.fst) := by
        simpa [hl] using C.pairwise
      have hmem : I ∈ J :: tail := by simpa [hl] using hI
      obtain ⟨i, hi, rfl⟩ := List.mem_iff_getElem.mp hmem
      by_cases hzero : i = 0
      · subst i
        simpa [hJ]
      · have hipos : 0 < i := Nat.pos_of_ne_zero hzero
        have hsep : J.snd ≤ (J :: tail)[i].fst := by
          simpa using
            (List.pairwise_iff_getElem.mp hp) 0 i (by simp) hi hipos
        have hbound : c ≤ (J :: tail)[i].fst := by
          rw [← hJ]
          exact J.fst_le_snd.trans hsep
        exact hbound

/-- Every chosen RS root is strictly ABOVE the original 149.5 Euler
seam. This uses only a PUBLIC original first-RS left endpoint and the
proved certified ordered-interval chain. It does NOT use any original
intermediate row coordinates. -/
theorem rsRoots_above : ∀ z ∈ rsRoots,
    (149500 : ℝ) / 1000 < z.im := by
  intro z hz
  have hlist : z ∈ R.zeros := List.mem_toFinset.mp hz
  simp only [CertifiedZeroIntervals.zeros, List.mem_map] at hlist
  obtain ⟨t, ht, rfl⟩ := hlist
  simp only [List.mem_pmap] at ht
  obtain ⟨I, hI, rfl⟩ := ht
  have hhead : R.intervals.head?.map (·.fst) =
      some ((149500 : ℝ) / 1000) := by
    simpa [R, Enclosure.sfrac] using CP013Seam.allRS.bundle_head?
  have hleft := lower_bound_of_first_endpoint
    R ((149500 : ℝ) / 1000) hhead I hI
  have hroot := (R.has_zero I hI).choose_spec.1.1
  simpa using lt_of_le_of_lt hleft hroot

/-- The actual original Gram block lower enclosure is ABOVE the
original final 1,000,449.286 source-row right endpoint. Replicates
the exact numerical comparison in original upstream CountCertificates. -/
private theorem original_source_end_le_gram :
    (1000449286 : ℝ) / 1000 ≤
      gramPoint certifiedZeroCount.minIdx := by
  change (1000449286 : ℝ) / 1000 ≤
    gramPoint certifiedGramBlockSeq.minIdx
  refine le_trans ?_ certifiedGramBlockSeq.head_left_le_gramPoint
  norm_num [certifiedGramBlockSeq, Enclosure.sfrac]

private theorem eulerCutLeGram :
    (149500 : ℝ) / 1000 ≤
      gramPoint certifiedZeroCount.minIdx := by
  calc
    (149500 : ℝ) / 1000 ≤ (1000449286 : ℝ) / 1000 := by norm_num
    _ ≤ gramPoint certifiedZeroCount.minIdx :=
      original_source_end_le_gram

/-- Strict cut below the genuine original source Gram point; needed
because N(T) counts only positive-height zeros STRICTLY below T and
a point on the seam must be inside the full height-g zero roster. -/
private theorem eulerCutLtGram :
    (149500 : ℝ) / 1000 <
      gramPoint certifiedZeroCount.minIdx := by
  calc
    (149500 : ℝ) / 1000 < (1000449286 : ℝ) / 1000 := by norm_num
    _ ≤ gramPoint certifiedZeroCount.minIdx :=
      original_source_end_le_gram

private theorem eulerHeightLeGram :
    E.height ≤ gramPoint certifiedZeroCount.minIdx :=
  eulerHeightLeCut.trans eulerCutLeGram

private theorem rsHeightLeGram :
    R.height ≤ gramPoint certifiedZeroCount.minIdx := by
  have hR : R.height ≤ (1000449286 : ℝ) / 1000 := by
    refine R.height_le_of_getLast?_snd
      CP013Seam.allRS.bundle_getLast? ?_
    norm_num [Enclosure.sfrac]
  exact hR.trans original_source_end_le_gram

/-- Both certified source zero lists are SUBSETS of the authentic complete
positive-height zero finset from original upstream Zeta. -/
theorem eulerRoots_subset :
    eulerRoots ⊆
      CP014ZetaCut.zerosUnder (gramPoint certifiedZeroCount.minIdx) := by
  intro z hz
  have hlist : z ∈ E.zeros := List.mem_toFinset.mp hz
  obtain ⟨hzim, hzero⟩ := E.zeros_spec z hlist
  exact (CP014ZetaCut.mem_zerosUnder_iff _ z).mpr
    ⟨Ioo_subset_Ioo le_rfl eulerHeightLeGram hzim, hzero⟩

theorem rsRoots_subset :
    rsRoots ⊆
      CP014ZetaCut.zerosUnder (gramPoint certifiedZeroCount.minIdx) := by
  intro z hz
  have hlist : z ∈ R.zeros := List.mem_toFinset.mp hz
  obtain ⟨hzim, hzero⟩ := R.zeros_spec z hlist
  exact (CP014ZetaCut.mem_zerosUnder_iff _ z).mpr
    ⟨Ioo_subset_Ioo le_rfl rsHeightLeGram hzim, hzero⟩

/-- The strict seam inequalities, not numerical zero approximations,
prove the two certified witness sets are disjoint. -/
theorem euler_rs_disjoint : Disjoint eulerRoots rsRoots := by
  classical
  apply Finset.disjoint_left.mpr
  intro z hzE hzR
  exact (lt_asymm (eulerRoots_below z hzE)
    (rsRoots_above z hzR))

/-- The TWO independently source-certified witness sets ACTUALLY
exhaust the genuine original Zeta finite-height zero set, even though
their BatchSpec.bundle Classical.choose witnesses are not definitionally
the same as the one original global count bundle's witnesses. -/
theorem original_complete_positive_roster_is_euler_union_rs :
    CP014ZetaCut.zerosUnder (gramPoint certifiedZeroCount.minIdx) =
      eulerRoots ∪ rsRoots := by
  classical
  apply CP014FiniteCut.exhausted_by_two_disjoint_parts
    (CP014ZetaCut.zerosUnder (gramPoint certifiedZeroCount.minIdx))
    eulerRoots rsRoots
  · exact Finset.union_subset eulerRoots_subset rsRoots_subset
  · exact euler_rs_disjoint
  · rw [CP014ZetaCut.original_full_source_finite_zero_card,
      eulerRoots_card, rsRoots_card]
    norm_num

/-- The exact original shared source boundary t = 149.5 is NOT a zeta
zero of ANY real part. This is stronger than the number N(149.5)=52
alone: N counts roots at *strictly smaller* heights. No numerical
Hardy Z evaluation is needed after the complete source partition. -/
theorem no_original_zero_exactly_at_149500_div1000 (z : ℂ)
    (hheight : z.im = (149500 : ℝ) / 1000) :
    riemannZeta z ≠ 0 := by
  intro hz
  have hmem :
      z ∈ CP014ZetaCut.zerosUnder (gramPoint certifiedZeroCount.minIdx) :=
    (CP014ZetaCut.mem_zerosUnder_iff _ z).mpr
      ⟨⟨by rw [hheight]; norm_num, by rw [hheight]; exact eulerCutLtGram⟩,
        hz⟩
  rw [original_complete_positive_roster_is_euler_union_rs] at hmem
  rcases Finset.mem_union.mp hmem with hE | hR
  · have hl := eulerRoots_below z hE
    rw [hheight] at hl
    exact (lt_irrefl ((149500 : ℝ) / 1000)) hl
  · have hl := rsRoots_above z hR
    rw [hheight] at hl
    exact (lt_irrefl ((149500 : ℝ) / 1000)) hl

/-- CP015's actual proof target. ALL the source-root witness finset
hypotheses of CP014 are DISCHARGED, so there is NO new mathematical
premise in this theorem's signature. Its proof relies on the original
externally accepted complete Zeta count and CP013's NEW RS-only
reconstruction. Only an ACTUAL kernel compile/axiom audit can accept it. -/
theorem original_N_at_149500_div1000_eq_52 :
    riemannZeta.N ((149500 : ℝ) / 1000) = 52 :=
  CP014ZetaCut.N_at_Euler_RS_seam_eq_52_of_source_witnesses
    eulerRoots rsRoots
    eulerRoots_card rsRoots_card
    eulerRoots_subset rsRoots_subset euler_rs_disjoint
    eulerRoots_below rsRoots_above eulerCutLeGram

end CP015SourceWitnesses

#print axioms CP015SourceWitnesses.eulerRoots_card
#print axioms CP015SourceWitnesses.rsRoots_card
#print axioms CP015SourceWitnesses.rsRoots_above
#print axioms CP015SourceWitnesses.eulerRoots_subset
#print axioms CP015SourceWitnesses.rsRoots_subset
#print axioms CP015SourceWitnesses.euler_rs_disjoint
#print axioms CP015SourceWitnesses.original_complete_positive_roster_is_euler_union_rs
#print axioms CP015SourceWitnesses.no_original_zero_exactly_at_149500_div1000
#print axioms CP015SourceWitnesses.original_N_at_149500_div1000_eq_52
