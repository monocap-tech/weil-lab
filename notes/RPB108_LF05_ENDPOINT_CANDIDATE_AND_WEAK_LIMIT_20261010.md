# RPB108 LF05 — endpoint candidate and whole weak limit

LF03 b02c9b7 passed run 38093915524, including the complete root library.
LF04 36ca7ca remains under hosted root checking at this pass.

## Added source

NeutralLogMetricEndpointSource.lean defines RC24's damped jump density,
one-endpoint tail, two-tail exterior source and full physical candidate.
It proves nonnegativity of the density and tails, reflection exchange of
the two endpoint contributions, and the exact constant-trial identity
`L_B(z) = z * (1 + E_B)`. Both tails are retained in every definition.

A whole weak limit theorem proves that L2 convergence of physical sources,
with exact truncated test identities and convergence of those forms to the
canonical metric, yields the full limiting weak identity. The tests range
over the entire canonical carrier; no spectral-domain upgrade is required
for the arbitrary test vector.

Four definitions and six theorems are submitted for hosted checking.

## Analytic boundary

Lean's Bochner integral is totalized. These definitions and nonnegativity
results alone do not certify improper convergence, local integrability,
endpoint divergence, or membership of the candidate in L2. The intended
source formula is used on the open cap, with strictly positive endpoint
distances. The diagonal singularity still requires Lipschitz cancellation.

The weak limit theorem assumes actual L2 convergence and convergence of the
whole truncated forms. It does not assert those premises for the Poisson
mixture. Their proof is the next analytic obligation, along with the exact
Laplace/Fourier representation and RC24's endpoint norm bounds.

No equality between the candidate and LF04's spectral source has yet been
proved. No numerical enclosure, new aperture, F4 or RH is certified.

## Cursor

Finish LF04/LF05 hosted checking. Prove the damped logarithm integral and
truncated Poisson attachment, then the endpoint-sensitive L2 limit.
