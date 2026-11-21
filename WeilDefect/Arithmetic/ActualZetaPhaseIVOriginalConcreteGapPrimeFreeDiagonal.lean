import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalTwoCollarPrimeFreeBump
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
IV016: KERNEL-CHECKABLE original two-collar exact finite log gap
and genuinely PRIME-FREE new Schwartz DIAGONAL.

IV015 constructed a genuine nonzero complex C∞ compactly supported
Schwartz bump around c=1/5 but left the precise finite n<10
two-collar logarithmic gap as a named hypothesis, separately checked
only with exact rational arithmetic. IV016 discharges that FINITE
arithmetic leaf directly in Lean, using rigorously established
Mathlib bounds for the actual Real.log 2,3,4,5 and monotonicity.

For this sufficiently narrow true new original physical source,
the self-pairing has ZERO original von-Mangoldt prime contribution
too. The original signed diagonal thus reduces to TWO real zeta pole
moments plus the unchanged Gamma/digamma integral; its sign is still
UNPROVED. Neither a zero prime cross term nor a zero prime diagonal
term implies global Weil positivity or RH.

This module is a Lean proof CANDIDATE until a genuine pinned compiler
build and strict source-bound standard axiom audit PASS.
-/

/-- The original finite n<10 relevant logarithms fall in four
rigorously separated rational bands. This relies on Mathlib's proven
nine-digit REAL log bounds, not a float approximation or a Python
runtime assertion. It includes n=0 and n=1 (both log value zero). -/
theorem neutralIV016FrozenLogBand_lt10
    (m : ℕ) (hm : m < 10) :
    Real.log (m : ℝ) ≤ (7/10:ℝ) ∨
      ((109/100:ℝ) ≤ Real.log (m : ℝ) ∧
        Real.log (m : ℝ) ≤ (11/10:ℝ)) ∨
      ((138/100:ℝ) ≤ Real.log (m : ℝ) ∧
        Real.log (m : ℝ) ≤ (14/10:ℝ)) ∨
      (16/10:ℝ) ≤ Real.log (m : ℝ) := by
  by_cases hfive : 5 ≤ m
  · right; right; right
    have hmn : (5 : ℝ) ≤ (m : ℝ) := by exact_mod_cast hfive
    have hmon : Real.log (5 : ℝ) ≤ Real.log (m : ℝ) :=
      Real.log_le_log (by norm_num) hmn
    have h5 := Real.log_five_gt_d9
    linarith
  · have hfour : m ≤ 4 := by omega
    interval_cases m
    · left
      simp
    · left
      simp
    · left
      have h2 := Real.log_two_lt_d9
      linarith
    · right; left
      constructor
      · have h3 := Real.log_three_gt_d9
        linarith
      · have h3 := Real.log_three_lt_d9
        linarith
    · right; right; left
      constructor
      · rw [Real.log_four_eq]
        have h2 := Real.log_two_gt_d9
        linarith
      · rw [Real.log_four_eq]
        have h2 := Real.log_two_lt_d9
        linarith

/-- The usual nonnegative real logarithm for every natural input,
including the special convention log(0)=0. -/
theorem neutralIV016NatLog_nonnegative (m : ℕ) :
    0 ≤ Real.log (m : ℝ) := by
  by_cases hz : m = 0
  · subst m
    simp
  · have hpos : 1 ≤ m := by omega
    exact Real.log_nonneg (by exact_mod_cast hpos)

/-- Two strict rational alternatives directly imply a strict
absolute-value clearance. This uses only real order. -/
private theorem neutralIV016AbsClearance
    (z : ℝ)
    (h : (1/500:ℝ) < z ∨ z < -(1/500:ℝ)) :
    (1/500:ℝ) < |z| := by
  rcases h with hp | hn
  · rw [abs_of_pos (by linarith)]
    exact hp
  · rw [abs_of_neg (by linarith)]
    linarith

