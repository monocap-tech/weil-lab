# RPB-108 — exterior weak convergence and exact shifted-tail defect

Date: 2026-10-01 (America/Los_Angeles).
Recovered research head: `c22d1b4a18d8918c617153f1a3296ab73cfd2aee`.

## Genuine test pairings

The constructed signed gap function is globally bounded by actual carrier
L1 mass times the gap denominator constant. Every Schwartz test is L1,
so its signed gap-function pairing genuinely converges. This assertion
does not require the test to be support-separated.

For a Schwartz test u vanishing on (-a,a), with 0≤c<a, the certified
exterior convolution error passes through the ordinary integral. The
pairing error is bounded by

    compactL1Mass(h) * L1Norm(u) * exp(-2(a-c))^N / (1-exp(-2(a-c))).

On the central interval the integrand vanishes because u does; on the
exterior the prior quantitative bound applies. Both individual pairings
and their sum are genuinely integrable. Geometric decay gives convergence
of the finite convolution pairing to minus the signed gap-function pairing.
No singular whole-line kernel is substituted into an integral.

## Exact remaining tail target

The prior exact operator split gives, for every N,

    shiftedTail_N(u) = actualArchimedeanAction(u) + finiteConvolutionPairing_N(u).

Consequently the actual shifted-tail pairing converges to

    actualArchimedeanAction(u) - signedGapFunctionPairing(u).

Uniqueness of limits proves that shifted-tail convergence to zero is
equivalent to actual exterior source attachment on this test. The limit
is constructed, but its zero value is not proved. This makes the remaining
obligation explicit without adding a tail-vanishing premise or concealing
the original retained full-symbol growth premise.

## Remaining obligations

Prove the actual shifted tail vanishes on support-separated tests using
independent digamma control. Whole residual/source identity, central
cancellation, boundary reconstruction and actual source-domain/quadratic/
polarization/normalized estimate witnesses remain open.

Threshold bookkeeping is closed; logarithmic coercivity has not started.
Canonical Weil, main and WD-T40 mathematical standing are unchanged.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,969 build jobs passed. All five audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `20948ced81df10d90d34de9dea740628ead1c53e`,
run `36969430502`, job `110720096333`, source blob
`079b87d17502e6159dffee61b3fb993ab31fa735`.

Validation-only workflow/cache changes
are excluded from research promotion; prior checkpoint notes are immutable.
