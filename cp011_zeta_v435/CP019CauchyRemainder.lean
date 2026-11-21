module

public import Zeta.EulerMaclaurin.ErrorBound
public import Zeta.EulerMaclaurin.Continuation
public import Mathlib.Analysis.Complex.Liouville

/-!
CP019: ORIGINAL published Euler–Maclaurin complex remainder + the
GENUINE original Mathlib v4.35 Cauchy estimates, NOT an invalid
differentiation of a real-axis FUNCTION VALUE error bound.

Use M=6,N=256, radius 1/4, centers s_t=1/2+i t with
t in [149.5,150.05353]. For ANY point on ANY of these circles:
  Re z >= 1/4, norm z < 151.
The original Borwein Euler–Maclaurin bound therefore has a uniform
RATIONAL majorant strictly less than C = 3/10^13, if the original
Bernoulli/Pochhammer finite majorant is discharged in Lean.

Cauchy: ‖iteratedDeriv k (zetaRemainder · 6 256) s_t‖
  <= k! C / (1/4)^k.
At k=1,2,3 the corresponding valid upper targets are
  12/10^13, 96/10^13, 1152/10^13.

The source already establishes HOLOMORPHY of the Euler–Maclaurin
improper remainder on the proper complex half-plane; deriving the
exact DiffContOnCl structure on this moving disk from that original
holomorphy remains an EXPLICIT formal premise below. So does the
source Borwein bound envelope on its circle. They must be discharged
before calling the final derivative remainder certificate unconditional.

This converts an ORIGINAL COMPLEX VALUE error into derivative error
VALIDLY via Cauchy, rather than differentiating the original
HardyZ real function-value inequality.

All new Lean source only, original 4.35 kernel and standard axioms
receipts pending; no RH/global Weil positivity claim.
-/

@[expose] public section

open Metric

namespace CP019CauchyRemainder

private noncomputable def sourceCenter (t : ℝ) : ℂ :=
  1 / 2 + Complex.I * (t : ℂ)

private abbrev radius : ℝ := 1 / 4
private abbrev C : ℝ := (3 : ℝ) / (10 : ℝ) ^ 13

/-- Each complex Cauchy circle around the original half-line stays
strictly in Re>0, hence inside original Euler-Maclaurin continuation
domain Re> -13 (with the pole at 1 excluded, since Im t≈150). -/
theorem sphere_re_quarter_le {t : ℝ} {z : ℂ}
    (hz : z ∈ sphere (sourceCenter t) radius) :
    (1 : ℝ) / 4 ≤ z.re := by
  have hd : ‖z - sourceCenter t‖ = radius :=
    mem_sphere_iff_norm.mp hz
  have hreal := Complex.abs_re_le_norm (z - sourceCenter t)
  have hlow := (abs_le.mp (hreal.trans_eq hd)).1
  have hc : (sourceCenter t).re = (1 : ℝ) / 2 := by
    simp [sourceCenter]
  have heq : z.re = (z - sourceCenter t).re + (1 : ℝ) / 2 := by
    rw [Complex.sub_re, hc]
    ring
  rw [heq]
  dsimp [radius] at hlow
  linarith

/-- The original value-error theorem applies at ALL complex points on
the centered Cauchy circle: it is truly a complex Euler-Maclaurin
remainder theorem, unlike the published HardyZ real value theorem. -/
theorem original_source_zeta_remainder_bound_on_circle
    {t : ℝ} {z : ℂ}
    (hz : z ∈ sphere (sourceCenter t) radius) :
    ‖zetaRemainder z 6 256‖ ≤ zetaRemainderBound z 6 256 := by
  have hre := sphere_re_quarter_le hz
  exact norm_zetaRemainder_le z 6 256 (by norm_num) (by
    norm_num
    linarith)

