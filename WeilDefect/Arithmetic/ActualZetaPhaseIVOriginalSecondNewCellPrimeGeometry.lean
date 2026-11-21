import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalWholeThreeCellSchwartzPartition
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalWiderPrimeFreeBump
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
IV022. Actual original FOUR-CELL arithmetic compatibility investigation.

The ORIGINAL frozen two NF543 collars remain unchanged. IV020/021
add the true positive-center physical Schwartz interval
  E₊ = [99/500,101/500] = [0.198,0.202].
This module proposes a SECOND independent physical Schwartz cell
  E₋ = [-1/5-1/4000,-1/5+1/4000].
The original cutoff remains b=11/10, N=10. We retain every true
von-Mangoldt coefficient and both signed logarithmic shifts.

Theorems independently check the actual old-to-second cell
FOUR signed real log inequalities, the new-to-new PRIME-ACTIVE
translated physical separation, and the second cell's self
separation; construct a real nonzero complex Schwartz second
direction independent of the old space plus EVERY first-cell
source. No source positivity is inferred from prime-free cross
terms. Compiler and strict source standard-axiom audit pending.
-/

/-- Center and radius of the SECOND prospective new physical cell. -/
def neutralIV022SecondCenter : ℝ := -(1/5:ℝ)
def neutralIV022SecondRadius : ℝ := 1/4000

/-- The true NF543 old collar source does not contain the
second candidate center, and the new second center lies outside
the first physical added cell. -/
theorem neutralIV022SecondCenter_outside :
    neutralIV022SecondCenter ∉ neutralNF543OriginalCollars ∧
    neutralIV022SecondCenter ∉ neutralIV020WidePhysicalInterval := by
  constructor
  · unfold neutralIV022SecondCenter neutralNF543OriginalCollars
    simp only [Set.mem_union,Set.mem_Ioo,not_or]
    norm_num
  · unfold neutralIV022SecondCenter neutralIV020WidePhysicalInterval
    norm_num

/-- Original log lower bound at every actual nonzero
von-Mangoldt prime power, obtained from genuine Mathlib
log 2 ≥ .693, not an oracle on finite prime samples. -/
theorem neutralIV022ActiveOriginalLog_gtHalf
    (m : ℕ) (hactive : ArithmeticFunction.vonMangoldt m ≠ 0) :
    (1/2:ℝ) < Real.log (m:ℝ) := by
  have hprime : Nat.IsPrimePow m :=
    ArithmeticFunction.vonMangoldt_ne_zero_iff.mp hactive
  have hm : 2 ≤ m := hprime.two_le
  have hmR : (2:ℝ) ≤ (m:ℝ) := by exact_mod_cast hm
  have hmon : Real.log (2:ℝ) ≤ Real.log (m:ℝ) :=
    Real.log_le_log (by norm_num) hmR
  have htwo := Real.log_two_gt_d9
  linarith

/-- Mirror the already rigorous IV016 TRUE original four-band
inequalities across x=0. The new source center is -1/5, with
actual old collar center differences +899/1000 and -1299/1000.
The new required clearance 1/1000+1/4000=1/800 is STRICTLY
smaller than IV016's certified 1/500 clearance. -/
theorem neutralIV022SecondFourGap_of_band
    (y : ℝ) (hy : 0 ≤ y)
    (hb :
      y ≤ (7/10:ℝ) ∨
      ((109/100:ℝ) ≤ y ∧ y ≤ (11/10:ℝ)) ∨
      ((138/100:ℝ) ≤ y ∧ y ≤ (14/10:ℝ)) ∨
      (16/10:ℝ) ≤ y) :
    ((1/800:ℝ) < |(899/1000:ℝ)-y| ∧
      (1/800:ℝ) < |(-1299/1000:ℝ)-y|) ∧
    ((1/800:ℝ) < |(899/1000:ℝ)+y| ∧
      (1/800:ℝ) < |(-1299/1000:ℝ)+y|) := by
  obtain ⟨⟨hA,hB⟩,⟨hC,hD⟩⟩ :=
    neutralIV016FrozenFourSignedGaps_of_band y hy hb
  have h1 : |(899/1000:ℝ)-y| = |(-899/1000:ℝ)+y| := by
    have he : (899/1000:ℝ)-y = -((-899/1000:ℝ)+y) := by ring
    rw [he,abs_neg]
  have h2 : |(-1299/1000:ℝ)-y| = |(1299/1000:ℝ)+y| := by
    have he : (-1299/1000:ℝ)-y = -((1299/1000:ℝ)+y) := by ring
    rw [he,abs_neg]
  have h3 : |(899/1000:ℝ)+y| = |(-899/1000:ℝ)-y| := by
    have he : (899/1000:ℝ)+y = -((-899/1000:ℝ)-y) := by ring
    rw [he,abs_neg]
  have h4 : |(-1299/1000:ℝ)+y| = |(1299/1000:ℝ)-y| := by
    have he : (-1299/1000:ℝ)+y = -((1299/1000:ℝ)-y) := by ring
    rw [he,abs_neg]
  rw [h1,h2,h3,h4]
  constructor
  · exact ⟨by linarith [hD],by linarith [hC]⟩
  · exact ⟨by linarith [hB],by linarith [hA]⟩

