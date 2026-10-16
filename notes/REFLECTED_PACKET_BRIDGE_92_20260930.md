# RPB-92 — WD-T40 F-3 residual Gaussian tail completion

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **SOURCE IMPLEMENTED / FULL EXTERIOR FILTERED-MODE GAUSSIAN ENVELOPE RETAINED / RESIDUAL EXPONENTIAL GROWTH ABSORBED BY COMPLETION-OF-THE-SQUARE / REMAINING EXTERIOR GAUSSIAN TAIL PROVED INTEGRABLE IN SOURCE / BUILD CERTIFICATION PENDING / FINAL PAIRING-INTEGRAL NUMERICAL BOUND STILL OPEN / F-4 NOT STARTED**

## 0. Objective

RPB-91 build-certified the actual filtered-mode exterior envelope with the
collar factor extracted.

RPB-92 audits whether that collar-only estimate is enough to integrate against
the certified residual growth

~~~math
|q(x)|\le C_q e^{\kappa |x|}.
~~~

It is not.

The collar-only estimate discards the remaining physical Gaussian decay in
`x`, leaving a nonintegrable factor `e^{\kappa |x|}`.

Therefore RPB-92 retains the full exterior Gaussian envelope through the
pairing and performs the correct completion-of-the-square reduction.

## 1. New module

Added:

~~~text
WeilDefect/Morphology/NeutralGaussianTail.lean
~~~

and registered it in the project root.

## 2. Full exterior filtered-mode envelope

The new theorem

~~~lean
movingGaussianPhysicalKernel_norm_le_exteriorEnvelope
~~~

proves, for

~~~math
x\notin(-a,a),
\qquad
y\in[-c,c],
\qquad
0\le c<a,
~~~

that

~~~math
|K_{R,C_K}(x-y)|
\le
|C_K|\sqrt R\,
e^{-R(|x|-c)^2/4}.
~~~

This retains the entire physical Gaussian tail instead of collapsing it to the
constant collar factor.

The corresponding actual convolution theorem

~~~lean
movingGaussianFilteredMode_norm_le_exteriorEnvelope
~~~

gives

~~~math
|G_R(x)|
\le
|C_K|\sqrt R\,
e^{-R(|x|-c)^2/4}
\int_{-c}^{c}|h(y)|\,dy
~~~

on the exterior.

## 3. Tail completion

Set

~~~math
\delta=a-c>0,
\qquad
d(x)=|x|-c.
~~~

The new theorem

~~~lean
gaussianTailCompletion_bound
~~~

shows that if

~~~math
8\kappa\le R\delta,
~~~

then on the exterior

~~~math
e^{\kappa|x|}
e^{-R d(x)^2/4}
\le
e^{\kappa c}
e^{-R\delta^2/16}
e^{-R d(x)^2/16}.
~~~

Thus the fixed exponential growth of the residual is absorbed into half of the
Gaussian exponent while a uniform exponentially small factor in `R` is
extracted.

## 4. Exterior Gaussian integrability

The module defines:

~~~lean
gaussianExteriorSet a
=
Iic (-a) union Ici a.
~~~

The theorem

~~~lean
gaussianExteriorTail_integrableOn
~~~

proves, for `R>0`,

~~~math
x\mapsto
e^{-R(|x|-c)^2/16}
~~~

is integrable on those two exterior half-lines.

The proof splits the two signs of `x` and reduces each half-line to a
translated ordinary real Gaussian, using the pinned mathlib Gaussian
integrability theorem.

## 5. What RPB-92 does not yet claim

RPB-92 does **not** yet package the completed pointwise majorant into the final
whole-line residual pairing bound

~~~math
|<q,G_R>|
\le
C e^{-\kappa'R}.
~~~

One final F-3 integration step remains:

1. use the residual's a.e. vanishing on `(-a,a)`;
2. dominate the exterior integrand by the completed Gaussian tail;
3. evaluate or uniformly bound the translated Gaussian tail mass;
4. absorb the remaining `sqrt R` normalization.

No logarithmic symbol lower bound is used in RPB-92.

## 6. F-3 standing

~~~text
strict support-gap geometry:
    BUILD-CERTIFIED

actual filtered-mode exterior envelope:
    BUILD-CERTIFIED

full x-dependent exterior envelope:
    SOURCE IMPLEMENTED

Gaussian completion against residual growth:
    SOURCE IMPLEMENTED

exterior Gaussian tail integrability:
    SOURCE IMPLEMENTED

source build:
    PENDING

final residual pairing integral bound:
    OPEN
~~~

## 7. RPB-92 determination

~~~math
\boxed{
\textbf{RPB-92 — THE FIXED EXPONENTIAL RESIDUAL GROWTH IS NOW REDUCED TO AN ORDINARY INTEGRABLE GAUSSIAN TAIL WITHOUT LOSING THE EXPONENTIAL COLLAR FACTOR IN R.}
}
~~~

F-3 remains open. F-4 remains closed.

## Next cursor

~~~text
RPB-93 / WD-T40 F-3 GAUSSIAN TAIL COMPLETION BUILD CERTIFICATION
~~~

The next pass should compile only
`WeilDefect.Morphology.NeutralGaussianTail`, repair genuine compiler
diagnostics, and stop.

Do not begin the final pairing integral or F-4 before that build gate closes.
