# RPB-82 — WD-T40 F-2 exponential-growth residual carrier

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **SOURCE IMPLEMENTED / CORRECTED FULL-RESIDUAL PHYSICAL CARRIER ADDED / LOCAL INTEGRABILITY + FIXED EXPONENTIAL GROWTH + STRICT CENTRAL A.E. VANISHING TYPED / ORDINARY COMPACT-TEST DISTRIBUTION ACCESS ADDED / EXT-4 WEAK-REALIZATION TARGET INTERFACE ADDED WITHOUT INSTANTIATION / BUILD CERTIFICATION PENDING / F-3 REMAINS CLOSED**

## 0. Objective

RPB-81 established that the pole-restored enlarged Weil residual must not be
forced into the F-1 tempered-distribution type.

RPB-82 implements the corrected carrier only.

No Gaussian support-gap estimate is attempted and no claim is made that EXT-4
already instantiates the new weak operator interface.

## 1. New module

Added:

~~~text
WeilDefect/Morphology/NeutralWeilResidualCarrier.lean
~~~

and registered it in the project root.

## 2. Physical residual carrier

The new structure is:

~~~lean
NeutralExponentialResidualCarrier
~~~

with load-bearing fields:

~~~text
a                         strict enlargement radius
strict                    c < a
q : R -> C                actual whole-line residual representative
q_locallyIntegrable       local integrability
growthConstant
growthRate
growthConstant_nonneg
growthRate_nonneg
growth_bound              ||q(x)|| <= C exp(k |x|)
vanishes_ae               q = 0 a.e. on (-a,a)
~~~

The vanishing field is deliberately **a.e.**, not pointwise.

This matches the natural function/distributional content of the promoted
WD-T40 theorem without adding an unjustified representative-regularity
hypothesis.

## 3. Ordinary distribution access

The carrier defines:

~~~lean
NeutralExponentialResidualCarrier.ordinaryDistribution
~~~

using pinned mathlib's:

~~~lean
Distribution.ofFun
~~~

on the whole real line.

This gives a compact-test distributional view of the locally integrable
physical residual.

It is not used as the sole F-3 carrier because ordinary distributions cannot
canonically consume the noncompact Gaussian test functions used later.

## 4. Strict interval vanishing adapter

The theorem:

~~~lean
vanishes_ae_on_strict_interval
~~~

repackages the stored global a.e. implication as equality almost everywhere
with zero under the restricted measure on

~~~math
(-a,a).
~~~

No pointwise strengthening is introduced.

## 5. Weak-realization target

RPB-82 also introduces:

~~~lean
NeutralWeilResidualWeakRealization
~~~

containing:

~~~text
residual        corrected exponential-growth physical carrier
multiplierCore  tempered scalar-multiplier component
pole            physical pole/evaluation component
pole_locallyIntegrable
weakIdentity
~~~

The weak identity is stated only for **compactly supported Schwartz tests**:

~~~math
\int u(x)q(x)\,dx
=
\langle T_{\rm mult},u\rangle
+
\int u(x)p(x)\,dx.
~~~

This is the common legal test class for:

- the physical locally integrable residual;
- the tempered multiplier core;
- the locally integrable pole function.

The structure is only a target interface.  RPB-82 does **not** construct an
inhabitant from EXT-4.

## 6. Important remaining multiplier issue

Pinned mathlib's tempered Fourier-multiplier constructor is total at the API
level but internally returns zero when the supplied scalar symbol does not
satisfy `HasTemperateGrowth`.

Therefore the mere build certification of

~~~lean
rightLimitCompactWeilSymbol
~~~

does not yet certify that applying
`TemperedDistribution.fourierMultiplierCLM` to that symbol produces the
intended multiplier.

A later F-2 pass must either:

1. prove the exact strict-right scalar symbol has mathlib
   `HasTemperateGrowth`; or
2. construct the multiplier core through an equivalent source-faithful route.

RPB-82 does not hide this obligation inside the new structure.

## 7. F-2 standing

~~~text
F-1 physical Fourier carrier:
    BUILD-CERTIFIED

F-2 strict-right scalar symbol:
    BUILD-CERTIFIED

F-2 full exponential-growth residual carrier:
    SOURCE IMPLEMENTED
    BUILD CERTIFICATE PENDING

F-2 weak-realization interface:
    SOURCE IMPLEMENTED
    NOT YET INSTANTIATED

F-2 scalar-symbol temperate-growth justification:
    OPEN

F-3:
    CLOSED
~~~

## 8. RPB-82 determination

~~~math
\boxed{
\textbf{RPB-82 — THE FULL WEIL RESIDUAL NOW HAS A SOURCE-LEVEL CARRIER MATCHING THE PROMOTED WD-T40 GROWTH HYPOTHESES, WITHOUT FORCING IT INTO TEMPERED DISTRIBUTIONS.}
}
~~~

## Next cursor

~~~text
RPB-83 / WD-T40 F-2 RESIDUAL-CARRIER BUILD CERTIFICATION
~~~

The next pass should compile only
`WeilDefect.Morphology.NeutralWeilResidualCarrier` under the pinned
toolchain, repair genuine compiler diagnostics, and stop.

Do not instantiate EXT-4 or begin F-3 in that pass.
