# RPB-108 — strict-source / right-limit threshold correction

**Date:** 2026-10-01 (America/Los_Angeles)  
**Research base:** `ea265a0023a8799d1ddc90c6d7c0e10e20c4f70f`  
**Effective status:** **STRICT SOURCE `<` / RIGHT-LIMIT `≤` PRIME CONVENTION SEPARATED AND BUILD-CERTIFIED / EQUALITY-THRESHOLD CORRECTION SUBSINGLETON / EXACT SYMBOL CONVERSION CERTIFIED / STRICT SOURCE SYMBOL TEMPERATE GROWTH DERIVED INTERNALLY / SOURCE FORM-DOMAIN + POLARIZATION + ACTUAL RESIDUAL ATTACHMENT STILL OPEN / RPB-108 CONTINUES / COERCIVITY NOT STARTED**

## 1. Source convention

The pinned compact-window formula uses

~~~math
\Psi_L(t)
=
\Re\psi\!\left(\frac14+\frac{it}{2}\right)-\log\pi
-
\sum_{\log n<2L}
\frac{2\Lambda(n)}{\sqrt n}\cos(t\log n).
~~~

The project right-limit operator instead deliberately retains equality
thresholds through

~~~math
\log n\le2a.
~~~

RPB-108 now represents these as distinct Lean objects rather than treating
the source formula as if it already used the right-limit convention.

## 2. New certified module

~~~text
WeilDefect/Morphology/NeutralWeilSourceThreshold.lean
~~~

Core declarations:

~~~text
rightLimitThresholdFinset
mem_rightLimitThresholdFinset
rightLimitThresholdFinset_subsingleton
activePrimePowerFinset_subset_rightLimit

strictSourcePrimeSymbol
strictSourceCompactWeilSymbol
strictSourceCompactWeilSymbolMathlib

rightLimitThresholdPrimeSymbolMathlib
rightLimitThresholdPrimeSymbolMathlib_eq

rightLimitCompactWeilSymbolMathlib_eq_strictSource_sub_threshold
rightLimitCompactWeilSymbolMathlib_eq_strictSource_of_no_threshold

rightLimitThresholdPrimeSymbolMathlib_hasTemperateGrowth
strictSourceCompactWeilSymbolMathlib_hasTemperateGrowth
~~~

Lean proves

~~~math
n\in T_a
\iff
n=p^m
\text{ and }
\log n=2a,
~~~

so the correction set is at most one natural prime power.

The exact symbol conversion is

~~~math
\boxed{
\Psi_a^{\le}(\xi)
=
\Psi_a^{<}(\xi)-\Theta_a(\xi).
}
~~~

If the threshold set is empty then the symbols agree identically.

## 3. Temperate-growth consequence

The threshold correction is a finite trigonometric polynomial, hence has
temperate growth internally.

Using

~~~math
\Psi_a^{<}
=
\Psi_a^{\le}+\Theta_a,
~~~

the strict source symbol inherits `HasTemperateGrowth` from the existing
right-limit `RightLimitWeilSymbolTemperatePremise`.

Thus the source-side strict symbol requires no new DLMF/polygamma input.

## 4. Source verification

The pinned source states its exact geometric formula for tests supported in
`[-L,L]` and uses the strict condition `log n < 2L`.  Its parity lemma
extends the quadratic form to arbitrary complex tests by real/imaginary and
even/odd decomposition.  RPB-108 therefore retains the strict source symbol
literally and treats the project equality-threshold correction separately.

## 5. Validation

Initial direct run:

~~~text
run: 36866938575
~~~

reached the target and exposed one final proof-script coercion in the
temperate-growth transfer.  The finite-set and symbol-correction declarations
had already compiled.  The repair introduced an explicit real equality before
casting to `ℂ`; no statement or hypothesis changed.

Successful corrected run:

~~~text
run: 36867533110
job: 110386685114
checked-out head: db27a3a2536746060d6eb7c3dabe756b7f85b62e
Lean: leanprover/lean4:v4.34.0
mathlib: 5ed2965256430c3649e86755f9576b54eca72435
target: lake build WeilDefect.Morphology.NeutralWeilSourceThreshold
result: PASS (8953 build-graph jobs)
source blob: ae44725b1147992aa0392e130e46611e3a268bad
declaration rejection gate: PASS
~~~

The four inspected endpoint closures report only:

~~~text
propext
Classical.choice
Quot.sound
~~~

No `sorryAx` or project axiom appears in those inspected dependency
closures.

## 6. Remaining source boundary

The threshold convention is no longer part of the ambiguity.

The live external/internal reconstruction frontier is now:

1. place the compact L2 carrier and its polarization partners in the source
   finite-window form domain;
2. reconstruct the Hermitian polarized identity from the source quadratic
   formula for arbitrary complex window-supported inputs;
3. connect that source-local strict action to the already-certified
   shell-corrected frozen action;
4. construct or identify the actual locally integrable whole-line residual
   representative with central vanishing and exponential growth.

The original F-1 null-extension interface contains an abstract endpoint/right
operator and interior-null observation, but it does **not** already supply
this whole-line exponential-growth representative.

## 7. Live continuation

~~~text
RPB-108 / WD-T40 F-4 — CONTINUES

STRICT SOURCE / RIGHT-LIMIT THRESHOLD CORRECTION: CERTIFIED
SOURCE-WINDOW GLOBALIZATION WITH PRIME SHELL: CERTIFIED
HERMITIAN GAUSSIAN BRIDGE: READY DOWNSTREAM

NEXT:
FINITE-WINDOW SOURCE FORM-DOMAIN
+ HERMITIAN POLARIZATION / COMPLEXIFICATION
+ ACTUAL WHOLE-LINE RESIDUAL REPRESENTATIVE ATTACHMENT

LOGARITHMIC COERCIVITY: NOT STARTED
~~~
