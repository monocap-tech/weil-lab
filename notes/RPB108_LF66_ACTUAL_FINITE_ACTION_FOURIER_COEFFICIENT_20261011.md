# RPB108 LF66 — actual finite-action Fourier coefficient

Extends `NeutralLogMetricTimeKernel.lean` with the Fourier identity of the actual full-line finite cancelled action and its cap-bounded zero-extension specialization.

The multiplier is the finite expression `1 + integral(weight) - integral(weight*exp(-t*|ξ|))`. The proof uses the exact LF65 action decomposition, integrability of the scalar trial term and integrated convolution, subtraction of genuinely integrable Fourier integrands, scalar Fourier transport, and the LF64 integrated convolution identity. It composes equalities explicitly. No desired Fourier identity or exchange is assumed; no new global definitions.

Validation at submission: LF63 commit a1310edf16d67bcfb23169db82b03c1a4cf13fa3 passed run 38181384412 including targeted transport, complete root library and unfinished-declaration rejection. LF65 run 38181762113 passed targeted transport and was still building the root. LF63 is the latest confirmed full-root checkpoint; LF65's targeted check validates the cumulative TimeKernel module through the finite-action decomposition and integrability. LF66 awaits cumulative remote Lean CI; no local Lean executable is available.

Next: justify cancellation of the two finite Laplace coefficient integrals and transfer the established coefficient limit to the Fourier transforms of the actual cutoff actions. This will be pointwise spectral convergence; spectral L2/domain and compressed/full-source attachment remain separate obligations. No aperture positivity, F4 closure or RH claim.
