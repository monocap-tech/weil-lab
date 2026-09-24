import Mathlib

namespace WeilDefect

/-- A raw conjugate-pair coefficient has two coordinates. -/
abbrev RawPair := Bool → ℂ

/-- Conjugation swaps the two raw coordinates. -/
def pairSwap (v : RawPair) : RawPair
  | false => v true
  | true => v false

/-- Unnormalized positive pair eigenchannel. -/
def pairPos : RawPair := fun _ => 1

/-- Unnormalized negative pair eigenchannel. -/
def pairNeg : RawPair
  | false => 1
  | true => -1

/-- WD-T20: the symmetric pair channel is fixed by conjugation. -/
theorem wd_t20_pair_pos_eigen : pairSwap pairPos = pairPos := by
  funext b
  cases b <;> simp [pairSwap, pairPos]

/-- WD-T20: the antisymmetric pair channel has conjugation eigenvalue -1. -/
theorem wd_t20_pair_neg_eigen : pairSwap pairNeg = -pairNeg := by
  funext b
  cases b <;> simp [pairSwap, pairNeg]


/--
WD-T20: the raw two-coordinate pair is linearly equivalent to its
positive/negative eigenchannel coordinates.
-/
noncomputable def pairEigenEquiv : (ℂ × ℂ) ≃ₗ[ℂ] RawPair where
  toFun p b := p.1 * pairPos b + p.2 * pairNeg b
  invFun v :=
    ((v false + v true) / 2, (v false - v true) / 2)
  left_inv p := by
    apply Prod.ext <;> simp [pairPos, pairNeg] <;> ring
  right_inv v := by
    funext b
    cases b <;> simp [pairPos, pairNeg] <;> ring
  map_add' x y := by
    funext b
    cases b <;> simp [pairPos, pairNeg] <;> ring
  map_smul' a x := by
    funext b
    cases b <;> simp [pairPos, pairNeg] <;> ring

/-- In eigenchannel coordinates, conjugation fixes the positive coordinate and negates the negative one. -/
theorem wd_t20_pair_diagonalization (a b : ℂ) :
    pairSwap (pairEigenEquiv (a, b)) = pairEigenEquiv (a, -b) := by
  funext q
  cases q <;> simp [pairSwap, pairEigenEquiv, pairPos, pairNeg] <;> ring

/-- The selected negative coordinate type for one simple functional-equation quartet. -/
abbrev SimpleQuartetNegative := Fin 2

/-- WD-T21: one simple quartet contains two negative conjugate-pair coordinates. -/
theorem wd_t21_simple_quartet_negative_count :
    Fintype.card SimpleQuartetNegative = 2 := by
  decide

/-- Raw residues contributed by finitely many negative pair coefficients. -/
def rawResiduesOfNegativePairs (xs : List ℂ) : List ℂ :=
  xs.flatMap fun α => [α, -α]

/-- WD-T26: every finite collection of negative pair channels has zero raw residue moment. -/
theorem wd_t26_zero_moment (xs : List ℂ) :
    (rawResiduesOfNegativePairs xs).sum = 0 := by
  induction xs with
  | nil =>
      simp [rawResiduesOfNegativePairs]
  | cons α xs ih =>
      change ([α, -α] ++ rawResiduesOfNegativePairs xs).sum = 0
      simp [ih]

end WeilDefect
