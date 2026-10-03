import WeilDefect.Arithmetic.ActualZetaWeightedSampling
import Mathlib.Data.Fintype.Sigma
import Mathlib.Data.Set.Countable

namespace WeilDefect

noncomputable section

open scoped BigOperators ComplexConjugate

/-- Actual open-strip zero points with bounded absolute imaginary height. -/
def neutralActualZetaPointHeightWindow (T : ℝ) : Set NeutralActualZetaZeroPoint :=
  {ρ | |ρ.val.im| ≤ T}

/-- Retain every actual analytic-multiplicity copy in the same height window. -/
def neutralActualZetaDivisorHeightWindow (T : ℝ) :
    Set NeutralActualZetaDivisorCoordinate :=
  {q | q.1 ∈ neutralActualZetaPointHeightWindow T}

/-- The actual open-strip coordinate bounds put every height window in a
compact ball; actual zeta discreteness, not a shell-count premise, gives finiteness. -/
theorem neutralActualZetaPointHeightWindow_finite (T : ℝ) :
    (neutralActualZetaPointHeightWindow T).Finite := by
  have hK := (isCompact_closedBall (0 : ℂ) (|T| + 2)).inter_riemannZetaZeros_finite
  have hf : ((fun ρ : NeutralActualZetaZeroPoint => ρ.val) ⁻¹'
      (Metric.closedBall (0 : ℂ) (|T| + 2) ∩ riemannZetaZeros)).Finite :=
    Set.Finite.preimage Subtype.val_injective.injOn hK
  apply hf.subset
  intro ρ hρ
  change |ρ.val.im| ≤ T at hρ
  refine ⟨?_, ρ.property.1⟩
  have hn := Complex.norm_le_abs_re_add_abs_im ρ.val
  rw [abs_of_pos ρ.property.2.1] at hn
  have hi : |ρ.val.im| ≤ |T| := hρ.trans (le_abs_self T)
  have hb : ‖ρ.val‖ ≤ |T| + 2 := by linarith [ρ.property.2.2]
  simpa only [Metric.mem_closedBall, dist_zero_right] using hb

instance neutralActualZetaPointHeightWindow_fintype (T : ℝ) :
    Fintype (neutralActualZetaPointHeightWindow T) :=
  (neutralActualZetaPointHeightWindow_finite T).fintype

/-- A bounded divisor truncation is exactly the dependent sum of the actual
multiplicity fibers over its actual bounded point set. -/
def neutralActualZetaHeightCopiesEquiv (T : ℝ) :
    (Σ ρ : neutralActualZetaPointHeightWindow T,
      Fin (neutralActualZetaMultiplicity ρ.val)) ≃
        neutralActualZetaDivisorHeightWindow T where
  toFun q := ⟨⟨q.1.val, q.2⟩, q.1.property⟩
  invFun q := ⟨⟨q.val.1, q.property⟩, q.val.2⟩
  left_inv := by rintro ⟨⟨ρ, hρ⟩, i⟩; rfl
  right_inv := by rintro ⟨⟨ρ, i⟩, hρ⟩; rfl

instance neutralActualZetaDivisorHeightWindow_fintype (T : ℝ) :
    Fintype (neutralActualZetaDivisorHeightWindow T) :=
  Fintype.ofEquiv _ (neutralActualZetaHeightCopiesEquiv T)

theorem neutralActualZetaDivisorHeightWindow_finite (T : ℝ) :
    (neutralActualZetaDivisorHeightWindow T).Finite :=
  Set.toFinite _

/-- Exact multiplicity count, without asserting any rate of growth in T. -/
theorem neutralActualZetaDivisorHeightWindow_card (T : ℝ) :
    Fintype.card (neutralActualZetaDivisorHeightWindow T) =
      ∑ ρ : neutralActualZetaPointHeightWindow T, neutralActualZetaMultiplicity ρ.val := by
  rw [← Fintype.card_congr (neutralActualZetaHeightCopiesEquiv T), Fintype.card_sigma]
  simp only [Fintype.card_fin]

theorem neutralActualZetaPointHeightWindow_cover :
    (⋃ n : ℕ, neutralActualZetaPointHeightWindow (n : ℝ)) = Set.univ := by
  apply Set.eq_univ_of_forall
  intro ρ
  obtain ⟨n, hn⟩ := exists_nat_ge |ρ.val.im|
  exact Set.mem_iUnion.mpr ⟨n, hn⟩

instance neutralActualZetaZeroPoint_countable : Countable NeutralActualZetaZeroPoint := by
  apply Set.countable_univ_iff.mp
  rw [← neutralActualZetaPointHeightWindow_cover]
  exact Set.countable_iUnion fun n =>
    (neutralActualZetaPointHeightWindow_finite (n : ℝ)).countable

instance neutralActualZetaDivisorCoordinate_countable :
    Countable NeutralActualZetaDivisorCoordinate := by
  infer_instance

theorem neutralActualZetaDivisorHeightWindow_ordinate (T : ℝ)
    (q : NeutralActualZetaDivisorCoordinate) :
    q ∈ neutralActualZetaDivisorHeightWindow T ↔
      |(neutralActualZetaDivisorOrdinate q).re| ≤ T := by
  simp only [neutralActualZetaDivisorHeightWindow, neutralActualZetaPointHeightWindow,
    Set.mem_setOf_eq, neutralActualZetaDivisorOrdinate, neutralActualZetaOrdinate_re]

theorem neutralActualZetaDivisorHeightWindow_pair (T : ℝ)
    (q : NeutralActualZetaDivisorCoordinate) :
    neutralActualZetaDivisorPair q ∈ neutralActualZetaDivisorHeightWindow T ↔
      q ∈ neutralActualZetaDivisorHeightWindow T := by
  rw [neutralActualZetaDivisorHeightWindow_ordinate,
    neutralActualZetaDivisorOrdinate_pair, Complex.conj_re,
    ← neutralActualZetaDivisorHeightWindow_ordinate]

theorem neutralActualZetaDivisorHeightWindow_mono {T U : ℝ} (hTU : T ≤ U) :
    neutralActualZetaDivisorHeightWindow T ⊆ neutralActualZetaDivisorHeightWindow U :=
  fun _ hq => hq.trans hTU

end

end WeilDefect
