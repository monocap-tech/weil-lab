import Mathlib.Tactic

namespace WeilDefect

/-! NF739: sharp COMPLEX Hermitian two-block Gram condition, expressed
over the six real and imaginary coordinates so there are no hidden
normalization conventions, positivity or zeta hypotheses. A future true
Weil use requires a literal signed EF Hermitian pairing and a proved
bound on its actual off-diagonal mixed term. -/

/-- Realification of a Hermitian 2×2 block with real diagonals a,b and
complex mixed coefficient p+iq; coefficient vectors are ur+i ui and
vr+i vi. The mixed term is 2 Re((p+iq)(ur+i ui)(vr-i vi)).
This definition imports NO Weil form or positivity hypothesis. -/
def neutralNF739HermitianTwoBlockEnergy
    (a b p q ur ui vr vi : ℝ) : ℝ :=
  a * (ur^2 + ui^2) +
    2 * (p * (ur*vr + ui*vi) + q * (ur*vi - ui*vr)) +
    b * (vr^2 + vi^2)

/-- Exact sufficient complex Hermitian 2×2 PSD criterion.
a≥0, b≥0 and p²+q²≤ab imply positivity for every complex
coefficient pair (ur+i ui,vr+i vi). This is pure finite algebra,
NOT a numerical mixed Weil bound. -/
theorem neutralNF739HermitianTwoBlockPSD
    (a b p q : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hdet : p^2 + q^2 ≤ a*b)
    (ur ui vr vi : ℝ) :
    0 ≤ neutralNF739HermitianTwoBlockEnergy a b p q ur ui vr vi := by
  by_cases hzero : a = 0
  · have hzdet : p^2 + q^2 ≤ 0 := by
      simpa [hzero] using hdet
    have hp : p = 0 := by
      nlinarith [sq_nonneg p, sq_nonneg q]
    have hq : q = 0 := by
      nlinarith [sq_nonneg p, sq_nonneg q]
    subst a
    subst p
    subst q
    simpa [neutralNF739HermitianTwoBlockEnergy] using
      (mul_nonneg hb (add_nonneg (sq_nonneg vr) (sq_nonneg vi)))
  · have hapos : 0 < a := lt_of_le_of_ne ha (Ne.symm hzero)
    have he :
        a * neutralNF739HermitianTwoBlockEnergy a b p q ur ui vr vi =
        (a*ur + p*vr + q*vi)^2 +
        (a*ui + p*vi - q*vr)^2 +
        (a*b - p^2 - q^2)*(vr^2+vi^2) := by
      unfold neutralNF739HermitianTwoBlockEnergy
      ring
    have hd : 0 ≤ a*b - p^2 - q^2 := by linarith
    have hsq : 0 ≤
        (a*ur + p*vr + q*vi)^2 +
        (a*ui + p*vi - q*vr)^2 +
        (a*b - p^2 - q^2)*(vr^2+vi^2) := by
      exact add_nonneg
        (add_nonneg (sq_nonneg _) (sq_nonneg _))
        (mul_nonneg hd
          (add_nonneg (sq_nonneg vr) (sq_nonneg vi)))
    have hmul :
        0 ≤ a * neutralNF739HermitianTwoBlockEnergy a b p q ur ui vr vi := by
      rw [he]
      exact hsq
    by_contra hn
    have hneg :
        neutralNF739HermitianTwoBlockEnergy a b p q ur ui vr vi < 0 :=
      lt_of_not_ge hn
    have hcontra :
        a * neutralNF739HermitianTwoBlockEnergy a b p q ur ui vr vi < 0 :=
      mul_neg_of_pos_of_neg hapos hneg
    linarith

/-- In the nondegenerate a>0 case the PSD certificate is an exact sum
of three nonnegative terms after multiplication by a. -/
theorem neutralNF739HermitianTwoBlockExactSquares
    (a b p q ur ui vr vi : ℝ) :
    a * neutralNF739HermitianTwoBlockEnergy a b p q ur ui vr vi =
      (a*ur + p*vr + q*vi)^2 +
      (a*ui + p*vi - q*vr)^2 +
      (a*b - p^2 - q^2)*(vr^2+vi^2) := by
  unfold neutralNF739HermitianTwoBlockEnergy
  ring

#print axioms neutralNF739HermitianTwoBlockPSD
#print axioms neutralNF739HermitianTwoBlockExactSquares

end WeilDefect
