# RC228 - actual eight-source inverse gate passed

The actual eight-source canonical inverse-response width is certified at
**0.485647 < 0.5**, with margin **0.014353**. This improves RC226's 0.766318
on exactly the same eight-source Gram normalization. Both endpoints of the
selected enclosure use the coupled identity. All twelve action errors and
all source, action, and residual tails are paid.

This closes the finite eight-source inverse-width gate. It does not close
Stage I or prove RH. Source-range and odd-sector coverage, the remaining
Stage I interfaces, F4, Lean, and RH remain open.

## Compatible twelve-trial calculation

The response family is unchanged:
P0, P2, f0, psi0, w14, v10, delta=z_b6-v10, and t10.
The trial order is
P0, P2, f0, psi0, w14, q185, v10, q202, delta, t10, q220, q227.
The twelfth trial is not a ninth independent response source.

q227's source, mixed-action, and nominal action-Gram entries are rebuilt
through degree 65534 using its exact degree-1536 polynomial, complete
canonical action certificate, and analytic endpoint output moments. The
eleven-by-eleven source/mixed/action prefix blocks agree exactly with
RC224. The new source pairings overlap RC227's independently constructed
source-Gram intervals. All twelve actual q227 self-adjoint pairing
intersections are nonempty, with the actual action errors paid in both
orientations. q227 has no infinite source tail; its infinite action output
and high regular input are still paid.

The new nominal least-residual trial coefficients are proposed from the
midpoint action Gram and rounded to rational denominator 10^30. Complete
shared-error payments retain the regular high-input, delta regular
low-input, matched centered endpoint, and remaining individual terms.
The complete q227 error is added to the latter term: its high regular
input error is not subtracted or silently set to zero.

The source Gram lower/upper bounds are checked against RC226 explicitly.
Every old complete action-error radius agrees with the previous ledger,
and the new radius agrees with RC227's complete certificate. The canonical
operator, domain, source definitions, and old action centers are unchanged.

## Certified quantities

| Quantity on the unchanged source Gram | RC226 | RC228 |
| --- | ---: | ---: |
| Actual inverse-response width upper bound | 0.766318 | 0.485647 |
| Eight-source half-Gram inverse gate | Open | Passed |

RC228's nominal residual Gram upper bound is 0.032017. Its complete shared
trial-action error Gram upper bound is 0.004995. These are intermediate
payments, not inverse widths. Coherent signed trial/residual tail bounds
are retained from RC226 and generalized to twelve trial columns. The
coupled inverse identity, positive parameter restrictions, and exact PSD
acceptance checks are unchanged.

The rational enclosure matrices satisfy

    (1/2) G_lower - (inverse_upper - inverse_lower) >= 0,

by exact rational PSD elimination. Numerical optimization only proposes
the rational parameters. The certified relative-width grid bound is
485647/1000000. The old RC226 enclosure remains an independently valid
fallback, but the passing selection uses two new coupled endpoints.

RC227's half-norm residual-capture tests did not pass. That does not
invalidate its exact polynomial or complete action certificate. The
uniform twelve-trial inverse calculation is a different test and has now
passed with every actual error paid. Likewise, RC226's fixed eleven-trial
payment-model obstruction does not apply unchanged to this new trial map.

## Verification and remaining frontier

Reverse replay reconstructs the prefix in reverse degree order and checks
the saved rational proposals, producing identical parsed main and prefix
certificates. Publication adds four files using an expected-head non-force
branch update. Existing files are preserved, dependency pins and remote
blob hashes are checked, and the additions contain no conflict markers.

The accepted six-source inverse width 0.4361 and RC216 eight-source native
action-error gate 0.420465 remain intact. The latter measures a different
quantity and is not directly comparable with the inverse widths.

RC229 should first audit the passed eight-source gate against the exact
remaining Stage I interface and coverage obligations. Further numerical
shrinking is not a substitute for proving source-range and odd-sector
coverage. No additional source count, completion date, or Stage I closure
is inferred from this finite gate alone.
