# RPB-81 — WD-T40 F-2 residual-carrier audit

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **INTERFACE CORRECTION / FULL ENLARGED RESIDUAL MUST NOT BE IDENTIFIED WITH THE F-1 TEMPERED RESIDUAL TYPE / SCALAR MULTIPLIER CORE REMAINS TEMPERED / POLE-EVALUATION TERM MAY HAVE FIXED EXPONENTIAL GROWTH / F-2 REQUIRES A BROADER PHYSICAL RESIDUAL CARRIER BEFORE THE WEAK OPERATOR IDENTITY CAN BE STATED FAITHFULLY / NO F-3 WORK OPENED**

## 0. Objective

RPB-80 build-certified the exact strict-right scalar Weil symbol.

RPB-81 was authorized to connect that symbol, the F-1 physical mode, and the
separate pole/evaluation contribution to the actual enlarged residual.

Before writing the bridge, this pass audits the target carrier against the
promoted WD-T40 proof and the pinned mathlib distribution APIs.

The audit finds a genuine interface mismatch.

## 1. The F-1 residual type is tempered

F-1 introduced:

~~~lean
abbrev RealComplexTempered := TemperedDistribution ℝ ℂ

structure NeutralStrictResidualData (c : ℝ) where
  a : ℝ
  strict : c < a
  residual : RealComplexTempered
  residual_vanishes :
    Distribution.IsVanishingOn residual (Set.Ioo (-a) a)
~~~

This was deliberately introduced before the residual was identified with the
actual Weil operator.

That separation now matters.

## 2. The promoted WD-T40 residual is broader

RPB-64/65 describe the pole/evaluation contribution as lying in a fixed
finite-dimensional span of real exponentials, schematically

~~~math
e^{\pm x/2}.
~~~

The same audit explicitly allows the full enlarged residual to have **fixed
exponential growth** outside the null interval.

Such functions are locally integrable and define ordinary distributions on
compactly supported test functions, but they are not in general tempered:
Schwartz decay is faster than every polynomial, not necessarily faster than a
fixed exponential.

Therefore the implication

~~~text
actual full enlarged residual q
    ->
TemperedDistribution ℝ ℂ
~~~

is not justified by the mathematical theorem being formalized.

This is not a defect in the certified F-1 carrier mode or Fourier transform.
It is a scope defect only in trying to reuse `NeutralStrictResidualData` as
the **full pole-restored residual**.

## 3. What remains safely tempered

The scalar multiplier part

~~~math
\Psi_a^{\rm right}(D)h
~~~

belongs to the tempered/Fourier side of the construction.

Pinned mathlib provides:

~~~lean
TemperedDistribution.fourierMultiplierCLM
TemperedDistribution.fourierMultiplierCLM_apply_apply
~~~

so the build-certified scalar symbol can be applied to the F-1 tempered mode
without inventing a new Fourier theory.

That is still the correct tempered core of F-2.

## 4. Pinned general-distribution support

Pinned mathlib also provides the newer ordinary distribution space

~~~text
Distribution
~~~

on compactly supported test functions and, in particular,

~~~lean
Distribution.ofFun
~~~

for locally integrable physical functions.

This carrier can accommodate fixed exponential functions because test
functions have compact support.

However, no packaged direct coercion from the project's
`TemperedDistribution` carrier into that newer `Distribution` API was
identified in the pinned corpus.

A project-local restriction map is therefore required if the multiplier core
is to be combined there with the pole distribution.

## 5. Why an ordinary distribution alone is still insufficient for F-3

WD-T40's next analytic step pairs the full residual with a **noncompact
Gaussian** filtered mode.

Ordinary distributions act canonically only on compactly supported test
functions.

Therefore merely changing

~~~text
TemperedDistribution -> Distribution
~~~

would fix the pole-growth typing but still would not expose the Gaussian
pairing needed by F-3.

The faithful full residual carrier must retain physical-function or weighted
pairing data, for example:

~~~text
q : ℝ -> ℂ
local integrability
fixed exponential-growth bound
compact-test distribution identity
strict central vanishing
~~~

so that Gaussian integrals can later be justified directly from the growth
bound.

RPB-81 does not canonize the final Lean structure yet; it fixes the required
semantics.

## 6. Corrected F-2 architecture

The lawful architecture is now:

~~~text
F-1 physical mode h
    |
    v
certified strict-right scalar symbol
    |
    v
tempered multiplier core Ψ_a(D)h
    +
explicit pole/evaluation physical component
    |
    v
full exponential-growth residual q
    |
    +-- compact-test weak identity
    +-- strict vanishing on (-a,a)
    +-- growth data for later Gaussian pairing
~~~

The imported EXT-4 compact-window formula may supply the equality identifying
these pieces.

It may **not** supply the Gaussian support-gap estimate, exponential Fourier
decay, or strip-holomorphy conclusion; those remain F-3 through F-5.

## 7. Effect on F-1 custody

F-1 remains BUILD-CERTIFIED.

No existing F-1 theorem is retracted.

The additive correction is only:

~~~text
NeutralStrictResidualData.residual
must not be interpreted as the full pole-restored enlarged residual
without an additional proof that the full residual is tempered.
~~~

Since the source comments already deferred the actual Weil-residual
identification to F-2, the certified F-1 mathematical claims remain intact.

## 8. RPB-81 determination

~~~math
\boxed{
\textbf{RPB-81 — F-2 CANNOT LAWFULLY IDENTIFY THE FULL WEIL RESIDUAL WITH THE F-1 TEMPERED RESIDUAL TYPE; A BROADER EXPONENTIAL-GROWTH PHYSICAL CARRIER IS REQUIRED.}
}
~~~

Current state:

~~~text
F-1  BUILD-CERTIFIED

F-2  IN PROGRESS
     strict-right scalar symbol: BUILD-CERTIFIED
     tempered multiplier core: API AVAILABLE
     full residual carrier: REQUIRES CORRECTION
     weak operator-residual identity: NOT YET STATED

F-3  CLOSED
F-4  CLOSED
F-5  CLOSED
F-6  CLOSED
~~~

WD-T40 remains LEAN-BLOCKED.

## Next cursor

~~~text
RPB-82 / WD-T40 F-2 EXPONENTIAL-GROWTH RESIDUAL CARRIER
~~~

The next pass should design and implement the corrected physical residual
carrier with:

1. an actual whole-line residual function;
2. local-integrability / ordinary-distribution access;
3. fixed exponential-growth control;
4. strict central vanishing;
5. a slot for the EXT-4 weak identity tying it to the certified tempered
   multiplier core plus the explicit pole/evaluation component.

Stop before Gaussian support-gap pairing.
