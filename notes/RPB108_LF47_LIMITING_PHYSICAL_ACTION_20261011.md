# RPB108 — LF47: limiting physical action

## Submitted theorem

Add neutralLogMetricPoissonTrialAction_tendsto_endpointCandidate: the trial value plus its Laplace-weighted Poisson difference action over [1/(n+1), n+1] converges to the endpoint candidate at cap-interior points. The trial is measurable, cap-bounded, and satisfies the pointwise Lipschitz cancellation bound at the evaluation point. The action uses the actual trial zero extension.

The proof identifies each finite time-mixture action with its truncated spatial jump integral using TruncatedJump, then applies LF46 spatial dominated convergence and TrialJump's endpoint-candidate identity. The limit is derived rather than supplied as a premise. No definitions are added.

## Validation boundary

LF45 commit 7658fd0cba2ec931b5b97acb53b7c5164434c99a passed run 38155803631, job 114518683548: targeted certificate transport, complete root library, and unfinished-declaration rejection all succeeded. This validates the cumulative analytic chain through truncated bounds, concrete density exhaustion, and cancelled pointwise convergence. LF46 run 38156067404 was still building during LF47 preparation. LF46 spatial integral convergence and this limiting-action theorem await cumulative CI; no local Lean executable is available.

## Remaining

Physical weak attachment, L2 convergence, and spectral source identification remain open. This theorem concerns pointwise evaluation of the cutoff time action under explicit trial regularity hypotheses. It makes no aperture positivity, F4 closure, or RH claim.
