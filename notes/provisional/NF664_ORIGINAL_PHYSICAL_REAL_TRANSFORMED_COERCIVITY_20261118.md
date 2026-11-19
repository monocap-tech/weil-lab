# NF664 — actual original physical transformed real Gram coercivity

## Verified compiler recovery

- **NF658 corrected workflow 44434056814**: SUCCESS including final Lean standard axiom audit. 120 authentic compact physical entry enclosures accepted.
- **NF659 workflow 44430374282**: SUCCESS including 225 exact integer transformed center gates, 225 exact radius gates, 15 integer margins, exact `10^-60` coercivity integer gate and standard axiom audit.
- **NF660 workflow 44437954229**: SUCCESS. The real symmetric quadratic Gershgorin row payment and interval-coercivity theorems have now passed Lean and standard axiom audit.
- **NF661 workflow 44437952335**: SUCCESS. The literal original 15-source `neutralNF661PhysicalH` integral-defined block and general surjective quantitative basis-transfer theorem have passed Lean and standard axiom audit.
- **NF662 initial workflow 44437951716**: generic symmetric lower-to-upper physical interval transport PASSED; genuine source artifact rehydration and NF658 regeneration PASSED; physical pilot compilation FAILED on a missing constant `NF591Ball.ext`. The original `NF591Ball` is a two-field structure with no generated `ext` theorem. This branch introduces `nf662Ball_ext` from explicit constructor elimination and changes both pilots and generated full 225-entry bank to use it. This is a proof elaboration repair; **new Lean acceptance pending**.
- **NF663 original source integer-to-real certification**: proposed `S^-3` scaled real interval attachment, CI pending. No accepted new NF663 theorem is asserted.

## New mathematical work: actual physical transformed Gram positivity

Committed `ActualZetaOriginalPhysicalGramTransformedDominance.lean`, with three concrete proof candidates.

1. **Transformed real symmetry**. For any real symmetric matrix H and real preconditioner K, the full double-sum `B_ij=∑p∑q K_ip K_jq H_pq` is symmetric, including the original `neutralNF661PhysicalH` integral-defined matrix.
2. **Exact integer-to-real row margin**. Given integer center and radius arrays T,U, positive real denominator D and exact integer row inequality `m ≤ T_ii-U_ii-∑_(j≠i)(|T_ij|+U_ij)`, derive the corresponding exact *real* row margin after division by D.
3. **Physical quadratic coercivity from certified integer margins and real interval membership**. If every *actual* transformed real entry lies in `T/D±U/D` and the integer row margins are verified, deduce
   `(m/D) * (∑i y_i²) ≤ ∑i∑j (K H_I Kᵀ)_ij y_i y_j`
   by using the already accepted NF660 symmetric-interval coercivity theorem. This module adds no new eigenvalue or numerical positivity premise.

The source-bound specialization `WeilDefect/Generated/NF664/OriginalTransformedCoercivity.lean` provides the actual NF659 centers/radii and certified row margins, and consumes NF663's authentic physical-real interval target, aiming to prove:

`∀ y : Fin 15 → ℝ, ((nf658MinMargin : ℝ)/(10^64:ℝ)^3) * neutralNF661SqNorm y ≤ neutralNF661Quadratic (neutralNF664ActualPhysicalB nf662OriginalPreconditionerReal) y`.

The specific physical specialization is **Lean pending**, and depends on NF662/NF663 original real attachment acceptance.

## CI division and remaining endpoint

New NF664 workflow `.github/workflows/nf664-original-transformed-coercivity.yml`:
- Job 1 independently checks generic real symmetric congruence, exact integer row margin and real quadratic coercivity with standard axiom audit.
- Job 2 rehydrates original pinned NF631/NF621/NF648/NF632 archive, rebuilds NF655 original physical H sources and NF657/NF658/NF659/NF662/NF663 generated modules, then checks the actual physical transformed coercivity theorem with standard axiom audit. Newly introduced modules remain compiler proposals until accepted.

After NF664 succeeds, the **remaining local terminal bridge** is:
- prove rational `K_int/S` lower-unit-triangular inverse/surjectivity in Lean;
- prove `‖Kᵀy‖² ≤ (kn/S²)‖y‖²`;
- prove the exact congruence *quadratic identity* between transformed B and the original H under `x=Kᵀy`;
- apply the accepted `m_int*10^60>S*kn` gate using the already accepted NF661 surjective-map coercivity theorem.

The original physical `xᵀH_I x ≥ 10^-60‖x‖²` is **still OPEN** until this actual specialization compiles. The full 242 physical system, global Weil positivity and RH remain **OPEN**. Draft only, no main merge.
