# RPB108 — LF49: exterior type repair and L2 budget

## Build evidence and repair

LF48 commit 77862fe27eb2c457188428f3beb62afae1ec21d0 failed run 38160517771, job 114532264412, in TrialJump at line 135. The inferred exterior const_mul witnesses were exposed as conjunctions, so dot notation searched for And.integrable_indicator. Give both exterior witnesses explicit IntegrableOn types before applying integrable_indicator, following the already checked earlier exterior-product proof. The build stopped before checking the remaining LF48 theorems. The absolute-budget argument remains submitted; this repair does not yet certify it.

## Added theorem

The real function M + 2 B L + M E_B(x) belongs to MemLp 2 on the cap interior. Its constant part is bounded on the finite-volume cap and its exterior part uses the checked L2 membership of both endpoint tails. No new definitions are introduced. Combined with the LF48 bound, this provides the proposed common physical L2 majorant; it does not itself prove L2 convergence or test-pairing convergence.

## Validation boundary

LF47 commit ba34eab71ac16212256d7311868d20be303c4e26 remains the latest full-root success, with spatial dominated convergence and limiting time-action identity checked. LF49 repairs and the L2 budget theorem await cumulative CI. No local Lean executable is available.

## Remaining

Validate the absolute and truncated-action budgets, then derive cap convergence and physical test-pairing convergence. Spectral source identification remains open. No aperture positivity, F4 closure, or RH claim.
