import WeilDefect.Arithmetic.ActualZetaPairSourceAttachment
import Mathlib.Analysis.Analytic.Order

namespace WeilDefect

noncomputable section

open scoped ENat Topology
open Filter

theorem neutralActualZetaZeroPoint_ne_one (ρ : NeutralActualZetaZeroPoint) :
    ρ.val ≠ 1 := by
  intro h
  have hre := congrArg Complex.re h
  simp only [Complex.one_re] at hre
  linarith [ρ.property.2.2]

theorem neutralActualZetaZeroPoint_analytic (ρ : NeutralActualZetaZeroPoint) :
    AnalyticAt ℂ riemannZeta ρ.val :=
  analyticOn_riemannZeta ρ.val (by simpa using neutralActualZetaZeroPoint_ne_one ρ)

/-- Finite analytic order follows from actual zeta analyticity and nonvanishing
at 2 on the connected punctured plane; it is not a packet hypothesis. -/
theorem neutralActualZetaOrder_ne_top (ρ : NeutralActualZetaZeroPoint) :
    analyticOrderAt riemannZeta ρ.val ≠ ⊤ := by
  have htwo : analyticOrderAt riemannZeta (2 : ℂ) ≠ ⊤ := by
    rw [analyticOrderAt_eq_zero.mpr
      (.inr (riemannZeta_ne_zero_of_one_le_re (by norm_num)))]
    exact ENat.zero_ne_top
  exact analyticOrderAt_ne_top_of_isPreconnected
    analyticOn_riemannZeta
    (isConnected_compl_singleton_of_one_lt_rank (by simp) (1 : ℂ)).isPreconnected
    (by norm_num : (2 : ℂ) ∈ ({1}ᶜ : Set ℂ))
    (by simpa using neutralActualZetaZeroPoint_ne_one ρ) htwo

/-- Actual multiplicity, read from the finite analytic order of zeta. -/
def neutralActualZetaMultiplicity (ρ : NeutralActualZetaZeroPoint) : ℕ :=
  analyticOrderNatAt riemannZeta ρ.val

theorem neutralActualZetaMultiplicity_order (ρ : NeutralActualZetaZeroPoint) :
    (neutralActualZetaMultiplicity ρ : ℕ∞) = analyticOrderAt riemannZeta ρ.val :=
  Nat.cast_analyticOrderNatAt (neutralActualZetaOrder_ne_top ρ)

theorem neutralActualZetaMultiplicity_pos (ρ : NeutralActualZetaZeroPoint) :
    0 < neutralActualZetaMultiplicity ρ := by
  apply Nat.pos_of_ne_zero
  intro h
  have horder := neutralActualZetaMultiplicity_order ρ
  rw [h, Nat.cast_zero] at horder
  exact (analyticOrderAt_ne_zero.mpr
    ⟨neutralActualZetaZeroPoint_analytic ρ, ρ.property.1⟩) horder.symm

/-- Actual local factorization at the actual multiplicity. -/
theorem neutralActualZetaMultiplicity_factor (ρ : NeutralActualZetaZeroPoint) :
    ∃ g : ℂ → ℂ, AnalyticAt ℂ g ρ.val ∧ g ρ.val ≠ 0 ∧
      riemannZeta =ᶠ[𝓝 ρ.val]
        fun z => (z - ρ.val) ^ neutralActualZetaMultiplicity ρ * g z := by
  simpa only [neutralActualZetaMultiplicity, smul_eq_mul] using
    (neutralActualZetaZeroPoint_analytic ρ).analyticOrderAt_ne_top.mp
      (neutralActualZetaOrder_ne_top ρ)

/-- Actual divisor copies, without a chosen shell enumeration or simplicity. -/
abbrev NeutralActualZetaDivisorCoordinate :=
  Σ ρ : NeutralActualZetaZeroPoint, Fin (neutralActualZetaMultiplicity ρ)

def neutralActualZetaDivisorOrdinate (q : NeutralActualZetaDivisorCoordinate) : ℂ :=
  neutralActualZetaOrdinate q.1

theorem neutralActualZetaDivisorOrdinate_zeta (q : NeutralActualZetaDivisorCoordinate) :
    riemannZeta ((1 / 2 : ℂ) + Complex.I * neutralActualZetaDivisorOrdinate q) = 0 :=
  neutralActualZetaOrdinate_zeta q.1

theorem neutralActualZetaMultiplicity_copies (ρ : NeutralActualZetaZeroPoint) :
    Nonempty (Fin (neutralActualZetaMultiplicity ρ)) :=
  ⟨⟨0, neutralActualZetaMultiplicity_pos ρ⟩⟩

theorem neutralActualZetaMultiplicity_card (ρ : NeutralActualZetaZeroPoint) :
    Fintype.card (Fin (neutralActualZetaMultiplicity ρ)) =
      neutralActualZetaMultiplicity ρ :=
  Fintype.card_fin _

end

end WeilDefect
