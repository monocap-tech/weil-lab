import WeilDefect.Arithmetic.ActualZetaIV097OriginalSmoothPlateauGate
import Mathlib.MeasureTheory.Group.Integral
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap

theorem neutralIV098Disjoint_norm_sq (a b u v : ℂ)
    (h : a = 0 ∨ b = 0) :
    ‖u * a + v * b‖^2 = ‖u‖^2 * ‖a‖^2 + ‖v‖^2 * ‖b‖^2 := by
  rcases h with ha | hb
  · simp [ha, norm_mul, mul_pow]
  · simp [hb, norm_mul, mul_pow]

theorem neutralIV098Disjoint_integral_sq (p q : ℝ → ℂ) (u v : ℂ)
    (hp : Integrable (fun x => ‖p x‖^2))
    (hq : Integrable (fun x => ‖q x‖^2))
    (hdis : ∀ x, p x = 0 ∨ q x = 0) :
    (∫ x : ℝ, ‖u * p x + v * q x‖^2) =
      ‖u‖^2 * (∫ x : ℝ, ‖p x‖^2) +
      ‖v‖^2 * (∫ x : ℝ, ‖q x‖^2) := by
  calc
    _ = ∫ x : ℝ, (‖u‖^2 * ‖p x‖^2 + ‖v‖^2 * ‖q x‖^2) := by
      apply integral_congr_ae
      exact Filter.Eventually.of_forall fun x =>
        neutralIV098Disjoint_norm_sq (p x) (q x) u v (hdis x)
    _ = _ := by
      rw [integral_add (hp.const_mul _) (hq.const_mul _),
        integral_const_mul, integral_const_mul]

theorem neutralIV098Reflection_integral (g : ℝ → ℝ) :
    (∫ x : ℝ, g (-x)) = ∫ x : ℝ, g x := by
  calc
    _ = ∫ x : ℝ, g ((-1:ℝ) * x) := by simp
    _ = _ := by rw [Measure.integral_comp_mul_left]; norm_num

theorem neutralIV098Plateau_zero_nonpos (x : ℝ) (hx : x ≤ 0) :
    neutralIV097Plateau x = 0 := by
  apply neutralIV097Plateau_zero
  rw [abs_of_nonpos (by linarith : x-1099/1000 ≤ 0)]
  linarith

theorem neutralIV098Derivative_zero_nonpos (x : ℝ) (hx : x ≤ 0) :
    neutralIV097PlateauDerivative x = 0 := by
  apply neutralIV097PlateauDerivative_zero
  rw [abs_of_nonpos (by linarith : x-1099/1000 ≤ 0)]
  linarith

theorem neutralIV098Plateau_reflection_disjoint (x : ℝ) :
    neutralIV097ComplexPlateau x = 0 ∨
      neutralIV097ComplexPlateau (-x) = 0 := by
  rcases le_total x 0 with hx | hx
  · left
    simp [neutralIV097ComplexPlateau, neutralIV098Plateau_zero_nonpos x hx]
  · right
    simp [neutralIV097ComplexPlateau,
      neutralIV098Plateau_zero_nonpos (-x) (by linarith)]

theorem neutralIV098Derivative_reflection_disjoint (x : ℝ) :
    (neutralIV097PlateauDerivative x : ℂ) = 0 ∨
      -(neutralIV097PlateauDerivative (-x) : ℂ) = 0 := by
  rcases le_total x 0 with hx | hx
  · left
    simp [neutralIV098Derivative_zero_nonpos x hx]
  · right
    simp [neutralIV098Derivative_zero_nonpos (-x) (by linarith)]

theorem neutralIV098ReflectedPlateau_hasDerivAt (x : ℝ) :
    HasDerivAt (fun y : ℝ => neutralIV097Plateau (-y))
      (-neutralIV097PlateauDerivative (-x)) x := by
  simpa using (neutralIV097Plateau_hasDerivAt (-x)).comp x (hasDerivAt_id x).neg

#print axioms neutralIV098Disjoint_norm_sq
#print axioms neutralIV098Disjoint_integral_sq
#print axioms neutralIV098Reflection_integral
#print axioms neutralIV098Plateau_zero_nonpos
#print axioms neutralIV098Derivative_zero_nonpos
#print axioms neutralIV098Plateau_reflection_disjoint
#print axioms neutralIV098Derivative_reflection_disjoint
#print axioms neutralIV098ReflectedPlateau_hasDerivAt


