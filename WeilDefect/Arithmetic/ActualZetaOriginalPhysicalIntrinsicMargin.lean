import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSystemEquiv
import WeilDefect.Arithmetic.ActualZetaOriginalResidualSignedMargin

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped SchwartzMap ComplexConjugate

/-- Frame-independent statement of the ultimate physical source:
the frame enters only in the proof of the exact physical solution
and frozen box, not in its characterization or corrected margin. -/
theorem neutralNF612OriginalPhysical_corrected
    (D : Fin 242 → Fin 242 → ℝ) (y0 : Fin 242 → ℝ)
    (r : ℝ) (hr : 0≤r)
    (hrow : ∀ i, (∑ j, |neutralNF606Defect (neutralNF606TransformedH D) i j|) ≤ 1/100)
    (hres : ∀ i, |neutralNF606TransformedRHS D i -
      neutralNF606Apply (neutralNF606TransformedH D) y0 i| ≤ r)
    (hpay : ∀ i, |neutralNF606Apply D y0 i-neutralNF587SelectedMid i|+
      (∑ j, |D i j|)*(2*r) ≤ neutralNF587SelectedRadius i)
    (c d : ℝ) (hd : 0<d) (hdc : d<c)
    (hlocal : neutralNF599SmoothCollarLower c) :
    ∃ (a : Fin 242 → ℝ)
      (hLp : MemLp (neutralNF575OriginalEndpoint
        (neutralNF587Source a neutralNF604OriginalCritical)) 2 volume)
      (K : NeutralActualZetaSourceDomain (11/10:ℝ))
      (f : ℕ → 𝓢(ℝ,ℂ)),
      neutralNF606Apply neutralNF606PhysicalH a = neutralNF612RHS ∧
      (∀ a', neutralNF606Apply neutralNF606PhysicalH a' = neutralNF612RHS → a'=a) ∧
      neutralNF587SourceInFrozenBox a neutralNF604OriginalCritical ∧
      neutralNF598GraphPhysical (11/10) K =
        hLp.toLp (neutralNF575OriginalEndpoint
          (neutralNF587Source a neutralNF604OriginalCritical)) ∧
      0 < d*‖neutralNF598GraphPhysical (11/10) K‖^2 ∧
      d*‖neutralNF598GraphPhysical (11/10) K‖^2 <
        neutralNF598GraphWeil (11/10) K ∧
      (∀ n x, conj (f n x) = f n x) ∧
      (∀ n x, f n (-x) = -f n x) ∧
      (∀ n x, x ∉ neutralNF543OriginalCollars → f n x = 0) ∧
      (∀ n, neutralNF546OriginalSelectedMoments ((f n).toLp 2 volume) =
        neutralNF546OriginalSelectedMoments (neutralNF598GraphPhysical (11/10) K)) ∧
      (∀ᶠ n in atTop, d*‖(f n).toLp 2 volume‖^2 < neutralNF598SmoothWeil (f n)) := by
  obtain ⟨a,⟨ha,hbox⟩,_⟩ := neutralNF612OriginalPhysicalSolve D y0 r hr hrow hres hpay
  have huniq (a' : Fin 242 → ℝ)
      (ha' : neutralNF606Apply neutralNF606PhysicalH a' = neutralNF612RHS) : a'=a :=
    (neutralNF612PhysicalH_bijective D hrow).1 (ha'.trans ha.symm)
  obtain ⟨hLp,K,f,hK,hpos,hstrict,hreal,hodd,hsupp,hmom,hevent⟩ :=
    neutralNF608OriginalCorrectedMargin_of_box a neutralNF604OriginalCritical hbox c d hd hdc hlocal
  exact ⟨a,hLp,K,f,ha,huniq,hbox,hK,hpos,hstrict,hreal,hodd,hsupp,hmom,hevent⟩

end
end WeilDefect
