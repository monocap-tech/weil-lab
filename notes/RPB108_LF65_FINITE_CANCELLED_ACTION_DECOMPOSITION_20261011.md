# RPB108 LF65 — finite cancelled-action decomposition and integrability

Extends `NeutralLogMetricTimeKernel.lean` with integrability of the complex Laplace weight on finite positive-time intervals, the exact finite cancelled-action decomposition, whole-line integrability of that action for bounded measurable integrable trials, and its cap-bounded zero-extension specialization.

The decomposition writes the actual action as `(1 + integral(weight))*v - integrated_convolution`. Both time integrals used in subtraction have proved integrability: the scalar weight uses the finite bound; the convolution uses joint integrability. Whole-line integrability then follows from the integrable trial and the LF64 integrated convolution result.

No new global definitions or integrability/exchange assumptions; no global conditions are imposed on the original cap-bounded trial beyond the existing finite-cap hypotheses in the specialization.

Validation at submission: LF63 run 38181384412 was still running targeted checks, and LF64 run 38181643395 was queued. LF57 commit f6fb2d2090614d7e4f3a9a15902c65366044d96c remains the latest confirmed full-root success. LF65 awaits cumulative remote Lean CI; no local Lean executable is available.

Next: Fourier subtraction for the actual finite action, coefficient cancellation, and passage to the existing logarithmic coefficient limit. Spectral L2/domain and compressed/full-source attachment remain open. No aperture positivity, F4 closure or RH claim.
