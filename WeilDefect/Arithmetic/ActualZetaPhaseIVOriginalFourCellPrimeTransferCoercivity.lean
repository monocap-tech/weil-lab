import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalFourCellSmoothSchwartzPartition
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalWiderThreeCellPrime9Coercivity
import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalSecondNewCellPrimeGeometry
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
IV023 — THE COMPLETE AUTHENTIC ORIGINAL FOUR-CELL PRIME DICTIONARY.

For any original three-cell source U and arbitrary SECOND new-cell
source t, all genuine von-Mangoldt-active ±log(n) correlation samples
of U+v•t equal those of U. The old original n=9 term is NOT zeroed.

First prove a genuine Schwartz-space source translated-correlation
integral identity with explicit three vanishing translated products.
Then derive signed samples at every true active n<10 using
  * IV022 second-vs-original-two-collar strict real-log gap;
  * IV022 first-new-vs-second-new strict real-log gap;
  * IV022 second self-log gap.
At inactive indices the ACTUAL coefficient Λ(n)=0. At n>=10
the original full physical radius 11/10 gives zero correlation.

The original complete infinite prime sum reduces to that of U.
IV021 then reduces U to the original old two-collar component.
Real disjointness of source supports preserves physical L2 mass,
so the NF600 historical original n9 cost remains <=2/5 total Mass.

Finally the IV022 signed two-pole + Gamma physical width estimate
establishes a 1/16 genuine original Weil lower for EVERY Schwartz
test supported in the actual FOUR-CELL union — a restricted
test-domain candidate, NEVER global Weil positivity or RH.

All are actual Lean source PROOF CANDIDATES until direct pinned
kernel compiler and standard axiom audits succeed.
-/

/-- Source-support dictionary: the three-cell base and second
physical cell are disjoint and their complex Schwartz sum stays
in the same ORIGINAL physical four-cell/window, without moving
the actual original zeta prime truncation. -/
theorem neutralIV023BaseSecond_supportedFourCell
    (U t : 𝓢(ℝ,ℂ)) (v : ℂ)
    (hU : ∀ x : ℝ,
      x ∉ neutralIV020WideThreeCellSupport → U x=0)
    (ht : ∀ x : ℝ,
      x ∉ neutralIV022FourthCellInterval → t x=0) :
    ∀ x : ℝ,
      x ∉ neutralIV022FourCellSupport → (U+v•t) x=0 := by
  intro x hx
  have hu : x ∉ neutralIV020WideThreeCellSupport :=
    fun h => hx (Or.inl h)
  have hv : x ∉ neutralIV022FourthCellInterval :=
    fun h => hx (Or.inr h)
  simp [hU x hu,ht x hv]

/-- Actual pointwise Lebesgue source mass-addition for THREE
physical base cells plus a disjoint fourth cell; both terms
are genuine complex Schwartz functions, not abstract vectors. -/
theorem neutralIV023BaseSecond_mass_add
    (U t : 𝓢(ℝ,ℂ)) (v : ℂ)
    (hU : ∀ x : ℝ,
      x ∉ neutralIV020WideThreeCellSupport → U x=0)
    (ht : ∀ x : ℝ,
      x ∉ neutralIV022FourthCellInterval → t x=0) :
    neutralNF600Mass (U+v•t) =
      neutralNF600Mass U + neutralNF600Mass (v•t) := by
  have hdisj (x : ℝ) : U x=0 ∨ t x=0 := by
    by_cases hx : x ∈ neutralIV020WideThreeCellSupport
    · right
      have hnot : x ∉ neutralIV022FourthCellInterval :=
        (Set.disjoint_left.mp neutralIV022FourCell_disjoint) hx
      exact ht x hnot
    · left
      exact hU x hx
  have hpoint (x : ℝ) :
      ‖(U+v•t) x‖^2 =
        ‖U x‖^2 + ‖(v•t) x‖^2 := by
    rcases hdisj x with hu | htzero
    · simp [hu]
    · simp [htzero]
  have hiU : Integrable (fun x : ℝ => ‖U x‖^2) :=
    (memLp_two_iff_integrable_sq_norm
      U.continuous.aestronglyMeasurable).mp (U.memLp 2 volume)
  have hiT : Integrable (fun x : ℝ => ‖(v•t) x‖^2) :=
    (memLp_two_iff_integrable_sq_norm
      (v•t).continuous.aestronglyMeasurable).mp
      ((v•t).memLp 2 volume)
  calc
    neutralNF600Mass (U+v•t) =
      ∫ x : ℝ, ‖(U+v•t) x‖^2 :=
        neutralNF600Mass_eq_integral _
    _ = ∫ x : ℝ, (‖U x‖^2+‖(v•t) x‖^2) := by
      apply integral_congr_ae
      filter_upwards [] with x
      exact hpoint x
    _ = (∫ x : ℝ, ‖U x‖^2)+
          (∫ x : ℝ, ‖(v•t) x‖^2) :=
        integral_add hiU hiT
    _ = neutralNF600Mass U+neutralNF600Mass (v•t) := by
      rw [←neutralNF600Mass_eq_integral U,
        ←neutralNF600Mass_eq_integral (v•t)]

