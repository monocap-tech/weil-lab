# RPB108 LF03 — build repair and attached residual interface

## Recovered build evidence

LF01 commit cecfa297 passed the complete root library and unfinished-declaration
check in run 38081711674, job 114299805937. The formerly pending baseline is
therefore checked at that commit, not merely present as source.

LF02 commit 8d82180f failed before the root step in run 38082152901.
The diagnostics identified a missing StarOrderedRing real instance, an
unavailable InnerProduct scoped namespace, and use of mul_le_mul_right as
an equivalence. The repair imports the complete Mathlib instance environment,
removes the unnecessary scoped opens, and uses nonlinear arithmetic directly.
The repair commit eae4d100 is submitted for hosted checking in run 38093853989.

## Added proof interfaces

- Direct squared-inclusion transport, preserving the explicit nonnegative
  budget even when the canonical space is zero.
- Whole residual attachment from separate whole source and trial-action
  identities, with conjugate-linear subtraction in the first slot.
- Actual supported-carrier consumption of that attached residual.

These three new declarations await their own hosted compilation. They do not
prove RC24's physical operator formula or its endpoint-sensitive weak identity.
The actual source and action attachments remain explicit premises. No numerical
matrix data, sharper actual inclusion estimate, aperture, F4, or RH is certified.

## Cursor

Finish LF02/LF03 hosted compilation, then attach the physical canonical metric
operator to its full weak form, preserving both endpoint terms. The rational
matrix witness data and interval-to-integral enclosures remain separate patches.
