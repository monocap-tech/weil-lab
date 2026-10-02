# RPB-108 — actual centered residual pairing limit

Date: 2026-10-02 (America/Los_Angeles).
Recovered research head: `536987d576594fd7ec9c110e8ecf26f79099dd1d`.

## Integrable domination

Let C_N be the actual centered shifted digamma symbol, L its certified
pointwise limit, S the fixed cubic-series mass, and v the inverse Fourier
transform of a Schwartz test u. The prior envelope gives

    ‖C_N(ξ)‖ ≤ ‖C_0(ξ)‖ + 64π²ξ²S.

The actual carrier h is globally L1, so its Fourier transform is bounded
by M=∫‖h‖. The two actual Schwartz functions

    v_0 = smulLeftCLM(C_0)(v),
    v_2 = smulLeftCLM(ξ ↦ ξ²)(v)

give the explicit integrable majorant

    B(ξ) = M(‖v_0(ξ)‖ + 64π²S‖v_2(ξ)‖).

The module proves ‖(v(ξ)C_N(ξ)) Fourier(h)(ξ)‖≤B(ξ) for every N and ξ.
This uses `RightLimitWeilSymbolTemperatePremise a` for C_0 and the actual
finite centered symbols, retaining the existing full-symbol growth input.
It requires no pointwise boundedness or physical smoothness of h.

## Actual action and represented residual

Fourier-side Fubini identifies the existing centered multiplier action
exactly with the actual frequency integral, with the inverse-test sign and
the fixed mathlib frequency normalization preserved. Dominated convergence
then proves, for every Schwartz test,

    centeredAction_N(h)(u) → ∫ (v(ξ)L(ξ)) Fourier(h)(ξ).

No smooth limiting-symbol multiplier is assumed. On support-separated tests,
uniqueness against the previously certified physical limit identifies this
frequency residual with the archimedean multiplier pairing minus the signed
physical gap pairing: precisely the actual exterior source-attachment defect.
Neither residual representation is asserted to vanish.

## Remaining obligations

The frequency pairing domination and limit passage are constructed.
Prove actual residual cancellation to obtain tail vanishing and exterior
attachment. Whole source identity, central cancellation, boundary reconstruction
and actual source-domain/quadratic/polarization/normalized estimate witnesses
remain open. The full-symbol growth premise is retained.

Threshold bookkeeping is closed; logarithmic coercivity has not started.
Canonical Weil, main and WD-T40 mathematical standing are unchanged.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,974 build jobs passed. All seven audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `726048d7d95a6002f74e5adda6ed19737be4eb9a`,
run `37028063173`, job `110907648291`, source blob
`23afba0e8b87f3255ebd9023f9d70161c22c3a7a`.

Validation-only workflow/cache changes
are excluded from research promotion; historical notes are immutable.
