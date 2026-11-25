# RPB-91 — WD-T40 F-3 filtered-mode envelope build certification

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **FILTERED-MODE ENVELOPE BUILD-CERTIFIED / FOUR REAL LEAN RUNS / THREE FORMAL REPAIR ROUNDS / ACTUAL MOVING-GAUSSIAN KERNEL + COMPACT-SUPPORT CONVOLUTION + EXTERIOR ENVELOPE NOW KERNEL-CHECKED / REPOSITORY-WIDE TRUST SCAN PASSED / RESIDUAL TAIL INTEGRATION REMAINS OPEN**

## 0. Objective

RPB-90 implemented the actual moving-Gaussian physical kernel and the
exterior convolution envelope for the certified F-1 mode.

RPB-91 performs only the pinned build certification of that F-3 slice.

## 1. Validation custody

Temporary validation branch:

~~~text
validation/rpb91-filtered-mode-envelope
~~~

Draft validation PR:

~~~text
#10  Validate RPB-91 filtered-mode envelope
~~~

The validation workflow targets exactly:

~~~text
WeilDefect.Morphology.NeutralGaussianSupportGap
~~~

and is not merged into the research branch.

## 2. First compiler boundary — run 36751124748

The first exact build exposed several proof-engineering defects:

- the kernel norm simplification did not close automatically;
- an explicit extended-nonnegative-real annotation parsed badly;
- a nested absolute-value display parsed badly;
- the newly defined kernel had no registered `fun_prop` continuity theorem;
- the restricted-measure proof used an unavailable unqualified
  `EventuallyLE` name.

The repair was purely formal:

- infer the `MemLp.locallyIntegrable` exponent;
- spell the reverse-triangle step without nested absolute notation;
- unfold the kernel before `fun_prop`;
- use `self_mem_ae_restrict` directly;
- split the kernel modulus into Gaussian and oscillatory factors.

Research repair commit:

~~~text
0cd02001e5ede766c73924bbece16a81abbf2ee3
~~~

## 3. Second compiler boundary — run 36751690110

The second build reduced the failures to:

- the coerced positive real Gaussian factor's complex norm;
- an unnecessary absolute-value intermediate in the reverse-triangle chain;
- one stale indentation block in the restricted-measure calculation.

The repairs were:

~~~text
direct real-to-complex norm proof
direct abs_sub_abs_le_abs_sub use
corrected calc indentation
~~~

Research repair commit:

~~~text
7ff395e9bf9dc10cc34e133167eca1b4eb864b83
~~~

## 4. Third compiler boundary — run 36752188733

The third build reduced the entire target to one remaining identity:

~~~text
|| (exp s : R) coerced to C || = exp s
~~~

This was closed explicitly with:

~~~lean
Complex.norm_real
Real.norm_of_nonneg (Real.exp_nonneg _)
~~~

Research repair commit:

~~~text
7287baccdf9efefd571a0357144782422a78e4ca
~~~

No mathematical statement changed in any repair round.

## 5. Successful build evidence

Final corrected run:

~~~text
run: 36752658074
job: 110014912282
validation head: e0ce54d3e87da27be1fef7888db3a8ae928fe52f
~~~

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

## 6. Certified source

Module:

~~~text
WeilDefect/Morphology/NeutralGaussianSupportGap.lean
~~~

Certified Git blob:

~~~text
d29c784bfdb15681c103e906f42a3ff946a0db76
~~~

This certificate covers the actual convention-parametric moving-Gaussian
kernel, compact L1 mass of the certified F-1 representative, compact-support
physical convolution, strict displacement geometry, kernel exterior bound,
and the actual filtered-mode exterior Gaussian envelope.

## 7. Linter notes

The successful run retains two nonblocking warnings for proof arguments that
are not explicitly referenced:

~~~text
hA
hR
~~~

These are stylistic only and do not affect the kernel certificate.

## 8. F-3 standing after RPB-91

~~~text
strict support-gap geometry:
    BUILD-CERTIFIED

exterior pointwise residual domination:
    BUILD-CERTIFIED

actual moving-Gaussian kernel:
    BUILD-CERTIFIED

compact-support filtered-mode convolution:
    BUILD-CERTIFIED

actual exterior filtered-mode envelope:
    BUILD-CERTIFIED

residual Gaussian tail integration:
    OPEN
~~~

Thus the only remaining F-3 analytic obligation is to use the certified
exponential-growth residual and the actual Gaussian envelope to prove the
exponentially small whole-line pairing.

## 9. RPB-91 determination

~~~math
\boxed{
\textbf{RPB-91 — THE ACTUAL FILTERED-MODE GAUSSIAN ENVELOPE IS BUILD-CERTIFIED; F-3 NOW REDUCES TO THE EXPONENTIAL-GROWTH RESIDUAL TAIL INTEGRATION.}
}
~~~

F-4 remains closed.

## Next cursor

~~~text
RPB-92 / WD-T40 F-3 RESIDUAL GAUSSIAN TAIL INTEGRATION
~~~

The next pass should address only the exterior integral / pairing estimate
needed to obtain exponential smallness in the moving parameter.

Do not begin logarithmic symbol coercivity or F-4 in that pass.