/- Append to staged IV098 namespace; import Mathlib.MeasureTheory.Group.Integral. -/
theorem neutralIV098Rho_pointwise_energy (a b : ℝ)
    (ha : 0 ≤ a) (hA : a ≤ 4000) (hb : 0 ≤ b) (hB : b ≤ 4000) :
    (a-b)^2 ≤ 4000*(a+b) := by
  nlinarith [mul_nonneg a (sub_nonneg.mpr hA),
    mul_nonneg b (sub_nonneg.mpr hB), mul_nonneg a b]

theorem neutralIV098Schwartz_energy_upper :
    neutralIV096DerivativeEnergy neutralIV097Schwartz ≤ 8000 := by
  let A : ℝ → ℝ := fun x => neutralIV097Rho (x + (-(1099/1000:ℝ)+1/2000))
  let B : ℝ → ℝ := fun x => neutralIV097Rho (x + (-(1099/1000:ℝ)-1/2000))
  let d := SchwartzMap.derivCLM ℂ ℂ neutralIV097Schwartz
  have hr : Integrable neutralIV097Rho := neutralIV097Bump.integrable_normed
  have hA : Integrable A := hr.comp_add_right _
  have hB : Integrable B := hr.comp_add_right _
  have hA1 : (∫ x, A x) = 1 := by
    dsimp [A]
    rw [integral_add_right_eq_self]
    exact neutralIV097Bump.integral_normed
  have hB1 : (∫ x, B x) = 1 := by
    dsimp [B]
    rw [integral_add_right_eq_self]
    exact neutralIV097Bump.integral_normed
  have hd : Integrable (fun x : ℝ => ‖deriv (neutralIV097Schwartz : ℝ → ℂ) x‖^2) :=
    (memLp_two_iff_integrable_sq_norm d.continuous.aestronglyMeasurable).mp (d.memLp 2 volume)
  unfold neutralIV096DerivativeEnergy
  calc
    _ ≤ ∫ x : ℝ, 4000 * (A x + B x) := by
      apply integral_mono hd ((hA.add hB).const_mul _)
      intro x
      rw [neutralIV097Schwartz_derivative, Complex.norm_real, Real.norm_eq_abs, sq_abs]
      have hD : neutralIV097PlateauDerivative x = A x - B x := by
        unfold neutralIV097PlateauDerivative A B
        congr 1 <;> congr 1 <;> ring
      rw [hD]
      exact neutralIV098Rho_pointwise_energy _ _
        (neutralIV097Rho_bounds _).1 (neutralIV097Rho_bounds _).2
        (neutralIV097Rho_bounds _).1 (neutralIV097Rho_bounds _).2
    _ = 8000 := by
      rw [integral_const_mul, integral_add hA hB, hA1, hB1]
      norm_num

def neutralIV098LeftFun (x : ℝ) : ℂ := neutralIV097ComplexPlateau (-x)

theorem neutralIV098LeftFun_compact : HasCompactSupport neutralIV098LeftFun := by
  apply HasCompactSupport.intro
    (K := Set.Icc (-(4399/4000:ℝ)) (-(4393/4000:ℝ))) isCompact_Icc
  intro x hx
  have hh : (3/4000:ℝ) ≤ |-x-1099/1000| := by
    by_contra h
    have ha := abs_lt.mp (lt_of_not_ge h)
    exact hx ⟨by linarith [ha.2], by linarith [ha.1]⟩
  simp [neutralIV098LeftFun, neutralIV097ComplexPlateau, neutralIV097Plateau_zero _ hh]

def neutralIV098Left : 𝓢(ℝ,ℂ) :=
  neutralIV098LeftFun_compact.toSchwartzMap
    ((Complex.ofRealCLM.contDiff.comp neutralIV097Plateau_smooth).comp
      (show ContDiff ℝ ∞ (fun x : ℝ => -x) by fun_prop))

theorem neutralIV098Left_collars : neutralNF735InOriginalCollars neutralIV098Left := by
  intro x hx
  have hh : (3/4000:ℝ) ≤ |-x-1099/1000| := by
    by_contra h
    have ha := abs_lt.mp (lt_of_not_ge h)
    apply hx
    unfold neutralNF543OriginalCollars
    left
    constructor <;> linarith [ha.1,ha.2]
  change (neutralIV097Plateau (-x) : ℂ) = 0
  simp [neutralIV097Plateau_zero _ hh]

