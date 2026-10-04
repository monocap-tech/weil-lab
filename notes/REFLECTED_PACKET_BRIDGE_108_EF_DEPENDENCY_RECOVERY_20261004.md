# RPB108 explicit-formula dependency recovery — 2026-10-04

Parent research commit: `ff550378b62854d3174f2573fa601dd374d5025a`.
Machine-readable custody: [dependency manifest](../docs/EF_LIT_ZETA_DEPENDENCY_MANIFEST.json).

## Recovered closure

The literal explicit-formula solution is pinned to prove2me/formalpedia commit `ae3af9184af2e274c721b1cf3b0dffa09af02c6c`, environment `0df444a`. Its accepted submission is [3baa154b-f40d-4423-bff3-ae84616db32e](https://prove2.me/submissions/3baa154b-f40d-4423-bff3-ae84616db32e).

All 13 direct theorem imports were fetched and inspected: each published Theorems file ends in `by sorry`. Each has a separate accepted Solutions body. Following the Solutions bodies' Theorems and Definitions imports recursively closes at **84 accepted proof bodies and 30 definition files**, 114 files total. There are no missing nodes, unresolved project imports or import cycles in this recovered closure. All other imports are Mathlib or Batteries. The retrieved UTF-8 sources total 958 KB approximately.

The manifest records the immutable source path, SHA-256, UTF-8 byte count, accepted receipt, expected export, direct project imports and dependency-first order for every file. Each of the 84 proof bodies declares a generic `solution` theorem; importing those files unchanged would not replace the theorem names demanded by their consumers. A port must rename each final export to the recorded declaration and supply it under the corresponding theorem module path. The published statement stubs must never enter the trusted build.

A nested-comment/string-aware lexical scan of every recovered source found no executable `sorry`, `admit`, `axiom` or `sorryAx` token. Mentions in comments were excluded, including the Hypotheses file's explanation of its Prop-valued fields. This is a source audit only: it does not establish elaboration, compatibility, theorem-type equality or kernel trust. The closure has not yet been compiled under our Lean/Mathlib 4.34.0. Accepted submission metadata is not a substitute for that validation.

| Proof family | Bodies |
| --- | ---: |
| WeilEF | 44 |
| RvM | 7 |
| DigammaSeries | 7 |
| Stirling | 7 |
| Rectangle/residue | 2 |
| Other supporting results | 17 |
| Total | 84 |

There are 37 proof leaves with no project theorem imports. Definitions may still be required. Start port validation in dependency-first order; audit the final literal explicit formula and any public local bridges with `#print axioms`. Definition-only Prop fields do not themselves discharge a theorem premise; check the final theorem's actual arguments rather than its imported namespace.

## Certification boundary

No Lean source or root import changed in this audit chunk. The last certified mathematical result remains the compact C² same-correlation attachment at `ff550378b62854d3174f2573fa601dd374d5025a`, validated by [run 37175481356](https://github.com/monocap-tech/weil-lab/actions/runs/37175481356). No new Lean build is claimed for the recovered external sources.

J_a(v,w) already satisfies compact C² admissibility; its all-complex sample equality, actual-divisor absolute convergence and zero sum, and pole identity on the exact canonical Green images are proved. Keep these results, rather than adding them as input hypotheses. The actual-zero configuration/multiplicity correspondence and exact prime/digamma arithmetic-form dictionary still require proofs after the external theorem is certified.

## Cursor and residue

Next cursor: port the fully recovered EF_lit_zeta import closure in docs/EF_LIT_ZETA_DEPENDENCY_MANIFEST.json to Lean/Mathlib 4.34.0, using its dependency-first order and all 84 recorded export mappings. Replace every theorem stub with its pinned accepted solution body, rename the generic solution export to the recorded declaration, and compile/audit the resulting theorem before importing it. The recovered closure comprises 84 proof bodies and 30 definition files; lexical hole scan is clean, but compiler/axiom validation remains open. Then prove actual-zero/multiplicity correspondence and apply EF to the already certified compact C² inverse correlation J, attaching prime/digamma terms on the same carrier. Retained WD-T38 coefficient/source and same-vector source/null identity remain required.

WD-T38 source/null attachment, central cancellation, background completion and F-4 remain open. The retained coefficient/source dictionary and identity with the constructed Green synthesis remain unproved. The zero-density reindex audit prevents inferring a physical source identity from independently named density/Q fields. Retained-mode spectral L²/operator-domain membership is unproved and unassumed. Sharp unit-height logarithmic counts and full log-domain raw sampling remain open. Earlier residue is preserved. SOURCE stays off the critical path; threshold stays closed; RH remains open.
