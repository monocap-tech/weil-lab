# RPB-84 — WD-T40 F-2 scalar-symbol temperate-growth realization

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **SOURCE IMPLEMENTED / MATHLIB HAS-TEMPERATE-GROWTH REQUIREMENT AUDITED / EXT-5 ALONE TOO WEAK FORMALLY / EXT-5D DLMF 5.15.9 PINNED FOR ALL POLYGAMMA DERIVATIVE ASYMPTOTICS / EXPLICIT IMPORTED TEMPERATE PREMISE ADDED / CANONICAL TEMPERED MULTIPLIER CORE EXPOSED CONDITIONALLY / BUILD CERTIFICATION PENDING / EXT-4 INSTANTIATION NOT STARTED**

## 0. Objective

RPB-83 build-certified the corrected exponential-growth full-residual carrier.

The next F-2 dependency was to determine whether the exact strict-right scalar
symbol can lawfully enter mathlib's tempered Fourier-multiplier API.

## 1. Exact mathlib requirement

Pinned mathlib defines:

~~~lean
Function.HasTemperateGrowth f
~~~

as:

1. `ContDiff R infinity f`;
2. for every iterated derivative order `n`, a global polynomial bound.

Thus this is strictly stronger than the already pinned statement

~~~math
\Psi_a(t)=\log|t|+O_a(1).
~~~

The old EXT-5 specialization controls only the function itself.

## 2. Pinned mathlib gap

The pinned mathlib Digamma module supplies the definition, meromorphicity, and
basic functional identities of `Complex.digamma`.

No theorem giving:

~~~text
digamma HasTemperateGrowth
polygamma polynomial bounds
all-derivative vertical-line asymptotics
~~~

was found in the pinned corpus.

Therefore an internal one-line `fun_prop` proof of the exact symbol's
temperate growth would be unsupported.

## 3. Stronger external pin

DLMF §5.15 states that polygamma properties include differentiated asymptotic
expansions and equation 5.15.9 gives the asymptotic expansion for every
`psi^(n)(z)`, `n >= 1`.

This has been pinned additively as:

~~~text
EXT-5D — polygamma derivative asymptotics
DLMF 5.15.9
~~~

Along

~~~math
z(t)=\frac14+\frac{it}{2},
~~~

all positive derivatives decay polynomially at infinity, while EXT-5 controls
the zeroth derivative logarithmically.

The vertical line avoids every digamma pole, so compact-core smoothness and
boundedness combine with the asymptotic tails to yield global polynomial
bounds.

The finite prime cosine sum has bounded derivatives of every order.

Hence the exact strict-right symbol is mathematically of temperate growth.

## 4. Formal custody

RPB-84 does not reconstruct DLMF 5.15.9 inside Lean.

Instead it introduces the explicit proposition:

~~~lean
RightLimitWeilSymbolTemperatePremise (a : R)
~~~

whose field is exactly:

~~~lean
Function.HasTemperateGrowth
  (fun t : R => (rightLimitCompactWeilSymbol a t : C))
~~~

This is an imported-premise interface, consistent with the existing project
policy for EXT-4/EXT-5.

It does not upgrade WD-T40 to full internal Lean certification.

## 5. Canonical multiplier core

The module now defines:

~~~lean
rightLimitWeilMultiplierCore
~~~

which applies pinned mathlib's:

~~~lean
TemperedDistribution.fourierMultiplierCLM
~~~

to the exact certified strict-right symbol and an input tempered distribution,
conditional on `RightLimitWeilSymbolTemperatePremise`.

This is the canonical tempered multiplier core required by the corrected F-2
architecture.

The proof parameter is semantically essential because mathlib's underlying
Schwartz multiplier is a total definition with a zero fallback when
`HasTemperateGrowth` is false.

## 6. Current F-2 state

~~~text
strict-right scalar symbol:
    BUILD-CERTIFIED

exponential-growth full residual carrier:
    BUILD-CERTIFIED

EXT-5D derivative-asymptotic source:
    SOURCE-PINNED

strict-right symbol temperate premise:
    SOURCE IMPLEMENTED
    EXPLICIT IMPORTED PREMISE

canonical tempered multiplier core:
    SOURCE IMPLEMENTED
    BUILD PENDING

EXT-4 weak-realization constructor:
    NOT STARTED

F-3:
    CLOSED
~~~

## 7. RPB-84 determination

~~~math
\boxed{
\textbf{RPB-84 — THE EXACT SYMBOL'S TEMPERATE-GROWTH GAP IS CLOSED AT THE SOURCE-PREMISE LEVEL BY EXT-5D, AND THE CANONICAL TEMPERED MULTIPLIER CORE IS NOW IMPLEMENTED CONDITIONALLY IN LEAN SOURCE.}
}
~~~

## Next cursor

~~~text
RPB-85 / WD-T40 F-2 TEMPERED-MULTIPLIER CORE BUILD CERTIFICATION
~~~

The next pass should compile the updated
`WeilDefect.Morphology.NeutralWeilMultiplier` module under the pinned
toolchain and repair only genuine compiler diagnostics.

Do not instantiate EXT-4 and do not begin F-3 in that pass.
