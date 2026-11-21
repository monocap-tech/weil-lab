module

public import CP015SourceWitnesses
public import Zeta.Zeros.RiemannHypothesisUpTo.Basic
public import Mathlib.Data.Set.Finite.Lemmas

/-!
CP016: SOURCE-CANONICAL ordinal #53, without claiming numerical ordinate
150.05352042 or equality of two different BatchSpec.choose witnesses.

The published complete finite-height Zeta source count and the actual
52 low Euler / 1,747,950 RS-only source witness partition (CP015 new Lean
proof candidates) imply there exists a LEAST genuine RS positive zero.
It has exactly 52 distinct/multiplicity-one positive zeros below its
ordinate, and is thus the 53rd positive-height zero.

New theorem sources are not accepted until real original Lean 4.35
kernel and standard-only axioms receipts pass. This source proof gives
NO precise right endpoint or same-root identity for CP010's proposed
narrow root, and is not a claim of global RH or signed Weil positivity.
-/

@[expose] public section

open Set Zeta.Certificates

namespace CP016FirstRSRank

/-- Finite nonempty original RS source witness set has a least ordinate.
Unlike the numerical 200-row first batch, this is independent of its
internal interval coordinates. -/
theorem exists_least_original_RS_witness :
    ∃ z ∈ CP015SourceWitnesses.rsRoots,
      ∀ w ∈ CP015SourceWitnesses.rsRoots, z.im ≤ w.im := by
  classical
  let R := CP015SourceWitnesses.rsRoots
  have hnon : (R : Set ℂ).Nonempty := by
    have hcard : 0 < R.card := by
      rw [show R.card = 1747950 from
        CP015SourceWitnesses.rsRoots_card]
      norm_num
    obtain ⟨z, hz⟩ := Finset.card_pos.mp hcard
    exact ⟨z, hz⟩
  have hfinite : (R : Set ℂ).Finite := R.finite_toSet
  obtain ⟨z, hz, hzmin⟩ :=
    Set.exists_min_image (R : Set ℂ) (fun z : ℂ => z.im) hfinite hnon
  refine ⟨z, ?_, ?_⟩
  · exact hz
  · intro w hw
    exact hzmin w hw

/-- At a genuine least original RS root z, the entire positive-height
zero roster strictly BELOW z consists EXACTLY of the 52 Euler zeros.
Any other RS root lies at or above z; any Euler root lies below 149.5,
while z lies strictly above that cut. -/
theorem original_roots_below_least_RS_are_exactly_Euler
    {z : ℂ} (hz : z ∈ CP015SourceWitnesses.rsRoots)
    (hmin : ∀ w ∈ CP015SourceWitnesses.rsRoots, z.im ≤ w.im) :
    (CP014ZetaCut.zerosUnder
       (gramPoint certifiedZeroCount.minIdx)).filter
         (fun w : ℂ => w.im < z.im) =
      CP015SourceWitnesses.eulerRoots := by
  classical
  ext w
  constructor
  · intro hw
    have hwg := (Finset.mem_filter.mp hw).1
    have hwlt := (Finset.mem_filter.mp hw).2
    rw [CP015SourceWitnesses.original_complete_positive_roster_is_euler_union_rs]
      at hwg
    rcases Finset.mem_union.mp hwg with hwE | hwR
    · exact hwE
    · exact False.elim ((not_lt_of_ge (hmin w hwR)) hwlt)
  · intro hwE
    have hbelow := CP015SourceWitnesses.eulerRoots_below w hwE
    have habove := CP015SourceWitnesses.rsRoots_above z hz
    refine Finset.mem_filter.mpr ⟨
      CP015SourceWitnesses.eulerRoots_subset hwE, ?_⟩
    exact lt_trans hbelow habove

/-- At the ORIGINAL first genuine RS zero, the multiplicity-counted
upstream zero count is exactly 52. Here the point z is source-chosen,
not a numerical 150.05352 bracket candidate. -/
theorem N_at_original_least_RS_root_eq_52
    {z : ℂ} (hz : z ∈ CP015SourceWitnesses.rsRoots)
    (hmin : ∀ w ∈ CP015SourceWitnesses.rsRoots, z.im ≤ w.im) :
    riemannZeta.N z.im = 52 := by
  have hzg : z ∈ CP014ZetaCut.zerosUnder
      (gramPoint certifiedZeroCount.minIdx) :=
    CP015SourceWitnesses.rsRoots_subset hz
  obtain ⟨hzim, hzeta⟩ :=
    (CP014ZetaCut.mem_zerosUnder_iff _ z).mp hzg
  have hT : z.im ≤ gramPoint certifiedZeroCount.minIdx := hzim.2.le
  have hcut := CP014ZetaCut.zerosUnder_cut_filter hT
  have hpart :=
    original_roots_below_least_RS_are_exactly_Euler hz hmin
  calc
    riemannZeta.N z.im =
        ((CP014ZetaCut.zerosUnder z.im).card : ℝ) :=
      CP014ZetaCut.N_eq_card_below_original_gram
        certifiedZeroCount z.im hT
    _ = ((CP015SourceWitnesses.eulerRoots).card : ℝ) := by
      rw [← hcut, hpart]
    _ = 52 := by rw [CP015SourceWitnesses.eulerRoots_card]
  
