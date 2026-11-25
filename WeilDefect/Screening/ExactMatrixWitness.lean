import Mathlib

/-! # Exact finite matrix witnesses

A certificate may supply rational entries, interpreted exactly in `ℝ`,
and an LDL factorization. Lean must verify the factorization equality and
the signs of its diagonal. The generator is outside the trusted base.
Zero diagonal values are permitted, so singular PSD witnesses are lawful.
-/

namespace WeilDefect.CanonicalCertificate

open Matrix

/-- Checked factorization implies PSD. No numerical eigensolver is used. -/
theorem positive_of_diagonal_factor
    {n k : Type*} [Fintype n] [Fintype k] [DecidableEq k]
    (M : Matrix n n ℝ) (L : Matrix k n ℝ) (d : k → ℝ)
    (hd : ∀ i, 0 ≤ d i)
    (hfactor : M = Lᴴ * Matrix.diagonal d * L) :
    M.PosSemidef := by
  rw [hfactor]
  exact (Matrix.PosSemidef.diagonal hd).conjTranspose_mul_mul_same L

/-- The checked witness yields the universal quadratic inequality needed
by certificate transport, including complex-independent real coefficients. -/
theorem quadratic_nonnegative_of_diagonal_factor
    {n k : Type*} [Fintype n] [Fintype k] [DecidableEq k]
    (M : Matrix n n ℝ) (L : Matrix k n ℝ) (d : k → ℝ)
    (hd : ∀ i, 0 ≤ d i)
    (hfactor : M = Lᴴ * Matrix.diagonal d * L)
    (x : n → ℝ) :
    0 ≤ star x ⬝ᵥ (M *ᵥ x) := by
  exact (positive_of_diagonal_factor M L d hd hfactor).dotProduct_mulVec_nonneg x

end WeilDefect.CanonicalCertificate
