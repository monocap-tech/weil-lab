import WeilDefect.Arithmetic.ActualZetaNativeSymbolSign
import WeilDefect.External.Zeta23.Theorems.Thm_Zeta23_DigammaSeries_hasSum_digamma_series
import Mathlib.Analysis.Complex.ExponentialBounds

namespace WeilDefect
noncomputable section
open Finset

/-! NF599: actual NF527 gamma lower bounds. The imported genuine
digamma series, not an assumed monotonicity of a numerical symbol,
supplies the nonnegative gain. Keep the exceptional zeroth summand
explicit because the imported HasSum begins at n+1. -/

def neutralNF599Gain (a t : ℝ) : ℝ :=
  (t/2)^2/(a*(a^2+(t/2)^2))

theorem neutralNF599Gain_nonneg (a t : ℝ) (ha : 0 < a) :
    0 ≤ neutralNF599Gain a t := by
  unfold neutralNF599Gain
  positivity

theorem neutralNF599Gain_mono_sq (a t u : ℝ) (ha : 0 < a)
    (htu : t^2 ≤ u^2) : neutralNF599Gain a t ≤ neutralNF599Gain a u := by
  unfold neutralNF599Gain
  apply (div_le_div_iff₀ (by positivity) (by positivity)).mpr
  have h : 0 ≤ a^3*(u^2-t^2) := mul_nonneg (by positivity) (sub_nonneg.mpr htu)
  nlinarith only [h]

theorem neutralNF599Gain_inv (a t : ℝ) (ha : 0<a) :
    neutralNF599Gain a t =
      1/a - (1/((a:ℂ)+Complex.I*((t/2:ℝ):ℂ))).re := by
  simp only [one_div,Complex.inv_re,Complex.add_re,Complex.add_im,Complex.mul_re,Complex.mul_im,
    Complex.ofReal_re,Complex.ofReal_im,Complex.I_re,Complex.I_im,
    zero_mul,one_mul,mul_zero,sub_zero,zero_add,add_zero,Complex.normSq_apply]
  unfold neutralNF599Gain
  field_simp
  <;> ring

theorem neutralNF599Quarter_noninteger (t : ℝ) :
    ((1/4:ℂ)+Complex.I*((t/2:ℝ):ℂ)) ∈ Complex.integerComplement := by
  rintro ⟨k,hk⟩
  have hr := congrArg Complex.re hk
  simp at hr
  have h4 : (4*k:ℤ)=1 := by
    have h : (4:ℝ)*(k:ℝ)=1 := by linarith
    exact_mod_cast h
  omega

