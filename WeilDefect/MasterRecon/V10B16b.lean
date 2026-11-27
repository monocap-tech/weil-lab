import WeilDefect.MasterRecon.V10B15a
import WeilDefect.MasterRecon.V10B16a

/-! One-sided high-frequency estimate. P is a separately certified prime
budget; the pole term must be retained exactly or annihilated. -/
namespace WeilDefect.MasterRecon.V10B16b

open Complex MeasureTheory Set
open V08I (logWeight)
open V10B8e (gammaSymbol residual)

theorem high_symbol (hV : V10B8f.VerticalStirling) (P V : ℝ)
    (hV3 : 3 ≤ V)
    (hthreshold : P+Real.log Real.pi+1+Real.log 4/4 ≤ (3/4:ℝ)*Real.log V)
    (u : ℝ) (hu : V ≤ |-Real.pi*u|) :
    (1/4:ℝ)*logWeight u ≤ gammaSymbol u-P := by
  let v := -Real.pi*u
  have hv : V ≤ |v| := hu
  have hv3 : 3 ≤ |v| := hV3.trans hv
  have hvpos : 0 < |v| := by linarith
  have hsq : 9 ≤ v^2 := by rw [← sq_abs]; nlinarith [abs_nonneg v]
  have herr : 5/v^2 ≤ 1 := (div_le_one (by linarith)).mpr (by linarith)
  have hψ := (abs_le.mp (hV v (by linarith))).1
  have hlog : Real.log V ≤ Real.log |v| := Real.log_le_log (by linarith) hv
  have hupper : Real.log (2+2*|v|) ≤ Real.log 4+Real.log |v| := by
    rw [← Real.log_mul (by norm_num : (4:ℝ) ≠ 0) hvpos.ne']
    exact Real.log_le_log (by positivity) (by linarith)
  rw [V10B8f.gammaSymbol_reparam,V10B8f.weight_reparam]
  change (1/4:ℝ)*Real.log (2+2*|v|) ≤
    (Complex.digamma ((1/4:ℂ)+I*(v:ℂ))).re-Real.log Real.pi-P
  linarith only [herr,hψ,hlog,hupper,hthreshold]

theorem low_symbol (C P : ℝ) (hC : ∀ u, |residual u| ≤ C) (u : ℝ) :
    (1/4:ℝ)*logWeight u-(C+P) ≤ gammaSymbol u-P := by
  have h := (abs_le.mp (hC u)).1
  unfold residual at h
  linarith [V08I.logWeight_pos u]

theorem signed_arch_prime (hV : V10B8f.VerticalStirling) (C P V : ℝ)
    (hC : ∀ u, |residual u| ≤ C) (hV3 : 3 ≤ V)
    (hthreshold : P+Real.log Real.pi+1+Real.log 4/4 ≤ (3/4:ℝ)*Real.log V)
    (f : ℝ → ℂ)
    (ha : MeasureTheory.Integrable (fun u => (gammaSymbol u-P)*‖f u‖^2))
    (hw : MeasureTheory.Integrable (fun u => logWeight u*‖f u‖^2))
    (hf : MeasureTheory.Integrable (fun u => ‖f u‖^2)) :
    (1/4:ℝ)*(∫ u, logWeight u*‖f u‖^2) -
      (C+P)*(∫ u in {u : ℝ | |-Real.pi*u| < V}, ‖f u‖^2) ≤
      ∫ u, (gammaSymbol u-P)*‖f u‖^2 := by
  apply V10B16a.signed_split _ _ _ _ _ _ _ ha hw hf
  · exact measurableSet_lt (by fun_prop) measurable_const
  · intro u _
    exact low_symbol C P hC u
  · intro u hu
    exact high_symbol hV P V hV3 hthreshold u (le_of_not_gt hu)

end WeilDefect.MasterRecon.V10B16b

#print axioms WeilDefect.MasterRecon.V10B16b.high_symbol
#print axioms WeilDefect.MasterRecon.V10B16b.low_symbol
#print axioms WeilDefect.MasterRecon.V10B16b.signed_arch_prime
