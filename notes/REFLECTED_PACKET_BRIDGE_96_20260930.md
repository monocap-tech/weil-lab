# RPB-96 — WD-T40 F-4 Fourier normalization audit and repair

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **FOURIER-CONVENTION DEFECT FOUND AND REPAIRED IN SOURCE / SOURCE VARIABLE t MUST MAP TO MATHLIB VARIABLE xi BY t=2*pi*xi / STRICT-RIGHT MULTIPLIER CORE RETARGETED TO THE NORMALIZED SYMBOL / EXISTING F-2/F-3 BUILD CERTIFICATES RETAINED AS HISTORICAL EVIDENCE BUT CURRENT INTEGRATED CERTIFICATE REOPENED / F-4 COERCIVITY NOT YET STARTED**

## 0. Objective

RPB-95 closed the physical-space F-3 Gaussian pairing layer.

RPB-96 was intended to open F-4 logarithmic Gaussian coercivity.

Before any coercive inequality could be stated lawfully, the Fourier
normalization had to be audited.

That audit found a real convention mismatch.

## 1. Source and mathlib Fourier coordinates are different

The pinned EXT-4 compact-window symbol is written in a source frequency
variable \(t\) for which

~~~math
\cos(t\log n)
~~~

corresponds to physical translations by \(\pm\log n\).

Mathlib's real Fourier transform uses

~~~math
\widehat f(\xi)
=
\int_{\mathbb R}
e^{-2\pi i x\xi}f(x)\,dx.
~~~

Hence the lawful coordinate map is

~~~math
\boxed{t=2\pi\xi.}
~~~

This factor had not previously been installed in the Lean multiplier layer.

## 2. Why this is load-bearing

Under mathlib's convention, physical translation by \(a\) produces the
Fourier phase

~~~math
e^{-2\pi i a\xi}.
~~~

Therefore the symmetric translation pair at \(a=\log n\) has scalar factor

~~~math
2\cos(2\pi\xi\log n).
~~~

The source symbol contains

~~~math
2\cos(t\log n),
~~~

so \(t=2\pi\xi\) is required.

A scalar amplitude constant cannot repair this mismatch because the defect is
in the **frequency coordinate**, not merely in normalization amplitude.

The same coordinate change applies to the archimedean digamma term and to the
moving Gaussian frequency window.

## 3. Source repair

The source-frequency symbol remains unchanged:

~~~lean
rightLimitCompactWeilSymbol a t
~~~

RPB-96 adds the mathlib-frequency symbol:

~~~lean
rightLimitCompactWeilSymbolMathlib a ξ :=
  rightLimitCompactWeilSymbol a (2 * Real.pi * ξ)
~~~

with its exact expanded formula.

The imported temperate-growth premise is retargeted to this normalized symbol.

The canonical tempered multiplier core is likewise corrected from

~~~text
Psi_a(source variable) used directly at mathlib xi
~~~

to

~~~text
Psi_a(2*pi*xi).
~~~

## 4. EXT-5 / EXT-5D standing

No new external theorem is needed.

The fixed positive rescaling preserves the asymptotic species:

~~~math
\Psi_a^{src}(t)=\log|t|+O_a(1)
~~~

implies

~~~math
\Psi_a^{ml}(\xi)=\log|\xi|+O_a(1).
~~~

Likewise the EXT-5D derivative-growth bounds remain polynomial after linear
rescaling.

Thus the imported-premise custody class is unchanged.

## 5. Effect on previous certificates

The old build runs are not erased or rewritten.

They remain exact historical compiler evidence for the source blobs that were
present at those checkpoints.

However, the current semantic dependency chain has changed upstream at F-2.

Therefore the present integrated status is:

~~~text
F-1:
    BUILD-CERTIFIED

F-2:
    MATHEMATICAL INTERFACES RETAINED
    FOURIER-CONVENTION SOURCE REPAIRED
    CURRENT BUILD CERTIFICATE REOPENED

F-3:
    PHYSICAL GAUSSIAN THEOREMS RETAIN THEIR LOCAL BUILD CERTIFICATES
    INTEGRATED DOWNSTREAM CERTIFICATE MUST BE REFRESHED AGAINST NORMALIZED F-2

F-4:
    NOT STARTED
~~~

This is a provenance correction, not a mathematical failure of the
support-gap estimate itself.

## 6. Additional F-4 domain audit

RPB-96 also confirms a separate interface that must be handled after the
normalization rebuild:

the current EXT-4 weak realization is stated only for **compactly supported
Schwartz tests**, whereas the moving Gaussian filtered mode is noncompact.

Moreover the stored pole function is only typed as locally integrable.

Therefore the eventual F-4 Fourier quadratic identity requires an explicit
Gaussian-admissibility / pole-growth bridge or an equivalent source-faithful
cutoff argument.

RPB-96 does not silently assume that bridge.

## 7. RPB-96 determination

~~~math
\boxed{
\textbf{RPB-96 — F-4 EXPOSED AN UPSTREAM 2*pi FOURIER-COORDINATE MISMATCH; THE MULTIPLIER SOURCE IS NOW CORRECTED BEFORE COERCIVITY PROCEEDS.}
}
~~~

## Next cursor

~~~text
RPB-97 / WD-T40 FOURIER-NORMALIZATION REPAIR BUILD CERTIFICATION
~~~

The next pass should compile the normalized dependency chain, preferably
through the current terminal F-3 module

~~~text
WeilDefect.Morphology.NeutralGaussianPairing
~~~

so that the corrected multiplier, residual interface, and unchanged F-3
physical layer are checked together.

Do not begin F-4 coercivity until that rebuild gate is green.