theorem neutralIV098Left_derivative (x : ℝ) :
    deriv (neutralIV098Left : ℝ → ℂ) x =
      -(neutralIV097PlateauDerivative (-x) : ℂ) := by
  simpa using (neutralIV098ReflectedPlateau_hasDerivAt x).ofReal_comp.deriv

theorem neutralIV098Mass_integral (s : 𝓢(ℝ,ℂ)) :
    (∫ x : ℝ, ‖s x‖^2) = ‖s.toLp 2 volume‖^2 := by
  let f := s.toLp 2 volume
  have hinner := inner_self_eq_norm_sq_to_K (𝕜 := ℂ) f
  rw [MeasureTheory.L2.inner_def] at hinner
  simp only [inner_self_eq_norm_sq_to_K] at hinner
  rw [integral_complex_ofReal] at hinner
  have hm : (∫ x : ℝ, ‖f x‖^2) = ‖f‖^2 := by exact_mod_cast hinner
  rw [← hm]
  apply integral_congr_ae
  filter_upwards [s.coeFn_toLp 2 volume] with x hx
  change f x = s x at hx
  rw [hx]

def neutralIV098Pair (u v : ℂ) : 𝓢(ℝ,ℂ) :=
  u • neutralIV097Schwartz + v • neutralIV098Left

theorem neutralIV098Pair_collars (u v : ℂ) :
    neutralNF735InOriginalCollars (neutralIV098Pair u v) := by
  intro x hx
  change u * neutralIV097Schwartz x + v * neutralIV098Left x = 0
  rw [neutralIV097Schwartz_collars x hx, neutralIV098Left_collars x hx]
  simp

#print axioms neutralIV098Rho_pointwise_energy
#print axioms neutralIV098Schwartz_energy_upper
#print axioms neutralIV098LeftFun_compact
#print axioms neutralIV098Left_collars
#print axioms neutralIV098Left_derivative
#print axioms neutralIV098Mass_integral
#print axioms neutralIV098Pair_collars

/- Append to the two earlier IV098 staging snippets. -/
theorem neutralIV098Pair_mass (u v : ℂ) :
    ‖(neutralIV098Pair u v).toLp 2 volume‖^2 =
      (‖u‖^2 + ‖v‖^2) * ‖neutralIV097Schwartz.toLp 2 volume‖^2 := by
  let R := neutralIV097Schwartz
  let L := neutralIV098Left
  have hR : Integrable (fun x : ℝ => ‖R x‖^2) :=
    (memLp_two_iff_integrable_sq_norm R.continuous.aestronglyMeasurable).mp (R.memLp 2 volume)
  have hL : Integrable (fun x : ℝ => ‖L x‖^2) :=
    (memLp_two_iff_integrable_sq_norm L.continuous.aestronglyMeasurable).mp (L.memLp 2 volume)
  have hdis (x : ℝ) : R x = 0 ∨ L x = 0 :=
    neutralIV098Plateau_reflection_disjoint x
  have href : (∫ x : ℝ, ‖L x‖^2) = ∫ x : ℝ, ‖R x‖^2 :=
    neutralIV098Reflection_integral (fun x : ℝ => ‖R x‖^2)
  rw [← neutralIV098Mass_integral (neutralIV098Pair u v)]
  change (∫ x : ℝ, ‖u * R x + v * L x‖^2) =
    (‖u‖^2 + ‖v‖^2) * ‖R.toLp 2 volume‖^2
  rw [neutralIV098Disjoint_integral_sq R L u v hR hL hdis, href,
    neutralIV098Mass_integral R]
  ring

theorem neutralIV098Pair_derivative (u v : ℂ) (x : ℝ) :
    deriv (neutralIV098Pair u v : ℝ → ℂ) x =
      u * deriv (neutralIV097Schwartz : ℝ → ℂ) x +
      v * deriv (neutralIV098Left : ℝ → ℂ) x := by
  have hR := (neutralIV097Schwartz.differentiable x).hasDerivAt
  have hL := (neutralIV098Left.differentiable x).hasDerivAt
  exact ((hR.const_mul u).add (hL.const_mul v)).deriv

