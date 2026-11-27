import WeilDefect.MasterRecon.V10B20a
import WeilDefect.MasterRecon.V10B22b
import WeilDefect.MasterRecon.V10B8f

/-! V10B23a: the missing reciprocal and the exact factor two in the
physical digamma normalization. The partial-fraction theorem remains an
explicit external input. -/
namespace WeilDefect.MasterRecon.V10B23a

open MeasureTheory Set Filter Complex
open scoped ComplexConjugate

noncomputable def tailKernel (z : ℂ) (s : ℝ) : ℂ :=
  Complex.exp (-(s:ℂ))*(1-Complex.exp (-z*(s:ℂ)))/(1-Complex.exp (-(s:ℂ)))

noncomputable def kernel (z : ℂ) (s : ℝ) : ℂ :=
  (Complex.exp (-(s:ℂ))-Complex.exp (-z*(s:ℂ)))/(1-Complex.exp (-(s:ℂ)))

theorem kernel_split (z : ℂ) (s : ℝ) (hs : 0 < s) :
    kernel z s = tailKernel z s-Complex.exp (-z*(s:ℂ)) := by
  have h : Complex.exp (-(s:ℂ)) ≠ 1 := by
    intro he
    have hh := congrArg norm he
    rw [Complex.norm_exp,Complex.neg_re,Complex.ofReal_re,norm_one] at hh
    have h' := Real.exp_lt_exp.mpr (show -s<0 by linarith)
    rw [Real.exp_zero] at h'
    linarith
  unfold kernel tailKernel
  field_simp [sub_ne_zero.mpr (Ne.symm h)]
  <;> ring

theorem denominator_bound (s : ℝ) (hs : 0 < s) :
    s ≤ (1+s)*(1-Real.exp (-s)) := by
  have h := mul_le_mul_of_nonneg_right (Real.add_one_le_exp s) (Real.exp_pos (-s)).le
  rw [← Real.exp_add,add_neg_cancel,Real.exp_zero] at h
  nlinarith only [h]

theorem tailKernel_bound (z : ℂ) (hz : 0 ≤ z.re) (s : ℝ) (hs : 0 < s) :
    ‖tailKernel z s‖ ≤ 2*‖z‖*(1+s)*Real.exp (-s) := by
  have hd : 0 < 1-Real.exp (-s) := by
    have h := Real.exp_lt_exp.mpr (show -s<0 by linarith)
    rw [Real.exp_zero] at h
    linarith
  have he : Complex.exp (-(s:ℂ)) = (Real.exp (-s):ℂ) := by
    rw [Complex.ofReal_exp,Complex.ofReal_neg]
  unfold tailKernel
  rw [he,norm_div,norm_mul,← Complex.ofReal_one,← Complex.ofReal_sub,
    Complex.norm_real,Real.norm_eq_abs,abs_of_pos hd,
    Complex.norm_real,Real.norm_eq_abs,abs_of_pos (Real.exp_pos _)]
  apply (div_le_iff₀ hd).mpr
  have h₁ := mul_le_mul_of_nonneg_left (V10B20a.exp_difference z hz s hs.le)
    (Real.exp_pos (-s)).le
  have h₂ := mul_le_mul_of_nonneg_left (denominator_bound s hs)
    (show 0 ≤ 2*‖z‖*Real.exp (-s) by positivity)
  nlinarith only [h₁,h₂]

