module

public import Zeta.EulerMaclaurin.ErrorBound
public import Mathlib.RingTheory.Polynomial.Pochhammer
public import Mathlib.NumberTheory.Bernoulli
public import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
CP021 LEAF KERNEL RECOVERY: genuine original Zeta-v1-1e6 and original
mathlib4@v4.35.0 ONLY. No imports from CP011 or CP013–CP020,
no circular new source candidate theorem, no Cauchy or RH dependency.

Original full complex Borwein all-circle bound M=6 N=256, r=1/4,
t∈[149.5,150.05353], z∈sphere(1/2+it,1/4):
  zetaRemainderBound z 6 256 < 3/10^13
by original published source formula and Mathlib exact Bernoulli,
Pochhammer, cpow arithmetic.

Ten SOURCE-CANDIDATE theorems. A genuine compiler receipt for this
single lean_lib would certify the leaf even when CP013–CP020's
heavy other source compilation is queued/blocked.
Uncompiled source alone is NOT original Lean KERNEL PASS.
-/

@[expose] public section

open Metric Finset Set

namespace CP021BorweinLeaf

/-- Original ascending Pochhammer polynomial is a finite product,
bounded on a COMPLEX disk by exactly the 13 scalar factors. The
bound works at arbitrary order and will be specialized to n=13. -/
theorem norm_ascPochhammer_eval_le_product
    (z : ℂ) (h : ‖z‖ ≤ (151 : ℝ)) (n : ℕ) :
    ‖(ascPochhammer ℂ n).eval z‖ ≤
      ∏ j ∈ Finset.range n, ((151 : ℝ) + j) := by
  induction n with
  | zero =>
      simp [ascPochhammer_zero]
  | succ n ih =>
      rw [ascPochhammer_succ_eval, norm_mul, Finset.prod_range_succ]
      have hfactor : ‖z + (n : ℂ)‖ ≤ (151 : ℝ) + n := by
        calc
          ‖z + (n : ℂ)‖ ≤ ‖z‖ + ‖(n : ℂ)‖ :=
            norm_add_le _ _
          _ = ‖z‖ + (n : ℝ) := by simp
          _ ≤ 151 + n := by linarith
      exact mul_le_mul ih hfactor (norm_nonneg _) (by positivity)

/-- The genuine source `Mathlib.NumberTheory.Bernoulli.bernoulli`
is rational, with B_14 = 7/6. This theorem is deliberately a
concrete original Lean kernel obligation, not an external numeric
hypothesis or a new axiom. -/
theorem original_bernoulli_fourteen :
    bernoulli 14 = (7 : ℚ) / 6 := by
  norm_num [bernoulli, bernoulli', Fin.sum_univ_eq_sum_range,
    Finset.sum_range_succ]

/-- For the source original M=6 Euler–Maclaurin error, its complex
coefficient is the EXACT real rational 7/(6*14!). -/
theorem source_B14_coefficient_norm :
    ‖(((bernoulli 14 : ℝ) / ((14 : ℕ).factorial : ℝ)) : ℂ)‖
      = (7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ)) := by
  rw [original_bernoulli_fourteen]
  norm_num [Complex.norm_real, Real.norm_eq_abs, Nat.factorial]

/-- All thirteen scalar Pochhammer majorants stay strictly positive. -/
theorem majorant_product_nonneg :
    (0 : ℝ) ≤ ∏ j ∈ Finset.range 13, ((151 : ℝ) + j) := by
  positivity

private abbrev a : ℝ := (149500 : ℝ) / 1000
private abbrev b : ℝ := (15005353 : ℝ) / 100000
private noncomputable def center (t : ℝ) : ℂ :=
  1 / 2 + Complex.I * (t : ℂ)
private abbrev rad : ℝ := 1 / 4
private abbrev cap : ℝ := (3 : ℝ) / (10 : ℝ) ^ 13

