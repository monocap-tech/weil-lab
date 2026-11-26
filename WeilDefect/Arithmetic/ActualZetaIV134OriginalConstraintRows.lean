import WeilDefect.Arithmetic.ActualZetaIV133OriginalProjectedRow
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace
open scoped SchwartzMap ComplexConjugate BigOperators

/-- The exact cell interval from IV129, with no change of coordinates. -/
def neutralIV134Cell (a : ℝ) (N : ℕ) (j : Fin N) : Set ℝ :=
  Set.Ioc (neutralIV126Node (-a) (2*a/(N:ℝ)) j.val)
    (neutralIV126Node (-a) (2*a/(N:ℝ)) (j.val+1))

def neutralIV134CellIndicator (a : ℝ) (N : ℕ) (j : Fin N) : ℝ → ℂ :=
  (neutralIV134Cell a N j).indicator (fun _ => 1)

theorem neutralIV134Cell_memLp (a : ℝ) (N : ℕ) (j : Fin N) :
    MemLp (neutralIV134CellIndicator a N j) 2 volume := by
  have hm : MeasurableSet (neutralIV134Cell a N j) := measurableSet_Ioc
  have ha : AEStronglyMeasurable (neutralIV134CellIndicator a N j) volume :=
    aestronglyMeasurable_const.indicator hm
  apply (memLp_two_iff_integrable_sq_norm ha).mpr
  have hi : IntegrableOn (fun _ : ℝ => ‖(1:ℂ)‖^2)
      (neutralIV134Cell a N j) volume :=
    (continuous_const.intervalIntegrable _ _).1
  apply (hi.integrable_indicator hm).congr
  filter_upwards [] with x
  by_cases hx : x ∈ neutralIV134Cell a N j <;>
    simp [neutralIV134CellIndicator, hx]

def neutralIV134CellRow (a : ℝ) (N : ℕ) (j : Fin N) : RealComplexL2 :=
  (neutralIV134Cell_memLp a N j).toLp (neutralIV134CellIndicator a N j)

