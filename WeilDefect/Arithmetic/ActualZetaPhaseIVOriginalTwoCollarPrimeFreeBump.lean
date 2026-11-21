import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalNonzeroPrimeFreeSchwartzBump
import WeilDefect.Arithmetic.ActualZetaPhaseIVFiniteLocalSpan
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
IV015 genuine FROZEN original two-collar Schwartz bump extension.

The original NF543/NF600/NF738 source lives in TWO strict
width-1/500 collars near ±11/10, not throughout the entire coarse
window [-11/10,11/10]. This module constructs an authentic nonzero
complex Schwartz direction outside those two collars whenever a
finite Λ-active translated-interval gap exists.

The resulting t is simultaneously prime-separated from EVERY member
of the original full collar Schwartz subspace, not only from an
abstract finite matrix generator; literal original pole and Gamma
residual remains. It does not prove any finite numerical log gap,
source positivity, or the new Weil diagonal sign.
-/

def neutralIV015FrozenLeftCenter : ℝ := -(11/10 : ℝ) + 1/1000

def neutralIV015FrozenRightCenter : ℝ := (11/10 : ℝ) - 1/1000

def neutralIV015FrozenCollarRadius : ℝ := 1/1000

/-- Exact original two open NF543 collars lie inside the two
closed center/radius intervals with their original 1/500 widths.
No enlargement or relocation of the frozen 2/5 source geometry. -/
theorem neutralIV015FrozenCollars_in_centerIntervals
    (x : ℝ) (hx : x ∈ neutralNF543OriginalCollars) :
    x ∈ Set.Icc (neutralIV015FrozenLeftCenter -
        neutralIV015FrozenCollarRadius)
        (neutralIV015FrozenLeftCenter +
          neutralIV015FrozenCollarRadius) ∨
    x ∈ Set.Icc (neutralIV015FrozenRightCenter -
        neutralIV015FrozenCollarRadius)
        (neutralIV015FrozenRightCenter +
          neutralIV015FrozenCollarRadius) := by
  unfold neutralNF543OriginalCollars at hx
  rcases hx with hL | hR
  · left
    dsimp [neutralIV015FrozenLeftCenter,
      neutralIV015FrozenCollarRadius]
    constructor <;> linarith [hL.1, hL.2]
  · right
    dsimp [neutralIV015FrozenRightCenter,
      neutralIV015FrozenCollarRadius]
    constructor <;> linarith [hR.1, hR.2]

/-- A center gap greater than the sum of physical support radii
excludes every literal overlap of the translated old Schwartz
interval with the prospective new physical bump interval. -/
theorem neutralIV015PhysicalIntervalTranslate_excluded
    (cs ct rs rt τ x : ℝ)
    (hgap : rs + rt < |ct-cs-τ|)
    (hx : x ∈ Set.Icc (ct-rt) (ct+rt)) :
    x-τ ∉ Set.Icc (cs-rs) (cs+rs) := by
  intro hy
  have hd : |ct-cs-τ| ≤ rs+rt := by
    apply abs_le.mpr
    constructor <;> linarith [hx.1,hx.2,hy.1,hy.2]
  exact (not_lt_of_ge hd) hgap

/-- Exact finite real log-frequency exclusion needed for the
UNCHANGED original two collars. The genuine von Mangoldt coefficient
decides which n are relevant, with every active prime power included. -/
def neutralIV015FrozenTwoCollarActiveGap (c r : ℝ) (N : ℕ) : Prop :=
  ∀ m : ℕ, m ∈ Finset.range N →
    ArithmeticFunction.vonMangoldt m ≠ 0 →
      (neutralIV015FrozenCollarRadius+r <
          |c-neutralIV015FrozenLeftCenter-Real.log m| ∧
       neutralIV015FrozenCollarRadius+r <
          |c-neutralIV015FrozenRightCenter-Real.log m|) ∧
      (neutralIV015FrozenCollarRadius+r <
          |c-neutralIV015FrozenLeftCenter+Real.log m| ∧
       neutralIV015FrozenCollarRadius+r <
          |c-neutralIV015FrozenRightCenter+Real.log m|)

