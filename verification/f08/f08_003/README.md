# F08-003 — exact original log-form energy under Fourier multiplier contraction

**Purpose:** Pay the bounded-multiplier step needed for mollification in the original supported logarithmic form Hilbert space. The parent source theorem and analytic dense-core construction are [F08 #932](https://github.com/monocap-tech/weil-lab/issues/932).

This candidate works against the real `logarithmicFourierWeight ξ := log(e+|ξ|)`, `NeutralCanonicalLogFormDomain` implementation and physical complex L² Fourier coordinate, **not** a surrogate positivity form. It proposes:

1. For any complex multiplier `m` of pointwise modulus ≤1, `w ξ * ‖m ξ * F ξ‖² ≤ w ξ * ‖F ξ‖²`.
2. For a strongly measurable such `m` and `F ∈ L²` with integrable weighted energy, `w ξ * ‖m ξ * F ξ‖²` is integrable.

Source pinned to mathematical IV023 commit `614ba879f7389fdb620c474adaee273b00eac71c`, actual `NeutralCanonicalFormDomain.lean` Git blob `2bf19165fce3a0cfa6e4d782d68caab268aaf82b`, Lean 4.34.0 and Mathlib v4.34.0.

**No acceptance until hosted compiler and strict 2/2 named axiom checks.** Once verified, these two statements are limited to bounded-multiplier integrability; they **do not prove** the physical convolution/Fourier identity, mollifier approximate identity, strong dilation convergence, interior smooth core density, the full original Weil-to-native pairing, F41/F42 or RH. Follow with a separate independent ZIP/source/axiom custody check before formal acceptance.
