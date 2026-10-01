import WeilDefect.Morphology.NeutralWeilSourceFormDomain

namespace WeilDefect

noncomputable section

open MeasureTheory FourierTransform
open scoped SchwartzMap ComplexConjugate FourierTransform

/-- Mixed energy is genuinely integrable, not merely a totalized integral.
The two diagonal absolute-symbol energies suffice by the elementary square
bound. No assertion about arbitrary compact L2 vectors is made. -/
theorem integrable_mixedMultiplier
    (m : ℝ → ℝ) (hm : AEStronglyMeasurable m volume)
    (F G : ℝ → ℂ)
    (hF : AEStronglyMeasurable F volume)
    (hG : AEStronglyMeasurable G volume)
    (eF : Integrable (fun x => |m x| * ‖F x‖ ^ 2) volume)
    (eG : Integrable (fun x => |m x| * ‖G x‖ ^ 2) volume) :
    Integrable (fun x => conj (F x) * (m x : ℂ) * G x) volume := by
  apply (eF.add eG).mono'
  · exact ((Complex.continuous_conj.comp_aestronglyMeasurable hF).mul
      (Complex.continuous_ofReal.comp_aestronglyMeasurable hm)).mul hG
  · filter_upwards [] with x
    simp only [norm_mul, Complex.norm_conj, Complex.norm_real, Real.norm_eq_abs,
      Pi.add_apply]
    have hs : ‖F x‖ * ‖G x‖ ≤ ‖F x‖ ^ 2 + ‖G x‖ ^ 2 := by
      nlinarith [sq_nonneg (‖F x‖ - ‖G x‖), sq_nonneg ‖F x‖, sq_nonneg ‖G x‖]
    nlinarith [mul_le_mul_of_nonneg_left hs (abs_nonneg (m x))]

