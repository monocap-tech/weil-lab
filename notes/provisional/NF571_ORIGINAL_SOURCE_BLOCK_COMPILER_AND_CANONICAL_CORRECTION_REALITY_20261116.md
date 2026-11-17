# NF571 — source-block compiler repair and real-data canonical correction

Draft stacked on NF570 PR #602. New proof candidates committed; no new Lean acceptance claimed.

## Newly available CI

NF567 run 44005817998:
- job 133780805266, exact original 58,564-entry SHA source custody: SUCCESS.
- job 133780804625, original 67 frequency blocks: FAILURE, specifically line 70 of ActualZetaOriginalJ242Actual67BlockCoverage.lean. Unknown constant List.get_map, and consequent type mismatch between indexed list and mapped-list entries. No other errors reported. The preceding and following statements are not promoted to independently certified module PASS.
- job 133780805169, full Hermite multiplicities: FAILURE at the already diagnosed missing iteratedDeriv import in NF566, on the older pre-NF570 head.
- job 133780805041, physical per last check in progress. NF568–NF570 focused runs queued.

The latest verified NF550 exact weighted square and collar-separation theorem, NF561–NF563 actual oscillator derivatives, first positive root, and NF565 exact formal frequency polynomial remain accepted per NF570 receipts.

## Precise repair

Replace List.get_map with List.get_eq_getElem and List.getElem_map in the NF567 source rational-frequency injectivity proof. These are current Lean lemmas observed in Mathlib source. No change to the actual table, nodes, multiplicities, or index-coverage claim. New compiler result pending. NF570's iteratedDeriv and odd-parity repairs are inherited unchanged.

## Independent real-structure gate

New ActualZetaOriginalJ242CanonicalCorrectionReality.lean imports the accepted NF549 actual physical integral, not the pending NF551 or NF566–NF569 argument. With C d the coordinatewise complex conjugate, Bχ the existing canonical bump synthesis, and Gχ the actual original weighted Gram, the candidate theorems are:

- Exact original physical sources j_i, full-window zero extensions, and χ are fixed under conjugation.
- Bχ(C d)(x) = conj(Bχ(d)(x)).
- For conjugate Schwartz tests t(x)=conj(s(x)), J242(t)_i=conj(J242(s)_i) via the actual physical integral.
- Gχ(C d)=C(Gχ d), without any positive-definite or invertibility premise.
- If the actual Gχ is injective, the actual NF544 linear equivalence inverse satisfies Gχ⁻¹(C d)=C(Gχ⁻¹ d). Proof: apply the injective equivalence to both sides and use the forward equivariance; no separate inverse.
- Under the existing explicit strict Gram positivity premise, the actual NF548 R=Bχ Gχ⁻¹ satisfies R(C d)(x)=conj(Rd(x)).
- For real data C d=d, the exact canonical correction is pointwise real, without post-hoc symmetrization.

This is not an unconditional construction of R before its positivity dependency compiles. It is also not yet an equivariance theorem for arbitrary physical L² inputs or the full corrected test (that requires real target moments and real initial test). The finite correction property is the direct independent obligation being addressed here.

## Verification

One focused NF571 CI job; separate steps for repaired block coverage, original root budget, independent reality, and full endpoint. Independent later steps still execute if one earlier proof fails, provided installation succeeded. Earlier checks remain queued. No new Lean acceptance asserted.

Next NF572: obtain actual NF568–NF571 compiler diagnostics, recover earliest source and parity/analytic failures; then integrate the real-data condition with the unconditional original right inverse only when the entire chain passes. NF528 full divisor graph, NF527 1/10 coercivity, NF539 signed Weil source identification, W_ODD_NEG and RH remain OPEN.
