# F08-045 — One common compact support interval for scaled Schwartz representatives

**Source-only original IV023 Lean candidate, not accepted until genuine native Lean 4.34.0 compiler SUCCESS and a separate original source/ZIP custody PASS.**

This theorem uses the original F08-042 source-native compact Schwartz radius: for a genuine `g:𝓢(ℝ,ℂ)` with `HasCompactSupport (g:ℝ→ℂ)`, there is some `R≥0` with `g ξ=0` whenever `R<|ξ|`. For every real scale `1/2≤λ≤3/2` it then shows `g ξ=g(λξ)=0` outside the **same** `[-2R,2R]`, from `|λ ξ|≥|ξ|/2`. This is strictly source-frequent Schwartz representative geometry.

Original F08-042 [producer run 45552542678](https://github.com/monocap-tech/weil-lab/actions/runs/45552542678) has native Lean PASS but its independent F08-044 custody is still pending. F08-045 is staged on top of exactly that F08-042 source; no alternative surrogate or new Mathlib upgrade. Proven F08-037 compact-Schwartz dense image, F08-038 dense-to-all transfer and F08-040 pointwise normalized representative continuity are separately accepted or in audit as stated in research ledger #932.

The next separate theorem must bound `‖Complex.ofReal(Real.sqrt(abs λ)) • g(λ ξ)-g ξ‖²` by a single scalar multiple of the indicator of `[-2R,2R]`, prove that envelope integrable in actual `volume`, and use frozen Mathlib v4.34.0 filtered dominated convergence plus exact original F08-030 a.e. `Lp` norm to establish actual source `RealComplexL2` strong convergence. F08-045 alone proves none of those analytic claims.

Physical compact support after inverse Fourier, logarithmic Weil-form core, complete signed original smooth Weil mixed pairing, F42 positivity, and RH remain unresolved.
