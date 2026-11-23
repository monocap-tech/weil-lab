# F08-007 — original physical window convolution/Fourier identity

**Mathematical scope:** actual `neutralWindowRepresentative a f` for arbitrary original physical complex `RealComplexL2` data; arbitrary integrable complex mollifier `rho`, no guessed smoothness; ordinary Fourier and original positive-exponent window sample with exact `-2πξ` normalization.

Fixed source: original research commit `614ba879f7389fdb620c474adaee273b00eac71c`; original `ActualZetaCorrelationFourierAgreement.lean` SHA `60453bd214c43feedb0fa64d74a15bd452e48998`; source window transform `ActualZetaCorrelationTransform.lean` SHA `d5aa1095b2fe64933ad8db64732d232631d3d3b7`; pinned Mathlib v4.34.0 `Real.fourier_mul_convolution_eq` (Mathlib `Analysis/Fourier/Convolution.lean` blob `e793dab8cb6cf15f5d6a0e76d4928138e3aa5d0e`). The source's own `neutralWindowRepresentative_twist_integrable`, `neutralWindowRepresentative_fourier`, and `neutralRawTransform_fourier` are used directly.

**Three real Lean targets:** actual compact-window physical representative is integrable; its Fourier convolution with integrable `rho` factors pointwise as `neutralWindowEvaluation a (-2πξ) f * 𝓕 rho ξ`; the same equality is expressed in the original positive-exponent `neutralRawTransform` convention.

**Nonclaim:** these lemmas do not create a positive smooth compact unit-mass `rho`, establish `|𝓕rho|≤1` or `𝓕rho→1`, identify L² Fourier classes, prove physical support of the resulting convolution, or complete fixed-radius dense smooth core, F08 original `literatureRHS`↔native, F41/F42 or RH. Requires genuine Lean v4.34.0 three-name strict axiom audit and separate independent full artifact custody before acceptance.
