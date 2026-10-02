# RPB-108 — actual right-half-plane digamma Euler identity

Date: 2026-10-02 (America/Los_Angeles).
Recovered research head: `d83104a00e91112b50b538a2b86585b26c735c21`.

## Actual analytic identification

Strictly positive real part excludes every nonpositive integer Gamma pole.
Actual Gamma is therefore complex differentiable on the right half-plane,
and its derivative is holomorphic there. Actual Gamma is nonzero throughout
that domain, so ψ=Γ'/Γ is holomorphic there as well.

The independent regularized Euler candidate E is already certified
holomorphic on this same domain. The preceding full complex positive-real
anchor gives ψ(x)=E(x) for every real x>0. Embedded real points x>1
accumulate at the interior point 1 and belong to the equality set with
that point removed. The right half-plane is convex and preconnected.
The analytic identity theorem thus proves ψ(z)=E(z) whenever Re z>0.

Combining equality with independent absolute summability gives

    HasSum [1/(n+1)-1/(z+n)] (Complex.digamma(z)+γ).

This is actual complex digamma representation on the whole right half-plane.
It uses full complex equality, not merely equality of real parts. No Gauss
representation or retained full-symbol growth premise enters the proof.
No pointwise Gamma approximation limit is differentiated.

## Remaining obligations

Specialize this actual HasSum to the source line, align its real reciprocal
terms with the certified centered-increment residual and prove cancellation.
Then consume the existing actual pairing limit, which retains full-symbol
growth, to establish exterior source attachment.

Residual cancellation, tail vanishing, exterior/whole source attachment,
central/boundary reconstruction and actual source-domain/quadratic/
polarization/normalized estimate witnesses remain open. Canonical Weil,
main and WD-T40 standing are unchanged. Threshold bookkeeping is closed;
logarithmic coercivity has not started.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,978 build jobs passed. All six endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; declaration gate passed. Validation head `42497ee96cc557201b2f87a12dee1f78e6786791`, run `37066190783`, job `111034442714`, source blob `5e236a85ccd8335f116e917e8c77cd94198ef626`.

Validation-only workflow/cache changes are excluded from research promotion;
historical notes are immutable.
