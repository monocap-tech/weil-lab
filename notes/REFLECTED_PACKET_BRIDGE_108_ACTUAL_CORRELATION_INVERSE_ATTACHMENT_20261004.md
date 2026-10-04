# RPB108 compact C² inverse correlation attachment — 2026-10-04

Definitions: [inverse attachment terminology](../docs/TERMINOLOGY_RPB108_ACTUAL_CORRELATION_INVERSE_ATTACHMENT.md).
Parent: `f4a0636db646e509eba4df9dee8754ec15a465fd`.

## Certified result

The new module `WeilDefect/Arithmetic/ActualZetaCorrelationInverseAttachment.lean` proves that the concrete inverse spectral integral J_a(v,w) agrees almost everywhere with the exact compact mixed correlation K_a(G_a(v),G_a(w)).

The proof uses inverse Fourier integral duality against Schwartz tests, the previously proved correlation spectrum identity, ordinary Fourier duality and Schwartz inversion. Uniqueness from compact smooth tests then identifies the two locally integrable functions. The inverse representative is continuous because its C² regularity was already derived. On the open complement of [-2a,2a], the identity and original correlation support give almost-everywhere vanishing. Positivity of volume on open sets and continuity promote this to pointwise exterior vanishing, hence compact support.

Thus J_a(v,w) now has both the ContDiff ℝ 2 and HasCompactSupport properties demanded by the recovered external explicit-formula statement. It is a proved representative of the same correlation, rather than a separately introduced test function with a supplied representation premise.

The almost-everywhere identity transfers every complex raw-transform sample to J. In particular, its actual-divisor samples converge absolutely and their sum is exactly Z_a(v,w). The two pole samples retain the exact cross-pole operator identity on the existing canonical images of G_a(v), G_a(w). All previous normalizations and partner conjugation are preserved.

Eight public theorems:

- `neutralActualZetaGreenCorrelationInverse_ae`
- `neutralActualZetaGreenCorrelationInverse_supported`
- `neutralActualZetaGreenCorrelationInverse_hasCompactSupport`
- `neutralActualZetaGreenCorrelationInverse_integrable`
- `neutralActualZetaGreenCorrelationInverse_rawTransform`
- `neutralActualZetaGreenCorrelationInverse_samples_summable`
- `neutralActualZetaGreenCorrelationInverse_zeroForm`
- `neutralActualZetaGreenCorrelationInverse_poleOperator`

## Validation

Exact candidate `00fc201d445a63a1e3d645bba08d4ea9770a0fac` passed [run 37175481356](https://github.com/monocap-tech/weil-lab/actions/runs/37175481356), job `111357103024`: isolated module 9,032 jobs; full `lake build WeilDefect` 9,065 jobs. All eight public theorem audits report only `[propext, Classical.choice, Quot.sound]`; the unfinished/project-axiom gate passed. The promoted source and root import match the exact validated contents. Workflow and pinned manifest remain validation-only.

Validation repairs made the inverse Schwartz coercion, bilinear flip symmetry, restricted-measure predicate and open-set uniqueness API explicit. Candidates `b1745bc3db075b6c8aadda3b111b7283b78fdb2b`, `eda3dea18839e347cb3655682c24d96f5b706bf3`, `11bde9baa1cac66285b095ec943c80d9520ebaea` and `073a5257cf405731b3ad24eee785293b728c6997` exposed those elaboration/reduction details. The final proof uses real_inner_comm directly rather than reducing the inner pairing to a scalar representation. No mathematical premise was added.

## Explicit-formula boundary

The compact C² admissibility and inverse identity are now closed for this constructed carrier. The external EF_lit_zeta theorem is still not imported: its published theorem file is a statement stub, and the recovered accepted solution body needs its proof-bearing transitive dependency closure audited under Lean/Mathlib 4.34.0. Its actual zero-configuration/multiplicity correspondence and the prime/digamma form dictionary also remain to be attached.

This result does not identify the retained WD-T38 mode with the constructed Green synthesis. That requires its retained coefficient/source dictionary and same-vector source/null identity.

## Cursor and residue

Next cursor: recover and audit the external EF_lit_zeta proof-bearing dependency closure under Lean/Mathlib 4.34.0, then apply the trusted explicit formula to J_a(v,w), the now-certified compact C² representative of the exact Green correlation. Compact C² admissibility, all-complex sample equality, actual-divisor absolute convergence and exact zero-side sum, and same-canonical-image pole operator identity are now proved; do not reintroduce them as hypotheses. Prove the actual zero-configuration/multiplicity correspondence required by the external theorem and attach the exact prime/digamma symbol terms on this same carrier. Recover the retained WD-T38 coefficient/source dictionary and prove the same-vector source/null identity before transferring these constructed-carrier results to that witness. No conditional representation wrapper discharges that identity.

WD-T38 source/null attachment, central cancellation, background completion and F-4 remain open. The retained coefficient/source dictionary and identity with the constructed G_a(v) are unproved. The typed WD-T38 record still permits independently named density/Q and abstract P/C operators; the zero-density reindex audit blocks inferring a physical source identity from those fields. Retained-mode spectral L²/operator-domain membership is unproved and unassumed. Sharp unit-height logarithmic counts and full log-domain raw sampling remain open. Earlier residue is preserved. SOURCE stays off the critical path; threshold stays closed; RH remains open.
