# RPB-85 — WD-T40 F-2 tempered-multiplier core build certification

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **TEMPERED-MULTIPLIER CORE BUILD-CERTIFIED / EXACT STRICT-RIGHT SYMBOL + EXPLICIT EXT-5D TEMPERATE PREMISE + CONDITIONAL MATHLIB FOURIER-MULTIPLIER CORE COMPILE UNDER LEAN 4.34.0 / REPOSITORY-WIDE TRUST SCAN PASSED / NO COMPILER REPAIR REQUIRED / EXT-4 INSTANTIATION NOT STARTED**

## 0. Objective

RPB-84 pinned the missing all-derivative special-function input as EXT-5D and
added the explicit `RightLimitWeilSymbolTemperatePremise` together with the
conditional canonical tempered multiplier core.

RPB-85 performs only the pinned build certification of that updated module.

## 1. Validation custody

Temporary validation branch:

~~~text
validation/rpb85-neutral-weil-multiplier-core
~~~

Draft validation PR:

~~~text
#7  Validate RPB-85 multiplier core
~~~

The validation-only workflow targets exactly:

~~~text
WeilDefect.Morphology.NeutralWeilMultiplier
~~~

and is not merged into the research branch.

## 2. Build result

GitHub Actions run:

~~~text
run: 36728858650
job: 109932772151
~~~

completed successfully.

Lean reported:

~~~text
Built WeilDefect.Morphology.NeutralFourierCarrier
Built WeilDefect.Morphology.NeutralWeilMultiplier
Build completed successfully (8935 jobs).
~~~

The repository-wide rejection gate for top-level `axiom`, `sorry`, and
`admit` also passed.

No compiler repair was required in RPB-85.

## 3. Certified source

Module:

~~~text
WeilDefect/Morphology/NeutralWeilMultiplier.lean
~~~

Certified Git blob:

~~~text
a2d67c1f30d8e658a2f349ff80ffc4d1ccb06fb1
~~~

This source contains both:

~~~lean
RightLimitWeilSymbolTemperatePremise
rightLimitWeilMultiplierCore
~~~

with the temperate-growth statement kept explicitly imported from the
EXT-5/EXT-5D source layer.

## 4. What the certificate does and does not prove

The build certifies the Lean implication:

~~~text
explicit exact-symbol HasTemperateGrowth premise
    ->
canonical tempered Fourier multiplier core exists.
~~~

It does **not** reconstruct DLMF 5.15.9 inside Lean.

It also does not yet prove that the actual compact-window Weil residual is
equal to:

~~~text
rightLimitWeilMultiplierCore
    +
pole/evaluation component.
~~~

That remaining identification is the EXT-4 weak-realization bridge.

## 5. F-2 standing after RPB-85

~~~text
strict-right scalar symbol:
    BUILD-CERTIFIED

EXT-5D polygamma derivative source:
    SOURCE-PINNED

symbol-temperate imported premise:
    BUILD-CERTIFIED AS INTERFACE

canonical tempered multiplier core:
    BUILD-CERTIFIED

exponential-growth residual carrier:
    BUILD-CERTIFIED

compact-test weak-realization target:
    BUILD-CERTIFIED AS INTERFACE

EXT-4 actual weak-realization constructor:
    OPEN
~~~

F-2 therefore now has all internal carrier pieces needed to state the imported
compact-window operator identification without weakening the later Gaussian
argument.

## 6. RPB-85 determination

~~~math
\boxed{
\textbf{RPB-85 — THE CONDITIONAL TEMPERED MULTIPLIER CORE IS BUILD-CERTIFIED; THE ONLY REMAINING F-2 BRIDGE IS THE EXT-4 ACTUAL WEAK-REALIZATION IDENTIFICATION.}
}
~~~

WD-T40 remains LEAN-BLOCKED because F-2 is not yet complete.

## Next cursor

~~~text
RPB-86 / WD-T40 F-2 EXT-4 WEAK-REALIZATION CONSTRUCTOR
~~~

The next pass should connect:

1. the certified physical F-1 mode;
2. the certified conditional tempered multiplier core;
3. the explicit pole/evaluation physical component; and
4. the certified exponential-growth residual carrier

through an **explicit imported EXT-4 premise** matching
`NeutralWeilResidualWeakRealization`.

Do not begin F-3 Gaussian support-gap pairing in that pass.
