import WeilDefect.Arithmetic.ActualZetaOriginalJ242OddParity
import Mathlib.Analysis.Analytic.Uniqueness
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap

/-!
NF551 — ORIGINAL SOURCE LOCAL-TO-GLOBAL IDENTITY THEOREM.

The prior NF550 exact Gram-positive criterion is local on the
single fixed open interval I ⊂ the ORIGINAL positive terminal
collar. Instead of separately proving local source independence,
use REAL ANALYTIC unique continuation of the actual entire
original NF407 generator formulas to show:

    source combinations vanish on I
           iff
    source combinations vanish on all ℝ.

Thus the exact single local Gram criterion is equivalent to
ordinary GLOBAL linear independence of the original J242
source family. The remaining difficult theorem is the
algebraic 136-characteristic-root exponential-polynomial
independence, not an additional collar-local analytic claim.

No source-specific independence axiom is introduced. The global
independence is an explicit premise of the terminal transfer.
-/

/-- The ACTUAL original NF407 real selected oscillator/pole
formula is real-analytic on ℝ: sin, cos, sinh and all source
monomials are real-analytic. -/
theorem neutralNF551OriginalRealGenerator_analytic
    (i : Fin 242) :
    AnalyticOnNhd ℝ (nf545OriginalSelectedRealGenerator i) Set.univ := by
  intro x hx
  unfold nf545OriginalSelectedRealGenerator
  split_ifs <;> dsimp <;> fun_prop

/-- Analyticity survives the faithful REAL-to-COMPLEX embedding
of the ACTUAL original selected J242 source generator. -/
theorem neutralNF551OriginalComplexGenerator_analytic
    (i : Fin 242) :
    AnalyticOnNhd ℝ (neutralNF546OriginalComplexGenerator i) Set.univ := by
  have h := (Complex.ofRealCLM.analyticOnNhd Set.univ).comp
    (neutralNF551OriginalRealGenerator_analytic i)
    (Set.mapsTo_univ _ _)
  simpa only [Function.comp_def, neutralNF546OriginalComplexGenerator] using h

/-- ALL finite complex combinations of the original 242 selected
source generator functions are real-analytic on the ENTIRE line,
including their genuine source sinh pole. -/
theorem neutralNF551OriginalSourceCombination_analytic
    (d : Fin 242 → ℂ) :
    AnalyticOnNhd ℝ (neutralNF550OriginalSourceCombination d) Set.univ := by
  unfold neutralNF550OriginalSourceCombination
  apply Finset.analyticOnNhd_fun_sum
  intro i hi
  have hs := neutralNF551OriginalComplexGenerator_analytic i
  simpa only [smul_eq_mul] using hs.const_smul (c := d i)

/-- The fixed canonical original source collar interval I
contains the ORIGINAL positive bump center c. -/
theorem neutralNF551OriginalCollarCenter_mem :
    neutralNF548CollarCenter ∈ Set.Ioo
      (neutralNF548CollarCenter - 1 / 2000)
      (neutralNF548CollarCenter + 1 / 2000) := by
  constructor <;> norm_num

/-- EXACT SOURCE LOCAL-TO-GLOBAL UNIQUE CONTINUATION:
If an unchanged original finite J242 combination vanishes on
the nonempty fixed collar interval (2197/2000,2199/2000),
then it VANISHES EVERYWHERE on the real physical line.
This is a genuine real-analytic identity theorem; no
nonzero-divisor source or Gram inverse is assumed. -/
theorem neutralNF551OriginalSourceCombination_eq_zero_of_collar_eq_zero
    (d : Fin 242 → ℂ)
    (hzero : ∀ x : ℝ,
      x ∈ Set.Ioo
        (neutralNF548CollarCenter - 1 / 2000)
        (neutralNF548CollarCenter + 1 / 2000) →
        neutralNF550OriginalSourceCombination d x = 0) :
    ∀ x : ℝ, neutralNF550OriginalSourceCombination d x = 0 := by
  have hnear :
      neutralNF550OriginalSourceCombination d =ᶠ[nhds neutralNF548CollarCenter]
        (fun _ : ℝ => (0 : ℂ)) := by
    filter_upwards
      [isOpen_Ioo.mem_nhds neutralNF551OriginalCollarCenter_mem] with x hx
    exact hzero x hx
  have hident :
      neutralNF550OriginalSourceCombination d =
        (fun _ : ℝ => (0 : ℂ)) :=
    AnalyticOnNhd.eq_of_eventuallyEq
      (neutralNF551OriginalSourceCombination_analytic d)
      (by fun_prop : AnalyticOnNhd ℝ (fun _ : ℝ => (0 : ℂ)) Set.univ)
      hnear
  exact fun x => congrFun hident x

/-- The exact STILL OPEN source theorem, formulated globally as
linear independence of the original 242 NF407 real-odd
exponential-polynomial generator formulas, not of a shadow Gram.
This is an explicit Prop, NOT a new axiom or assumed theorem. -/
def NeutralNF551OriginalJ242GlobalIndependence : Prop :=
  ∀ d : Fin 242 → ℂ,
    (∀ x : ℝ, neutralNF550OriginalSourceCombination d x = 0) →
      d = 0

/-- Global source independence from the 136-root
exponential-polynomial argument IMPLIES the NF550 original
positive-collar source-separation condition. The identity
theorem handles the entire local-to-global step in Lean. -/
theorem neutralNF551OriginalJ242GlobalIndependence_implies_collar
    (hglobal : NeutralNF551OriginalJ242GlobalIndependence) :
    NeutralNF550OriginalCollarSeparatesJ242 := by
  intro d hd
  by_contra hnone
  have hzero : ∀ x : ℝ,
      x ∈ Set.Ioo
        (neutralNF548CollarCenter - 1 / 2000)
        (neutralNF548CollarCenter + 1 / 2000) →
      neutralNF550OriginalSourceCombination d x = 0 := by
    intro x hx
    by_contra hn
    exact hnone ⟨x, hx, hn⟩
  exact hd (hglobal d
    (neutralNF551OriginalSourceCombination_eq_zero_of_collar_eq_zero d hzero))

/-- Global source independence and the NF550 local canonical
Gram-separation condition are in fact EQUIVALENT. The original
real-analytic unique continuation supplies the nontrivial
reverse-local implication; the direct implication is immediate. -/
theorem neutralNF551OriginalJ242GlobalIndependence_iff_collar :
    NeutralNF551OriginalJ242GlobalIndependence ↔
      NeutralNF550OriginalCollarSeparatesJ242 := by
  constructor
  · exact neutralNF551OriginalJ242GlobalIndependence_implies_collar
  · intro hcollar d hzero
    by_contra hn
    obtain ⟨x, hx, hnonzero⟩ := hcollar d hn
    exact hnonzero (hzero x)

/-- A future proof of the ORIGINAL global 136-characteristic-root
source independence now gives the fixed original canonical Gram
strict positivity and its authentic Schwartz correction, without
reproving analytic uniqueness on the thin original terminal
collar separately. -/
theorem neutralNF551OriginalGlobalIndependence_implies_Gram_pos
    (hglobal : NeutralNF551OriginalJ242GlobalIndependence) :
    ∀ d : Fin 242 → ℂ, d ≠ 0 →
      0 < (∑ i : Fin 242,
        conj (d i) * (neutralNF548CanonicalOriginalWeightedGram d) i).re := by
  exact neutralNF550CanonicalOriginalGram_pos_of_collar_separation
    (neutralNF551OriginalJ242GlobalIndependence_implies_collar hglobal)

end
end WeilDefect
