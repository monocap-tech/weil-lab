# RPB108 — LF51: cap L2 convergence

## Submitted theorem

Add neutralLogMetricTruncatedTrialAction_tendsto_L2: along the concrete [1/(n+1), n+1] time exhaustion, the cap L2 seminorm of the difference between the actual truncated spatial action and the endpoint candidate tends to zero. Trials are measurable, uniformly bounded on the cap, and satisfy a uniform cap Lipschitz modulus. No convergence or attachment identity is supplied as a hypothesis.

Use the checked endpoint-aware common L2 budget, cast to a complex-valued majorant, to derive uniform integrability of the cutoff actions. The cutoff actions' measurability comes from LF50. Their almost-everywhere pointwise limit follows from LF46 spatial dominated convergence and the endpoint trial-jump identity. The candidate's L2 membership comes from CapL2. Apply Mathlib's tendsto_Lp_finite_of_tendsto_ae on the finite-volume cap. This is convergence of the eLpNorm of the difference with exponent 2, not merely boundedness or pointwise convergence. No new definitions are introduced.

## Validation boundary

LF49 run 38162141548, job 114537100031, and LF50 commit 7f05854f88006919526056c2597a625a6adbece1 run 38162268721, job 114540910706, both passed targeted certificate transport, complete root library, and unfinished-declaration rejection. The repaired absolute budget, common L2 envelope, cutoff action measurability, and L2 membership are now checked. LF50 is the latest full-root success. LF51 awaits cumulative CI; no local Lean executable is available. The uniform-integrability API was read from the pinned Mathlib revision 5ed2965256430c3649e86755f9576b54eca72435.

## Remaining

Validate cap L2 convergence, transfer it to physical L2 representatives and the time-action expression, then derive physical test-pairing convergence and spectral source identification. No aperture positivity, F4 closure, or RH claim.
