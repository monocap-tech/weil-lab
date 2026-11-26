import WeilDefect.Arithmetic.ActualZetaNativeSymbolSign
import WeilDefect.Arithmetic.ActualZetaNativeLogBounds
import WeilDefect.External.Zeta23.Theorems.Thm_Zeta23_DigammaSeries_hasSum_digamma_series
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

/-- Real part of a reciprocal is dominated by the reciprocal real part. -/
theorem neutralIV106E2Inv_re (z : ℂ) (hz : 0 < z.re) :
    (1/z).re ≤ 1/z.re := by
  rw [one_div, Complex.inv_re, Complex.normSq_apply]
  have hd : 0 < z.re*z.re+z.im*z.im := by nlinarith [sq_pos_of_pos hz, sq_nonneg z.im]
  apply (div_le_div_iff₀ hd hz).mpr
  nlinarith [sq_nonneg z.im]

/-- Quarter-line digamma comparison from the original convergent series. -/
theorem neutralIV106E2Quarter (y : ℝ) :
    (Complex.digamma (1/4:ℂ)).re ≤
      (Complex.digamma (1/4 + Complex.I*(y:ℂ))).re := by
  let z : ℂ := 1/4 + Complex.I*(y:ℂ)
  let w : ℂ := 1/4
  have hz : z.re = 1/4 := by simp [z]
  have hw : w.re = 1/4 := by norm_num [w]
  have hzmem : z ∈ Complex.integerComplement := by
    rintro ⟨n,hn⟩
    have he := congrArg Complex.re hn
    simp only [Complex.intCast_re, hz] at he
    have hi : (1:ℤ) = 4*n := by exact_mod_cast (show (1:ℝ) = 4*(n:ℝ) by linarith)
    omega
  have hwmem : w ∈ Complex.integerComplement := by
    rintro ⟨n,hn⟩
    have he := congrArg Complex.re hn
    simp only [Complex.intCast_re, hw] at he
    have hi : (1:ℤ) = 4*n := by exact_mod_cast (show (1:ℝ) = 4*(n:ℝ) by linarith)
    omega
  have hs := Complex.hasSum_re (Zeta23.DigammaSeries.hasSum_digamma_series hzmem)
  have ht := Complex.hasSum_re (Zeta23.DigammaSeries.hasSum_digamma_series hwmem)
  have hc : ∀ n : ℕ,
      (1 / ((n:ℂ)+1) - 1/(w+n+1)).re ≤
      (1 / ((n:ℂ)+1) - 1/(z+n+1)).re := by
    intro n
    have hpos : 0 < (z+(n:ℂ)+1).re := by
      simp only [Complex.add_re, Complex.natCast_re, Complex.one_re, hz]
      positivity
    have h := neutralIV106E2Inv_re (z+(n:ℂ)+1) hpos
    have he : (1/(w+(n:ℂ)+1)).re = 1/(z+(n:ℂ)+1).re := by
      simp [w,z,one_div,Complex.inv_re,Complex.normSq_apply]
      <;> field_simp <;> ring
    simp only [Complex.sub_re]
    rw [he]
    linarith
  have hsum := Summable.tsum_le_tsum hc ht.summable hs.summable
  rw [ht.tsum_eq, hs.tsum_eq] at hsum
  have hi := neutralIV106E2Inv_re z (by rw [hz]; norm_num)
  have hwrec : (1/w).re = 4 := by norm_num [w]
  have hi' : (1/z).re ≤ 4 := by
    calc
      _ ≤ 1/z.re := hi
      _ = 4 := by rw [hz]; norm_num
  simp only [Complex.add_re, Complex.ofReal_re] at hsum
  rw [hwrec] at hsum
  change (Complex.digamma w).re ≤ (Complex.digamma z).re
  linarith only [hsum, hi']

/-- Sharp vertical Stirling estimate, with the explicit real reciprocal correction. -/
theorem neutralIV106E2High (ξ : ℝ) (hξ : ξ ≠ 0)
    (ht : 1/2 ≤ |Real.pi*ξ|) :
    Real.log |ξ| - 25/(8*Real.pi^2*ξ^2) ≤
      compactWindowArchimedeanSymbol (2*Real.pi*ξ) := by
  let z : ℂ := 1/4 + Complex.I*((Real.pi*ξ:ℝ):ℂ)
  have hre : z.re = 1/4 := by simp [z]
  have him : z.im = Real.pi*ξ := by simp [z]
  have hs := Zeta23.StirlingVert.digamma_stirling (w := z)
    (by rw [hre]; norm_num) (by rwa [him])
  have hd := (neg_le_abs (Complex.digamma z - Complex.log z + (1/2:ℂ)/z).re).trans
    ((Complex.abs_re_le_norm _).trans hs)
  simp only [Complex.add_re, Complex.sub_re, Complex.log_re] at hd
  have hn : Real.pi*|ξ| ≤ ‖z‖ := by
    have h := Complex.abs_im_le_norm z
    rwa [him,abs_mul,abs_of_pos Real.pi_pos] at h
  have hlog := Real.log_le_log (mul_pos Real.pi_pos (abs_pos.mpr hξ)) hn
  rw [Real.log_mul Real.pi_pos.ne' (abs_ne_zero.mpr hξ)] at hlog
  have hy : 0 < (Real.pi*ξ)^2 := sq_pos_of_ne_zero (mul_ne_zero Real.pi_pos.ne' hξ)
  have hrec : ((1/2:ℂ)/z).re ≤ 1/(8*(Real.pi*ξ)^2) := by
    rw [div_eq_mul_inv, Complex.mul_re, Complex.inv_re, Complex.inv_im,
      Complex.normSq_apply, hre, him]
    norm_num
    have hden : 0 < (1/16:ℝ)+(Real.pi*ξ)^2 := by positivity
    have haux : (1/8:ℝ)/(1/16+(Real.pi*ξ)^2) ≤ (1/8)/((Real.pi*ξ)^2) := by
      apply (div_le_div_iff₀ hden hy).mpr
      linarith
    calc
      _ = (1/8:ℝ)/(1/16+(Real.pi*ξ)^2) := by
        rw [pow_two]
        ring
      _ ≤ (1/8:ℝ)/((Real.pi*ξ)^2) := haux
      _ = _ := by ring
  rw [him] at hd
  have hsym : ((1:ℂ)/4)+Complex.I*(((2*Real.pi*ξ:ℝ):ℂ)/2) = z := by
    dsimp [z]; push_cast; ring
  unfold compactWindowArchimedeanSymbol
  rw [hsym]
  change _ ≤ (Complex.digamma z).re - Real.log Real.pi
  have he : 25/(8*Real.pi^2*ξ^2) =
      3/(Real.pi*ξ)^2 + 1/(8*(Real.pi*ξ)^2) := by
    field_simp [Real.pi_pos.ne',hξ]
    <;> ring
  rw [he]
  linarith

/-- Global lower comparison, combining high-frequency Stirling with the quarter anchor. -/
theorem neutralIV106E2Global (ξ : ℝ) (hξ : ξ ≠ 0) :
    Real.log |ξ| - 25/(8*Real.pi^2*ξ^2) ≤
      compactWindowArchimedeanSymbol (2*Real.pi*ξ) := by
  by_cases ht : 1/2 ≤ |Real.pi*ξ|
  · exact neutralIV106E2High ξ hξ ht
  have hsmall : |Real.pi*ξ| < 1/2 := lt_of_not_ge ht
  have hpi := Real.pi_gt_three
  have hpi4 := Real.pi_lt_four
  have hξsmall : |ξ| ≤ 1 := by
    rw [abs_mul,abs_of_pos Real.pi_pos] at hsmall
    nlinarith [abs_nonneg ξ]
  have hlog := Real.log_le_sub_one_of_pos (abs_pos.mpr hξ)
  have hs : (Real.pi*ξ)^2 < 1/4 := by nlinarith [sq_abs (Real.pi*ξ),abs_nonneg (Real.pi*ξ)]
  have hb : (25/2:ℝ) ≤ 25/(8*Real.pi^2*ξ^2) := by
    apply (le_div_iff₀ (by positivity)).mpr
    calc
      _ = 100*(Real.pi*ξ)^2 := by ring
      _ ≤ 25 := by linarith
  have ha := neutralIV106E2Quarter (Real.pi*ξ)
  rw [neutralActualZetaDigamma_quarter_re] at ha
  have h2 := Real.log_le_sub_one_of_pos (by norm_num : 0 < (2:ℝ))
  have hp := Real.log_le_sub_one_of_pos Real.pi_pos
  have hg := Real.eulerMascheroniConstant_lt_two_thirds
  have hsym : ((1:ℂ)/4)+Complex.I*(((2*Real.pi*ξ:ℝ):ℂ)/2) =
      1/4+Complex.I*((Real.pi*ξ:ℝ):ℂ) := by push_cast; ring
  unfold compactWindowArchimedeanSymbol
  rw [hsym]
  change _ ≤ (Complex.digamma (1/4+Complex.I*((Real.pi*ξ:ℝ):ℂ))).re - Real.log Real.pi
  linarith

#print axioms neutralIV106E2Inv_re
#print axioms neutralIV106E2Quarter
#print axioms neutralIV106E2High
#print axioms neutralIV106E2Global
end
end WeilDefect
