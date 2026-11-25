# RPB108 LF60 — Laplace cutoff multiplier limit

Adds `NeutralLogMetricLaplaceCutoff.lean`, registered in targeted CI and the root library.

The three new theorems recover the existing `logarithmicFourierWeight` by integrating the cancelled Poisson coefficient over increasing finite time intervals:

- Generic increasing intervals exhausting positive time give the real multiplier limit.
- The concrete intervals [1/(n+1), n+1] give the same limit without exhaustion premises.
- The actual complex coefficient, one plus the integral of `exp(-e*t)/t * (1-exp(-t*|ξ|))`, converges to the complex cast of the logarithmic weight.

All frequencies are included, including zero. The real proof uses genuine integrability of the cancelled Laplace integrand, monotone set exhaustion, and the existing exact Frullani evaluation. The complex statement follows from a proved integrand equality, complex-real integral compatibility, and continuity of the cast. No new global definitions or multiplier-limit assumptions.

Validation at submission: LF57 commit f6fb2d2090614d7e4f3a9a15902c65366044d96c passed run 38174810652 with targeted transport, complete root library, and unfinished-declaration rejection. LF58 run 38175545325 failed on a convolution Fourier rewrite that omitted explicit frequency instantiation (line 42). LF60 repairs it by constructing the instantiated theorem at ξ and using its equality directly. LF59 run 38176317196 is queued. LF57 remains the latest confirmed full-root checkpoint. LF60 awaits cumulative remote Lean CI; no local Lean executable is available.

This is pointwise coefficient convergence. Fourier transport of the time-integrated physical action, spectral L2 convergence/domain membership, and compressed/full-source attachment remain separate obligations. No aperture positivity, F4 closure or RH claim.