/-- All FOUR exact physical old/new collar translation gaps hold
whenever the real prime log belongs to the proven four bands. The
right minus and left plus gaps use only log >= 0; the other two
distances use the actual disjoint log-band constraints. -/
theorem neutralIV016FrozenFourSignedGaps_of_band
    (y : ℝ) (hy : 0 ≤ y)
    (hband :
      y ≤ (7/10:ℝ) ∨
      ((109/100:ℝ) ≤ y ∧ y ≤ (11/10:ℝ)) ∨
      ((138/100:ℝ) ≤ y ∧ y ≤ (14/10:ℝ)) ∨
      (16/10:ℝ) ≤ y) :
    ((1/500:ℝ) < |(1299/1000:ℝ) - y| ∧
      (1/500:ℝ) < |(-899/1000:ℝ) - y|) ∧
    ((1/500:ℝ) < |(1299/1000:ℝ) + y| ∧
      (1/500:ℝ) < |(-899/1000:ℝ) + y|) := by
  have hRightMinus :
      (1/500:ℝ) < |(-899/1000:ℝ) - y| := by
    apply neutralIV016AbsClearance
    right
    linarith
  have hLeftPlus :
      (1/500:ℝ) < |(1299/1000:ℝ) + y| := by
    apply neutralIV016AbsClearance
    left
    linarith
  refine ⟨⟨?_, hRightMinus⟩, ⟨hLeftPlus, ?_⟩⟩
  · rcases hband with hsmall | ⟨hlo, hhi⟩ | ⟨hlo, hhi⟩ | hlarge
    · apply neutralIV016AbsClearance
      left
      linarith
    · apply neutralIV016AbsClearance
      left
      linarith
    · apply neutralIV016AbsClearance
      right
      linarith
    · apply neutralIV016AbsClearance
      right
      linarith
  · rcases hband with hsmall | ⟨hlo, hhi⟩ | ⟨hlo, hhi⟩ | hlarge
    · apply neutralIV016AbsClearance
      right
      linarith
    · apply neutralIV016AbsClearance
      left
      linarith
    · apply neutralIV016AbsClearance
      left
      linarith
    · apply neutralIV016AbsClearance
      left
      linarith

/-- IV015's SPECIFIC previously outstanding exact finite arithmetic
gap is now proved as a direct Lean theorem: the genuine ORIGINAL
two width-1/500 strict collars at +/- 11/10, the new complex bump
around 1/5 with radius 1/1000, and all signed log n translations
for EVERY n<10, not just nonzero von-Mangoldt coefficients. -/
theorem neutralIV016FrozenConcrete_allIntegerGap :
    neutralIV015FrozenTwoCollarActiveGap
      (1/5:ℝ) (1/1000:ℝ) 10 := by
  intro m hm _
  have hb :=
    neutralIV016FrozenLogBand_lt10 m (Finset.mem_range.mp hm)
  have hy := neutralIV016NatLog_nonnegative m
  have hh :=
    neutralIV016FrozenFourSignedGaps_of_band (Real.log (m : ℝ)) hy hb
  have hleft :
      (1/5:ℝ) - neutralIV015FrozenLeftCenter =
        (1299/1000:ℝ) := by
    norm_num [neutralIV015FrozenLeftCenter]
  have hright :
      (1/5:ℝ) - neutralIV015FrozenRightCenter =
        (-899/1000:ℝ) := by
    norm_num [neutralIV015FrozenRightCenter]
  have hrad :
      neutralIV015FrozenCollarRadius + (1/1000:ℝ) =
        (1/500:ℝ) := by
    norm_num [neutralIV015FrozenCollarRadius]
  simpa only [hleft, hright, hrad] using hh

/-- The formerly explicit finite-number premise is now REMOVED
from the original concrete nonzero Schwartz source construction.
No new positiveness assumption is hidden in the statement. -/
theorem neutralIV016FrozenConcrete_originalPrimeFreeBump
    {n : ℕ}
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, neutralNF735InOriginalCollars (s i)) :
    ∃ t : 𝓢(ℝ, ℂ),
      t (1/5:ℝ) = 1 ∧
      (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
        t x = 0) ∧
      ¬ neutralNF735InOriginalCollars t ∧
      t ≠ neutralIV009PhysicalSchwartzSum s u ∧
      neutralIV011OriginalMixedPrime (11/10:ℝ)
        (neutralIV009PhysicalSchwartzSum s u) t = 0 ∧
      neutralIV010Mixed (11/10:ℝ)
        (neutralIV009PhysicalSchwartzSum s u) t =
        neutralIV013OriginalMixedAnalyticRemainder
          (11/10:ℝ) (neutralIV009PhysicalSchwartzSum s u) t := by
  exact neutralIV015FrozenConcrete_originalPrimeFreeBump_of_gap
    s u hs neutralIV016FrozenConcrete_allIntegerGap

