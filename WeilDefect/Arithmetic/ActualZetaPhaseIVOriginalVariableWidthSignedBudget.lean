import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalThreeCellPrime9Transfer
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalNarrowSignedGamma
import Mathlib.Analysis.Complex.ExponentialBounds
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory Set
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
IV019 — REAL original signed zeta Weil analytic CAPACITY for variable
physical support size; do not confuse it with a global positivity
theorem or with uncompiled original IV009–IV018 source candidates.

The source attaches the NF599 genuine SIGNED Gamma symbol and BOTH
real zeta pole evaluations to the original literatureRHS, and then
pays the surviving original von Mangoldt PRIME coefficient explicitly.
For an authentic test f supported in the SAME original physical
window [-11/10,11/10], the exact algebraic gate is

 Re W(f,f) >= (7/10) Mass(f) - 75 * ||f||_L1^2

provided the actual prime term satisfies the accepted NF600-style
|Re P(f,f)| <= 2/5 Mass(f). This does NOT assume the NF600 bound
continues outside the old frozen collar class.

For a physical length budget m satisfying ||f||_1^2 <= m Mass,
the residual margin is 7/10 - 75m. For the old two-collar width
1/250 plus a new centered cell of radius r, m=1/250+2r,
giving exactly 2/5-150r. The new radius r=1/500 has a
strict 1/10 prospective original signed margin. It crosses 0
at r=1/375; this is a limit of THIS signed symbolic budget,
not an impossibility theorem for full zeta positivity.
-/

/-- The signed original Gamma contribution is controlled from below
without assuming support on the OLD strict two collars. It is the
TRUE Gamma/digamma Plancherel integral and actual Schwartz L1 norm. -/
theorem neutralIV019OriginalSignedGamma_L1Budget
    (f : 𝓢(ℝ,ℂ)) :
    (11/10:ℝ) * neutralNF600Mass f -
      67 * ‖f.toLp 1 volume‖^2 ≤
      neutralNF600Arch f := by
  have hgamma := neutralIV017SignedGamma_lower f
  have hlow := neutralIV017LowMass_le_tenL1_sq f
  linarith only [hgamma,hlow]

/-- Both ORIGINAL zeta polar residues are retained; the real
original pole diagonal may be negative but is no smaller than
minus eight times genuine Schwartz L1 squared mass. -/
theorem neutralIV019OriginalSignedPole_L1Budget
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → f x = 0) :
    -(8:ℝ) * ‖f.toLp 1 volume‖^2 ≤
      (neutralIV011OriginalMixedPole (11/10:ℝ) f f).re := by
  have hp :=
    neutralIV017OriginalPole_norm_le_eightL1_sq f hf
  have hre :=
    (Complex.abs_re_le_norm
      (neutralIV011OriginalMixedPole (11/10:ℝ) f f)).trans hp
  exact (abs_le.mp hre).1

/-- Genuine TWO poles and signed original Gamma combined into
one source-bound analytic budget. This is the TRUE pole-plus-Gamma
remainder of the original signed literatureRHS, not a positive
replacement oracle or a bound on an abstract Gram operator. -/
theorem neutralIV019OriginalAnalytic_L1Budget
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → f x = 0) :
    (11/10:ℝ) * neutralNF600Mass f -
      75 * ‖f.toLp 1 volume‖^2 ≤
      (neutralIV013OriginalMixedAnalyticRemainder
        (11/10:ℝ) f f).re := by
  have hp := neutralIV019OriginalSignedPole_L1Budget f hf
  have hg := neutralIV019OriginalSignedGamma_L1Budget f
  have heq := neutralIV017OriginalWindowArch_real_eq_spectral
    f hf
  unfold neutralIV013OriginalMixedAnalyticRemainder
  simp only [Complex.add_re]
  rw [heq]
  linarith only [hp,hg]

/-- The source-specific ORIGINAL arithmetic-numerical budget.
THE PRIME HYPOTHESIS IS EXPLICIT and mentions the unchanged
von-Mangoldt term; no diagonal sign or mixed Schur assumption.
-/
theorem neutralIV019OriginalSignedWeil_L1Budget_of_prime
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → f x = 0)
    (hp :
      |(neutralIV011OriginalMixedPrime
        (11/10:ℝ) f f).re| ≤
        (2/5:ℝ) * neutralNF600Mass f) :
    (7/10:ℝ) * neutralNF600Mass f ≤
      (neutralIV010Diagonal (11/10:ℝ) f).re +
        75 * ‖f.toLp 1 volume‖^2 := by
  have ha := neutralIV019OriginalAnalytic_L1Budget f hf
  have hsplit := neutralIV011OriginalMixed_arithmeticSplit
    (11/10:ℝ) f f
  change neutralIV010Diagonal (11/10:ℝ) f =
      neutralIV011OriginalMixedPole (11/10:ℝ) f f -
        neutralIV011OriginalMixedPrime (11/10:ℝ) f f +
        neutralIV011OriginalMixedArch (11/10:ℝ) f f at hsplit
  have hr := congrArg Complex.re hsplit
  simp only [Complex.add_re, Complex.sub_re] at hr
  have hres :
      (neutralIV013OriginalMixedAnalyticRemainder
        (11/10:ℝ) f f).re =
      (neutralIV011OriginalMixedPole
        (11/10:ℝ) f f).re +
      (neutralIV011OriginalMixedArch
        (11/10:ℝ) f f).re := by
    rfl
  have hpUpper := (abs_le.mp hp).2
  linarith only [ha,hr,hres,hpUpper]