theorem neutralIV023BaseMass_le_expandedMass
    (U t : 𝓢(ℝ,ℂ)) (v : ℂ)
    (hU : ∀ x : ℝ,
      x ∉ neutralIV020WideThreeCellSupport → U x=0)
    (ht : ∀ x : ℝ,
      x ∉ neutralIV022FourthCellInterval → t x=0) :
    neutralNF600Mass U ≤ neutralNF600Mass (U+v•t) := by
  have heq := neutralIV023BaseSecond_mass_add U t v hU ht
  have hm : 0 ≤ neutralNF600Mass (v•t) := by
    unfold neutralNF600Mass
    positivity
  linarith

/-- The authentic original real translated correlation integral.
Whenever all THREE non-base complex Schwartz translated products
vanish at τ, U+v•t has EXACTLY U's original complex correlation.
This also proves the other orientation of each mixed term rather
than assuming Hermitian symmetry of the prime sum. -/
theorem neutralIV023BaseSecondCorrelation_eq_base_of_threeZeros
    (U t : 𝓢(ℝ,ℂ)) (v : ℂ) (τ : ℝ)
    (hU : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → U x=0)
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x=0)
    (hTU : ∀ x : ℝ, t x=0 ∨ U (x-τ)=0)
    (hUT : ∀ x : ℝ, t (x-τ)=0 ∨ U x=0)
    (hTT : ∀ x : ℝ, t x=0 ∨ t (x-τ)=0) :
    neutralWindowCorrelation (11/10:ℝ)
      ((U+v•t).toLp 2 volume) ((U+v•t).toLp 2 volume) τ =
    neutralWindowCorrelation (11/10:ℝ)
      (U.toLp 2 volume) (U.toLp 2 volume) τ := by
  have hW : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
        (U+v•t) x=0 := by
    intro x hx
    simp [hU x hx,ht x hx]
  rw [neutralIV011MixedCorrelation_eq_schwartzIntegral
      (11/10:ℝ) (11/10:ℝ) (le_refl _)
      (U+v•t) (U+v•t) hW hW τ,
      neutralIV011MixedCorrelation_eq_schwartzIntegral
      (11/10:ℝ) (11/10:ℝ) (le_refl _)
      U U hU hU τ]
  apply integral_congr_ae
  filter_upwards [] with x
  have ha : (v*t x)*conj (U (x-τ))=0 := by
    rcases hTU x with hz|hz <;> simp [hz]
  have hb : U x*conj (v*t (x-τ))=0 := by
    rcases hUT x with hz|hz <;> simp [hz]
  have hc : (v*t x)*conj (v*t (x-τ))=0 := by
    rcases hTT x with hz|hz <;> simp [hz]
  change (U x+v*t x)*conj (U (x-τ)+v*t (x-τ)) =
    U x*conj (U (x-τ))
  calc
    _ = U x*conj (U (x-τ))+
          (v*t x)*conj (U (x-τ))+
          U x*conj (v*t (x-τ))+
          (v*t x)*conj (v*t (x-τ)) := by
      rw [map_add]
      ring
    _ = U x*conj (U (x-τ)) := by
      rw [ha,hb,hc]
      ring

/-- The actual arithmetic-active separation property is stable
under adding TWO complex Schwartz base components. No artificial
scalar positivity or Gram condition is needed. -/
theorem neutralIV023ActiveSeparated_add
    (s₁ s₂ t : 𝓢(ℝ,ℂ)) (N : ℕ)
    (h₁ : neutralIV014ActivePrimeSeparated s₁ t N)
    (h₂ : neutralIV014ActivePrimeSeparated s₂ t N) :
    neutralIV014ActivePrimeSeparated (s₁+s₂) t N := by
  intro n hn hactive x
  rcases h₁ n hn hactive x with htzero|⟨hpos₁,hneg₁⟩
  · exact Or.inl htzero
  · rcases h₂ n hn hactive x with htzero|⟨hpos₂,hneg₂⟩
    · exact Or.inl htzero
    · right
      constructor
      · simp [hpos₁,hpos₂]
      · simp [hneg₁,hneg₂]

