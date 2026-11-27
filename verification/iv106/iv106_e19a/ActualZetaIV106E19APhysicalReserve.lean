import WeilDefect.Arithmetic.ActualZetaIV106E19AExactTrialEnergy
import WeilDefect.Arithmetic.ActualZetaIV106E18VLiteralMatch

namespace WeilDefect
noncomputable section
open MeasureTheory Set FourierTransform
open scoped FourierTransform

/-- Full physical L² norm of a compact cell representative, with the
affine Jacobian and its literal pointwise squared profile. -/
theorem neutralIV106E19AAffine_square
    (l h : ℝ) (hh : 0 < h) (f : ℝ → ℂ) (hf : MemLp f 2 volume)
    (g : ℝ → ℝ)
    (hout : ∀ x ∉ Icc l (l+h), f x = 0)
    (hin : ∀ t ∈ Icc (0:ℝ) 1, ‖f (h*t+l)‖^2 = g t) :
    ‖hf.toLp f‖^2 = h*(∫ t in (0:ℝ)..1, g t) := by
  rw [neutralPhysicalL2_norm_sq]
  have he : (∫ x : ℝ, ‖hf.toLp f x‖^2) = ∫ x : ℝ, ‖f x‖^2 := by
    apply integral_congr_ae
    filter_upwards [hf.coeFn_toLp] with x hx
    rw [hx]
  rw [he, ← setIntegral_eq_integral_of_forall_compl_eq_zero
    (s := Icc l (l+h)) (f := fun x => ‖f x‖^2) (fun x hx => by simp [hout x hx]),
    integral_Icc_eq_integral_Ioc, ← intervalIntegral.integral_of_le (by linarith : l ≤ l+h)]
  let F : ℝ → ℝ := fun x => ‖f x‖^2
  have hchange : (∫ x in l..l+h, F x) =
      h • (∫ t in (0:ℝ)..1, F (h*t+l)) := by
    have hh' := intervalIntegral.smul_integral_comp_mul_add F
      (a := (0:ℝ)) (b := 1) h l
    simpa [add_comm] using hh'.symm
  change (∫ x in l..l+h, F x) = _
  rw [hchange,smul_eq_mul]
  congr 1
  apply intervalIntegral.integral_congr
  intro t ht
  rw [uIcc_of_le (by norm_num : (0:ℝ) ≤ 1)] at ht
  exact hin t ht

