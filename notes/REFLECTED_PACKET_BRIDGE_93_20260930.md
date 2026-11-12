# RPB-93 — WD-T40 F-3 Gaussian tail completion build certification

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **GAUSSIAN TAIL COMPLETION BUILD-CERTIFIED / FULL EXTERIOR X-GAUSSIAN ENVELOPE + RESIDUAL-GROWTH COMPLETION + EXTERIOR TAIL INTEGRABILITY COMPILE UNDER LEAN 4.34.0 / ONE HALF-LINE INTEGRABILITY REPAIR / REPOSITORY-WIDE TRUST SCAN PASSED / FINAL RESIDUAL PAIRING INTEGRAL STILL OPEN / F-4 NOT STARTED**

## 0. Objective

RPB-92 implemented the stronger exterior Gaussian envelope and completion
inequality required to absorb the certified residual's fixed exponential
growth.

RPB-93 performs only the pinned build certification of that source slice.

## 1. Validation custody

Temporary validation branch:

~~~text
validation/rpb93-gaussian-tail-completion
~~~

Draft validation PR:

~~~text
#11  Validate RPB-93 Gaussian tail completion
~~~

The validation-only workflow targets exactly:

~~~text
WeilDefect.Morphology.NeutralGaussianTail
~~~

and is not merged into the research branch.

## 2. First real compiler diagnostic

Initial exact-target run:

~~~text
run: 36763185666
job: 110050662753
~~~

reached `NeutralGaussianTail`.

The completion inequality itself compiled.  The failures were confined to the
final proof that the remaining Gaussian is integrable on the two exterior
half-lines:

- two pointwise absolute-value rewrites were attempted before exposing the
  lambda body;
- the translated Gaussian proof used a brittle `convert ... ring` step whose
  generated function equality did not normalize as intended.

The repair replaced those proof-engineering steps by:

- direct use of `hbase.comp_sub_right c` on the positive half-line;
- `simpa [sub_neg_eq_add]` from `hbase.comp_sub_right (-c)` on the negative
  half-line;
- explicit pointwise `change` statements before the sign-specific
  `abs_of_nonneg` / `abs_of_nonpos` rewrites.

Research-branch repair commit:

~~~text
a1deab61ca9a91ab3e383af1ea3d1372c54c4976
~~~

No mathematical statement changed.

## 3. Certified source

Module:

~~~text
WeilDefect/Morphology/NeutralGaussianTail.lean
~~~

Certified Git blob:

~~~text
7ee6dacf94e4e6b4c694209a7be9ee4ba72846e6
~~~

The certified source contains:

~~~lean
gaussianExteriorSet
movingGaussianPhysicalKernel_norm_le_exteriorEnvelope
movingGaussianFilteredMode_norm_le_exteriorEnvelope
gaussianTailCompletion_bound
gaussianExteriorTail_integrableOn
~~~

## 4. Successful build evidence

Corrected validation run:

~~~text
run: 36763669865
job: 110052304855
validation head: aeb2384119ef1c6854ca2c88fb2a3662dce2ab26
~~~

Lean reported:

~~~text
Built WeilDefect.Morphology.NeutralFourierCarrier
Built WeilDefect.Morphology.NeutralWeilMultiplier
Built WeilDefect.Morphology.NeutralWeilResidualCarrier
Built WeilDefect.Morphology.NeutralGaussianSupportGap
Built WeilDefect.Morphology.NeutralGaussianTail
Build completed successfully (8938 jobs).
~~~

The repository-wide rejection gate for top-level `axiom`, `sorry`, and
`admit` also passed.

## 5. Linter note

The successful run retains one nonblocking warning in the new module:

~~~text
gaussianTailCompletion_bound: hκ is not explicitly referenced
~~~

The nonnegativity is already implied strongly enough by the large-parameter
hypothesis in the proof body.  This is stylistic and does not affect the
certificate.

## 6. F-3 standing after RPB-93

~~~text
strict support-gap geometry:
    BUILD-CERTIFIED

actual filtered-mode exterior envelope:
    BUILD-CERTIFIED

full x-dependent exterior envelope:
    BUILD-CERTIFIED

residual-growth Gaussian completion:
    BUILD-CERTIFIED

exterior Gaussian tail integrability:
    BUILD-CERTIFIED

final residual pairing integral bound:
    OPEN
~~~

The remaining F-3 step is now genuinely the final pairing integration:
combine a.e. central vanishing, the residual growth bound, the certified
filtered-mode envelope, and the Gaussian completion/integrability package into
the exponentially small whole-line pairing estimate.

## 7. RPB-93 determination

~~~math
\boxed{
\textbf{RPB-93 — THE GAUSSIAN TAIL COMPLETION LAYER IS BUILD-CERTIFIED; F-3 NOW HAS ONLY THE FINAL RESIDUAL PAIRING INTEGRAL TO CLOSE.}
}
~~~

F-4 remains closed.

## Next cursor

~~~text
RPB-94 / WD-T40 F-3 FINAL RESIDUAL PAIRING INTEGRAL
~~~

The next pass should prove only the final physical pairing estimate from the
certified F-2 residual and certified F-3 Gaussian-tail stack.

Do not begin logarithmic symbol coercivity or F-4 in that pass.
