# RPB108 LF04 — constructed spectral log-metric source

LF02 repair eae4d100 passed the certificate targets, complete root library,
and unfinished-declaration check in hosted run 38093853989. LF03 b02c9b7
remains under hosted checking at the time of this pass.

## New construction

NeutralLogMetricPhysicalSource.lean defines the exact logarithmic spectral
product and constructs its inverse-Fourier physical L2 source whenever that
product belongs to L2. It proves the Fourier identity, the full-carrier mixed
metric identity, the whole weak source identity, and the moment residual
identity using the constructed trial action. Two definitions and four theorems
are submitted for hosted checking.

This removes the abstract trial-action premise for spectral-domain vectors.
It does not prove operator-domain membership from form-domain membership.
The one-logarithm form-energy domain is retained without strengthening it.

## RC24 boundary

RC24 gives a Lipschitz-trial source via the jump density and both exterior
tails. The new spectral construction is the exact Fourier-side object to
which that formula must attach. Missing: the Laplace representation and
Poisson transform, truncated-source convergence, identification on the cap,
and the Lipschitz endpoint L2 estimate. These are not imported as axioms.
No numerical witness, aperture extension, F4, or RH is certified.

## Cursor

Complete LF03/LF04 hosted checks; prove the truncated Poisson difference
attachment, then its endpoint-sensitive L2 limit.
