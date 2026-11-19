# NF658 — original physical H to 64-digit finite-block coercivity

## Recovered verified head

NF655 draft PR #680 run 44422031265, job 135217176892 **SUCCESS**. The actual original 120 physical (H)-entry analytic enclosures, including all 14 pole cross terms and signed mixed moment row, passed Lean with standard axioms. No newer PR than #680 at inspection. NF657 contains an external integer-coercivity certificate and a *candidate* real-analytic physical symmetry theorem. These are not yet final Lean positivity proofs.

## New actual preflight

The original NF631 archived entry ZIP sha256
`e91a83cae117e98608aefa6849dac178e4ddb58dd1dffbfe37304ad248af9ed9`
was read directly, including retained compressed entry file sha256
`9e76e2dea4f46ed5fc3ff8875f804c186cd0cacb86c47295f0cd93d189b9f7e6`.
The compact 64-digit rational congruence witness was independently checked against the frozen original data:
- All 120 original (Q=10^{2600}) entry intervals widen into fixed ((c_{ij}pm e_{ij})/S) intervals, (S=10^{64}), by exact integer cross multiplication.
- Full 15x15 symmetric C/E matrices, 15x15 lower-unit K preconditioner, and all 15 transformed dominance margins were independently recomputed by four-index integer sums.
- All 15 margins are strictly positive.
- The conservative coercivity gate `min_margin * 10^60 > 10^64 * K_integer_Frobenius_norm_sq` passed exact integer arithmetic.
- The local emitter generated 17 new Lean module candidates (WitnessData, 15 source rows, Complete), containing 120 original-to-small rational widening gates and 120 actual analytic H containment transfers. It does not regenerate original NF655 data or change the physical basis.

Original session witness file sha256
`f884548b04664516a9b508a1ca8ac41cc52ccf0295a959198bf528e561d1c39b`.
The committed producer independently validates the full witness content (all margins and norm, original archive pins) instead of requiring that exact presentation-dependent SHA, because the NF657 regenerated JSON can have a different annotation string. The local emitter used an equivalent implementation; the committed script is scheduled to be tested on an actual workflow runner.

## Formal proof candidates and specific next compiler tests

Added `scripts/emit_nf658_original_gram_widenings.py` binding each 64-digit ball to its genuine already certified `nf655H*_Contains` theorem via the accepted `NF591Ball.contains_widen`. The source generated modules use an explicit rational `decide` gate rather than a typeclass-generated abstract widening proof, avoiding the exact old NF655 decidability failure.

Also added `WeilDefect/Generated/NF658/TransformPilot.lean`: direct integer double-sum formulas for transformed centers/radii and two independent representative entries, one oscillator and one genuine pole. Added `ActualZetaOriginalPhysicalGramCoercivityLemmas.lean` with source-independent cross-term inequality and an exact bilinear interval lower bound. These are candidates with no `sorry`/new `axiom` instructions, and are not yet accepted.

The focused CI workflow checks, in order: recovered original physical H symmetry theorem, fifteen stored integer margins/coercivity gate, first and pole source rows, all 120 rational widenings, cross-term/bilinear lemmas, two numerical transform pilots, explicit axiom audit. It regenerates original NF655 proof proposals from exactly the same GitHub artifact inventory that passed on run 44422031265 and uses the NF631 archive to independently regenerate the compact NF657 witness. **CI has not yet passed; do not mark NF658 formal positivity CLOSED.**

## Remaining obligations

1. Original physical H symmetry is **already Lean-certified** as `neutralNF606PhysicalH_symm` in `ActualZetaOriginalPhysicalSolveResidual.lean` (integral product commutativity). NF658 now reuses that exact theorem instead of relying on a second unverified NF657 proof. Lean accept all 120 NF658 rational-widening theorems.
2. Prove generic finite-dimensional diagonal-dominance lower bound and exact congruence/triangular invertibility in Lean, then bind all transformed center/radius sums to their printed integer results. Two transform arithmetic pilots have been proposed, not all 225.
3. Conclude (x^\mathsf{T}H_Ix\ge10^{-60}\|x\|_2^2) as a **Lean theorem for this original fifteen-generator principal block**. The corresponding exact external mathematical certificate is already validated, but this Lean theorem remains OPEN.
4. This is neither the complete 242-generator physical matrix, nor global Weil positivity or RH. The numerical solve containment is separate.

No merge to `main`; the draft PR is scoped to the NF657 branch so numerical arithmetic and analytic entry custody remain independently reviewable.
