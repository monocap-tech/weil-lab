module

public import CP020Pochhammer
public import CP019CauchyRemainder
public import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
CP020: CLOSE the original source all-circle M=6,N=256
Borwein envelope hBorweinOnCircle, WITHOUT any assumed source
rounding, new axiom, sorry, or differentiating real-axis error bounds.

Exact source specification:
 a=149.5, b=150.05353; s_t=1/2+i t, radius=1/4;
 z∈sphere(s_t,1/4) =>
   Re z>=1/4 and ‖z‖<=151;
   |(z)_13| <= ∏_{j=0}^{12}(151+j);
   |256^(-z-13)| <= 1/256^13;
   K(z)=‖z+13‖/(Re z+13) <=656/53;
   Bernoulli B14=7/6.
Therefore the REAL original zetaRemainderBound z 6 256
 <= [656/53]*[7/(6*14!)]*∏(151+j)/256^13
 <3/10^13.

When this SOURCE LEAN CANDIDATE compiles, CP019's previous
hBorweinOnCircle premise is discharged for EVERY original target
t in the frozen interval, and Cauchy supplies true complex zeta
Euler–Maclaurin remainder derivative errors k=0,1,2,3.

NO original Z'(149.5)>=2.4, HardyZ curvature, refined zero53 sign,
source signed Weil↔spectral dictionary, global positivity, or RH.
-/

@[expose] public section

open Metric Finset Set

namespace CP020BorweinCircle

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
  have hcoef := CP020Pochhammer.source_B14_coefficient_norm
  have hpoly := CP020Pochhammer.norm_ascPochhammer_eval_le_product
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
      gcongr
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

/-- This actually eliminates CP019's last explicit original Borwein
circle hypothesis, delivering source-level Cauchy derivative errors
for every k and all original heights. A genuine Lean kernel run is
STILL REQUIRED to accept the new proof and all its dependencies. -/
theorem original_EM_Cauchy_all_heights (t : ℝ) (ht : t ∈ Icc a b)
    (k : ℕ) :
    ‖iteratedDeriv k (fun z : ℂ => zetaRemainder z 6 256)
      (center t)‖ ≤
      (k.factorial : ℝ) * cap / rad ^ k := by
  have h := CP019CauchyRemainder.original_zeta_EM_cauchy_of_Borwein_circle_only
    t k (by
      intro z hz
      exact original_Borwein_all_circles t ht z hz)
  simpa [center, cap, rad] using h

/-- Exact uniform order-three numerical error result for the true
original Euler–Maclaurin ζ remainder, source candidate:
1.152×10^-10 for every t∈[149.5,150.05353]. -/
theorem original_EM_third_derivative_all_heights
    (t : ℝ) (ht : t ∈ Icc a b) :
    ‖iteratedDeriv 3 (fun z : ℂ => zetaRemainder z 6 256)
      (center t)‖ ≤ (1152 : ℝ) / (10 : ℝ) ^ 13 := by
  have h := original_EM_Cauchy_all_heights t ht 3
  convert h using 1 <;> norm_num [cap, rad, Nat.factorial]

end CP020BorweinCircle

#print axioms CP020BorweinCircle.source_circle_geometry
#print axioms CP020BorweinCircle.original_Borwein_prefactor_le
#print axioms CP020BorweinCircle.original_complex_cpow_bound
#print axioms CP020BorweinCircle.original_Borwein_omitted_term_le
#print axioms CP020BorweinCircle.exact_original_Borwein_real_envelope
#print axioms CP020BorweinCircle.original_Borwein_all_circles
#print axioms CP020BorweinCircle.original_EM_Cauchy_all_heights
#print axioms CP020BorweinCircle.original_EM_third_derivative_all_heights
