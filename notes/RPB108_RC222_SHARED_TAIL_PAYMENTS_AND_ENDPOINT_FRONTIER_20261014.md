# RC222: shared tail payments and the endpoint precision frontier

Starting head: `10ea35bd0aa320ee4c55657a7fcdf5826217df62` (RC221).

The certified actual eight-source inverse width improves from **6.717377**
to **4.590826**, on the unchanged source D-Gram normalization. The selected
new endpoints are both coupled. The required width is at most 0.5, so
**eight-source inverse acceptance remains open**.

This calculation uses actual paid errors. No radius is artificially zeroed,
and neither the eleven trial vectors nor their nominal action centers change.
The improvement comes from applying shared operators after signed input
combinations, rather than summing independent marginal tail bounds.

## Four complete error components

For the fixed RC221 `least_residual_11` trial map, the error is decomposed
into four paid components:

| Component | Certified relative Gram upper bound before component Young weights |
| --- | ---: |
| Shared regular high input, degrees at least 514 | 0.000235 |
| Delta regular low band, degrees 130 through 512 | 0.000128 |
| Shared centered endpoint omitted inputs | 0.164556 |
| Remaining projection, rounding, and other errors | 0.000001 |

These are Gram bounds for errors of the inverse trial map, relative to its
eight-source reference Gram. They are not the RC216 native-source action-error
test. Combining the four components with the selected positive rational
Young weights gives a complete relative trial-error Gram bound of **0.176061**.

### Shared regular input

The six signed source tails are `[f0, psi0, w14, v10, delta, t10]`. Their
physical L2 input Gram is summed through degree 65534. The common leading
eta tail is retained as a signed rank-one Gram term; four nonleading
remainders are paid separately. The inherited high-input smoothing bound
and D-metric floor then bound `D^-1 R` applied to their signed combination.

Delta's regular input cutoff is 128, while the other retained regular
inputs have cutoff 512 (psi's entire regular action is represented by zero).
The additional delta band 130 through 512 is therefore paid separately
using the cutoff-128 smoothing bound. Output errors of these bands are not
assumed orthogonal.

### Shared centered endpoint input

The endpoint omitted-input errors have the common form

`(C - (1/2) I) sum(source_tail_i * trial_coefficient_i)`.

The same global positive-contraction bound gives D-operator norm at most
1/2 for `C - (1/2) I`. The masked input source Gram includes delta/t10 from
degree 4096 and psi/w14/v10 from degree 32768. The complete signed D-Gram
of that combination is computed before applying the common operator bound.
Its infinite tail uses the pinned RC221 source-tail Gram.

The input masks remain on the input side of the operator. No commutation
between the endpoint action and a cutoff projection is assumed.

### Remaining errors and combination

The saved additive source certificates identify the exact marginal regular
omitted-input and centered endpoint omitted-input norm terms. These terms
are subtracted from the original full column radii. Every remaining term,
including finite input quantization, regular projection and output tails,
endpoint output rounding and analytic remainders, and negative-r rounding,
remains in the eleven-column triangle-error Gram. All remainders are
nonnegative; all source cutoffs and original complete radii are checked.

For positive component weights `lambda_j`, the combined error Gram is

`(sum_j 1/lambda_j) sum_j lambda_j E_j`.

This pays arbitrary relative output directions of all four errors. The
validator optimizes only rational proposals for these weights, the remaining
column weights, and the coupled transport parameters. Every reported width
and matrix inequality is then verified with exact rational PSD arithmetic.

## An exact limit of parameter-only tuning

The centered endpoint payment dominates. RC222 saves a rational source
probe `v` for which

`v^* E_endpoint v / a >= 1.183005 v^* G_reference v`,

where `a=32125/230953`. This is a lower bound for the **payment model's
two-sided coupled enclosure width**, not for the actual operator error.

Every positive four-component Young combination is at least `E_endpoint`
in Loewner order. For admissible two-sided coupled parameters, the other
gap terms are positive semidefinite, and the complete error Gram enters
with coefficient at least `1/a`. The validator checks the necessary
base-gap and residual-Gram ordering, the selected complete error Gram's
dominance over the endpoint component, and the exact probe inequality.

Consequently parameter tuning alone cannot bring this fixed trial map and
this particular centered-endpoint payment model below 0.5. Mixed structural
endpoints, changed trial maps, and sharper endpoint error models are not
excluded. An upper error bound being costly does not prove a lower bound
on the true error or failure of the true inverse.

## Next action

RC223 should refine or explicitly realize the remaining centered endpoint
omitted inputs. Delta/t10 presently retain endpoint input only through
degree 4094, while psi/w14/v10 retain it through 32766. Extending the
delta/t10 endpoint carriers, or proving a sharper bound on their shared
omitted action, directly addresses the dominant payment. Changed nominal
centers must receive compatible new mixed/action rows; improved radii
must not be attached to old centers.

## Replay and scope

```bash
python scripts/validate_rpb108_rc222_shared_tail_error_inverse.py --output certificates/rpb108_rc222_shared_tail_error_inverse.json
python scripts/validate_rpb108_rc222_shared_tail_error_inverse.py --output certificates/rpb108_rc222_shared_tail_error_inverse.json --replay
```

Replay verifies all input/helper Git blob pins, recomputes both shared input
Grams in reverse order, reuses saved rational optimization proposals, and
compares the complete certificate, including the endpoint payment audit.
Publication adds this validator, certificate, and note without editing
existing repository files.

The accepted RC210 six-source inverse width 0.4361 and RC216 eight-source
action-error gate 0.420465 remain unchanged. There are still eight response
sources and eleven inverse trials. Actual eight-source inverse acceptance,
source-range and odd coverage, Stage I, RH, F4, and Lean closure remain open.