/-- Every single point of every complex Cauchy circle uniformly
in the entire compact original source height interval has the
required complex norm and real part bounds. -/
theorem source_circle_geometry (t : ℝ) (ht : t ∈ Icc a b)
    (z : ℂ) (hz : z ∈ sphere (center t) rad) :
    (1 : ℝ) / 4 ≤ z.re ∧ ‖z‖ ≤ 151 := by
  have hdist : ‖z - center t‖ = (1 : ℝ) / 4 := by
    simpa [rad] using (mem_sphere_iff_norm.mp hz)
  have hreal := Complex.abs_re_le_norm (z - center t)
  have hlow : -(1 : ℝ) / 4 ≤ (z - center t).re := by
    have := (abs_le.mp (hreal.trans_eq hdist)).1
    linarith
  have hcentre_re : (center t).re = (1 : ℝ) / 2 := by
    simp [center]
  have hcentre_norm : ‖center t‖ ≤ (1 : ℝ) / 2 + t := by
    calc
      ‖center t‖ =
        ‖(1 / 2 : ℂ) + Complex.I * (t : ℂ)‖ := rfl
      _ ≤ ‖(1 / 2 : ℂ)‖ + ‖Complex.I * (t : ℂ)‖ :=
        norm_add_le _ _
      _ = (1 : ℝ) / 2 + t := by
        simp [norm_mul, abs_of_nonneg ht.1]
  have hnorm : ‖z‖ ≤ (1 : ℝ) / 4 + ‖center t‖ := by
    have := norm_add_le (z - center t) (center t)
    rw [sub_add_cancel] at this
    rwa [hdist] at this
  constructor
  · have heq : z.re = (z - center t).re + (1 : ℝ) / 2 := by
      rw [Complex.sub_re, hcentre_re]
      ring
    linarith
  · have htb : t ≤ b := ht.2
    have hb : b = (15005353 : ℝ) / 100000 := rfl
    linarith

/-- The source Borwein K(z) prefactor ≤ 656/53 uniformly across all
complex circles, using no real-only or sign-changing estimates. -/
theorem original_Borwein_prefactor_le (z : ℂ)
    (hre : (1 : ℝ) / 4 ≤ z.re)
    (hnorm : ‖z‖ ≤ 151) :
    ‖z + (13 : ℂ)‖ / (z.re + 13) ≤ (656 : ℝ) / 53 := by
  have htop : ‖z + (13 : ℂ)‖ ≤ (164 : ℝ) := by
    calc
      ‖z + (13 : ℂ)‖ ≤ ‖z‖ + ‖(13 : ℂ)‖ := norm_add_le _ _
      _ = ‖z‖ + 13 := by simp
      _ ≤ 164 := by linarith
  have hpos : 0 < z.re + 13 := by linarith
  have hright : (164 : ℝ) ≤ (656 : ℝ) / 53 * (z.re + 13) := by
    nlinarith
  exact (div_le_iff₀ hpos).2 (htop.trans hright)

/-- The complex-power norm in the ORIGINAL published Borwein source
satisfies |256^(-z-13)|≤256^-13 whenever Re z≥1/4. -/
theorem original_complex_cpow_bound (z : ℂ)
    (hre : (1 : ℝ) / 4 ≤ z.re) :
    ‖(256 : ℂ) ^ (-z - (13 : ℂ))‖ ≤
      1 / (256 : ℝ) ^ 13 := by
  rw [Complex.norm_cpow_eq_rpow_re_of_pos (by norm_num :
    (0 : ℝ) < 256)]
  have hexp : (-z - (13 : ℂ)).re ≤ -(13 : ℝ) := by
    simp only [Complex.sub_re, Complex.neg_re, Complex.natCast_re]
    linarith
  calc
    (256 : ℝ) ^ (-z - (13 : ℂ)).re ≤
        (256 : ℝ) ^ (-(13 : ℝ)) :=
      Real.rpow_le_rpow_of_exponent_le (by norm_num) hexp
    _ = 1 / (256 : ℝ) ^ 13 := by
      norm_num [Real.rpow_neg (by norm_num : (0 : ℝ) ≤ 256),
        Real.rpow_natCast]