/-- The concrete PURELY RATIONAL Borwein majorant calculation.
Proof-source target uses only factorials, a 13-factor product and
rational arithmetic. It is NOT the missing complex-circle
Pochhammer inequality itself (that separate source bridge is
exposed below). -/
theorem exact_rational_Borwein_majorant :
    ((656 : ℚ) / 53) *
      ((7 : ℚ) / (6 * ((Nat.factorial 14 : ℕ) : ℚ))) *
      ((∏ j ∈ Finset.range 13, ((151 + j : ℕ) : ℚ)) /
        (256 : ℚ) ^ 13)
      =
        (181596617021805363 : ℚ) /
          633825300114114700748351602688 := by
  norm_num [Finset.prod_range_succ]

/-- The exact source Borwein rational envelope is STRICTLY below
3×10^-13; this is exact arithmetic, not numerical sampling. -/
theorem exact_Borwein_majorant_lt_three_1e13 :
    ((181596617021805363 : ℚ) /
      633825300114114700748351602688) <
        3 / (10 : ℚ) ^ 13 := by
  norm_num

/-- The real Cauchy transfer for k=0..3 and indeed EVERY k.
The missing hholomorphic/hBorweinOnCircle are explicit:
 * original source holomorphic remainder must be formally attached
   as DiffContOnCl on each genuine complex closed disk,
 * original source finite Borwein envelope must be formally proven
   on every complex circle from its original norm_zetaRemainder_le.

When both are available, this gives a GENUINE derivative error
certificate for the ORIGINAL published Euler–Maclaurin remainder. -/
theorem original_zeta_EM_remainder_cauchy_budget (t : ℝ) (k : ℕ)
    (hholomorphic :
      DiffContOnCl ℂ (fun z : ℂ => zetaRemainder z 6 256)
        (ball (sourceCenter t) radius))
    (hBorweinOnCircle :
      ∀ z ∈ sphere (sourceCenter t) radius,
        zetaRemainderBound z 6 256 ≤ C) :
    ‖iteratedDeriv k (fun z : ℂ => zetaRemainder z 6 256)
        (sourceCenter t)‖ ≤
      (k.factorial : ℝ) * C / radius ^ k := by
  exact Complex.norm_iteratedDeriv_le_of_forall_mem_sphere_norm_le
    k (by norm_num [radius]) hholomorphic
    (fun z hz =>
      (original_source_zeta_remainder_bound_on_circle hz).trans
        (hBorweinOnCircle z hz))

/-- Explicit order-three original Euler-Maclaurin derivative error
bound: ≤1152/10^13, CONDITIONAL on the actual original-circle
holomorphy and uniform Borwein interval enclosure. -/
theorem third_derivative_original_zeta_EM_remainder_budget (t : ℝ)
    (hholomorphic :
      DiffContOnCl ℂ (fun z : ℂ => zetaRemainder z 6 256)
        (ball (sourceCenter t) radius))
    (hBorweinOnCircle :
      ∀ z ∈ sphere (sourceCenter t) radius,
        zetaRemainderBound z 6 256 ≤ C) :
    ‖iteratedDeriv 3 (fun z : ℂ => zetaRemainder z 6 256)
        (sourceCenter t)‖ ≤ (1152 : ℝ) / (10 : ℝ) ^ 13 := by
  have h := original_zeta_EM_remainder_cauchy_budget t 3
    hholomorphic hBorweinOnCircle
  convert h using 1 <;> norm_num [radius, C, Nat.factorial]

end CP019CauchyRemainder

#print axioms CP019CauchyRemainder.sphere_re_quarter_le
#print axioms CP019CauchyRemainder.original_source_zeta_remainder_bound_on_circle
#print axioms CP019CauchyRemainder.exact_rational_Borwein_majorant
#print axioms CP019CauchyRemainder.exact_Borwein_majorant_lt_three_1e13
#print axioms CP019CauchyRemainder.original_zeta_EM_remainder_cauchy_budget
#print axioms CP019CauchyRemainder.third_derivative_original_zeta_EM_remainder_budget
