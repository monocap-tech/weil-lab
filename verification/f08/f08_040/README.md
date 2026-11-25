# F08-040 — pointwise limit of the exact F08-030 normalized Schwartz representative

**Original native Lean candidate, not a certified declaration until actual frozen IV023 Lean 4.34.0 and independent source/archive custody PASS.**

The original F08-030 `RealComplexL2` dilation has the genuine `volume` a.e. formula `(Uλk)(ξ)=Complex.ofReal(Real.sqrt(abs λ)) • k(λ ξ)`. This candidate establishes only the corresponding **pointwise** convergence as nonzero λ→1 for an actual `g : 𝓢(ℝ,ℂ)`. It carefully does not evaluate the equivalence class `k : RealComplexL2` pointwise as if the equality were everywhere valid. It uses the true nonzero scaling subtype and actual `SchwartzMap.continuous`.

For the next true F08 compact-Schwartz `L²` continuity theorem, still needed are: a common bounded support interval and uniform integrable bound on `‖√|λ|g(λξ)-g(ξ)‖²`; the original pinned Mathlib 4.34.0 filtered dominated convergence of this square; exact original `Lp` norm-integral identification using F08-030 a.e. source representative and `SchwartzMap.coeFn_toLp`; then genuine F08-037 image density (unaccepted as of creation) and the independently accepted F08-038 conditional dense-to-all transfer.

Do not conflate *frequency-side* support of `g` with original physically supported `C_c^∞((-a,a))` under inverse Fourier, logarithmic weighted topology, the complete signed smooth Weil form, positivity or RH.
