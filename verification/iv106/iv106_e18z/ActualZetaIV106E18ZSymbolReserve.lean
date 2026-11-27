import WeilDefect.Arithmetic.ActualZetaIV106E17AExplicitShift
import WeilDefect.Arithmetic.ActualZetaNativeFormOperator

namespace WeilDefect
noncomputable section
open MeasureTheory InnerProductSpace ContinuousLinearMap
open scoped InnerProduct ComplexConjugate

/-- Monotonicity of the real reciprocal on a fixed positive vertical line. -/
theorem neutralIV106E18ZReciprocal (r y t : ℝ) (hr : 0 < r)
    (h : |y| ≤ |t|) :
    (1/((r:ℂ)+Complex.I*(t:ℂ))).re ≤
      (1/((r:ℂ)+Complex.I*(y:ℂ))).re := by
  simp only [one_div,Complex.inv_re,Complex.normSq_apply,Complex.add_re,
    Complex.add_im,Complex.mul_re,Complex.mul_im,Complex.ofReal_re,
    Complex.ofReal_im,Complex.I_re,Complex.I_im,zero_mul,one_mul,
    mul_zero,sub_zero,zero_add,add_zero]
  have hy : y^2 ≤ t^2 := by
    have hh := pow_le_pow_left₀ (abs_nonneg y) h 2
    simpa only [sq_abs] using hh
  apply (div_le_div_iff₀ (by positivity : 0 < r*r+t*t)
    (by positivity : 0 < r*r+y*y)).mpr
  exact mul_le_mul_of_nonneg_left (by nlinarith) hr.le

/-- The same convergent digamma series used in E2 gives monotonicity
in absolute height, not merely comparison with the quarter anchor. -/
theorem neutralIV106E18ZQuarter_mono (y t : ℝ) (h : |y| ≤ |t|) :
    (Complex.digamma (1/4+Complex.I*(y:ℂ))).re ≤
      (Complex.digamma (1/4+Complex.I*(t:ℂ))).re := by
  let z : ℂ := 1/4+Complex.I*(y:ℂ)
  let w : ℂ := 1/4+Complex.I*(t:ℂ)
  have hz : z.re = 1/4 := by simp [z]
  have hw : w.re = 1/4 := by simp [w]
  have hzmem : z ∈ Complex.integerComplement := by
    rintro ⟨n,hn⟩
    have he := congrArg Complex.re hn
    simp only [Complex.intCast_re,hz] at he
    have hi : (1:ℤ) = 4*n := by exact_mod_cast (show (1:ℝ) = 4*(n:ℝ) by linarith)
    omega
  have hwmem : w ∈ Complex.integerComplement := by
    rintro ⟨n,hn⟩
    have he := congrArg Complex.re hn
    simp only [Complex.intCast_re,hw] at he
    have hi : (1:ℤ) = 4*n := by exact_mod_cast (show (1:ℝ) = 4*(n:ℝ) by linarith)
    omega
  have hs := Complex.hasSum_re (Zeta23.DigammaSeries.hasSum_digamma_series hzmem)
  have ht := Complex.hasSum_re (Zeta23.DigammaSeries.hasSum_digamma_series hwmem)
  have hc (n : ℕ) :
      (1/((n:ℂ)+1)-1/(z+n+1)).re ≤
      (1/((n:ℂ)+1)-1/(w+n+1)).re := by
    have hr := neutralIV106E18ZReciprocal ((1/4:ℝ)+n+1) y t (by positivity) h
    simp only [Complex.sub_re]
    have ez : z+n+1 = (((1/4:ℝ)+n+1:ℝ):ℂ)+Complex.I*(y:ℂ) := by
      dsimp [z]; push_cast; ring
    have ew : w+n+1 = (((1/4:ℝ)+n+1:ℝ):ℂ)+Complex.I*(t:ℂ) := by
      dsimp [w]; push_cast; ring
    rw [ez,ew]
    linarith
  have hsum := Summable.tsum_le_tsum hc hs.summable ht.summable
  rw [hs.tsum_eq,ht.tsum_eq] at hsum
  have hrec : (1/w).re ≤ (1/z).re := by
    simpa [w,z,Complex.ofReal_div] using
      neutralIV106E18ZReciprocal (1/4) y t (by norm_num) h
  simp only [Complex.add_re,Complex.ofReal_re] at hsum
  change (Complex.digamma z).re ≤ (Complex.digamma w).re
  linarith only [hsum,hrec]

