# F08-030 — genuine native same-volume frequency dilation (first unsimplified gate)

**Source-only until genuine frozen-source Lean compiler and independent custody PASS.**

F08-027 provides a complex-linear *actual* L² isometric pullback from the pushed-forward measure to original Lebesgue. F08-029 proposes the actual original native `RealComplexL2` vector in that scaled measure and its exact source-eLpNorm. This module performs the mathematically correct composition by inserting the `Complex.ofReal (Real.sqrt (abs λ))` scalar before the native pullback to get `Uλ : RealComplexL2 → RealComplexL2` for λ ≠ 0.

Three independent Lean theorem targets:

- `f08_030_nativeFrequencyDilation_ae`: the same-Lebesgue-volume L² equivalence class genuinely represents `sqrt(|λ|) k(λξ)` a.e. (uses `Lp.coeFn_smul`, genuine source-to-pushforward a.e. and `QuasiMeasurePreserving.ae_eq_comp`).
- `f08_030_nativeFrequencyDilation_norm`: its norm equals `sqrt(|λ|)` times the actual pushed-forward native L² norm (no false direct same-measure composition norm).
- `f08_030_nativeFrequencyDilation_norm_exact`: source-inherited exact ENNReal-Jacobian formula before scalar cancellation.

**Still unproved:** `‖Uλ k‖=‖k‖` and complex linearity as an operator, strong L² continuity at 1, original paper Fourier physical scaling, logarithmic form-carrier identity and fixed-support smooth form core, original signed Weil mixed identity, F42 and RH. The first two slices F08-027 and F08-029 are dependencies; F08-029 remains nonpromoting until independent archive evidence.

Original frozen IV023 source `614ba879f7389fdb620c474adaee273b00eac71c`; original canonical source `WeilDefect/Morphology/NeutralCanonicalFormDomain.lean` blob `2bf19165fce3a0cfa6e4d782d68caab268aaf82b`. Parent #932; master #898.
