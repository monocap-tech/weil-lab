# RPB-83 — WD-T40 F-2 residual-carrier build certification

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **RESIDUAL-CARRIER SLICE BUILD-CERTIFIED / ONE NAMESPACE-SCOPE REPAIR / EXPONENTIAL-GROWTH PHYSICAL CARRIER + ORDINARY DISTRIBUTION ACCESS + COMPACT-TEST WEAK-REALIZATION TARGET ALL COMPILE UNDER LEAN 4.34.0 / REPOSITORY-WIDE TRUST SCAN PASSED / EXT-4 INSTANTIATION NOT STARTED**

## 0. Objective

RPB-82 implemented the corrected full-residual carrier and required the next
pass to do only one thing: compile that module under the pinned toolchain.

RPB-83 executes that gate.

## 1. Validation custody

Temporary validation branch:

~~~text
validation/rpb83-neutral-weil-residual-carrier
~~~

Draft validation PR:

~~~text
#6  Validate RPB-83 residual carrier
~~~

The workflow mutation exists only on the validation branch and targets:

~~~text
WeilDefect.Morphology.NeutralWeilResidualCarrier
~~~

The PR is not merged into the research branch.

## 2. First real compiler diagnostic

Initial exact-target run:

~~~text
run: 36724068300
job: 109916273977
~~~

reached the new module and failed at:

~~~text
NeutralWeilResidualCarrier.lean:46:22
Function expected at Opens
Hint: The identifier Opens is unknown
~~~

The ordinary distribution type used:

~~~lean
Distribution (⊤ : Opens ℝ) ℂ ⊤
~~~

but the `TopologicalSpace` namespace had not been opened in the project
module.

The repair was:

~~~lean
open MeasureTheory TopologicalSpace
~~~

No carrier field, theorem statement, growth hypothesis, vanishing statement,
or weak-realization semantics changed.

Research-branch repair commit:

~~~text
515f53744396f15c77b2531053e8896dc56a85cb
~~~

## 3. Certified source

Module:

~~~text
WeilDefect/Morphology/NeutralWeilResidualCarrier.lean
~~~

Certified Git blob:

~~~text
a26743ed32c75245cd4c952bad3054cd7d51510e
~~~

The certified module includes:

- `NeutralExponentialResidualCarrier`;
- local integrability of the full physical residual;
- fixed exponential-growth control;
- strict central a.e. vanishing;
- ordinary compact-test distribution access via `Distribution.ofFun`;
- `NeutralWeilResidualWeakRealization`;
- compact-support Schwartz weak identity as a target interface.

No EXT-4 constructor theorem is present.

## 4. Successful build evidence

Successful corrected run:

~~~text
run: 36724518728
job: 109917828385
validation head: ea13129a2a8c9a8fbdce1e2589dc8e69a57a0c92
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

Thus the corrected full-residual carrier slice is kernel-checked under the
pinned Lean 4.34.0 / mathlib environment.

## 5. F-2 standing after RPB-83

~~~text
F-2 strict-right scalar symbol:
    BUILD-CERTIFIED

F-2 exponential-growth residual carrier:
    BUILD-CERTIFIED

F-2 compact-test weak-realization target:
    BUILD-CERTIFIED AS AN INTERFACE
    NOT YET INSTANTIATED

F-2 scalar symbol HasTemperateGrowth:
    OPEN

F-2 actual multiplier core construction:
    OPEN

F-2 EXT-4 weak-realization constructor:
    OPEN
~~~

The next dependency is not F-3.

Before the exact symbol can be passed lawfully to mathlib's tempered
Fourier-multiplier machinery, its `HasTemperateGrowth` property must be
proved (or an equivalent source-faithful multiplier route must be constructed).

## 6. RPB-83 determination

~~~math
\boxed{
\textbf{RPB-83 — THE CORRECTED EXPONENTIAL-GROWTH RESIDUAL CARRIER IS BUILD-CERTIFIED; THE NEXT F-2 OBSTRUCTION IS TEMPERATE GROWTH OF THE EXACT SCALAR WEIL SYMBOL.}
}
~~~

WD-T40 remains LEAN-BLOCKED because F-2 is not yet complete.

## Next cursor

~~~text
RPB-84 / WD-T40 F-2 SCALAR-SYMBOL TEMPERATE-GROWTH REALIZATION
~~~

The next pass should address only the exact strict-right symbol's
`HasTemperateGrowth` obligation and, if discharged, expose the canonical
tempered multiplier core.

Do not instantiate EXT-4 and do not begin F-3 in that pass.
