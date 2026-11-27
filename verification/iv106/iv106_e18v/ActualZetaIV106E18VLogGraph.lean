import WeilDefect.Arithmetic.ActualZetaIV106E18VBump
import WeilDefect.Arithmetic.ActualZetaIV106E18SFourierGraph

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric Filter FourierTransform InnerProductSpace
open scoped SchwartzMap Topology FourierTransform

/-- Extract a sequence of genuine supported smooth graph pairs, with
both physical coordinates converging. No independent derivative
sequence is chosen. -/
theorem neutralIV106E18VSequence (A B : ℝ) (f d : RealComplexL2)
    (h : (f,d) ∈ neutralIV106E18UGraphSpace A B) :
    ∃ s : ℕ → 𝓢(ℝ,ℂ),
      (∀ n x, x ∉ Icc A B → s n x = 0) ∧
      Tendsto (fun n => (s n).toLp 2 volume) atTop (𝓝 f) ∧
      Tendsto (fun n => (SchwartzMap.derivCLM ℂ ℂ (s n)).toLp 2 volume)
        atTop (𝓝 d) := by
  classical
  have hc : (f,d) ∈ closure (neutralIV106E18UGraphCore A B :
      Set neutralIV106E18UGraphAmbient) := h
  obtain ⟨v,hv,ht⟩ := mem_closure_iff_seq_limit.mp hc
  have hex (n : ℕ) : ∃ s : 𝓢(ℝ,ℂ), (∀ x ∉ Icc A B, s x = 0) ∧
      v n = (s.toLp 2 volume,(SchwartzMap.derivCLM ℂ ℂ s).toLp 2 volume) :=
    hv n
  choose s hs he using hex
  have h1 := continuous_fst.continuousAt.tendsto.comp ht
  have h2 := continuous_snd.continuousAt.tendsto.comp ht
  change Tendsto (fun n => (v n).1) atTop (𝓝 f) at h1
  change Tendsto (fun n => (v n).2) atTop (𝓝 d) at h2
  refine ⟨s,hs,?_,?_⟩
  · simpa only [he] using h1
  · simpa only [he] using h2

def neutralIV106E18VScale : ℂ := (2*(Real.pi:ℂ)*Complex.I)⁻¹

/-- Graph membership discharges the simultaneous-limit premise of the
E18S Fourier receiver, with the original physical derivative scaling. -/
theorem neutralIV106E18VWitness (A B : ℝ) (f d : RealComplexL2)
    (h : (f,d) ∈ neutralIV106E18UGraphSpace A B) :
    ∀ᵐ ξ ∂volume, (𝓕 (neutralIV106E18VScale • d) : RealComplexL2) ξ =
      (ξ:ℂ)*(𝓕 f : RealComplexL2) ξ := by
  obtain ⟨s,_,hf,hd⟩ := neutralIV106E18VSequence A B f d h
  have hn : Tendsto (fun n => (neutralIV106E18SNormalized (s n)).toLp 2 volume)
      atTop (𝓝 (neutralIV106E18VScale • d)) := by
    have hh := tendsto_const_nhds.smul hd (c := neutralIV106E18VScale)
    change Tendsto (fun n => neutralIV106E18VScale •
      (SchwartzMap.toLpCLM ℂ ℂ 2 volume (SchwartzMap.derivCLM ℂ ℂ (s n))))
      atTop (𝓝 (neutralIV106E18VScale • d)) at hh
    simpa only [neutralIV106E18SNormalized, ← map_smul,
      neutralIV106E18VScale] using hh
  exact neutralIV106E18SFourier_limit s f _ hf hn

/-- Use the original NF541 carrier admission theorem, not a new carrier. -/
theorem neutralIV106E18VAdmission (A B a : ℝ) (f d : RealComplexL2)
    (h : (f,d) ∈ neutralIV106E18UGraphSpace A B)
    (hs : ∀ᵐ x ∂volume, x ∉ Icc (-a) a → f x = 0) :
    ∃ p : NeutralLogHilbertCarrier a, neutralLogPhysical p.val = f := by
  exact neutralPhysicalL2_hasOriginalLogHilbertCarrier_of_derivativeWitness
    a f (neutralIV106E18VScale • d) hs
    (neutralIV106E18SWitness_sq f _ (neutralIV106E18VWitness A B f d h))

/-- Exact L2 square integral, in the frozen physical L2 type. -/
theorem neutralIV106E18VL2sq (u : RealComplexL2) :
    (∫ x : ℝ, ‖u x‖^2) = ‖u‖^2 := by
  have h := inner_self_eq_norm_sq_to_K (𝕜 := ℂ) u
  rw [MeasureTheory.L2.inner_def] at h
  simp only [inner_self_eq_norm_sq_to_K] at h
  change (∫ x : ℝ, (‖u x‖ : ℂ)^2) = (‖u‖ : ℂ)^2 at h
  simp only [← Complex.ofReal_pow] at h
  rw [integral_complex_ofReal] at h
  exact Complex.ofReal_injective h

