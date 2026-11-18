import WeilDefect.Arithmetic.ActualZetaOriginalCollarLiteralArch
import WeilDefect.Arithmetic.ActualZetaOriginalCollarPoleBound
import WeilDefect.Arithmetic.ActualZetaOriginalSupportCoercivityTransfer

namespace WeilDefect
noncomputable section
open MeasureTheory FourierTransform
open scoped SchwartzMap FourierTransform ComplexConjugate

theorem neutralNF600SmoothWeil_split (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x=0) :
    neutralNF598SmoothWeil s =
      neutralNF600Arch s-(neutralNF600Prime s).re+(neutralNF600Pole s).re := by
  unfold neutralNF598SmoothWeil Zeta23.EF.literatureRHS
  simp only [Complex.add_re,Complex.sub_re]
  have h := neutralNF600LiteralArch_eq s hs
  unfold neutralNF600Prime neutralNF600Pole
  simp only [Complex.add_re] at *
  linarith only [h]

/-- Strong local signed margin, not full-space Weil positivity. -/
theorem neutralNF600SmoothCollarLower :
    neutralNF599SmoothCollarLower (2/5) := by
  intro s hs
  have ha := neutralNF600ArchLower s hs (neutralNF600Arch_integrable s)
  have hp := neutralNF600Prime_bound_actual s hs
  have hq := neutralNF600Pole_bound s hs
  rw [neutralNF600SmoothWeil_split s hs]
  change (2/5:ℝ)*neutralNF600Mass s ≤ _
  change (104/125:ℝ)*neutralNF600Mass s ≤ neutralNF600Arch s at ha
  linarith only [ha,hp,hq,le_abs_self (neutralNF600Prime s).re,neg_abs_le (neutralNF600Pole s).re]

theorem neutralNF600NF407GraphLower (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) :
    ∃ (hLp : MemLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) 2 volume)
      (K : NeutralActualZetaSourceDomain (11/10:ℝ)),
      neutralNF598GraphPhysical (11/10) K =
        hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) ∧
      (2/5:ℝ)*‖neutralNF598GraphPhysical (11/10) K‖^2 ≤
        neutralNF598GraphWeil (11/10) K :=
  neutralNF599NF407GraphLower a b (2/5) neutralNF600SmoothCollarLower

end
end WeilDefect
