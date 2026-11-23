# F08-013 — actual shrinking physical mollifier Fourier convergence

**Candidate — no theorem credit before genuine Lean 4.34 + independent F08-014 custody.** This imports the accepted original-source F08-011 generated Lean physical mollifier module **byte-exactly** from `verification/f08/f08_011/F08OriginalNormalizedMollifier.lean` Git blob `b1f53459762df682f6d1d358aae9c82b5396c5a7`. Its proof source is staged under `WeilDefect/Generated/F08` alongside the new purely additive module; both are directly compiled atop frozen original source IV023 commit `614ba879f7389fdb620c474adaee273b00eac71c` and pinned v4.34.0.

Four candidates: exact source Fourier phase error `|exp(-2πixξ)-1|≤2π|ξ|ε` when `|x|≤ε`; integrand error for *actual* complex-valued normalized physical `ρ_φ` bounded by its radius; quantitative `‖𝓕ρ_φ(ξ)-1‖ ≤ 2π|ξ|φ.rOut`; and true pointwise convergence `𝓕ρ_{φ_n}(ξ)→1` for every real frequency when the actual positive bump radii shrink to zero.

This directly supplies the **pointwise multiplier hypothesis** of previously kernel-passed F08-005 for an actual Fourier symbol, together with F08-011 contraction and F08-009 physical support. No claim of existence of a shrink-to-zero sequence (would be a separate specified family), ordinary Fourier equivalence to native `RealComplexL2` class for convolutions, support-preserving physical smoothing, inward dilation strong continuity, complete smooth supported logarithmic form core, all-Schwartz original signed Weil↔native mixed form, F42 or RH.

Acceptance requires source-exact direct Lean `.olean`, **4/4 precise standard-only named `#print axioms`**, followed by independent producer ZIP/source/CRC/hash/negative tests.