/-- Every original THREE-CELL Schwartz source is genuinely
separated from the second new cell at ALL original arithmetic-
active prime powers. The proof uses IV021's REAL physical smooth
Schwartz decomposition and BOTH authentic IV022 gap certificates. -/
theorem neutralIV023ThreeCellSecond_activeSeparated
    (U t : 𝓢(ℝ,ℂ))
    (hU : ∀ x : ℝ,
      x ∉ neutralIV020WideThreeCellSupport → U x=0)
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc ((-1/5:ℝ)-(1/4000:ℝ))
        ((-1/5:ℝ)+(1/4000:ℝ)) → t x=0) :
    neutralIV014ActivePrimeSeparated U t 10 := by
  obtain ⟨hOld,hFirst,hSplit⟩ :=
    neutralIV021EveryThreeCellSchwartz_decomposes U hU
  have hOldGap : neutralIV014ActivePrimeSeparated
      (neutralIV021OldCellPart U) t 10 :=
    neutralIV015FrozenCollar_activeSeparated_of_gap
      (neutralIV021OldCellPart U) t 10
      (-1/5:ℝ) (1/4000:ℝ) hOld ht
      (by simpa only [neutralIV022SecondCenter,
        neutralIV022SecondRadius] using
          neutralIV022SecondFrozenTwoCollarActiveGap)
  have hFirstRange :
      ∀ x : ℝ,
      x ∉ Set.Icc ((1/5:ℝ)-(1/500:ℝ))
        ((1/5:ℝ)+(1/500:ℝ)) →
        neutralIV021NewCellPart U x=0 := by
    simpa only [neutralIV020WidePhysicalInterval,
      show (1/5:ℝ)-(1/500:ℝ)=99/500 by norm_num,
      show (1/5:ℝ)+(1/500:ℝ)=101/500 by norm_num] using hFirst
  have hFirstGap : neutralIV014ActivePrimeSeparated
      (neutralIV021NewCellPart U) t 10 :=
    neutralIV014ActiveSeparated_of_intervalGap
      (neutralIV021NewCellPart U) t 10
      (1/5:ℝ) (-1/5:ℝ)
      (1/500:ℝ) (1/4000:ℝ)
      hFirstRange ht neutralIV022FirstSecondActiveGap
  have hUnion := neutralIV023ActiveSeparated_add
    (neutralIV021OldCellPart U)
    (neutralIV021NewCellPart U) t 10 hOldGap hFirstGap
  simpa only [←hSplit] using hUnion

