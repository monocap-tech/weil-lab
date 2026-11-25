# RPB108 — LF46: spatial cutoff removal

## Submitted theorem

Add convergence of the full-line spatial integrals of actual cancelled truncated trial jumps along [1/(n+1),n+1] to the genuine full trial-jump integral. Hypotheses are cap-interior x, nonnegative B/L/M, measurable trial, a cap norm bound M, and the pointwise Lipschitz cancellation bound L at x.

The proof invokes dominated convergence with the norm of the full trial jump as majorant. Its integrability comes from TrialJump, norm domination comes from TruncatedBounds, and pointwise convergence including the diagonal comes from LF45. Measurability of each truncated integrand is obtained from its proved integrability after applying TruncatedJump to the actual trial zero extension; cap membership identifies the extension at x with v x. No desired limit, spectral identity, or additional domain premise is assumed. No new definitions are introduced.

## Validation boundary

LF44 run 38155437430 was cancelled while pending after supersession, which is not proof rejection. LF45 commit 7658fd0cba2ec931b5b97acb53b7c5164434c99a run 38155803631 was still running at preparation. LF46 awaits CI; no local Lean executable is available. LF42 compiled TrialJump, PoissonAction and PoissonMixture but failed TruncatedJump before LF44's repairs. Truncated and convergence modules remain submitted and unverified. LF28 remains the latest full-root success.

## Remaining

Identify the limiting positive-time physical mixture with the endpoint candidate, validate all submitted modules, then address physical weak attachment, L2 convergence and spectral source identification. No aperture positivity, F4 closure or RH claim.
