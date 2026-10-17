# RPB108 LF09: actual jump convergence and diagonal cancellation

Adds `NeutralLogMetricJumpBounds.lean` to the isolated formalization branch.
The pinned research base and all research branch refs remain unchanged.

## Analytic result submitted

Three private Cauchy lemmas establish the genuine full-line integrability
and exact integral of `1/(t^2+a^2)` for a>0. Three public declarations then
establish:

1. Integrability on t>0 of the defining exponentially damped jump integrand,
   whenever r>0. The exponential is bounded by one on this domain.
2. The conservative bound `ell(r) <= 1/r`. Extending the undamped majorant
   from the positive half-line to the full line loses a factor of two but
   is sufficient for cancellation.
3. Pointwise norm bound L for the jump difference under an explicit
   Lipschitz modulus. The x=y case is handled directly by the zero trial
   difference, without asserting convergence of the defining time integral
   at r=0.

This replaces an actual off-diagonal convergence obligation from LF05;
the conclusion no longer relies on the totalized value of a divergent
integral. The cancellation conclusion is pointwise, not yet a spatial
integrability theorem.

## Validation boundary

LF01 through LF04 have passed complete hosted Lean root builds. At the
LF09 submission, LF05 run 38096709611 remains in its full-root build and
LF08 run 38097120934 is pending. LF06 through LF09 have not yet passed
hosted compilation. Superseded pending runs are cancellations, not proof
failures. LF09 is added to the targeted analytic build before the root.
Local source scans check unfinished declarations only; no local Lean
executable is available. Do not treat submitted declarations as checked.

## Next cursor

Prove spatial measurability of the jump density, then integrate the bounded
Lipschitz difference on a finite cap. Obtain an integrable far-tail majorant
using exponential damping (the 1/r bound alone is insufficient at infinity).
Both endpoint tails, their L2 bounds, finite Poisson mixture exchange,
zero-extension splitting and whole weak attachment remain required. The
full-line Poisson unit mass does not remove either exterior contribution.

No new aperture, CC119 import, F4 closure, RH conclusion or identification
of the Green source domain with the metric form domain is claimed.
