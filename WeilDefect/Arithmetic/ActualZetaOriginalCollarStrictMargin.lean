import WeilDefect.Arithmetic.ActualZetaOriginalCollarCoercivity
import WeilDefect.Arithmetic.ActualZetaOriginalCollarPrimeSharpen
import WeilDefect.Arithmetic.ActualZetaOriginalResidualSignedMargin

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap ComplexConjugate

theorem neutralNF610SmoothCollarLower :
    neutralNF599SmoothCollarLower (17/40) := by
  intro s hs
  have ha := neutralNF600ArchLower s hs (neutralNF600Arch_integrable s)
  have hp := neutralNF610Prime_bound_actual s hs
  have hq := neutralNF600Pole_bound s hs
  rw [neutralNF600SmoothWeil_split s hs]
  change (17/40:ℝ)*neutralNF600Mass s ≤ _
  change (104/125:ℝ)*neutralNF600Mass s ≤ neutralNF600Arch s at ha
  linarith only [ha,hp,hq,le_abs_self (neutralNF600Prime s).re,neg_abs_le (neutralNF600Pole s).re]

theorem neutralNF610OriginalCorrectedMargin (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b) :=
  neutralNF608OriginalCorrectedMargin_of_box a b hbox (17/40) (2/5)
    (by norm_num) (by norm_num) neutralNF610SmoothCollarLower

end
end WeilDefect