theorem tailKernel_integrable (z : ℂ) (hz : 0 < z.re) :
    IntegrableOn (tailKernel z) (Ioi 0) := by
  have h₁ : IntegrableOn (fun s : ℝ => Real.exp (-s)) (Ioi 0) := by
    simpa using integrableOn_exp_mul_Ioi (a := (-1:ℝ)) (by norm_num) 0
  have h₂ : IntegrableOn (fun s : ℝ => s*Real.exp (-s)) (Ioi 0) := by
    apply Integrable.of_integral_ne_zero
    have h := V10B20a.exp_moment 1 (by norm_num)
    simpa using (show (∫ s in Ioi (0:ℝ), s*Real.exp (-1*s)) ≠ 0 by rw [h]; norm_num)
  have h₃ := (h₁.add h₂).const_mul (2*‖z‖)
  have hm : Measurable (tailKernel z) := by unfold tailKernel; fun_prop
  apply h₃.mono' hm.aestronglyMeasurable
  rw [ae_restrict_iff' measurableSet_Ioi]
  exact Eventually.of_forall fun s hs => by
    change ‖tailKernel z s‖ ≤ 2*‖z‖*(Real.exp (-s)+s*Real.exp (-s))
    rw [← add_mul]
    exact tailKernel_bound z hz.le s hs

theorem exp_integral (z : ℂ) (hz : 0 < z.re) :
    (∫ s in Ioi (0:ℝ), Complex.exp (-z*(s:ℂ))) = 1/z := by
  have h : (-z).re < 0 := by rw [Complex.neg_re]; linarith
  rw [integral_exp_mul_complex_Ioi h 0]
  simp

theorem kernel_integrable (z : ℂ) (hz : 0 < z.re) :
    IntegrableOn (kernel z) (Ioi 0) := by
  have h : (-z).re < 0 := by rw [Complex.neg_re]; linarith
  apply ((tailKernel_integrable z hz).sub (integrableOn_exp_mul_complex_Ioi h 0)).congr
  rw [ae_restrict_iff' measurableSet_Ioi]
  exact Eventually.of_forall fun s hs => (kernel_split z s hs).symm

theorem digamma_integral (z : ℂ) (hz : 0 < z.re) (hp : V10B20a.PartialFraction z) :
    (∫ s in Ioi (0:ℝ), kernel z s) =
      Complex.digamma z+(Real.eulerMascheroniConstant:ℂ) := by
  have h : (-z).re < 0 := by rw [Complex.neg_re]; linarith
  calc
    _ = ∫ s in Ioi (0:ℝ), tailKernel z s-Complex.exp (-z*(s:ℂ)) := by
      apply setIntegral_congr_fun measurableSet_Ioi
      intro s hs
      exact kernel_split z s hs
    _ = _ := by
      rw [integral_sub (tailKernel_integrable z hz) (integrableOn_exp_mul_complex_Ioi h 0)]
      change (∫ s in Ioi (0:ℝ), tailKernel z s) -
        (∫ s in Ioi (0:ℝ), Complex.exp (-z*(s:ℂ))) = _
      rw [show (∫ s in Ioi (0:ℝ), tailKernel z s) =
        Complex.digamma z+(Real.eulerMascheroniConstant:ℂ)+1/z from
        V10B20a.scalar_integral_receiver z hz hp,exp_integral z hz]
      ring

noncomputable def argument (u : ℝ) : ℂ := 1/4+I*((-Real.pi*u:ℝ):ℂ)

theorem argument_re (u : ℝ) : (argument u).re = 1/4 := by
  unfold argument
  norm_num [Complex.add_re,Complex.mul_re,Complex.div_re,Complex.normSq]

theorem symbol_kernel (r u : ℝ) (hr : 0 < r) :
    V10B22b.symbol r u = ((2*(kernel (argument u) (2*r)).re:ℝ):ℂ) := by
  have he : Complex.exp (-((2*r:ℝ):ℂ)) = (Real.exp (-2*r):ℂ) := by
    rw [Complex.ofReal_exp]
    push_cast
    ring_nf
  have hz : Complex.exp (-(argument u)*((2*r:ℝ):ℂ)) =
      (Real.exp (-r/2):ℂ)*V10B22b.phase r u := by
    unfold argument V10B22b.phase
    rw [Complex.ofReal_exp,← Complex.exp_add]
    congr 1
    push_cast
    ring
  have hp : conj (V10B22b.phase r u) = V10B22b.phase (-r) u := by
    unfold V10B22b.phase
    rw [← Complex.exp_conj]
    congr 1
    simp
    ring
  have hd : 0 < 1-Real.exp (-2*r) := V10B21c.denominator_pos r hr
  unfold V10B22b.symbol kernel V10B21c.denominator
  rw [he,hz,← Complex.ofReal_one,← Complex.ofReal_sub,Complex.real_smul,Complex.ofReal_inv]
  apply Complex.ext
  · rw [← hp]
    simp [Complex.div_re,Complex.normSq,Complex.mul_re,Complex.add_re,Complex.sub_re]
    field_simp [hd.ne']
    <;> ring
  · rw [← hp]
    simp [Complex.mul_im,Complex.add_im,Complex.sub_im]

theorem symbol_integral (u : ℝ) (hp : V10B20a.PartialFraction (argument u)) :
    (∫ r in Ioi (0:ℝ), V10B22b.symbol r u) =
      (((Complex.digamma (argument u)).re+Real.eulerMascheroniConstant:ℝ):ℂ) := by
  have hz : 0 < (argument u).re := by rw [argument_re]; norm_num
  calc
    _ = ∫ r in Ioi (0:ℝ), ((2*(kernel (argument u) (2*r)).re:ℝ):ℂ) := by
      apply setIntegral_congr_fun measurableSet_Ioi
      intro r hr
      exact symbol_kernel r u hr
    _ = _ := by
      rw [← integral_complex_ofReal,integral_const_mul,
        integral_comp_mul_left_Ioi (fun s => (kernel (argument u) s).re) 0 (by norm_num : (0:ℝ)<2)]
      simp only [mul_zero,smul_eq_mul]
      rw [integral_re (kernel_integrable _ hz),digamma_integral _ hz hp]
      push_cast
      simp only [Complex.add_re,Complex.ofReal_re]
      ring

theorem literal_symbol_integral (u : ℝ) (hp : V10B20a.PartialFraction (argument u)) :
    (∫ r in Ioi (0:ℝ), V10B22b.symbol r u) =
      ((V10B8e.gammaSymbol u+Real.log Real.pi+Real.eulerMascheroniConstant:ℝ):ℂ) := by
  rw [symbol_integral u hp,V10B8f.gammaSymbol_reparam]
  unfold argument
  congr 1
  ring

end WeilDefect.MasterRecon.V10B23a

#print axioms WeilDefect.MasterRecon.V10B23a.kernel_split
#print axioms WeilDefect.MasterRecon.V10B23a.denominator_bound
#print axioms WeilDefect.MasterRecon.V10B23a.tailKernel_bound
#print axioms WeilDefect.MasterRecon.V10B23a.tailKernel_integrable
#print axioms WeilDefect.MasterRecon.V10B23a.exp_integral
#print axioms WeilDefect.MasterRecon.V10B23a.kernel_integrable
#print axioms WeilDefect.MasterRecon.V10B23a.digamma_integral
#print axioms WeilDefect.MasterRecon.V10B23a.argument_re
#print axioms WeilDefect.MasterRecon.V10B23a.symbol_kernel
#print axioms WeilDefect.MasterRecon.V10B23a.symbol_integral
#print axioms WeilDefect.MasterRecon.V10B23a.literal_symbol_integral
