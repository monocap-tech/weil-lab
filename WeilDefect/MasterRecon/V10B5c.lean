import WeilDefect.MasterRecon.V10B5b
import WeilDefect.MasterRecon.V10B4f

/-! V10B5c: restore the literal angular ordinate in the Mellin
slice estimate. The Fourier-to-ordinate Jacobian is 2π, not 1.
Outer rectangle integrability and arithmetic count attachment remain
separate. This source is staged, not yet natively verified. -/
namespace WeilDefect.MasterRecon.V10B5c

open Set MeasureTheory
open scoped ENNReal Interval BigOperators

theorem real_energy_of_lintegral (F : ℝ → ℝ) (hF : Continuous F)
    (h0 : ∀ u, 0 ≤ F u) (B : ℝ) (hB : 0 ≤ B)
    (hb : (∫⁻ u, ENNReal.ofReal (F u)) ≤ ENNReal.ofReal B) :
    Integrable F ∧ (∫ u, F u) ≤ B := by
  have hfi : HasFiniteIntegral F volume := by
    change (∫⁻ u, ‖F u‖ₑ) < ⊤
    have he : (∫⁻ u, ‖F u‖ₑ) = ∫⁻ u, ENNReal.ofReal (F u) := by
      apply lintegral_congr
      intro u
      rw [← ofReal_norm, Real.norm_eq_abs, abs_of_nonneg (h0 u)]
    rw [he]
    exact lt_of_le_of_lt hb ENNReal.ofReal_lt_top
  have hi : Integrable F := ⟨hF.aestronglyMeasurable, hfi⟩
  refine ⟨hi, ?_⟩
  rw [← ofReal_integral_eq_lintegral_ofReal hi (ae_of_all _ h0)] at hb
  have h := ENNReal.toReal_mono ENNReal.ofReal_ne_top hb
  simpa only [ENNReal.toReal_ofReal (integral_nonneg h0), ENNReal.toReal_ofReal hB] using h

theorem rescale_real_energy (F : ℝ → ℝ) (c : ℝ) (hc : c ≠ 0)
    (hi : Integrable (fun u => F (c*u))) :
    Integrable F ∧ (∫ y, F y) = |c| * (∫ u, F (c*u)) := by
  have h' := hi.comp_mul_left' (R := c⁻¹) (inv_ne_zero hc)
  have hF : Integrable F := by
    convert h' using 1
    funext y
    rw [← mul_assoc, mul_inv_cancel₀ hc, one_mul]
  refine ⟨hF, ?_⟩
  rw [Measure.integral_comp_mul_left F c, smul_eq_mul, abs_inv, ← mul_assoc,
    mul_inv_cancel₀ (abs_ne_zero.mpr hc), one_mul]

noncomputable def comparisonConstant : ℝ :=
  1 + Real.log (2*Real.pi)/Real.log 2

theorem comparisonConstant_nonneg : 0 ≤ comparisonConstant := by
  unfold comparisonConstant
  have h : 1 ≤ 2*Real.pi := by linarith [Real.pi_gt_three]
  exact add_nonneg (by norm_num)
    (div_nonneg (Real.log_nonneg h) (Real.log_pos (by norm_num)).le)

theorem weight_continuous : Continuous V10B3a.weight := by
  unfold V10B3a.weight
  apply Continuous.log (by fun_prop)
  intro y
  linarith [abs_nonneg y]

noncomputable def angularMoment (t : ℝ) (g : V08I.logCarrier t)
    (j : ℕ) (s y : ℝ) : ℂ :=
  V07A.mellin (V10B4f.momentInput (V08I.physicalInclusion t g : ℝ → ℂ) j)
    ((s : ℂ) + (y : ℂ) * Complex.I)

theorem angularMoment_continuous (t : ℝ) (ht : 0 ≤ t)
    (g : V08I.logCarrier t) (j : ℕ) : Continuous (fun p : ℝ × ℝ =>
      angularMoment t g j p.1 p.2) := by
  let f := V08I.physicalInclusion t g
  have hf := V08K.supported_integrable t f (V08I.physicalInclusion_support t g)
  have hM : Differentiable ℂ (V07A.mellin (V10B4f.momentInput (f : ℝ → ℂ) j)) :=
    fun z => (V10B4f.moment_derivative t ht _ hf
      (V08I.physicalInclusion_support t g) j z).differentiableAt
  exact hM.continuous.comp (show Continuous (fun p : ℝ × ℝ =>
    (p.1 : ℂ) + (p.2 : ℂ) * Complex.I) by fun_prop)

