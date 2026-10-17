# RPB108 LF06 — damped logarithm Laplace representation

Continues LF05 884b0fd on the isolated formalization branch.
LF01 through LF04 have completed full-root hosted checks. LF05 remains
in progress in run 38096709611 at this pass.

## New analytic patch

The pinned Mathlib v4.34.0 includes Frullani.integral_Ioi_eq. The new
NeutralLogMetricLaplace.lean specializes it to f(t)=exp(-t), damping b>0
and b+s with s>=0. Before applying Frullani, the patch proves

    0 <= exp(-b*t)(1-exp(-s*t))/t <= s exp(-b*t), t>0.

The integrable exponential majorant establishes actual improper convergence.
The specialized integral is log((b+s)/b); at b=exp(1), this gives RC24's
exact logarithmic weight representation. One definition and four theorems
are submitted for hosted checking. No convergence premise is assumed in
the final logarithm identity.

The module is added to the small certificate-build step so elaboration
errors surface before the complete root audit. No project axiom or unfinished
proof is introduced.

## Remaining boundary

This is the scalar multiplier identity only. The Poisson Fourier transform,
exchange of integrals, truncated physical source attachment, diagonal
Lipschitz cancellation and endpoint-sensitive L2 convergence remain open
in Lean. LF05's endpoint candidate is not yet identified with LF04's source.
No matrix, aperture, F4 or RH result is certified by this pass.

## Cursor

Check LF05/LF06 hosted results; then formalize the Poisson Fourier pair
with the project's exp(-2*pi*i*xi*x) normalization.