theorem neutralNF599GammaGainSeries (t : ℝ) :
    HasSum (fun n : ℕ => neutralNF599Gain ((n:ℝ)+1+1/4) t)
      (Zeta23.EF.gammaBracket t - Zeta23.EF.gammaBracket 0 -
        neutralNF599Gain (1/4) t) := by
  let z : ℂ := (1/4:ℂ)+Complex.I*((t/2:ℝ):ℂ)
  have hz : z ∈ Complex.integerComplement := neutralNF599Quarter_noninteger t
  have h0 : (1/4:ℂ) ∈ Complex.integerComplement := by
    simpa using neutralNF599Quarter_noninteger 0
  have h := Complex.reCLM.hasSum
    ((Zeta23.DigammaSeries.hasSum_digamma_series hz).sub
      (Zeta23.DigammaSeries.hasSum_digamma_series h0))
  have he (n : ℕ) :
      ((1/((n:ℂ)+1)-1/(z+n+1))-
        (1/((n:ℂ)+1)-1/((1/4:ℂ)+n+1))).re =
      neutralNF599Gain ((n:ℝ)+1+1/4) t := by
    rw [neutralNF599Gain_inv _ _ (by positivity)]
    have hq : (1/4:ℂ)+n+1 = (((n:ℝ)+1+1/4:ℝ):ℂ) := by push_cast; ring
    have hzq : z+n+1 = (((n:ℝ)+1+1/4:ℝ):ℂ)+Complex.I*((t/2:ℝ):ℂ) := by
      dsimp [z]
      push_cast
      ring
    rw [hq,hzq]
    simp only [Complex.sub_re,← Complex.ofReal_div,Complex.ofReal_one,Complex.ofReal_re,← Complex.ofReal_inv,one_div]
    ring
  have he' :
      (fun n : ℕ => Complex.reCLM
        ((1/((n:ℂ)+1)-1/(z+n+1))-
          (1/((n:ℂ)+1)-1/((1/4:ℂ)+n+1)))) =
      (fun n : ℕ => neutralNF599Gain ((n:ℝ)+1+1/4) t) := funext he
  rw [he'] at h
  convert h using 1
  unfold Zeta23.EF.gammaBracket
  rw [neutralNF599Gain_inv _ _ (by norm_num)]
  simp only [Complex.reCLM_apply,Complex.sub_re,Complex.add_re]
  have hz' : (1/4:ℂ)+Complex.I*(t:ℂ)/2=z := by
    dsimp [z]
    push_cast
    ring
  rw [hz']
  norm_num
  dsimp [z]
  push_cast
  congr 1 <;> ring

theorem neutralNF599GammaLower_partial (t : ℝ) (N : ℕ) :
    Zeta23.EF.gammaBracket 0 + neutralNF599Gain (1/4) t +
      ∑ n ∈ range N, neutralNF599Gain ((n:ℝ)+1+1/4) t ≤
        Zeta23.EF.gammaBracket t := by
  have h := neutralNF599GammaGainSeries t
  have hs := h.summable.sum_le_tsum (range N)
    (fun n _ => neutralNF599Gain_nonneg _ _ (by positivity))
  rw [h.tsum_eq] at hs
  linarith only [hs]

def neutralNF599GainQ (n : ℕ) : ℚ :=
  let a : ℚ := n+1/4
  225/(a*(a^2+225))

set_option maxRecDepth 10000 in
set_option maxHeartbeats 2000000 in
theorem neutralNF599Gain20_rat :
    (67/10:ℚ) < ∑ n ∈ range 20, neutralNF599GainQ n := by
  decide +kernel

theorem neutralNF599Gain20_real :
    (67/10:ℝ) < neutralNF599Gain (1/4) 30 +
      ∑ n ∈ range 19, neutralNF599Gain ((n:ℝ)+1+1/4) 30 := by
  have h : ((67/10:ℚ):ℝ) < ((∑ n ∈ range 20, neutralNF599GainQ n:ℚ):ℝ) :=
    Rat.cast_lt.mpr neutralNF599Gain20_rat
  rw [sum_range_succ',Rat.cast_add,Rat.cast_sum] at h
  simpa [neutralNF599GainQ,neutralNF599Gain,show (30/2:ℝ)^2=225 by norm_num,add_comm,add_left_comm,add_assoc] using h

theorem neutralNF599GammaZero_lower :
    -(28/5:ℝ) < Zeta23.EF.gammaBracket 0 := by
  have hp : Real.pi < 22/7 := Real.pi_lt_d4.trans (by norm_num)
  have hl2 : Real.log 2 < 7/10 := Real.log_two_lt_d9.trans (by norm_num)
  have he : (22/7:ℝ) < Real.exp (6/5) := by
    have h := Real.sum_le_exp_of_nonneg (show (0:ℝ) ≤ 6/5 by norm_num) 5
    apply lt_of_lt_of_le _ h
    norm_num [Finset.sum_range_succ,Nat.factorial_succ]
  have hlp : Real.log Real.pi < 6/5 := by
    apply (Real.log_lt_iff_lt_exp Real.pi_pos).mpr
    exact hp.trans he
  have hg := Real.eulerMascheroniConstant_lt_two_thirds
  unfold Zeta23.EF.gammaBracket
  simp only [Complex.ofReal_zero,mul_zero,zero_div,add_zero]
  rw [neutralActualZetaDigamma_quarter_re]
  linarith

theorem neutralNF599GammaLower (t : ℝ) :
    -(28/5:ℝ) < Zeta23.EF.gammaBracket t := by
  have h := neutralNF599GammaLower_partial t 0
  simp only [range_zero,sum_empty,add_zero] at h
  have h0 := neutralNF599Gain_nonneg (1/4) t (by norm_num)
  linarith [neutralNF599GammaZero_lower]

theorem neutralNF599GammaHigh (t : ℝ) (ht : 30 ≤ |t|) :
    (11/10:ℝ) < Zeta23.EF.gammaBracket t := by
  have hsq : (30:ℝ)^2 ≤ t^2 := by
    rw [← sq_abs t]
    exact pow_le_pow_left₀ (by norm_num) ht 2
  have h0 := neutralNF599Gain_mono_sq (1/4) 30 t (by norm_num) hsq
  have hs : (∑ n ∈ range 19, neutralNF599Gain ((n:ℝ)+1+1/4) 30) ≤
      ∑ n ∈ range 19, neutralNF599Gain ((n:ℝ)+1+1/4) t :=
    sum_le_sum (fun n _ => neutralNF599Gain_mono_sq _ _ _ (by positivity) hsq)
  linarith [neutralNF599GammaLower_partial t 19,neutralNF599Gain20_real,
    neutralNF599GammaZero_lower]

end
end WeilDefect
