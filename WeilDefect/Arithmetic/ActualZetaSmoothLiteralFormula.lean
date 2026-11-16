import WeilDefect.Arithmetic.ActualZetaLiteralFormula

namespace WeilDefect
noncomputable section

/-!
NF530: The authentic zeta explicit formula is not restricted to Green
synthesis. This lemma applies it to the *original window correlation*
of arbitrary physical inputs, once C² regularity, compact support, and
full-divisor summability are proved for the concrete test.

No source-representation assumption, Green density or RH is used.
-/

/-- Generic complex-frequency correlation -> the actual full-divisor explicit
formula. The hypotheses are intended to be discharged for smooth compact
collar-supported tests; no test admissibility is manufactured here. -/
theorem neutralActualZetaWindowCorrelation_literature
    (a : ℝ) (f g : RealComplexL2)
    (hreg : ContDiff ℝ 2 (neutralWindowCorrelation a f g))
    (hcompact : HasCompactSupport (neutralWindowCorrelation a f g))
    (hsum : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      conj (neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q)) f) *
        neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q) g)) :
    (∑' q : NeutralActualZetaDivisorCoordinate,
      conj (neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q)) f) *
        neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q) g) =
      Zeta23.EF.literatureRHS (neutralWindowCorrelation a f g) := by
  have hsum' : Summable (fun q : NeutralActualZetaDivisorCoordinate =>
      neutralRawTransform (neutralWindowCorrelation a f g)
        (neutralActualZetaDivisorOrdinate q)) := by
    convert hsum using 1
    funext q
    exact (neutralWindowCorrelation_rawTransform a f g
      (neutralActualZetaDivisorOrdinate q)).symm
  calc
    (∑' q : NeutralActualZetaDivisorCoordinate,
      conj (neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q)) f) *
        neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q) g) =
      ∑' q : NeutralActualZetaDivisorCoordinate,
        neutralRawTransform (neutralWindowCorrelation a f g)
          (neutralActualZetaDivisorOrdinate q) := by
            apply tsum_congr
            intro q
            exact (neutralWindowCorrelation_rawTransform a f g
              (neutralActualZetaDivisorOrdinate q)).symm
    _ = ∑' ρ : (Zeta23.zetaZeros Zeta23.zetaSeam).carrier,
        ((Zeta23.zetaZeros Zeta23.zetaSeam).mult ρ : ℂ) *
          Zeta23.paperFT (neutralWindowCorrelation a f g)
            (Zeta23.gammaOf ρ.val) :=
      neutralActualZetaDivisor_tsum_literature _ hsum'
    _ = Zeta23.EF.literatureRHS (neutralWindowCorrelation a f g) :=
      ((Zeta23.WeilEF.EF_lit_zeta Zeta23.zetaSeam)
        (neutralWindowCorrelation a f g) hreg hcompact).2

end
end WeilDefect
