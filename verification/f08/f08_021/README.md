# F08-021 — actual original physical smooth convolution → native RealComplexL2 and Fourier coordinate

**Unaccepted candidate** until real Lean v4.34.0 original-source compilation and distinct independent F08-022 ZIP/source/6-axiom custody.

This bridge uses the actual original signed-Weil physical convolution `f08_019_originalSmoothedWindow a f φ`, for any `a:ℝ`, `f:RealComplexL2`, `φ:ContDiffBump (0:ℝ)`. The F08-019 source has already proven this function is genuinely smooth, compactly supported, L¹ and `MemLp 2 volume`. **We now install it as the *native* `RealComplexL2` equivalence class via actual `MemLp.toLp`, and retain the a.e. representative equality.** Original source lemma `neutralIntegrableL2_fourier_ae` converts its L² Fourier coordinate to the ordinary L¹ integral, and the F08-019 theorem converts the latter to the exact original `-2π` Fourier product.

Six new Lean targets:
1. `f08_021_original_smoothed_window_native_ae`: actual native `MemLp.toLp` representative equals genuine original physical smooth convolution a.e.
2. `f08_021_original_smoothed_window_native_integrable`: native representative is also L¹ by true a.e. identification.
3. `f08_021_original_smoothed_window_native_ae_support`: native representative a.e. vanishes outside `[-a-φ.rOut,a+φ.rOut]` (no false pointwise smoothness of arbitrary `Lp` representative).
4. `f08_021_original_smoothed_window_native_fourier_ae`: native L² Fourier coordinate agrees a.e. with the ordinary `-2π` L¹ Fourier of actual physical convolution.
5. `f08_021_original_smoothed_window_native_fourier_product_ae`: native L² Fourier coordinate equals original source `neutralWindowEvaluation a(-2πξ) f * 𝓕ρ_φ(ξ)` a.e., without introducing an abstract multiplier.
6. `f08_021_explicit_original_smoothed_window_native_fourier_ae`: same exact a.e. source expression for F08-017's explicit constructed shrinking physical bumps.

**Immutable original IV023 research source:** commit `614ba879f7389fdb620c474adaee273b00eac71c`, Fourier Agreement original Git blob `60453bd214c43feedb0fa64d74a15bd452e48998`, original physical transform blob `d5aa1095b2fe64933ad8db64732d232631d3d3b7`, native log weight domain blob `2bf19165fce3a0cfa6e4d782d68caab268aaf82b`. Eight previously independently accepted Lean dependency source blobs, all staged directly under original `WeilDefect/Generated/F08` and source-hash-pinned: F08-005 `2a8199ff817f59d1437fa173518a588cbbd467b9`; F08-007 `606d324ca9fcfd53d059efe1b57d1b0e30349476`; F08-009 `6badab7f17605d3131ee414282683d390c6f1964`; F08-011 `b1f53459762df682f6d1d358aae9c82b5396c5a7`; F08-013 `7b91eda87ce5a0d7691fdc643865e72fb153287c`; F08-015 `f1969dede41f0d799788411420c0cb2a63c5e53a`; F08-017 `b767da47b302734c9b1de0bd0fde38b727c84b20`; F08-019 `efe3260cbd8798ad7192142c1e656f31a6729d13`.

**Not proved by this gate:** finite original weighted log energy for arbitrary source-smoothed convolution, native weighted form-norm convergence to un-smoothed original function, inward source support-preserving dilation, full fixed-support `C_c∞((-a,a))` source log-form core, all-complex signed `Zeta23.EF.literatureRHS`↔native mixed identity, global positivity, F42 or RH. These require separate later source-specific proofs. Parent issue #932, master ledger #898.
