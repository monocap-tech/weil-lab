# RPB-108 — independent holomorphic complex Euler candidate

Date: 2026-10-02 (America/Los_Angeles).
Recovered research head: `b500cb88d2fbc22b25bc9cd22cb8d24d25775cc4`.

## Independent analytic construction

Define T_n(z)=1/(n+1)-1/(z+n) and E(z)=-γ+∑' n,T_n(z).
These definitions assert no equality with actual complex digamma.
For 0<a≤1 and a≤Re z, the positive real part of z+n gives

    a(n+1) ≤ Re(z+n) ≤ ‖z+n‖,
    ‖T_n(z)‖ ≤ (‖z-1‖/a)/(n+1)^2.

The rational identity T_n(z)=(z-1)/[(n+1)(z+n)] supplies the
cancellation yielding this quadratic decay. The shifted p-series is
summable, so the candidate series is absolutely summable at every point
with Re z>0 by choosing a=min(Re z,1).

On each open region a<Re z and ‖z-1‖<R, the bound becomes the uniform
summable majorant (R/a)/(n+1)^2. Each rational term is holomorphic there
since its only variable denominator has strictly positive real part.
The complex uniformly dominated sum theorem gives holomorphy of the sum
on that region. Every right-half-plane point belongs to such a region,
which proves E is holomorphic throughout the right half-plane.

No Gauss representation, actual digamma identification or retained
full-symbol growth premise enters this construction. No pointwise Gamma
approximation limit is differentiated.

## Remaining obligations

Establish actual digamma holomorphy on the same connected domain and apply
the identity theorem using the certified full complex positive-real Euler
anchor. Then cancel the actual centered source-line residual and consume
the existing certified pairing limit, which retains full-symbol growth.

Residual cancellation, tail vanishing, exterior/whole source attachment,
central/boundary reconstruction and actual source-domain/quadratic/
polarization/normalized estimate witnesses remain open. Canonical Weil,
main and WD-T40 standing are unchanged. Threshold bookkeeping is closed;
logarithmic coercivity has not started.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,977 build jobs passed. All five endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `c2659d1fba74be355f672b65dcaebc8a12f43aa4`, run `37064676684`, job `111029397055`, source blob `e3ae2c1ecd5d0bca73ba5b2eb9fa1d328c0a69e1`.

Validation-only workflow/cache changes are excluded from research promotion;
historical notes are immutable.
