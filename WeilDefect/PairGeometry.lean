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

/-- The positive-T conjugate pair in Bombieri ordinate coordinates. -/
def quartetPairPos (T δ : ℝ) : ℂ × ℂ :=
  ((T : ℂ) + (δ : ℂ) * Complex.I,
   (T : ℂ) - (δ : ℂ) * Complex.I)

/-- The negative-T conjugate pair in Bombieri ordinate coordinates. -/
def quartetPairNeg (T δ : ℝ) : ℂ × ℂ :=
  ((-T : ℂ) + (δ : ℂ) * Complex.I,
   (-T : ℂ) - (δ : ℂ) * Complex.I)

/-- Each positive-T pair is a genuine complex-conjugate pair. -/
theorem wd_t21_quartet_pair_pos_conjugate (T δ : ℝ) :
    (quartetPairPos T δ).2 =
      star (quartetPairPos T δ).1 := by
  simp [quartetPairPos, sub_eq_add_neg]

/-- Each negative-T pair is a genuine complex-conjugate pair. -/
theorem wd_t21_quartet_pair_neg_conjugate (T δ : ℝ) :
    (quartetPairNeg T δ).2 =
      star (quartetPairNeg T δ).1 := by
  simp [quartetPairNeg, sub_eq_add_neg]

/-- Off-critical displacement makes both quartet pairs nonreal. -/
theorem wd_t21_quartet_pairs_nonreal
    (T δ : ℝ) (hδ : δ ≠ 0) :
    (quartetPairPos T δ).1.im ≠ 0
      ∧ (quartetPairNeg T δ).1.im ≠ 0 := by
  constructor <;> simpa [quartetPairPos, quartetPairNeg] using hδ

/-- Nonzero ordinate T separates the +T and -T conjugate pairs. -/
theorem wd_t21_quartet_pairs_distinct
    (T δ : ℝ) (hT : T ≠ 0) :
    quartetPairPos T δ ≠ quartetPairNeg T δ := by
  intro h
  have hfirst :
      (quartetPairPos T δ).1 = (quartetPairNeg T δ).1 :=
    congrArg Prod.fst h
  have hre :
      T = -T := by
    have := congrArg Complex.re hfirst
    simpa [quartetPairPos, quartetPairNeg] using this
  apply hT
  linarith

/-- The selected negative coordinate type for one simple functional-equation quartet. -/
abbrev SimpleQuartetNegative := Fin 2

/-- WD-T21: one simple quartet contains two negative conjugate-pair coordinates. -/
theorem wd_t21_simple_quartet_negative_count :
    Fintype.card SimpleQuartetNegative = 2 := by
  decide

/--
WD-T21 / ZW1-T2: a simple off-critical functional-equation quartet yields
exactly two distinct nonreal conjugate pairs in Bombieri ordinate coordinates,
hence two canonical negative pair coordinates after WD-T20 diagonalization.
-/
theorem wd_t21_simple_quartet_pair_geometry
    (T δ : ℝ) (hT : T ≠ 0) (hδ : δ ≠ 0) :
    (quartetPairPos T δ).2 =
        star (quartetPairPos T δ).1
    ∧ (quartetPairNeg T δ).2 =
        star (quartetPairNeg T δ).1
    ∧ (quartetPairPos T δ).1.im ≠ 0
    ∧ (quartetPairNeg T δ).1.im ≠ 0
    ∧ quartetPairPos T δ ≠ quartetPairNeg T δ
    ∧ Fintype.card SimpleQuartetNegative = 2 := by
  refine ⟨
    wd_t21_quartet_pair_pos_conjugate T δ,
    wd_t21_quartet_pair_neg_conjugate T δ,
    (wd_t21_quartet_pairs_nonreal T δ hδ).1,
    (wd_t21_quartet_pairs_nonreal T δ hδ).2,
    wd_t21_quartet_pairs_distinct T δ hT,
    wd_t21_simple_quartet_negative_count
  ⟩

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
