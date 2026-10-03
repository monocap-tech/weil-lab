# RPB-108 — actual zeta Jensen count bridge (2026-10-03)

Parent: `3fa5dc53c8dcd6358dff48f000e57ba3729f8dd2`.
Cursor: actual divisor count-to-growth transport.

### RPB-108: actual entire-zeta Jensen count bridge (2026-10-03)

The actual entire pole-cleared completed-zeta function
X(z) = z(z-1) completedRiemannZeta₀(z) + 1 is constructed without a
spectral L2 premise. Away from 0 and 1 it equals z(z-1) completedRiemannZeta(z).
Its analytic order at every actual open-strip zero equals the actual zeta
order, so the analytic divisor retains the exact actual multiplicity.

Actual height-window divisor cardinality is bounded by the actual analytic
divisor mass in the enclosing disk of radius |T|+2. Jensen then bounds it by
log(M_X(T))/log(2), where M_X(T) is the actual enclosing-circle supremum,
normalized to at least one. Compactness supplies the envelope bound, so this
last count theorem has no external count or shell-growth premise.

This closes the actual-divisor-to-Jensen bridge, not an explicit asymptotic
count rate or local logarithmic sampling estimate. Next: obtain an explicit
growth rate and local multiplicity count/sampling control sufficient for the
canonical logarithmic form domain, then transport the full zero-side form.

WD-T38 physical source-null attachment and enlarged central cancellation
remain open. Background completion remains retained/written; spectral L2
unproved and unassumed. Threshold closed; F-4 pending; RH standing unchanged.

See [actual zeta Jensen growth](../notes/REFLECTED_PACKET_BRIDGE_108_ACTUAL_ZETA_JENSEN_GROWTH_20261003.md).

## Proof route

1. Construct the entire function from the pinned entire completed-zeta function.
2. Prove its equality with z(z-1) times actual completed zeta away from the two endpoints.
3. Preserve the actual analytic order by the nonvanishing polynomial factor and the existing Gamma/order bridge.
4. Identify the analytic divisor at each actual strip point with its exact integer multiplicity.
5. Inject the actual finite height-window point set into the finite support of that divisor. Nonnegativity bounds the exact sum of multiplicities by the total disk divisor mass.
6. Apply pinned Mathlib `AnalyticOnNhd.sum_divisor_le` with the actual value X(0)=1 and outer radius twice the enclosing radius.
7. Define the actual enclosing-circle norm envelope and derive its finiteness/bound from compactness, removing any supplied circle-bound premise from the final count theorem.

## Next objective

Bound the actual growth envelope with an explicit rate. The pinned Hurwitz-zeta construction already exposes `HurwitzZeta.isBigO_atTop_evenKernel_sub` and `HurwitzZeta.isBigO_atTop_cosKernel_sub`, and the entire completion is a Mellin transform of the modified functional-equation kernel. These are source entrances for growth estimation, not growth-rate certificates obtained in this pass.

Keep global cumulative growth distinct from local unit-height multiplicity control. A cumulative count rate alone must not be claimed to imply the local logarithmic count bound or bounded sampling on the canonical logarithmic carrier. Infinite-divisor convergence, full Weil form extension, and retained WD-T38 coefficient/source-null identification remain separate obligations.

## Custody

Historical status records are preserved additively. The research workflow is unchanged; the validation workflow is confined to its own branch. `main` is untouched. The actual source remains on the form domain; spectral operator-domain membership is not assumed.

## Validation

Exact candidate `cefaea2a29a2a075a402e7f1061d8a9f0346fb16` passed
[run 37156729768](https://github.com/monocap-tech/weil-lab/actions/runs/37156729768),
job `111301541891`. The new module and full `lake build WeilDefect` passed
(9,003 and 9,047 jobs respectively). Thirteen public declaration audits
report only `[propext, Classical.choice, Quot.sound]`. The unfinished/project-axiom
gate passed. The new module produced no warnings in the successful run.
