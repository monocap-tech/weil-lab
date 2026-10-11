# RPB108 LF55 — actual time-action pairing integrals

Adds `neutralLogMetricPoissonTrialAction_integral_inner_tendsto` in `NeutralLogMetricTruncatedLimit.lean`.

For a measurable, cap-bounded, uniformly Lipschitz trial and every physical L2 test vector, the whole-line integral pairing of the cap-supported Poisson cutoff action converges to the pairing integral of the endpoint zero extension. The cutoffs are [1/(n+1), n+1]. The inner product convention is source first, test second.

The proof identifies the time action with the spatial cutoff action on the closed cap, including the endpoints, and both zero extensions vanish outside it. It rewrites L2 inner products using `L2.inner_def` and the existing almost-everywhere representative identities, then applies LF54 pairing convergence. No new global definition, convergence assumption, or spectral premise is introduced.

Validation at submission: LF54 run 38169696291 passed the targeted transport check; its complete-root build remained in progress. LF50 remains the latest confirmed full-root success. LF55 requires cumulative remote Lean CI; no local Lean executable is available.

Spectral source identification remains open. This does not establish aperture positivity, F4 closure, or RH.
