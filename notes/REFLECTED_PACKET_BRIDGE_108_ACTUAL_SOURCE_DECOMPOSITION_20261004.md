# RPB108 full-divisor source decomposition — 2026-10-04

Definitions: [source decomposition terminology](../docs/TERMINOLOGY_RPB108_ACTUAL_SOURCE_DECOMPOSITION.md). Parent cursor: `9f2276e7f50f501f92e0922fc1b0fd037904bf12`.

## Certified same-vector identity

The earlier canonical logarithmic realization L_a(v) has physical realization exactly G_a(v), the actual supported H¹ Green synthesis. The new module `WeilDefect/Arithmetic/ActualZetaSourceDecomposition.lean` attaches the existing positive source to this same vector; its negative source was already attached in the preceding chunk.

Both full-divisor source analyses have summable norm squares. Both mixed source forms converge absolutely, by the sum of their two square bounds. The source forms include every actual analytic multiplicity copy.

Pointwise positive-minus-negative source diagonalization retains both cross terms. Reindexing by the certified actual divisor pair identifies their sums. Thus

`2 * neutralActualZetaGreenZeroForm a v w = neutralActualZetaGreenPositiveForm a ha v w - neutralActualZetaGreenNegativeForm a ha v w`.

The factor 2 is essential: the divisor sum counts both partner members, without choosing one representative per orbit. Partner-fixed points also satisfy the identity. On the diagonal, twice the real zero-side value is the difference of the two convergent real source energies. No positivity or critical-line claim follows from this identity.

Seven public theorems:

- `neutralActualZetaGreenCanonical_positiveSource_sampling`
- `neutralActualZetaGreenCanonical_positiveSource_sq_summable`
- `neutralActualZetaGreenCanonical_positiveSource_mixed_summable`
- `neutralActualZetaGreenCanonical_negativeSource_mixed_summable`
- `neutralLogPairSource_mixed_difference`
- `neutralActualZetaGreenZeroForm_source_decomposition`
- `neutralActualZetaGreenZeroForm_source_energy`

## Validation

Exact candidate `09adad3b22105e45feeae99b49ed955fe9cbc3b9` passed [run 37172170322](https://github.com/monocap-tech/weil-lab/actions/runs/37172170322), job `111347187543`: isolated module 9,027 jobs; full `lake build WeilDefect` 9,060 jobs. All seven public theorem audits report only `[propext, Classical.choice, Quot.sound]`; the unfinished/project-axiom gate passed. The successful workflow saved its compiled dependency cache. Research promotion includes the exact validated source and root import, excluding the validation workflow and pinned manifest.

Candidate `a11a633fe3e5ca9c4ec6169c35c6dc787d3ad517` exposed normalization/conjugation rewrites and sum-binder scope issues. It also exceeded the cache action's ten-key limit, causing an uncached rebuild. Candidate `3498ab2805716e6a4ec209399021723f167229ba` repaired those issues and left only a redundant `rfl` after an already-closing rewrite. Removing it produced the exact successful candidate above; no mathematical premise was added. Keep the primary cache key plus fallback keys at most ten in future validation edits.

## Recovered explicit-formula boundary

The Formalpedia theorem export [Thm_Zeta23_WeilEF_EF_lit_zeta.lean](https://github.com/prove2me/formalpedia/blob/main/envs/0df444a/Theorems/Thm_Zeta23_WeilEF_EF_lit_zeta.lean) states the theorem with a `by sorry` stub despite metadata marking it Proved. Its separate accepted [solution body](https://github.com/prove2me/formalpedia/blob/main/envs/0df444a/Solutions/Sol_Zeta23_WeilEF_EF_lit_zeta.lean), submission [3baa154b-f40d-4423-bff3-ae84616db32e](https://prove2.me/submissions/3baa154b-f40d-4423-bff3-ae84616db32e), was recovered during this chunk. That body contains no `sorry` or `axiom` declarations but imports 13 project theorem modules, whose exported statements cannot substitute for their proofs. A theorem status label is not the local trust certificate.

The retrieved definition `Zeta23.EF.EF_lit` requires `ContDiff ℝ 2 k` and `HasCompactSupport k`; its conclusion is multiplicity-weighted actual-zero summability plus the literal prime/pole/digamma formula. The current supported H¹ Green vector is not automatically a C² test function. A lawful route must certify the mixed correlation/test regularity (or smooth approximation and continuous passage), its raw-transform product dictionary, the zero/multiplicity indexing dictionary, and the arithmetic symbol/pole dictionary, then audit the proof-bearing EF dependency closure under Lean/Mathlib 4.34.0. None of these missing obligations is inserted as a new axiom or a conditional representation layer here.

Immediate top-level imported theorem modules in the recovered solution:

- Theorems.Thm_Zeta23_RvM_zeta_local_zero_count
- Theorems.Thm_Zeta23_WeilEF_EF_zero_sum_summable_gen
- Theorems.Thm_Zeta23_WeilEF_Hfn_mirror
- Theorems.Thm_Zeta23_WeilEF_continuous_logDeriv_zeta_line
- Theorems.Thm_Zeta23_WeilEF_differentiableAt_GammaR
- Theorems.Thm_Zeta23_WeilEF_differentiable_paperFT
- Theorems.Thm_Zeta23_WeilEF_full_line_identity
- Theorems.Thm_Zeta23_WeilEF_gammaR_bracket
- Theorems.Thm_Zeta23_WeilEF_gamma_line_shift
- Theorems.Thm_Zeta23_WeilEF_integrable_mul_logDeriv_GammaR_of_decay
- Theorems.Thm_Zeta23_WeilEF_norm_Hfn_le
- Theorems.Thm_Zeta23_WeilEF_norm_logDeriv_zeta_le_of_one_lt_re
- Theorems.Thm_Zeta23_WeilEF_prime_side_line

These are a retrieval inventory, not a claim that the transitive closure has been certified in weil-lab. The source decomposition module imports only the earlier certified weil-lab module and does not depend on this external formula.


## Next cursor and residue

Next cursor: actual arithmetic explicit-formula transport of the now decomposed partner zero-side form. First certify the compact mixed correlation/test regularity and raw-transform product dictionary on the constructed supported H¹ class, and recover/audit the proof-bearing explicit-formula dependency closure under Lean/Mathlib 4.34.0. Then identify the actual zero/multiplicity and arithmetic symbol/pole dictionaries. In parallel with that mathematical cursor, recover the retained WD-T38 coefficient/source dictionary and prove the same-vector identity before applying the constructed-carrier results to that witness. No conditional representation wrapper discharges this identity.

WD-T38 source/null attachment, central cancellation, background completion and F-4 remain open. The retained coefficient/source dictionary and identity with the constructed G_a(v) are unproved. The typed WD-T38 record still permits independently named density/Q and abstract P/C operators; the zero-density reindex audit blocks inferring a physical source identity from those fields. Retained-mode spectral L²/operator-domain membership is unproved and unassumed. Sharp unit-height logarithmic counts and full log-domain raw sampling remain open. Earlier residue is preserved. SOURCE stays off the critical path; threshold stays closed; RH remains open.
