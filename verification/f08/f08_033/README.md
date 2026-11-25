# F08-033 — original native same-volume L² dilation isometry

**This is an UNCOMPILED source candidate until original frozen IV023 Lean v4.34.0 and independent whole-archive custody both PASS.** No assumption of the statement in the source.

Actual F08-030 original native same-volume operator `f08_030_nativeFrequencyDilation λ hλ k : RealComplexL2` represents `sqrt(|λ|) k(λ ξ)` a.e., but previously only has the unsimplified norm. F08-033 attempts to complete the necessary real Jacobian cancellation:

`‖f08_030_nativeFrequencyDilation λ hλ k‖ = ‖k‖` for `λ ≠ 0`.

Three source-native Lean goals: one-dimensional Haar Jacobian factor, exact positive square-root normalization cancellation, and norm preservation of **actual original** complex L² dilation (using F08-029 exact ENNReal formula and F08-030 native same-volume operator). No `sorry`, `admit` or `unsafe` proof.

**This is not yet a continuous complex-linear isometry in Lean.** The next target is a `LinearIsometry` with exact a.e. representative and strong L² continuity at λ=1, and then the original physical Fourier and weighted form-carrier transfer. Support-preserving smooth `C_c^∞((-a,a))` density, arbitrary smooth original signed Weil pairing, global positivity and RH remain OPEN.

Frozen IV023 source commit `614ba879f7389fdb620c474adaee273b00eac71c` and canonical source blob `2bf19165fce3a0cfa6e4d782d68caab268aaf82b`. Predecessor exact original source blobs F08-027 `eecfe2a849fa79aa13810ede85e9ba625eba7777`, F08-029 `4da65f9b9df7cae6ea30a4a7f25d3e6c1606c294`, F08-030 `5c260b69f464f5793e095f9b5448c90f7984617f`. Parent #932; ledger #898.