/-- Genuine original two-collar old Schwartz functions and a small
new-support Schwartz test cannot have physical translated overlaps
at ANY nonzero original Λ(n) frequency, if the four explicit
frozen collar center separations hold. -/
theorem neutralIV015FrozenCollar_activeSeparated_of_gap
    (s t : 𝓢(ℝ, ℂ)) (N : ℕ) (c r : ℝ)
    (hs : neutralNF735InOriginalCollars s)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (c-r) (c+r) → t x = 0)
    (hgap : neutralIV015FrozenTwoCollarActiveGap c r N) :
    neutralIV014ActivePrimeSeparated s t N := by
  intro m hm hactive x
  by_cases hx : x ∈ Set.Icc (c-r) (c+r)
  · right
    obtain ⟨⟨hLp,hRp⟩,⟨hLn,hRn⟩⟩ := hgap m hm hactive
    constructor
    · apply hs
      intro hy
      rcases neutralIV015FrozenCollars_in_centerIntervals _ hy with hL | hR
      · exact (neutralIV015PhysicalIntervalTranslate_excluded
          neutralIV015FrozenLeftCenter c neutralIV015FrozenCollarRadius r
          (Real.log m) x hLp hx) hL
      · exact (neutralIV015PhysicalIntervalTranslate_excluded
          neutralIV015FrozenRightCenter c neutralIV015FrozenCollarRadius r
          (Real.log m) x hRp hx) hR
    · apply hs
      intro hy
      rcases neutralIV015FrozenCollars_in_centerIntervals _ hy with hL | hR
      · have hnot :=
          neutralIV015PhysicalIntervalTranslate_excluded
            neutralIV015FrozenLeftCenter c neutralIV015FrozenCollarRadius r
            (-Real.log m) x (by simpa only [sub_neg_eq_add] using hLn) hx
        exact hnot (by simpa only [sub_neg_eq_add] using hL)
      · have hnot :=
          neutralIV015PhysicalIntervalTranslate_excluded
            neutralIV015FrozenRightCenter c neutralIV015FrozenCollarRadius r
            (-Real.log m) x (by simpa only [sub_neg_eq_add] using hRn) hx
        exact hnot (by simpa only [sub_neg_eq_add] using hR)
  · left
    exact ht x hx

/-- CONCRETE Schwartz existence relative to the complete original
two-collar support class: if a finite active-log gap fits inside
the authentic window, Mathlib produces a genuine complex Schwartz
bump equal to ONE at c and outside the original two collars.
Uniform active-prime separation is proved for ALL original collar
Schwartz tests, not postulated for a specific matrix representation. -/
theorem neutralIV015ExistsNonzeroNewTwoCollarPrimeSeparatedBump
    (b c r : ℝ) (N : ℕ)
    (hr : 0 < r)
    (hwin : |c| + r < b)
    (houtside : c ∉ neutralNF543OriginalCollars)
    (hgap : neutralIV015FrozenTwoCollarActiveGap c r N) :
    ∃ t : 𝓢(ℝ, ℂ),
      t c = 1 ∧
      (∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0) ∧
      ¬ neutralNF735InOriginalCollars t ∧
      (∀ s : 𝓢(ℝ, ℂ), neutralNF735InOriginalCollars s →
        neutralIV014ActivePrimeSeparated s t N) := by
  obtain ⟨t, htc, htlocal⟩ :=
    neutralIV015ExistsComplexSchwartzBump c r hr
  have htwide :=
    neutralIV015Bump_supported_largeWindow b c r hwin t htlocal
  refine ⟨t, htc, htwide, ?_, ?_⟩
  · intro hOld
    have he : t c = 0 := hOld c houtside
    rw [htc] at he
    exact one_ne_zero he
  · intro s hs
    exact neutralIV015FrozenCollar_activeSeparated_of_gap
      s t N c r hs htlocal hgap

/-- ACTUAL original zeta arithmetic consequence for every old finite
physical Schwartz family in the literal NF543 two collars.
The constructed complex test t is nonzero, cannot belong to the
old collar-supported test class or its finite span, and has ZERO
authentic mixed von-Mangoldt prime term. The complete ORIGINAL
two poles plus Gamma remainder are retained exactly.

New diagonal positivity and the residual Schur determinant bound
are NOT established or even silently assumed in this theorem. -/
theorem neutralIV015ExistsOriginalTwoCollarPrimeFreeDirection
    {n : ℕ} (b c r : ℝ) (N : ℕ)
    (hb : (11/10 : ℝ) ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, neutralNF735InOriginalCollars (s i))
    (hr : 0 < r)
    (hwin : |c| + r < b)
    (houtside : c ∉ neutralNF543OriginalCollars)
    (hgap : neutralIV015FrozenTwoCollarActiveGap c r N)
    (hcut : ∀ m : ℕ, N ≤ m → (11/10 : ℝ)+b < Real.log m) :
    ∃ t : 𝓢(ℝ, ℂ),
      t c = 1 ∧
      (∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0) ∧
      ¬ neutralNF735InOriginalCollars t ∧
      t ≠ neutralIV009PhysicalSchwartzSum s u ∧
      neutralIV011OriginalMixedPrime b
        (neutralIV009PhysicalSchwartzSum s u) t = 0 ∧
      neutralIV010Mixed b
        (neutralIV009PhysicalSchwartzSum s u) t =
        neutralIV013OriginalMixedAnalyticRemainder b
          (neutralIV009PhysicalSchwartzSum s u) t := by
  obtain ⟨t, htc, htwide, hnew, hsepAll⟩ :=
    neutralIV015ExistsNonzeroNewTwoCollarPrimeSeparatedBump
      b c r N hr hwin houtside hgap
  let S := neutralIV009PhysicalSchwartzSum s u
  have hScollar : neutralNF735InOriginalCollars S := by
    change neutralNF735InOriginalCollars
      (∑ i : Fin n, u i • s i)
    exact neutralNF738OriginalCollars_finset_linear
      (Finset.univ : Finset (Fin n)) s u
      (by intro i _; exact hs i)
  have hSwindow :
      ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → S x = 0 :=
    neutralIV009OriginalCollars_supported_window S hScollar
  have hsep : neutralIV014ActivePrimeSeparated S t N :=
    hsepAll S hScollar
  have hprime := neutralIV014ActiveMixedPrime_zero
    (11/10:ℝ) b hb S t hSwindow htwide N hcut hsep
  have hEF := neutralIV014ActiveMixed_eq_analytic
    (11/10:ℝ) b hb S t hSwindow htwide N hcut hsep
  refine ⟨t, htc, htwide, hnew, ?_, hprime, hEF⟩
  intro heq
  have hcZero : S c = 0 := hScollar c houtside
  have hv := congrArg (fun f : 𝓢(ℝ, ℂ) => f c) heq
  rw [htc, hcZero] at hv
  exact one_ne_zero hv

