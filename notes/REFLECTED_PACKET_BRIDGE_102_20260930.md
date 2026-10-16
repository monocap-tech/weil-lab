# RPB-102 — WD-T40 F-4 moving-filtered-mode Schwartz realization: carrier-side reduction

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **CARRIER-SIDE SCHWARTZ PRECURSOR BUILD-CERTIFIED / NO EXTRA REGULARITY ASSUMPTION ON h / EXACT REMAINING SEAM = GAUSSIAN SCHWARTZ SEED + FOURIER IDENTIFICATION / FULL MOVING-MODE SCHWARTZMAP STILL OPEN**

## 0. Objective

After RPB-101 build-certified the Gaussian-admissibility cutoff/growth layer,
the first open burden was to realize the actual moving filtered mode

~~~text
movingGaussianFilteredMode Ck R carrier
~~~

as a genuine `SchwartzMap ℝ ℂ`.

The F-1 carrier representative `carrier.h` is only an L2 representative with
compact support.  RPB-102 therefore first determines whether additional
smoothness of `h` is needed.

## 1. Compact support supplies all polynomial moments

The new module

~~~text
WeilDefect/Morphology/NeutralGaussianSchwartz.lean
~~~

proves

~~~lean
neutralPhysicalRepresentative_polynomialNorm_integrable
neutralPhysicalRepresentative_polynomialSmul_integrable
~~~

For every natural `n`,

~~~math
x \mapsto |x|^n |h(x)|
~~~

is integrable.

The proof uses only:

- the already-certified compact support `[-c,c]`;
- the already-certified L1 integrability of `h`;
- continuity of the polynomial weight.

No differentiability of `h` is assumed or derived.

## 2. Fourier smoothness follows from compact support

Pinned mathlib's Fourier derivative API then gives

~~~lean
neutralPhysicalRepresentative_fourier_contDiff
~~~

with

~~~math
\widehat h \in C^\infty(\mathbb R).
~~~

The important point is structural: the physical representative may remain
merely L2/L1, while compact support gives all moments required to
differentiate its Fourier transform arbitrarily many times.

## 3. Fourier transform is a temperate multiplier

RPB-102 further proves

~~~lean
neutralPhysicalRepresentative_fourier_hasTemperateGrowth
~~~

Every derivative of `𝓕 carrier.h` is uniformly bounded by the L1 norm of the
corresponding polynomially weighted physical representative.  Thus degree
zero already suffices in the temperate-growth definition.

Consequently the carrier side can multiply a Schwartz frequency seed through
the existing `SchwartzMap.bilinLeftCLM` / temperate-growth machinery.

There is therefore no missing regularity assumption on the F-1 carrier.

## 4. Compiler record

The initial validation passes exposed only API/elaboration issues:

1. `IntegrableOn` norm needed an explicitly typed intermediate before
   `.mul_continuousOn`;
2. the smoothness exponent had to use mathlib's `ContDiff` `∞` notation,
   not analytic `ω` / absolute top.

The carrier moment/smoothness layer then passed:

~~~text
run: 36794685260
job: 110155298721
head: 2c9b74e74590d1766f681ac2155bdc418f9845d0
~~~

The temperate-growth extension passed:

~~~text
run: 36795139285
job: 110156751629
head: eedbd92800e750711c02e7a5c30b97f50f75d85c
blob: 4bb1fec7270d25fc8a9b899b8d3f204e12b342b1
~~~

Both successful runs passed the exact module build and the repository-wide
unfinished-proof/project-axiom rejection gate.

## 5. Exact remaining seam

Pinned mathlib supplies:

- Schwartz-space Fourier and inverse Fourier continuous maps;
- Schwartz multiplication by a temperate-growth function;
- argument translation on Schwartz space;
- exact Gaussian Fourier formulas.

It does **not** currently provide a bundled theorem declaring the required
moving Gaussian function itself to be a `SchwartzMap`.

Thus the remaining construction is local and Gaussian-only:

~~~text
A. build the positive-R Gaussian seed as SchwartzMap ℝ ℂ;
B. obtain the translated/modulated/scaled moving Gaussian seed with the
   project's exact Fourier convention;
C. multiply that seed by the certified temperate function 𝓕 h;
D. inverse Fourier transform;
E. identify the resulting SchwartzMap pointwise with
   movingGaussianFilteredMode Ck R carrier.
~~~

No new source theorem or imported premise is indicated by this seam.

## 6. RPB-102 determination

~~~math
\boxed{
\textbf{RPB-102 — COMPACT SUPPORT ALONE DISCHARGES THE ENTIRE CARRIER-SIDE REGULARITY BURDEN: }\widehat h\textbf{ IS }C^\infty\textbf{ AND TEMPERATE.  THE MOVING-MODE SCHWARTZ OBLIGATION IS NOW PURELY THE EXPLICIT GAUSSIAN SEED/FOURIER-IDENTIFICATION LAYER.}
}
~~~

## Next cursor

~~~text
RPB-103 / WD-T40 F-4 GAUSSIAN SCHWARTZ SEED + MOVING-MODE FOURIER IDENTIFICATION
~~~

Do not add smoothness assumptions to `carrier.h`.

Do not begin cutoff convergence or logarithmic coercivity until the actual
moving filtered mode is bundled as `SchwartzMap ℝ ℂ`.
