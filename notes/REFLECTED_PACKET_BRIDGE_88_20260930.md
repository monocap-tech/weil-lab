# RPB-88 — WD-T40 F-3 Gaussian support-gap geometry entry

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **F-3 OPEN / SOURCE IMPLEMENTED FOR STRICT SUPPORT-GAP GEOMETRY AND EXTERIOR POINTWISE GAUSSIAN DOMINATION / NO TAIL INTEGRAL YET / NO LOGARITHMIC COERCIVITY / BUILD CERTIFICATION PENDING**

## 0. Objective

RPB-87 closed F-2.

RPB-88 opens F-3 but deliberately takes only the first internal analytic
sublayer: turn the strict collar

~~~math
0\le c<a
~~~

and exterior condition

~~~math
x\notin(-a,a)
~~~

into the quantitative Gaussian support-gap exponent used by the residual
pairing argument.

No F-4 coercivity is touched.

## 1. New module

Added:

~~~text
WeilDefect/Morphology/NeutralGaussianSupportGap.lean
~~~

and registered it in the project root.

## 2. Gaussian envelope

The module defines:

~~~lean
gaussianSupportEnvelope R c x
=
exp (-R * (|x|-c)^2 / 4).
~~~

This is the modulus profile of the physical moving-frequency Gaussian kernel
after convolution against a mode supported in `[-c,c]`.

RPB-88 does not yet prove that the actual filtered mode satisfies this
envelope. That kernel/convolution estimate is the next F-3 subproblem.

## 3. Strict support-gap geometry

The source proves:

~~~lean
radius_le_abs_of_not_mem_Ioo
supportGap_le_abs_sub
supportGap_sq_le_abs_sub_sq
~~~

giving the chain

~~~math
x\notin(-a,a)
\Longrightarrow
a\le |x|
\Longrightarrow
a-c\le |x|-c
\Longrightarrow
(a-c)^2\le(|x|-c)^2.
~~~

The support-radius premise is retained explicitly as `0 <= c`.

## 4. Gaussian suppression from the collar

The theorem:

~~~lean
gaussianSupportEnvelope_le_gap
~~~

deduces, for `R >= 0`,

~~~math
e^{-R(|x|-c)^2/4}
\le
e^{-R(a-c)^2/4}
~~~

on the exterior of `(-a,a)`.

This is the exact geometric exponential factor consumed by the later pairing
estimate.

## 5. Residual-product domination

Two pointwise theorems are added:

~~~lean
residual_mul_gaussianEnvelope_bound
residual_mul_gaussianExterior_bound
~~~

Given a filtered mode `g` satisfying the expected physical Gaussian envelope,

~~~math
|g(x)|
\le
A\sqrt R\,
e^{-R(|x|-c)^2/4},
~~~

the certified F-2 residual growth bound gives:

~~~math
|q(x)g(x)|
\le
C_q e^{\kappa_q |x|}
A\sqrt R,
e^{-R(|x|-c)^2/4}.
~~~

On the strict exterior, RPB-88 further extracts the collar factor

~~~math
e^{-R(a-c)^2/4}.
~~~

The remaining exponential-growth/Gaussian-tail integration is intentionally
not claimed here.

## 6. What remains in F-3

F-3 is not closed.

Two internal steps remain:

1. derive the filtered-mode envelope from the actual Gaussian convolution
   kernel and compact support of the F-1 mode;
2. integrate the exponential-growth residual against that Gaussian tail and
   obtain the pairing estimate
   `|<q,phi_R(D)h>| <= C exp(-kappa R)`.

Only after those steps are build-certified may F-4 open.

## 7. RPB-88 determination

~~~math
\boxed{
\textbf{RPB-88 — THE STRICT COLLAR NOW PRODUCES THE CORRECT EXTERIOR GAUSSIAN SUPPRESSION FACTOR IN LEAN SOURCE; F-3 REMAINS OPEN AT THE ACTUAL FILTERED-MODE AND TAIL-INTEGRATION STEPS.}
}
~~~

## Next cursor

~~~text
RPB-89 / WD-T40 F-3 SUPPORT-GAP GEOMETRY BUILD CERTIFICATION
~~~

The next pass should compile only
`NeutralGaussianSupportGap`, repair genuine compiler diagnostics, and stop.

Do not begin the Gaussian convolution/tail integral until that source slice is
build-certified.
