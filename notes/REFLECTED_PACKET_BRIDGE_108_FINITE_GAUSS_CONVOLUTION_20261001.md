# RPB-108 — finite Gauss convolution and weak Fourier transfer

Date: 2026-10-01 (America/Los_Angeles).
Recovered research head: `542d00ae49757f9926654b5ded58988ebf9f1c89`.

## Actual finite physical kernel

The prior geometric kernel is pointwise exactly the finite sum
K_N(x) = sum(n<N) exp(-(2n+1/2)|x|), including x=0 and N=0.
Every term is globally integrable. Finite integral interchange computes
the Fourier transform as the actual sum of digamma reciprocal terms at
t=2πξ. No off-diagonal restriction is needed at this finite stage.

## Actual rough-carrier convolution

For the retained actual compact carrier h, q_N = h * K_N is globally L1.
The convolution Fourier theorem applies from actual global L1 of both
inputs, without pointwise boundedness or smoothness of the rough carrier.

Its exact Fourier transform is
FT(q_N)(ξ) = FT(h)(ξ) sum(n<N) neutralGaussReciprocal(n,2πξ).

On every Schwartz test u, the physical product u q_N is genuinely
integrable and its integral equals the frequency integral
inverseFT(u)(ξ) FT(h)(ξ) sum(n<N) neutralGaussReciprocal(n,2πξ).
This uses the library's bilinear L1 Fourier/Fubini identity and Schwartz
inversion, so the test sign and normalization are fixed.

The positive finite kernel matches the positive reciprocal sum; its
negative is the term subtracted from the shifted digamma tail.

## Remaining obligations

This is the actual finite convolution and weak Fourier identity.
It is not yet packaged as the existing tempered Fourier-multiplier CLM.
That packaging and the shifted digamma tail's weak/operator limit remain
separate next obligations. The infinite Gauss kernel is singular at zero;
its off-diagonal pointwise limit cannot justify a whole-line L1 limit.

Whole archimedean source attachment, central cancellation, boundary
reconstruction, actual compact weak realization and source-domain/
quadratic/polarization/normalized estimates remain open. Threshold
bookkeeping is closed; logarithmic coercivity has not started.
Canonical Weil, main and WD-T40 mathematical standing are unchanged.

## Certification

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`;
8,965 build jobs passed. Seven endpoints use only `propext`, `Classical.choice`,
and `Quot.sound`; declaration gate passed. Validation head
`9d88d87631c8526cad40e106fe8f25e8feff1eed`, run `36958521515`,
job `110686795036`, source blob `38c6bf719c8cb5aecc4ffcb5673d14af57d0fad9`.
Validation-only workflow/cache changes are excluded from research promotion.
Prior checkpoint notes remain immutable.
