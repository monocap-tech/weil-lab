import WeilDefect.MasterReturn.LogWeightComparison
import WeilDefect.MasterRecon.V08J
import WeilDefect.Morphology.NeutralLogHilbertCarrier

/-! RETURN108-T integration-only candidate. The third import is on the
pinned IV091 lineage, not present on the RECON staging branch.
Do not compile until both source closures have been authenticated.
No graph/sample equality is assumed. -/
namespace WeilDefect.MasterReturn.LogCarrierBridge

open MeasureTheory Set
open scoped FourierTransform
open WeilDefect.MasterRecon
open LogWeightComparison

theorem recon_le_scaled_iv (x : ℝ) :
    V08I.logWeight x ≤ (1+|cRI|)*logarithmicFourierWeight x := by
  change reconWeight x ≤ (1+|cRI|)*ivWeight x
  have h := mul_le_mul_of_nonneg_left (ivWeight_lower x) (abs_nonneg cRI)
  nlinarith only [recon_le_iv_add x, le_abs_self cRI, h]

theorem iv_le_scaled_recon (x : ℝ) :
    logarithmicFourierWeight x ≤
      (1+|cIR|/Real.log 2)*V08I.logWeight x := by
  change ivWeight x ≤ (1+|cIR|/Real.log 2)*reconWeight x
  have hlog : 0 < Real.log 2 := Real.log_pos (by norm_num)
  have h := mul_le_mul_of_nonneg_left (reconWeight_lower x)
    (div_nonneg (abs_nonneg cIR) hlog.le)
  have he : (|cIR|/Real.log 2)*Real.log 2 = |cIR| := by
    field_simp
  rw [he] at h
  nlinarith only [iv_le_recon_add x, le_abs_self cIR, h]

theorem iv_energy_to_recon (f : RealComplexL2)
    (hf : Integrable (fun x => logarithmicFourierWeight x *
      ‖(𝓕 f : RealComplexL2) x‖^2) volume) :
    Integrable (fun x => V08I.logWeight x * ‖(𝓕 f : RealComplexL2) x‖^2) volume := by
  apply (hf.const_mul (1+|cRI|)).mono'
  · exact V08I.logWeight_continuous.aestronglyMeasurable.mul
      ((Lp.aestronglyMeasurable (𝓕 f : RealComplexL2)).norm.pow 2)
  · filter_upwards with x
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg (V08I.logWeight_pos x).le (sq_nonneg _))]
    calc
      _ ≤ ((1+|cRI|)*logarithmicFourierWeight x)*‖(𝓕 f : RealComplexL2) x‖^2 :=
        mul_le_mul_of_nonneg_right (recon_le_scaled_iv x) (sq_nonneg _)
      _ = _ := by ring

theorem recon_energy_to_iv (f : RealComplexL2)
    (hf : Integrable (fun x => V08I.logWeight x *
      ‖(𝓕 f : RealComplexL2) x‖^2) volume) :
    Integrable (fun x => logarithmicFourierWeight x * ‖(𝓕 f : RealComplexL2) x‖^2) volume := by
  apply (hf.const_mul (1+|cIR|/Real.log 2)).mono'
  · exact logarithmicFourierWeight_continuous.aestronglyMeasurable.mul
      ((Lp.aestronglyMeasurable (𝓕 f : RealComplexL2)).norm.pow 2)
  · filter_upwards with x
    have hw : 0 ≤ logarithmicFourierWeight x :=
      (by norm_num : (0:ℝ) ≤ 1).trans (one_le_logarithmicFourierWeight x)
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg hw (sq_nonneg _))]
    calc
      _ ≤ ((1+|cIR|/Real.log 2)*V08I.logWeight x)*‖(𝓕 f : RealComplexL2) x‖^2 :=
        mul_le_mul_of_nonneg_right (iv_le_scaled_recon x) (sq_nonneg _)
      _ = _ := by ring

