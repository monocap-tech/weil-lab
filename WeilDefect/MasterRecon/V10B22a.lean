import WeilDefect.MasterRecon.V10B21c
import Mathlib.Analysis.SpecialFunctions.Integrability.Basic

/-! V10B22a: strong continuity from the local translation modulus,
then Bochner integrability on the positive half-line. -/
namespace WeilDefect.MasterRecon.V10B22a

open MeasureTheory Set Filter
open scoped Topology
open V08I (FullL2)
open V10B8d (shift)
open V10B21c (actionTerm numerator denominator)

theorem shift_add (r s : ℝ) (f : FullL2) :
    shift r (shift s f) = shift (r+s) f := by
  apply Lp.ext
  filter_upwards [V10B8d.shift_ae r (shift s f),
    V06D.ae_translate (V10B8d.shift_ae s f) r,
    V10B8d.shift_ae (r+s) f] with x h₁ h₂ h₃
  rw [h₁,h₂,h₃,add_assoc]

theorem shift_zero (f : FullL2) : shift 0 f = f := by
  apply Lp.ext
  filter_upwards [V10B8d.shift_ae 0 f] with x hx
  simpa using hx

theorem shift_dist (r s : ℝ) (f : FullL2) :
    dist (shift r f) (shift s f) = ‖shift (r-s) f-f‖ := by
  rw [dist_eq_norm,← V10B8d.shift_norm (-s) (shift r f-shift s f),
    map_sub,shift_add,shift_add,neg_add_cancel,shift_zero]
  rw [show -s+r=r-s by ring]

theorem two_sided_modulus (f : FullL2) (C : ℝ)
    (h : ∀ r : ℝ, 0 < r → r ≤ 1 → ‖shift r f-f‖ ≤ C*Real.sqrt r)
    (r : ℝ) (hr : |r| ≤ 1) :
    ‖shift r f-f‖ ≤ C*Real.sqrt |r| := by
  rcases lt_trichotomy r 0 with hneg|heq|hpos
  · rw [abs_of_neg hneg,← V10B21c.opposite_shift_norm r f]
    exact h (-r) (by linarith) (by simpa [abs_of_neg hneg] using hr)
  · simp [heq,shift_zero]
  · rw [abs_of_pos hpos]
    exact h r hpos (by simpa [abs_of_pos hpos] using hr)

theorem shift_continuous (f : FullL2) (C : ℝ) (hC : 0 ≤ C)
    (h : ∀ r : ℝ, 0 < r → r ≤ 1 → ‖shift r f-f‖ ≤ C*Real.sqrt r) :
    Continuous (fun r : ℝ => shift r f) := by
  rw [continuous_iff_continuousAt]
  intro s
  rw [Metric.continuousAt_iff]
  intro ε hε
  let δ : ℝ := min 1 ((ε/(C+1))^2)
  have hden : 0 < C+1 := by linarith
  have hδ : 0 < δ := by
    change (0:ℝ) < min 1 ((ε/(C+1))^2)
    exact lt_min (by norm_num : (0:ℝ)<1) (pow_pos (div_pos hε hden) 2)
  refine ⟨δ,hδ,?_⟩
  intro r hr
  rw [Real.dist_eq] at hr
  have hr1 : |r-s| ≤ 1 := hr.le.trans (min_le_left _ _)
  have hrs : |r-s| < (ε/(C+1))^2 := hr.trans_le (min_le_right _ _)
  have hs : Real.sqrt |r-s| < ε/(C+1) := by
    apply (sq_lt_sq₀ (Real.sqrt_nonneg _) (div_nonneg hε.le hden.le)).mp
    rwa [Real.sq_sqrt (abs_nonneg _)]
  rw [shift_dist]
  refine (two_sided_modulus f C h (r-s) hr1).trans_lt ?_
  have hh := mul_le_mul_of_nonneg_left hs.le hC
  have he : C*(ε/(C+1)) < ε := by
    rw [mul_div_assoc]
    apply (div_lt_iff₀ hden).mpr
    nlinarith
  exact hh.trans_lt he

