# RPB108 LF35 — Explicit exterior product types

## Change

Give each complex exterior kernel product an explicit `IntegrableOn` type
before applying `integrable_indicator`. Both halves are changed in both the
full-line convergence and integral-splitting proofs. The annotation preserves
the restricted measure and the complex function explicitly; it changes no
hypothesis or conclusion.

## Validation evidence

LF33 run 38109551907 job 114382086270 passed parsing after the LF33 repair,
but TrialJump failed because indicator method lookup saw the exterior
product's inferred integrability as an `And` rather than `IntegrableOn`.
The run reported `And.integrable_indicator` at both left product calls.
The right calls used the same construction and are repaired as well.
PoissonAction, PoissonMixture, TruncatedJump and TruncatedBounds remain
downstream and unchecked. LF35 requires fresh cumulative checking.

LF28 remains the latest full-root success (run 38107491130), including the
unfinished-declaration check. No unfinished proof or project axiom is added.

## Next cursor

Resolve subsequent diagnostics, then prove truncated time-kernel convergence
and remove the cutoff using LF34's actual spatial majorant. Physical weak
attachment, L2 convergence and spectral source identification remain open.
No new aperture positivity, F4 or RH claim.
