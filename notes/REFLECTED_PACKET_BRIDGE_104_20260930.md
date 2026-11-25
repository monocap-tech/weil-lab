# RPB-104 — WD-T40 F-4 compact Schwartz cutoff construction and topology convergence

**Date:** 2026-09-30  
**Branch:** research/reflected-packet-bridge  
**Status:** **COMPLETE / BUILD-CERTIFIED / COMPACT CUTOFF SEQUENCE CONSTRUCTED / FULL SCHWARTZ-TOPOLOGY CONVERGENCE CERTIFIED / PAIRING CONVERGENCE NOT STARTED / COERCIVITY NOT STARTED**

## 0. Objective

RPB-103 build-certified the actual moving filtered mode as a genuine
`SchwartzMap ℝ ℂ`, pointwise equal to the existing F-3 physical
convolution.

RPB-104 discharges burden B from RPB-100:

~~~text
construct compactly supported Schwartz cutoffs converging to the actual
moving filtered mode in the full Schwartz topology.
~~~

## 1. Fixed expanding smooth cutoff

The new module

~~~text
WeilDefect/Morphology/NeutralGaussianCutoff.lean
~~~

uses a fixed `ContDiffBump` centered at zero with inner radius 1 and outer
radius 2.

For `R > 0`, define the rescaled cutoff

~~~math
\chi_R(x)=\chi(R^{-1}x).
~~~

The source proves:

~~~lean
neutralGaussianCutoffScalar_contDiff
neutralGaussianCutoffScalar_compact
neutralGaussianCutoffScalar_one
~~~

Thus `χ_R` is smooth, compactly supported, and equal to one on
`|x| ≤ R`.

## 2. Schwartz truncation operator

For `f : SchwartzMap ℝ ℂ`, define

~~~lean
neutralGaussianSchwartzCutoff R f
~~~

by pointwise multiplication with `χ_R`.

The cutoff is represented through `SchwartzMap.smulLeftCLM`, with the
cutoff's temperate growth supplied by compact support plus smoothness.

The source proves exact pointwise evaluation and compact support:

~~~lean
neutralGaussianSchwartzCutoff_apply
neutralGaussianSchwartzCutoff_compact
~~~

## 3. Quantitative seminorm estimate

The cutoff derivatives are uniformly bounded after rescaling.  Combining
those derivative bounds with the Leibniz rule and the fact that
`χ_R - 1` vanishes on `|x| < R` gives the explicit estimate

~~~math
p_{k,n}(\chi_R f-f)
\le
\frac{C_{k+1,n}(f)}{R}
\qquad (R\ge1).
~~~

The relevant declarations are:

~~~lean
neutralGaussianCutoffScalar_derivative_bound
neutralGaussianCutoff_sub_one_derivative_bound
neutralGaussianSchwartzCutoff_derivative_bound
neutralGaussianSchwartzCutoff_derivative_zero
neutralGaussianSchwartzCutoff_seminorm_le
~~~

The constant is independent of `R`.

## 4. Full Schwartz-topology convergence

From the seminorm estimate and `R_N=N+1 → ∞`, Lean proves

~~~lean
neutralGaussianSchwartzCutoff_tendsto
~~~

with

~~~math
\chi_{N+1}f \to f
~~~

in the full Schwartz topology.

This is not merely pointwise or Lp convergence.

## 5. Actual moving-mode cutoff sequence

The project-specific sequence is:

~~~lean
movingGaussianFilteredModeCompactCutoff
~~~

applied to the RPB-103 object

~~~lean
movingGaussianFilteredModeSchwartz Ck R hR carrier.
~~~

Lean certifies:

~~~lean
movingGaussianFilteredModeCompactCutoff_compact
movingGaussianFilteredModeCompactCutoff_tendsto
~~~

Hence every term has compact support and the sequence converges to the actual
moving filtered mode in Schwartz topology.

Burden B from RPB-100 is therefore fully discharged.

## 6. Validation

The complete source passed directly under the pinned toolchain:

~~~text
run:  36800396833
job:  110173193606
head: 8e8cf915220bf5bff355d4df006b3c18b926a780
blob: e8f5319b0b8a8b2a1c840e8630f53f2c7dce08da
~~~

The validation target was:

~~~text
lake build WeilDefect.Morphology.NeutralGaussianCutoff
~~~

The repository-wide rejection gate for `axiom`, `sorry`, and `admit`
also passed.

## 7. RPB-104 determination

~~~math
\boxed{
\textbf{RPB-104 — THE ACTUAL MOVING FILTERED MODE NOW HAS AN EXPLICIT COMPACTLY SUPPORTED SCHWARTZ APPROXIMATION SEQUENCE CONVERGING IN THE FULL SCHWARTZ TOPOLOGY.}
}
~~~

No new imported analytic premise was introduced.

## 8. Remaining F-4 pre-coercivity burdens

After RPB-104:

~~~text
A. actual moving filtered mode as SchwartzMap — CLOSED
B. compact Schwartz cutoff sequence + topology convergence — CLOSED
C. residual pairing convergence along cutoffs — OPEN
D. pole pairing convergence along cutoffs — OPEN
E. actual EXT-4 pole exponential-growth instantiation — OPEN
~~~

The logarithmic coercivity theorem remains unopened.

## Next cursor

~~~text
RPB-105 / WD-T40 F-4 RESIDUAL + POLE CUTOFF PAIRING CONVERGENCE
~~~

Use the explicit RPB-104 cutoff sequence and the already-certified whole-line
integrability of the moving-mode residual and pole pairings.

Do not begin actual pole-growth instantiation or logarithmic coercivity before
the two ordinary-integral convergence statements are certified.
