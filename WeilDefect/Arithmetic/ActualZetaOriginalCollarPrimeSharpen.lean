import WeilDefect.Arithmetic.ActualZetaOriginalCollarPrimeBound

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped SchwartzMap ComplexConjugate

/-! NF610: sharpen only the exact coefficient of the authentic n=9
prime contribution. No dependency on the pending pole or gamma modules. -/

theorem neutralNF610Prime_bound (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0)
    (hc : ArithmeticFunction.vonMangoldt 9 / Real.sqrt 9 ≤ (3/8:ℝ)) :
    |(neutralNF600Prime s).re| ≤ (3/8:ℝ)*neutralNF600Mass s := by
  have h1 := neutralNF600Correlation_log9_bound s hs (Real.log 9) (Or.inl rfl)
  have h2 := neutralNF600Correlation_log9_bound s hs (-Real.log 9) (Or.inr rfl)
  apply (Complex.abs_re_le_norm _).trans
  rw [neutralNF600Prime_single s hs,norm_mul,Complex.norm_real,Real.norm_eq_abs,
    abs_of_nonneg (div_nonneg ArithmeticFunction.vonMangoldt_nonneg (Real.sqrt_nonneg _))]
  have hs0 := norm_add_le
    (neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) (Real.log 9))
    (neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) (-Real.log 9))
  have hh : ‖neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) (Real.log 9) +
    neutralWindowCorrelation (11/10:ℝ) (s.toLp 2 volume) (s.toLp 2 volume) (-Real.log 9)‖ ≤
    neutralNF600Mass s := by linarith
  exact mul_le_mul hc hh (norm_nonneg _) (by norm_num)

theorem neutralNF610Prime9_coefficient :
    ArithmeticFunction.vonMangoldt 9 / Real.sqrt 9 ≤ (3/8:ℝ) := by
  have h9 : ArithmeticFunction.vonMangoldt 9 = Real.log 3 := by
    rw [show (9:ℕ)=3^2 by norm_num,
      ArithmeticFunction.vonMangoldt_apply_pow (by decide),
      ArithmeticFunction.vonMangoldt_apply_prime (by decide)]
    norm_num
  have he : (3:ℝ) < Real.exp (9/8) := by
    have h := Real.sum_le_exp_of_nonneg (show (0:ℝ) ≤ 9/8 by norm_num) 5
    apply lt_of_lt_of_le _ h
    norm_num [Finset.sum_range_succ,Nat.factorial_succ]
  have hl := (Real.log_lt_iff_lt_exp (by norm_num : (0:ℝ)<3)).mpr he
  rw [h9,show Real.sqrt 9=3 by norm_num]
  linarith

theorem neutralNF610Prime_bound_actual (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0) :
    |(neutralNF600Prime s).re| ≤ (3/8:ℝ)*neutralNF600Mass s :=
  neutralNF610Prime_bound s hs neutralNF610Prime9_coefficient


end
end WeilDefect
