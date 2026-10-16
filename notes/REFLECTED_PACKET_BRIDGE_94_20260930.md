# RPB-94 — WD-T40 F-3 final residual pairing integral

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **FINAL F-3 PAIRING SOURCE IMPLEMENTED / WHOLE-LINE PAIRING REDUCED A.E. TO THE EXTERIOR / EXTERIOR PRODUCT INTEGRABILITY IMPLEMENTED / TWO HALF-LINE GAUSSIAN MASSES BOUNDED BY TWO FULL TRANSLATED GAUSSIANS / EXPLICIT PAIRING NORM BOUND IMPLEMENTED / BUILD CERTIFICATION PENDING / F-4 NOT STARTED**

## 0. Objective

RPB-93 build-certified every analytic ingredient of F-3 except the final
whole-line physical pairing estimate.

RPB-94 packages those pieces into the actual residual pairing.

## 1. New module

Added:

~~~text
WeilDefect/Morphology/NeutralGaussianPairing.lean
~~~

and registered it in the project root.

## 2. Global physical regularity helpers

The source first closes the small regularity interfaces needed for the pairing:

~~~lean
neutralPhysicalRepresentative_integrable
movingGaussianPhysicalKernel_continuous
movingGaussianPhysicalKernel_bddAbove_norm
movingGaussianFilteredMode_eq_convolution
movingGaussianFilteredMode_continuous
~~~

Thus the actual filtered mode is not merely a pointwise integral with a
formal bound; it is recognized as a continuous whole-line convolution of the
globally integrable compactly supported F-1 representative with the bounded
continuous moving Gaussian kernel.

## 3. Completed exterior product bound

The theorem

~~~lean
residualFilteredMode_norm_le_completedTail
~~~

combines:

- the certified exponential-growth residual bound;
- the certified full exterior filtered-mode Gaussian envelope; and
- the certified Gaussian completion inequality.

It yields, on the exterior,

~~~math
|q(x)G_R(x)|
\le
A_R
e^{-R(|x|-c)^2/16},
~~~

where

~~~math
A_R
=
C_q |C_K|\sqrt R\,
\|h\|_{L^1([-c,c])}
e^{\kappa c}
e^{-R(a-c)^2/16}.
~~~

The theorem

~~~lean
residualFilteredMode_integrableOn_exterior
~~~

then proves the actual residual-filtered-mode product is integrable on the two
exterior half-lines.

## 4. Exact Gaussian tail mass bound

The theorem

~~~lean
gaussianExteriorTail_integral_le
~~~

splits the exterior into

~~~math
(-\infty,-a]\cup[a,\infty),
~~~

uses the sign-specific formulas for `|x|), and bounds each translated
half-line Gaussian by its corresponding full translated Gaussian.

Translation invariance and `integral_gaussian` then give

~~~math
\boxed{
\int_{\mathrm{ext}}
e^{-R(|x|-c)^2/16}\,dx
\le
2\sqrt{\frac{\pi}{R/16}}.
}
~~~

This is the quantitative step that cancels the kernel's `sqrt R`
normalization up to fixed constants.

## 5. Whole-line residual pairing

RPB-94 defines:

~~~lean
movingGaussianResidualPairing
~~~

for

~~~math
\int_{\mathbb R}q(x)G_R(x)\,dx.
~~~

The theorem

~~~lean
movingGaussianResidualPairing_norm_le
~~~

uses the certified field

~~~lean
residual.vanishes_ae
~~~

to reduce the whole-line integral exactly to the exterior via
`setIntegral_eq_integral_of_ae_compl_eq_zero`.

It then applies the completed pointwise majorant and the Gaussian tail mass
bound to obtain:

~~~math
\boxed{
|\langle q,G_R\rangle|
\le
C_q |C_K|\sqrt R\,
\|h\|_1
e^{\kappa c}
e^{-R(a-c)^2/16}
\cdot
2\sqrt{\frac{\pi}{R/16}}.
}
~~~

No Fourier-side logarithmic coercivity is used.

## 6. F-3 standing

~~~text
support-gap geometry:
    BUILD-CERTIFIED

actual filtered-mode envelope:
    BUILD-CERTIFIED

Gaussian completion:
    BUILD-CERTIFIED

exterior Gaussian tail integrability:
    BUILD-CERTIFIED

final whole-line residual pairing:
    SOURCE IMPLEMENTED

final F-3 build certificate:
    PENDING
~~~

Thus the mathematical F-3 source stack is now complete, but F-3 is not yet
marked closed until this final module passes the pinned Lean build.

## 7. RPB-94 determination

~~~math
\boxed{
\textbf{RPB-94 — THE FINAL WHOLE-LINE RESIDUAL PAIRING ESTIMATE IS IMPLEMENTED IN LEAN SOURCE FROM THE CERTIFIED F-2/F-3 CARRIERS, WITH NO NEW IMPORTED PREMISE.}
}
~~~

## Next cursor

~~~text
RPB-95 / WD-T40 F-3 FINAL PAIRING BUILD CERTIFICATION
~~~

The next pass should compile only
`WeilDefect.Morphology.NeutralGaussianPairing`, repair genuine compiler
diagnostics, and stop.

Do not begin F-4 until that final F-3 build gate closes.
