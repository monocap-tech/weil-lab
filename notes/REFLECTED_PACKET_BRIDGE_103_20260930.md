# RPB-103 — WD-T40 F-4 Gaussian Schwartz seed and moving-mode Fourier identification

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **COMPLETE / BUILD-CERTIFIED / ACTUAL MOVING FILTERED MODE BUNDLED AS SCHWARTZMAP / POINTWISE IDENTIFICATION CERTIFIED / NO NEW IMPORTED PREMISE / CUTOFF CONVERGENCE NOT STARTED**

## 0. Objective

RPB-102 reduced the open Schwartz burden to a Gaussian-only construction:
bundle the exact physical moving Gaussian kernel as a Schwartz function, combine
it with the certified temperate Fourier multiplier of the F-1 carrier, invert
the Fourier transform, and identify the resulting Schwartz function with the
existing F-3 filtered mode.

RPB-103 closes that burden.

## 1. Gaussian Schwartz seed

The new module

~~~text
WeilDefect/Morphology/NeutralGaussianSchwartzSeed.lean
~~~

constructs the standard Gaussian

~~~math
x \mapsto e^{-x^2/2}
~~~

as an actual `SchwartzMap ℝ ℝ`.

The proof uses mathlib's Hermite derivative formula together with the existing
superpolynomial-decay theorem for real Gaussians.  It then obtains the project
centered Gaussian

~~~math
x \mapsto e^{-R x^2/4}
~~~

for `R > 0` by positive linear rescaling, complexifies it, and multiplies by
the oscillatory phase

~~~math
x \mapsto e^{iRx},
~~~

whose temperate growth is already available in mathlib.

The exact project physical kernel is therefore bundled as

~~~lean
movingGaussianPhysicalKernelSchwartz
~~~

with pointwise theorem

~~~lean
movingGaussianPhysicalKernelSchwartz_apply
~~~

identifying it with the already-used

~~~lean
movingGaussianPhysicalKernel Ck R.
~~~

No change of kernel normalization is introduced.

## 2. Frequency-side filtered mode

The second new module

~~~text
WeilDefect/Morphology/NeutralGaussianFilteredSchwartz.lean
~~~

defines

~~~lean
movingGaussianFrequencyProductSchwartz
~~~

by multiplying the Schwartz Fourier transform of the Gaussian kernel by the
RPB-102 temperate multiplier `𝓕 carrier.h`.

Mathlib's convolution/Fourier theorem gives the exact identity

~~~math
\widehat h(\xi)\,\widehat K_R(\xi)
=
\mathcal F(h*K_R)(\xi).
~~~

Thus no manually inserted Fourier-normalization constant is required beyond
the explicit `Ck` already present in the physical kernel.

## 3. Fourier inversion and pointwise identification

Define

~~~lean
movingGaussianFilteredModeSchwartz
~~~

as the inverse Fourier transform of that frequency-side Schwartz product.

The source proves:

~~~lean
movingGaussianFilteredModeSchwartz_eq_convolution
~~~

using:

- global L1 integrability of the compactly supported representative;
- integrability and boundedness of the Schwartz Gaussian kernel;
- continuity and L1 integrability of the convolution;
- Fourier multiplication/convolution;
- the ordinary Fourier inversion theorem.

Finally:

~~~lean
movingGaussianFilteredModeSchwartz_apply
~~~

proves pointwise

~~~math
\texttt{movingGaussianFilteredModeSchwartz}\;C_k\;R\;h_R\;carrier\;x
=
\texttt{movingGaussianFilteredMode}\;C_k\;R\;carrier\;x.
~~~

The last step uses the certified support of `carrier.h` to replace the
whole-line convolution integral by the original integral over `[-c,c]`.

Therefore burden A from RPB-100 is fully discharged.

## 4. Validation and custody reconciliation

An earlier green validation lineage was checked against a fresh reconstruction
because one intermediate commit appeared to remove a local global-L1 lemma.

The fresh compiler run showed that this theorem was already supplied upstream
by `NeutralGaussianPairing`; reintroducing it locally correctly generated a
duplicate-declaration error.  After removing that duplicate, the full module
was rebuilt from the reconciled tree.

Final successful validation:

~~~text
run:  36799159760
job:  110169382060
head: 105afd4f4fdb215e138af4af642ff2acfa165512

Gaussian seed blob:
5874ebc61f915e4612fa6ee02bec033a418b0d6a

Filtered-mode realization blob:
c639b2f5df08d2365cf9dc0c6933a60ed72dbebe
~~~

The run passed:

~~~text
lake build WeilDefect.Morphology.NeutralGaussianFilteredSchwartz
~~~

and the repository-wide rejection gate for `axiom`, `sorry`, and `admit`.

## 5. RPB-103 determination

~~~math
\boxed{
\textbf{RPB-103 — THE ACTUAL MOVING-GAUSSIAN FILTERED MODE IS NOW A BUILD-CERTIFIED SCHWARTZ FUNCTION, POINTWISE IDENTICAL TO THE EXISTING F-3 PHYSICAL CONVOLUTION.}
}
~~~

No smoothness assumption on `carrier.h` was added and no new imported
analytic premise was introduced.

## 6. Remaining F-4 pre-coercivity burden

After RPB-103, the RPB-100 list becomes:

~~~text
A. actual moving filtered mode as SchwartzMap — CLOSED
B. compactly supported Schwartz cutoffs converging in Schwartz topology — OPEN
C. residual pairing convergence along those cutoffs — OPEN
D. pole pairing convergence along those cutoffs — OPEN
E. actual EXT-4 pole exponential-growth instantiation — OPEN
~~~

The logarithmic coercivity theorem itself remains unopened.

## Next cursor

~~~text
RPB-104 / WD-T40 F-4 COMPACT SCHWARTZ CUTOFF CONSTRUCTION + SCHWARTZ-TOPOLOGY CONVERGENCE
~~~

Construct compactly supported Schwartz approximants to
`movingGaussianFilteredModeSchwartz` and certify convergence in Schwartz
topology.

Do not begin residual/pole pairing convergence or logarithmic coercivity until
this cutoff sequence exists.
