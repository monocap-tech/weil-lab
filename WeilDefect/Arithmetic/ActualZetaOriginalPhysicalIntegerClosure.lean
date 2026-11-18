import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerPayments
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalBooleanClosure

namespace WeilDefect
noncomputable section

/-! NF626: replace only the fourth reference gate by a checked
integer product cache and scalar payment comparisons. No analytic
premise or numerical truth has disappeared. -/

theorem neutralNF626OriginalPhysical_of_fast_checks
    (bank : Array NF624KeyTable) (s : NF626ScaledInputs) (c : NF626CenterCache)
    (hbank : neutralNF624BankCheck bank = true)
    (hcov : neutralNF624CoverageCheck bank (neutralNF624Index bank) = true)
    (hentry : neutralNF625EntryCheck
      (neutralNF624Lookup bank (neutralNF624Index bank)) s.payment = true)
    (hcache : c.check s = true)
    (hpay : c.fastPayCheck s = true) :
    ∃! a : Fin 242 → ℝ,
      neutralNF606Apply neutralNF606PhysicalH a = neutralNF612RHS ∧
      neutralNF587SourceInFrozenBox a neutralNF604OriginalCritical :=
  neutralNF625OriginalPhysical_of_checks bank s.payment hbank hcov hentry
    (c.payment_of_fast s (c.check_sound s hcache) hpay)

end
end WeilDefect