/-- Exact frozen TWO-collar signed logarithmic gap for ALL
arithmetic-active m<10 for the SECOND real new source cell. -/
theorem neutralIV022SecondFrozenTwoCollarActiveGap :
    neutralIV015FrozenTwoCollarActiveGap
      neutralIV022SecondCenter neutralIV022SecondRadius 10 := by
  intro m hm _
  have hy := neutralIV016NatLog_nonnegative m
  have hb := neutralIV016FrozenLogBand_lt10 m (Finset.mem_range.mp hm)
  have hh := neutralIV022SecondFourGap_of_band
    (Real.log (m:ℝ)) hy hb
  have hL :
      neutralIV022SecondCenter-neutralIV015FrozenLeftCenter =
        (899/1000:ℝ) := by
    norm_num [neutralIV022SecondCenter,neutralIV015FrozenLeftCenter]
  have hR :
      neutralIV022SecondCenter-neutralIV015FrozenRightCenter =
        (-1299/1000:ℝ) := by
    norm_num [neutralIV022SecondCenter,neutralIV015FrozenRightCenter]
  have hrad :
      neutralIV015FrozenCollarRadius+neutralIV022SecondRadius =
        (1/800:ℝ) := by
    norm_num [neutralIV015FrozenCollarRadius,neutralIV022SecondRadius]
  simpa only [hL,hR,hrad] using hh

/-- First-new-to-second-new center difference is -2/5.
Its gap to every ACTUAL prime-power log is at least 1/10,
much larger than total cell radii 1/500+1/4000=9/4000. -/
theorem neutralIV022FirstSecondActiveGap :
    ∀ m : ℕ, m ∈ Finset.range 10 →
      ArithmeticFunction.vonMangoldt m ≠ 0 →
      (1/500:ℝ)+(1/4000:ℝ) <
        |(-1/5:ℝ)-(1/5:ℝ)-Real.log m| ∧
      (1/500:ℝ)+(1/4000:ℝ) <
        |(-1/5:ℝ)-(1/5:ℝ)+Real.log m| := by
  intro m _ hactive
  have hy := neutralIV022ActiveOriginalLog_gtHalf m hactive
  have h1 :
      (-1/5:ℝ)-(1/5:ℝ)-Real.log m < 0 := by linarith
  have h2 :
      0 < (-1/5:ℝ)-(1/5:ℝ)+Real.log m := by linarith
  rw [abs_of_neg h1,abs_of_pos h2]
  constructor <;> linarith

/-- The second new source is also separated from ITS OWN
±log m prime-power shifts: its physical diameter is 1/2000,
whereas every active log m is >1/2. -/
theorem neutralIV022SecondSelfActiveGap :
    ∀ m : ℕ, m ∈ Finset.range 10 →
      ArithmeticFunction.vonMangoldt m ≠ 0 →
      (1/4000:ℝ)+(1/4000:ℝ) <
        |(-1/5:ℝ)-(-1/5:ℝ)-Real.log m| ∧
      (1/4000:ℝ)+(1/4000:ℝ) <
        |(-1/5:ℝ)-(-1/5:ℝ)+Real.log m| := by
  intro m _ hactive
  have hy := neutralIV022ActiveOriginalLog_gtHalf m hactive
  simp only [sub_self,zero_sub,abs_neg,zero_add,abs_of_pos (by linarith : 0<Real.log (m:ℝ))]
  constructor <;> linarith

/-- Actual SECOND complex Schwartz direction at x=-1/5:
independent of the entire ORIGINAL old-collar source plus ANY
complex multiple of the first new interval-supported Schwartz
test. All true source active prime-power old/new1/new2 and new2
self shifts are separated by exact geometry.