/-- Quantitative logarithmic energy in the joint graph norm, by the
original Fourier isometry and E18S multiplier bound. -/
theorem neutralIV106E18VEnergy (A B : ℝ) (f d : RealComplexL2)
    (h : (f,d) ∈ neutralIV106E18UGraphSpace A B) :
    (∫ ξ, logarithmicFourierWeight ξ * ‖(𝓕 f : RealComplexL2) ξ‖^2) ≤
      (Real.exp 1+1)*‖f‖^2 + ‖neutralIV106E18VScale‖^2*‖d‖^2 := by
  have he := neutralIV106E18SLog_bound f (neutralIV106E18VScale • d)
    (neutralIV106E18VWitness A B f d h)
  rw [neutralIV106E18VL2sq,neutralIV106E18VL2sq] at he
  change _ ≤ (Real.exp 1+1)*‖(Lp.fourierTransformₗᵢ ℝ ℂ) f‖^2 +
    ‖(Lp.fourierTransformₗᵢ ℝ ℂ) (neutralIV106E18VScale • d)‖^2 at he
  rw [(Lp.fourierTransformₗᵢ ℝ ℂ).norm_map,
    (Lp.fourierTransformₗᵢ ℝ ℂ).norm_map,norm_smul,mul_pow] at he
  exact he

/-- Errors themselves are graph pairs, by subtraction in the same
closed submodule; the log bound applies to the actual difference. -/
theorem neutralIV106E18VError (A B : ℝ) (f d : RealComplexL2)
    (h : (f,d) ∈ neutralIV106E18UGraphSpace A B)
    (s : 𝓢(ℝ,ℂ)) (hs : ∀ x ∉ Icc A B, s x = 0) :
    (∫ ξ, logarithmicFourierWeight ξ *
      ‖(𝓕 (s.toLp 2 volume-f) : RealComplexL2) ξ‖^2) ≤
      (Real.exp 1+1)*‖s.toLp 2 volume-f‖^2 +
        ‖neutralIV106E18VScale‖^2*
          ‖(SchwartzMap.derivCLM ℂ ℂ s).toLp 2 volume-d‖^2 := by
  have hc : (s.toLp 2 volume,(SchwartzMap.derivCLM ℂ ℂ s).toLp 2 volume) ∈
      neutralIV106E18UGraphCore A B := ⟨s,hs,rfl⟩
  have hc' := (neutralIV106E18UGraphCore A B).le_topologicalClosure hc
  have hsub := (neutralIV106E18UGraphSpace A B).sub_mem hc' h
  exact neutralIV106E18VEnergy A B _ _ hsub

/-- One exact affine observation receiver, now with authentic log-energy
error in addition to the two physical graph errors. -/
theorem neutralIV106E18VMatch {F : Type*}
    [NormedAddCommGroup F] [NormedSpace ℂ F] [FiniteDimensional ℂ F]
    (A B : ℝ) (T : RealComplexL2 →L[ℂ] F)
    (f d : RealComplexL2) (h : (f,d) ∈ neutralIV106E18UGraphSpace A B)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ s : 𝓢(ℝ,ℂ), (∀ x ∉ Icc A B, s x = 0) ∧
      T (s.toLp 2 volume) = T f ∧
      dist (s.toLp 2 volume) f < ε ∧
      dist ((SchwartzMap.derivCLM ℂ ℂ s).toLp 2 volume) d < ε ∧
      (∫ ξ, logarithmicFourierWeight ξ *
        ‖(𝓕 (s.toLp 2 volume-f) : RealComplexL2) ξ‖^2) ≤
        (Real.exp 1+1+‖neutralIV106E18VScale‖^2)*ε^2 := by
  obtain ⟨s,hs,hT,hf,hd⟩ := neutralIV106E18UGraph_match A B T f d h ε hε
  refine ⟨s,hs,hT,hf,hd,(neutralIV106E18VError A B f d h s hs).trans ?_⟩
  rw [dist_eq_norm] at hf hd
  have hf2 := pow_le_pow_left₀ (norm_nonneg _) hf.le 2
  have hd2 := pow_le_pow_left₀ (norm_nonneg _) hd.le 2
  calc
    _ ≤ (Real.exp 1+1)*ε^2 + ‖neutralIV106E18VScale‖^2*ε^2 :=
      add_le_add (mul_le_mul_of_nonneg_left hf2 (by positivity))
        (mul_le_mul_of_nonneg_left hd2 (sq_nonneg _))
    _ = _ := by ring

#print axioms neutralIV106E18VSequence
#print axioms neutralIV106E18VWitness
#print axioms neutralIV106E18VAdmission
#print axioms neutralIV106E18VL2sq
#print axioms neutralIV106E18VEnergy
#print axioms neutralIV106E18VError
#print axioms neutralIV106E18VMatch
end
end WeilDefect
