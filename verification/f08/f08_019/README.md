# F08-019 — genuine smooth physical original Weil window convolution

**Unaccepted candidate until actual pinned Lean .olean and distinct independent F08-020 source archive custody.**

We are finally proving physical regularity of the *original* sharp physical window representative `neutralWindowRepresentative a f` for arbitrary `f : RealComplexL2` under convolution with a genuine nonnegative normalized unit-mass `C∞` complex physical bump, **without falsely asserting the sharp L² cutoff is smooth.**

The genuine convolution uses `ContinuousLinearMap.mul ℂ ℂ`, exactly the same bilinear operation as original F08-007 and F08-009; Mathlib's differentiability theorem is real-bilinear, so the candidate first proves that `ContinuousLinearMap.mul ℝ ℂ` defines the same physical complex convolution function. Imports pinned `Mathlib.Analysis.Calculus.ContDiff.Convolution` and the original source module. It then proves:

1. Original complex/real bilinear convolution equal pointwise.
2. Original physical window convolved with actual F08-011 complex `ρ_φ` is L¹.
3. For **any** source `f : RealComplexL2`, original physical window convolved with real `C∞` physical mollifier becomes genuine real `C∞` complex-valued smooth function. Uses `HasCompactSupport.contDiff_convolution_right`, with actual original `LocallyIntegrable` source window.
4. True support radius `[-a-φ.rOut,a+φ.rOut]` using F08-009 original support.
5. Actual compact support, not assumed.
6. Genuine `MemLp · 2 volume` for smoothed compact original physical representative.
7. Exact ordinary negative-`2π` Fourier product with original `neutralWindowEvaluation a(-2πξ) f` and certified physical multiplier.
8. Actual selected F08-017 bump sequence has eventual physical support in `[-a-ε,a+ε]` for any positive ε.

Frozen original source IV023 commit `614ba879f7389fdb620c474adaee273b00eac71c`, original Fourier source blob `60453bd214c43feedb0fa64d74a15bd452e48998`, original physical source `d5aa1095b2fe64933ad8db64732d232631d3d3b7`, original log carrier source blob `2bf19165fce3a0cfa6e4d782d68caab268aaf82b`, pinned Lean v4.34.0. Exact source-bound additive dependencies are F08-005,007,009,011,013,015,017, pinned by the compiler workflow and independently verified again in F08-020.

**Not proven here:** fixed-radius supported core density (support still grows by `φ.rOut` unless we make an inward dilation), L² Fourier-to-native a.e. coordinate identity for newly produced physical smooth L² source, inward-dilation strong continuity in log energy, full source `C_c∞((-a,a))` density, signed original `Zeta23.EF.literatureRHS`↔native mixed form identity, F42, global positivity, RH. Parent issue #932 and ledger #898.
