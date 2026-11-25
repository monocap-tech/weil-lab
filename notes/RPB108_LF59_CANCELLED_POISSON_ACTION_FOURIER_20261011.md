# RPB108 LF59 — cancelled Poisson action Fourier transport

Extends `NeutralLogMetricPoissonConvolution.lean` with integrability and exact Fourier transport of identity minus the whole-line Poisson convolution.

For an integrable trial and positive time, the cancelled action is integrable and has Fourier multiplier `1 - exp(-t*|ξ|)`. The proof establishes integrability of the convolution, distributes the Fourier character over subtraction, and uses integrability of both Fourier integrands to justify subtraction of integrals. It then applies LF58 convolution transport. Two specializations give the corresponding integrability and transform identities for cap-bounded measurable trials through their actual zero extensions.

No new global definitions, Fourier identity hypotheses, or global assumptions on the original cap-bounded trial are introduced. This is a whole-line action and retains the exterior component.

Validation at submission: LF57 commit f6fb2d2090614d7e4f3a9a15902c65366044d96c passed run 38174810652, including targeted transport, complete root library, and unfinished-declaration rejection. LF58 run 38175545325 was fetching its Mathlib cache. LF57 is the latest confirmed full-root checkpoint. LF59 awaits cumulative remote Lean CI; no local Lean executable is available.

Next is Laplace multiplier passage, together with precise compressed/full-source attachment and domain conditions. No aperture positivity, F4 closure or RH claim.
