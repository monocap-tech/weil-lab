import WeilDefect.Arithmetic.ActualZetaOriginalAnalyticNonzeroGraph
import WeilDefect.Arithmetic.ActualZetaOriginalNF407SignedMarginTransfer
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSolveResidual

namespace WeilDefect
noncomputable section
open MeasureTheory Filter
open scoped SchwartzMap ComplexConjugate

/-! NF608: for every coefficient choice in the authentic frozen
box, the certified remote nonvanishing and graph lower transfer
give every strict margin below the universal local constant.
No endpoint checker, exact inverse evaluation or U400 is needed.
The local smooth inequality is still an explicit premise. -/

theorem neutralNF608OriginalCorrectedMargin_of_box
    (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b)
    (c d : ℝ) (hd : 0 < d) (hdc : d < c)
    (hlocal : neutralNF599SmoothCollarLower c) :
    ∃ (hLp : MemLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) 2 volume)
      (K : NeutralActualZetaSourceDomain (11/10:ℝ))
      (f : ℕ → 𝓢(ℝ,ℂ)),
      neutralNF598GraphPhysical (11/10) K =
        hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) ∧
      0 < d*‖neutralNF598GraphPhysical (11/10) K‖^2 ∧
      d*‖neutralNF598GraphPhysical (11/10) K‖^2 <
        neutralNF598GraphWeil (11/10) K ∧
      (∀ n x, conj (f n x) = f n x) ∧
      (∀ n x, f n (-x) = -f n x) ∧
      (∀ n x, x ∉ neutralNF543OriginalCollars → f n x = 0) ∧
      (∀ n, neutralNF546OriginalSelectedMoments ((f n).toLp 2 volume) =
        neutralNF546OriginalSelectedMoments (neutralNF598GraphPhysical (11/10) K)) ∧
      (∀ᶠ n in atTop, d*‖(f n).toLp 2 volume‖^2 < neutralNF598SmoothWeil (f n)) := by
  obtain ⟨hLp,K,hK,hlo⟩ := neutralNF599NF407GraphLower a b c hlocal
  have hn : neutralNF598GraphPhysical (11/10) K ≠ 0 := by
    rw [hK]
    exact neutralNF603OriginalCarrier_nonzero_of_box a b hbox hLp
  have hsq : 0 < ‖neutralNF598GraphPhysical (11/10) K‖^2 :=
    sq_pos_of_pos (norm_pos_iff.mpr hn)
  have hpos := mul_pos hd hsq
  have hstrict := (mul_lt_mul_of_pos_right hdc hsq).trans_le hlo
  obtain ⟨f,hreal,hodd,hsupp,hmom,hevent⟩ :=
    neutralNF598NF407SmoothMargin a b hLp K hK d hstrict
  exact ⟨hLp,K,f,hK,hpos,hstrict,hreal,hodd,hsupp,hmom,hevent⟩

/-- The graph of the exact transformed physical solution has a
strict positive local margin, conditional on the residual inputs
and local inequality. The historically frozen frame binding is
NOT supplied by this theorem. -/
theorem neutralNF608PhysicalResidual_positive
    (D : Fin 242 → Fin 242 → ℝ) (y y0 : Fin 242 → ℝ)
    (r : ℝ) (hr : 0≤r)
    (hrow : ∀ i, (∑ j, |neutralNF606Defect (neutralNF606TransformedH D) i j|) ≤ 1/100)
    (hsolve : ∀ i, neutralNF606Apply (neutralNF606TransformedH D) y i =
      neutralNF606TransformedRHS D i)
    (hres : ∀ i, |neutralNF606TransformedRHS D i -
      neutralNF606Apply (neutralNF606TransformedH D) y0 i| ≤ r)
    (hpay : ∀ i, |neutralNF606Apply D y0 i-neutralNF587SelectedMid i|+
      (∑ j, |D i j|)*(2*r) ≤ neutralNF587SelectedRadius i)
    (hlocal : neutralNF599SmoothCollarLower (2/5)) :
    ∃ (hLp : MemLp (neutralNF575OriginalEndpoint
        (neutralNF587Source (neutralNF606Apply D y) neutralNF604OriginalCritical)) 2 volume)
      (K : NeutralActualZetaSourceDomain (11/10:ℝ)),
      neutralNF598GraphPhysical (11/10) K =
        hLp.toLp (neutralNF575OriginalEndpoint
          (neutralNF587Source (neutralNF606Apply D y) neutralNF604OriginalCritical)) ∧
      0 < neutralNF598GraphWeil (11/10) K :=
  neutralNF603NF407Graph_positive_of_box (neutralNF606Apply D y) neutralNF604OriginalCritical
    (neutralNF606OriginalBox_of_physical_residual D y y0 r hr hrow hsolve hres hpay)
    (2/5) (by norm_num) hlocal

end
end WeilDefect