theorem neutralIV106E19AMass_physical (l : ℝ) :
    ‖(neutralIV106E18JTrial_memLp l (11/3325) (by norm_num)).toLp _‖^2 =
      12994320639248774641/98293908912022687500000 := by
  let h : ℝ := 11/3325
  have hh : 0 < h := by norm_num [h]
  have he := neutralIV106E19AAffine_square l h hh (neutralIV106E18ITrial l h)
    (neutralIV106E18JTrial_memLp l h hh) (fun t => (neutralIV106E18IPoly h t)^2)
    (neutralIV106E18ITrial_outside l h hh) (by
      intro t ht
      have hx : h*t+l ∈ Icc l (l+h) := by
        constructor
        · nlinarith [mul_nonneg hh.le ht.1]
        · nlinarith [mul_nonneg hh.le (sub_nonneg.mpr ht.2)]
      have ha : (h*t+l-l)/h = t := by field_simp [hh.ne'] <;> ring
      rw [neutralIV106E18ITrial_inside l h hh _ hx,ha,Complex.norm_real,
        Real.norm_eq_abs,sq_abs])
  exact he.trans neutralIV106E19AMass_unit

theorem neutralIV106E19ADerivative_physical (l : ℝ) :
    ‖(neutralIV106E18SDTrial_memLp l (11/3325) (by norm_num)).toLp _‖^2 =
      27926390440838204641/16514364829462500 := by
  let h : ℝ := 11/3325
  have hh : 0 < h := by norm_num [h]
  have he := neutralIV106E19AAffine_square l h hh (neutralIV106E18SDTrial l h)
    (neutralIV106E18SDTrial_memLp l h hh) (fun t => (neutralIV106E18SDPoly h t/h)^2)
    (neutralIV106E18SDTrial_outside l h hh) (by
      intro t ht
      have ha : (h*t+l-l)/h = t := by field_simp [hh.ne'] <;> ring
      unfold neutralIV106E18SDTrial
      rw [ha]
      simp only [neutralIV106E18SClip,min_eq_right ht.2,max_eq_right ht.1,
        Complex.norm_real,Real.norm_eq_abs,sq_abs])
  change ‖(neutralIV106E18SDTrial_memLp l h hh).toLp _‖^2 = _
  rw [he]
  have hi : (∫ t in (0:ℝ)..1, (neutralIV106E18SDPoly h t/h)^2) =
      (∫ t in (0:ℝ)..1, (neutralIV106E18SDPoly h t)^2)/h^2 := by
    simp only [div_pow,intervalIntegral.integral_div]
  rw [hi]
  have hu : h*((∫ t in (0:ℝ)..1, (neutralIV106E18SDPoly h t)^2)/h^2) =
      (∫ t in (0:ℝ)..1, (neutralIV106E18SDPoly h t)^2)/h := by
    field_simp [hh.ne'] <;> ring
  rw [hu]
  exact neutralIV106E19ADerivative_unit

/-- Uniform reserve on any original carrier representative of a literal
cell, using the actual Fourier graph bound. The explicit exponential
upper premise is kept separate to make the scalar dependency visible. -/
theorem neutralIV106E19ACarrier_bound (a l b : ℝ) (hb : 0 < b)
    (p : NeutralLogHilbertCarrier a)
    (hp : neutralLogPhysical p.val =
      (neutralIV106E18JTrial_memLp l (11/3325) (by norm_num)).toLp _)
    (hexp : Real.exp 1+1 ≤ 4) :
    ‖p‖ < 7 := by
  let h : ℝ := 11/3325
  have hh : 0 < h := by norm_num [h]
  have he := neutralIV106E18VEnergy (l-b) (l+h+b)
    ((neutralIV106E18JTrial_memLp l h hh).toLp _)
    ((neutralIV106E18SDTrial_memLp l h hh).toLp _)
    (neutralIV106E18VTrial_graph l h b hh hb)
  change (∫ ξ, logarithmicFourierWeight ξ *
    ‖(𝓕 ((neutralIV106E18JTrial_memLp l (11/3325) (by norm_num)).toLp _) :
      RealComplexL2) ξ‖^2) ≤ _ at he
  change _ ≤ (Real.exp 1+1)*
    ‖(neutralIV106E18JTrial_memLp l (11/3325) (by norm_num)).toLp _‖^2+
      ‖neutralIV106E18VScale‖^2*
    ‖(neutralIV106E18SDTrial_memLp l (11/3325) (by norm_num)).toLp _‖^2 at he
  rw [neutralIV106E19AMass_physical,neutralIV106E19ADerivative_physical,
    neutralIV106E18VScale_sq] at he
  have hpi : (1:ℝ)/(4*Real.pi^2) ≤ 1/36 := by
    apply (div_le_div_iff₀ (by positivity) (by norm_num : (0:ℝ)<36)).mpr
    nlinarith [Real.pi_gt_three, sq_nonneg (Real.pi-3)]
  have hr := neutralIV106E19ARational_reserve
  have hmass := mul_le_mul_of_nonneg_right hexp
    (by norm_num : (0:ℝ) ≤ 12994320639248774641/98293908912022687500000)
  have hd := mul_le_mul_of_nonneg_right hpi
    (by norm_num : (0:ℝ) ≤ 27926390440838204641/16514364829462500)
  have hsq : ‖p‖^2 < 49 := by
    rw [neutralLogHilbertCarrier_norm_sq,hp]
    linarith only [he,hr,hmass,hd]
  nlinarith [norm_nonneg p]

#print axioms neutralIV106E19AAffine_square
#print axioms neutralIV106E19AMass_physical
#print axioms neutralIV106E19ADerivative_physical
#print axioms neutralIV106E19ACarrier_bound
end
end WeilDefect