noncomputable def toRecon (a : ℝ) (g : NeutralLogHilbertCarrier a) :
    V08I.logCarrier a :=
  V08J.liftPhysical a (neutralLogPhysical g.val)
    (neutralLogHilbertCarrier_supported g)
    (iv_energy_to_recon _ (neutralLogPhysical_energy g.val))

noncomputable def toIV (a : ℝ) (g : V08I.logCarrier a) :
    NeutralLogHilbertCarrier a :=
  neutralCanonicalToLogHilbert ⟨V08I.physicalInclusion a g,
    V08I.physicalInclusion_support a g,
    recon_energy_to_iv _ (V08I.logCarrier_energy_integrable a g)⟩

theorem toRecon_physical (a : ℝ) (g : NeutralLogHilbertCarrier a) :
    V08I.physicalInclusion a (toRecon a g) = neutralLogPhysical g.val :=
  V08J.physicalInclusion_lift _ _ _ _

theorem toIV_physical (a : ℝ) (g : V08I.logCarrier a) :
    neutralLogPhysical (toIV a g).val = V08I.physicalInclusion a g := by
  unfold toIV
  exact congrArg Subtype.val (neutralLogHilbertToCanonical_leftInverse _)

theorem iv_physical_injective (a : ℝ) :
    Function.Injective (fun g : NeutralLogHilbertCarrier a => neutralLogPhysical g.val) := by
  intro g h hgh
  have he : neutralLogHilbertToCanonical g = neutralLogHilbertToCanonical h :=
    Subtype.ext hgh
  exact (neutralLogHilbertToCanonical_rightInverse (a:=a)).injective he

/-- Exact same-vector linear equivalence; continuity is a subsequent
norm-bound step. Neither equality of weights nor isometry is assumed. -/
noncomputable def carrierEquiv (a : ℝ) :
    NeutralLogHilbertCarrier a ≃ₗ[ℂ] V08I.logCarrier a where
  toFun := toRecon a
  invFun := toIV a
  left_inv g := by
    apply iv_physical_injective a
    change neutralLogPhysical (toIV a (toRecon a g)).val = neutralLogPhysical g.val
    rw [toIV_physical, toRecon_physical]
  right_inv g := by
    apply V08J.physicalInclusion_injective a
    rw [toRecon_physical, toIV_physical]
  map_add' g h := by
    apply V08J.physicalInclusion_injective a
    rw [map_add, toRecon_physical, toRecon_physical, toRecon_physical]
    exact neutralLogPhysical.map_add g.val h.val
  map_smul' z g := by
    apply V08J.physicalInclusion_injective a
    rw [map_smul, toRecon_physical, toRecon_physical]
    exact neutralLogPhysical.map_smul z g.val

theorem carrierEquiv_physical (a : ℝ) (g : NeutralLogHilbertCarrier a) :
    V08I.physicalInclusion a (carrierEquiv a g) = neutralLogPhysical g.val :=
  toRecon_physical a g

end WeilDefect.MasterReturn.LogCarrierBridge

#print axioms WeilDefect.MasterReturn.LogCarrierBridge.recon_le_scaled_iv
#print axioms WeilDefect.MasterReturn.LogCarrierBridge.iv_le_scaled_recon
#print axioms WeilDefect.MasterReturn.LogCarrierBridge.iv_energy_to_recon
#print axioms WeilDefect.MasterReturn.LogCarrierBridge.recon_energy_to_iv
#print axioms WeilDefect.MasterReturn.LogCarrierBridge.toRecon_physical
#print axioms WeilDefect.MasterReturn.LogCarrierBridge.toIV_physical
#print axioms WeilDefect.MasterReturn.LogCarrierBridge.iv_physical_injective
#print axioms WeilDefect.MasterReturn.LogCarrierBridge.carrierEquiv
#print axioms WeilDefect.MasterReturn.LogCarrierBridge.carrierEquiv_physical
