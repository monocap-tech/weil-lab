# RPB-87 — WD-T40 F-2 EXT-4 weak-realization build certification

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **F-2 COMPLETE / EXT-4 WEAK-REALIZATION SOURCE BUILD-CERTIFIED / ONE DECLARATION-KIND REPAIR / EXACT F-1 MODE + CONDITIONAL TEMPERED MULTIPLIER CORE + POLE TERM + EXPONENTIAL-GROWTH RESIDUAL PACKAGE COMPILES UNDER LEAN 4.34.0 / REPOSITORY-WIDE TRUST SCAN PASSED / F-3 NOT STARTED**

## 0. Objective

RPB-86 implemented the final F-2 bridge as an explicit imported EXT-4
weak-realization premise plus a packaging declaration.

RPB-87 performs the final pinned build gate for F-2.

## 1. Validation custody

Temporary validation branch:

~~~text
validation/rpb87-ext4-weak-realization
~~~

Draft validation PR:

~~~text
#8  Validate RPB-87 EXT-4 weak realization
~~~

The validation-only workflow targets exactly:

~~~text
WeilDefect.Morphology.NeutralWeilResidualCarrier
~~~

and is not merged into the research branch.

## 2. First real compiler diagnostic

Initial exact-target run:

~~~text
run: 36734827257
job: 109953666384
~~~

reached the new declaration and failed with:

~~~text
NeutralWeilResidualCarrier.lean:117:0
type of theorem rightLimitWeilWeakRealization is not a proposition
~~~

The declaration returns the data structure

~~~lean
NeutralWeilResidualWeakRealization c
~~~

rather than a proposition.

The repair was therefore purely declaration-kind:

~~~text
theorem
    ->
noncomputable def
~~~

No parameter, premise, weak identity, carrier field, or mathematical relation
changed.

Research-branch repair commit:

~~~text
c3e62338edbf91e859915f0e52678dea40b1ee3f
~~~

## 3. Certified source

Module:

~~~text
WeilDefect/Morphology/NeutralWeilResidualCarrier.lean
~~~

Certified Git blob:

~~~text
d11e51ea0199f134b3c8f17f76c341a27d6d2881
~~~

The certified source contains:

~~~lean
RightLimitWeilWeakRealizationPremise
rightLimitWeilWeakRealization
~~~

where the latter is now correctly a `noncomputable def`.

## 4. Successful build evidence

Successful corrected run:

~~~text
run: 36735403643
job: 109955656734
validation head: e14a1135a95559a2c67c42b3b29f97c4ae7835f4
~~~

Lean reported:

~~~text
Built WeilDefect.Morphology.NeutralFourierCarrier
Built WeilDefect.Morphology.NeutralWeilMultiplier
Built WeilDefect.Morphology.NeutralWeilResidualCarrier
Build completed successfully (8936 jobs).
~~~

The repository-wide rejection gate for top-level `axiom`, `sorry`, and
`admit` also passed.

## 5. F-2 final standing

The full F-2 formalization stack is now:

~~~text
exact strict-right scalar symbol:
    BUILD-CERTIFIED

EXT-5D polygamma derivative source:
    SOURCE-PINNED / EXPLICIT IMPORTED PREMISE

symbol-temperate interface:
    BUILD-CERTIFIED AS IMPORTED-PREMISE INTERFACE

canonical tempered multiplier core:
    BUILD-CERTIFIED

exponential-growth physical residual carrier:
    BUILD-CERTIFIED

generic compact-test weak-realization target:
    BUILD-CERTIFIED

EXT-4 actual weak-realization premise:
    BUILD-CERTIFIED AS IMPORTED-PREMISE INTERFACE

EXT-4 packaging definition:
    BUILD-CERTIFIED
~~~

Thus:

~~~math
\boxed{
\textbf{F-2 — COMPLETE, CONDITIONAL ON THE EXPLICIT EXT-4 / EXT-5D IMPORTED PREMISES.}
}
~~~

This is exactly the expected custody class for the eventual
`LEAN-CERTIFIED-FROM-IMPORTED-PREMISE` WD-T40 result.

## 6. What F-2 does not prove

F-2 does not prove:

- the Gaussian support-gap pairing estimate;
- exponential smallness in the moving frequency parameter;
- logarithmic Gaussian coercivity;
- exponential Fourier decay;
- strip holomorphy;
- compact-support contradiction.

Those remain internal F-3 through F-5 obligations.

## 7. RPB-87 determination

~~~math
\boxed{
\textbf{RPB-87 — F-2 IS CLOSED: THE ACTUAL WEAK-REALIZATION LAYER IS BUILD-CERTIFIED FROM EXPLICIT IMPORTED SOURCE PREMISES, AND THE WD-T40 FORMALIZATION FRONTIER ADVANCES TO F-3.}
}
~~~

WD-T40 remains LEAN-BLOCKED because F-3 through F-6 are still open.

## Next cursor

~~~text
RPB-88 / WD-T40 F-3 GAUSSIAN SUPPORT-GAP PAIRING
~~~

The next pass may open F-3.

It should attack only the Gaussian support-gap pairing theorem from:

- compact support of the F-1 physical mode;
- strict central vanishing and exponential growth of the certified F-2 residual;
- the Gaussian Fourier/filter infrastructure in pinned mathlib.

Do not begin F-4 coercivity until F-3 is complete.
