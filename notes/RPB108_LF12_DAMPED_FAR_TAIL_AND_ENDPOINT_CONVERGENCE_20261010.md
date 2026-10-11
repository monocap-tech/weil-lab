# RPB108 LF12: damped far-tail and endpoint convergence

Adds `NeutralLogMetricEndpointBounds.lean` to the isolated formalization
branch. This is an analytic source submission, not yet a checked result.

## Four public declarations submitted

Let `C = 1/(2*pi^2*exp(1))`.

1. The actual jump density satisfies `ell(r) <= C/r^2` for r>0. The
   spatial denominator is bounded below by `4*pi^2*r^2`; integrating the
   remaining exponential over t>0 gives `1/exp(1)`.
2. The jump density is integrable beyond any d>0. LF10 supplies spatial
   measurability, and the inverse-square majorant is genuinely integrable.
3. The endpoint tail satisfies `tail(d) <= C/d` for d>0. Two private
   lemmas specialize Mathlib's real-power improper-integral theorems.
4. At every interior point |x|<B, both exterior contributions obey the
   sum of the reciprocal-distance bounds at B-x and B+x.

This closes the submitted far-tail convergence obligation left by LF09's
nonintegrable-at-infinity 1/r majorant. Both endpoint tails are retained.
The reciprocal-distance upper bound is coarse and cannot establish L2
integrability up to either endpoint. A logarithmic near-endpoint estimate
is still needed for trials with nonzero endpoint traces.

## Validation boundary

LF01 through LF04 remain the kernel-checked boundary. LF05 and LF10 runs
failed in the endpoint, Laplace and Poisson foundations; LF11 repairs the
observed diagnostics. LF11 run 38098224642 is still in progress while this
pass is prepared. LF12 is included in the next cumulative targeted and
full-root builds. No local Lean executable is available, and a source scan
does not substitute for kernel compilation. LF05 onward remain unchecked.

## Next cursor

First resolve any remaining hosted elaboration diagnostics. Analytically,
combine the 1/r near-diagonal budget with the inverse-square far budget
to obtain logarithmic endpoint growth, then actual endpoint-sensitive L2
control. Mixture exchange, truncated source attachment, zero-extension
splitting and equality with the spectral physical source remain open.
Research branch refs and the PR base remain unchanged. No aperture,
F4, Green-domain identification or RH claim is made.
