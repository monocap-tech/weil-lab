# RC221: eleven-trial inverse and the action-error payment frontier

Starting head: `ae3045e1ca42b6ec0e7f5ec121b753297146c5c9` (RC220).

RC221 adds the complete q220 mixed/action rows to the existing ten-trial
interface, retaining **eight response sources**. It evaluates the enlarged
inverse trial space with all actual error radii and signed tails paid.

The actual eight-source inverse gate **does not pass**. Its selected width
remains **6.717377**, the inherited/refined structural fallback. Nevertheless,
the enlarged nominal residual geometry is substantially better, and an
explicitly artificial zero-action-error payment model passes at **0.378106**.
This gives a concrete reason to prioritize collective error payments next.

## Same-reference comparison

| Certified quantity | Embedded RC218 ten-trial map | Enlarged eleven-trial map |
| --- | ---: | ---: |
| Nominal residual Gram relative upper bound | 0.099641 | 0.055220 |
| Nominal-only residual-chord geometry width upper | 0.666519 | 0.369378 |
| Selected actual inverse enclosure width upper | 6.717377 | 6.717377 |

Each row measures a different quantity. The first two rows describe the
stored nominal carriers and are **not actual inverse acceptance tests**.
For the second row, the exact certified residual Gram bound is multiplied
by `1/a - 1/2`, with `a=32125/230953`. The validator checks the resulting
rational matrix inequality directly. The eleven-trial nominal geometry
is below 0.5; the actual inverse width in the last row is not.

The source D-Gram lower/upper reference matrices are unchanged from RC218.
The original RC217 reference-floor width is also recorded separately. No
normalization change is presented as an improvement of the inverse bound.

## Paid new interface

The old 10 by 10 prefix blocks are copied unchanged from RC218's pinned
materialized interface. Only the new q220 source, source/action, and
action/action rows are assembled through degree 65534. All original native
source centers, nominal action formulas, and cutoff corrections are
retained. Signed analytic polynomials are evaluated by directed interval
Horner arithmetic; this encloses the same exact polynomials, without
changing their definitions.

q220 is an exact finite polynomial of degree 768. Its source has no infinite
input tail. Its canonical action uses RC220's complete error radius and
signed 25-moment analytic endpoint tail. Every old-source/new-action mixed
tail is paid using the inherited source amplitudes and the new signed
endpoint model. Each actual mixed pairing is independently bounded in both
self-adjoint orientations, including complete action-error payments and
full source-norm bounds; all eleven interval intersections are nonempty.

The new nominal Gram blocks are not silently made self-adjoint. The coupled
inverse transport retains the finite trial/residual cross matrix, source
and residual analytic tails, and the same action error combined before
Young's inequality. Positive rational optimization parameters are only
proposed numerically. Exact rational PSD tests certify all accepted
enclosures and widths.

The reusable eleven-column prefix interface is saved separately. The main
certificate saves both trial maps, complete residual/error matrices, all
rational proposals, the actual enclosure, and the diagnostic model.

## Explicitly counterfactual payment check

For the eleven-trial map, RC221 reruns the same transport with all eleven
action-error radii **artificially set to zero**. Source and infinite-output
tails, finite interval uncertainty, variational-tail payments, cross-tail
payments, and the fixed source normalization remain in place.

The resulting rational width is `189053/500000 = 0.378106`, with a positive
margin `0.121894` to 0.5. Its matrix PSD checks replay exactly. The output
labels this as a counterfactual payment enclosure, **not an actual operator
certificate**. RC221 neither constructs zero-error actions nor reduces the
actual action radii. The diagnostic isolates a feasible payment model; it
does not assert the existence of an operator with those exact nominal
actions, and it cannot establish actual inverse acceptance or Stage I.

In particular, the already accepted RC216 action-error gate and this
inverse-transport error payment are different tests. Passing RC216 does
not eliminate the error amplification in a trial inverse map.

## Replay, custody, and next frontier

```bash
python scripts/validate_rpb108_rc221_eleven_trial_inverse.py --output certificates/rpb108_rc221_eleven_trial_inverse.json --interface certificates/rpb108_rc221_materialized_prefix_interface.json
python scripts/validate_rpb108_rc221_eleven_trial_inverse.py --output certificates/rpb108_rc221_eleven_trial_inverse.json --interface certificates/rpb108_rc221_materialized_prefix_interface.json --replay
```

Replay verifies all immutable input/helper Git blob pins, reverses the
finite prefix and proposal traversal, and compares both complete artifacts.
Both actual and counterfactual payments are recomputed, using saved rational
proposals rather than rerunning floating optimization. Publication is
add-only with an expected-head, non-force branch update; existing files
remain unchanged.

RC222 should refine shared/correlated action-error payments in the saved
eleven-trial transport, including shared regular-input tails and compatible
endpoint-tail structure where justified. Another independent response
source is not required by this checkpoint. More enrichment remains possible,
but the present diagnostic does not demand it as the immediate next step.

The RC210 six-source inverse width 0.4361 and RC216 eight-source action-error
gate 0.420465 remain accepted and unchanged. Actual-residual half-norm capture
is not assumed. Eight-source inverse acceptance, source-range and odd
coverage, Stage I, RH, F4, and Lean closure remain open. No failure of the
true inverse is inferred from a failed sufficient enclosure.
