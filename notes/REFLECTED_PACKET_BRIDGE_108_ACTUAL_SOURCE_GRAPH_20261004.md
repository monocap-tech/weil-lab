# RPB108 actual full-divisor source graph — 2026-10-04

## Definitions and construction

The source ambient space is the logarithmic Hilbert carrier together with two full actual-divisor ℓ² coefficient vectors. The source graph requires every positive and negative coefficient, including multiplicity copies, to equal the corresponding Hilbert source sample of the same first coordinate.

The graph is a complex submodule. It is closed because each scalar sampling equation equates two continuous functions: coordinate evaluation in ℓ² and evaluation against the fixed logarithmic Hilbert source. Its inherited product norm is a source graph norm. The closed graph is complete in that norm.

Positive and negative analysis are actual continuous linear projections from this concrete graph to actual-divisor ℓ². Their vector norms are bounded by the graph vector norm. This does not establish a uniform ℓ² analysis bound in the original logarithmic carrier norm.

Every previously constructed canonical Green vector has a graph lift. The lift uses the already proved complete positive and negative square summability; it preserves the original logarithmic coordinate exactly. The difference of squared coefficient norms on this lift equals twice the native signed Weil quadratic with the certified physical cross-pole moments. Full-divisor partner multiplicity explains the factor two.

## Certified code

- Module: `WeilDefect/Arithmetic/ActualZetaSourceGraph.lean`.
- Root imports the new module.
- Validation candidate: e7723a82cb2d95f51a72d471a7d808fe4ae5e40a.
- Passed run: 37182835373; job: 111378676050.
- Isolated module and full root compiled with Lean 4.34.0.
- Six audited declarations: graph closure, domain completeness, source sampling, analysis norm bounds, Green-lift physical custody, and coefficient/native-quadratic normalization.
- Axiom audit: all six are exactly [propext, Classical.choice, Quot.sound].
- The unfinished trusted-declaration gate passed.

## Scope and residue

This supplies a complete graph domain and continuous actual P/N coefficient maps, rather than assuming an actual source representation. The physical image is not claimed closed, dense, exhaustive, or equal to the abstract retained carrier. Completeness uses the source graph norm, not the original carrier norm. The native arithmetic/form identity is proved on lifted Green vectors; extension to all graph vectors remains unproved. No spectral operator-domain membership follows.

The WD-T38 constructor's retained unit-gain and physical-adjoint proofs survive unchanged. The previous pinned 152-file scan recovered no concrete constructor application. The abstract P/C/k still require actual identification; this graph does not supply retained k membership.

Next cursor: construct the normalized finite-selected negative/background split from the certified full actual-divisor source graph, and realize the effective-positive construction on a lawful complete source/form domain. The graph has bounded full P/N coefficient maps and contains all constructed Green vectors, whose norm difference is twice the native Weil quadratic. Its completeness is in the source graph norm; the physical image is not claimed closed or equal to the whole logarithmic carrier. Prove any needed density, Hilbert/form completion and native-form extension, and retained k membership/same-vector source/null identification before invoking WD-T38. No concrete WD-T38 application was recovered by the pinned 152-file scan. Central cancellation, background completion, boundary removal and F-4 remain open; SOURCE is off the critical path.
