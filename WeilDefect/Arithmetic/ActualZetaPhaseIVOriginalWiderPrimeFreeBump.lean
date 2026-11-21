import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalVariableWidthSignedBudget
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Set
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
IV019: genuine wider NONZERO original complex Schwartz direction.

The IV015 selected original nonzero bump had radius 1/1000
around x=1/5. The prospective positive signed source capacity
permits a radius of 1/500, twice the previous radius. Its new
physical interval [99/500,101/500] is disjoint from the
ORIGINAL unchanged two NF543 strict collars and fits within
the original physical [-11/10,11/10] window.

This Lean module makes NO claim of new full 1/10 old-plus-new
coercivity: to use the IV019 general signed mass budget on a
whole enlarged class one still needs an EXACT NEW old/new
prime transfer and L1 mass bound on the new three-cell union.
This module proves only new real ±log arithmetic separation
of the wider direction, not a fabricated prime bound.
-/

/-- Elementary strict absolute-distance comparison with a true
new physical width 2/500 and old collar radius 1/1000. -/
theorem neutralIV019WideAbsClearance
    (z : ℝ)
    (h : (3/1000:ℝ) < z ∨ z < -(3/1000:ℝ)) :
    (3/1000:ℝ) < |z| := by
  rcases h with hp | hn
  · rw [abs_of_pos (by linarith)]
    exact hp
  · rw [abs_of_neg (by linarith)]
    linarith

/-- The original four signed old-collar-to-new support distances
remain strictly positive at the DOUBLE IV015 new radius 1/500,
using rigorous IV016 exact Real.log-band facts. -/
theorem neutralIV019WideFourSignedGaps_of_band
    (y : ℝ) (hy : 0 ≤ y)
    (hband :
      y ≤ (7/10:ℝ) ∨
      ((109/100:ℝ) ≤ y ∧ y ≤ (11/10:ℝ)) ∨
      ((138/100:ℝ) ≤ y ∧ y ≤ (14/10:ℝ)) ∨
      (16/10:ℝ) ≤ y) :
    ((3/1000:ℝ) < |(1299/1000:ℝ) - y| ∧
      (3/1000:ℝ) < |(-899/1000:ℝ) - y|) ∧
    ((3/1000:ℝ) < |(1299/1000:ℝ) + y| ∧
      (3/1000:ℝ) < |(-899/1000:ℝ) + y|) := by
  have hRminus :
      (3/1000:ℝ) < |(-899/1000:ℝ) - y| := by
    apply neutralIV019WideAbsClearance
    right
    linarith
  have hLplus :
      (3/1000:ℝ) < |(1299/1000:ℝ) + y| := by
    apply neutralIV019WideAbsClearance
    left
    linarith
  refine ⟨⟨?_, hRminus⟩, ⟨hLplus, ?_⟩⟩
  · rcases hband with hsmall | ⟨hlo,hhi⟩ | ⟨hlo,hhi⟩ | hlarge
    · apply neutralIV019WideAbsClearance
      left
      linarith
    · apply neutralIV019WideAbsClearance
      left
      linarith
    · apply neutralIV019WideAbsClearance
      right
      linarith
    · apply neutralIV019WideAbsClearance
      right
      linarith
  · rcases hband with hsmall | ⟨hlo,hhi⟩ | ⟨hlo,hhi⟩ | hlarge
    · apply neutralIV019WideAbsClearance
      right
      linarith
    · apply neutralIV019WideAbsClearance
      left
      linarith
    · apply neutralIV019WideAbsClearance
      left
      linarith
    · apply neutralIV019WideAbsClearance
      left
      linarith

