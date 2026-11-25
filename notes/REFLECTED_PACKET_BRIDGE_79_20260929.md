# RPB-79 — WD-T40 F-2 scalar-symbol realization entry

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **F-2 IN PROGRESS / EXACT STRICT-RIGHT SCALAR WEIL SYMBOL IMPLEMENTED IN LEAN SOURCE / DIGAMMA ARCHIMEDEAN TERM AND VON MANGOLDT PRIME COEFFICIENTS ARE NOW CONCRETE / EQUALITY-THRESHOLD PRIME POWERS ARE RETAINED BY CONSTRUCTION / COMPRESSED-SYMBOL CAUTION PRESERVED / DISTRIBUTIONAL OPERATOR-RESIDUAL REALIZATION NOT YET IMPLEMENTED / BUILD CERTIFICATION PENDING**

## 0. Objective

RPB-78 closed F-1 with a real pinned Lean build.

RPB-79 opens F-2 only far enough to type the exact scalar Fourier symbol needed
by the strict-right compact-window operator.  It does not attempt F-3 and does
not yet identify the F-1 residual with the actual Weil operator.

## 1. New source module

Added:

~~~text
WeilDefect/Morphology/NeutralWeilMultiplier.lean
~~~

and registered it in the project root.

The module imports the certified F-1 carrier and the pinned mathlib definitions
of:

~~~text
Complex.digamma
ArithmeticFunction.vonMangoldt
~~~

from the exact Lean 4.34.0 / mathlib v4.34.0 dependency line.

## 2. Strict-right prime-power custody

The module defines:

~~~lean
rightLimitPrimePowerFinset (a : ℝ)
~~~

from the already certified finite set:

~~~lean
rightLimitPrimePowers a
=
{n | IsPrimePow n ∧ log n ≤ 2a}.
~~~

Thus F-2 does not reuse the endpoint strict-active finset with `< 2a`.

Two source theorems record the intended custody:

~~~text
active_mem_rightLimitPrimePowerFinset
threshold_mem_rightLimitPrimePowerFinset
~~~

so both the old strict-active terms and an equality-threshold term enter the
strict-right symbol.

## 3. Exact scalar ingredients

The archimedean term is now concrete:

~~~math
A_\infty(t)
=
\Re\psi\!\left(\frac14+\frac{it}{2}\right)
-
\log\pi.
~~~

Lean definition:

~~~lean
compactWindowArchimedeanSymbol
~~~

The arithmetic coefficient is now concrete:

~~~math
w_n
=
\frac{2\Lambda(n)}{\sqrt n}.
~~~

Lean definition:

~~~lean
compactWindowPrimeCoefficient
~~~

The finite prime symbol is:

~~~math
P_a(t)
=
\sum_{\substack{n=p^m\\ \log n\le2a}}
\frac{2\Lambda(n)}{\sqrt n}
\cos(t\log n).
~~~

Lean definition:

~~~lean
rightLimitPrimeSymbol
~~~

and the scalar Weil symbol is:

~~~math
\boxed{
\Psi_a^{\mathrm{right}}(t)
=
A_\infty(t)-P_a(t).
}
~~~

Lean definition:

~~~lean
rightLimitCompactWeilSymbol
~~~

## 4. Compressed-symbol caution

RPB-79 does **not** assert

~~~math
\Psi_a^{\mathrm{right}}(t)\widehat h(t)=0.
~~~

That would be an invalid collapse of the compressed compact-window kernel
relation into a whole-line pointwise symbol equation.

The scalar symbol is being constructed because WD-T40 later uses it inside a
whole-line **distributional pairing identity** for the enlarged residual.

The finite-rank pole/evaluation contribution is also deliberately kept
separate from the scalar symbol.

## 5. What remains inside F-2

The unfinished part of F-2 is the actual distributional realization:

~~~text
F-1 physical mode h
    +
rightLimitCompactWeilSymbol a
    +
finite-rank pole/evaluation contribution
    ->
the exact enlarged residual q
~~~

in a form strong enough to prove the Fourier-side pairing identity consumed by
F-3/F-4.

That bridge must come from the explicit compact-window formula / operator
premise retained as EXT-4.  It may be represented as an explicit imported
premise, but the later support-gap pairing and coercivity steps may not be
hidden inside that premise.

## 6. Current status

~~~text
F-1  physical Fourier carrier lift
     BUILD-CERTIFIED

F-2  actual compact-window Weil multiplier realization
     IN PROGRESS
     exact scalar symbol source: IMPLEMENTED
     module build certificate: PENDING
     distributional residual/operator identity: OPEN

F-3  NOT STARTED
F-4  NOT STARTED
F-5  NOT STARTED
F-6  NOT STARTED
~~~

WD-T40 remains LEAN-BLOCKED.

## 7. RPB-79 determination

~~~math
\boxed{
\textbf{RPB-79 — THE EXACT THRESHOLD-CORRECTED SCALAR WEIL SYMBOL IS NOW TYPED IN LEAN SOURCE; F-2 REMAINS OPEN AT THE DISTRIBUTIONAL OPERATOR BRIDGE.}
}
~~~

## Next cursor

~~~text
RPB-80 / WD-T40 F-2 SCALAR-SYMBOL BUILD CERTIFICATION
~~~

The next pass should compile only the new scalar-symbol module under the pinned
toolchain, repair any genuine compiler diagnostic, and stop.  Do not begin the
distributional residual bridge until this source slice is build-certified.
