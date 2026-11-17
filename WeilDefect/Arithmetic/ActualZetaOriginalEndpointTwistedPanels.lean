import WeilDefect.Arithmetic.ActualZetaOriginalEndpointTwistedAmplitude
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointLogFourierSplit

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped Interval

/-! NF585: discharge the analytic panel integrability inputs for
the actual twisted U. Keep the original closed collar and exact
C0,C1. The final source identity is not inferred from numerical
bounds on an unrelated function. -/

def neutralNF585A (U : ℝ → ℝ) (y : ℝ) (d : ℝ) : ℂ :=
  (neutralNF585TwistedAmplitude U y d : ℂ)

def neutralNF585A' (U U' : ℝ → ℝ) (y : ℝ) (d : ℝ) : ℂ :=
  (neutralNF585TwistedDerivative U U' y d : ℂ)

theorem neutralNF585FullPanel_integrable (U : ℝ → ℝ) (y t : ℝ)
    (hU : ContinuousOn U (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B)) :
    IntervalIntegrable (fun d => neutralNF584Amplitude neutralNF578B
      (neutralNF585A U y) d * neutralNF584Phase t d) volume 0 neutralNF578Delta := by
  have hδ : 0 ≤ neutralNF578Delta := by unfold neutralNF578Delta; norm_num
  have hA : ContinuousOn (neutralNF585A U y) (uIcc 0 neutralNF578Delta) := by
    rw [uIcc_of_le hδ]
    exact Complex.continuous_ofReal.comp_continuousOn
      (neutralNF585Twisted_continuousOn U y hU)
  have hl := neutralNF584LogKernel_intervalIntegrable neutralNF578B 0 neutralNF578Delta
  have hc : IntervalIntegrable
      (fun d => (neutralNF584LogKernel neutralNF578B d:ℂ)) volume 0 neutralNF578Delta :=
    ⟨hl.1.ofReal,hl.2.ofReal⟩
  have hp : Continuous (neutralNF584Phase t) := by
    unfold neutralNF584Phase
    fun_prop
  exact (hc.continuousOn_mul hA).mul_continuousOn hp.continuousOn

theorem neutralNF585DerivativePanel_integrable
    (U U' : ℝ → ℝ) (y a : ℝ) (ha : 0 < a) (haδ : a ≤ neutralNF578Delta)
    (hU : ContinuousOn U (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B))
    (hU' : ContinuousOn U' (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B)) :
    IntervalIntegrable (neutralNF584AmplitudeDeriv neutralNF578B
      (neutralNF585A U y) (neutralNF585A' U U' y)) volume a neutralNF578Delta := by
  have hs : uIcc a neutralNF578Delta ⊆ Icc 0 neutralNF578Delta := by
    rw [uIcc_of_le haδ]
    exact Icc_subset_Icc ha.le le_rfl
  have hA : ContinuousOn (neutralNF585A U y) (uIcc a neutralNF578Delta) :=
    Complex.continuous_ofReal.comp_continuousOn
      ((neutralNF585Twisted_continuousOn U y hU).mono hs)
  have hA' : ContinuousOn (neutralNF585A' U U' y) (uIcc a neutralNF578Delta) :=
    Complex.continuous_ofReal.comp_continuousOn
      ((neutralNF585TwistedDerivative_continuousOn U U' y hU hU').mono hs)
  have hn : ∀ d ∈ uIcc a neutralNF578Delta, d ≠ 0 := by
    intro d hd
    rw [uIcc_of_le haδ] at hd
    exact (ha.trans_le hd.1).ne'
  have hl : ContinuousOn (fun d => neutralNF584LogKernel neutralNF578B d)
      (uIcc a neutralNF578Delta) := by
    unfold neutralNF584LogKernel
    exact continuousOn_const.sub (continuousOn_id.log hn)
  have hi : ContinuousOn (fun d : ℝ => d⁻¹) (uIcc a neutralNF578Delta) :=
    continuousOn_id.inv₀ hn
  exact ((hA'.mul (Complex.continuous_ofReal.comp_continuousOn hl)).sub
    (hA.mul (Complex.continuous_ofReal.comp_continuousOn hi))).intervalIntegrable

theorem neutralNF585Log550_lt_seven : Real.log ((11/10:ℝ)/(1/500)) < 7 := by
  have h := Real.log_lt_log (by norm_num : 0 < (11/10:ℝ)/(1/500))
    (by norm_num : (11/10:ℝ)/(1/500) < 2^10)
  rw [Real.log_pow] at h
  norm_num at h
  linarith [Real.log_two_lt_d9]

theorem neutralNF585LogBT_le (T : ℝ) (hT : 0 < T) :
    Real.log ((11/10:ℝ)*T) ≤ 1+Real.log (2+T) := by
  have hB := Real.log_le_log (by norm_num : (0:ℝ)<11/10)
    (by norm_num : (11/10:ℝ)≤2)
  have ht := Real.log_le_log hT (by linarith : T≤2+T)
  rw [Real.log_mul (by norm_num : (11/10:ℝ)≠0) hT.ne']
  linarith [Real.log_two_lt_d9]

/-- Conditional on the actual U and U' bounds, the literal twisted
interval integral satisfies the original 1/40000 half-envelope.
No estimate on the approximation family is used. -/
theorem neutralNF585TwistedPanel_strip
    (U U' : ℝ → ℝ)
    (hU : ContinuousOn U (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B))
    (hU' : ContinuousOn U' (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B))
    (hder : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      HasDerivAt U (U' x) x)
    (h0 : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      |U x| ≤ neutralNF578C0)
    (h1 : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      |U' x| ≤ (7/10^4:ℝ))
    (t y : ℝ) (hy : |y| ≤ 1/2) :
    ‖∫ d in (0:ℝ)..neutralNF578Delta,
      neutralNF584Amplitude neutralNF578B (neutralNF585A U y) d *
        neutralNF584Phase t d‖ ≤
      (1/40000:ℝ)*(1+Real.log (2+|t|))/(1+|t|) := by
  let A := neutralNF585A U y
  let A' := neutralNF585A' U U' y
  let T := |t|
  let L := Real.log (2+T)
  have hT0 : 0 ≤ T := abs_nonneg _
  have hL : 0 ≤ L := Real.log_nonneg (by dsimp [T]; linarith [abs_nonneg t])
  have hδ : 0 < neutralNF578Delta := by unfold neutralNF578Delta; norm_num
  have hδB : neutralNF578Delta ≤ neutralNF578B := by unfold neutralNF578B neutralNF578Delta; norm_num
  have hC0 : 0 ≤ neutralNF578C0 := by unfold neutralNF578C0; norm_num
  have hC1 : 0 ≤ neutralNF578C1 := by unfold neutralNF578C1 neutralNF578C0; norm_num
  have hAd (d : ℝ) (hd : d ∈ Icc 0 neutralNF578Delta) :
      HasDerivAt A (A' d) d := by
    have hx : neutralNF578B-d ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B :=
      ⟨by linarith [hd.2],by linarith [hd.1]⟩
    exact (neutralNF585Twisted_hasDerivAt U U' y d (hder _ hx)).ofReal_comp
  have hA (d : ℝ) (hd : d ∈ Icc 0 neutralNF578Delta) : ‖A d‖ ≤ neutralNF578C0 := by
    simpa only [A,neutralNF585A,Complex.norm_real,Real.norm_eq_abs] using
      (neutralNF585Twisted_bounds U U' y d hy hd h0 h1).1
  have hA' (d : ℝ) (hd : d ∈ Icc 0 neutralNF578Delta) : ‖A' d‖ ≤ neutralNF578C1 := by
    simpa only [A',neutralNF585A',Complex.norm_real,Real.norm_eq_abs] using
      (neutralNF585Twisted_bounds U U' y d hy hd h0 h1).2
  have hlδ : neutralNF584LogKernel neutralNF578B neutralNF578Delta+1 ≤ 8 := by
    rw [neutralNF584LogKernel_eq_ratio _ _ (hδ.trans_le hδB) hδ]
    unfold neutralNF578B neutralNF578Delta
    linarith [neutralNF585Log550_lt_seven]
  change ‖∫ d in (0:ℝ)..neutralNF578Delta,
      neutralNF584Amplitude neutralNF578B A d*neutralNF584Phase t d‖ ≤
        (1/40000:ℝ)*(1+L)/(1+T)
  by_cases ht : T ≤ 500
  · have hn := neutralNF584NearPanel A neutralNF578B neutralNF578Delta
      neutralNF578C0 hδ hδB hA t
    change ‖∫ d in (0:ℝ)..neutralNF578Delta,
      neutralNF584Amplitude neutralNF578B A d*neutralNF584Phase t d‖ ≤ _ at hn
    apply hn.trans
    have hm := mul_le_mul_of_nonneg_left hlδ (mul_nonneg hC0 hδ.le)
    unfold neutralNF578Delta at hm
    exact hm.trans (neutralNF578LowBand_scalar T L hT0 ht hL)
  · have ht' : 500 ≤ T := le_of_lt (lt_of_not_ge ht)
    have ht0 : 0 < T := by linarith
    let a := 1/T
    have ha : 0 < a := by dsimp [a]; positivity
    have haδ : a ≤ neutralNF578Delta := by
      unfold a neutralNF578Delta
      exact div_le_div_of_nonneg_left (by norm_num) (by norm_num) ht'
    have hsplit : |t| * a = 1 := by change T*(1/T)=1; field_simp
    have hf := neutralNF584SplitPanel A A' neutralNF578B a neutralNF578Delta
      neutralNF578C0 neutralNF578C1 t ha haδ hδB hC0 hC1
      (fun d hd => hAd d ⟨ha.le.trans hd.1,hd.2⟩) hA
      (fun d hd => hA' d ⟨ha.le.trans hd.1,hd.2⟩)
      (neutralNF585DerivativePanel_integrable U U' y a ha haδ hU hU')
      (neutralNF585FullPanel_integrable U y t hU) ht0 hsplit
    have hla : neutralNF584LogKernel neutralNF578B a ≤ 1+L := by
      rw [neutralNF584LogKernel_eq_ratio _ _ (hδ.trans_le hδB) ha]
      have he : neutralNF578B/a = (11/10:ℝ)*T := by
        unfold a neutralNF578B
        field_simp
      rw [he]
      exact neutralNF585LogBT_le T ht0
    have hnum : neutralNF578C0*(3*neutralNF584LogKernel neutralNF578B a+1)+
        neutralNF578C1*neutralNF578Delta*
          (neutralNF584LogKernel neutralNF578B neutralNF578Delta+1) ≤
        neutralNF578C0*(3*(1+L)+1)+neutralNF578C1*(1/500)*8 := by
      have hleft := mul_le_mul_of_nonneg_left (show
        3*neutralNF584LogKernel neutralNF578B a+1 ≤ 3*(1+L)+1 by linarith) hC0
      have hright := mul_le_mul_of_nonneg_left hlδ (mul_nonneg hC1 hδ.le)
      unfold neutralNF578Delta at hright
      exact add_le_add hleft hright
    have hf' := hf.trans hnum
    have hdiv := (le_div_iff₀ ht0).mpr (by simpa only [T,mul_comm] using hf')
    exact hdiv.trans (neutralNF578HighBand_scalar T L (le_of_lt (lt_of_not_ge ht)) hL)

end
end WeilDefect
