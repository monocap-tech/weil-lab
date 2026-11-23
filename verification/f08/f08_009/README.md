# F08-009 — support containment for convolution of original physical Weil window

**New mathematical work: physical support propagation**, not global form positivity.

The original research defines `neutralWindowRepresentative a f = (Icc (-a) a).indicator f` for `f : RealComplexL2`. This work stages three source-specific Lean theorems: the representative's pointwise support lies in `[-a,a]`; its convolution using the genuine `ContinuousLinearMap.mul ℂ ℂ` has support inside the Minkowski sum of source window and `support rho`; if `support rho ⊆ [-ε,ε]`, the convolution is supported in `[-(a+ε),a+ε]`.

**Original frozen source:** IV023 commit `614ba879f7389fdb620c474adaee273b00eac71c`, original `ActualZetaCorrelationTransform.lean` blob `d5aa1095b2fe64933ad8db64732d232631d3d3b7`, original `ActualZetaCorrelationFourierAgreement.lean` blob `60453bd214c43feedb0fa64d74a15bd452e48998`. Relies on pinned Mathlib `MeasureTheory.support_convolution_subset` and exact pointwise physical support of the source indicator; no new source domain, no unverified cutoff boundedness.

**The support argument is valid even without assuming a smooth mollifier or ε>0** (which are needed for the later true mollification application). Theorem only asserts support for a given function `rho`. It does not produce a positive unit-mass compact smooth `rho_ε` or establish `|𝓕ρ_ε|≤1`, `𝓕ρ_ε→1`, strong norm convergence of inward dilation, physical mollification smoothness, dense source Schwartz core, arbitrary complex source-to-native full Weil mixed pairing, F42 or RH.

One scoped pinned Lean 4.34.0 compile and strict three-name standard-only axiom audit; independently archived ZIP/source/axiom custody mandatory before acceptance. The earlier F08-007 ordinary Fourier convolution product and F08-005 DCT certificates remain independent accepted prerequisites.
