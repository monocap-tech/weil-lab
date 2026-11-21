module

public import CP016FirstRSRank
public import CP014HardyRank

/-!
CP016: EXACT first RS ordinal #53 zero identity for an independently
kernel-certified refined Hardy-Z root at real ordinate t, CONDITIONAL
on a rigorously proved strict HardyZ monotonicity on [149.5,b].

Unlike any SHA-to-original-row guess, the proof is based on original
complete global Turing count + CP013 RS-only witness roster + full
source witness exhaustion + published finite RH below g.

No numerical HardyZ derivative screen is accepted as strict monotonicity.
No new narrow root Z(t)=0 has yet passed CP010's true Lean kernel.
This module's own new Lean proof is also only a candidate until compiled.
-/

@[expose] public section

open Set Zeta.Certificates

namespace CP016MonotoneAttach

/-- A new narrow zero belongs to the genuine RS-only root witness roster,
without assuming its numerical bracket is an original private source
interval. The real source theorem N(g) is used through CP015 exhaustion.
-/
theorem refined_critical_root_is_RS_source_witness
    {t : ℝ}
    (ht : t ∈ Ioo ((149500 : ℝ) / 1000)
      (gramPoint certifiedZeroCount.minIdx))
    (hzt : riemannZeta
      (1 / 2 + Complex.I * (t : ℂ)) = 0) :
    (1 / 2 + Complex.I * (t : ℂ)) ∈
      CP015SourceWitnesses.rsRoots := by
  let w : ℂ := 1 / 2 + Complex.I * (t : ℂ)
  have hw_im : w.im = t := by simp [w]
  have hglobal : w ∈ CP014ZetaCut.zerosUnder
      (gramPoint certifiedZeroCount.minIdx) :=
    (CP014ZetaCut.mem_zerosUnder_iff _ w).mpr
      ⟨by simpa [hw_im] using
        ⟨(show (0 : ℝ) < (149500 : ℝ) / 1000 by norm_num).trans ht.1, ht.2⟩,
        hzt⟩
  rw [CP015SourceWitnesses.original_complete_positive_roster_is_euler_union_rs]
    at hglobal
  rcases Finset.mem_union.mp hglobal with hE | hR
  · have hlow := CP015SourceWitnesses.eulerRoots_below w hE
    rw [hw_im] at hlow
    exact False.elim ((not_lt.mpr ht.1.le) hlow)
  · exact hR

/-- Canonical source-first RS root is actually critical-line; this is
from true original finite RH below the original certified Gram g,
not from a source-indexed decimal batch-row equality. -/
private theorem source_first_RS_re_half
    {z : ℂ} (hz : z ∈ CP015SourceWitnesses.rsRoots) :
    z.re = 1 / 2 := by
  have hroot := (CP014ZetaCut.mem_zerosUnder_iff _ z).mp
    (CP015SourceWitnesses.rsRoots_subset hz)
  by_contra hne
  exact (riemannZeta.ne_zero_of_re_ne_half_upto
    certifiedZeroCount hroot.1 hne) hroot.2

/-- The ORIGINAL source-first positive RS zero and a new independently
certified refined critical-line zero at t are the SAME complex zero
provided a genuine uniform monotonicity certificate holds on the
full compact interval [149.5,b]. This is source-canonical ordinal
identity, not a numerical first original RS row endpoint equation. -/
theorem refined_root_equals_original_53rd_of_hardy_monotone
    {t b : ℝ}
    (ht : t ∈ Ioo ((149500 : ℝ) / 1000) b)
    (hb : b < gramPoint certifiedZeroCount.minIdx)
    (hmono : StrictMonoOn Zeta.hardyZ
      (Icc ((149500 : ℝ) / 1000) b))
    (hzt : riemannZeta (1 / 2 + Complex.I * (t : ℂ)) = 0) :
    ∃ z : ℂ,
      z ∈ CP015SourceWitnesses.rsRoots ∧
      riemannZeta.N z.im = 52 ∧
      z = 1 / 2 + Complex.I * (t : ℂ) := by
  obtain ⟨z, hz, hmin⟩ :=
    CP016FirstRSRank.exists_least_original_RS_witness
  have htG : t ∈ Ioo ((149500 : ℝ) / 1000)
      (gramPoint certifiedZeroCount.minIdx) :=
    ⟨ht.1, ht.2.trans hb⟩
  have hsource :
      (1 / 2 + Complex.I * (t : ℂ)) ∈
        CP015SourceWitnesses.rsRoots :=
    refined_critical_root_is_RS_source_witness htG hzt
  have hz_le_t : z.im ≤ t := by
    simpa using hmin (1 / 2 + Complex.I * (t : ℂ)) hsource
  have hz_from_source := (CP014ZetaCut.mem_zerosUnder_iff _ z).mp
    (CP015SourceWitnesses.rsRoots_subset hz)
  have hzh : z.re = 1 / 2 := source_first_RS_re_half hz
  have hzform : z = 1 / 2 + Complex.I * (z.im : ℂ) := by
    apply Complex.ext <;> simp [hzh]
  have hztlocal : riemannZeta
      (1 / 2 + Complex.I * (z.im : ℂ)) = 0 := by
    rw [← hzform]
    exact hz_from_source.2
  have hzcut : z.im ∈ Ioo ((149500 : ℝ) / 1000) b :=
    ⟨CP015SourceWitnesses.rsRoots_above z hz,
      lt_of_le_of_lt hz_le_t ht.2⟩
  have hz_ordinate_eq_t : z.im = t :=
    CP014HardyRank.unique_critical_zero_of_hardy_strictMonoOn
      ((149500 : ℝ) / 1000) b (by norm_num)
      hmono hzcut ht hztlocal hzt
  refine ⟨z, hz,
    CP016FirstRSRank.N_at_original_least_RS_root_eq_52 hz hmin, ?_⟩
  rw [hzform, hz_ordinate_eq_t]

end CP016MonotoneAttach

#print axioms CP016MonotoneAttach.refined_critical_root_is_RS_source_witness
#print axioms CP016MonotoneAttach.refined_root_equals_original_53rd_of_hardy_monotone