/-- Flexible TRUE signed arithmetic-original quadratic lower
with a quantitative support-measure / L1 charge m. The genuine
original prime bound is still an EXPLICIT hypothesis. -/
theorem neutralIV019OriginalSignedWeil_massBudget_of_prime
    (f : 𝓢(ℝ,ℂ)) (m : ℝ)
    (hf : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → f x = 0)
    (hp :
      |(neutralIV011OriginalMixedPrime
        (11/10:ℝ) f f).re| ≤
        (2/5:ℝ) * neutralNF600Mass f)
    (hL1 :
      ‖f.toLp 1 volume‖^2 ≤ m * neutralNF600Mass f) :
    ((7/10:ℝ) - 75*m) * neutralNF600Mass f ≤
      (neutralIV010Diagonal (11/10:ℝ) f).re := by
  have hbase :=
    neutralIV019OriginalSignedWeil_L1Budget_of_prime f hf hp
  have hcost :
      75 * ‖f.toLp 1 volume‖^2 ≤
        75 * (m * neutralNF600Mass f) :=
    mul_le_mul_of_nonneg_left hL1 (by norm_num)
  nlinarith only [hbase,hcost]

/-- This exact threshold is the limit of the ACTUAL signed
Gamma/two-pole/n9-prime ABSOLUTE BUDGET for a new centered
physical interval radius r, preserving the historical old
two-collar total measure 1/250. -/
theorem neutralIV019OriginalRadiusMargin_identity
    (r : ℝ) :
    (7/10:ℝ) - 75*((1/250:ℝ)+2*r) =
      (2/5:ℝ) - 150*r := by
  ring

theorem neutralIV019OriginalRadiusMargin_positive_iff
    (r : ℝ) :
    0 < (2/5:ℝ) - 150*r ↔ r < 1/375 := by
  constructor <;> intro h <;> linarith

/-- Doubling the IV015 bump radius from 1/1000 to 1/500
remains STRICTLY inside the arithmetic-plus-signed-analytic
capacity budget; its proposed full original coercive lower
constant is exactly 1/10 (not a floating-point estimate). -/
theorem neutralIV019OriginalDoubleRadius_margin :
    (7/10:ℝ) -
      75*((1/250:ℝ)+2*(1/500:ℝ)) = 1/10 := by
  norm_num

/-- Actual original source signed 1/10 positivity condition for
any PHYSICAL complex Schwartz test with L1 size <= Mass/125.
This is a flexible real Weil-form statement, not a theorem that
the enlarged 1/500-radius support class automatically satisfies
the genuine prime bound. That physical prime transfer is the
separate outstanding future compiler/source obligation. -/
theorem neutralIV019OriginalOneTenth_of_prime_and_L1
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → f x = 0)
    (hp :
      |(neutralIV011OriginalMixedPrime
        (11/10:ℝ) f f).re| ≤
        (2/5:ℝ) * neutralNF600Mass f)
    (hL1 :
      ‖f.toLp 1 volume‖^2 ≤
        (1/125:ℝ) * neutralNF600Mass f) :
    (1/10:ℝ) * neutralNF600Mass f ≤
      (neutralIV010Diagonal (11/10:ℝ) f).re := by
  have h := neutralIV019OriginalSignedWeil_massBudget_of_prime
    f (1/125:ℝ) hf hp hL1
  convert h using 1 <;> norm_num

#print axioms neutralIV017SignedGamma_lower
#print axioms neutralIV017LowMass_le_tenL1_sq
#print axioms neutralIV017OriginalPole_norm_le_eightL1_sq
#print axioms neutralIV017OriginalWindowArch_real_eq_spectral
#print axioms neutralIV019OriginalSignedGamma_L1Budget
#print axioms neutralIV019OriginalSignedPole_L1Budget
#print axioms neutralIV019OriginalAnalytic_L1Budget
#print axioms neutralIV019OriginalSignedWeil_L1Budget_of_prime
#print axioms neutralIV019OriginalSignedWeil_massBudget_of_prime
#print axioms neutralIV019OriginalRadiusMargin_identity
#print axioms neutralIV019OriginalRadiusMargin_positive_iff
#print axioms neutralIV019OriginalDoubleRadius_margin
#print axioms neutralIV019OriginalOneTenth_of_prime_and_L1

end
end WeilDefect
