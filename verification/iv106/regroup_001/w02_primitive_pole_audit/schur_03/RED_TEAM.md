# Schur 03 — bounded two-error proof-body repair

## Parent and clearance
Schur 02 native run 46112537490, job 140879055835, failed in the only compilation target; custody job 140884290567 passed. Original evidence archive ID 15250454320 and remote custody in schur_02/evidence. The Schur 03 candidate is *not admitted* before strict native build and 5/5 named-axiom replay. Neither a successful preflight nor a green custody job is proof certification.

## Exact bounded delta
The 74 overlay destinations, 38 source refs, 39 F08 modules, pinned base, target module and five statements remain unchanged. The sole changed mathematical source is ActualZetaIV106W02SchurCompletion.lean. Two local proof-body edits only: (1) expand the complementary diagonal after transporting the first pairings and then rewrite the complementary cross term, preserving the exact Schur completion identity; (2) type-annotate additive inverse cancellation by explicitly applying neg_add_cancel to the admitted constrained-response vector. No new assumptions, sorry/admit/axiom, or changed coefficients.

## Red-team static assessment
The line-80 failure in the prior run was hcrossE used before its exact occurrence appeared on the right-hand side. The candidate first rewrites other pairings, expands the remaining complementary sum, and only then rewrites hcrossE. The Lean elaborator may still expose a syntactic orientation mismatch: native compilation determines this, not static review.

Line-100 type mismatch arose from an ambiguous neg_add_cancel instance on the constrained submodule; the candidate states the argument explicitly. This is a *proposed* source-level fix until independently compiled.

The two previously clean declarations S_generic and S_canonical are unchanged; S_complete, S_lower, S_attained must all independently pass. Audit rejects any sorryAx. Formal completion does not establish a finite-matrix sign, the original whole-form positivity, or RH.

## Governance
No re-opening Schur 01/02 predecessor mathematics, no changes to the constraints, no downstream mathematical promotion or Phase IV gate. The exact prior archives remain under custody. New build results must be preserved regardless of compilation success, with SHA256, size, ZIP CRC, remote readback and failed-job diagnostics retained.