/-- True original Euler–Maclaurin leading remainder term bound:
the source coefficient is B14/14!, the polynomial is the
original ascPochhammer_13, and the complex power is the original
N^(-z-13), with N=256. -/
theorem original_Borwein_omitted_term_le (z : ℂ)
    (hre : (1 : ℝ) / 4 ≤ z.re)
    (hnorm : ‖z‖ ≤ 151) :
    ‖(((bernoulli 14 : ℝ) / ((14 : ℕ).factorial : ℝ)) : ℂ) *
      (ascPochhammer ℂ 13).eval z *
      (256 : ℂ) ^ (-z - (13 : ℂ))‖
      ≤ ((7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ))) *
          (∏ j ∈ Finset.range 13, ((151 : ℝ) + j)) /
          (256 : ℝ) ^ 13 := by
  have hcoef := CP021BorweinLeaf.source_B14_coefficient_norm
  have hpoly := CP021BorweinLeaf.norm_ascPochhammer_eval_le_product
    z hnorm 13
  have hpower := original_complex_cpow_bound z hre
  calc
    ‖(((bernoulli 14 : ℝ) / ((14 : ℕ).factorial : ℝ)) : ℂ) *
      (ascPochhammer ℂ 13).eval z *
      (256 : ℂ) ^ (-z - (13 : ℂ))‖
        =
        ((7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ))) *
          ‖(ascPochhammer ℂ 13).eval z‖ *
          ‖(256 : ℂ) ^ (-z - (13 : ℂ))‖ := by
      rw [norm_mul, norm_mul, hcoef]
    _ ≤ ((7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ))) *
          (∏ j ∈ Finset.range 13, ((151 : ℝ) + j)) *
          (1 / (256 : ℝ) ^ 13) := by
      gcongr <;> assumption
    _ = ((7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ))) *
          (∏ j ∈ Finset.range 13, ((151 : ℝ) + j)) /
          (256 : ℝ) ^ 13 := by ring

/-- Exact real rational final comparison, including ALL original
13 scalar Pochhammer factors. NO new numerical axiom. -/
theorem exact_original_Borwein_real_envelope :
    ((656 : ℝ) / 53) *
      (((7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ))) *
        (∏ j ∈ Finset.range 13, ((151 : ℝ) + j)) /
        (256 : ℝ) ^ 13) < cap := by
  norm_num [cap, Finset.prod_range_succ, Nat.factorial]

/-- MAIN CP020 CLAIM: the actual original source Borwein error-bound
FUNCTION is uniformly ≤3×10^-13 on every genuine moving COMPLEX
circle in the entire [149.5,150.05353] window. This was the
formerly OPEN hBorweinOnCircle premise of CP019. -/
theorem original_Borwein_all_circles
    (t : ℝ) (ht : t ∈ Icc a b)
    (z : ℂ) (hz : z ∈ sphere (center t) rad) :
    zetaRemainderBound z 6 256 ≤ cap := by
  obtain ⟨hre, hnorm⟩ := source_circle_geometry t ht z hz
  have hK := original_Borwein_prefactor_le z hre hnorm
  have hterm := original_Borwein_omitted_term_le z hre hnorm
  have hK0 : 0 ≤ ‖z + (13 : ℂ)‖ / (z.re + 13) := by
    positivity
  have hMajor : 0 ≤
      ((7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ))) *
        (∏ j ∈ Finset.range 13, ((151 : ℝ) + j)) /
        (256 : ℝ) ^ 13 := by positivity
  have hOriginal :
      zetaRemainderBound z 6 256 =
        (‖z + (13 : ℂ)‖ / (z.re + 13)) *
        ‖(((bernoulli 14 : ℝ) /
          ((14 : ℕ).factorial : ℝ)) : ℂ) *
          (ascPochhammer ℂ 13).eval z *
          (256 : ℂ) ^ (-z - (13 : ℂ))‖ := by
    rfl
  rw [hOriginal]
  calc
    _ ≤ ((656 : ℝ) / 53) *
        (((7 : ℝ) / (6 * ((14 : ℕ).factorial : ℝ))) *
          (∏ j ∈ Finset.range 13, ((151 : ℝ) + j)) /
          (256 : ℝ) ^ 13) := by
      exact mul_le_mul hK hterm (norm_nonneg _) hMajor
    _ ≤ cap := (exact_original_Borwein_real_envelope).le

end CP021BorweinLeaf

#print axioms CP021BorweinLeaf.norm_ascPochhammer_eval_le_product
#print axioms CP021BorweinLeaf.original_bernoulli_fourteen
#print axioms CP021BorweinLeaf.source_B14_coefficient_norm
#print axioms CP021BorweinLeaf.majorant_product_nonneg
#print axioms CP021BorweinLeaf.source_circle_geometry
#print axioms CP021BorweinLeaf.original_Borwein_prefactor_le
#print axioms CP021BorweinLeaf.original_complex_cpow_bound
#print axioms CP021BorweinLeaf.original_Borwein_omitted_term_le
#print axioms CP021BorweinLeaf.exact_original_Borwein_real_envelope
#print axioms CP021BorweinLeaf.original_Borwein_all_circles
