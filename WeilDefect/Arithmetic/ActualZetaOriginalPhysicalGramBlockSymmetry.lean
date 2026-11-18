import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramTerms

namespace WeilDefect
noncomputable section

/-! NF657: symmetry belongs to the authentic physical H, not the
rounded or archived surrogate. The source pair evaluator is commutative
because it uses only the product of coefficients and sums of exponents
and degrees. This establishes symmetry before interval coercivity. -/

theorem neutralNF657Pair_comm (a b : NF607Term) :
    neutralNF607Pair a b = neutralNF607Pair b a := by
  unfold neutralNF607Pair
  rw [add_comm a.exponent b.exponent, add_comm a.degree b.degree]
  ring

theorem neutralNF657SelectedH_symm (i j : Fin 242) :
    neutralNF607SelectedH i j = neutralNF607SelectedH j i := by
  unfold neutralNF607SelectedH
  rw [neutralNF657Pair_comm (neutralNF607SelectedTerm i true)
    (neutralNF607SelectedTerm j true)]
  rw [neutralNF657Pair_comm (neutralNF607SelectedTerm i true)
    (neutralNF607SelectedTerm j false)]
  rw [neutralNF657Pair_comm (neutralNF607SelectedTerm i false)
    (neutralNF607SelectedTerm j true)]
  rw [neutralNF657Pair_comm (neutralNF607SelectedTerm i false)
    (neutralNF607SelectedTerm j false)]
  ring

theorem neutralNF657PhysicalH_symm (i j : Fin 242) :
    neutralNF606PhysicalH i j = neutralNF606PhysicalH j i := by
  apply Complex.ofReal_injective
  calc
    (neutralNF606PhysicalH i j : ℂ) =
        neutralNF607SelectedH i j := (neutralNF607SelectedH_eq i j).symm
    _ = neutralNF607SelectedH j i := neutralNF657SelectedH_symm i j
    _ = (neutralNF606PhysicalH j i : ℂ) := neutralNF607SelectedH_eq j i

end
end WeilDefect
