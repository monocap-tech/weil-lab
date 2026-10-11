# RPB108 — LF45: cancelled jump pointwise limit

## Submitted coverage

Extend TruncatedLimit with generic and concrete pointwise convergence of the cancelled trial jump at every spatial y, for x in the cap. Away from x=y, use off-diagonal real density convergence, continuity of the real-to-complex inclusion, and multiplication by the fixed trial difference. At x=y, the trial zero extension agrees with the trial because x belongs to the cap, so both products are exactly zero. No convergence of the density at zero radius is asserted or needed. No trial measurability or Lipschitz hypothesis is required for this pointwise step.

No new definitions are introduced. Existing root imports and targeted CI cover the extension.

## Validation boundary

LF44 commit c9b04beb1774c142199040df4bdaf9167a490379, run 38155437430, was pending at preparation. LF45 awaits CI. LF42 run 38154766498 job 114515356176 compiled TrialJump, PoissonAction and PoissonMixture, then failed TruncatedJump. LF44 repairs that blocker; all truncated/limit modules remain unverified until cumulative checking succeeds. LF28 remains the latest full-root success. No local Lean executable is available.

## Next obligation

Use full trial-jump integrability and cutoff-independent norm domination to prove convergence of the spatial integrals. Then identify the limit of the physical time-mixture action with the endpoint candidate. Physical weak attachment, L2 convergence and spectral source identification remain open. No aperture positivity, F4 closure or RH claim.