/-- Upper vertical tail with the actual pi-normalization. -/
theorem neutralIV106E18ZGamma_tail (ξ : ℝ) (hξ : 1 ≤ |ξ|) :
    compactWindowArchimedeanSymbol (2*Real.pi*ξ) ≤
      Real.log (|ξ|+1/(4*Real.pi))+4 := by
  let z : ℂ := 1/4+Complex.I*((Real.pi*ξ:ℝ):ℂ)
  have hre : z.re = 1/4 := by simp [z]
  have him : z.im = Real.pi*ξ := by simp [z]
  have hi : 1 ≤ |z.im| := by
    rw [him,abs_mul,abs_of_pos Real.pi_pos]
    nlinarith [Real.pi_gt_three]
  have hn : 0 < ‖z‖ := lt_of_lt_of_le zero_lt_one (hi.trans (Complex.abs_im_le_norm z))
  have hd := (abs_le.mp (neutralActualZetaDigamma_log_error
    (z := z) (by rw [hre]; norm_num) hi)).2
  have hu : ‖z‖ ≤ 1/4+Real.pi*|ξ| := by
    have hh := norm_add_le (1/4:ℂ) (Complex.I*((Real.pi*ξ:ℝ):ℂ))
    simpa only [z,norm_mul,Complex.norm_I,one_mul,Complex.norm_real,
      Real.norm_eq_abs,abs_mul,abs_of_pos Real.pi_pos,
      show ‖(1/4:ℂ)‖ = (1/4:ℝ) by norm_num] using hh
  have he : Real.pi*(|ξ|+1/(4*Real.pi)) = 1/4+Real.pi*|ξ| := by
    field_simp [Real.pi_ne_zero] <;> ring
  rw [← he] at hu
  have hl := Real.log_le_log hn hu
  rw [Real.log_mul Real.pi_ne_zero (by positivity)] at hl
  have hz : ((1:ℂ)/4)+Complex.I*(((2*Real.pi*ξ:ℝ):ℂ)/2) = z := by
    dsimp [z]; push_cast; ring
  unfold compactWindowArchimedeanSymbol
  rw [hz]
  linarith

theorem neutralIV106E18ZGamma_upper (ξ : ℝ) :
    compactWindowArchimedeanSymbol (2*Real.pi*ξ) ≤
      logarithmicFourierWeight ξ+4 := by
  have hp := Real.pi_gt_three
  have he : 1 ≤ Real.exp 1 := by
    rw [← Real.exp_zero]
    exact Real.exp_le_exp.mpr (by norm_num)
  have hs : 1/(4*Real.pi) ≤ 1 := by
    apply (div_le_iff₀ (by positivity)).mpr
    linarith
  by_cases hξ : 1 ≤ |ξ|
  · have hl := Real.log_le_log (show 0 < |ξ|+1/(4*Real.pi) by positivity)
      (show |ξ|+1/(4*Real.pi) ≤ Real.exp 1+|ξ| by linarith)
    unfold logarithmicFourierWeight
    linarith [neutralIV106E18ZGamma_tail ξ hξ]
  · have hm := neutralIV106E18ZQuarter_mono (Real.pi*ξ) Real.pi (by
      rw [abs_mul,abs_of_pos Real.pi_pos]
      exact mul_le_of_le_one_right Real.pi_pos.le (le_of_not_ge hξ))
    have hz : ((1:ℂ)/4)+Complex.I*(((2*Real.pi*ξ:ℝ):ℂ)/2) =
        1/4+Complex.I*((Real.pi*ξ:ℝ):ℂ) := by push_cast; ring
    have hz1 : ((1:ℂ)/4)+Complex.I*(((2*Real.pi*(1:ℝ):ℝ):ℂ)/2) =
        1/4+Complex.I*(Real.pi:ℂ) := by push_cast; ring
    have hu := neutralIV106E18ZGamma_tail 1 (by norm_num)
    rw [abs_one] at hu
    have hl := Real.log_le_sub_one_of_pos (show 0 < 1+1/(4*Real.pi) by positivity)
    have hw := one_le_logarithmicFourierWeight ξ
    unfold compactWindowArchimedeanSymbol at hu ⊢
    rw [hz1] at hu
    rw [hz]
    linarith

/-- Absolute ratio envelope for the literal seven-prime window. -/
theorem neutralIV106E18ZRatio (ξ : ℝ) :
    ‖neutralLogSymbolRatio (11/10:ℝ) ξ‖ ≤ 19 := by
  have hlo := neutralIV106E17ASymbol_shift ξ
  have hu := neutralIV106E18ZGamma_upper ξ
  have hp := (abs_le.mp ((neutralActualZetaPrimeSymbol_abs_le (11/10)
    (2*Real.pi*ξ)).trans neutralIV106E17APrime_bound)).1
  have hw := one_le_logarithmicFourierWeight ξ
  have hhi : rightLimitCompactWeilSymbolMathlib (11/10:ℝ) ξ ≤
      logarithmicFourierWeight ξ+12 := by
    unfold rightLimitCompactWeilSymbolMathlib rightLimitCompactWeilSymbol
    linarith
  have hbound : |rightLimitCompactWeilSymbolMathlib (11/10:ℝ) ξ| ≤
      19*logarithmicFourierWeight ξ := by
    apply abs_le.mpr
    constructor <;> linarith
  have hwpos : 0 < logarithmicFourierWeight ξ := zero_lt_one.trans_le hw
  simp only [neutralLogSymbolRatio,Complex.norm_real,Real.norm_eq_abs,
    abs_div,abs_of_pos hwpos]
  exact (div_le_iff₀ hwpos).mpr hbound

#print axioms neutralIV106E18ZReciprocal
#print axioms neutralIV106E18ZQuarter_mono
#print axioms neutralIV106E18ZGamma_tail
#print axioms neutralIV106E18ZGamma_upper
#print axioms neutralIV106E18ZRatio
end
end WeilDefect
