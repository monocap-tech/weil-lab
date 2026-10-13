# RPB108 bounded actual Green graph lift and packet convergence — 2026-10-04

## Physical synthesis continuity

For every fixed physical L² test, the existing Green sample square summability constructs its actual full-divisor ℓ² sample vector. Testing the unchanged synthesis against that physical test equals the coefficient inner product with this vector.

Those fixed-test equations characterize the graph of physical synthesis. Each equation is closed in the coefficient/physical product topology, independently of synthesis continuity. The closed graph theorem on the complete coefficient and physical spaces therefore proves continuity of the actual synthesis.

## Full source graph continuity

The ordinary physical L² projection of the Hilbert source graph is injective: the canonical/logarithmic correspondence is injective, and both full source coefficient vectors are determined by the source graph equations.

Consequently the graph of the actual linear Green Hilbert source lift is exactly the equality set between this physical projection and the now continuous physical synthesis. It is closed. The closed graph theorem proves boundedness into the full source graph norm, without stipulating a source bound or replacing either source vector.

The resulting operator norm bounds the graph norm of every unchanged Green lift.

## Actual finite packet convergence

The existing ℓ² coordinate HasSum expansion is transported through the proved continuous full source lift. The Green lifts of actual single-coordinate coefficient vectors therefore have unordered finite sums converging to the original lift in the full source graph topology.

This controls the logarithmic physical coordinate and both complete source vectors together. Physical convergence alone was insufficient for that statement.

## Certification

- Module: `WeilDefect/Arithmetic/ActualZetaGreenGraphPackets.lean`.
- Candidate: 77f6e55a4f0eb1fb2be19e121ee01d5a35dc57cd.
- Passed [run 37215507755](https://github.com/monocap-tech/weil-lab/actions/runs/37215507755), job 111475079660.
- Lean 4.34.0; isolated 9164/full 9195 build jobs.
- Seven theorem axiom audits, each exactly [propext, Classical.choice, Quot.sound].
- Unfinished trusted-declaration gate passed.
- Saved validation cache: rpb108-actual-green-graph-packets-verified-v1.
- The promoted module and root import are the exact tested contents.

## Scope and residue

This establishes actual graph packet convergence for every constructed Green lift. The separate closed-span identification and arbitrary retained membership/full-density obligations remain. No explicit quantitative truncation rate or bounded inverse is claimed.

Source/null attachment, central cancellation, unshifted background positivity, contractive WD-T10 factorization, background completion, boundary removal and F-4 remain open.

Next cursor: Identify the actual Green closed graph subspace with the closure of finite actual-divisor packets using the newly proved graph-topology HasSum expansion; then prove the needed lawful retained membership or full density/extension without assuming it. The unchanged Green Hilbert source lift is now proved bounded by closed graph, and every coefficient vector expands into actual single-coordinate packets converging in the full graph norm. Physical synthesis continuity is proved from fixed-test ℓ² duality, and source physical uniqueness identifies the full lift graph. The actual closure remains a complete Hilbert subspace; no equality with the entire source graph or logarithmic carrier is proved. Retained same-vector P/C/k graph membership and source/null identity, fixed-packet orbit/multiplicity custody and central cancellation remain independent. Actual unshifted effective-background positivity/contractive WD-T10 factorization is not implied by shifted Gårding control. No concrete WD-T38 constructor application was recovered in the prior pinned 152-file scan. Background completion, boundary removal and F-4 remain open; SOURCE is off the critical path.
