import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalShapedBank
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalTriangularEntryCustody

namespace WeilDefect
open Finset MeasureTheory Filter
open scoped SchwartzMap ComplexConjugate
noncomputable section

/-- The local analytic receipts suffice directly for the original
unique physical solve. No second reference-Boolean replay is needed. -/
theorem neutralNF690OriginalPhysical_of_tables
    (bank : Array NF624KeyTable)
    (s : NF626ScaledInputs) (c : NF626CenterCache)
    (hbank : ∀ i < bank.size, neutralNF690TableSound (neutralNF624BankRead bank i))
    (hcov : neutralNF624CoverageCheck bank (neutralNF624Index bank) = true)
    (htri : neutralNF673EntryCheck
      (neutralNF624Lookup bank (neutralNF624Index bank)) s.payment = true)
    (hcache : c.check s = true)
    (hpay : c.fastPayCheck s = true) :
    ∃! a : Fin 242 → ℝ,
      neutralNF606Apply neutralNF606PhysicalH a = neutralNF612RHS ∧
      neutralNF587SourceInFrozenBox a neutralNF604OriginalCritical := by
  have hm := neutralNF690AllMoments_of_tables bank (neutralNF624Index bank)
    hbank (neutralNF624Index_coverage bank hcov)
  have he := neutralNF673EntryCheck_sound
    (neutralNF624Lookup bank (neutralNF624Index bank)) s.payment hm htri
  have hv : c.Valid s := c.check_sound s hcache
  have hp : s.payment.check = true := c.payment_of_fast s hv hpay
  exact s.payment.check_sound hp he.1 he.2

#print axioms neutralNF690OriginalPhysical_of_tables

end
end WeilDefect