/-- ALL integer 0<=m<10 signed original logarithmic shifts avoid
the exact HISTORICAL two collar supports for a radius 1/500
new cell centered at 1/5. Actual von Mangoldt activity is only
a weaker hypothesis, preserved verbatim from IV014. -/
theorem neutralIV019WideFrozenConcrete_allIntegerGap :
    neutralIV015FrozenTwoCollarActiveGap
      (1/5:ℝ) (1/500:ℝ) 10 := by
  intro m hm _
  have hb :=
    neutralIV016FrozenLogBand_lt10 m (Finset.mem_range.mp hm)
  have hy := neutralIV016NatLog_nonnegative m
  have hh :=
    neutralIV019WideFourSignedGaps_of_band
      (Real.log (m:ℝ)) hy hb
  have hleft :
      (1/5:ℝ) - neutralIV015FrozenLeftCenter =
        (1299/1000:ℝ) := by
    norm_num [neutralIV015FrozenLeftCenter]
  have hright :
      (1/5:ℝ) - neutralIV015FrozenRightCenter =
        (-899/1000:ℝ) := by
    norm_num [neutralIV015FrozenRightCenter]
  have hrad :
      neutralIV015FrozenCollarRadius + (1/500:ℝ) =
        (3/1000:ℝ) := by
    norm_num [neutralIV015FrozenCollarRadius]
  simpa only [hleft,hright,hrad] using hh

/-- All TRUE active original prime-power self-translation shifts
exceed diameter 2/500 of the wider new cell. This is a
real original von Mangoldt/Mathlib LOG proof, not numerical
inspection of a finite list. -/
theorem neutralIV019WideSelfLogClearance
    (m : ℕ)
    (hactive : ArithmeticFunction.vonMangoldt m ≠ 0) :
    (1/250:ℝ) < Real.log (m:ℝ) := by
  have hp :
      Nat.IsPrimePow m :=
    ArithmeticFunction.vonMangoldt_ne_zero_iff.mp hactive
  have hm : 2 ≤ m := hp.two_le
  have hmreal : (2:ℝ) ≤ (m:ℝ) := by
    exact_mod_cast hm
  have hlog : Real.log (2:ℝ) ≤ Real.log (m:ℝ) :=
    Real.log_le_log (by norm_num) hmreal
  have hlo := Real.log_two_gt_d9
  linarith

theorem neutralIV019WideSelfActiveGap :
    ∀ m : ℕ, m ∈ Finset.range 10 →
      ArithmeticFunction.vonMangoldt m ≠ 0 →
      (1/500:ℝ) + (1/500:ℝ) <
        |(1/5:ℝ)-(1/5:ℝ)-Real.log m| ∧
      (1/500:ℝ) + (1/500:ℝ) <
        |(1/5:ℝ)-(1/5:ℝ)+Real.log m| := by
  intro m _ hactive
  have hl := neutralIV019WideSelfLogClearance m hactive
  have habs : |Real.log (m:ℝ)| = Real.log (m:ℝ) :=
    abs_of_pos (by linarith)
  have hs : (1/500:ℝ) + (1/500:ℝ) = 1/250 := by
    norm_num
  constructor
  · simpa only [sub_self,zero_sub,abs_neg,habs,hs] using hl
  · simpa only [sub_self,zero_add,habs,hs] using hl

