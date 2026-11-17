import WeilDefect.Arithmetic.ActualZetaOriginalCollarPrimeBound

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped SchwartzMap ComplexConjugate

/-! NF600: both literal poles are retained as cross moments. The
 bound holds for arbitrary complex collar tests, not merely real odd. -/

theorem neutralNF600Moment_bound (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0)
    (t : ℝ) (ht : |t| ≤ 1/2) :
    ‖sourceWindowMoment (11/10:ℝ) t (s.toLp 2 volume)‖ ≤
      2*‖s.toLp 1 volume‖ := by
  rw [← neutralWindowEvaluation_imaginary (11/10:ℝ) (-t)]
  simp only [neg_neg]
  rw [neutralNF573WindowEvaluation_eq_raw_of_ae _ _ _ (neutralNF573OriginalCollar_window_ae s hs)]
  unfold neutralRawTransform
  let f := fun x : ℝ => s x * Complex.exp (Complex.I*(Complex.I*((-t:ℝ):ℂ))*(x:ℂ))
  have hf (x : ℝ) : ‖f x‖ ≤ 2*‖s x‖ := by
    by_cases hx : x∈neutralNF543OriginalCollars
    · have hwin : |x| ≤ (11/10:ℝ) := by
        rcases hx with h|h <;> exact abs_le.mpr ⟨by linarith [h.1],by linarith [h.2]⟩
      have htx : t*x ≤ 11/20 := by
        calc
          _ ≤ |t*x| := le_abs_self _
          _ = |t|*|x| := abs_mul _ _
          _ ≤ (1/2:ℝ)*(11/10) := mul_le_mul ht hwin (abs_nonneg _) (by norm_num)
          _ = _ := by norm_num
      have he : Complex.I*(Complex.I*((-t:ℝ):ℂ))*(x:ℂ)=((t*x:ℝ):ℂ) := by
        calc
          _ = (Complex.I*Complex.I)*((-t:ℝ):ℂ)*(x:ℂ) := by ring
          _ = _ := by rw [Complex.I_mul_I]; push_cast; ring
      have hE : Real.exp (t*x) ≤ 2 :=
        (Real.exp_le_exp.mpr htx).trans
          (by simpa [neutralNF578B] using neutralNF585Exp_half_le_two)
      dsimp [f]
      rw [he,norm_mul,Complex.norm_exp,Complex.ofReal_re]
      exact (mul_le_mul_of_nonneg_left hE (norm_nonneg _)).trans_eq (mul_comm _ _)
    · simp [f,hs x hx]
  have hi : Integrable (fun x : ℝ => 2*‖s x‖) :=
    s.integrable.norm.const_mul 2
  have hfi : Integrable (fun x => ‖f x‖) := by
    apply hi.mono' (by dsimp [f]; fun_prop)
    filter_upwards [] with x
    rw [Real.norm_eq_abs,abs_of_nonneg (norm_nonneg _)]
    exact hf x
  change ‖∫ x,f x‖ ≤ _
  calc
    _ ≤ ∫ x,‖f x‖ := norm_integral_le_integral_norm _
    _ ≤ ∫ x,2*‖s x‖ := integral_mono hfi hi hf
    _ = _ := by rw [integral_const_mul,SchwartzMap.norm_toLp_one]

def neutralNF600Pole (s : 𝓢(ℝ,ℂ)) : ℂ :=
  Zeta23.paperFT (neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume)) (Complex.I/2) +
  Zeta23.paperFT (neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume)) (-Complex.I/2)

theorem neutralNF600Pole_bound (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0) :
    |(neutralNF600Pole s).re| ≤ (4/125:ℝ)*neutralNF600Mass s := by
  let f := s.toLp 2 volume
  let m := neutralNF600Mass s
  let A := sourceWindowMoment (11/10:ℝ) (1/2) f
  let B := sourceWindowMoment (11/10:ℝ) (-1/2) f
  have hA : ‖A‖ ≤ 2*‖s.toLp 1 volume‖ := neutralNF600Moment_bound s hs _ (by norm_num)
  have hB : ‖B‖ ≤ 2*‖s.toLp 1 volume‖ := neutralNF600Moment_bound s hs _ (by norm_num)
  have hL := neutralNF600L1_bound s hs
  have hm : 0≤m := by dsimp [m,neutralNF600Mass]; positivity
  have hq : ‖s.toLp 1 volume‖^2 ≤ m/250 := by
    calc
      _ ≤ (Real.sqrt m*Real.sqrt (1/250))^2 := pow_le_pow_left₀ (norm_nonneg _) hL 2
      _ = _ := by rw [mul_pow,Real.sq_sqrt hm,Real.sq_sqrt (by norm_num)]; ring
  have hp : neutralNF600Pole s=conj B*A+conj A*B := by
    unfold neutralNF600Pole
    simp only [← neutralRawTransform_eq_paperFT]
    rw [show Complex.I/2=Complex.I*((1/2:ℝ):ℂ) by push_cast; ring,
      show -Complex.I/2=Complex.I*((-(1/2):ℝ):ℂ) by push_cast; ring]
    exact neutralWindowCorrelation_poleCrossTerms (11/10:ℝ) f f
  apply (Complex.abs_re_le_norm _).trans
  rw [hp]
  calc
    _ ≤ ‖conj B*A‖+‖conj A*B‖ := norm_add_le _ _
    _ = 2*(‖A‖*‖B‖) := by rw [norm_mul,norm_mul,Complex.norm_conj,Complex.norm_conj]; ring
    _ ≤ 2*((2*‖s.toLp 1 volume‖)*(2*‖s.toLp 1 volume‖)) :=
      mul_le_mul_of_nonneg_left (mul_le_mul hA hB (norm_nonneg _) (by positivity)) (by norm_num)
    _ ≤ _ := by change _ ≤ (4/125:ℝ)*m; nlinarith only [hq]

end
end WeilDefect