/-- LITERAL signed ±log m original correlation equality for EVERY
genuinely active original von-Mangoldt prime power m<10. The
three physical cross terms vanish by real source evaluation,
not from averaging or a spectral positivity assumption. -/
theorem neutralIV023ThreeCellSecond_activeCorrelation_eq
    (U t : 𝓢(ℝ,ℂ)) (v : ℂ)
    (hU : ∀ x : ℝ,
      x ∉ neutralIV020WideThreeCellSupport → U x=0)
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc ((-1/5:ℝ)-(1/4000:ℝ))
        ((-1/5:ℝ)+(1/4000:ℝ)) → t x=0)
    (m : ℕ) (hm : m ∈ Finset.range 10)
    (hactive : ArithmeticFunction.vonMangoldt m ≠ 0) :
    neutralWindowCorrelation (11/10:ℝ)
      ((U+v•t).toLp 2 volume) ((U+v•t).toLp 2 volume)
      (Real.log m) =
    neutralWindowCorrelation (11/10:ℝ)
      (U.toLp 2 volume) (U.toLp 2 volume)
      (Real.log m) ∧
    neutralWindowCorrelation (11/10:ℝ)
      ((U+v•t).toLp 2 volume) ((U+v•t).toLp 2 volume)
      (-Real.log m) =
    neutralWindowCorrelation (11/10:ℝ)
      (U.toLp 2 volume) (U.toLp 2 volume)
      (-Real.log m) := by
  have hTU : neutralIV014ActivePrimeSeparated U t 10 :=
    neutralIV023ThreeCellSecond_activeSeparated U t hU ht
  have hTT : neutralIV014ActivePrimeSeparated t t 10 :=
    neutralIV014ActiveSeparated_of_intervalGap
      t t 10 (-1/5:ℝ) (-1/5:ℝ)
      (1/4000:ℝ) (1/4000:ℝ)
      ht ht neutralIV022SecondSelfActiveGap
  have hUw :=
    neutralIV020WideThreeCell_supported_window U hU
  have htw :
      ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → t x=0 := by
    intro x hx
    apply ht x
    intro hy
    exact hx ⟨by linarith [hy.1],by linarith [hy.2]⟩
  have hpTU (x : ℝ) :
      t x=0 ∨ U (x-Real.log m)=0 := by
    rcases hTU m hm hactive x with hz|⟨hz,_⟩
    · exact Or.inl hz
    · exact Or.inr hz
  have hnTU (x : ℝ) :
      t x=0 ∨ U (x-(-Real.log m))=0 := by
    rcases hTU m hm hactive x with hz|⟨_,hz⟩
    · exact Or.inl hz
    · exact Or.inr (by simpa only [sub_neg_eq_add] using hz)
  have hpUT (x : ℝ) :
      t (x-Real.log m)=0 ∨ U x=0 := by
    rcases hTU m hm hactive (x-Real.log m) with hz|⟨_,hz⟩
    · exact Or.inl hz
    · exact Or.inr (by simpa only [sub_add_cancel] using hz)
  have hnUT (x : ℝ) :
      t (x-(-Real.log m))=0 ∨ U x=0 := by
    rcases hTU m hm hactive (x+Real.log m) with hz|⟨hz,_⟩
    · exact Or.inl (by simpa only [sub_neg_eq_add] using hz)
    · exact Or.inr (by simpa only [add_sub_cancel_right] using hz)
  have hpTT (x : ℝ) :
      t x=0 ∨ t (x-Real.log m)=0 := by
    rcases hTT m hm hactive x with hz|⟨hz,_⟩
    · exact Or.inl hz
    · exact Or.inr hz
  have hnTT (x : ℝ) :
      t x=0 ∨ t (x-(-Real.log m))=0 := by
    rcases hTT m hm hactive x with hz|⟨_,hz⟩
    · exact Or.inl hz
    · exact Or.inr (by simpa only [sub_neg_eq_add] using hz)
  constructor
  · exact neutralIV023BaseSecondCorrelation_eq_base_of_threeZeros
      U t v (Real.log m) hUw htw hpTU hpUT hpTT
  · exact neutralIV023BaseSecondCorrelation_eq_base_of_threeZeros
      U t v (-Real.log m) hUw htw hnTU hnUT hnTT

/-- COMPLETE ORIGINAL INFINITE von Mangoldt sum transfer for
EVERY THREE-CELL Schwartz base U and SECOND-cell t. At inactive
m the original literal Λ(m) coefficient is zero. At all m>=10
the original unchanged |x|<=11/10 physical support eliminates
the relevant translated correlation. n=9 is NOT removed. -/
theorem neutralIV023ThreeCellSecond_originalPrime_eq
    (U t : 𝓢(ℝ,ℂ)) (v : ℂ)
    (hU : ∀ x : ℝ,
      x ∉ neutralIV020WideThreeCellSupport → U x=0)
    (ht : ∀ x : ℝ,
      x ∉ Set.Icc ((-1/5:ℝ)-(1/4000:ℝ))
        ((-1/5:ℝ)+(1/4000:ℝ)) → t x=0) :
    neutralIV011OriginalMixedPrime (11/10:ℝ)
      (U+v•t) (U+v•t) =
    neutralIV011OriginalMixedPrime (11/10:ℝ) U U := by
  have htSecond :
      ∀ x : ℝ, x ∉ neutralIV022FourthCellInterval → t x=0 := by
    simpa only [neutralIV022FourthCellInterval] using ht
  have hW : ∀ x : ℝ,
      x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) →
        (U+v•t) x=0 :=
    neutralIV022FourCell_supported_window (U+v•t)
      (neutralIV023BaseSecond_supportedFourCell
        U t v hU htSecond)
  have hUw := neutralIV020WideThreeCell_supported_window U hU
  rw [neutralIV011OriginalMixedPrime_eq_finite
      (11/10:ℝ) (11/10:ℝ) (le_refl _)
      (U+v•t) (U+v•t) hW hW 10
      neutralIV015FrozenConcrete_logCutoff,
      neutralIV011OriginalMixedPrime_eq_finite
      (11/10:ℝ) (11/10:ℝ) (le_refl _)
      U U hUw hUw 10 neutralIV015FrozenConcrete_logCutoff]
  apply Finset.sum_congr rfl
  intro m hm
  by_cases hz : ArithmeticFunction.vonMangoldt m=0
  · simp [hz]
  · obtain ⟨hPlus,hMinus⟩ :=
      neutralIV023ThreeCellSecond_activeCorrelation_eq
        U t v hU ht m hm hz
    rw [hPlus,hMinus]

