# RPB108 LF57 — forward Poisson Fourier pair

Adds `NeutralLogMetricPoissonFourier.lean`, with root and targeted-CI registration.

The new proofs establish integrability of the damped spectral exponential, compute its forward Fourier transform using the existing two-half-line integral evaluation, and apply Fourier inversion to obtain the forward transform of the physical Poisson density:

`Fourier(P_t)(ξ) = exp(-t * |ξ|)` for `t > 0`.

This is the exact existing density `2*t/(t^2 + 4*pi^2*x^2)` and Mathlib's 2*pi convention. It introduces no new global definitions. Both integrability premises required by Fourier inversion are proved, using exponential integrability and the density's existing Cauchy-kernel integrability.

Validation: LF55 run 38170456841 and LF56 run 38170941105 both passed targeted transport, the complete root library, and unfinished-declaration rejection. LF56 commit 0e7918c7606028085ee9925a100cdc4fa1f8ae1b is the latest confirmed full-root checkpoint. LF57 awaits cumulative remote Lean CI; no local Lean executable is available.

Next attachment obligations include convolution transport and Laplace multiplier passage. The cap-supported pairing source is a compression: the full spectral action on a zero-extended trial can have an exterior component. The forward kernel pair alone does not identify the cap-supported candidate with the full spectral source, or establish spectral operator-domain membership.

No aperture positivity, F4 closure or RH claim.
