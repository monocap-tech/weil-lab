# RPB-108 — full complex actual digamma positive-real Euler anchor

Date: 2026-10-02 (America/Los_Angeles).
Recovered research head: `bb800b705de708043a33b3d880cb8afc8edaa71a`.

## Actual derivative comparison

The actual complex Gamma is differentiable at every positive real x.
Restrict its derivative to the real line, where Gamma_ofReal identifies it
with the embedding of actual Real.Gamma. Embedding the actual real derivative
produces a second derivative of that same real-to-complex function. Uniqueness
therefore proves

    deriv Complex.Gamma(x)=ofReal(deriv Real.Gamma(x)).

Dividing by the actual Gamma value gives

    Complex.digamma(x)=ofReal(deriv Real.Gamma(x)/Real.Gamma(x)),
    Im Complex.digamma(x)=0.

This is actual positive-real digamma real-valuedness. No representation
formula or retained full-symbol growth premise is used.

## Full complex series anchor

Map the preceding certified actual real-axis HasSum through the continuous
real-to-complex linear embedding. Real-valuedness identifies its endpoint
with the actual full complex digamma value. Hence for every real x>0,

    HasSum [1/(n+1)-1/(x+n)] (Complex.digamma(x)+γ),
    Complex.digamma(x)=-γ+∑' n,[1/(n+1)-1/(x+n)].

This is full complex equality, supplying the exact real-axis anchor needed
for a later complex identity theorem. Equality of real parts alone is no
longer substituted for that input.

## Remaining obligations

Construct and justify the holomorphic regularized Euler series on the right
half-plane, establish actual digamma holomorphy there, and identify them
from the full real-axis anchor. Then cancel the actual centered source-line
residual and consume the existing certified pairing limit.
The existing pairing transfer retains its full-symbol growth premise.

Residual cancellation, tail vanishing, exterior/whole source attachment,
central cancellation, boundary reconstruction and actual source-domain/
quadratic/polarization/normalized estimate witnesses remain open.
Threshold bookkeeping is closed; logarithmic coercivity has not started.
Canonical Weil, main and WD-T40 mathematical standing are unchanged.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,976 build jobs passed. All six endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `bf973e0f991b129030d6e72371ab0317ed313ad4`, run `37063437169`, job `111025310561`, source blob `ec5ef4a4c4eaf1c21b96b3f5a979fd4764a0531f`.

Validation-only workflow/cache changes are excluded from research promotion;
historical notes are immutable.