theorem neutralIV134CellRow_pair (a : ℝ) (N : ℕ) (j : Fin N)
    (v : 𝓢(ℝ,ℂ)) :
    inner ℂ (neutralIV134CellRow a N j) (v.toLp 2 volume) =
      neutralIV129CellMap a N v j := by
  rw [L2.inner_def]
  change (∫ x : ℝ, inner ℂ (neutralIV134CellRow a N j x)
    ((v.toLp 2 volume : RealComplexL2) x)) =
    ∫ x in neutralIV134Cell a N j, v x
  rw [← integral_indicator (show MeasurableSet (neutralIV134Cell a N j) from measurableSet_Ioc)]
  apply integral_congr_ae
  filter_upwards [(neutralIV134Cell_memLp a N j).coeFn_toLp,
    v.coeFn_toLp 2 volume] with x hx hv
  change inner ℂ ((neutralIV134Cell_memLp a N j).toLp
    (neutralIV134CellIndicator a N j) x) ((v.toLp 2 volume : RealComplexL2) x) = _
  rw [hx,hv]
  by_cases hmem : x ∈ neutralIV134Cell a N j <;>
    simp [neutralIV134CellIndicator, hmem, RCLike.inner_apply']

/-- A cell indicator annihilates every actual original tail vector. -/
theorem neutralIV134CellRow_annihilates (k : ℕ) (hk : 0 < k) (N : ℕ)
    (j : Fin N) (z : neutralIV131Tail k hk N) :
    inner ℂ (neutralIV134CellRow (11/10:ℝ) N j) (z.val.toLp 2 volume) = 0 := by
  have hz := z.property
  change z.val ∈ neutralIV129Complement k hk ∧
    z.val ∈ LinearMap.ker (neutralIV129CellMap (11/10:ℝ) N) at hz
  rw [neutralIV134CellRow_pair, LinearMap.mem_ker.mp hz.2]
  rfl

/-- The actual packed physical columns annihilate the same tail. -/
theorem neutralIV134Packed_annihilates (k : ℕ) (hk : 0 < k) (N : ℕ)
    (c : Fin k → ℂ) (z : neutralIV131Tail k hk N) :
    inner ℂ ((neutralIV100Packed k hk c).toLp 2 volume) (z.val.toLp 2 volume) = 0 := by
  have hz := z.property
  change z.val ∈ neutralIV129Complement k hk ∧
    z.val ∈ LinearMap.ker (neutralIV129CellMap (11/10:ℝ) N) at hz
  exact hz.1.2 c

/-- Actual finite physical synthesis of cell and packed annihilators. -/
def neutralIV134ConstraintSynthesis (k : ℕ) (hk : 0 < k) (N : ℕ)
    (c : Fin N → ℂ) (d : Fin k → ℂ) : RealComplexL2 :=
  (∑ j : Fin N, c j • neutralIV134CellRow (11/10:ℝ) N j) +
    (neutralIV100Packed k hk d).toLp 2 volume

theorem neutralIV134Synthesis_annihilates (k : ℕ) (hk : 0 < k) (N : ℕ)
    (c : Fin N → ℂ) (d : Fin k → ℂ) (z : neutralIV131Tail k hk N) :
    inner ℂ (neutralIV134ConstraintSynthesis k hk N c d) (z.val.toLp 2 volume) = 0 := by
  unfold neutralIV134ConstraintSynthesis
  rw [inner_add_left, sum_inner, neutralIV134Packed_annihilates k hk N d z, add_zero]
  apply Finset.sum_eq_zero
  intro j hj
  rw [inner_smul_left, neutralIV134CellRow_annihilates k hk N j z, mul_zero]

/-- An actual finite residual Gram, in the same physical L2 space. -/
def neutralIV134ResidualGram {n : ℕ} (r : Fin n → RealComplexL2) :
    Matrix (Fin n) (Fin n) ℂ :=
  fun i j => inner ℂ (r i) (r j)

theorem neutralIV134ResidualGram_energy {n : ℕ}
    (r : Fin n → RealComplexL2) (c : Fin n → ℂ) :
    (∑ i : Fin n, conj (c i) *
      (neutralIV134ResidualGram r).mulVec c i).re =
      ‖∑ i : Fin n, c i • r i‖^2 := by
  rw [← inner_self_eq_norm_sq_to_K (𝕜 := ℂ)]
  simp only [Complex.ofReal_re]
  congr 1
  rw [sum_inner]
  apply Finset.sum_congr rfl
  intro i hi
  rw [inner_smul_left, inner_sum]
  congr 1
  apply Finset.sum_congr rfl
  intro j hj
  rw [inner_smul_right]
  rfl

/-- The concrete annihilator payment for a trial in the literal cell-null tail. -/
theorem neutralIV134Trial_payment (k : ℕ) (hk : 0 < k) (N : ℕ)
    (h : 𝓢(ℝ,ℂ)) (y : neutralIV131Tail k hk N)
    (c : Fin N → ℂ) (d : Fin k → ℂ)
    (hh : ∀ x : ℝ, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → h x = 0)
    (eta : ℝ) (he : 0 < eta)
    (hc : ∀ z : neutralIV131Tail k hk N,
      eta*‖z.val.toLp 2 volume‖^2 ≤ neutralIV107SchurEnergy k hk z.val) :
    neutralIV131Penalty k hk (neutralIV131Tail k hk N) h ≤
      neutralIV131Loss k hk h y.val +
      ‖neutralIV133CorrectedRow k hk (h+y.val) -
        neutralIV134ConstraintSynthesis k hk N c d‖^2/eta :=
  neutralIV133Penalty_trial_projected_le k hk (neutralIV131Tail k hk N) h y
    (neutralIV134ConstraintSynthesis k hk N c d) hh
    (neutralIV132Tail_supported k hk N) eta he hc
    (neutralIV134Synthesis_annihilates k hk N c d)

#print axioms neutralIV134Cell_memLp
#print axioms neutralIV134CellRow_pair
#print axioms neutralIV134CellRow_annihilates
#print axioms neutralIV134Packed_annihilates
#print axioms neutralIV134Synthesis_annihilates
#print axioms neutralIV134ResidualGram_energy
#print axioms neutralIV134Trial_payment

end
end WeilDefect