/-- Main falsifiable IV022-C compatibility conjecture attached to
the ACTUAL original zeta prime definition: for ANY Schwartz f
supported in ALL FOUR physical cells, the COMPLETE original
arithmetical prime term equals that of the ORIGINAL strict
two-collar Schwartz component selected by the two smooth cuts.

This is a proposed exact equality, not an assumed equivalence
to another arithmetic or spectral realization. -/
theorem neutralIV023EveryFourCell_originalPrime_eq_old
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ neutralIV022FourCellSupport → f x=0) :
    neutralIV011OriginalMixedPrime (11/10:ℝ) f f =
      neutralIV011OriginalMixedPrime (11/10:ℝ)
        (neutralIV023OldPart f) (neutralIV023OldPart f) := by
  obtain ⟨hU,ht,hSplit⟩ :=
    neutralIV023FourCell_split_threePlusOne f hf
  have htRange :
      ∀ x : ℝ,
      x ∉ Set.Icc ((-1/5:ℝ)-(1/4000:ℝ))
        ((-1/5:ℝ)+(1/4000:ℝ)) →
          neutralIV023SecondPart f x=0 := by
    simpa only [neutralIV022FourthCellInterval] using ht
  have hp := neutralIV023ThreeCellSecond_originalPrime_eq
    (neutralIV023BasePart f) (neutralIV023SecondPart f)
    (1:ℂ) hU htRange
  have hOld := neutralIV021EveryThreeCell_originalPrime_eq_old
    (neutralIV023BasePart f) hU
  change neutralIV011OriginalMixedPrime (11/10:ℝ) f f =
    neutralIV011OriginalMixedPrime (11/10:ℝ)
      (neutralIV021OldCellPart (neutralIV023BasePart f))
      (neutralIV021OldCellPart (neutralIV023BasePart f))
  calc
    _ = neutralIV011OriginalMixedPrime (11/10:ℝ)
          (neutralIV023BasePart f+neutralIV023SecondPart f)
          (neutralIV023BasePart f+neutralIV023SecondPart f) := by
      rw [←hSplit]
    _ = neutralIV011OriginalMixedPrime (11/10:ℝ)
          (neutralIV023BasePart f) (neutralIV023BasePart f) := by
      simpa only [one_smul] using hp
    _ = neutralIV011OriginalMixedPrime (11/10:ℝ)
          (neutralIV021OldCellPart (neutralIV023BasePart f))
          (neutralIV021OldCellPart (neutralIV023BasePart f)) := hOld

/-- The genuine original old two-collar L2 mass is NO LARGER
than the actual four-cell physical source mass, because both
new parts are supported on REAL disjoint physical cells.
This is not a numerical solve containment or formal Gram claim. -/
theorem neutralIV023OldMass_le_fourCellMass
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ neutralIV022FourCellSupport → f x=0) :
    neutralNF600Mass (neutralIV023OldPart f) ≤
      neutralNF600Mass f := by
  obtain ⟨hU,hSecond,hFullSplit⟩ :=
    neutralIV023FourCell_split_threePlusOne f hf
  obtain ⟨hOld,hFirst,hThreeSplit⟩ :=
    neutralIV021EveryThreeCellSchwartz_decomposes
      (neutralIV023BasePart f) hU
  have hOldBound := neutralIV020WideOldMass_le_expandedMass
    (neutralIV021OldCellPart (neutralIV023BasePart f))
    (neutralIV021NewCellPart (neutralIV023BasePart f))
    (1:ℂ) hOld hFirst
  have hBaseBound := neutralIV023BaseMass_le_expandedMass
    (neutralIV023BasePart f) (neutralIV023SecondPart f)
    (1:ℂ) hU hSecond
  have hOldLe : neutralNF600Mass (neutralIV023OldPart f) ≤
      neutralNF600Mass (neutralIV023BasePart f) := by
    simpa only [neutralIV023OldPart,one_smul,←hThreeSplit]
      using hOldBound
  have hBaseLe : neutralNF600Mass (neutralIV023BasePart f) ≤
      neutralNF600Mass f := by
    simpa only [one_smul,←hFullSplit] using hBaseBound
  exact le_trans hOldLe hBaseLe

