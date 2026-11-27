import WeilDefect.Arithmetic.ActualZetaIV106E18OLiteralMatrix
import WeilDefect.Arithmetic.ActualZetaIV106E18PDeterminantTransfer

namespace WeilDefect
noncomputable section

/-- The actual IV105C response matrix has the strict corrected determinant
sign on the first k consecutive eligible cells. No Schur margin asserted. -/
theorem neutralIV106E18QDet_pos (k : ℕ) (hk : 0 < k) (hk34 : k ≤ 34) :
    0 < neutralIV106E18POrient k * (neutralIV106E18OMatrix k hk).det := by
  apply neutralIV106E18PInfinite k (neutralIV106E18OW k hk)
    neutralIV106E18OX (neutralIV106E18OY k)
  · intro n
    by_cases hn : n = 0
    · rw [hn,neutralIV106E18OW_zero]
    · exact (neutralIV106E18OW_pos k hk n (Nat.pos_of_ne_zero hn)).le
  · exact neutralIV106E18OW_pos k hk
  · exact neutralIV106E18OX_strict
  · exact neutralIV106E18OY_strict k hk
  · exact neutralIV106E18OMatrix_series k hk hk34

theorem neutralIV106E18QDet_ne (k : ℕ) (hk : 0 < k) (hk34 : k ≤ 34) :
    (neutralIV106E18OMatrix k hk).det ≠ 0 := by
  intro hz
  have hp := neutralIV106E18QDet_pos k hk hk34
  rw [hz,mul_zero] at hp
  exact (lt_irrefl 0) hp

/-- Full row independence of the original physical response bank. -/
theorem neutralIV106E18QRows (k : ℕ) (hk : 0 < k) (hk34 : k ≤ 34) :
    LinearIndependent ℝ (fun i => neutralIV106E18OMatrix k hk i) :=
  Matrix.linearIndependent_rows_of_det_ne_zero (neutralIV106E18QDet_ne k hk hk34)

#print axioms neutralIV106E18QDet_pos
#print axioms neutralIV106E18QDet_ne
#print axioms neutralIV106E18QRows
end
end WeilDefect
