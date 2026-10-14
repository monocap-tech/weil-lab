# RC225 - optimize the paid eleven-vector trial

RC225 certifies an actual eight-source inverse-response width of
**0.770397**, improving RC224's 0.778220 by 0.007823 (about 1%). Both
endpoints of the selected enclosure use the coupled identity. The
half-Gram gate remains open: 0.770397 exceeds 0.5.

## What changed

RC224 chose its new trial coefficients by minimizing the nominal residual.
RC225 instead proposes all 88 coefficients of the eleven-by-eight trial
map jointly with seven positive error/tail payment parameters, targeting
the fully paid inverse-width objective. Raw action and response Gram
whitening improves the conditioning of this numerical proposal problem.
The proposed coefficients are rounded to exact rationals with denominator
10^30, and the shared-error payment parameters are then optimized again
for this rational trial.

The source family, eleven-vector trial span, canonical operator, domain,
source Gram normalization, RC223 endpoint centers, complete action-error
radii, and all input/output cutoffs remain unchanged. Only the trial map
and its payment parameters change. In particular, trial optimization does
not create additional independent response sources.

| Certified quantity on the same source Gram | RC224 | RC225 |
| --- | ---: | ---: |
| Nominal residual Gram upper bound | 0.057170 | 0.060681 |
| Complete shared trial-action error Gram upper bound | 0.005812 | 0.005660 |
| Actual inverse-response width upper bound | 0.778220 | 0.770397 |

These quantities measure different intermediate/final bounds. Increasing
the nominal residual slightly can improve the final inverse enclosure
when it reduces the other paid contributions. Nominal least-residual
selection is therefore not identical to paid inverse-width selection.

## Verification and scope

The validator pins the RC224 interface, certificate, and helper together
with all inherited dependencies. It checks that the complete action-error
ledger agrees with the interface and that the reference source Gram agrees
with RC222. For the new rational trial it reconstructs the residual,
mixed-action, source-tail, and action-tail matrices using RC224's directed
interval machinery. Shared regular high-input, delta regular low-input,
matched centered endpoint, and remaining individual errors are all paid.
No actual action error is set to zero or attached to incompatible centers.

The floating optimizer supplies candidates only. Exact rational PSD checks
certify the chosen two-sided enclosure, relative width, and failed gate.
The prior RC224 actual enclosure remains an independent fallback. A
reverse-order replay uses the saved rational trial and payment proposals
and reproduces the parsed certificate exactly. Publication adds the
validator, certificate, and this note using an expected-head non-force
update; no earlier file is replaced.

The numerical optimizer's local convergence is not a global minimum proof.
This checkpoint supplies no fixed-span impossibility claim, no actual-error
lower bound, and no assertion that parameter optimization can never pass.
The modest observed gain supports prioritizing a stronger residual/action
construction or a new trial enrichment in RC226 rather than assuming
further tuning will close the gate.

The accepted six-source inverse width 0.4361 and RC216 eight-source native
action-error gate 0.420465 are retained. The actual eight-source inverse
gate, source-range and odd-sector coverage, Stage I, F4, Lean, and RH remain
open.
