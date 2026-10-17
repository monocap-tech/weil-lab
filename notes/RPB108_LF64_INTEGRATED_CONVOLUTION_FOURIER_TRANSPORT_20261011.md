# RPB108 LF64 — actual integrated convolution Fourier transport

Extends `NeutralLogMetricTimeKernel.lean` with three theorems:

- Whole-line integrability of the actual finite weighted time-integrated convolution for a bounded measurable integrable trial.
- Its Fourier transform is the trial transform times the finite integral of the Laplace weight multiplied by `exp(-t*|ξ|)`.
- The actual cap-bounded zero extension satisfies this identity using only measurability and boundedness on the cap.

The proofs use the pointwise LF62 time-kernel attachment, the LF61 kernel integrability/Fourier identity, and Mathlib's convolution theorem. Equalities are explicitly composed rather than relying on nested Fourier rewrites. No Fourier/time exchange, global integrability of the original cap-bounded trial, or spectral source identity is assumed. No new global definitions.

Validation at submission: LF63 run 38181384412 was running targeted checks. LF62 compiled the convolution/cancelled-action Fourier module and the Laplace cutoff-limit module, but its complete build failed on time-kernel errors addressed in LF63. LF57 commit f6fb2d2090614d7e4f3a9a15902c65366044d96c remains the latest confirmed full-root success. LF64 awaits cumulative remote Lean CI; no local Lean executable is available.

Next: combine the integrated identity term with the integrated convolution to obtain the actual cancelled-action multiplier and apply the existing coefficient limit. Spectral L2/domain and compressed/full-source attachment remain open. No aperture positivity, F4 closure or RH claim.