theorem neutralIV098Pair_energy (u v : ℂ) :
    neutralIV096DerivativeEnergy (neutralIV098Pair u v) =
      (‖u‖^2 + ‖v‖^2) * neutralIV096DerivativeEnergy neutralIV097Schwartz := by
  let R := neutralIV097Schwartz
  let L := neutralIV098Left
  let p := deriv (R : ℝ → ℂ)
  let q := deriv (L : ℝ → ℂ)
  let dR := SchwartzMap.derivCLM ℂ ℂ R
  let dL := SchwartzMap.derivCLM ℂ ℂ L
  have hp : Integrable (fun x : ℝ => ‖p x‖^2) :=
    (memLp_two_iff_integrable_sq_norm dR.continuous.aestronglyMeasurable).mp (dR.memLp 2 volume)
  have hq : Integrable (fun x : ℝ => ‖q x‖^2) :=
    (memLp_two_iff_integrable_sq_norm dL.continuous.aestronglyMeasurable).mp (dL.memLp 2 volume)
  have hdis (x : ℝ) : p x = 0 ∨ q x = 0 := by
    change deriv (neutralIV097Schwartz : ℝ → ℂ) x = 0 ∨
      deriv (neutralIV098Left : ℝ → ℂ) x = 0
    rw [neutralIV097Schwartz_derivative, neutralIV098Left_derivative]
    exact neutralIV098Derivative_reflection_disjoint x
  have href : (∫ x : ℝ, ‖q x‖^2) = ∫ x : ℝ, ‖p x‖^2 := by
    calc
      _ = ∫ x : ℝ, ‖p (-x)‖^2 := by
        apply integral_congr_ae
        apply Filter.Eventually.of_forall
        intro x
        change ‖deriv (neutralIV098Left : ℝ → ℂ) x‖^2 =
          ‖deriv (neutralIV097Schwartz : ℝ → ℂ) (-x)‖^2
        rw [neutralIV098Left_derivative, neutralIV097Schwartz_derivative, norm_neg]
      _ = _ := neutralIV098Reflection_integral _
  unfold neutralIV096DerivativeEnergy
  simp_rw [neutralIV098Pair_derivative]
  change (∫ x : ℝ, ‖u * p x + v * q x‖^2) =
    (‖u‖^2 + ‖v‖^2) * (∫ x : ℝ, ‖p x‖^2)
  rw [neutralIV098Disjoint_integral_sq p q u v hp hq hdis, href]
  ring

theorem neutralIV098Pair_energy_ratio (u v : ℂ) :
    neutralIV096DerivativeEnergy (neutralIV098Pair u v) ≤
      16000000 * ‖(neutralIV098Pair u v).toLp 2 volume‖^2 := by
  rw [neutralIV098Pair_energy, neutralIV098Pair_mass]
  have h : neutralIV096DerivativeEnergy neutralIV097Schwartz ≤
      16000000 * ‖neutralIV097Schwartz.toLp 2 volume‖^2 := by
    linarith [neutralIV098Schwartz_energy_upper, neutralIV097Schwartz_mass_lower]
  calc
    _ ≤ (‖u‖^2 + ‖v‖^2) * (16000000 * ‖neutralIV097Schwartz.toLp 2 volume‖^2) :=
      mul_le_mul_of_nonneg_left h (by positivity)
    _ = _ := by ring

theorem neutralIV098ArithmeticCutoff : Real.exp (2*(11/10:ℝ)) < (10:ℝ) := by
  calc
    _ < Real.exp (Real.log (10:ℝ)) := by
      apply Real.exp_lt_exp.mpr
      rw [Real.log_ten_eq]
      linarith [Real.log_two_gt_d9, Real.log_five_gt_d9]
    _ = _ := Real.exp_log (by norm_num)

theorem neutralIV098Pair_margin (N : ℕ) (u v : ℂ) :
    ((2/5:ℝ) - 16000000 / ((N:ℝ)+1)^2) *
      ‖(neutralIV098Pair u v).toLp 2 volume‖^2 ≤
      neutralIV095FiniteDiagonal 10 N (neutralIV098Pair u v) := by
  let s := neutralIV098Pair u v
  have hf := neutralNF600SmoothCollarLower s (neutralIV098Pair_collars u v)
  have ht := neutralIV096CollarTail_derivative_bound 10 N s
    (neutralIV098Pair_collars u v) (by exact_mod_cast neutralIV098ArithmeticCutoff)
  have he := neutralIV098Pair_energy_ratio u v
  have hd : 0 < ((N:ℝ)+1)^2 := by positivity
  have hb : neutralIV096DerivativeEnergy s / ((N:ℝ)+1)^2 ≤
      (16000000 / ((N:ℝ)+1)^2) * ‖s.toLp 2 volume‖^2 := by
    rw [div_mul_eq_mul_div]
    exact div_le_div_of_nonneg_right he hd.le
  change neutralNF598SmoothWeil s - neutralIV095FiniteDiagonal 10 N s ≤ _ at ht
  change ((2/5:ℝ) - 16000000 / ((N:ℝ)+1)^2) * ‖s.toLp 2 volume‖^2 ≤
    neutralIV095FiniteDiagonal 10 N s
  rw [sub_mul]
  linarith

