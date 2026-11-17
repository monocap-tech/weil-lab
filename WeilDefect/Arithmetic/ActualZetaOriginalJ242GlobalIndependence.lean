import WeilDefect.Arithmetic.ActualZetaOriginalJ242SquareKernelTransport
import WeilDefect.Arithmetic.ActualZetaOriginalJ242GlobalCombinationJets
import WeilDefect.Arithmetic.ActualZetaOriginalJ242ActualOddJetKernelClosure

namespace WeilDefect
noncomputable section

/-!
NF569 — original full analytic source independence. The earlier
NF568 candidate left-kernel contradiction is now transported to
the right kernel and hence to genuine global real and complex
source combinations. No physical Gram hypothesis occurs.
-/

/-- The actual original square odd-jet matrix has trivial RIGHT
kernel, by the NF568 actual left-kernel theorem and finite-
dimensional square-matrix transport. -/
theorem neutralNF569OriginalActualOddJetMatrix_rightKernel_zero
    (b : Fin 242 → ℝ)
    (hker : ∀ n : Fin 242,
      (∑ j : Fin 242, neutralNF560ActualOriginalOddJetMatrix n j * b j) = 0) :
    b = 0 :=
  neutralNF569RealSquare_rightKernel_zero_of_leftKernel_zero
    neutralNF560ActualOriginalOddJetMatrix
    neutralNF568OriginalActual242OddJetMatrix_leftKernel_zero b hker

/-- Global independence of the 242 original real generators.
Differentiating the vanishing combination gives its actual
right-kernel vector, already discharged above. -/
theorem neutralNF569OriginalRealCombination_globalIndependence
    (b : Fin 242 → ℝ)
    (hzero : ∀ x : ℝ, neutralNF569OriginalRealCombination b x = 0) :
    b = 0 :=
  neutralNF569OriginalActualOddJetMatrix_rightKernel_zero b
    (neutralNF569OriginalRealCombination_zero_forcesRightKernel b hzero)

/-- Global independence for arbitrary COMPLEX coefficients of
the same 242 original real analytic source functions. Taking
real and imaginary parts gives two exact real source
combinations, each of which vanishes identically.
This is independent of any Gram-positivity premise. -/
theorem neutralNF569OriginalComplexCombination_globalIndependence
    (d : Fin 242 → ℂ)
    (hzero : ∀ x : ℝ, neutralNF569OriginalComplexCombination d x = 0) :
    d = 0 := by
  have hre : (fun j : Fin 242 => (d j).re) = 0 := by
    apply neutralNF569OriginalRealCombination_globalIndependence
    intro x
    have h := congrArg Complex.re (hzero x)
    simpa only [neutralNF569OriginalComplexCombination_re,
      Complex.zero_re] using h
  have him : (fun j : Fin 242 => (d j).im) = 0 := by
    apply neutralNF569OriginalRealCombination_globalIndependence
    intro x
    have h := congrArg Complex.im (hzero x)
    simpa only [neutralNF569OriginalComplexCombination_im,
      Complex.zero_im] using h
  funext j
  apply Complex.ext
  · simpa using congrFun hre j
  · simpa using congrFun him j

end
end WeilDefect
