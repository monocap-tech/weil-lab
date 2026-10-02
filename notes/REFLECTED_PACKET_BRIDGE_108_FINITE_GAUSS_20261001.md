# RPB-108 — finite digamma tail split and Gauss kernel limit

Date: 2026-10-01 (America/Los_Angeles).
Recovered research head: `e873b75ea172e31a55362bf39ab303c0da68bbfd`.

## Pinned library boundary

At mathlib `5ed2965256430c3649e86755f9576b54eca72435`,
`Mathlib/Analysis/SpecialFunctions/Gamma/Digamma.lean` explicitly lists
Gauss's integral representation as TODO. Its proved
`Complex.digamma_apply_add_nat` recurrence is usable now. No missing Gauss
theorem is assumed or disguised as a completed source attachment.

## Exact finite scalar identity

The source line s(t)=1/4+it/2 avoids every nonpositive integer. Taking real
parts in the actual recurrence proves

\[
 \Psi_{\rm arch}(t)
 =\Re\psi(s(t)+N)-\log\pi
 -\sum_{n<N}\frac{n+1/4}{(n+1/4)^2+(t/2)^2}.
\]

This is an equality of the actual source symbol, not an asymptotic approximation.
The shifted digamma tail remains visible.

## Constructed finite kernel and limit

The positive finite half-density is

\[
 K_N(z)=e^{-|z|/2}\sum_{n<N}(e^{-2|z|})^n.
\]

For z≠0, its exact geometric formula is

\[
 K_N(z)=\frac{e^{-|z|/2}}{1-e^{-2|z|}}
             (1-e^{-2N|z|}).
\]

Thus the finite function converges pointwise away from zero to the positive
half-density of the pinned Gauss kernel. The signed exterior candidate uses
its negative. The zero-diagonal singularity is not included in the limit claim.

## Remaining operator transfer

These are the two finite sides of the proposed transfer, not yet their Fourier
identification. Next: prove the rational resolvent/exponential kernel transform,
identify the finite physical action, and control the shifted digamma tail in
the relevant weak/exterior operator limit. Pointwise kernel convergence alone
does not provide those facts or justify exchanging integrals.

Actual archimedean source attachment, central cancellation, boundary/whole-line
reconstruction and source-domain/quadratic/normalized estimates remain open.
Threshold bookkeeping is closed; coercivity has not started. Canonical Weil
and WD-T40 standing are unchanged.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,963 build jobs passed. Six endpoints use only `propext`, `Classical.choice`,
and `Quot.sound`; declaration gate passed. Validation head
`fc66ef1e6111d637f5c538f0e4f8c48cda386aa9`, run `36942968489`,
job `110638504163`, source blob `b5ba95325f037c893d1da96866bb3fd064764978`.

Validation-only workflow/cache changes are excluded from research promotion.
The original research workflow blob remains
`f194e9564577d3b79831b7abfb91b5933f3af98f`.
Prior checkpoint notes remain immutable.
