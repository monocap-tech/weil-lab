import WeilDefect.Arithmetic.ActualZetaOriginalStripLogConvergence
import WeilDefect.Arithmetic.ActualZetaOriginalLogStripGraphLimit

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped ComplexConjugate

/-!
NF575: physical L² convergence and a common endpoint-log strip
majorant now suffice for complete graph convergence, without
having to assume the logarithmic Hilbert convergence separately.
The actual supported target and seed estimates remain explicit.
-/

theorem neutralNF575OriginalPhysicalSequence_fullGraph_of_strip
    (f : RealComplexL2) (g : ℕ → RealComplexL2)
    (hf : ∀ᵐ x ∂volume, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → f x = 0)
    (hg : ∀ n, ∀ᵐ x ∂volume, x ∉ Set.Icc (-(11/10:ℝ)) (11/10:ℝ) → g n x = 0)
    (hl2 : Tendsto g atTop (nhds f))
    (M : ℝ) (hM : 0 ≤ M)
    (hft : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation (11/10:ℝ) z f‖ ≤ M*neutralNF575StripEnvelope z.re)
    (hgt : ∀ n (z : ℂ), |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation (11/10:ℝ) z (g n)‖ ≤ M*neutralNF575StripEnvelope z.re) :
    ∃ (K : NeutralActualZetaSourceDomain (11/10:ℝ))
      (G : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ)),
      neutralLogPhysical (neutralActualZetaSourcePhysical (11/10:ℝ) K).val = f ∧
      (∀ n, neutralLogPhysical (neutralActualZetaSourcePhysical (11/10:ℝ) (G n)).val = g n) ∧
      Tendsto G atTop (nhds K) := by
  obtain ⟨k,v,hk,hv,hconv⟩ :=
    neutralNF575PhysicalSequence_logLimit_of_strip (11/10:ℝ) f g
      hf hg hl2 M hM hft hgt
  have hkt : ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation (11/10:ℝ) z (neutralLogPhysical k.val)‖ ≤
        M*neutralNF574StripEnvelope z.re := by
    intro z hz
    rw [hk]
    exact hft z hz
  have hvt : ∀ n (z : ℂ), |z.im| ≤ 1/2 →
      ‖neutralWindowEvaluation (11/10:ℝ) z (neutralLogPhysical (v n).val)‖ ≤
        M*neutralNF574StripEnvelope z.re := by
    intro n z hz
    rw [hv n]
    exact hgt n z hz
  obtain ⟨K,G,hK,hG,hlim⟩ :=
    neutralNF574OriginalFullSourceLimit_of_stripEnvelope k v hconv M hM hkt hvt
  refine ⟨K,G,?_,?_,hlim⟩
  · rw [hK,hk]
  · intro n
    rw [hG n,hv n]

end
end WeilDefect