/-- The original HISTORICAL NF600 n=9 source bound is now
transferred to EVERY arbitrary complex Schwartz source supported
in ALL FOUR actual cells, without a fresh prime-side assumption
or arbitrary numerical matrix. The old prime DOES NOT vanish. -/
theorem neutralIV023EveryFourCell_originalPrime_real_bound
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ neutralIV022FourCellSupport → f x=0) :
    |(neutralIV011OriginalMixedPrime
        (11/10:ℝ) f f).re| ≤
      (2/5:ℝ)*neutralNF600Mass f := by
  have hp := neutralIV023EveryFourCell_originalPrime_eq_old f hf
  have hOld :
      neutralNF735InOriginalCollars (neutralIV023OldPart f) :=
    (neutralIV023EveryFourCellSchwartz_decomposes f hf).1
  have hbound := neutralNF600Prime_bound_actual
    (neutralIV023OldPart f) hOld
  have hmass := neutralIV023OldMass_le_fourCellMass f hf
  rw [hp]
  have hconvert :
      neutralIV011OriginalMixedPrime (11/10:ℝ)
        (neutralIV023OldPart f) (neutralIV023OldPart f) =
      neutralNF600Prime (neutralIV023OldPart f) := rfl
  rw [hconvert]
  linarith only [hbound,hmass]

/-- TERMINAL IV023 SOURCE THEOREM TARGET: the ORIGINAL signed
arithmetic Zeta23 Weil form is genuinely 1/16-coercive for
EVERY complex Schwartz test supported in the actual FOUR-cell
region. This directly combines IV023's verified-source-candidate
complete real n9 prime dictionary and IV022's signed full
Gamma + TWO poles + 17/2000 mass budget.

No explicit prime-bound, mixed Schur, finite basis, new diagonal
sign or spectral-equivalence hypothesis occurs in the target.
It remains a PROOF CANDIDATE until real source Lean and full
dependency strict standard-axiom audits PASS. It is NOT global
Weil positivity or RH; only one special bounded support domain.
-/
theorem neutralIV023WholeFourCellOriginalWeil_oneSixteenth
    (f : 𝓢(ℝ,ℂ))
    (hf : ∀ x : ℝ,
      x ∉ neutralIV022FourCellSupport → f x=0) :
    (1/16:ℝ)*neutralNF600Mass f ≤
      (neutralIV010Diagonal (11/10:ℝ) f).re := by
  exact neutralIV022FourCell_oneSixteenth_of_originalPrime
    f hf (neutralIV023EveryFourCell_originalPrime_real_bound f hf)

#print axioms neutralIV021EveryThreeCell_originalPrime_eq_old
#print axioms neutralIV020WideOldMass_le_expandedMass
#print axioms neutralIV022SecondFrozenTwoCollarActiveGap
#print axioms neutralIV022FirstSecondActiveGap
#print axioms neutralIV022SecondSelfActiveGap
#print axioms neutralIV022FourCell_oneSixteenth_of_originalPrime
#print axioms neutralIV023BaseSecond_supportedFourCell
#print axioms neutralIV023BaseSecond_mass_add
#print axioms neutralIV023BaseMass_le_expandedMass
#print axioms neutralIV023BaseSecondCorrelation_eq_base_of_threeZeros
#print axioms neutralIV023ActiveSeparated_add
#print axioms neutralIV023ThreeCellSecond_activeSeparated
#print axioms neutralIV023ThreeCellSecond_activeCorrelation_eq
#print axioms neutralIV023ThreeCellSecond_originalPrime_eq
#print axioms neutralIV023EveryFourCell_originalPrime_eq_old
#print axioms neutralIV023OldMass_le_fourCellMass
#print axioms neutralIV023EveryFourCell_originalPrime_real_bound
#print axioms neutralIV023WholeFourCellOriginalWeil_oneSixteenth

end
end WeilDefect
