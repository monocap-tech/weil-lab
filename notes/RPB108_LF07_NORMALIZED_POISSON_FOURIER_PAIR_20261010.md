# RPB108 LF07 — normalized Poisson inverse Fourier pair

Continues LF06 c2e3988 on the isolated formalization branch.
LF01 through LF04 have completed full-root hosted checks. LF05 remains
building and LF06 queued at the start of this pass.

## New analytic patch

NeutralLogMetricPoisson.lean uses the pinned Mathlib complex exponential
Iic/Ioi integral theorems. On the negative half-line the coefficient is
t+i*w; on the positive half-line it is -t+i*w. Their real parts establish
absolute integrability for t>0. Splitting the full line and evaluating both
integrals gives 2*t/(t^2+w^2). Setting w=2*pi*x gives RC24's normalized
Poisson density. The final theorem states the actual inverse Fourier pair
for exp(-t*|ξ|) using Mathlib's Fourier inversion convention.

Two definitions, two private half-line identities and four public theorems
are submitted for hosted checking. The module is checked before the full
root library. No Fourier-normalization premise is assumed.

## Remaining boundary

The inverse pair does not by itself attach the integral mixture to a
physical source. Still needed: exchange of integrals, truncated Poisson
difference attachment, zero-extension split with both exterior tails,
Lipschitz diagonal cancellation and endpoint-sensitive L2 convergence.
The endpoint candidate remains to be identified with the spectral source.
No numerical matrix, aperture, F4 or RH result is certified.

## Cursor

Finish LF05/LF06/LF07 hosted checking; prove the truncated Poisson mixture
attachment and its two-tail cap decomposition.
