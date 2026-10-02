# RPB-108 — actual scalar action separation and centered digamma tail

Date: 2026-10-02 (America/Los_Angeles).
Recovered research head: `0ed9df1239eabbfbba06eec7509badbe07432d9b`.

## Generic scalar subtraction law

For a temperate symbol m and any scalar k, the existing tempered Fourier
multiplier satisfies

    M(m-k) f(u) = M(m) f(u) - k f(u).

This follows from lawful multiplier additivity and the actual constant-
multiplier identity, not from an assumed physical representation.

## Actual carrier support attachment

If u vanishes on (-a,a) and c<a, its product with the actual compact
carrier representative is pointwise zero. Inside [-c,c], u is zero;
outside [-c,c], the representative is zero. The existing ordinary-integral
evaluation therefore gives carrier.temperedMode(u)=0. This is annihilation
of the carrier distribution, not central cancellation of the source
residual and not vanishing of the archimedean multiplier action.

## Actual centered tail

Define centeredSymbol_N(ξ) as shiftedSymbol_N(ξ)-shiftedSymbol_N(0).
For every fixed N its temperate growth is derived from the retained actual
full-symbol growth premise and constant growth; no uniform bound is proved.
The scalar subtraction law and actual support attachment show that the
centered and uncentered shifted actions agree exactly on every separated
test, regardless of the scalar's growth with N.

The centered pairing therefore has the previously constructed limit:
actual archimedean action minus signed gap-function pairing. Its convergence
to zero is equivalent to exterior source attachment on the test. Neither
zero limit nor source attachment is supplied as a witness.

## Remaining obligations

Scalar action separation is closed. Independent control of the actual
centered nonzero-frequency digamma remainder remains next. Prove its
tested action tends to zero. Exterior/whole source identity, central
cancellation, boundary reconstruction and actual source-domain/quadratic/
polarization/normalized estimate witnesses remain open.

Threshold bookkeeping is closed; logarithmic coercivity has not started.
Canonical Weil, main and WD-T40 mathematical standing are unchanged.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,971 build jobs passed. All six audited endpoints use only `propext`,
`Classical.choice`, and `Quot.sound`; declaration gate passed.
Validation head `4c562ff72edae1571e590ca3357bbc03a0c3940f`,
run `37009813241`, job `110846577087`, source blob
`0e2c679ae105a1fc0e7cead1cb33a6e190ea3183`.

Validation-only workflow/cache changes
are excluded from research promotion; prior checkpoint notes are immutable.
