# RPB-68 — WD-T40 physical Fourier carrier lift

**Date:** 2026-09-29  
**Branch:** research/reflected-packet-bridge  
**Status:** **SOURCE IMPLEMENTED / F-1 STRUCTURE ADDED / ABSTRACT WD-T38 MODE NOW LIFTED TO A CONCRETE REAL-LINE L2 REPRESENTATIVE WITH COMPACT SUPPORT AND TEMPERED-DISTRIBUTION FOURIER COMPATIBILITY / STRICT RESIDUAL VANISHING TYPED SEMANTICALLY / BUILD CERTIFICATION INCONCLUSIVE BECAUSE TEMPORARY ACTIONS RUN FAILED BEFORE EXPOSING STEPS OR COMPILER LOGS / WD-T40 REMAINS LEAN-BLOCKED**  
**Dependencies:** RPB-67; WD-T38 Lean interface; mathlib Lp Fourier/tempered-distribution/support APIs.  
**Formal target class:** still **LEAN-CERTIFIED-FROM-IMPORTED-PREMISE** after the remaining formal stack is discharged.

## 0. Objective

RPB-67 identified Formal Blocker F-1:

~~~text
physical real-line Fourier/distribution carrier lift.
~~~

RPB-68 implements that source layer without altering the existing WD-T38
abstract theorem and without moving into F-2.

The new module is

~~~text
WeilDefect/Morphology/NeutralFourierCarrier.lean
~~~

and is imported by the project root WeilDefect.lean.

---

## 1. Concrete physical carrier

The module introduces

~~~lean
abbrev RealComplexL2 := MeasureTheory.Lp (α := ℝ) ℂ 2
~~~

and

~~~lean
abbrev RealComplexTempered := TemperedDistribution ℝ ℂ
~~~

together with

~~~lean
structure NeutralPhysicalFourierCarrier
    (c : ℝ)
    (EndpointObs RightObs : Type*)
    ...
~~~

whose fields include:

~~~lean
h : ℝ → ℂ
h_memLp : MemLp h 2 volume
support_subset : Function.support h ⊆ Set.Icc (-c) c
interface :
  NeutralNullExtensionInterface
    c RealComplexL2 EndpointObs RightObs
kExt_eq_toLp :
  interface.kExt = h_memLp.toLp h
~~~

Thus the WD-T38 abstract mode is identified with the L2 class of an actual
physical representative on the real line.

---

## 2. Adapter back to WD-T38

The module defines

~~~lean
toNeutralNullExtensionInterface
~~~

by forgetting only the extra Fourier-carrier structure.

The theorem

~~~lean
interface_kExt_eq_l2Mode
~~~

records the exact equality between the attached WD-T38 vector and the concrete
L2 mode.

The theorem

~~~lean
l2Mode_ne_zero
~~~

transfers the existing WD-T38 nonzero hypothesis to the concrete L2 carrier.

---

## 3. Compact support is represented at function level

The carrier stores the actual representative

~~~lean
h : ℝ → ℂ
~~~

rather than only an L2 equivalence class.

Its support field is

~~~lean
Function.support h ⊆ Set.Icc (-c) c.
~~~

The theorem

~~~lean
representative_eq_zero_of_not_mem
~~~

extracts pointwise zero outside the certified support interval.

This representation choice is deliberate.

WD-T40 later requires both a canonical L2 object for Fourier/Plancherel and a
concrete representative whose compact support is visible.

The field kExt_eq_toLp binds those two views.

---

## 4. Tempered-distribution lift and Fourier compatibility

The module defines

~~~lean
temperedMode :
  NeutralPhysicalFourierCarrier ... → RealComplexTempered
~~~

by coercing the concrete L2 mode into the mathlib tempered-distribution
carrier.

It then proves

~~~lean
fourier_temperedMode_eq
~~~

using the existing mathlib theorem

~~~lean
MeasureTheory.Lp.fourier_toTemperedDistribution_eq.
~~~

