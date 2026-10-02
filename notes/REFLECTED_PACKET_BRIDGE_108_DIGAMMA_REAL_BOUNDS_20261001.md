# RPB-108 — independent actual real-axis digamma bounds

Date: 2026-10-01 (America/Los_Angeles).
Recovered research head: `b2be21a14300825e897a5242665192480d85887a`.

## Independent special-function estimate

The actual positive-real Gamma function is positive and log-convex.
Complex Gamma differentiation restricted to the real axis identifies the
derivative of log Gamma with the real part of the actual complex digamma.
The Gamma recurrence makes each unit secant slope exactly log x.
Convexity places the derivative between its predecessor and successor
secants. Hence

    Re ψ(x) ≤ log x                       (x>0),
    log(x-1) ≤ Re ψ(x) ≤ log x            (x>1).

These estimates are derived from actual Gamma properties, not retained
source comparison hypotheses, a Gauss representation premise, or the
previous source-attachment defect equivalence.

## Exact source normalization at zero frequency

For every natural N≥1, the actual shifted symbol at ξ=0 satisfies

    log(N-3/4)-log π ≤ Re shiftedSymbol_N(0) ≤ log(N+1/4)-log π.

The coordinate and constants match the existing source symbol exactly.
This controls the scalar contact value that must be separated from the
frequency-dependent remainder in an eventual support-separated tail
argument. It is not itself a tail-vanishing statement or a bound on
nonzero frequencies.

## Remaining obligations

Remove the scalar action lawfully on support-separated tests and obtain
independent bounds for the centered nonzero-frequency digamma remainder.
Prove the actual shifted-tail pairing vanishes. Exterior attachment, whole
residual/source identity, central cancellation, boundary reconstruction
and actual source-domain/quadratic/polarization/normalized estimate
witnesses remain open.

Threshold bookkeeping is closed; logarithmic coercivity has not started.
Canonical Weil, main and WD-T40 mathematical standing are unchanged.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,970 build jobs passed. All five audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `1d21396b8414c7524be3fa72cc80b7024136b455`,
run `36972763212`, job `110730043467`, source blob
`82d0918374ac39fb1e1799a5ebf67e27e46ab87f`.

Validation-only workflow/cache changes
are excluded from research promotion; prior checkpoint notes are immutable.
