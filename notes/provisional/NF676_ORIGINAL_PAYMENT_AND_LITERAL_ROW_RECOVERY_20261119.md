# NF676 — original numerical custody recovery and isolated literal row replay

## Actual compiler evidence

NF674 run 44470828909, job 135379584139:
- OriginalPhysicalFullQuadratic built successfully. The three previously failed declarations nf670AssembleOriginal_roundtrip, nf670FullPhysicalGram_blockEnergy, nf670FullPhysicalGram_allCoefficients printed only [propext, Classical.choice, Quot.sound].
- OriginalPhysicalRieszResponse failed on lines 34, 78 and 104. Matrix.mulVec_apply_eq_sum did not rewrite the real matrix row expression; downstream prints contained sorryAx. The complete Riesz/Schur result is not accepted.
- The separate NF674 row gate emitter test passed (job 135379585511).

NF673 job 135370275766, NF674 job 135379584712, and NF675 jobs 135385073928/135385074349 failed at the SAME inherited NF626 integer-payment theorem NF626CenterCache.defect_eq, which had parser and unsolved-goal errors near lines 79–85. This was not a negative result for the original numerical comparisons.

NF675 actual original source reconstruction succeeded before the Lean build (job 135385073928): the emitter reported 67 original source moment keys, and the immutable NF631 archive digest and eight NF621 shard/source hashes matched. The actual numerical check was additionally blocked by an incorrect generated import path WeilDefect.Generated.NF627.Bank for files generated in WeilDefect/Generated/NF675.

## Repairs on NF676 head

1. Replace the erroneous chained tactic in NF626CenterCache.defect_eq by explicit equality and inequality index cases. Diagonal uses exact cast/sub_div/div_self under the existing positive denominator hypothesis; off-diagonal uses explicit integer zero cast and sub_div. No numerical predicate, constants, or assumptions are changed.
2. Use the exact finite row definition of Matrix.mulVec in the actual 15-source Riesz row-action theorem, and explicitly transport existence and uniqueness through that theorem.
3. Make the two three-part Boolean conjunction groupings explicit, and replace tactic-dependent List.all congruence in the NF675 row projection with pointwise function equalities.
4. Fix the NF675 emitter's internal NF627 module prefix to the isolated NF675 namespace, including the import of the generated Bank, and update generated bank file hashes. No archived numerical literals or bounds are altered.
5. Move only executable NF673/NF674 checker definitions into ActualZetaOriginalPhysicalExecutableEntryChecks.lean. The literal first-row gate now imports those definitions instead of the downstream integer-payment or projection proof. NF673/NF674 conditional soundness and NF675 projection theorems remain separate. The underlying NF625 original comparator is unchanged.

## Verification

The NF676 workflow has four independent jobs: literal archived row decision and axiom audit; exact row projection; repaired integer payment and terminal signed-carrier conditional theorem soundness; pinned full original Riesz/Schur replay. The original row test no longer depends on the success of the downstream integer payment/Riesz proofs. Failed numeric gates must remain failed.

Every new repair is compiler pending until the new run finishes. The clean original full 242-source block identity is already accepted in the prior NF674 build, but Riesz, source-specific Schur positivity, first-row Boolean truth, and the full linked original data gate truths remain open. First-row proof alone cannot prove complete bank validity/coverage or transfer to the full original payment without the necessary equality checks. No unconditional Phase III closure, global Weil positivity, or RH claim.

Next: check the isolated literal row and the earliest failed proof, if any. Then instantiate genuine full-bank/coverage and complete original payment gates with independent source receipts.