/-- The original source certificate DOES identify a distinguished
53rd zero by ordinal rank. It does NOT attach the CP010 numerical
interval [150.05352,150.05353] to that zero. -/
theorem original_53rd_positive_zeta_zero_exists :
    ∃ z : ℂ,
      z ∈ CP015SourceWitnesses.rsRoots ∧
      riemannZeta z = 0 ∧
      (149500 : ℝ) / 1000 < z.im ∧
      riemannZeta.N z.im = 52 ∧
      (∀ w ∈ CP015SourceWitnesses.rsRoots, z.im ≤ w.im) := by
  obtain ⟨z, hz, hzmin⟩ := exists_least_original_RS_witness
  have hzroot := (CP014ZetaCut.mem_zerosUnder_iff _ z).mp
    (CP015SourceWitnesses.rsRoots_subset hz)
  refine ⟨z, hz, hzroot.2, CP015SourceWitnesses.rsRoots_above z hz,
    N_at_original_least_RS_root_eq_52 hz hzmin, hzmin⟩

/-- Any TWO source-chosen least RS roots are the SAME complex zero.
Their minimal ordinates agree, and upstream original bounded-height RH
places every original source root on Re=1/2. No source numeric first
RS interval or extra zero uniqueness axiom is assumed. -/
theorem original_least_RS_root_unique
    {z w : ℂ}
    (hz : z ∈ CP015SourceWitnesses.rsRoots)
    (hw : w ∈ CP015SourceWitnesses.rsRoots)
    (hminz : ∀ v ∈ CP015SourceWitnesses.rsRoots, z.im ≤ v.im)
    (hminw : ∀ v ∈ CP015SourceWitnesses.rsRoots, w.im ≤ v.im) :
    z = w := by
  have hzim : z.im = w.im :=
    le_antisymm (hminz w hw) (hminw z hz)
  have hzg := (CP014ZetaCut.mem_zerosUnder_iff _ z).mp
    (CP015SourceWitnesses.rsRoots_subset hz)
  have hwg := (CP014ZetaCut.mem_zerosUnder_iff _ w).mp
    (CP015SourceWitnesses.rsRoots_subset hw)
  have hzre : z.re = 1 / 2 := by
    by_contra hne
    exact (riemannZeta.ne_zero_of_re_ne_half_upto
      certifiedZeroCount hzg.1 hne) hzg.2
  have hwre : w.re = 1 / 2 := by
    by_contra hne
    exact (riemannZeta.ne_zero_of_re_ne_half_upto
      certifiedZeroCount hwg.1 hne) hwg.2
  apply Complex.ext
  · exact hzre.trans hwre.symm
  · exact hzim

/-- The original canonical first RS zero is the FIRST genuine positive
zero above 149.5. Proves an EMPTY OPEN GAP between the method seam and
that source-defined zero, without demanding a numerical right endpoint. -/
theorem original_first_RS_zero_has_no_preceding_zero
    {z : ℂ} (hz : z ∈ CP015SourceWitnesses.rsRoots)
    (hmin : ∀ w ∈ CP015SourceWitnesses.rsRoots, z.im ≤ w.im)
    {w : ℂ} (hwcut : w.im ∈ Ioo ((149500 : ℝ) / 1000) z.im) :
    riemannZeta w ≠ 0 := by
  intro hwroot
  have hzg : z ∈ CP014ZetaCut.zerosUnder
      (gramPoint certifiedZeroCount.minIdx) :=
    CP015SourceWitnesses.rsRoots_subset hz
  obtain ⟨hzheight, _⟩ := (CP014ZetaCut.mem_zerosUnder_iff _ z).mp hzg
  have hwG : w ∈ CP014ZetaCut.zerosUnder
      (gramPoint certifiedZeroCount.minIdx) :=
    (CP014ZetaCut.mem_zerosUnder_iff _ w).mpr
      ⟨⟨(by linarith [hwcut.1]), hwcut.2.trans hzheight.2⟩, hwroot⟩
  rw [CP015SourceWitnesses.original_complete_positive_roster_is_euler_union_rs]
    at hwG
  rcases Finset.mem_union.mp hwG with hwE | hwR
  · have hE := CP015SourceWitnesses.eulerRoots_below w hwE
    linarith [hwcut.1]
  · have hR := hmin w hwR
    linarith [hwcut.2]

end CP016FirstRSRank

#print axioms CP016FirstRSRank.exists_least_original_RS_witness
#print axioms CP016FirstRSRank.original_roots_below_least_RS_are_exactly_Euler
#print axioms CP016FirstRSRank.N_at_original_least_RS_root_eq_52
#print axioms CP016FirstRSRank.original_53rd_positive_zeta_zero_exists
#print axioms CP016FirstRSRank.original_first_RS_zero_has_no_preceding_zero
#print axioms CP016FirstRSRank.original_least_RS_root_unique
