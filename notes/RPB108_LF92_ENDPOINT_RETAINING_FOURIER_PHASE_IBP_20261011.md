# RPB108 LF92 — endpoint-retaining Fourier-phase integration by parts

Derives the exact finite-interval Fourier-phase identity with c=−2πiξ:

c ∫_a^b v(x) exp(cx) dx = v(b) exp(cb) − v(a) exp(ca) − ∫_a^b v′(x) exp(cx) dx.

The phase derivative is constructed using the real-to-complex derivative and complex exponential chain rule; its interval integrability follows from continuity. The trial's derivative witness on the closed unordered interval and interval-integrable derivative remain explicit regularity hypotheses. Neither endpoint value is set to zero. The desired Fourier/source identity is not assumed.

This prepares the reciprocal decay estimate for smooth finite-interval trials with nonzero endpoint jumps after zero extension. Norm control and attachment of the interval integral to the actual ordinary Fourier transform remain next steps. General cap-Lipschitz or bounded-variation classes are not yet covered by this differentiable interface. No new global definitions.

Validation: LF89 run 38202260080 was running targeted checks; LF86 and LF91 had no job assigned at the initial check. Local structural checks and unfinished-declaration rejection pass for LF92; cumulative remote Lean validation is pending. LF84 commit 42c6a56d50d9b40e757b8214dec07ddd162aad10 remains the latest confirmed full-root code checkpoint. No local Lean executable is available.

Next: derive the reciprocal phase-integral norm bound from endpoint values and derivative L1 mass, attach it to the zero-extension Fourier integral, and consume LF91's domain criterion. No aperture positivity, F4 closure or RH claim.
