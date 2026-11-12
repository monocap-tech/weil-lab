# RPB-97 — WD-T40 Fourier-normalization repair build certification

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **NORMALIZED F-2/F-3 DEPENDENCY CHAIN BUILD-CERTIFIED / SOURCE-FREQUENCY TO MATHLIB-FREQUENCY MAP t=2*pi*xi KERNEL-CHECKED THROUGH FINAL F-3 PAIRING MODULE / REPOSITORY-WIDE TRUST SCAN PASSED / NO COMPILER REPAIR REQUIRED / F-4 COERCIVITY STILL NOT STARTED**

## 0. Objective

RPB-96 found and repaired the load-bearing Fourier-coordinate mismatch between
the pinned compact-window source variable and mathlib's real Fourier variable.

RPB-97 performs the integrated pinned build through the current F-3 terminal
module.

## 1. Validation custody

Temporary validation branch:

~~~text
validation/rpb97-fourier-normalization
~~~

Draft validation PR:

~~~text
#13  Validate RPB-97 Fourier normalization
~~~

The validation workflow targets:

~~~text
WeilDefect.Morphology.NeutralGaussianPairing
~~~

so the build transitively checks:

- the corrected strict-right multiplier;
- the residual weak-realization carrier;
- the support-gap Gaussian modules; and
- the final whole-line F-3 pairing theorem.

The validation workflow mutation is not merged into the research branch.

## 2. Corrected multiplier source

The current multiplier module now contains:

~~~lean
rightLimitCompactWeilSymbolMathlib a xi :=
  rightLimitCompactWeilSymbol a (2 * Real.pi * xi)
~~~

and both

~~~lean
RightLimitWeilSymbolTemperatePremise
rightLimitWeilMultiplierCore
~~~

are bound to that normalized symbol.

Certified multiplier blob:

~~~text
4c24084c8a058cbb6685d54bc8226b746cabc413
~~~

The downstream residual-carrier blob remains:

~~~text
d11e51ea0199f134b3c8f17f76c341a27d6d2881
~~~

and the final F-3 pairing blob remains:

~~~text
54732470ab2cf2a3a99be646372fdc186225363a
~~~

Their source text did not require mutation; recompilation against the corrected
multiplier is the relevant integrated certificate.

## 3. Successful integrated build

Validation run:

~~~text
run: 36774149872
job: 110087718352
validation head: 3ca9e273d957cebe3b639917f8529e4b422ddfc7
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

The repository-wide rejection gate for top-level \`axiom\`, \`sorry\`, and
\`admit\` also passed.

No compiler repair was required after the RPB-96 source normalization.

## 4. Restored current standing

The normalization repair is now part of the active certified chain:

~~~text
F-1:
    BUILD-CERTIFIED

F-2:
    NORMALIZED / BUILD-CERTIFIED
    source variable t mapped to mathlib xi by t = 2*pi*xi
    explicit EXT-4 / EXT-5D premise custody unchanged

F-3:
    COMPLETE / BUILD-CERTIFIED
    revalidated transitively against normalized F-2

F-4:
    NOT STARTED
~~~

The earlier certificates remain append-only historical evidence; RPB-97 is the
current integrated certificate after the normalization correction.

## 5. Remaining pre-coercivity interface

RPB-96 also identified a second, independent interface:

the F-2 weak realization is presently stated only for compactly supported
Schwartz tests, whereas the moving Gaussian filtered mode used by the F-3/F-4
argument is noncompact.

The stored pole term is only locally integrable.

Therefore the next pass must address the **Gaussian-admissibility bridge**
before the Fourier-side coercivity identity may be invoked.

That bridge may be discharged by a source-faithful cutoff/limit argument or by
an explicit imported Gaussian-admissibility premise, but it must not be
silently assumed.

## 6. RPB-97 determination

~~~math
\boxed{
\textbf{RPB-97 — THE 2\pi FOURIER-COORDINATE REPAIR IS BUILD-CERTIFIED THROUGH THE FULL F-3 STACK; F-4 REMAINS BLOCKED ONLY BY THE EXPLICIT GAUSSIAN-ADMISSIBILITY INTERFACE.}
}
~~~

## Next cursor

~~~text
RPB-98 / WD-T40 F-4 GAUSSIAN-ADMISSIBILITY WEAK-REALIZATION BRIDGE
~~~

Do not begin the logarithmic coercivity inequality until that domain bridge is
lawfully closed.
