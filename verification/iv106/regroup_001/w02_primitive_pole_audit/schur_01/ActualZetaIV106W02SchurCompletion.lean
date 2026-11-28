import WeilDefect.Arithmetic.ActualZetaIV106W02ConstrainedResponse

namespace WeilDefect
noncomputable section
open InnerProductSpace ContinuousLinearMap
open scoped InnerProductSpace ComplexConjugate

section Completion
variable {H E : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]
  [NormedAddCommGroup E] [InnerProductSpace ℂ E]

/-- Completion on an embedded complementary sector. The solve and both
pairing equations are explicit; no invariance of the embedded sector is used. -/
theorem neutralIV106W02S_generic (A : H →L[ℂ] H) (C : E →L[ℂ] E)
    (J : E →L[ℂ] H) (v : H) (b r q : E)
    (hs : ∀ x y, inner ℂ (A x) y = inner ℂ x (A y))
    (hC : ∀ x y, inner ℂ x (C y) = inner ℂ (J x) (A (J y)))
    (hB : ∀ x, inner ℂ x b = inner ℂ (J x) (A v))
    (hr : C r = b) :
    (inner ℂ (v + J q) (A (v + J q))).re =
      (inner ℂ v (A v)).re - (inner ℂ b r).re +
        (inner ℂ (q+r) (C (q+r))).re := by
  have hswap (x y : H) :
      inner ℂ x (A y) = conj (inner ℂ y (A x)) := by
    rw [← inner_conj_symm (𝕜 := ℂ) x (A y), hs y x]
  have hcrossH : inner ℂ v (A (J q)) = conj (inner ℂ q b) := by
    rw [hswap v (J q), hB q]
  have hcrossE : inner ℂ r (C q) = conj (inner ℂ q b) := by
    rw [hC r q, hswap (J r) (J q), ← hC q r, hr]
  have hdiag : (inner ℂ r b).re = (inner ℂ b r).re := by
    rw [← inner_conj_symm (𝕜 := ℂ) b r, Complex.conj_re]
  simp only [map_add, inner_add_left, inner_add_right, Complex.add_re]
  rw [hcrossH, hcrossE, ← hB q, ← hC q q, hr, hdiag]
  simp only [Complex.conj_re]
  ring

end Completion

/-- Exact diagonal of the actual logarithmic Weil form operator. -/
def neutralIV106W02SQ (v : neutralIV106W02IH) : ℝ :=
  (inner ℂ v (neutralIV106W02RA v)).re

/-- Exact complementary correction; this is not yet a finite matrix. -/
def neutralIV106W02SS (v : neutralIV106W02IH) : ℝ :=
  neutralIV106W02SQ v -
    (inner ℂ (neutralIV106W02RB v) (neutralIV106W02RResponse v)).re

theorem neutralIV106W02S_canonical (v : neutralIV106W02IH) :
    neutralIV106W02SQ v =
      neutralActualZetaCanonicalNativeQuadratic (11/10:ℝ)
        (neutralLogHilbertToCanonical v) := by
  unfold neutralIV106W02SQ
  rw [neutralActualZetaLogWeilFormOperator_diagonal, Complex.ofReal_re]

set_option maxHeartbeats 2000000 in
theorem neutralIV106W02S_complete (v : neutralIV106W02IH) (q : neutralIV106W02IK) :
    neutralIV106W02SQ (v + (q : neutralIV106W02IH)) =
      neutralIV106W02SS v +
      (inner ℂ (q + neutralIV106W02RResponse v)
        (neutralIV106W02IC (q + neutralIV106W02RResponse v))).re := by
  unfold neutralIV106W02SS neutralIV106W02SQ
  exact neutralIV106W02S_generic (H := neutralIV106W02IH) (E := neutralIV106W02IK)
    neutralIV106W02RA neutralIV106W02IC neutralIV106W02IK.subtypeL
    v (neutralIV106W02RB v) (neutralIV106W02RResponse v) q
    neutralIV106W02R_symm neutralIV106W02I_pair
    (fun x => neutralIV106W02R_pair x v) (neutralIV106W02R_solve v)

set_option maxHeartbeats 2000000 in
theorem neutralIV106W02S_lower (v : neutralIV106W02IH) (q : neutralIV106W02IK) :
    neutralIV106W02SS v + (1/17:ℝ)*‖q + neutralIV106W02RResponse v‖^2 ≤
      neutralIV106W02SQ (v + (q : neutralIV106W02IH)) := by
  rw [neutralIV106W02S_complete v q]
  exact add_le_add_left (neutralIV106W02I_coercive (q + neutralIV106W02RResponse v)) _

set_option maxHeartbeats 2000000 in
theorem neutralIV106W02S_attained (v : neutralIV106W02IH) :
    neutralIV106W02SQ
      (v + ((-neutralIV106W02RResponse v : neutralIV106W02IK) : neutralIV106W02IH)) =
      neutralIV106W02SS v := by
  rw [neutralIV106W02S_complete v (-neutralIV106W02RResponse v)]
  simp only [neg_add_cancel, inner_zero_left, Complex.zero_re, add_zero]

#print axioms neutralIV106W02S_generic
#print axioms neutralIV106W02S_canonical
#print axioms neutralIV106W02S_complete
#print axioms neutralIV106W02S_lower
#print axioms neutralIV106W02S_attained
end
end WeilDefect
