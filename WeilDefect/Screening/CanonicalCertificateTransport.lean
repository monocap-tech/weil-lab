import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# Canonical certificate transport

RC23's robust acceptance inequalities, evaluated on an arbitrary coefficient
vector, and the two-sector Schur estimate. The scalar variables stand for
quadratic evaluations, not matrix entries. Bounds on these evaluations must
hold for every coefficient vector before the conclusions are Loewner bounds.

This module checks the algebra only. Native source attachment, whole-space
error bounds, and the infinite complementary floor remain hypotheses.
-/

namespace WeilDefect.CanonicalCertificate

/-- A certified approximate metric floor survives its whole error budget. -/
theorem metric_floor_transport
    (M Mh n e μ : ℝ)
    (herr : |M - Mh| ≤ e * n)
    (hgate : μ * n ≤ Mh - e * n) :
    μ * n ≤ M := by
  have h := (abs_le.mp herr).1
  linarith

/-- RC23 head gate (4), for one arbitrary quadratic evaluation. -/
theorem head_floor_transport
    (M Mh A Ah n eM eA m : ℝ)
    (hm : 0 ≤ m)
    (hM : |M - Mh| ≤ eM * n)
    (hA : |A - Ah| ≤ eA * n)
    (hgate : (eA + m * eM) * n ≤ Ah - m * Mh) :
    m * M ≤ A := by
  have hMu := (abs_le.mp hM).2
  have hAl := (abs_le.mp hA).1
  have hpaid := mul_le_mul_of_nonneg_left hMu hm
  nlinarith

/-- RC23 source gate (5). The residual error is supplied as a whole
quadratic bound; it is not inferred from an unchecked inverse. -/
theorem source_residual_transport
    (M Mh E Eh n eM eE β : ℝ)
    (hM : |M - Mh| ≤ eM * n)
    (hE : |E - Eh| ≤ eE * n)
    (hgate : (eE + β ^ 2 * eM) * n ≤ β ^ 2 * Mh - Eh) :
    E ≤ β ^ 2 * M := by
  have hMl := (abs_le.mp hM).1
  have hEu := (abs_le.mp hE).2
  have hpaid := mul_le_mul_of_nonneg_left hMl (sq_nonneg β)
  nlinarith

/-- Simultaneous metric, head and complete source-residual acceptance.
Specialize to every coefficient vector to obtain the finite matrix gate. -/
theorem robust_gate
    (M Mh A Ah E Eh n eM eA eE μ m β : ℝ)
    (hm : 0 ≤ m)
    (hM : |M - Mh| ≤ eM * n)
    (hA : |A - Ah| ≤ eA * n)
    (hE : |E - Eh| ≤ eE * n)
    (hmetric : μ * n ≤ Mh - eM * n)
    (hhead : (eA + m * eM) * n ≤ Ah - m * Mh)
    (hsource : (eE + β ^ 2 * eM) * n ≤ β ^ 2 * Mh - Eh) :
    μ * n ≤ M ∧ m * M ≤ A ∧ E ≤ β ^ 2 * M := by
  exact ⟨metric_floor_transport M Mh n eM μ hM hmetric,
    head_floor_transport M Mh A Ah n eM eA m hm hM hA hhead,
    source_residual_transport M Mh E Eh n eM eE β hM hE hsource⟩

/-- Whole-space residual control transports through a supported inclusion.
Here `errorSq`, `residualSq`, and `mass` are squared-norm evaluations. -/
theorem canonical_residual_transport
    (errorSq residualSq mass ρ β : ℝ)
    (hρ : 0 ≤ ρ)
    (hattach : errorSq ≤ ρ * residualSq)
    (hphysical : residualSq ≤ β * mass) :
    errorSq ≤ (ρ * β) * mass := by
  calc
    errorSq ≤ ρ * residualSq := hattach
    _ ≤ ρ * (β * mass) := mul_le_mul_of_nonneg_left hphysical hρ
    _ = (ρ * β) * mass := (mul_assoc ρ β mass).symm

/-- RC36's exact conversion factor; no decimal computation is trusted. -/
theorem rc36_conversion :
    (252 / 257 : ℝ) * (771078401 / 100000000000) =
      48577939263 / 6425000000000 := by
  norm_num

/-- RC36's canonical budget, conditional on the physical enclosure and
the actual supported weak-source attachment, for arbitrary coefficients. -/
theorem rc36_canonical_budget
    (errorSq residualSq mass : ℝ)
    (hattach : errorSq ≤ (252 / 257 : ℝ) * residualSq)
    (hphysical : residualSq ≤ (771078401 / 100000000000 : ℝ) * mass) :
    errorSq ≤ (48577939263 / 6425000000000 : ℝ) * mass := by
  have h := canonical_residual_transport errorSq residualSq mass
    (252 / 257) (771078401 / 100000000000) (by norm_num) hattach hphysical
  rw [rc36_conversion] at h
  exact h

/-- Two-sector Schur transport with an explicit common reserve `δ`.
The complement need not be finite dimensional. Its full lower estimate
and the mixed leakage estimate enter through `hlower`. -/
theorem schur_reserve
    (q x y m d β δ : ℝ)
    (hm : δ < m)
    (hdet : β ^ 2 ≤ (m - δ) * (d - δ))
    (hlower : m * x ^ 2 - 2 * β * x * y + d * y ^ 2 ≤ q) :
    δ * (x ^ 2 + y ^ 2) ≤ q := by
  have hsq := sq_nonneg ((m - δ) * x - β * y)
  have hdetY := mul_le_mul_of_nonneg_right hdet (sq_nonneg y)
  have hmul := mul_le_mul_of_nonneg_left hlower (le_of_lt (sub_pos.mpr hm))
  nlinarith

/-- Exact RC22 head/tail/leakage budgets admit this positive common reserve.
This checks the numerical Schur algebra, not the native inequalities. -/
theorem rc22_schur_budget :
    (1 / 10000 : ℝ) < 1 / 4000 ∧
    (1 / 300 : ℝ) ^ 2 ≤
      (1 / 4000 - 1 / 10000) * (247 / 2500 - 1 / 10000) := by
  norm_num

theorem rc22_whole_floor
    (q x y : ℝ)
    (hlower : (1 / 4000 : ℝ) * x ^ 2 - 2 * (1 / 300) * x * y +
      (247 / 2500) * y ^ 2 ≤ q) :
    (1 / 10000 : ℝ) * (x ^ 2 + y ^ 2) ≤ q := by
  exact schur_reserve q x y (1 / 4000) (247 / 2500) (1 / 300) (1 / 10000)
    rc22_schur_budget.1 rc22_schur_budget.2 hlower

end WeilDefect.CanonicalCertificate