theorem neutralIV098Pair_cutoff8944 (N : ℕ) (hN : 8944 ≤ N) (u v : ℂ) :
    (1/5:ℝ) * ‖(neutralIV098Pair u v).toLp 2 volume‖^2 ≤
      neutralIV095FiniteDiagonal 10 N (neutralIV098Pair u v) := by
  have hn : (8944:ℝ) ≤ (N:ℝ) := by exact_mod_cast hN
  have hsq : (8945:ℝ)^2 ≤ ((N:ℝ)+1)^2 :=
    pow_le_pow_left₀ (by norm_num) (by linarith) 2
  have h : (16000000:ℝ) / ((N:ℝ)+1)^2 ≤ 1/5 := by
    apply (div_le_iff₀ (by positivity)).mpr
    linarith
  exact (mul_le_mul_of_nonneg_right (show (1/5:ℝ) ≤ 2/5 - 16000000 / ((N:ℝ)+1)^2 by linarith)
    (sq_nonneg _)).trans (neutralIV098Pair_margin N u v)

theorem neutralIV098Pair_cutoff20000 (N : ℕ) (hN : 20000 ≤ N) (u v : ℂ) :
    (9/25:ℝ) * ‖(neutralIV098Pair u v).toLp 2 volume‖^2 ≤
      neutralIV095FiniteDiagonal 10 N (neutralIV098Pair u v) := by
  have hn : (20000:ℝ) ≤ (N:ℝ) := by exact_mod_cast hN
  have hsq : (20001:ℝ)^2 ≤ ((N:ℝ)+1)^2 :=
    pow_le_pow_left₀ (by norm_num) (by linarith) 2
  have h : (16000000:ℝ) / ((N:ℝ)+1)^2 ≤ 1/25 := by
    apply (div_le_iff₀ (by positivity)).mpr
    linarith
  exact (mul_le_mul_of_nonneg_right (show (9/25:ℝ) ≤ 2/5 - 16000000 / ((N:ℝ)+1)^2 by linarith)
    (sq_nonneg _)).trans (neutralIV098Pair_margin N u v)

theorem neutralIV098Pair_mass_zero_iff (u v : ℂ) :
    ‖(neutralIV098Pair u v).toLp 2 volume‖^2 = 0 ↔ u = 0 ∧ v = 0 := by
  rw [neutralIV098Pair_mass]
  have hm : 0 < ‖neutralIV097Schwartz.toLp 2 volume‖^2 :=
    lt_of_lt_of_le (by norm_num) neutralIV097Schwartz_mass_lower
  constructor
  · intro h
    have hsum : ‖u‖^2 + ‖v‖^2 = 0 := (mul_eq_zero.mp h).resolve_right hm.ne'
    have hu2 : ‖u‖^2 = 0 := le_antisymm (by linarith [sq_nonneg ‖v‖]) (sq_nonneg _)
    have hv2 : ‖v‖^2 = 0 := le_antisymm (by linarith [sq_nonneg ‖u‖]) (sq_nonneg _)
    have hu : ‖u‖ = 0 := by simpa using (pow_eq_zero hu2)
    have hv : ‖v‖ = 0 := by simpa using (pow_eq_zero hv2)
    exact ⟨norm_eq_zero.mp hu, norm_eq_zero.mp hv⟩
  · rintro ⟨rfl, rfl⟩
    simp

#print axioms neutralIV098Pair_mass
#print axioms neutralIV098Pair_derivative
#print axioms neutralIV098Pair_energy
#print axioms neutralIV098Pair_energy_ratio
#print axioms neutralIV098ArithmeticCutoff
#print axioms neutralIV098Pair_margin
#print axioms neutralIV098Pair_cutoff8944
#print axioms neutralIV098Pair_cutoff20000
#print axioms neutralIV098Pair_mass_zero_iff

end
end WeilDefect
