# RPB108 LF10: measurable and integrable internal jump source

Adds `NeutralLogMetricJumpCap.lean` on the isolated formalization branch.

## Four public declarations submitted

1. Measurability of the actual jump density as a parameter integral. The
   underlying function on (r,t) is measurable; Mathlib's strongly measurable
   Bochner parameter integral theorem applies with restricted time measure.
2. Measurability of the spatial cancelled difference for measurable trials.
3. Genuine spatial integrability on any finite cap, under an explicit
   nonnegative modulus L for the trial differences there. LF09's pointwise
   cancellation and finite cap measure give an integrable bounded function.
4. Integral norm budget `2*B*L` for B>=0. The proof compares the integral
   of the norm against the constant L and evaluates the interval measure.

The trial modulus is given for a fixed x and every y in the cap; no global
Lipschitz assumption is needed. The diagonal is handled by the zero trial
difference. Parameter measurability does not assert that the defining time
integral converges at r=0; LF09 supplies convergence only for r>0.

## Validation boundary

LF01 through LF04 passed full hosted root builds. LF05 run 38096709611 is
still building the root. LF09 run 38097432785 was pending before this
submission. LF06 through LF10 remain unverified by hosted compilation.
The cumulative analytic modules are targeted before the complete root.
There is no local Lean executable. The local unfinished-declaration scan
is not a kernel check.

## Remaining source obligations

The internal spatial convergence obligation is addressed by the submitted
theorems. The next analytic cursor is an integrable far-tail majorant using
the exponential damping, followed by actual endpoint-tail convergence
and L2 control. The conservative LF09 1/r bound does not suffice at infinity.
Poisson mixture exchange, zero-extension splitting, endpoint-sensitive L2
convergence and identification with the spectral physical source remain
open. Both endpoint tails remain in the candidate. No new aperture, F4 or
RH claim is made, and research branches remain unchanged.
