import WeilDefect.MasterRecon.V10B17a
import WeilDefect.MasterRecon.V10B16c
import WeilDefect.MasterRecon.V10B8h

/-! A 16-vector small-support tail pilot (15 moments + one pole
difference). The transport norm product and literal symbol attachment
are explicit premises; the rational remainder test is internal. -/
namespace WeilDefect.MasterRecon.V10B17b

open MeasureTheory Set
open scoped InnerProduct FourierTransform BigOperators ComplexConjugate
open V08I (logCarrier FullL2 physicalInclusion)
open V10B13a (moment out input remainderBound)
open V10B17a (poleDifference)

noncomputable def bank : Fin 15 ⊕ Unit → logCarrier (1/4) :=
  Sum.elim (fun j => (moment (1/4) (by norm_num) j.val).adjoint 1)
    (fun _ => (poleDifference (1/4) (by norm_num)).adjoint 1)

noncomputable def retained : Submodule ℂ (logCarrier (1/4)) :=
  Submodule.span ℂ (Set.range bank)

theorem retained_finite : FiniteDimensional ℂ retained :=
  FiniteDimensional.span_of_finite ℂ (Set.finite_range bank)

theorem moment_subspace :
    V10B13b.retained (1/4) (by norm_num) 15 ≤ retained := by
  apply Submodule.span_le.mpr
  rintro _ ⟨j,rfl⟩
  exact Submodule.subset_span ⟨Sum.inl j,rfl⟩

theorem pole_zero (g : logCarrier (1/4)) (hg : g ∈ retainedᗮ) :
    poleDifference (1/4) (by norm_num) g = 0 := by
  have hm : (poleDifference (1/4) (by norm_num)).adjoint 1 ∈ retained :=
    Submodule.subset_span ⟨Sum.inr (),rfl⟩
  have h := hg _ hm
  rw [ContinuousLinearMap.adjoint_inner_left] at h
  change conj (1:ℂ)*poleDifference (1/4) (by norm_num) g = 0 at h
  simpa using h

theorem prime_free : V10B8d.physicalPrime (1/4) = 0 := by
  have he : Real.exp (2*(1/4:ℝ)) < 2 := by
    rw [← Real.exp_log (by norm_num : (0:ℝ)<2)]
    exact Real.exp_lt_exp.mpr (by linarith [Real.log_two_gt_d9])
  have hn : ⌊Real.exp (2*(1/4:ℝ))⌋₊ < 2 :=
    (Nat.floor_lt (Real.exp_pos _).le).mpr (by exact_mod_cast he)
  unfold V10B8d.physicalPrime
  apply Finset.sum_eq_zero
  intro n hn'
  have h := Finset.mem_Ioc.mp hn'
  have hn'' : n = 1 := by
    have hh : n ≤ ⌊Real.exp (2*(1/4:ℝ))⌋₊ := h.2
    omega
  subst n
  simp [V10B8d.primeWeight]

theorem ratio_test : (2*Real.pi*3)*(1/4)/((15:ℝ)+1) ≤ 1/2 := by
  linarith [Real.pi_lt_d2]

theorem rational_reserve :
    144*(2*((189:ℝ)/40)^15/(Nat.factorial 15:ℝ))^2 ≤ 1/8 := by
  norm_num [Nat.factorial]

theorem remainder_test :
    144*(remainderBound (1/4) 3 15)^2 ≤ 1/8 := by
  have h : (2*Real.pi*3)*(1/4) ≤ (189:ℝ)/40 := by linarith [Real.pi_lt_d2]
  have hp : ((2*Real.pi*3)*(1/4))^15 ≤ ((189:ℝ)/40)^15 :=
    pow_le_pow_left₀ (by positivity) h 15
  have hr : remainderBound (1/4) 3 15 ≤ 2*((189:ℝ)/40)^15/(Nat.factorial 15:ℝ) := by
    unfold remainderBound
    exact div_le_div_of_nonneg_right (mul_le_mul_of_nonneg_left hp (by norm_num)) (by positivity)
  have hs := (sq_le_sq₀ (by unfold remainderBound; positivity) (by positivity)).mpr hr
  linarith [rational_reserve]