/-- At EVERY genuinely nonzero von-Mangoldt frequency, n>=2,
and thus the literal prime shift log n exceeds the entire width
2/1000 of our selected NONZERO original physical bump. -/
theorem neutralIV016FrozenSelfLogClearance
    (m : ℕ)
    (hactive : ArithmeticFunction.vonMangoldt m ≠ 0) :
    (1/500:ℝ) < Real.log (m : ℝ) := by
  have hprime :
      Nat.IsPrimePow m := ArithmeticFunction.vonMangoldt_ne_zero_iff.mp hactive
  have hm : 2 ≤ m := hprime.two_le
  have hmR : (2 : ℝ) ≤ (m : ℝ) := by exact_mod_cast hm
  have hmon : Real.log (2 : ℝ) ≤ Real.log (m : ℝ) :=
    Real.log_le_log (by norm_num) hmR
  have h2 := Real.log_two_gt_d9
  linarith

/-- The SAME compact bump is separated from ITSELF at every active
prime-power translation in the true finite original arithmetic sum.
This is the new feature not obtained from merely prime-free old/new
mixed pairings in IV015. -/
theorem neutralIV016FrozenSelfActiveGap :
    ∀ m : ℕ, m ∈ Finset.range 10 →
      ArithmeticFunction.vonMangoldt m ≠ 0 →
      (1/1000:ℝ) + (1/1000:ℝ) <
          |(1/5:ℝ) - (1/5:ℝ) - Real.log m| ∧
      (1/1000:ℝ) + (1/1000:ℝ) <
          |(1/5:ℝ) - (1/5:ℝ) + Real.log m| := by
  intro m _ hactive
  have hlog := neutralIV016FrozenSelfLogClearance m hactive
  have habs :
      |Real.log (m : ℝ)| = Real.log (m : ℝ) :=
    abs_of_pos (by linarith)
  have hrad : (1/1000:ℝ) + (1/1000:ℝ) = 1/500 := by
    norm_num
  constructor
  · simpa only [sub_self, zero_sub, abs_neg, habs, hrad] using hlog
  · simpa only [sub_self, zero_add, habs, hrad] using hlog

/-- The selected narrow PHYSICAL Schwartz source has zero genuine
original von-Mangoldt contribution to its own DIAGONAL, provided
the selected bump retains its literal small support; and the exact
original diagonal is the actual two-pole-plus-Gamma remainder.
No sign of this remainder is claimed. -/
theorem neutralIV016FrozenSmallBump_selfPrime_zero
    (t : 𝓢(ℝ, ℂ))
    (htlocal : ∀ x : ℝ,
      x ∉ Set.Icc ((1/5:ℝ)-(1/1000:ℝ))
        ((1/5:ℝ)+(1/1000:ℝ)) → t x = 0) :
    neutralIV011OriginalMixedPrime (11/10:ℝ) t t = 0 ∧
      neutralIV010Diagonal (11/10:ℝ) t =
        neutralIV013OriginalMixedAnalyticRemainder (11/10:ℝ) t t := by
  have htwide : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x = 0 :=
    neutralIV015Bump_supported_largeWindow
      (11/10:ℝ) (1/5:ℝ) (1/1000:ℝ)
      (by norm_num) t htlocal
  have hsep : neutralIV014ActivePrimeSeparated t t 10 :=
    neutralIV014ActiveSeparated_of_intervalGap t t 10
      (1/5:ℝ) (1/5:ℝ) (1/1000:ℝ) (1/1000:ℝ)
      htlocal htlocal neutralIV016FrozenSelfActiveGap
  have hp :=
    neutralIV014ActiveMixedPrime_zero
      (11/10:ℝ) (11/10:ℝ) (le_refl _)
      t t htwide htwide 10
      neutralIV015FrozenConcrete_logCutoff hsep
  have hEF :=
    neutralIV014ActiveMixed_eq_analytic
      (11/10:ℝ) (11/10:ℝ) (le_refl _)
      t t htwide htwide 10
      neutralIV015FrozenConcrete_logCutoff hsep
  exact ⟨hp, hEF⟩

/-- The concrete nonzero original test simultaneously has:
  - exact value 1 outside both historical frozen original collars;
  - zero authentic original mixed prime interaction with ANY old finite
    original collar Schwartz superposition S;
  - zero genuine original new DIAGONAL von-Mangoldt prime term;
  - unchanged actual pole+Gamma residual for BOTH mixed and diagonal
    zeta arithmetic entries.

