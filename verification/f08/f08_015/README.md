# F08-015 — instantiate original logarithmic weighted Fourier DCT with genuine complex physical mollifiers

**Source-bound candidate only** until actual pinned Lean `.olean`, precise 6/6 named standard-only axiom reports, and independent F08-016 archive custody PASS.

## Source inputs, not assumptions invented here

Original frozen IV023 research commit `614ba879f7389fdb620c474adaee273b00eac71c`. Genuine mathematical physical window Fourier source `ActualZetaCorrelationFourierAgreement.lean` blob `60453bd214c43feedb0fa64d74a15bd452e48998`, original log-weight domain `NeutralCanonicalFormDomain.lean` blob `2bf19165fce3a0cfa6e4d782d68caab268aaf82b`.

Actual independently accepted additive Lean prerequisites staged **exactly** alongside new source:

- F08-005 `verification/f08/f08_005/F08WeightedMollifierMultiplier.lean`, blob `2a8199ff817f59d1437fa173518a588cbbd467b9`. Supplies the original source weight `log(e+|ξ|)`, exact `RealComplexL2`, and genuinely compiled dominated-convergence lemma for measurable complex contractions approaching 1.
- F08-011 `verification/f08/f08_011/F08OriginalNormalizedMollifier.lean`, blob `b1f53459762df682f6d1d358aae9c82b5396c5a7`. Supplies `φ.normed volume` complex positive normalized compact smooth physical mollifier, its integrability and contraction `‖𝓕ρ_φ(ξ)‖≤1`.
- F08-013 `verification/f08/f08_013/F08OriginalMollifierFourierLimit.lean`, blob `7b91eda87ce5a0d7691fdc643865e72fb153287c`. Supplies exact `-2πxξ` phase bound and genuine shrinking-radius family Fourier pointwise `𝓕ρ_{φ_n}(ξ)→1` given `rOut(φ_n)→0`.

## Six new target declarations

1. Actual multiplier `m_φ(ξ)=(𝓕(f08_011_complexMollifier φ)) ξ` is continuous because the physical `ρ_φ` is L¹, using pinned `VectorFourier.fourierIntegral_continuous`.
2. Actual multiplier is `AEStronglyMeasurable`.
3. Actual multiplier is norm-bounded by 1.
4. Weighted squared error `w(ξ) ‖(m_φ(ξ)-1)F(ξ)‖²` is integrable for finite original source weighted Fourier energy.
5. Pointwise `m_{φ_n}(ξ)→1` for any **explicitly assumed** shrinking-radius sequence `φ_n`.
6. **Full F08-005 weighted error convergence instantiated with actual physical mollifier symbols**:
```
Tendsto (fun n => ∫ ξ : ℝ, logarithmicFourierWeight ξ *
  ‖(m_{φ_n}(ξ)-1) * F ξ‖^2 ∂volume) atTop (𝓝 0)
```
for `F : RealComplexL2` satisfying the actual weighted energy integrability premise and `φ_n.rOut→0`. This theorem does not assume arbitrary multipliers with unspecified measurability/bound/limit; those facts are discharged by the actual source-specific modules.

## Important nonclaims

Even this does NOT construct a specific radius-shrinking bump sequence; prove `F` arises as the Fourier coordinate of the physical convolution in the true `RealComplexL2` source/domain; establish `C^∞` regularity of physical window convolved with `ρ`; prove inward dilation is strongly continuous in the `log(e+|ξ|)` form norm; or complete fixed-radius `C_c^∞((-a,a))` density. No original arbitrary complex Schwartz signed `Zeta23.EF.literatureRHS`↔native operator form identity, all-support positivity, F42 or RH. Parent issue #932, master ledger #898.
