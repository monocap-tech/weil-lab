import WeilDefect.MasterRecon.V10B29a

/-! V10B29b: explicit finite polynomial trial bounds and exact
singular coefficient action. No endpoint vanishing is required. -/
namespace WeilDefect.MasterRecon.V10B29b

open MeasureTheory Set Complex
open scoped BigOperators

noncomputable def poly (n : ℕ) (c : ℕ → ℂ) (x : ℝ) : ℂ :=
  ∑ j ∈ Finset.range n, c j*(x:ℂ)^j

noncomputable def B (n : ℕ) (c : ℕ → ℂ) : ℝ := ∑ j ∈ Finset.range n, ‖c j‖
noncomputable def K (n : ℕ) (c : ℕ → ℂ) : ℝ := ∑ j ∈ Finset.range n, (j:ℝ)*‖c j‖

theorem poly_continuous (n : ℕ) (c : ℕ → ℂ) : Continuous (poly n c) := by
  unfold poly
  fun_prop

theorem pow_difference (j : ℕ) (x y : ℂ) (hx : ‖x‖ ≤ 1) (hy : ‖y‖ ≤ 1) :
    ‖x^j-y^j‖ ≤ (j:ℝ)*‖x-y‖ := by
  induction j with
  | zero => simp
  | succ j ih =>
    rw [show x^(j+1)-y^(j+1)=(x^j-y^j)*x+y^j*(x-y) by rw [pow_succ,pow_succ]; ring]
    have h₁ : ‖(x^j-y^j)*x‖ ≤ (j:ℝ)*‖x-y‖ := by
      rw [norm_mul]
      exact (mul_le_of_le_one_right (norm_nonneg _) hx).trans ih
    have h₂ : ‖y^j*(x-y)‖ ≤ ‖x-y‖ := by
      rw [norm_mul,norm_pow]
      exact mul_le_of_le_one_left (norm_nonneg _) (pow_le_one₀ (norm_nonneg _) hy)
    refine (norm_add_le _ _).trans ((add_le_add h₁ h₂).trans ?_)
    push_cast
    ring_nf
    exact le_rfl

theorem poly_bounded (n : ℕ) (c : ℕ → ℂ) (x : ℝ) (hx : x ∈ Icc 0 1) :
    ‖poly n c x‖ ≤ B n c := by
  unfold poly B
  refine (norm_sum_le _ _).trans (Finset.sum_le_sum fun j _ => ?_)
  rw [norm_mul,norm_pow,Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg hx.1]
  exact mul_le_of_le_one_right (norm_nonneg _) (pow_le_one₀ hx.1 hx.2)

theorem poly_lipschitz (n : ℕ) (c : ℕ → ℂ) (x y : ℝ)
    (hx : x ∈ Icc 0 1) (hy : y ∈ Icc 0 1) :
    ‖poly n c x-poly n c y‖ ≤ K n c*|x-y| := by
  unfold poly K
  rw [← Finset.sum_sub_distrib,Finset.sum_mul]
  refine (norm_sum_le _ _).trans (Finset.sum_le_sum fun j _ => ?_)
  rw [← mul_sub,norm_mul]
  have h := pow_difference j (x:ℂ) (y:ℂ)
    (by simpa [Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg hx.1] using hx.2)
    (by simpa [Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg hy.1] using hy.2)
  rw [← Complex.ofReal_sub,Complex.norm_real,Real.norm_eq_abs] at h
  calc
    _ ≤ ‖c j‖*((j:ℝ)*|x-y|) := mul_le_mul_of_nonneg_left h (norm_nonneg _)
    _ = _ := by ring

theorem poly_carrier_exists (n : ℕ) (c : ℕ → ℂ)
    (hS : V10B23b.SeriesSupply) (C : ℝ) (hC : ∀ u, |V10B8e.residual u| ≤ C) :
    ∃ g : V08I.logCarrier (1/4),
      (V08I.physicalInclusion (1/4) g : ℝ → ℂ) =ᵐ[volume]
        V10B28c.trial (1/4) (poly n c) := by
  have hB : 0 ≤ B n c := Finset.sum_nonneg fun _ _ => norm_nonneg _
  have hK : 0 ≤ K n c := Finset.sum_nonneg fun _ _ => by positivity
  have hb : ∀ x ∈ Icc 0 (2*(1/4:ℝ)), ‖poly n c x‖ ≤ B n c :=
    fun x hx => poly_bounded n c x ⟨hx.1,by linarith [hx.2]⟩
  have hl : ∀ x ∈ Icc 0 (2*(1/4:ℝ)), ∀ y ∈ Icc 0 (2*(1/4:ℝ)),
      ‖poly n c x-poly n c y‖ ≤ K n c*|x-y| :=
    fun x hx y hy => poly_lipschitz n c x y ⟨hx.1,by linarith [hx.2]⟩ ⟨hy.1,by linarith [hy.2]⟩
  obtain ⟨g,hg⟩ := V10B29a.trial_carrier_exists (1/4) (B n c) (K n c) (by norm_num)
    hB hK (poly n c) (poly_continuous n c).measurable hb hl hS C hC
  refine ⟨g,?_⟩
  rw [hg]
  exact V10B29a.physicalTrial_ae _ _ _ _ _

theorem singular_monomial (j : ℕ) (x : ℝ) (hx : 0 < x) :
    V10B28a.singular (fun y : ℝ => (y:ℂ)^j) x =
      (V10B24a.harmonic j:ℂ)*(x:ℂ)^j/2 := by
  unfold V10B28a.singular
  have he : (∫ r in Ioc (0:ℝ) x, ((1/(2*r):ℝ):ℂ)*((x:ℂ)^j-((x-r:ℝ):ℂ)^j)) =
      ∫ r in Ioc (0:ℝ) x, ((V10B24a.dd j x r:ℝ):ℂ)/2 := by
    apply setIntegral_congr_fun measurableSet_Ioc
    intro r hr
    rw [V10B24a.dd_eq j x r hr.1.ne']
    push_cast
    field_simp [show (r:ℂ) ≠ 0 by exact_mod_cast hr.1.ne']
    <;> ring
  rw [he,integral_div,integral_complex_ofReal,← intervalIntegral.integral_of_le hx.le,
    V10B24a.dd_integral j x hx]
  push_cast
  ring

end WeilDefect.MasterRecon.V10B29b

#print axioms WeilDefect.MasterRecon.V10B29b.poly_continuous
#print axioms WeilDefect.MasterRecon.V10B29b.pow_difference
#print axioms WeilDefect.MasterRecon.V10B29b.poly_bounded
#print axioms WeilDefect.MasterRecon.V10B29b.poly_lipschitz
#print axioms WeilDefect.MasterRecon.V10B29b.poly_carrier_exists
#print axioms WeilDefect.MasterRecon.V10B29b.singular_monomial