theorem action_continuousOn (f : FullL2) (C : ℝ) (hC : 0 ≤ C)
    (h : ∀ r : ℝ, 0 < r → r ≤ 1 → ‖shift r f-f‖ ≤ C*Real.sqrt r) :
    ContinuousOn (actionTerm f) (Ioi 0) := by
  have hs := shift_continuous f C hC h
  have hs' : Continuous (fun r : ℝ => shift (-r) f) := hs.comp continuous_neg
  have hn : Continuous (numerator f) := by
    unfold numerator
    have h₁ : Continuous (fun r : ℝ => 2*Real.exp (-2*r)) := by fun_prop
    have h₂ : Continuous (fun r : ℝ => Real.exp (-r/2)) := by fun_prop
    exact (h₁.smul continuous_const).sub (h₂.smul (hs.add hs'))
  have hd : Continuous denominator := by unfold denominator; fun_prop
  unfold actionTerm
  exact (hd.continuousOn.inv₀ (fun r hr => (V10B21c.denominator_pos r hr).ne')).smul hn.continuousOn

theorem near_envelope_integrable (f : FullL2) (C : ℝ) :
    IntegrableOn (fun r : ℝ => (9/2:ℝ)*‖f‖+3*C*(Real.sqrt r)⁻¹) (Ioc 0 1) := by
  have hp : IntegrableOn (fun r : ℝ => r^(-1/2:ℝ)) (Ioc 0 1) :=
    (intervalIntegrable_iff_integrableOn_Ioc_of_le (by norm_num : (0:ℝ)≤1)).mp
      (intervalIntegral.intervalIntegrable_rpow' (by norm_num))
  have h := (integrableOn_const (C := (9/2:ℝ)*‖f‖)
    (μ := volume) (s := Ioc (0:ℝ) 1) (measure_Ioc_lt_top.ne)).add (hp.const_mul (3*C))
  apply h.congr_fun _ measurableSet_Ioc
  intro r hr
  change (9/2:ℝ)*‖f‖+3*C*r^(-1/2:ℝ) =
    (9/2:ℝ)*‖f‖+3*C*(Real.sqrt r)⁻¹
  rw [Real.sqrt_eq_rpow,← Real.rpow_neg (le_of_lt hr.1)]
  norm_num

theorem action_integrable (f : FullL2) (C : ℝ) (hC : 0 ≤ C)
    (h : ∀ r : ℝ, 0 < r → r ≤ 1 → ‖shift r f-f‖ ≤ C*Real.sqrt r) :
    IntegrableOn (actionTerm f) (Ioi 0) := by
  have hm : AEStronglyMeasurable (actionTerm f) (volume.restrict (Ioi (0:ℝ))) :=
    (action_continuousOn f C hC h).aestronglyMeasurable measurableSet_Ioi
  have hnear : IntegrableOn (actionTerm f) (Ioc 0 1) := by
    apply (near_envelope_integrable f C).mono' (hm.mono_measure (Measure.restrict_mono
      (fun _ hx => hx.1) le_rfl))
    rw [ae_restrict_iff' measurableSet_Ioc]
    exact Eventually.of_forall fun r hr =>
      V10B21c.action_near f C r hC hr.1 hr.2 (h r hr.1 hr.2)
  have hfar : IntegrableOn (actionTerm f) (Ioi 1) := by
    have hi := (integrableOn_exp_mul_Ioi (a := (-1/2:ℝ)) (by norm_num) 1).const_mul (6*‖f‖)
    apply hi.mono' (hm.mono_measure (Measure.restrict_mono
      (fun r hr => show 0 < r from lt_trans (by norm_num : (0:ℝ)<1) (show 1<r from hr)) le_rfl))
    rw [ae_restrict_iff' measurableSet_Ioi]
    exact Eventually.of_forall fun r hr => by
      simpa only [show -r/2=(-1/2:ℝ)*r by ring] using V10B21c.action_far f r hr.le
  have he : Ioc (0:ℝ) 1 ∪ Ioi 1 = Ioi 0 := by
    ext r
    simp only [mem_union,mem_Ioc,mem_Ioi]
    constructor
    · rintro (h|h)
      · exact h.1
      · linarith
    · intro hr
      by_cases h : r≤1
      · exact Or.inl ⟨hr,h⟩
      · exact Or.inr (lt_of_not_ge h)
  rw [← he,integrableOn_union]
  exact ⟨hnear,hfar⟩

theorem supported_action_integrable (a b B K : ℝ) (hab : a ≤ b)
    (hB : 0 ≤ B) (hK : 0 ≤ K) (p : ℝ → ℂ)
    (hb : ∀ x ∈ Icc a b, ‖p x‖ ≤ B)
    (hl : ∀ x ∈ Icc a b, ∀ y ∈ Icc a b, ‖p x-p y‖ ≤ K*|x-y|)
    (f : FullL2) (hf : (f : ℝ → ℂ) =ᵐ[volume] V10B21b.supported a b p) :
    IntegrableOn (actionTerm f) (Ioi 0) :=
  action_integrable f (Real.sqrt ((b-a)*K^2+2*B^2)) (Real.sqrt_nonneg _)
    (fun r hr hr1 => V10B21b.translation_sqrt a b B K r hab hr.le hr1 hB hK p hb hl f hf)

end WeilDefect.MasterRecon.V10B22a

#print axioms WeilDefect.MasterRecon.V10B22a.shift_add
#print axioms WeilDefect.MasterRecon.V10B22a.shift_zero
#print axioms WeilDefect.MasterRecon.V10B22a.shift_dist
#print axioms WeilDefect.MasterRecon.V10B22a.two_sided_modulus
#print axioms WeilDefect.MasterRecon.V10B22a.shift_continuous
#print axioms WeilDefect.MasterRecon.V10B22a.action_continuousOn
#print axioms WeilDefect.MasterRecon.V10B22a.near_envelope_integrable
#print axioms WeilDefect.MasterRecon.V10B22a.action_integrable
#print axioms WeilDefect.MasterRecon.V10B22a.supported_action_integrable