/-- The ORIGINAL 11/10 physical radius has a fully kernel-reducible
cutoff N=10. This uses explicit rigorous Mathlib rational log 2 and
log 5 bounds, not a floating-point value of log 10. -/
theorem neutralIV015FrozenConcrete_logCutoff
    (m : ℕ) (hm : 10 ≤ m) :
    (11/10:ℝ) + (11/10:ℝ) < Real.log (m : ℝ) := by
  have hten : (11/5 : ℝ) < Real.log (10 : ℝ) := by
    rw [Real.log_ten_eq]
    have htwo := Real.log_two_gt_d9
    have hfive := Real.log_five_gt_d9
    linarith
  have hmR : (10 : ℝ) ≤ (m : ℝ) := by exact_mod_cast hm
  have hmon : Real.log (10 : ℝ) ≤ Real.log (m : ℝ) :=
    Real.log_le_log (by norm_num) hmR
  linarith

/-- Source-specific fixed rational center c=1/5 and radius 1/1000,
strictly inside the original 11/10 window BUT OUTSIDE the unchanged
two original strict frozen 1/500 collars. -/
theorem neutralIV015FrozenConcrete_centerOutside :
    (1/5 : ℝ) ∉ neutralNF543OriginalCollars := by
  unfold neutralNF543OriginalCollars
  simp only [Set.mem_union, Set.mem_Ioo, not_or]
  norm_num

/-- The EXACT physical complex Schwartz witness at rational center
1/5 follows from ONE finite numerical arithmetic leaf: the original
signed ±log n frozen-two-collar gap for n<10.
The genuine infinite-prime cutoff itself is already discharged by
the Mathlib-based exact real log(10) inequality above.

The accompanying exact-Fraction arithmetic script INDEPENDENTLY
verifies the finite gap, but the present Lean theorem KEEPS that
finite inequality as an EXPLICIT hypothesis until it is discharged
by a direct kernel theorem. No proof promotion from Python. -/
theorem neutralIV015FrozenConcrete_originalPrimeFreeBump_of_gap
    {n : ℕ}
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, neutralNF735InOriginalCollars (s i))
    (hgap :
      neutralIV015FrozenTwoCollarActiveGap
        (1/5:ℝ) (1/1000:ℝ) 10) :
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
  exact neutralIV015ExistsOriginalTwoCollarPrimeFreeDirection
    (11/10:ℝ) (1/5:ℝ) (1/1000:ℝ) 10
    (le_refl _) s u hs
    (by norm_num)
    (by norm_num)
    neutralIV015FrozenConcrete_centerOutside
    hgap neutralIV015FrozenConcrete_logCutoff

#print axioms neutralIV015ExistsComplexSchwartzBump
#print axioms neutralNF738OriginalCollars_finset_linear
#print axioms neutralIV014ActiveMixedPrime_zero
#print axioms neutralIV014ActiveMixed_eq_analytic
#print axioms neutralIV015FrozenCollars_in_centerIntervals
#print axioms neutralIV015PhysicalIntervalTranslate_excluded
#print axioms neutralIV015FrozenCollar_activeSeparated_of_gap
#print axioms neutralIV015ExistsNonzeroNewTwoCollarPrimeSeparatedBump
#print axioms neutralIV015ExistsOriginalTwoCollarPrimeFreeDirection
#print axioms neutralIV015FrozenConcrete_logCutoff
#print axioms neutralIV015FrozenConcrete_centerOutside
#print axioms neutralIV015FrozenConcrete_originalPrimeFreeBump_of_gap

end
end WeilDefect
