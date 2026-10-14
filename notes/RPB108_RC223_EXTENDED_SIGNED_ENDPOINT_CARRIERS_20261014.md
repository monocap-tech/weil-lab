# RC223: extended signed delta/t10 endpoint carriers

Starting head: `402fdbe0c5c2df4fe345b90cb91f3b57d9b7bb7c` (RC222).

RC223 extends the actual delta/t10 endpoint input carriers from degree
4094 to **32766**, with finite endpoint output through **65534** and a
paid signed analytic output tail. Their native source definitions, regular
actions, and exact negative-r multipliers remain unchanged.

The five endpoint omitted-input masks now start at degree 32768. On the
same fixed eleven-trial map and eight-source D-Gram reference, the centered
endpoint error component bound drops from **0.164556 to 0.002177**, a
reduction of about **98.677%**.

This is an endpoint component result, **not a new full inverse bound**.
The compatible nominal mixed/action rows must be rebuilt before inverse
acceptance can be tested with these new centers. The accepted actual
eight-source inverse enclosure remains RC222's **4.590826**, above 0.5.

## Complete individual action errors

| Quantity | Delta | t10 |
| --- | ---: | ---: |
| Previous endpoint action error upper | 4.94773e-6 | 3.66644e-5 |
| New endpoint action error upper | 4.22186e-7 | 2.77650e-6 |
| Endpoint improvement factor lower | 11.7193 | 13.2052 |
| New complete canonical action error upper | 1.17868e-5 | 1.58762e-5 |

The complete canonical radii retain the original paid regular-action errors.
The negative-r term continues to multiply the actual native source exactly.
The new endpoint radii apply only to the new endpoint centers; they are not
attached to the old RC214/RC216 nominal actions.

## Exact signed fixed-point construction

The native finite source coefficients are read from RC218's materialized
carriers. Above those finite prefixes, the same selected native analytic
moment polynomials are evaluated with directed interval arithmetic. Each
input coefficient is quantized at scale `2^48`, with its entire D-energy
quantization error recorded. The kernel is rounded at scale `2^40`.

A direct 88-bit-scale dot product cannot be assumed safe in int64. Each
signed input integer is therefore represented exactly by three base-`2^16`
limbs: two nonnegative low limbs and a signed high limb. This representation
also handles negative floor quantization of delta correctly. Every limb's
absolute dot-sum is bounded by

`max_abs_limb * kernel_scale * (max_diagonal + 2 H_input_count)`.

All six guards are below `2^63`. Kernel numerator and denominator bounds
are checked independently. NumPy computes only these bounded limb dot
products. Python integers reconstruct their exact signed result afterward.
The certificate and materialized carriers save the input-integer and
output-dot SHA256 controls, bit scales, and limb guards.

Finite output coefficient intervals include both signs of kernel rounding
error, diagonal interval uncertainty, and signed division by the D metric.
All coefficient-center rounding is paid in the D norm.

For every output degree above 65534, the exact finite input has a signed
25-moment endpoint expansion. Exact signed moments, their quantized centers,
moment-rounding error, and an absolute geometric remainder are recorded.
The centered omitted native input contributes its independently bounded
half-norm error. Input quantization, finite output rounding, analytic moment
rounding, geometric remainder, and the entire omitted input are all retained
in the complete endpoint radius.

## Matched shared endpoint budget

For `[psi0, w14, v10, delta, t10]`, the complete signed input-tail D-Gram
is now formed on the common mask of even degrees at least 32768. Its finite
part is summed through 65534 and its infinite part uses the pinned source
tail Gram. Applying `||C - (1/2) I||_D <= 1/2` gives one quarter of that
input Gram as the shared endpoint error Gram. The same fixed trial map
transports it to the same eight-source reference Gram.

An exact rational PSD width check certifies the **0.002177** component bound.
No cutoff is commuted through C, and no relative output-error orthogonality
is assumed. This removes much of RC222's dominant input-tail payment, but
does not reevaluate the full two-sided inverse payment model or claim its
half-Gram gate has passed.

## Replay and next frontier

```bash
python scripts/validate_rpb108_rc223_extended_delta_t10_endpoints.py --output certificates/rpb108_rc223_extended_delta_t10_endpoints.json --carriers certificates/rpb108_rc223_materialized_delta_t10_endpoint_carriers.json
python scripts/validate_rpb108_rc223_extended_delta_t10_endpoints.py --output certificates/rpb108_rc223_extended_delta_t10_endpoints.json --carriers certificates/rpb108_rc223_materialized_delta_t10_endpoint_carriers.json --replay
```

Replay verifies all immutable input/helper blob pins, reverses input and
output traversal, recomputes exact limb arithmetic and tail payments, and
compares both complete artifacts. Publication is add-only; existing
repository files remain unchanged.

RC224 should rebuild compatible delta/t10 mixed/action and residual rows
using these new centers, then reevaluate the shared-error eight-source
inverse. Reusing the old residual centers with the improved new action
radii would be invalid.

There are still eight response sources and eleven inverse trials. RC210's
six-source inverse width 0.4361 and RC216's eight-source action-error gate
0.420465 remain accepted and unchanged. Eight-source inverse acceptance,
source-range and odd coverage, Stage I, RH, F4, and Lean closure remain open.