No custom Fourier compatibility axiom is introduced.

---

## 5. Strict residual vanishing is now semantically typed

The module also introduces

~~~lean
structure NeutralStrictResidualData (c : ℝ)
~~~

with fields

~~~lean
a : ℝ
strict : c < a
residual : RealComplexTempered
residual_vanishes :
  Distribution.IsVanishingOn residual (Set.Ioo (-a) a)
~~~

Mathlib's Distribution.IsVanishingOn means exactly that the distribution
annihilates every Schwartz/test function whose topological support lies in the
target interval.

The theorem

~~~lean
vanishes_on_old_interval
~~~

transfers vanishing from the strict enlarged interval back to the old open
support interval.

---

## 6. What is deliberately not encoded yet

RPB-68 does **not** assert

~~~math
\text{residual}
=
\mathcal W_a^{\rm ext}h.
~~~

That equality is Formal Blocker F-2.

The new strict residual data therefore does not yet claim that the typed
tempered distribution is the actual Weil residual.

This separation prevents the carrier layer from smuggling the multiplier
realization into a structure field.

---

## 7. Build-validation attempt

The repository's normal push workflow runs only on the main branch and its
build step targets

~~~text
WeilDefect.Examples.WeakCriticalFallthrough
~~~

which does not transitively import the new carrier module.

To avoid altering the research-branch workflow merely for validation, RPB-68
created a temporary branch

~~~text
validation/rpb68-neutral-fourier-carrier
~~~

and draft PR #1 against

~~~text
research/reflected-packet-bridge.
~~~

The only additional validation-branch change was to add

~~~text
WeilDefect.Morphology.NeutralFourierCarrier
~~~

to the CI build target.

GitHub Actions run

~~~text
36638336287
~~~

completed with conclusion failure.

However:

- the connector returned no job steps;
- the workflow job exposed no decoded compiler log;
- the combined commit status contained no theorem/compiler status;
- the run completed before any usable Lean diagnostic was available.

Therefore this run cannot lawfully be classified as a Lean compile failure of
the carrier source.

The validation PR was closed without merge.

The research branch never received the temporary CI-only workflow change.

---

## 8. Current F-1 standing

~~~text
F-1 SOURCE DESIGN:
    IMPLEMENTED

F-1 ABSTRACT WD-T38 ADAPTER:
    IMPLEMENTED

F-1 CONCRETE L2 REPRESENTATIVE:
    IMPLEMENTED

F-1 COMPACT SUPPORT FIELD:
    IMPLEMENTED

F-1 L2 -> TEMPERED DISTRIBUTION FOURIER COMPATIBILITY:
    IMPLEMENTED

F-1 STRICT RESIDUAL VANISHING TYPE:
    IMPLEMENTED

F-1 LEAN BUILD CERTIFICATE:
    NOT YET OBTAINED
~~~

Thus F-1 is source-complete but not yet certification-complete.

WD-T40 remains

~~~text
LEAN-BLOCKED.
~~~

---

## 9. RPB-68 determination

~~~math
\boxed{
\textbf{RPB-68 — THE PHYSICAL FOURIER CARRIER LAYER NOW EXISTS IN LEAN SOURCE, BUT IT MUST PASS A REAL MODULE BUILD BEFORE F-1 IS CLOSED.}
}
~~~

No WD-T40 mathematical statement changed.

No surrogate formal theorem was introduced.

## Next cursor

~~~text
RPB-69 / WD-T40 PHYSICAL FOURIER CARRIER BUILD CERTIFICATION
~~~

The next pass should solve only the F-1 build gate.

Priority order:

1. establish a validation route that actually compiles
   WeilDefect.Morphology.NeutralFourierCarrier;
2. repair any genuine Lean errors produced by that build;
3. record a successful module-level certificate or exact unresolved compiler
   blocker;
4. only after a successful build advance to F-2 / actual Weil multiplier
   realization.