variable {c : ℝ} {EndpointObs RightObs : Type*}
  [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
  [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]

variable {carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs}
  {a : ℝ}

/-- Transfer the retained log-energy hypothesis using the explicit EXT5 upper
bound. The bound and the domain witness remain visible source inputs. -/
theorem NeutralSourceFormDomainAttachment.absoluteSymbolEnergy
    (D : NeutralSourceFormDomainAttachment carrier a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (C : ℝ)
    (hbound : ∀ ξ, |rightLimitCompactWeilSymbolMathlib a ξ| ≤
      C * logarithmicFourierWeight ξ) (f : D.domain) :
    Integrable (fun ξ => |rightLimitCompactWeilSymbolMathlib a ξ| *
      ‖(𝓕 f.val : RealComplexL2) ξ‖ ^ 2) volume := by
  have hm : Continuous (rightLimitCompactWeilSymbolMathlib a) :=
    Complex.continuous_re.comp hSymbol.hasTemperateGrowth.1.continuous
  apply ((D.logEnergy f).const_mul C).mono'
  · exact hm.abs.aestronglyMeasurable.mul
      ((Lp.aestronglyMeasurable (𝓕 f.val : RealComplexL2)).norm.pow 2)
  · filter_upwards [] with ξ
    rw [Real.norm_eq_abs, abs_of_nonneg
      (mul_nonneg (abs_nonneg _) (sq_nonneg _))]
    simpa only [mul_assoc] using mul_le_mul_of_nonneg_right
      (hbound ξ) (sq_nonneg ‖(𝓕 f.val : RealComplexL2) ξ‖)

/-- Genuine convergence of the actual normalized multiplier pairing on the
retained source domain. -/
theorem NeutralSourceFormDomainAttachment.mixedMultiplier_integrable
    (D : NeutralSourceFormDomainAttachment carrier a)
    (hSymbol : RightLimitWeilSymbolTemperatePremise a)
    (C : ℝ)
    (hbound : ∀ ξ, |rightLimitCompactWeilSymbolMathlib a ξ| ≤
      C * logarithmicFourierWeight ξ) (f g : D.domain) :
    Integrable (fun ξ => conj ((𝓕 f.val : RealComplexL2) ξ) *
      (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
      (𝓕 g.val : RealComplexL2) ξ) volume := by
  apply integrable_mixedMultiplier
  · exact (Complex.continuous_re.comp
      hSymbol.hasTemperateGrowth.1.continuous).aestronglyMeasurable
  · exact Lp.aestronglyMeasurable _
  · exact Lp.aestronglyMeasurable _
  · exact D.absoluteSymbolEnergy hSymbol C hbound f
  · exact D.absoluteSymbolEnergy hSymbol C hbound g

/-- The actual normalized multiplier integral; its linear laws below use the
mixed convergence theorem and Lp a.e. representative laws. -/
def sourceDomainMultiplierPairing
    (D : NeutralSourceFormDomainAttachment carrier a) (f g : D.domain) : ℂ :=
  ∫ ξ, conj ((𝓕 f.val : RealComplexL2) ξ) *
    (rightLimitCompactWeilSymbolMathlib a ξ : ℂ) *
    (𝓕 g.val : RealComplexL2) ξ

variable (D : NeutralSourceFormDomainAttachment carrier a)
  (hSymbol : RightLimitWeilSymbolTemperatePremise a) (C : ℝ)
  (hbound : ∀ ξ, |rightLimitCompactWeilSymbolMathlib a ξ| ≤
    C * logarithmicFourierWeight ξ)

include hSymbol C hbound in
theorem sourceDomainMultiplierPairing_add_right (f g k : D.domain) :
    sourceDomainMultiplierPairing D f (g + k) =
      sourceDomainMultiplierPairing D f g + sourceDomainMultiplierPairing D f k := by
  unfold sourceDomainMultiplierPairing
  rw [← integral_add (D.mixedMultiplier_integrable hSymbol C hbound f g)
    (D.mixedMultiplier_integrable hSymbol C hbound f k)]
  apply integral_congr_ae
  have hae := Lp.coeFn_add (𝓕 g.val : RealComplexL2) (𝓕 k.val : RealComplexL2)
  filter_upwards [hae] with ξ hξ
  have hFourier : (𝓕 (g + k).val : RealComplexL2) = 𝓕 g.val + 𝓕 k.val :=
    (Lp.fourierTransformₗᵢ ℝ ℂ).map_add g.val k.val
  rw [hFourier, hξ]
  simp only [Pi.add_apply, mul_add]

include hSymbol C hbound in
theorem sourceDomainMultiplierPairing_add_left (f g k : D.domain) :
    sourceDomainMultiplierPairing D (f + g) k =
      sourceDomainMultiplierPairing D f k + sourceDomainMultiplierPairing D g k := by
  unfold sourceDomainMultiplierPairing
  rw [← integral_add (D.mixedMultiplier_integrable hSymbol C hbound f k)
    (D.mixedMultiplier_integrable hSymbol C hbound g k)]
  apply integral_congr_ae
  have hae := Lp.coeFn_add (𝓕 f.val : RealComplexL2) (𝓕 g.val : RealComplexL2)
  filter_upwards [hae] with ξ hξ
  have hFourier : (𝓕 (f + g).val : RealComplexL2) = 𝓕 f.val + 𝓕 g.val :=
    (Lp.fourierTransformₗᵢ ℝ ℂ).map_add f.val g.val
  rw [hFourier, hξ]
  simp only [Pi.add_apply, map_add, add_mul]

theorem sourceDomainMultiplierPairing_smul_right (z : ℂ) (f g : D.domain) :
    sourceDomainMultiplierPairing D f (z • g) =
      z * sourceDomainMultiplierPairing D f g := by
  unfold sourceDomainMultiplierPairing
  rw [← integral_const_mul]
  apply integral_congr_ae
  have hae := Lp.coeFn_smul z (𝓕 g.val : RealComplexL2)
  filter_upwards [hae] with ξ hξ
  simp only [Submodule.coe_smul, fourier_smul, hξ, Pi.smul_apply, smul_eq_mul]
  ring

theorem sourceDomainMultiplierPairing_smul_left (z : ℂ) (f g : D.domain) :
    sourceDomainMultiplierPairing D (z • f) g =
      conj z * sourceDomainMultiplierPairing D f g := by
  unfold sourceDomainMultiplierPairing
  rw [← integral_const_mul]
  apply integral_congr_ae
  have hae := Lp.coeFn_smul z (𝓕 f.val : RealComplexL2)
  filter_upwards [hae] with ξ hξ
  simp only [Submodule.coe_smul, fourier_smul, hξ, Pi.smul_apply, smul_eq_mul, map_mul]
  ring

/-- The normalized multiplier is now an actual sesquilinear form on the
retained domain, not an abstract form variable. -/
def sourceDomainMultiplierForm : D.domain →ₗ⋆[ℂ] D.domain →ₗ[ℂ] ℂ where
  toFun f :=
    { toFun := sourceDomainMultiplierPairing D f
      map_add' := sourceDomainMultiplierPairing_add_right D hSymbol C hbound f
      map_smul' := fun z g => by
        simpa using sourceDomainMultiplierPairing_smul_right D z f g }
  map_add' f g := by
    ext k
    exact sourceDomainMultiplierPairing_add_left D hSymbol C hbound f g k
  map_smul' z f := by
    ext g
    simpa using sourceDomainMultiplierPairing_smul_left D z f g

/-- Compact-window exponential moments converge for every L2 representative.
This claim is only about a restricted integral, not a global exponential
moment of an arbitrary L2 function. -/
theorem sourceWindowMoment_integrable (b s : ℝ) (f : RealComplexL2) :
    IntegrableOn (fun x => f x * (Real.exp (s * x) : ℂ)) (Set.Icc (-b) b) volume := by
  exact ((Lp.memLp f).locallyIntegrable (by norm_num)).integrableOn_isCompact
    isCompact_Icc |>.mul_continuousOn (by fun_prop) isCompact_Icc

/-- A genuine complex-linear moment of the L2 equivalence class. -/
def sourceWindowMoment (b s : ℝ) : RealComplexL2 →ₗ[ℂ] ℂ where
  toFun f := ∫ x in Set.Icc (-b) b, f x * (Real.exp (s * x) : ℂ)
  map_add' f g := by
    rw [← integral_add (sourceWindowMoment_integrable b s f)
      (sourceWindowMoment_integrable b s g)]
    apply integral_congr_ae
    filter_upwards [ae_restrict_of_ae (Lp.coeFn_add f g)] with x hx
    simp only [hx, Pi.add_apply, add_mul]
  map_smul' z f := by
    change (∫ x in Set.Icc (-b) b, (z • f) x * (Real.exp (s * x) : ℂ)) =
      z * ∫ x in Set.Icc (-b) b, f x * (Real.exp (s * x) : ℂ)
    rw [← integral_const_mul]
    apply integral_congr_ae
    filter_upwards [ae_restrict_of_ae (Lp.coeFn_smul z f)] with x hx
    simp only [hx, Pi.smul_apply, smul_eq_mul, mul_assoc]

/-- Enlargement of the pole integration window does not change the actual
carrier's named source moments. This is a support identity, not threshold
bookkeeping or an assumption of new form-domain membership. -/
theorem sourceWindowMoment_carrier (hca : c ≤ a) (s : ℝ) :
    sourceWindowMoment a s carrier.l2Mode = neutralWeilPoleMoment carrier s := by
  change (∫ x in Set.Icc (-a) a,
    carrier.l2Mode x * (Real.exp (s * x) : ℂ)) = _
  rw [show (∫ x in Set.Icc (-a) a,
      carrier.l2Mode x * (Real.exp (s * x) : ℂ)) =
      ∫ x in Set.Icc (-a) a, carrier.h x * (Real.exp (s * x) : ℂ) from by
    apply integral_congr_ae
    filter_upwards [ae_restrict_of_ae carrier.h_memLp.coeFn_toLp] with x hx
    rw [NeutralPhysicalFourierCarrier.l2Mode, hx]]
  apply setIntegral_eq_of_subset_of_ae_sdiff_eq_zero
    measurableSet_Icc.nullMeasurableSet
  · exact Set.Icc_subset_Icc (neg_le_neg hca) hca
  · filter_upwards [] with x hx
    have hz : carrier.h x = 0 := by
      by_contra hn
      exact hx.2 (carrier.support_subset hn)
    simp only [hz, zero_mul]

/-- The two pole cross terms, restricted to the exact retained domain. -/
def sourceDomainPoleForm : D.domain →ₗ⋆[ℂ] D.domain →ₗ[ℂ] ℂ where
  toFun f :=
    { toFun := fun g =>
        conj (sourceWindowMoment a (-(1 / 2)) f.val) * sourceWindowMoment a (1 / 2) g.val +
        conj (sourceWindowMoment a (1 / 2) f.val) * sourceWindowMoment a (-(1 / 2)) g.val
      map_add' := by intros; simp only [Submodule.coe_add, map_add]; ring
      map_smul' := by
        intros
        simp only [Submodule.coe_smul, map_smul, smul_eq_mul, RingHom.id_apply]
        ring }
  map_add' f g := by
    ext k
    change
      conj (sourceWindowMoment a (-(1 / 2)) (f + g).val) * sourceWindowMoment a (1 / 2) k.val +
      conj (sourceWindowMoment a (1 / 2) (f + g).val) * sourceWindowMoment a (-(1 / 2)) k.val =
      (conj (sourceWindowMoment a (-(1 / 2)) f.val) * sourceWindowMoment a (1 / 2) k.val +
       conj (sourceWindowMoment a (1 / 2) f.val) * sourceWindowMoment a (-(1 / 2)) k.val) +
      (conj (sourceWindowMoment a (-(1 / 2)) g.val) * sourceWindowMoment a (1 / 2) k.val +
       conj (sourceWindowMoment a (1 / 2) g.val) * sourceWindowMoment a (-(1 / 2)) k.val)
    simp only [Submodule.coe_add, map_add]
    ring
  map_smul' z f := by
    ext k
    change
      conj (sourceWindowMoment a (-(1 / 2)) (z • f).val) * sourceWindowMoment a (1 / 2) k.val +
      conj (sourceWindowMoment a (1 / 2) (z • f).val) * sourceWindowMoment a (-(1 / 2)) k.val =
      conj z *
      (conj (sourceWindowMoment a (-(1 / 2)) f.val) * sourceWindowMoment a (1 / 2) k.val +
       conj (sourceWindowMoment a (1 / 2) f.val) * sourceWindowMoment a (-(1 / 2)) k.val)
    simp only [Submodule.coe_smul, map_smul, smul_eq_mul, map_mul]
    ring

/-- The actual normalized multiplier integral plus its named pole moment
cross terms. Source identification is still a separate diagonal obligation. -/
def sourceDomainWeilForm : D.domain →ₗ⋆[ℂ] D.domain →ₗ[ℂ] ℂ :=
  sourceDomainMultiplierForm D hSymbol C hbound + sourceDomainPoleForm D

theorem sourceDomainWeilForm_apply (f g : D.domain) :
    sourceDomainWeilForm D hSymbol C hbound f g =
      sourceDomainMultiplierPairing D f g +
      (conj (sourceWindowMoment a (-(1 / 2)) f.val) * sourceWindowMoment a (1 / 2) g.val +
       conj (sourceWindowMoment a (1 / 2) f.val) * sourceWindowMoment a (-(1 / 2)) g.val) := rfl

/-- Consume polarization for the concrete multiplier-plus-pole form, without
admitting vectors outside the retained source domain. -/
theorem sourceDomainWeilForm_eq_of_diagonal
    (B : D.domain →ₗ⋆[ℂ] D.domain →ₗ[ℂ] ℂ)
    (hdiag : ∀ z : D.domain, B z z = sourceDomainWeilForm D hSymbol C hbound z z)
    (f g : D.domain) :
    B f g = sourceDomainWeilForm D hSymbol C hbound f g :=
  sourceFormDomain_eq_of_diagonal D.domain B _ hdiag f g

end

end WeilDefect