The final full FOUR-CELL signed positivity theorem is NOT
derived here: it requires true joint prime transfer and
physical support-measure custody, separately testable. -/
theorem neutralIV022ExistsIndependentSecondPrimeFreeSchwartz
    (t₁ : 𝓢(ℝ,ℂ))
    (ht₁ : ∀ x : ℝ,
      x ∉ Set.Icc ((1/5:ℝ)-(1/500:ℝ))
        ((1/5:ℝ)+(1/500:ℝ)) → t₁ x = 0) :
    ∃ t₂ : 𝓢(ℝ,ℂ),
      t₂ (-1/5:ℝ)=1 ∧
      (∀ x : ℝ,
        x ∉ Set.Icc ((-1/5:ℝ)-(1/4000:ℝ))
          ((-1/5:ℝ)+(1/4000:ℝ)) → t₂ x=0) ∧
      (∀ S : 𝓢(ℝ,ℂ), neutralNF735InOriginalCollars S →
        ∀ v : ℂ, t₂ ≠ S+v•t₁) ∧
      (∀ S : 𝓢(ℝ,ℂ), neutralNF735InOriginalCollars S →
        neutralIV014ActivePrimeSeparated S t₂ 10) ∧
      neutralIV014ActivePrimeSeparated t₁ t₂ 10 ∧
      neutralIV014ActivePrimeSeparated t₂ t₂ 10 := by
  obtain ⟨t₂,ht₂,htloc⟩ :=
    neutralIV015ExistsComplexSchwartzBump
      (-1/5:ℝ) (1/4000:ℝ) (by norm_num)
  have hOldGap :
      ∀ S : 𝓢(ℝ,ℂ), neutralNF735InOriginalCollars S →
        neutralIV014ActivePrimeSeparated S t₂ 10 := by
    intro S hS
    exact neutralIV015FrozenCollar_activeSeparated_of_gap
      S t₂ 10 neutralIV022SecondCenter neutralIV022SecondRadius
      hS (by simpa only [neutralIV022SecondCenter,
        neutralIV022SecondRadius] using htloc)
      neutralIV022SecondFrozenTwoCollarActiveGap
  have hcross : neutralIV014ActivePrimeSeparated t₁ t₂ 10 :=
    neutralIV014ActiveSeparated_of_intervalGap
      t₁ t₂ 10 (1/5:ℝ) (-1/5:ℝ)
      (1/500:ℝ) (1/4000:ℝ) ht₁ htloc
      neutralIV022FirstSecondActiveGap
  have hself : neutralIV014ActivePrimeSeparated t₂ t₂ 10 :=
    neutralIV014ActiveSeparated_of_intervalGap
      t₂ t₂ 10 (-1/5:ℝ) (-1/5:ℝ)
      (1/4000:ℝ) (1/4000:ℝ) htloc htloc
      neutralIV022SecondSelfActiveGap
  refine ⟨t₂,ht₂,htloc,?_,hOldGap,hcross,hself⟩
  intro S hS v heq
  have hzS : S (-1/5:ℝ)=0 :=
    hS (-1/5:ℝ) (by
      unfold neutralNF543OriginalCollars
      simp only [Set.mem_union,Set.mem_Ioo,not_or]
      norm_num)
  have hzt₁ : t₁ (-1/5:ℝ)=0 := ht₁ (-1/5:ℝ) (by norm_num)
  have heval := congrArg (fun f : 𝓢(ℝ,ℂ) => f (-1/5:ℝ)) heq
  simp [hzS,hzt₁] at heval
  exact one_ne_zero heval.symm

#print axioms neutralIV016FrozenFourSignedGaps_of_band
#print axioms neutralIV019WideFrozenConcrete_allIntegerGap
#print axioms neutralIV014ActiveSeparated_of_intervalGap
#print axioms neutralIV015ExistsComplexSchwartzBump
#print axioms neutralIV022SecondCenter_outside
#print axioms neutralIV022ActiveOriginalLog_gtHalf
#print axioms neutralIV022SecondFourGap_of_band
#print axioms neutralIV022SecondFrozenTwoCollarActiveGap
#print axioms neutralIV022FirstSecondActiveGap
#print axioms neutralIV022SecondSelfActiveGap
#print axioms neutralIV022ExistsIndependentSecondPrimeFreeSchwartz

end
end WeilDefect
