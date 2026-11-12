# RPB-90 — WD-T40 F-3 filtered-mode Gaussian envelope

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **SOURCE IMPLEMENTED / ACTUAL MOVING-GAUSSIAN PHYSICAL KERNEL ADDED WITH EXPLICIT FOURIER-NORMALIZATION CONSTANT / F-1 COMPACT REPRESENTATIVE SHOWN L1-INTEGRABLE ON SUPPORT / ACTUAL COMPACT-SUPPORT CONVOLUTION DEFINED / EXTERIOR FILTERED-MODE GAUSSIAN ENVELOPE IMPLEMENTED / RPB-88 GLOBAL-ENVELOPE EXPECTATION CORRECTED TO EXTERIOR-ONLY USE / BUILD CERTIFICATION PENDING / TAIL INTEGRATION NOT STARTED**

## 0. Objective

RPB-89 build-certified the strict support-gap geometry slice.

RPB-90 addresses only the next internal F-3 obligation: derive the physical
Gaussian envelope for the actual filtered F-1 mode.

## 1. Interface correction

RPB-88 had introduced a generic hypothesis of the form

~~~math
|g(x)| \le A\sqrt R\,e^{-R(|x|-c)^2/4}
~~~

for all real (x).

That global form is too strong for the actual compact-support convolution:
inside ([-c,c]), one may choose (y\approx x), so the kernel distance
(|x-y|) can be zero even when ((|x|-c)^2>0).

The actual WD-T40 argument never needs such an interior estimate, because the
full residual vanishes on the strict enlarged interval ((-a,a)).

RPB-90 therefore uses the correct exterior-only formulation.

## 2. Moving Gaussian physical kernel

The source now defines

~~~lean
movingGaussianPhysicalKernel
~~~

with an explicit normalization constant (C_K\in\mathbb C):

~~~math
K_{R,C_K}(z)
=
C_K\sqrt R\,
e^{-R|z|^2/4}
e^{iRz}.
~~~

The exact modulus theorem is implemented as:

~~~lean
norm_movingGaussianPhysicalKernel
~~~

The constant (C_K) is intentionally retained rather than silently fixing a
Fourier normalization.

## 3. Compact L1 mass of the F-1 representative

Using the certified F-1 field

~~~lean
h_memLp : MemLp h 2 volume
~~~

and local finiteness of Lebesgue measure, RPB-90 derives compact integrability
on the certified support interval:

~~~lean
neutralPhysicalRepresentative_integrableOn
~~~

and defines:

~~~lean
neutralPhysicalCompactL1Mass
~~~

for

~~~math
\int_{-c}^{c}|h(y)|\,dy.
~~~

## 4. Actual filtered mode

The source defines the physical convolution:

~~~lean
movingGaussianFilteredMode
~~~

corresponding to

~~~math
G_R(x)
=
\int_{-c}^{c}
h(y)K_{R,C_K}(x-y)\,dy.
~~~

No Fourier-side coercivity is used here.

## 5. Exterior support-gap transfer to the kernel

The theorem:

~~~lean
supportGap_le_abs_sub_point
~~~

proves that if

~~~math
x\notin(-a,a),
\qquad
y\in[-c,c],
\qquad
0\le c<a,
~~~

then

~~~math
a-c\le |x-y|.
~~~

This is the actual convolution geometry needed by the Gaussian kernel.

The theorem:

~~~lean
movingGaussianPhysicalKernel_norm_le_gap
~~~

then gives

~~~math
|K_{R,C_K}(x-y)|
\le
|C_K|\sqrt R\,
e^{-R(a-c)^2/4}.
~~~

## 6. Actual exterior filtered-mode envelope

RPB-90 implements:

~~~lean
movingGaussianFilteredMode_norm_le_exterior
~~~

which proves

~~~math
|G_R(x)|
\le
|C_K|\sqrt R\,
e^{-R(a-c)^2/4}
\int_{-c}^{c}|h(y)|\,dy
~~~

for every

~~~math
x\notin(-a,a).
~~~

This is exactly the filtered-mode envelope required before pairing with the
exponential-growth residual.

## 7. F-3 standing

~~~text
strict support-gap geometry:
    BUILD-CERTIFIED

exterior pointwise residual domination:
    BUILD-CERTIFIED

actual moving Gaussian kernel:
    SOURCE IMPLEMENTED

actual filtered-mode compact-support convolution:
    SOURCE IMPLEMENTED

actual exterior filtered-mode envelope:
    SOURCE IMPLEMENTED

build certification:
    PENDING

Gaussian residual tail integration:
    OPEN
~~~

## 8. RPB-90 determination

~~~math
\boxed{
\textbf{RPB-90 — THE ACTUAL COMPACTLY SUPPORTED F-1 MODE NOW HAS THE CORRECT EXTERIOR MOVING-GAUSSIAN CONVOLUTION ENVELOPE IN LEAN SOURCE; THE ONLY REMAINING F-3 ANALYTIC STEP IS THE EXPONENTIAL-GROWTH TAIL INTEGRATION.}
}
~~~

## Next cursor

~~~text
RPB-91 / WD-T40 F-3 FILTERED-MODE ENVELOPE BUILD CERTIFICATION
~~~

The next pass should compile only the updated
`NeutralGaussianSupportGap` module, repair genuine compiler diagnostics, and
stop.

Do not begin the residual tail integral until this convolution-envelope slice
is build-certified.
