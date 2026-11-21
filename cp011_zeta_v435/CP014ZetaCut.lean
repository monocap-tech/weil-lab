module

public import CP014FiniteCut
public import Zeta.Zeros.CountCertificates
public import Zeta.Zeros.RiemannHypothesisUpTo.Basic

/-!
CP014 genuine original-Zeta 4.35 source-proposition bridge from
finite-height zeta multiplicity count N(T) to ordinary finite cardinality
when T does not exceed the original certified Gram point.

Original source provides the finite-height simplicity theorem and
N_eq_sum. The final seam theorem is deliberately CONDITIONAL on
a proof-bearing finite Euler/RS witness cover: a bare source file SHA,
a separate BatchSpec existence or a decimal bracket does not produce
the required E and R subsets.

All modules here are real Lean SOURCE CANDIDATES, not accepted yet.
-/

@[expose] public section

open Set Zeta.Certificates

namespace CP014ZetaCut

/-- Genuine zeta positive-height zero finset below T; original finite
type is provided by the published Zeta zeroes_rect_Ioo_finite theorem. -/
noncomputable def zerosUnder (T : ℝ) : Finset ℂ :=
  (riemannZeta.zeroes_rect Set.univ (Set.Ioo 0 T)).toFinset

/-- Source-format finset membership: for T>0 the set contains exactly
those nonreal zeta zeros whose positive imaginary ordinates are <T. -/
theorem mem_zerosUnder_iff (T : ℝ) (z : ℂ) :
    z ∈ zerosUnder T ↔ z.im ∈ Ioo 0 T ∧ riemannZeta z = 0 := by
  simp [zerosUnder, riemannZeta.zeroes_rect, riemannZeta.zeroes]

/-- The actual original Zeta count N(T) becomes the FINITE CARDINALITY
of all positive-height zeros for T within the already certified simple
zero range. The original N(T) counts multiplicities; their equality is
NOT a general property outside this original finite simple-height range. -/
theorem N_eq_card_below_original_gram (Z : CertifiedZeroCount) (T : ℝ)
    (hT : T ≤ gramPoint Z.minIdx) :
    riemannZeta.N T = (zerosUnder T).card := by
  let S : Finset ℂ := zerosUnder T
  have horder : ∀ z ∈ S, riemannZeta.order z = 1 := by
    intro z hz
    obtain ⟨hzim, hz⟩ := (mem_zerosUnder_iff T z).mp hz
    exact riemannZeta.order_eq_one_upto Z
      ⟨hzim.1, hzim.2.trans_le hT⟩ hz
  calc
    riemannZeta.N T
        = ∑ z ∈ S, ((riemannZeta.order z : ℤ) : ℝ) := by
            rw [riemannZeta.N_eq_sum]
            rfl
    _ = ∑ z ∈ S, (1 : ℝ) := by
          apply Finset.sum_congr rfl
          intro z hz
          simp [horder z hz]
    _ = S.card := by simp

/-- An explicit identity of the low-cut zero set with the original
Gram-height zero set restricted by the cut ordinate. -/
theorem zerosUnder_cut_filter {c g : ℝ} (hcg : c ≤ g) :
    (zerosUnder g).filter (fun z : ℂ => z.im < c) = zerosUnder c := by
  ext z
  constructor
  · intro hz
    have hzg := (Finset.mem_filter.mp hz).1
    have hzlt := (Finset.mem_filter.mp hz).2
    obtain ⟨hzgim, hzero⟩ := (mem_zerosUnder_iff g z).mp hzg
    exact (mem_zerosUnder_iff c z).mpr ⟨⟨hzgim.1, hzlt⟩,hzero⟩
  · intro hz
    obtain ⟨hzim,hzero⟩ := (mem_zerosUnder_iff c z).mp hz
    apply Finset.mem_filter.mpr
    exact ⟨(mem_zerosUnder_iff g z).mpr
      ⟨⟨hzim.1,hzim.2.trans_le hcg⟩,hzero⟩,hzim.2⟩

/-- The genuine published original Zeta v4.35 Turing certificate has
exactly 1,748,002 distinct positive-height zeros below its terminal Gram
point, since the original original-source count also proves all are
SIMPLE there. The result uses no new Euler/RS root enclosures. -/
theorem original_full_source_finite_zero_card :
    (zerosUnder (gramPoint certifiedZeroCount.minIdx)).card = 1748002 := by
  have hN := N_eq_card_below_original_gram certifiedZeroCount
    (gramPoint certifiedZeroCount.minIdx) (le_refl _)
  have hT : riemannZeta.N (gramPoint certifiedZeroCount.minIdx) =
      certifiedZeroCount.intervals.length :=
    riemannZeta.N_gramPoint_eq certifiedZeroCount
  have hlength : certifiedZeroCount.intervals.length = 1748002 := by
    change certifiedZeroIntervals.intervals.length = 1748002
    exact certifiedZeroIntervals_length
  have hcast : ((zerosUnder (gramPoint certifiedZeroCount.minIdx)).card : ℝ) =
      1748002 := by
    rw [← hN]
    exact hT.trans (by exact_mod_cast hlength)
  exact_mod_cast hcast

/-- Exactly 52 original source Euler roots below 149.5, provided the
separate source-verified Euler and RS witness finsets E,R each carry
their genuine root membership and order information and together
saturate the already published 1,748,002 multiplicity count.

THIS IS A CONDITIONAL THEOREM; proving all six E/R/source binding
hypotheses from original BatchSpec.bundle remains an independent
Lean task. No original zero #53 rank has been claimed here. -/
theorem N_at_Euler_RS_seam_eq_52_of_source_witnesses
    (E R : Finset ℂ)
    (hEcount : E.card = 52)
    (hRcount : R.card = 1747950)
    (hEsub : E ⊆ zerosUnder (gramPoint certifiedZeroCount.minIdx))
    (hRsub : R ⊆ zerosUnder (gramPoint certifiedZeroCount.minIdx))
    (hdisjoint : Disjoint E R)
    (hEbelow : ∀ z ∈ E, z.im < (149500 : ℝ) / 1000)
    (hRabove : ∀ z ∈ R, (149500 : ℝ) / 1000 < z.im)
    (hcut : (149500 : ℝ) / 1000 ≤ gramPoint certifiedZeroCount.minIdx) :
    riemannZeta.N ((149500 : ℝ) / 1000) = 52 := by
  have hfull := original_full_source_finite_zero_card
  have htotal :
      (zerosUnder (gramPoint certifiedZeroCount.minIdx)).card =
      E.card + R.card := by omega
  have hcut_card := CP014FiniteCut.original_seam_root_cardinality
    (zerosUnder (gramPoint certifiedZeroCount.minIdx))
    E R (Finset.union_subset hEsub hRsub)
    hdisjoint hEcount hRcount hfull hEbelow hRabove
  have hfilter :
      (zerosUnder ((149500 : ℝ) / 1000)).card = 52 := by
    rw [← zerosUnder_cut_filter hcut]
    exact hcut_card
  rw [N_eq_card_below_original_gram certifiedZeroCount
    ((149500 : ℝ) / 1000) hcut]
  exact_mod_cast hfilter

end CP014ZetaCut

#print axioms CP014ZetaCut.N_eq_card_below_original_gram
#print axioms CP014ZetaCut.original_full_source_finite_zero_card
#print axioms CP014ZetaCut.zerosUnder_cut_filter
#print axioms CP014ZetaCut.N_at_Euler_RS_seam_eq_52_of_source_witnesses
