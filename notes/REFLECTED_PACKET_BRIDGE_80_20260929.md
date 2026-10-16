# RPB-80 — WD-T40 F-2 scalar-symbol build certification

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **SCALAR-SYMBOL SLICE BUILD-CERTIFIED / ONE PARSER-LEVEL FINSET-SUM REPAIR / EXACT NEUTRAL WEIL MULTIPLIER MODULE BUILT UNDER LEAN 4.34.0 + PINNED MATHLIB / REPOSITORY-WIDE TRUST SCAN PASSED / F-2 REMAINS OPEN AT THE DISTRIBUTIONAL OPERATOR-RESIDUAL BRIDGE**

## 0. Objective

RPB-79 introduced the exact strict-right compact-window scalar Weil symbol and
left one bounded gate before deeper F-2 work: build the new module under the
pinned Lean toolchain.

RPB-80 performs that build gate only.

## 1. Validation custody

Temporary validation branch:

~~~text
validation/rpb80-neutral-weil-multiplier
~~~

Draft validation PR:

~~~text
#5  Validate RPB-80 scalar-symbol module
~~~

The PR targets `main` only to obtain GitHub Actions execution.  Its workflow
mutation is validation-only and is not to be merged into the research branch.

## 2. Initial validation-target correction

The first validation run,

~~~text
36677305867
~~~

was green but was **not** accepted as evidence for F-2 because inspection of
the workflow and logs showed that it still built the old target:

~~~text
WeilDefect.Examples.WeakCriticalFallthrough
~~~

rather than the new multiplier module.

The validation workflow was corrected before any certification claim was made.

## 3. First real F-2 compiler diagnostic

Corrected target run:

~~~text
run: 36677608452
job: 109765888840
~~~

reached

~~~text
WeilDefect.Morphology.NeutralWeilMultiplier
~~~

and failed only at two parser locations:

~~~text
NeutralWeilMultiplier.lean:45:5
unexpected token 'in'; expected ','

NeutralWeilMultiplier.lean:63:13
unexpected token 'in'; expected ','
~~~

Both came from the unsupported display form

~~~lean
∑ n in rightLimitPrimePowerFinset a, ...
~~~

The repair replaced those expressions by explicit

~~~lean
Finset.sum (rightLimitPrimePowerFinset a) (fun n => ...)
~~~

No mathematical statement, coefficient, threshold convention, or API changed.

Research-branch repair commit:

~~~text
5d66e74009479ffbbfbb0bdc6fd2922ab9c849f9
~~~

## 4. Certified scalar-symbol source

Module:

~~~text
WeilDefect/Morphology/NeutralWeilMultiplier.lean
~~~

Certified source blob:

~~~text
fe0b84a5c7a1d8d7acfe57ce2674c36d8e386202
~~~

The certified source retains:

- `Complex.digamma` for the archimedean term;
- `ArithmeticFunction.vonMangoldt` for the arithmetic coefficient;
- strict-right prime-power custody with `log n ≤ 2a`;
- explicit equality-threshold inclusion;
- a separate finite-rank pole/evaluation term by design;
- the compressed-symbol caution.

## 5. Successful build evidence

Successful corrected validation run:

~~~text
run: 36677931966
job: 109766890617
validation head: 6c1f24f1f7e012c65b168d406c3462c36cdc7dd9
~~~

Lean reported:

~~~text
Built WeilDefect.Morphology.NeutralFourierCarrier
Built WeilDefect.Morphology.NeutralWeilMultiplier
Build completed successfully (8935 jobs).
~~~

The repository-wide rejection gate for top-level `axiom`, `sorry`, and
`admit` also passed.

Thus the RPB-79 scalar-symbol slice is genuinely kernel-checked under the
pinned Lean 4.34.0 environment.

## 6. F-2 standing after RPB-80

~~~text
F-2 exact strict-right scalar symbol:
    BUILD-CERTIFIED

F-2 distributional operator/residual identity:
    OPEN
~~~

The remaining F-2 bridge is still:

~~~text
F-1 physical mode h
    +
rightLimitCompactWeilSymbol a
    +
finite-rank pole/evaluation contribution
    ->
actual enlarged tempered residual q
~~~

in a form strong enough to support the later Gaussian pairing identity.

That bridge must preserve the compressed-window / whole-line distinction and
may consume the explicit compact-window formula as an imported EXT-4 premise.

## 7. RPB-80 determination

~~~math
\boxed{
\textbf{RPB-80 — THE EXACT STRICT-RIGHT SCALAR WEIL SYMBOL IS BUILD-CERTIFIED; F-2 NOW REDUCES TO THE DISTRIBUTIONAL OPERATOR-RESIDUAL REALIZATION.}
}
~~~

WD-T40 remains LEAN-BLOCKED because F-2 is not yet complete.

## Next cursor

~~~text
RPB-81 / WD-T40 F-2 DISTRIBUTIONAL OPERATOR-RESIDUAL BRIDGE
~~~

The next pass should design and implement only the faithful weak/distributional
identity connecting the certified scalar symbol and pole term to the actual
enlarged residual.  Do not begin F-3 Gaussian support-gap pairing until F-2 is
closed.
