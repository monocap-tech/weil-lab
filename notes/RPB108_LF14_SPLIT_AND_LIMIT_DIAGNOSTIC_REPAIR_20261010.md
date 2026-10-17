# RPB108 LF14: split-set and limit-uniqueness repair

LF11 run 38098224642 and LF13 run 38098484897 completed with failures.
The Laplace module compiled successfully in both runs. The full-root check
was skipped because the targeted build failed. LF01 through LF04 remain
the full-root checked boundary; Laplace has independent module-level evidence.

## Observed remaining failures and submitted repair

The Poisson integral split left the endpoint of its Iic set unconstrained.
Specify `s := Iic (0 : real)` in `integral_add_compl`. This preserves the
same exact decomposition into nonpositive and positive frequency halves.

The endpoint weak-limit theorem used a `.unique` projection not available
for `Tendsto` in the pinned Mathlib version. Invoke `tendsto_nhds_unique`
with the two established convergence proofs explicitly. Its conclusion is
the same whole weak attachment equality, with no added assumption.

The jump-bound module only uses standard Cauchy integrability and integral
facts, not the Poisson Fourier pair or its mass theorem. Replace its unused
PoissonMass import with the direct Mathlib improper-integral import. This
allows the actual jump and endpoint modules to be compiled independently
of the pending Poisson algebra.

## Validation boundary and next cursor

These repairs await a fresh hosted cumulative build. They do not certify
LF05 or LF07 onward. No local Lean executable is available. All research
refs and the pinned PR base remain unchanged.

First resolve remaining kernel diagnostics. The analytic cursor remains
square integrability of the actual two-tail exterior source from the
logarithmic endpoint majorant, then the full bounded Lipschitz candidate.
Mixture exchange, physical L2 convergence, zero-extension splitting and
equality with the spectral metric source remain open. No new aperture,
F4 closure, Green-domain identification or RH claim is made.
