# RPB-95 — WD-T40 F-3 final pairing build certification

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **F-3 COMPLETE / FINAL WHOLE-LINE GAUSSIAN RESIDUAL PAIRING BUILD-CERTIFIED / A.E. NULL-INTERVAL REDUCTION + EXTERIOR INTEGRABILITY + TWO-GAUSSIAN-MASS BOUND KERNEL-CHECKED / REPOSITORY-WIDE TRUST SCAN PASSED / F-4 NOT STARTED**

## 0. Objective

RPB-94 implemented the final physical residual pairing theorem for F-3.

RPB-95 performs the pinned build certification of that final source slice.

## 1. Validation custody

Temporary validation branch:

~~~text
validation/rpb95-final-gaussian-pairing
~~~

Draft validation PR:

~~~text
#12  Validate RPB-95 final Gaussian pairing
~~~

The validation-only workflow targets exactly:

~~~text
WeilDefect.Morphology.NeutralGaussianPairing
~~~

and is not merged into the research branch.

## 2. First compiler boundary

The initial exact build reached the new pairing module and exposed several
proof-engineering defects, all local to the final packaging layer:

- real-norm / absolute-value normalization in the integrable majorant;
- brittle set-integral monotonicity targets on restricted measures;
- translated-Gaussian integral rewrites that needed explicit whole-line forms;
- the local pairing abbreviation `f` needed to be unfolded before applying
  the residual's a.e. vanishing;
- one method-style `.const_mul` use and one positivity side condition needed
  explicit witnesses.

No mathematical statement or bound was weakened.

The repaired research and validation sources are byte-identical at the final
certificate.

## 3. Successful build evidence

Final corrected run:

~~~text
run: 36769646305
job: 110072481339
validation head: 395b15fc7c98981b735dd31d4a569bfef3f75b13
~~~

Lean reported:

~~~text
Built WeilDefect.Morphology.NeutralFourierCarrier
Built WeilDefect.Morphology.NeutralWeilMultiplier
Built WeilDefect.Morphology.NeutralWeilResidualCarrier
Built WeilDefect.Morphology.NeutralGaussianSupportGap
Built WeilDefect.Morphology.NeutralGaussianTail
Built WeilDefect.Morphology.NeutralGaussianPairing
Build completed successfully (8939 jobs).
~~~

The repository-wide rejection gate for top-level `axiom`, `sorry`, and
`admit` also passed.

## 4. Certified source

Module:

~~~text
WeilDefect/Morphology/NeutralGaussianPairing.lean
~~~

Certified Git blob:

~~~text
54732470ab2cf2a3a99be646372fdc186225363a
~~~

The certificate covers:

~~~lean
neutralPhysicalRepresentative_integrable
movingGaussianPhysicalKernel_continuous
movingGaussianPhysicalKernel_bddAbove_norm
movingGaussianFilteredMode_eq_convolution
movingGaussianFilteredMode_continuous
residualFilteredMode_norm_le_completedTail
residualFilteredMode_integrableOn_exterior
gaussianExteriorTail_integral_le
movingGaussianResidualPairing
movingGaussianResidualPairing_norm_le
~~~

## 5. F-3 final standing

~~~text
strict support-gap geometry:
    BUILD-CERTIFIED

actual filtered-mode exterior envelope:
    BUILD-CERTIFIED

full x-dependent Gaussian completion:
    BUILD-CERTIFIED

exterior Gaussian tail integrability:
    BUILD-CERTIFIED

whole-line residual pairing:
    BUILD-CERTIFIED

explicit Gaussian tail mass bound:
    BUILD-CERTIFIED
~~~

Therefore:

~~~math
\boxed{
\textbf{F-3 — COMPLETE.}
}
~~~

No additional imported premise was introduced in F-3.

## 6. RPB-95 determination

~~~math
\boxed{
\textbf{RPB-95 — THE FULL F-3 GAUSSIAN SUPPORT-GAP PAIRING LAYER IS BUILD-CERTIFIED.}
}
~~~

WD-T40 remains LEAN-BLOCKED because F-4 through F-6 are still open.

## Next cursor

~~~text
RPB-96 / WD-T40 F-4 LOGARITHMIC GAUSSIAN COERCIVITY
~~~

The next pass may open F-4 and should attack only the Fourier-side logarithmic
coercivity step from the certified F-3 pairing estimate plus the exact
strict-right symbol lower bound.

Do not begin F-5 strip holomorphy in that pass.
