# NF666 — compiler recovery of the original 15-source physical Gram endpoint

## Exact verification evidence

- NF658 corrected run 44434056814 and NF659 run 44430374282 remain successful: original 120 source enclosures and 450 integer congruence identities respectively.
- NF660 run 44437954229, NF661 run 44437952335, NF663 generic job 135306031307 (run 44446318789), and NF664 generic job 135305351619 (run 44446318889) reported successful builds and standard-axiom audits.
- NF662 job 135305535446 (run 44446318907) built the genuine oscillator/pole pilot and all 15 row modules containing all 225 individual physical-entry membership theorems. The aggregate declarations nf662AllOriginalPhysicalCompact and nf662AllOriginalTransformedRealEnclosed printed only [propext, Classical.choice, Quot.sound]. However, the aggregate file FAILED compilation at line 49 because a real division definition was not marked noncomputable; the audit stage did not run and no complete module artifact should be treated as accepted.
- NF663/664 physical attachments and the NF665 terminal job failed upstream at that NF662 aggregate definition.
- NF665 generic job 135304122071 (run 44446318876) printed standard axioms for the Frobenius estimate and four-sum exchange, but failed on the final factorization in the quadratic congruence theorem and on a nonexistent triangular determinant field. The incomplete theorems are NOT accepted; the failed build included sorryAx on the incomplete congruence statement.

## NF666 repairs

1. In the original NF662 emitter, mark its three real matrix definitions explicitly noncomputable. This preserves the exact definitions, the original physical source proofs, and the transformed interval statements. The only reported NF662 aggregate failure was the noncomputable division definition.
2. In ActualZetaOriginalPhysicalGramPreconditionerFrame.lean, explicitly isolate the finite-sum factorization, rather than allowing rw to distribute the outer product across the wrong sum.
3. Replace the nonexistent hTri.det_ne_zero_iff projection by the triangular determinant product theorem Matrix.det_of_isLowerTriangular followed by nonzero of the finite product of nonzero diagonal entries. No invertibility assumption is introduced.

All repairs are proof/elaboration and computation-annotation changes, not changes to the frozen numerical witness, original physical integral definition, or threshold.

## Terminal closure criterion

The existing NF665 theorem candidate remains:

    ∀ x : Fin 15 → ℝ,
      ((1 : ℝ) / (10 ^ 60 : ℝ)) * neutralNF661SqNorm x ≤
        neutralNF661Quadratic neutralNF661PhysicalH x

The scope is exactly the original 15 sources (0..13 and 241). A fresh successful full source build and explicit axiom audit of nf665OriginalPhysical_coercivity is required, with no sorryAx, before reporting closure. Existing NF662 and NF665 workflows cover the modified emitter and generic preconditioner module; the NF665 terminal job must rebuild NF662/663/664 and the original K frame/endpoint. The project remains draft-stacked; no merge to main. The 242-source physical system, global Weil positivity, and RH remain OPEN.
