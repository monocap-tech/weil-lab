# RPB108 compact L² correlation transform — 2026-10-04

Definitions: [compact correlation terminology](../docs/TERMINOLOGY_RPB108_ACTUAL_CORRELATION_TRANSFORM.md).
Parent: `9231c4d7496c13a33ecf8125124f08d1b0826c8c`.

## Certified result

The new module `WeilDefect/Arithmetic/ActualZetaCorrelationTransform.lean` defines W_a(f), the exact compact representative, K_a(f,g), the mixed conjugate-reflected correlation, and H(k,z), the full-line positive-exponent raw transform.

For any physical L² inputs f,g, W_a(f) has integrable exponential twists for every complex z. This is proved from local L¹ integrability of L², restriction to the compact finite window, and continuous exponential weighting. Conjugation and reflection preserve the requisite integrability. The mixed correlation is integrable and vanishes pointwise outside [-2a,2a], so it has compact support.

Direct convolution integration gives the all-complex dictionary

`H(K_a(f,g),z) = conj(E_a(conj z,f)) * E_a(z,g)`.

This includes nonreal z. It is not the positive same-index square formula. No smoothness or critical-line premise is used in this identity.

For the actual supported Green vector, W_a(G_a(v)) equals G_a(v) almost everywhere, using the already certified support theorem. Substituting two actual Green syntheses in the dictionary identifies every actual-divisor correlation transform sample with the partner pairing. Thus those samples are absolutely summable for a > 0 and their sum is exactly Z_a(v,w), the previously certified zero-side form. The preceding 2 Z = P - N source decomposition now belongs to this explicit compact correlation kernel.

Eight public theorems:

- `neutralActualZetaGreenSynthesis_windowRepresentative_ae`
- `neutralWindowRepresentative_twist_integrable`
- `neutralWindowCorrelation_supported`
- `neutralWindowCorrelation_hasCompactSupport`
- `neutralWindowCorrelation_integrable`
- `neutralWindowCorrelation_rawTransform`
- `neutralActualZetaGreenCorrelation_samples_summable`
- `neutralActualZetaGreenCorrelation_zeroForm`

## Validation

Exact candidate `b9023a73373a02696ed92ebbfaaacde9a80b0df0` passed [run 37172964116](https://github.com/monocap-tech/weil-lab/actions/runs/37172964116), job `111349539339`: isolated module 9,028 jobs; full `lake build WeilDefect` 9,061 jobs. All eight public theorem audits report only `[propext, Classical.choice, Quot.sound]`; the unfinished/project-axiom gate passed. The compiled dependency cache was saved. The promoted source and root import match the exact validated contents; workflow and pinned manifest remain validation-only.

Candidate `ba674fcbbf451c6765ac7bf5502cd0f38c012963` exposed explicit Lp/conjugation APIs and reflected-integral rewriting issues. Candidate `9a125ad27c41b110ff578c8c51a903041016f3ee` fixed all but the change-of-variables rewrite. An explicit `integral_neg_eq_self` equality completed the exact successful candidate above. No mathematical premise was added. Cache primary plus fallback keys total at most ten.

## Remaining explicit-formula boundary

Compact support and integrability do not establish the `ContDiff ℝ 2` premise of the recovered external EF_lit theorem. H¹ regularity of the inputs is available, but C² regularity of this correlation has not been certified. The alternative is smooth approximation with a justified limit on both sides. The external theorem export is a `sorry` statement stub; the separately recovered accepted solution body requires its proof-bearing transitive dependency closure. The preceding [source decomposition note](REFLECTED_PACKET_BRIDGE_108_ACTUAL_SOURCE_DECOMPOSITION_20261004.md) retains the exact retrieval inventory. This module depends only on certified weil-lab modules and Mathlib convolution, not that external export.

## Cursor and residue

Next cursor: certify C² regularity of the compact mixed correlation K_a(G_a(v),G_a(w)), or supply a smooth approximation with justified passage in both the zero-side and arithmetic forms. The raw-transform product and actual-divisor zero-sum dictionaries are now proved; do not reintroduce them as hypotheses. Recover and audit the external EF_lit_zeta proof-bearing dependency closure under Lean/Mathlib 4.34.0, then attach the exact pole and prime/digamma symbol terms on this same carrier. Recover the retained WD-T38 coefficient/source dictionary and prove the same-vector source/null identity before transferring these constructed-carrier results to that witness. No conditional representation wrapper discharges that identity.

WD-T38 source/null attachment, central cancellation, background completion and F-4 remain open. The retained coefficient/source dictionary and identity with the constructed G_a(v) are unproved. The typed WD-T38 record still permits independently named density/Q and abstract P/C operators; the zero-density reindex audit blocks inferring a physical source identity from those fields. Retained-mode spectral L²/operator-domain membership is unproved and unassumed. Sharp unit-height logarithmic counts and full log-domain raw sampling remain open. Earlier residue is preserved. SOURCE stays off the critical path; threshold stays closed; RH remains open.
