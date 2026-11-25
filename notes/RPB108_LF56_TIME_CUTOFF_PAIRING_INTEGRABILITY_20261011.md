# RPB108 LF56 — time-cutoff pairing integrability

Adds three theorems to `NeutralLogMetricTruncatedLimit.lean`:

- `neutralLogMetricPoissonTrialAction_zeroExtension_memLp_two`: the actual cap-supported Poisson time action belongs to whole-line physical L2 for every finite cutoff with positive lower endpoint.
- `neutralLogMetricPoissonTrialAction_integrable_inner`: the pointwise pairing with every physical L2 test vector is integrable for each such cutoff.
- `neutralLogMetricEndpointZeroExtension_integrable_inner`: the endpoint pairing integrand is also integrable.

The first proof transfers the existing spatial-action membership using the finite-cutoff identity on the closed cap and zero values outside it. The pairing results use Mathlib's `L2.integrable_inner` and almost-everywhere representatives. This supplies explicit integrability witnesses for the integrals occurring in LF55, beyond Lean's totalized integral notation. Source is the first inner-product argument, test the second.

No new global definitions, convergence assumptions or spectral attachment premises. Existing boundedness and Lipschitz hypotheses are retained.

Validation at submission: LF54 run 38169696291 passed targeted transport, with the root build still in progress. LF55 run 38170456841 had started dependency resolution. LF50 remains the latest confirmed complete-root success. LF56 awaits cumulative remote Lean CI; no local Lean executable is available.

Spectral identification remains open. No new aperture positivity, F4 closure or RH claim.
