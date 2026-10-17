# RPB108 LF61 — finite time-kernel Fourier exchange

Adds `NeutralLogMetricTimeKernel.lean`, registered in targeted CI and the root library.

The module proves joint integrability of the physical Poisson kernel times the logarithmic Laplace weight on a finite positive-time interval and the whole spatial line. Unit Poisson mass and the finite-time weight bound supply the norm budget. It then obtains whole-line integrability of the time-mixture kernel and commutes its Fourier transform with the time integral by Fubini, proving the exact coefficient integral of `exp(-t*|ξ|)`.

The Fourier-character multiplication is jointly integrable because its norm is unchanged. No Fourier/time exchange is assumed. No new global definitions or spectral source premises.

Validation at submission: LF57 commit f6fb2d2090614d7e4f3a9a15902c65366044d96c is the latest complete-root success. LF58 and LF59 failed on the same convolution Fourier rewrite; LF60 repairs the application by explicitly instantiating the frequency. LF60 run 38176750873 has started and awaits its checks. LF61 awaits cumulative remote Lean CI; no local Lean executable is available.

This closes the finite-time Fourier exchange at the mixture-kernel layer when validated. The next action-level step is to identify the actual integrated convolution with convolution by this kernel, then combine the cancelled-action coefficient and the LF60 limit. Spectral L2/domain attachment and compressed/full-source identification remain open.

No aperture positivity, F4 closure or RH claim.
