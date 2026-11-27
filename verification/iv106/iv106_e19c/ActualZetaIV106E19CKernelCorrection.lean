import WeilDefect.Arithmetic.ActualZetaIV106C3ActualConstraints

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap

abbrev neutralIV106E19CH := NeutralLogHilbertCarrier (11/10:ℝ)

/-- Literal terminal response observation, with exactly the C3 row convention. -/
def neutralIV106E19CResponse (k : ℕ) (hk : 0 < k) :
    neutralIV106E19CH →L[ℂ] (Fin k → ℂ) :=
  ContinuousLinearMap.pi fun i =>
    neutralIV106C3PhysicalRow (11/10:ℝ) (neutralIV105CResponse k hk i)

/-- Embed response coordinates into the original constraint codomain,
leaving the cell, pole-difference and mass rows at zero. -/
def neutralIV106E19CResponseOnly (k : ℕ) (z : Fin k → ℂ) :
    neutralIV106C3Index 665 k → ℂ :=
  fun j => match j with
    | .inl _ => 0
    | .inr (.inl _) => 0
    | .inr (.inr (.inl _)) => 0
    | .inr (.inr (.inr i)) => z i

theorem neutralIV106E19CResponse_extract (k : ℕ) (hk : 0 < k)
    (p : neutralIV106E19CH) (i : Fin k) :
    neutralIV106C3Constraints 665 k hk p (Sum.inr (Sum.inr (Sum.inr i))) =
      neutralIV106E19CResponse k hk p i := rfl

/-- A right inverse of the response on the base-null subspace provides
an exact terminal kernel correction. The right inverse must preserve
ALL base constraints, not just the two source moments. -/
theorem neutralIV106E19CCorrect (k : ℕ) (hk : 0 < k)
    (J : (Fin k → ℂ) →L[ℂ] neutralIV106E19CH)
    (hJ : ∀ z, neutralIV106C3Constraints 665 k hk (J z) =
      neutralIV106E19CResponseOnly k z)
    (p : neutralIV106E19CH)
    (hp : neutralIV106C3Constraints 665 k hk p =
      neutralIV106E19CResponseOnly k (neutralIV106E19CResponse k hk p)) :
    neutralIV106C3Constraints 665 k hk
      (p - J (neutralIV106E19CResponse k hk p)) = 0 := by
  rw [map_sub,hp,hJ,sub_self]

/-- A square, invertible response pivot cannot itself contain a nonzero
terminal kernel direction. This prevents confusing a response bank
with an admissible kernel-trial bank. -/
theorem neutralIV106E19CPivot_obstruction (k : ℕ) (hk : 0 < k)
    (J : (Fin k → ℂ) →L[ℂ] neutralIV106E19CH)
    (hJ : ∀ z, neutralIV106C3Constraints 665 k hk (J z) =
      neutralIV106E19CResponseOnly k z)
    (z : Fin k → ℂ)
    (hz : neutralIV106C3Constraints 665 k hk (J z) = 0) :
    z = 0 := by
  rw [hJ] at hz
  funext i
  exact congrFun hz (Sum.inr (Sum.inr (Sum.inr i)))

/-- Any surplus base-null vector outside the pivot's range yields a
nonzero terminal kernel direction. No numerical rank threshold. -/
theorem neutralIV106E19CSurplus (k : ℕ) (hk : 0 < k)
    (J : (Fin k → ℂ) →L[ℂ] neutralIV106E19CH)
    (hJ : ∀ z, neutralIV106C3Constraints 665 k hk (J z) =
      neutralIV106E19CResponseOnly k z)
    (p : neutralIV106E19CH)
    (hp : neutralIV106C3Constraints 665 k hk p =
      neutralIV106E19CResponseOnly k (neutralIV106E19CResponse k hk p))
    (houtside : ∀ z, p ≠ J z) :
    ∃ t : neutralIV106E19CH, t ≠ 0 ∧ neutralIV106C3Constraints 665 k hk t = 0 := by
  exact ⟨p-J (neutralIV106E19CResponse k hk p),
    sub_ne_zero.mpr (houtside _),neutralIV106E19CCorrect k hk J hJ p hp⟩

#print axioms neutralIV106E19CResponse_extract
#print axioms neutralIV106E19CCorrect
#print axioms neutralIV106E19CPivot_obstruction
#print axioms neutralIV106E19CSurplus
end
end WeilDefect
