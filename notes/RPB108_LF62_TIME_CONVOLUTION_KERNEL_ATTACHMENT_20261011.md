# RPB108 LF62 — time convolution/kernel attachment and proof repairs

Adds joint integrability of the weighted Poisson convolution at each spatial point for bounded measurable trials, and identifies the actual time-integrated convolution with convolution by the finite time-mixture kernel. Unit shifted Poisson mass and the finite-time weight bound supply the norm budget; Fubini and constant multiplication through integrals give the equality.

Repairs two LF60 errors:

- Replace the remaining Fourier-kernel rewrite with composition of the convolution equality and a congruence of the kernel equality.
- Unfold `Function.comp_def` when simplifying the cast of the real cutoff multiplier limit.

No new global definitions, exchange premises, or spectral source assumptions.

Validation: LF60 run 38176750873 failed at the remaining Fourier-kernel rewrite (PoissonConvolution line 44) and the cast-composition simplification (LaplaceCutoff line 61). LF61 run 38177383568 was still running targeted checks at submission. LF57 commit f6fb2d2090614d7e4f3a9a15902c65366044d96c remains the latest confirmed full-root success. LF62 awaits cumulative remote Lean CI; no local Lean executable is available.

Next is Fourier transport of the actual finite integrated cancelled action using this attachment and the finite kernel Fourier pair, followed by spectral L2/domain and compressed/full-source attachment. No aperture positivity, F4 closure or RH claim.
