import WeilDefect.Arithmetic.ActualZetaOddPhysicalSampleSummability
import WeilDefect.Arithmetic.ActualZetaSourceGraph

namespace WeilDefect
noncomputable section
open InnerProductSpace
open scoped ENNReal

/-!
NF536: An arbitrary logarithmic physical vector satisfying the true
actual-divisor positive/negative sample ℓ² conditions has a literal
full source-graph lift, not merely a Green-packet lift. The conditions
are NOT asserted for arbitrary physical vectors.
-/

/-- Generic, source-exact full-divisor graph lift from the two necessary
square-summability hypotheses. Retains every actual multiplicity copy.
No Green synthesis or density assumption. -/
def neutralActualZetaFullSourceLiftOfSquareSummable
    (a : ℝ) (f : NeutralLogHilbertCarrier a)
    (hp : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) f‖ ^ 2))
    (hn : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) f‖ ^ 2)) :
    NeutralActualZetaSourceDomain a := by
  let p : NeutralActualZetaGreenCoefficients := ⟨
    fun q => inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) f,
    memℓp_gen (by simpa only [ENNReal.toReal_ofNat, Real.rpow_two] using hp)⟩
  let n : NeutralActualZetaGreenCoefficients := ⟨
    fun q => inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) f,
    memℓp_gen (by simpa only [ENNReal.toReal_ofNat, Real.rpow_two] using hn)⟩
  exact ⟨(f, p, n), fun _ => ⟨rfl, rfl⟩⟩

/-- Exact same-vector physical custody for the generic lift. -/
theorem neutralActualZetaFullSourceLiftOfSquareSummable_physical
    (a : ℝ) (f : NeutralLogHilbertCarrier a)
    (hp : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) f‖ ^ 2))
    (hn : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) f‖ ^ 2)) :
    neutralActualZetaSourcePhysical a
      (neutralActualZetaFullSourceLiftOfSquareSummable a f hp hn) = f := rfl

/-- Generic lift retains exactly the two actual source sample identities. -/
theorem neutralActualZetaFullSourceLiftOfSquareSummable_samples
    (a : ℝ) (f : NeutralLogHilbertCarrier a)
    (hp : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) f‖ ^ 2))
    (hn : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      ‖inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) f‖ ^ 2))
    (q : NeutralActualZetaDivisorCoordinate) :
    neutralActualZetaPositiveAnalysis a
      (neutralActualZetaFullSourceLiftOfSquareSummable a f hp hn) q =
        inner ℂ (neutralLogPositivePairSource a (neutralActualZetaDivisorOrdinate q)) f ∧
    neutralActualZetaNegativeAnalysis a
      (neutralActualZetaFullSourceLiftOfSquareSummable a f hp hn) q =
        inner ℂ (neutralLogNegativePairSource a (neutralActualZetaDivisorOrdinate q)) f := by
  simpa only [neutralActualZetaFullSourceLiftOfSquareSummable_physical] using
    neutralActualZetaSourceAnalysis_sampling a
      (neutralActualZetaFullSourceLiftOfSquareSummable a f hp hn) q

end
end WeilDefect
