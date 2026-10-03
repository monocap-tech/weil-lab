# RPB-108 — actual theta growth ingredients (2026-10-03)

Parent: `68ea26911c742bcd9e5023ded7014273ea4975e5`.
Continues the certified actual-divisor/Jensen bridge.

### RPB-108: actual theta exponential and factorial moment bounds (2026-10-03)

The actual zero-parameter even theta remainder is now bounded by
C exp(-p t) for all t ≥ 1, with positive p and C obtained from the
actual kernel. Pinned exponential decay supplies the tail; continuity
and compactness supply the finite initial interval.

For every natural n, its polynomially weighted absolute value is bounded
by C n!/(p/2)^n exp(-(p/2)t). All moments on (1,∞) are integrable,
with the same actual constants and the explicit bound
C n!/(p/2)^n exp(-p/2)/(p/2). No divisor-count, shell-growth, or
spectral-domain premise is supplied.

Next: connect these actual moments to the completed-zeta complex Mellin
weights and prove an explicit rate for the existing actual circle
envelope. This chunk does not prove that envelope rate, local unit-height
logarithmic counts, infinite sampling boundedness or full Weil-form extension.

WD-T38 coefficient/source-null attachment and enlarged central cancellation
remain open. Background completion remains retained; spectral L2 unproved
and unassumed. Threshold closed; F-4 pending; RH standing unchanged.

See [actual theta growth](../notes/REFLECTED_PACKET_BRIDGE_108_ACTUAL_THETA_GROWTH_20261003.md).


## Proof route

1. Use the pinned actual `HurwitzZeta.isBigO_atTop_evenKernel_sub 0` decay theorem.
2. Extract positive actual decay constants and an eventual threshold.
3. Bound |K(t)| exp(p t) on the compact finite initial interval by continuity.
4. Combine initial and tail bounds, retaining the same p and a larger positive C.
5. Apply the real exponential-series term bound to (p/2)t: polynomial growth is bounded by n!/(p/2)^n exp((p/2)t).
6. Retain half of the actual decay in the polynomial majorant.
7. Prove moment integrability by measurable domination, then integrate the exponential majorant explicitly.

The source imports Mathlib's actual zeta construction directly. It does not
depend on any WD representation module or supplied divisor estimate.

## Restart cursor

Use the actual completed-zeta Mellin construction to dominate complex
weights on a radius-R circle by an actual theta moment of order proportional
to R. The factorial majorant is intended to give log envelope O(R log R).
This comparison and the resulting rate remain unproved here.

A cumulative O(T log T) count bound must not be promoted as a local
O(log T) unit-height multiplicity bound or bounded logarithmic-domain
sampling theorem. Keep those obligations distinct.

## Custody

The source and terminology are promoted separately from the validation
workflow. Historical records are unchanged except for additive updates.
The retained WD-T38 source identification is not assumed, and no spectral
operator-domain membership is introduced.

## Validation

Exact candidate `5ee1aa9ace2f8f652d89d9b3961ef1f6177e5926` passed
[run 37159106688](https://github.com/monocap-tech/weil-lab/actions/runs/37159106688),
job `111308606670`. The isolated module and full `lake build WeilDefect`
passed (3,204 and 9,048 jobs). All four new public declaration audits
report only `[propext, Classical.choice, Quot.sound]`. The unfinished/project-axiom
gate passed. Source and root import are promoted without the validation workflow.

The validation runner retained compiled dependencies under
`rpb108-theta-growth-verified-compiled-v1` for the next bounded proof chunk.
