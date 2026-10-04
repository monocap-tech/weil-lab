# RPB108 proof-bearing literal explicit formula port — 2026-10-04

Parent research: `434229b7e04a8b54740c87ecdde82617447619c0`.
Definitions: [port terminology](../docs/TERMINOLOGY_RPB108_EXPLICIT_FORMULA_PORT.md).
Custody: [pinned original manifest](../docs/EF_LIT_ZETA_DEPENDENCY_MANIFEST.json), [ported source hashes](../docs/EF_LIT_ZETA_PORT_MANIFEST.json).

## Certified result

The complete recovered literal explicit-formula closure is now compiled under Lean/Mathlib 4.34.0 and imported by WeilDefect. It contains 84 accepted proof bodies and 30 definition files. Each theorem statement stub has been replaced by its separate pinned accepted proof body, under repository-local import paths and its recorded export name.

The final exported theorem is:

```lean
Zeta23.WeilEF.EF_lit_zeta (hs : Zeta23.ZetaSeam) :
  Zeta23.EF.EF_lit (Zeta23.zetaZeros hs)
```

Its conclusion quantifies over compact C² complex test functions and supplies actual-zero sample summability and the literal zero sum = two poles − prime sum + digamma integral formula. The seam structure records the actual-zeta carrier facts; the bundle also compiles the existing closed seam `Zeta23.zetaSeam`. It does not take the literal explicit formula as an input premise. The retained WD-T38 mode is not identified by this external theorem.

The sources are pinned to prove2me/formalpedia `ae3af9184af2e274c721b1cf3b0dffa09af02c6c`, environment `0df444a`. Original accepted receipts and original hashes remain in the recovery manifest. Copyright and source attribution comments are retained. The root accepted receipt is [3baa154b-f40d-4423-bff3-ae84616db32e](https://prove2.me/submissions/3baa154b-f40d-4423-bff3-ae84616db32e).

## Port repairs

The standalone solution bodies copy supporting declarations from their original project contexts. Combining them exposed helper-name collisions. Copied repeated helper declarations now have module-specific names; the 84 main exports and their statement types are preserved. Making a helper private alone cannot shadow an imported public declaration, so the port uses distinct names.

Lean 4.34 product inequalities distinguish nonnegative real products from ordered monoid products: the port uses Finset.prod_le_prod₀ and Finset.prod_le_one₀ where nonnegativity is supplied. Logarithmic derivative rewrites require explicit function-level multiplication and finite products. These changes make the original proof's pointwise identities explicit. A comment-only wording repair prevents the existing raw unfinished-declaration gate from misreading the Hypotheses file's explanation as an axiom declaration. No mathematical premise was added.

Compiler candidates:
- `b4f919db8cbac7bf90c4cde722a9cfd805b2ab23`: initial combined closure.
- `e44212899e876f96fbe0650fbdc83286a650eb8c`: function product and first helper repairs.
- `a0a3c55a24cabc3d8306fd74f73bb803e6e44542`: distinct names and nonnegative product APIs.
- `95c9a6ca04773d50aa9e83ab494112fe876ec407`: later contour/prime/Stirling collisions.
- `652f9e9fd3eab0374173d349e35dc09fe86ff9e5`: successful complete port.

## Validation

Exact candidate `652f9e9fd3eab0374173d349e35dc09fe86ff9e5` passed [run 37177275511](https://github.com/monocap-tech/weil-lab/actions/runs/37177275511), job `111362416280`: isolated explicit-formula closure 3,857 jobs; full `lake build WeilDefect` 9,179 jobs. The final theorem's axiom audit is exactly `[propext, Classical.choice, Quot.sound]`. The unfinished/project-axiom gate passed. The validation dependency cache was saved under `rpb108-ef-closure-port-verified-v1`. Workflow and pinned manifest remain validation-only. Research promotion uses the exact validated 114 source files and root import.

This closes the external explicit-formula recovery/compiler trust prerequisite. It does not yet prove the correspondence between our multiplicity-copy divisor and the external distinct-zero weighted sum, nor transport the arithmetic RHS to our concrete source form.

## Cursor and residue

Next cursor: prove the actual-zero carrier and analytic multiplicity correspondence between our full-copy actual divisor and the now-certified Zeta23.zetaZeros Zeta23.zetaSeam. Apply Zeta23.WeilEF.EF_lit_zeta to the already certified compact C² inverse correlation J_a(v,w), using its proved sample summability/zero form and canonical-image pole identity. Attach the exact prime and digamma terms on that same carrier. No external theorem hypothesis or admissibility/representation wrapper is needed. Retained WD-T38 coefficient/source dictionary and same-vector source/null identity remain required before transferring the result to that witness.

Compact C² admissibility, all-complex raw-transform equality, actual-divisor absolute convergence and exact zero form, and the pole identity on the exact canonical Green images were already certified and remain closed. Do not replace them with input hypotheses.

WD-T38 source/null attachment, central cancellation, background completion and F-4 remain open. The retained coefficient/source dictionary and identity with the constructed Green synthesis are unproved. The zero-density reindex audit blocks inferring a physical source identity from independently named density/Q fields. Retained-mode spectral L²/operator-domain membership remains unproved and unassumed. Sharp unit-height logarithmic counts and full log-domain raw sampling remain open. Earlier residue is preserved. SOURCE stays off the critical path; threshold stays closed; RH remains open.
