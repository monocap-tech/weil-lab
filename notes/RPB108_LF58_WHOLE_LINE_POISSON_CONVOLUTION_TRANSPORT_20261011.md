# RPB108 LF58 — whole-line Poisson convolution transport

Adds `NeutralLogMetricPoissonConvolution.lean`, registered in targeted CI and the root library.

The four new theorems prove:

- Cap-bounded measurable trials have integrable zero extensions.
- The whole-line convolution of an integrable trial with the physical Poisson kernel is integrable.
- Its Fourier transform is the trial transform multiplied by `exp(-t*|ξ|)` at each positive time.
- The same identity specializes to actual zero-extended trials using only finite-cap boundedness and measurability.

The convolution is the explicit integral used by the existing time action, `integral_y v(y)*P_t(x-y)`. Its identity with Mathlib's multiplication convolution is definitional. Fourier transport uses the proved forward kernel pair and Mathlib's integrable convolution theorem. No new definitions, Fourier attachment assumptions, or global bounds on the original trial are introduced.

Validation at submission: LF57 run 38174810652 passed targeted transport, with the complete root build still running. LF56 commit 0e7918c7606028085ee9925a100cdc4fa1f8ae1b remains the latest confirmed full-root checkpoint. LF58 awaits cumulative remote Lean CI; no local Lean executable is available.

This is whole-line transport, retaining the exterior convolution. It does not identify the cap-supported endpoint zero extension with the full spectral source. Remaining steps include cancelled-action Fourier transport, Laplace multiplier passage, and the precise compressed/full-source attachment with its domain conditions.

No aperture positivity, F4 closure or RH claim.
