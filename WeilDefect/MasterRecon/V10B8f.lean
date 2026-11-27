import WeilDefect.MasterRecon.V10B8e
import Mathlib.Analysis.Complex.CauchyIntegral

/-! Reduction of the uniform Archimedean residual to the classical vertical
Stirling estimate, whose exact source is Zeta23/GammaFacts/StirlingVert.lean
at mirror revision 77f832c86fbb3e5336b949dae0fdcae26baea87c.
No external theorem is adopted here. -/
namespace WeilDefect.MasterRecon.V10B8f

open Set Complex
open scoped Topology
open V10B8e (gammaSymbol residual ResidualEstimate)

theorem gamma_ne_neg_nat {z : ℂ} (hz : 0 < z.re) (n : ℕ) : z ≠ -(n:ℂ) := by
  intro h
  rw [h,Complex.neg_re,Complex.natCast_re] at hz
  exact (not_lt_of_ge (neg_nonpos.mpr (Nat.cast_nonneg n))) hz

theorem digamma_analytic {z : ℂ} (hz : 0 < z.re) :
    AnalyticAt ℂ Complex.digamma z := by
  have ho : IsOpen {w : ℂ | 0 < w.re} := isOpen_lt continuous_const Complex.continuous_re
  have h : DifferentiableOn ℂ Complex.Gamma {w : ℂ | 0 < w.re} :=
    fun w hw => (Complex.differentiableAt_Gamma w (gamma_ne_neg_nat hw)).differentiableWithinAt
  have ha := h.analyticOnNhd ho z hz
  rw [Complex.digamma_def]
  change AnalyticAt ℂ (fun w => deriv Complex.Gamma w / Complex.Gamma w) z
  exact ha.deriv.div ha (Complex.Gamma_ne_zero (gamma_ne_neg_nat hz))

theorem gammaSymbol_continuous : Continuous gammaSymbol := by
  apply continuous_iff_continuousAt.mpr
  intro u
  let z : ℝ → ℂ := fun v => 1/4+I*((-(2*Real.pi*v):ℝ):ℂ)/2
  have hz : 0 < (z u).re := by simp [z]
  have hc : Continuous z := by dsimp [z]; fun_prop
  exact (Complex.continuous_re.continuousAt.comp
    ((digamma_analytic hz).continuousAt.comp hc.continuousAt)).sub continuousAt_const

theorem residual_continuous : Continuous residual :=
  gammaSymbol_continuous.sub V08I.logWeight_continuous

def VerticalStirling : Prop :=
  ∀ v : ℝ, 1/2 ≤ |v| →
    |(Complex.digamma ((1/4:ℂ)+I*(v:ℂ))).re - Real.log (|v|)| ≤ 5/v^2

theorem gammaSymbol_reparam (u : ℝ) :
    gammaSymbol u =
      (Complex.digamma ((1/4:ℂ)+I*((-Real.pi*u:ℝ):ℂ))).re - Real.log Real.pi := by
  unfold gammaSymbol
  congr 2
  push_cast
  ring

theorem weight_reparam (u : ℝ) :
    V08I.logWeight u = Real.log (2+2*|-Real.pi*u|) := by
  unfold V08I.logWeight
  congr 1
  simp only [abs_mul,abs_neg,abs_of_pos Real.pi_pos,abs_of_nonneg (by norm_num : (0:ℝ) ≤ 2)]
  ring

theorem log_comparison (v : ℝ) (hv : 1/2 ≤ |v|) :
    |Real.log (|v|) - Real.log (2+2*|v|)| ≤ Real.log 6 := by
  have hp : 0 < |v| := by linarith
  have h1 : Real.log (|v|) ≤ Real.log (2+2*|v|) :=
    Real.log_le_log hp (by linarith)
  have h2 : Real.log (2+2*|v|) ≤ Real.log (6*|v|) :=
    Real.log_le_log (by positivity) (by linarith)
  rw [Real.log_mul (by norm_num : (6:ℝ) ≠ 0) hp.ne'] at h2
  rw [abs_of_nonpos (sub_nonpos.mpr h1)]
  linarith

theorem tail_residual (hs : VerticalStirling) (u : ℝ)
    (hu : 1/2 ≤ |-Real.pi*u|) :
    |residual u| ≤ 20+|Real.log Real.pi|+Real.log 6 := by
  let v := -Real.pi*u
  have hv : 1/2 ≤ |v| := hu
  have hsq : 1/4 ≤ v^2 := by
    rw [← sq_abs]
    nlinarith [abs_nonneg v]
  have hb : 5/v^2 ≤ 20 := (div_le_iff₀ (by linarith)).mpr (by linarith)
  have hψ := (hs v hv).trans hb
  have hlog := log_comparison v hv
  rw [residual,gammaSymbol_reparam,weight_reparam]
  change |(Complex.digamma ((1/4:ℂ)+I*(v:ℂ))).re - Real.log Real.pi -
    Real.log (2+2*|v|)| ≤ _
  calc
    _ = |((Complex.digamma ((1/4:ℂ)+I*(v:ℂ))).re - Real.log (|v|)) +
        (-Real.log Real.pi + (Real.log (|v|) - Real.log (2+2*|v|)))| := by congr 1; ring
    _ ≤ |(Complex.digamma ((1/4:ℂ)+I*(v:ℂ))).re - Real.log (|v|)| +
        |-Real.log Real.pi + (Real.log (|v|) - Real.log (2+2*|v|))| := abs_add_le _ _
    _ ≤ _ := by
      have h := abs_add_le (-Real.log Real.pi) (Real.log (|v|) - Real.log (2+2*|v|))
      rw [abs_neg] at h
      linarith

theorem residual_of_stirling (hs : VerticalStirling) : ResidualEstimate := by
  let R : ℝ := 1/(2*Real.pi)
  obtain ⟨B,hB⟩ := (isCompact_Icc (a := -R) (b := R)).exists_bound_of_continuousOn
    residual_continuous.continuousOn
  let D := 20+|Real.log Real.pi|+Real.log 6
  refine ⟨residual_continuous.measurable, max 0 (max B D), le_max_left _ _, ?_⟩
  intro u
  by_cases hu : 1/2 ≤ |-Real.pi*u|
  · exact (tail_residual hs u hu).trans ((le_max_right B D).trans (le_max_right 0 _))
  · have ha : |u| ≤ R := by
      have h := le_of_lt (lt_of_not_ge hu)
      rw [abs_mul,abs_neg,abs_of_pos Real.pi_pos] at h
      dsimp [R]
      apply (le_div_iff₀ (by positivity : 0 < 2*Real.pi)).mpr
      linarith
    have h := hB u (abs_le.mp ha)
    rw [Real.norm_eq_abs] at h
    exact h.trans ((le_max_left B D).trans (le_max_right 0 _))

end WeilDefect.MasterRecon.V10B8f

#print axioms WeilDefect.MasterRecon.V10B8f.gamma_ne_neg_nat
#print axioms WeilDefect.MasterRecon.V10B8f.digamma_analytic
#print axioms WeilDefect.MasterRecon.V10B8f.gammaSymbol_continuous
#print axioms WeilDefect.MasterRecon.V10B8f.residual_continuous
#print axioms WeilDefect.MasterRecon.V10B8f.gammaSymbol_reparam
#print axioms WeilDefect.MasterRecon.V10B8f.weight_reparam
#print axioms WeilDefect.MasterRecon.V10B8f.log_comparison
#print axioms WeilDefect.MasterRecon.V10B8f.tail_residual
#print axioms WeilDefect.MasterRecon.V10B8f.residual_of_stirling
