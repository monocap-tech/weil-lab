# RPB108 — LF43: concrete time exhaustion

## Submitted coverage

Extend NeutralLogMetricTruncatedLimit with monotonicity and exact union proofs for the intervals [1/(n+1), n+1], n a natural number. The lower endpoint decreases, the upper endpoint increases, every endpoint is positive, and choosing n larger than max(t,1/t) puts every positive t into an interval. Instantiate LF40's general convergence theorem to obtain density convergence for this concrete sequence at every nonzero signed spatial displacement, with no remaining exhaustion premises.

No new definitions are introduced; all expressions are explicit and theorem names are descriptive. The existing root import and targeted CI entry cover the extended module.

## Validation boundary

LF42 commit dad07dd53302e861ab6a82d7bb11170baf86e06a, run 38154766498, was still running at preparation. LF43 is submitted for CI; no local Lean executable is available. LF28 remains the latest full-root success. TrialJump has module-level compilation evidence, while PoissonAction and subsequent modules await cumulative checking. No new completion is inferred from a running build.

## Next obligation

Use concrete density convergence to obtain cancelled trial-jump pointwise convergence, handling the diagonal by exact cancellation. Then use the integrable full trial-jump majorant to pass the spatial integral to the limit. Physical weak attachment, L2 convergence and spectral source identification remain open. No aperture positivity, F4 closure or RH claim.
