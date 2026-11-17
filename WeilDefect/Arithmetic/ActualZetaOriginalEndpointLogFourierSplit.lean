import WeilDefect.Arithmetic.ActualZetaOriginalEndpointLogFourierPanels

namespace WeilDefect
noncomputable section
open MeasureTheory Set
open scoped Interval

/-! NF584: literal differentiated logarithmic amplitude and split
estimate. Source-specific twist bounds and raw/interval attachment
are separate obligations; the estimate uses the full integral,
not a truncated target. -/

def neutralNF584Amplitude (B : ℝ) (A : ℝ → ℂ) (d : ℝ) : ℂ :=
  A d * (neutralNF584LogKernel B d : ℂ)

def neutralNF584AmplitudeDeriv (B : ℝ) (A A' : ℝ → ℂ) (d : ℝ) : ℂ :=
  A' d * (neutralNF584LogKernel B d : ℂ) - A d * (d⁻¹ : ℝ)

theorem neutralNF584Amplitude_hasDerivAt (B d : ℝ) (A A' : ℝ → ℂ)
    (hd : 0 < d) (hA : HasDerivAt A (A' d) d) :
    HasDerivAt (neutralNF584Amplitude B A)
      (neutralNF584AmplitudeDeriv B A A' d) d := by
  have hlog : HasDerivAt (neutralNF584LogKernel B) (-(d⁻¹)) d := by
    unfold neutralNF584LogKernel
    simpa using (hasDerivAt_const d (Real.log B)).sub (Real.hasDerivAt_log hd.ne')
  have hc := hlog.ofReal_comp
  have h := hA.mul hc
  unfold neutralNF584Amplitude neutralNF584AmplitudeDeriv
  push_cast at h
  convert h using 1 <;> ring

theorem neutralNF584LogKernel_mass_le (B a δ : ℝ)
    (ha : 0 < a) (haδ : a ≤ δ) (hδB : δ ≤ B) :
    (∫ d in a..δ, neutralNF584LogKernel B d) ≤
      δ*(neutralNF584LogKernel B δ+1) := by
  have h := intervalIntegral.integral_add_adjacent_intervals
    (neutralNF584LogKernel_intervalIntegrable B 0 a)
    (neutralNF584LogKernel_intervalIntegrable B a δ)
  rw [neutralNF584LogKernel_zero_mass B a,
      neutralNF584LogKernel_zero_mass B δ] at h
  have hn : 0 ≤ neutralNF584LogKernel B a :=
    neutralNF584LogKernel_nonneg B a ha (haδ.trans hδB)
  have hp : 0 ≤ a*(neutralNF584LogKernel B a+1) := by positivity
  linarith

theorem neutralNF584LogKernel_cancel (B a δ : ℝ)
    (ha : 0 < a) (hδ : 0 < δ) :
    neutralNF584LogKernel B δ+Real.log (δ/a) =
      neutralNF584LogKernel B a := by
  unfold neutralNF584LogKernel
  rw [Real.log_div hδ.ne' ha.ne']
  ring

/-- The nonsingular derivative panel bound, with the genuine
1/d term integrated exactly. A' may be any certified derivative
of the twisted amplitude on the proper interval. -/
theorem neutralNF584HighPanel
    (A A' : ℝ → ℂ) (B a δ C0 C1 t : ℝ)
    (ha : 0 < a) (haδ : a ≤ δ) (hδB : δ ≤ B)
    (hC0 : 0 ≤ C0) (hC1 : 0 ≤ C1)
    (hder : ∀ d ∈ Icc a δ, HasDerivAt A (A' d) d)
    (hA : ∀ d ∈ Icc a δ, ‖A d‖ ≤ C0)
    (hA' : ∀ d ∈ Icc a δ, ‖A' d‖ ≤ C1)
    (hi : IntervalIntegrable (neutralNF584AmplitudeDeriv B A A') volume a δ) :
    |t| * ‖∫ d in a..δ, neutralNF584Amplitude B A d * neutralNF584Phase t d‖ ≤
      2*C0*neutralNF584LogKernel B a +
        C1*δ*(neutralNF584LogKernel B δ+1) := by
  have hδ : 0 < δ := ha.trans_le haδ
  have hB : ∀ d ∈ uIcc a δ, HasDerivAt (neutralNF584Amplitude B A)
      (neutralNF584AmplitudeDeriv B A A' d) d := by
    intro d hd
    rw [uIcc_of_le haδ] at hd
    exact neutralNF584Amplitude_hasDerivAt B d A A' (ha.trans_le hd.1) (hder d hd)
  have hf := neutralNF584OscillatoryPanel _ _ a δ t haδ hB hi
  have hb (d : ℝ) (hd : d ∈ Icc a δ) :
      ‖neutralNF584Amplitude B A d‖ ≤ C0*neutralNF584LogKernel B d := by
    have hl := neutralNF584LogKernel_nonneg B d (ha.trans_le hd.1)
      (hd.2.trans hδB)
    unfold neutralNF584Amplitude
    rw [norm_mul,Complex.norm_real,Real.norm_eq_abs,abs_of_nonneg hl]
    exact mul_le_mul_of_nonneg_right (hA d hd) hl
  have hmaj : IntervalIntegrable (fun d => C1*neutralNF584LogKernel B d +
      C0*d⁻¹) volume a δ := by
    have hc : ContinuousOn (fun d : ℝ => d⁻¹) (uIcc a δ) := by
      apply continuousOn_id.inv₀
      intro d hd
      rw [uIcc_of_le haδ] at hd
      exact (ha.trans_le hd.1).ne'
    exact ((neutralNF584LogKernel_intervalIntegrable B a δ).const_mul C1).add
      (hc.intervalIntegrable.const_mul C0)
  have hbound : (∫ d in a..δ, ‖neutralNF584AmplitudeDeriv B A A' d‖) ≤
      ∫ d in a..δ, C1*neutralNF584LogKernel B d + C0*d⁻¹ := by
    apply intervalIntegral.integral_mono_on haδ hi.norm hmaj
    intro d hd
    have hd0 : 0 < d := ha.trans_le hd.1
    have hl := neutralNF584LogKernel_nonneg B d hd0 (hd.2.trans hδB)
    unfold neutralNF584AmplitudeDeriv
    calc
      _ ≤ ‖A' d * (neutralNF584LogKernel B d:ℂ)‖ +
          ‖A d * (d⁻¹:ℝ)‖ := norm_sub_le _ _
      _ ≤ _ := by
        rw [norm_mul,norm_mul,Complex.norm_real,Complex.norm_real,
          Real.norm_eq_abs,Real.norm_eq_abs,abs_of_nonneg hl,
          abs_of_nonneg (inv_nonneg.mpr hd0.le)]
        exact add_le_add (mul_le_mul_of_nonneg_right (hA' d hd) hl)
          (mul_le_mul_of_nonneg_right (hA d hd) (inv_nonneg.mpr hd0.le))
  have hinv : IntervalIntegrable (fun d : ℝ => d⁻¹) volume a δ := by
    apply ContinuousOn.intervalIntegrable
    apply continuousOn_id.inv₀
    intro d hd
    rw [uIcc_of_le haδ] at hd
    exact (ha.trans_le hd.1).ne'
  rw [intervalIntegral.integral_add
    ((neutralNF584LogKernel_intervalIntegrable B a δ).const_mul C1)
    (hinv.const_mul C0),intervalIntegral.integral_const_mul,
    intervalIntegral.integral_const_mul,integral_inv_of_pos ha hδ] at hbound
  have hm := mul_le_mul_of_nonneg_left (neutralNF584LogKernel_mass_le B a δ ha haδ hδB) hC1
  have hc := neutralNF584LogKernel_cancel B a δ ha hδ
  have hc' := congrArg (fun x : ℝ => C0*x) hc
  have hba := hb a ⟨le_rfl,haδ⟩
  have hbδ := hb δ ⟨haδ,le_rfl⟩
  nlinarith only [hf,hba,hbδ,hbound,hm,hc']

/-- Combined full interval bound. At a=1/|t| this is the exact
NF576 high-band expression, after division by |t|. -/
theorem neutralNF584SplitPanel
    (A A' : ℝ → ℂ) (B a δ C0 C1 t : ℝ)
    (ha : 0 < a) (haδ : a ≤ δ) (hδB : δ ≤ B)
    (hC0 : 0 ≤ C0) (hC1 : 0 ≤ C1)
    (hder : ∀ d ∈ Icc a δ, HasDerivAt A (A' d) d)
    (hA : ∀ d ∈ Icc (0:ℝ) δ, ‖A d‖ ≤ C0)
    (hA' : ∀ d ∈ Icc a δ, ‖A' d‖ ≤ C1)
    (hi : IntervalIntegrable (neutralNF584AmplitudeDeriv B A A') volume a δ)
    (hfull : IntervalIntegrable
      (fun d => neutralNF584Amplitude B A d * neutralNF584Phase t d) volume 0 δ)
    (ht : 0 < |t|) (hsplit : |t|*a = 1) :
    |t| * ‖∫ d in (0:ℝ)..δ, neutralNF584Amplitude B A d * neutralNF584Phase t d‖ ≤
      C0*(3*neutralNF584LogKernel B a+1) +
        C1*δ*(neutralNF584LogKernel B δ+1) := by
  let f := fun d => neutralNF584Amplitude B A d * neutralNF584Phase t d
  have hnear : ‖∫ d in (0:ℝ)..a, f d‖ ≤
      C0*a*(neutralNF584LogKernel B a+1) :=
    neutralNF584NearPanel A B a C0 ha (haδ.trans hδB)
      (fun d hd => hA d ⟨hd.1,hd.2.trans haδ⟩) t
  have hhigh := neutralNF584HighPanel A A' B a δ C0 C1 t ha haδ hδB hC0 hC1
    hder (fun d hd => hA d ⟨ha.le.trans hd.1,hd.2⟩) hA' hi
  have hnear' := mul_le_mul_of_nonneg_left hnear ht.le
  have hsplit' : |t|*(C0*a*(neutralNF584LogKernel B a+1)) =
      C0*(neutralNF584LogKernel B a+1) := by
    calc
      _ = (|t|*a)*(C0*(neutralNF584LogKernel B a+1)) := by ring
      _ = _ := by rw [hsplit,one_mul]
  rw [hsplit'] at hnear'
  have hsub1 : uIcc (0:ℝ) a ⊆ uIcc 0 δ := by
    rw [uIcc_of_le ha.le,uIcc_of_le (ha.le.trans haδ)]
    exact Icc_subset_Icc le_rfl haδ
  have hsub2 : uIcc a δ ⊆ uIcc 0 δ := by
    rw [uIcc_of_le haδ,uIcc_of_le (ha.le.trans haδ)]
    exact Icc_subset_Icc ha.le le_rfl
  have hadd := intervalIntegral.integral_add_adjacent_intervals
    (hfull.mono_set hsub1) (hfull.mono_set hsub2)
  change |t|*‖∫ d in (0:ℝ)..δ, f d‖ ≤ _
  rw [← hadd]
  have htri := mul_le_mul_of_nonneg_left
    (norm_add_le (∫ d in (0:ℝ)..a, f d) (∫ d in a..δ, f d)) ht.le
  change |t| * ‖∫ d in a..δ, f d‖ ≤ _ at hhigh
  nlinarith only [htri,hnear',hhigh]

end
end WeilDefect
