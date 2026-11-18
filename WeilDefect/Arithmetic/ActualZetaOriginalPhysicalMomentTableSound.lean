import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMomentTable

namespace WeilDefect
noncomputable section

def NF617MomentRow.value (q : NF617MomentRow) : ℂ :=
  ((q.re:ℝ):ℂ)+((q.im:ℝ):ℂ)*Complex.I

theorem NF617MomentRow.rect_sound (q : NF617MomentRow) (Q : ℕ) (hQ : 0<Q) :
    (q.rect Q).Contains q.value := by
  constructor
  · simpa [NF617MomentRow.rect,NF617MomentRow.value,Complex.add_re,Complex.mul_re]
      using NF591Ball.contains_exactQ q.re Q hQ
  · simpa [NF617MomentRow.rect,NF617MomentRow.value,Complex.add_im,Complex.mul_im]
      using NF591Ball.contains_exactQ q.im Q hQ

/-- Row-by-row soundness uses only the cached actual endpoints, a
positive rational denominator bound and the prior certified row.
Array bounds are supplied independently of default-valued reads. -/
theorem neutralNF618MomentRows_sound (p : NF591Ball) (hp : p.Contains Real.pi)
    (k : NF616Frequency) (hh : |k.h|≤1) (hd : 0<k.lower)
    (Q N : ℕ) (hQ : 0<Q) (hN : 1≤N)
    (hfee : 2/(N.factorial:ℝ) ≤ 1/(Q:ℝ))
    (rows : Array NF617MomentRow)
    (hc : ∀ n < rows.size,
      neutralNF617MomentRowCheck (neutralNF617Cache p k Q N) k.lower Q rows n = true)
    (n : ℕ) (hn : n<rows.size) :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) k.value n-
      (neutralNF617MomentRead rows n).value‖ ≤ (neutralNF617MomentRead rows n).rad := by
  have hd' : (0:ℝ)<(k.lower:ℝ) := by exact_mod_cast hd
  have hz := k.lower_sound
  induction n with
  | zero =>
    let q := neutralNF617MomentRead rows 0
    have h0 := hc 0 hn
    simp only [neutralNF617MomentRowCheck,Bool.and_eq_true] at h0
    have hcheck := h0.2
    rw [neutralNF617Cache_boundary_eq] at hcheck
    change neutralNF615RectBelow
      (neutralNF615BaseResidualRect (neutralNF615BoundaryRect p k.h k.f Q N 0)
        (neutralNF615LambdaRect p k.h k.f Q) (q.rect Q) Q)
      (k.lower*q.rad) = true at hcheck
    exact neutralNF615Moment_zero_of_rect p hp k.h k.f hh (q.rect Q) q.value
      (q.rect_sound Q hQ) Q N hQ hN hfee (k.lower:ℝ) (q.rad:ℝ)
      (k.lower*q.rad) hd' hz hcheck (by push_cast; rfl)
  | succ n ih =>
    let q := neutralNF617MomentRead rows (n+1)
    let prev := neutralNF617MomentRead rows n
    have h0 := hc (n+1) hn
    simp only [neutralNF617MomentRowCheck,Bool.and_eq_true] at h0
    have hcheck := h0.2
    rw [neutralNF617Cache_boundary_eq] at hcheck
    let S : ℚ := k.lower*q.rad-(n+1:ℚ)*prev.rad
    change neutralNF615RectBelow
      (neutralNF615ResidualRect (neutralNF615BoundaryRect p k.h k.f Q N (n+1))
        (neutralNF615LambdaRect p k.h k.f Q) (prev.rect Q) (q.rect Q) Q n) S = true at hcheck
    exact neutralNF615Moment_succ_of_rect p hp k.h k.f hh (prev.rect Q) (q.rect Q)
      prev.value q.value (prev.rect_sound Q hQ) (q.rect_sound Q hQ)
      Q N n hQ hN hfee (k.lower:ℝ) (prev.rad:ℝ) (q.rad:ℝ) S hd' hz
      (ih (by omega)) hcheck (by dsimp [S]; push_cast; linarith)

end
end WeilDefect