/-- An actual nonzero complex Schwartz bump at DOUBLE the old
new-cell radius exists using Mathlib's real C∞ compact bump,
Complex.ofRealCLM, and HasCompactSupport.toSchwartzMap.
It is outside the frozen two-collar source class and
PRIME-ACTIVE separated from every original collar test and
from its own nonzero original prime-power translates. -/
theorem neutralIV019ExistsWiderOriginalPrimeSeparatedBump :
    ∃ t : 𝓢(ℝ,ℂ),
      t (1/5:ℝ) = 1 ∧
      (∀ x : ℝ,
        x ∉ Set.Icc ((1/5:ℝ)-(1/500:ℝ))
          ((1/5:ℝ)+(1/500:ℝ)) → t x = 0) ∧
      ¬ neutralNF735InOriginalCollars t ∧
      (∀ S : 𝓢(ℝ,ℂ),
        neutralNF735InOriginalCollars S →
        neutralIV014ActivePrimeSeparated S t 10) ∧
      neutralIV014ActivePrimeSeparated t t 10 := by
  obtain ⟨t,htc,htloc⟩ :=
    neutralIV015ExistsComplexSchwartzBump
      (1/5:ℝ) (1/500:ℝ) (by norm_num)
  have hnew : ¬ neutralNF735InOriginalCollars t := by
    intro hOld
    have hz := hOld (1/5:ℝ)
      neutralIV015FrozenConcrete_centerOutside
    rw [htc] at hz
    exact one_ne_zero hz
  have hself : neutralIV014ActivePrimeSeparated t t 10 :=
    neutralIV014ActiveSeparated_of_intervalGap
      t t 10
      (1/5:ℝ) (1/5:ℝ)
      (1/500:ℝ) (1/500:ℝ)
      htloc htloc neutralIV019WideSelfActiveGap
  refine ⟨t,htc,htloc,hnew,?_,hself⟩
  intro S hS
  exact neutralIV015FrozenCollar_activeSeparated_of_gap
    S t 10 (1/5:ℝ) (1/500:ℝ)
    hS htloc neutralIV019WideFrozenConcrete_allIntegerGap

/-- For the genuinely constructed WIDER real physical test,
both the ORIGINAL mixed old/new and self von Mangoldt prime
contributions vanish exactly, at the SAME historical
original physical window. The old-old n=9 prime may survive
and has not been dropped. The new test's full diagonal sign
is a separate question, not part of the existence proof. -/
theorem neutralIV019ExistsWiderOriginalMixedAndSelfPrimeFree :
    ∃ t : 𝓢(ℝ,ℂ),
      t (1/5:ℝ) = 1 ∧
      ¬ neutralNF735InOriginalCollars t ∧
      neutralIV011OriginalMixedPrime (11/10:ℝ) t t = 0 ∧
      (∀ S : 𝓢(ℝ,ℂ), neutralNF735InOriginalCollars S →
        neutralIV011OriginalMixedPrime (11/10:ℝ) S t = 0) := by
  obtain ⟨t,htc,htloc,hnew,hall,hself⟩ :=
    neutralIV019ExistsWiderOriginalPrimeSeparatedBump
  have htwide :
      ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
        t x = 0 :=
    neutralIV015Bump_supported_largeWindow
      (11/10:ℝ) (1/5:ℝ) (1/500:ℝ)
      (by norm_num) t htloc
  have hPself :=
    neutralIV014ActiveMixedPrime_zero
      (11/10:ℝ) (11/10:ℝ) (le_refl _)
      t t htwide htwide 10
      neutralIV015FrozenConcrete_logCutoff hself
  refine ⟨t,htc,hnew,hPself,?_⟩
  intro S hS
  have hSw :=
    neutralIV009OriginalCollars_supported_window S hS
  exact neutralIV014ActiveMixedPrime_zero
    (11/10:ℝ) (11/10:ℝ) (le_refl _)
    S t hSw htwide 10
    neutralIV015FrozenConcrete_logCutoff (hall S hS)

#print axioms neutralIV016FrozenLogBand_lt10
#print axioms neutralIV015ExistsComplexSchwartzBump
#print axioms neutralIV014ActiveMixedPrime_zero
#print axioms neutralIV019WideAbsClearance
#print axioms neutralIV019WideFourSignedGaps_of_band
#print axioms neutralIV019WideFrozenConcrete_allIntegerGap
#print axioms neutralIV019WideSelfLogClearance
#print axioms neutralIV019WideSelfActiveGap
#print axioms neutralIV019ExistsWiderOriginalPrimeSeparatedBump
#print axioms neutralIV019ExistsWiderOriginalMixedAndSelfPrimeFree

end
end WeilDefect