No arithmetic prime positivity is assumed. The original new diagonal
is NOT proved nonnegative, because the pole+Gamma remainder's sign
has not been estimated. This is an actual new analytic reduction. -/
theorem neutralIV016ExistsConcretePrimeFreeMixedAndDiagonal
    {n : ℕ}
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, neutralNF735InOriginalCollars (s i)) :
    ∃ t : 𝓢(ℝ, ℂ),
      t (1/5:ℝ) = 1 ∧
      (∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
        t x = 0) ∧
      ¬ neutralNF735InOriginalCollars t ∧
      t ≠ neutralIV009PhysicalSchwartzSum s u ∧
      neutralIV011OriginalMixedPrime (11/10:ℝ)
        (neutralIV009PhysicalSchwartzSum s u) t = 0 ∧
      neutralIV011OriginalMixedPrime (11/10:ℝ) t t = 0 ∧
      neutralIV010Mixed (11/10:ℝ)
        (neutralIV009PhysicalSchwartzSum s u) t =
        neutralIV013OriginalMixedAnalyticRemainder
          (11/10:ℝ) (neutralIV009PhysicalSchwartzSum s u) t ∧
      neutralIV010Diagonal (11/10:ℝ) t =
        neutralIV013OriginalMixedAnalyticRemainder (11/10:ℝ) t t := by
  obtain ⟨t, htc, htlocal⟩ :=
    neutralIV015ExistsComplexSchwartzBump
      (1/5:ℝ) (1/1000:ℝ) (by norm_num)
  have htwide : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x = 0 :=
    neutralIV015Bump_supported_largeWindow
      (11/10:ℝ) (1/5:ℝ) (1/1000:ℝ) (by norm_num)
      t htlocal
  have hnew : ¬ neutralNF735InOriginalCollars t := by
    intro hOld
    have hz := hOld (1/5:ℝ) neutralIV015FrozenConcrete_centerOutside
    rw [htc] at hz
    exact one_ne_zero hz
  let S := neutralIV009PhysicalSchwartzSum s u
  have hScollar : neutralNF735InOriginalCollars S := by
    change neutralNF735InOriginalCollars
      (∑ i : Fin n, u i • s i)
    exact neutralNF738OriginalCollars_finset_linear
      (Finset.univ : Finset (Fin n)) s u
      (by intro i _; exact hs i)
  have hSwide :
      ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → S x = 0 :=
    neutralIV009OriginalCollars_supported_window S hScollar
  have hsep : neutralIV014ActivePrimeSeparated S t 10 :=
    neutralIV015FrozenCollar_activeSeparated_of_gap
      S t 10 (1/5:ℝ) (1/1000:ℝ)
      hScollar htlocal neutralIV016FrozenConcrete_allIntegerGap
  have hcrossPrime :=
    neutralIV014ActiveMixedPrime_zero
      (11/10:ℝ) (11/10:ℝ) (le_refl _)
      S t hSwide htwide 10
      neutralIV015FrozenConcrete_logCutoff hsep
  have hcrossEF :=
    neutralIV014ActiveMixed_eq_analytic
      (11/10:ℝ) (11/10:ℝ) (le_refl _)
      S t hSwide htwide 10
      neutralIV015FrozenConcrete_logCutoff hsep
  obtain ⟨hselfPrime, hselfEF⟩ :=
    neutralIV016FrozenSmallBump_selfPrime_zero t htlocal
  refine ⟨t, htc, htwide, hnew, ?_,
    hcrossPrime, hselfPrime, hcrossEF, hselfEF⟩
  intro heq
  have hzero : S (1/5:ℝ) = 0 :=
    hScollar (1/5:ℝ) neutralIV015FrozenConcrete_centerOutside
  have hv := congrArg (fun f : 𝓢(ℝ, ℂ) => f (1/5:ℝ)) heq
  rw [htc, hzero] at hv
  exact one_ne_zero hv

#print axioms neutralIV015ExistsComplexSchwartzBump
#print axioms neutralIV015FrozenConcrete_logCutoff
#print axioms neutralIV014ActiveMixedPrime_zero
#print axioms neutralIV015FrozenCollar_activeSeparated_of_gap
#print axioms neutralIV016FrozenLogBand_lt10
#print axioms neutralIV016NatLog_nonnegative
#print axioms neutralIV016FrozenFourSignedGaps_of_band
#print axioms neutralIV016FrozenConcrete_allIntegerGap
#print axioms neutralIV016FrozenConcrete_originalPrimeFreeBump
#print axioms neutralIV016FrozenSelfLogClearance
#print axioms neutralIV016FrozenSelfActiveGap
#print axioms neutralIV016FrozenSmallBump_selfPrime_zero
#print axioms neutralIV016ExistsConcretePrimeFreeMixedAndDiagonal

end
end WeilDefect