theorem angular_slice_energy (t : ℝ) (ht : 0 ≤ t) (j : ℕ) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ s ∈ Icc (-(1/2):ℝ) (1/2),
      ∀ g : V08I.logCarrier t,
      Integrable (fun y => V10B3a.weight y * ‖angularMoment t g j s y‖^2) ∧
      (∫ y, V10B3a.weight y * ‖angularMoment t g j s y‖^2) ≤ C * ‖g‖^2 := by
  obtain ⟨D, hD, hD'⟩ := V10B4f.carrier_multiplier_energy t ht j
  let c : ℝ := -(2*Real.pi)
  have hc : c ≠ 0 := neg_ne_zero.mpr (by positivity)
  have hcp : |c| = 2*Real.pi := by
    dsimp [c]
    rw [abs_neg, abs_of_pos (by positivity : 0 < 2*Real.pi)]
  refine ⟨2*Real.pi*comparisonConstant*D.toReal, by
    exact mul_nonneg (mul_nonneg (by positivity) comparisonConstant_nonneg) ENNReal.toReal_nonneg, ?_⟩
  intro s hs g
  let M := angularMoment t g j s
  let F : ℝ → ℝ := fun y => V10B3a.weight y * ‖M y‖^2
  let G : ℝ → ℝ := fun u => V10B3a.weight u * ‖M (c*u)‖^2
  have hM : Continuous M :=
    (angularMoment_continuous t ht g j).comp (continuous_const.prodMk continuous_id)
  have hF : Continuous F := weight_continuous.mul (hM.norm.pow 2)
  have hG : Continuous G := weight_continuous.mul ((hM.comp
    (continuous_const.mul continuous_id)).norm.pow 2)
  have harg (u : ℝ) : M (c*u) =
      V07A.mellin (V10B4f.momentInput (V08I.physicalInclusion t g : ℝ → ℂ) j)
        ((s : ℂ) - (2*Real.pi*u : ℝ) * Complex.I) := by
    unfold M angularMoment c
    congr 1
    push_cast
    ring
  have hb := hD' s hs g
  simp only [V10B4f.weightedNorm_square] at hb
  have he : D * ENNReal.ofReal (‖g‖^2) =
      ENNReal.ofReal (D.toReal * ‖g‖^2) := by
    rw [ENNReal.ofReal_mul ENNReal.toReal_nonneg, ENNReal.ofReal_toReal hD]
  have hb' : (∫⁻ u, ENNReal.ofReal (G u)) ≤
      ENNReal.ofReal (D.toReal * ‖g‖^2) := by
    simpa only [G, harg, ← he] using hb
  obtain ⟨hi, hbound⟩ := real_energy_of_lintegral G hG
    (fun u => mul_nonneg (V10B3a.weight_pos u).le (sq_nonneg _)) _
    (mul_nonneg ENNReal.toReal_nonneg (sq_nonneg _)) hb'
  have hw (u : ℝ) : V10B3a.weight (c*u) = V08I.logWeight u := by
    unfold V10B3a.weight V08I.logWeight c
    rw [neg_mul, abs_neg]
  have hdom (u : ℝ) : F (c*u) ≤ comparisonConstant * G u := by
    dsimp [F, G]
    rw [hw]
    calc
      _ ≤ (comparisonConstant * V10B3a.weight u) * ‖M (c*u)‖^2 :=
        mul_le_mul_of_nonneg_right (V10B4f.carrier_le_weight u) (sq_nonneg _)
      _ = _ := by ring
  have hfc : Continuous (fun u => F (c*u)) :=
    hF.comp (continuous_const.mul continuous_id)
  have hfi : Integrable (fun u => F (c*u)) := by
    apply (hi.const_mul comparisonConstant).mono' hfc.aestronglyMeasurable
    filter_upwards with u
    rw [Real.norm_eq_abs, abs_of_nonneg
      (show 0 ≤ F (c*u) from mul_nonneg (V10B3a.weight_pos _).le (sq_nonneg _))]
    exact hdom u
  obtain ⟨hreal, hscale⟩ := rescale_real_energy F c hc hfi
  change Integrable F ∧ (∫ y, F y) ≤ _ 
  refine ⟨hreal, ?_⟩
  calc
    _ = |c| * (∫ u, F (c*u)) := hscale
    _ ≤ |c| * (∫ u, comparisonConstant * G u) :=
      mul_le_mul_of_nonneg_left (integral_mono hfi (hi.const_mul _) hdom) (abs_nonneg _)
    _ = 2*Real.pi*comparisonConstant * (∫ u, G u) := by
      rw [hcp, integral_const_mul]
      ring
    _ ≤ (2*Real.pi*comparisonConstant) * (D.toReal * ‖g‖^2) :=
      mul_le_mul_of_nonneg_left hbound
        (mul_nonneg (by positivity) comparisonConstant_nonneg)
    _ = _ := by ring


