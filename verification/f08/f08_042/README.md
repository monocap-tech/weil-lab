# F08-042 — Original compact-Schwartz support radius and global amplitude bounds

**Source-only candidate until direct original frozen IV023 Lean 4.34.0 and separate hosted source/archive custody PASS.**

The original source-side image density theorem F08-037 is now independently certified and merged. The separate original normalized Schwartz pointwise limit F08-040 has genuine Lean producer PASS; independent custody is still pending.

The next two source-exact support/size estimates proposed here are:

1. `f08_042_compactSchwartz_supportRadius`: from `g:𝓢(ℝ,ℂ)` and `HasCompactSupport (g:ℝ→ℂ)`, construct `R≥0` such that `R < |ξ|` forces `g ξ=0`. This uses actual pinned Mathlib compactness of `tsupport`, metric boundedness and `subset_tsupport`.
2. `f08_042_originalSchwartz_globalBound`: choose the original Schwartz seminorm `M=SchwartzMap.seminorm ℝ 0 0 g` to bound `‖g ξ‖≤M` uniformly. No new surrogate norm or source carrier is introduced.

Once both are original kernel-certified, use `1/2≤λ≤3/2` to get a common support interval `[-2R,2R]` for `g ξ` and `g(λξ)`. The explicit real scalar `(M*(1+√(3/2)))²` times the common-interval indicator then dominates the squared difference `‖Complex.ofReal (Real.sqrt (abs λ)) • g (λξ)-g ξ‖²`. **That pointwise bound itself and the filtered original `volume` dominated-convergence theorem are still future obligations**, not proved by F08-042.

This source uses genuine `SchwartzMap` and the canonical original research domain at pinned IV023 commit `614ba879f7389fdb620c474adaee273b00eac71c`, frozen Mathlib and Lean 4.34.0. This is **frequency-side** compact support, not original physical-space support of inverse Fourier transforms. Does not certify full L² dilation strong continuity, the logarithmically weighted physically supported Weil core, original signed `Zeta23.EF.literatureRHS` form, positivity, F42 or RH.

Research ledger #932; master ledger #898.