theorem pilot_low_mass
    (hB : (‖out 3 (by norm_num)‖*‖input (1/4)‖)^2 ≤ 6)
    (g : logCarrier (1/4)) (hg : g ∈ retainedᗮ) :
    24*‖V08K.physicalCutoff (1/4) 3 (by norm_num) (by norm_num) g‖^2 ≤
      (1/8:ℝ)*‖g‖^2 := by
  have hm : g ∈ (V10B13b.retained (1/4) (by norm_num) 15)ᗮ :=
    fun x hx => hg x (moment_subspace hx)
  have h := V10B16c.low_band_bound (1/4) 3 (by norm_num) (by norm_num) 15
    ratio_test g hm
  have hh := (sq_le_sq₀ (norm_nonneg _) (by
    have hr : 0 ≤ remainderBound (1/4) 3 15 := by unfold remainderBound; positivity
    positivity)).mpr h
  rw [mul_pow,mul_pow,mul_pow] at hh
  have h1 := mul_le_mul_of_nonneg_right hB (sq_nonneg (remainderBound (1/4) 3 15))
  have h2 := mul_le_mul_of_nonneg_right
    (show 24*((‖out 3 (by norm_num)‖*‖input (1/4)‖)^2*
      (remainderBound (1/4) 3 15)^2) ≤ 1/8 by
      linarith only [h1,remainder_test]) (sq_nonneg ‖g‖)
  rw [mul_pow] at h2
  nlinarith only [hh,h2]

theorem pilot_tail
    (hd : Measurable V10B8e.residual) (hC : ∀ u, |V10B8e.residual u| ≤ 24)
    (hV : V10B8f.VerticalStirling)
    (hB : (‖out 3 (by norm_num)‖*‖input (1/4)‖)^2 ≤ 6)
    (ha : ∀ g : logCarrier (1/4), Integrable (fun u =>
      V10B8e.gammaSymbol u*‖(𝓕 (physicalInclusion (1/4) g) : FullL2) u‖^2))
    (hArch : ∀ g : logCarrier (1/4),
      (inner ℂ (V10B8e.archOperator (1/4) hd 24 hC g) g).re =
      ∫ u, V10B8e.gammaSymbol u*‖(𝓕 (physicalInclusion (1/4) g) : FullL2) u‖^2)
    (g : logCarrier (1/4)) (hg : g ∈ retainedᗮ) :
    (1/8:ℝ)*‖g‖^2 ≤
      (inner ℂ (V10B8h.arithmeticOperator (1/4) (by norm_num) hd 24 hC g) g).re := by
  let f : ℝ → ℂ := fun u => (𝓕 (physicalInclusion (1/4) g) : FullL2) u
  have hf : Integrable (fun u => ‖f u‖^2) :=
    (memLp_two_iff_integrable_sq_norm (Lp.aestronglyMeasurable
      (𝓕 (physicalInclusion (1/4) g) : FullL2))).mp (Lp.memLp _)
  have h := V10B17a.small_symbol_split hV hC f (ha g)
    (V08I.logCarrier_energy_integrable (1/4) g) hf
  rw [← V08I.logCarrier_energy (1/4) g,← V10B16c.low_band_mass (1/4) 3
    (by norm_num) (by norm_num) g,← hArch g] at h
  have hp := V10B17a.pole_nonneg_of_difference_zero (1/4) (by norm_num) g (pole_zero g hg)
  have hm := pilot_low_mass hB g hg
  unfold V10B8h.arithmeticOperator V10B8d.primeOperator
  rw [prime_free]
  simp only [ContinuousLinearMap.comp_zero,ContinuousLinearMap.zero_comp,sub_zero,
    ContinuousLinearMap.add_apply,inner_add_left,Complex.add_re]
  linarith only [h,hp,hm]

end WeilDefect.MasterRecon.V10B17b

#print axioms WeilDefect.MasterRecon.V10B17b.retained_finite
#print axioms WeilDefect.MasterRecon.V10B17b.moment_subspace
#print axioms WeilDefect.MasterRecon.V10B17b.pole_zero
#print axioms WeilDefect.MasterRecon.V10B17b.prime_free
#print axioms WeilDefect.MasterRecon.V10B17b.ratio_test
#print axioms WeilDefect.MasterRecon.V10B17b.rational_reserve
#print axioms WeilDefect.MasterRecon.V10B17b.remainder_test
#print axioms WeilDefect.MasterRecon.V10B17b.pilot_low_mass
#print axioms WeilDefect.MasterRecon.V10B17b.pilot_tail
