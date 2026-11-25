# RPB-89 — WD-T40 F-3 support-gap geometry build certification

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **F-3 GEOMETRY SLICE BUILD-CERTIFIED / STRICT COLLAR GEOMETRY + EXTERIOR GAUSSIAN ENVELOPE + POINTWISE RESIDUAL-PRODUCT DOMINATION COMPILE UNDER LEAN 4.34.0 / REPOSITORY-WIDE TRUST SCAN PASSED / NO COMPILER REPAIR REQUIRED / ONE NONBLOCKING UNUSED-VARIABLE LINTER WARNING / FILTERED-MODE CONVOLUTION ENVELOPE STILL OPEN**

## 0. Objective

RPB-88 opened F-3 and implemented only the strict support-gap geometry and
exterior pointwise Gaussian domination.

RPB-89 performs the pinned build gate for that source slice.

## 1. Validation custody

Temporary validation branch:

~~~text
validation/rpb89-gaussian-support-gap
~~~

Draft validation PR:

~~~text
#9  Validate RPB-89 Gaussian support-gap layer
~~~

The validation-only workflow targets exactly:

~~~text
WeilDefect.Morphology.NeutralGaussianSupportGap
~~~

and is not merged into the research branch.

## 2. Build result

GitHub Actions run:

~~~text
run: 36739623602
job: 109970289157
~~~

completed successfully.

Lean reported:

~~~text
Built WeilDefect.Morphology.NeutralFourierCarrier
Built WeilDefect.Morphology.NeutralWeilMultiplier
Built WeilDefect.Morphology.NeutralWeilResidualCarrier
Built WeilDefect.Morphology.NeutralGaussianSupportGap
Build completed successfully (8937 jobs).
~~~

The repository-wide rejection gate for top-level `axiom`, `sorry`, and
`admit` also passed.

No compiler repair was required.

## 3. Certified source

Module:

~~~text
WeilDefect/Morphology/NeutralGaussianSupportGap.lean
~~~

Certified Git blob:

~~~text
ca837ad7eb468f6fb392f3df7649bb24ff143084
~~~

The certified source contains:

~~~lean
gaussianSupportEnvelope
radius_le_abs_of_not_mem_Ioo
supportGap_le_abs_sub
supportGap_sq_le_abs_sub_sq
gaussianSupportEnvelope_le_gap
residual_mul_gaussianEnvelope_bound
residual_mul_gaussianExterior_bound
~~~

## 4. Linter note

Lean emitted one nonblocking warning:

~~~text
NeutralGaussianSupportGap.lean:110:5
Variable name hA is not explicitly referenced.
~~~

The proof term uses the envelope hypothesis `hg`, whose own type already
contains the factor `A`; the separate nonnegativity hypothesis `hA` is not
needed by that theorem body.

RPB-89 does not change the source merely to silence this stylistic warning.

## 5. F-3 standing after RPB-89

~~~text
strict support-gap geometry:
    BUILD-CERTIFIED

exterior Gaussian envelope suppression:
    BUILD-CERTIFIED

pointwise residual-product domination:
    BUILD-CERTIFIED

actual filtered-mode Gaussian convolution envelope:
    OPEN

Gaussian tail integration / exponentially small pairing:
    OPEN
~~~

The geometry layer is therefore closed.

## 6. RPB-89 determination

~~~math
\boxed{
\textbf{RPB-89 — THE F-3 SUPPORT-GAP GEOMETRY SLICE IS BUILD-CERTIFIED; THE NEXT INTERNAL OBSTRUCTION IS THE ACTUAL FILTERED-MODE GAUSSIAN CONVOLUTION ENVELOPE.}
}
~~~

F-3 remains in progress.  F-4 remains closed.

## Next cursor

~~~text
RPB-90 / WD-T40 F-3 FILTERED-MODE GAUSSIAN ENVELOPE
~~~

The next pass should derive the physical-space bound for the actual Gaussian
filtered mode from:

- the F-1 compact support of the physical representative;
- the explicit Gaussian physical kernel; and
- the relevant L1/L2 compact-support estimate.

Do not perform the exterior tail integration and do not begin F-4 in that pass.
