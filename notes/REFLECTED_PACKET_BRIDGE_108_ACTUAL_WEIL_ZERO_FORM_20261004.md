# RPB108 actual conjugate-partner zero form — 2026-10-04

Definitions: [terminology registry](../docs/TERMINOLOGY_RPB108_ACTUAL_WEIL_ZERO_FORM.md).

Recovered parent: `b3585e06acd077c2d96fd2c1d97ad867290ffbda`.

The raw same-index sum from the preceding chunk is not the Weil partner pairing. The first slot must evaluate at conj(gamma(q)). The actual divisor pair q ↦ p(q) implements precisely this ordinate change and preserves analytic multiplicity. No RH assumption or extra multiplicity weight is used.

## Certified source

`WeilDefect/Arithmetic/ActualZetaWeilZeroForm.lean` defines the actual divisor pair equivalence and Z_a(v,w), then proves:

1. Partner raw square sampling is summable by reindexing the certified full-divisor square sum.
2. Partner mixed raw sampling is absolutely summable by the two square bounds.
3. Z_a has Hermitian symmetry by actual partner reindexing.
4. Its diagonal imaginary part vanishes. Positivity is not asserted.
5. Negative pair-source analysis of the canonical realization of G_a(v) equals the normalized difference of its two raw evaluations exactly.
6. This same-vector negative-source analysis is square summable over every actual divisor copy.

The logarithmic canonical vector is exactly the already constructed physical G_a(v), not a newly stipulated witness. The new form definition does not assume its identification with the arithmetic Weil form. Hermitian symmetry holds via unconditional reindexing; analytic applications additionally use the certified absolute convergence for a > 0.

## Validation

Exact candidate `1ab244918869f602a4b1ba2a9ff1283ab69b4563` passed [run 37171227339](https://github.com/monocap-tech/weil-lab/actions/runs/37171227339), job `111344423551`: isolated module 9,026 jobs; full `lake build WeilDefect` 9,059 jobs. All six theorem audits report only `[propext, Classical.choice, Quot.sound]`. The unfinished/project-axiom gate passed. The source and root import below are the exact validated contents; validation workflow and pinned manifest are excluded from research promotion.

The initial candidate `2acd7f265dfe5b5ae15b740501cf31d7c0923450` failed at two equivalence-coercion reductions. Explicit `change` reductions repaired them; no theorem premise was added.

## Cursor and residue

Next cursor: derive the convergent positive-minus-negative source decomposition of Z_a on this same constructed vector, and prove its actual arithmetic explicit-formula transport. Recover the retained WD-T38 coefficient/source dictionary and same-vector identity before using these constructed-carrier theorems on that witness. Do not replace the missing identity with a conditional representation wrapper.

WD-T38 source/null attachment, central cancellation, background completion and F-4 remain open. The retained coefficient/source dictionary and identity with G_a(v) are unproved. The typed WD-T38 record permits independently named density/Q and abstract P/C operators; the existing zero-density reindex audit prevents inferring attachment from those fields. Retained-mode spectral L²/operator-domain membership is unproved and unassumed. Full log-domain raw sampling and sharp unit-height logarithmic counts remain open. Earlier residue is preserved. SOURCE stays off the critical path; threshold stays closed. RH remains open.