/-- The four rectangle fields are the first three literal Mellin
moments, with the two vertical derivatives carrying a factor I. -/
theorem angular_rectangle_budget (t : ℝ) (ht : 0 ≤ t) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ (g : V08I.logCarrier t) (J : Finset ℤ),
      (∀ n ∈ J, IntervalIntegrable (fun s =>
        V10B2.rowEnergy (angularMoment t g 0)
          (fun x y => Complex.I * angularMoment t g 1 x y) (n : ℝ) s +
        V10B2.rowEnergy (angularMoment t g 1)
          (fun x y => Complex.I * angularMoment t g 2 x y) (n : ℝ) s)
        volume (-(1/2):ℝ) (-(1/2)+1)) →
      (∑ n ∈ J, Real.log (|(n : ℝ)|+3) *
        V10B2.rectangleEnergy (angularMoment t g 0) (angularMoment t g 1)
          (fun x y => Complex.I * angularMoment t g 1 x y)
          (fun x y => Complex.I * angularMoment t g 2 x y)
          (-(1/2):ℝ) (n : ℝ)) ≤ C * ‖g‖^2 := by
  obtain ⟨C₀,h₀,h₀'⟩ := angular_slice_energy t ht 0
  obtain ⟨C₁,h₁,h₁'⟩ := angular_slice_energy t ht 1
  obtain ⟨C₂,h₂,h₂'⟩ := angular_slice_energy t ht 2
  refine ⟨2*(C₀+2*C₁+C₂), by positivity, ?_⟩
  intro g J houter
  let H := angularMoment t g 0
  let X := angularMoment t g 1
  let Y := fun s y => Complex.I * X s y
  let Z := fun s y => Complex.I * angularMoment t g 2 s y
  let B := (C₀+2*C₁+C₂)*‖g‖^2
  have hslice (j : ℕ) (s : ℝ) : Continuous (angularMoment t g j s) :=
    (angularMoment_continuous t ht g j).comp (continuous_const.prodMk continuous_id)
  have hnormY (s y : ℝ) : ‖Y s y‖ = ‖X s y‖ := by
    simp [Y, norm_mul, Complex.norm_I]
  have hnormZ (s y : ℝ) : ‖Z s y‖ = ‖angularMoment t g 2 s y‖ := by
    simp [Z, norm_mul, Complex.norm_I]
  have hstrip (s : ℝ) (hs : s ∈ Icc (-(1/2):ℝ) (-(1/2)+1)) :
      s ∈ Icc (-(1/2):ℝ) (1/2) := by
    convert hs using 1 <;> norm_num
  have hh (s : ℝ) : Continuous (fun y => ‖H s y‖^2 + ‖Y s y‖^2) := by
    simp only [hnormY]
    exact ((hslice 0 s).norm.pow 2).add ((hslice 1 s).norm.pow 2)
  have hx (s : ℝ) : Continuous (fun y => ‖X s y‖^2 + ‖Z s y‖^2) := by
    simp only [hnormZ]
    exact ((hslice 1 s).norm.pow 2).add ((hslice 2 s).norm.pow 2)
  have hi (s : ℝ) (hs : s ∈ Icc (-(1/2):ℝ) (-(1/2)+1)) :
      Integrable (fun y => V10B3a.weight y * (‖H s y‖^2 + ‖Y s y‖^2)) := by
    simp only [hnormY, mul_add]
    exact (h₀' s (hstrip s hs) g).1.add (h₁' s (hstrip s hs) g).1
  have hj (s : ℝ) (hs : s ∈ Icc (-(1/2):ℝ) (-(1/2)+1)) :
      Integrable (fun y => V10B3a.weight y * (‖X s y‖^2 + ‖Z s y‖^2)) := by
    simp only [hnormZ, mul_add]
    exact (h₁' s (hstrip s hs) g).1.add (h₂' s (hstrip s hs) g).1
  have hb (s : ℝ) (hs : s ∈ Icc (-(1/2):ℝ) (-(1/2)+1)) :
      (∫ y, V10B3a.weight y * (‖H s y‖^2 + ‖Y s y‖^2)) +
      (∫ y, V10B3a.weight y * (‖X s y‖^2 + ‖Z s y‖^2)) ≤ B := by
    obtain ⟨i₀,b₀⟩ := h₀' s (hstrip s hs) g
    obtain ⟨i₁,b₁⟩ := h₁' s (hstrip s hs) g
    obtain ⟨i₂,b₂⟩ := h₂' s (hstrip s hs) g
    simp only [hnormY, hnormZ, mul_add]
    change (∫ y, V10B3a.weight y * ‖angularMoment t g 0 s y‖^2 +
        V10B3a.weight y * ‖angularMoment t g 1 s y‖^2) +
      (∫ y, V10B3a.weight y * ‖angularMoment t g 1 s y‖^2 +
        V10B3a.weight y * ‖angularMoment t g 2 s y‖^2) ≤ B
    rw [integral_add i₀ i₁, integral_add i₁ i₂]
    dsimp [B]
    linarith only [b₀,b₁,b₂]
  have h := V10B5b.rectangle_budget H X Y Z (-(1/2):ℝ) B J hh hx hi hj houter hb
  exact h.trans (le_of_eq (by dsimp [B]; ring))

end WeilDefect.MasterRecon.V10B5c

#print axioms WeilDefect.MasterRecon.V10B5c.real_energy_of_lintegral
#print axioms WeilDefect.MasterRecon.V10B5c.rescale_real_energy
#print axioms WeilDefect.MasterRecon.V10B5c.comparisonConstant_nonneg
#print axioms WeilDefect.MasterRecon.V10B5c.weight_continuous
#print axioms WeilDefect.MasterRecon.V10B5c.angularMoment_continuous
#print axioms WeilDefect.MasterRecon.V10B5c.angular_slice_energy

#print axioms WeilDefect.MasterRecon.V10B5c.angular_rectangle_budget
