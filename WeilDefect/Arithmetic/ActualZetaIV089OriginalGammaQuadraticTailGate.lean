import WeilDefect.Arithmetic.ActualZetaIV087OriginalMixedPhysicalLimitGate
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open Filter
open scoped Topology

/-!
IV089: explicit quadratic-frequency remainder for the literal
original Gamma multiplier. The envelope is r²/(N+1)².
This is a pointwise bound, not an integrated error theorem:
the latter requires a genuine second absolute Fourier moment.
-/

def neutralIV089TailEnvelope (N : ℕ) (r : ℝ) : ℝ :=
  r ^ 2 / ((N : ℝ) + 1) ^ 2

/-- The actual NF599 gain has a telescoping quadratic tail majorant. -/
theorem neutralIV089Gain_le_envelope_drop (n : ℕ) (r : ℝ) :
    neutralNF599Gain ((n : ℝ) + 1 + 1/4) r ≤
      neutralIV089TailEnvelope n r - neutralIV089TailEnvelope (n+1) r := by
  let x : ℝ := (n : ℝ) + 1
  have hx : 1 ≤ x := by dsimp [x]; positivity
  have hx0 : 0 < x := by linarith
  have hx1 : 0 < x + 1 := by linarith
  have hd : x^3 ≤ (x+1/4)*( (x+1/4)^2 + (r/2)^2) := by
    have h1 := mul_nonneg (show 0 ≤ x by linarith) (sq_nonneg r)
    have h2 := sq_nonneg r
    have h3 := sq_nonneg x
    nlinarith only [h1,h2,h3,hx]
  have hp : (x+1)^2 ≤ 4*x*(2*x+1) := by
    nlinarith only [sq_nonneg x,hx]
  have hfirst : neutralNF599Gain (x+1/4) r ≤ r^2/(4*x^3) := by
    unfold neutralNF599Gain
    apply (div_le_div_iff₀ (by positivity) (by positivity)).mpr
    have h := mul_nonneg (sq_nonneg r) (sub_nonneg.mpr hd)
    nlinarith only [h]
  have hsecond : r^2/(4*x^3) ≤ r^2*(2*x+1)/(x^2*(x+1)^2) := by
    apply (div_le_div_iff₀ (by positivity) (by positivity)).mpr
    have h := mul_nonneg (mul_nonneg (sq_nonneg r) (sq_nonneg x))
      (sub_nonneg.mpr hp)
    nlinarith only [h]
  have he : r^2*(2*x+1)/(x^2*(x+1)^2) =
      r^2/x^2-r^2/(x+1)^2 := by
    field_simp [ne_of_gt hx0, ne_of_gt hx1] <;> ring
  have h := hfirst.trans (hsecond.trans_eq he)
  simpa only [neutralIV089TailEnvelope, Nat.cast_add, Nat.cast_one, x] using h

/-- Adding one literal gain consumes at most the envelope drop. -/
theorem neutralIV089GammaFinite_add_envelope_step (N : ℕ) (r : ℝ) :
    neutralIV071GammaFinite (N+1) r + neutralIV089TailEnvelope (N+1) r ≤
      neutralIV071GammaFinite N r + neutralIV089TailEnvelope N r := by
  rw [neutralIV071GammaFinite_succ]
  linarith [neutralIV089Gain_le_envelope_drop N r]

/-- Finite telescope valid for every number of additional modes. -/
theorem neutralIV089GammaFinite_add_envelope_tail (N k : ℕ) (r : ℝ) :
    neutralIV071GammaFinite (N+k) r + neutralIV089TailEnvelope (N+k) r ≤
      neutralIV071GammaFinite N r + neutralIV089TailEnvelope N r := by
  induction k with
  | zero => simp
  | succ k ih =>
    exact (neutralIV089GammaFinite_add_envelope_step (N+k) r).trans ih

/-- Quantitative pointwise remainder of the original infinite Gamma
symbol, with no altered normalization or substitute multiplier. -/
theorem neutralIV089GammaRemainder_bound (N : ℕ) (r : ℝ) :
    0 ≤ Zeta23.EF.gammaBracket r - neutralIV071GammaFinite N r ∧
    Zeta23.EF.gammaBracket r - neutralIV071GammaFinite N r ≤
      neutralIV089TailEnvelope N r := by
  constructor
  · exact sub_nonneg.mpr (neutralIV071GammaFinite_le N r)
  · have hlim : Zeta23.EF.gammaBracket r ≤
        neutralIV071GammaFinite N r + neutralIV089TailEnvelope N r := by
      apply le_of_tendsto (neutralIV071GammaFinite_tendsto r)
      filter_upwards [eventually_ge_atTop N] with m hm
      obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hm
      have ht := neutralIV089GammaFinite_add_envelope_tail N k r
      have hn : 0 ≤ neutralIV089TailEnvelope (N+k) r := by
        unfold neutralIV089TailEnvelope
        positivity
      linarith
    linarith

#print axioms neutralIV089Gain_le_envelope_drop
#print axioms neutralIV089GammaFinite_add_envelope_step
#print axioms neutralIV089GammaFinite_add_envelope_tail
#print axioms neutralIV089GammaRemainder_bound

end
end WeilDefect
