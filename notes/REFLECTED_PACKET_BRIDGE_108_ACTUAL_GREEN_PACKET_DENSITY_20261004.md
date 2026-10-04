# RPB108 exact actual packet closed span — 2026-10-04

## Actual columns and scalar custody

Each packet column is the existing Green Hilbert source lift of the actual unit-coordinate coefficient vector. Every divisor multiplicity copy retains its own index. Linearity proves that a packet with coefficient c is c times that same unit packet column.

The finite packet span is the complex linear span of these actual columns. Its closure uses the full source graph topology, controlling both complete source vectors and the logarithmic physical coordinate.

## Exact closed-span identification

The previously certified full-graph HasSum expansion places every actual Green lift in the closed finite packet span. Conversely, every packet column is an actual Green lift and hence belongs to the already certified Green graph closure. Closed-submodule minimality in both directions proves equality of the packet closed span with the actual Green closed submodule.

This is concrete packet density inside the certified Green subspace. It does not identify that subspace with the full source graph or logarithmic physical carrier.

## Concrete orthogonal-complement tests

A source graph vector is orthogonal to every vector in the Green graph closure if and only if it is orthogonal to each actual packet column. The reverse direction follows by linearity of the inner-product functional and closedness of its kernel.

This gives concrete equations for the remaining orthogonal complement. It does not prove that complement is zero or place an arbitrary retained vector in the subspace.

## Certification

- Module: `WeilDefect/Arithmetic/ActualZetaGreenPacketDensity.lean`.
- Candidate: d23f13474f1a9497533e9a96b01185c96276e150.
- Passed [run 37217789105](https://github.com/monocap-tech/weil-lab/actions/runs/37217789105), job 111481758174.
- Lean 4.34.0; isolated 9165/full 9196 build jobs.
- Five theorem axiom audits, each exactly [propext, Classical.choice, Quot.sound].
- Unfinished trusted-declaration gate passed.
- Saved validation cache: rpb108-actual-green-packet-density-verified-v1.
- The promoted module and root import are the exact tested contents.

## Scope and residue

Finite-packet closed-span identification is now proved. Lawful retained membership, full-density/extension if needed, source/null attachment, central cancellation and unshifted background positivity remain independent. Background completion, boundary removal and F-4 remain open.

Next cursor: Prove lawful retained same-vector membership/source-null attachment or the needed full density/extension from concrete actual packet tests. Finite actual-divisor packet columns now have closed span exactly equal to the actual Green graph closure, with both source coordinates preserved; orthogonality to that closure is equivalent to orthogonality to every actual packet column. The orthogonal complement is not proved zero, and no equality with the entire source graph or logarithmic carrier is asserted. The unchanged Green Hilbert source lift is bounded and its actual coordinate packets converge in the full graph norm. Retained same-vector P/C/k graph membership and source/null identity, fixed-packet orbit/multiplicity custody and central cancellation remain independent. Actual unshifted effective-background positivity/contractive WD-T10 factorization is not implied by shifted Gårding control. No concrete WD-T38 constructor application was recovered in the prior pinned 152-file scan. Background completion, boundary removal and F-4 remain open; SOURCE is off the critical path.
