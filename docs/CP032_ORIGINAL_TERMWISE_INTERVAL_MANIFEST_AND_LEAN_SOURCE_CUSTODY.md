# Weil-Lab — CP032: 526 original finite term cells and source-identity proof candidates

**Track:** CP### cross-projection, stacked on CP031 draft #853. No mutation of original IV/NF/PI certification or workflows. **EXTERNAL INTERVAL PROGRESS ONLY; NO NEW LEAN PASS.**

## 1. Original source formula and exact term count

I inspected the genuine original Zeta EulerMaclaurin/Continuation.lean at commit c06b4e13d9c847e50a32c3d738271cbad62ae9f3. Its actual M=6,N=256 approximant is

    A(s) = sum[n=1..255] n^(-s)
           + 256^(1-s)/(s-1) + 256^(-s)/2
           + sum[k=1..6] B_(2k)/(2k)! * (s)_(2k-1) * 256^(-s-(2k-1)).

Thus there are 255 + 1 + 1 + 6 = 263 complex finite terms per height and 526 for the two exact source heights 150.05352 and 150.05353.

The accompanying isolated CP032OriginalTermSplit.lean imports ONLY original Zeta EulerMaclaurin/Continuation and HardyZ, reconstructs those original terms, and proposes (a) a definitional source identity via rfl, and (b) generic Finset.sum_le_sum component interval transport. It includes two genuine #print axioms instructions. It has NOT been compiled, and its shared Lake target is intentionally NOT registered.

## 2. Real executed independent interval results

Executed local cp032_term_cells.py against the locally mounted CP031 independent rational reconstruction. For each of the 526 complex terms, its real and imaginary parts were rounded outwards to integer endpoints divided by 10^15. The program added integer term endpoints to reconstruct both original-source-oriented complex sums, separately enclosed the source Stirling-two theta sine and cosine on the same grid, and applied sign-safe interval multiplication to the real rotation

    F(t) = cos(thetaStirling2(t)) * Re A(t)
           - sin(thetaStirling2(t)) * Im A(t).

Every aggregate interval contains the separately evaluated CP031 original-source-oriented bulk interval. The resulting six 10^-9 cells are exactly those in CP031.

| External scalar, integers / 10^15 | left 150.05352 | right 150.05353 |
|---|---:|---:|
| Re A | [-515401799,-515401535] | [11733226104,11733226368] |
| Im A | [-446241931,-446241667] | [10158461695,10158461959] |
| Rotated finite real F | [-681741062,-681740689] | [15519759624,15519759999] |

| External scalar, integers / 10^9 | left 150.05352 | right 150.05353 |
|---|---:|---:|
| Re A | [-516,-515] | [11733,11734] |
| Im A | [-447,-446] | [10158,10159] |
| Rotated finite real F | [-682,-681] | [15519,15520] |

Full executed locally available manifest: /mnt/data/cp032_526_term_cells_NOT_LEAN.json (116168 bytes), SHA-256 0e1ac8fff81121c0ffba3df87f387c47381d784d65e80d5ad921c435e55e9885.

Repository script cp032_original_term_cells_source_oriented_manifest.py uses the immutable **REPOSITORY** CP031 independent source script identified by blob 61b0cc0577986753a74f61cd51aa8391023161e2. The local executed implementation was a separately mounted CP031 source with the same mathematical formulas, not that exact repo blob; therefore the repository-version replay is **prepared, not claimed executed in this step**.

## 3. Falsifiable actual Lean proof payments

No JSON numerical value becomes an axiom. Each true source membership remains an explicit unpaid proof obligation:

1. For 255 true source Dirichlet terms at two rational heights, prove 510 **complex** memberships; for actual original pole, half and Bernoulli corrections prove 16 more. Each complex membership consists of two real components with both a lower and upper rational bound. This gives 526 complex cells, or 1052 scalar interval memberships, all currently pending.
2. Verify genuine original phase sine and cosine at both heights (four real membership proofs) and identify those formulas with the published original HardyZ theta-Stirling approximation.
3. Apply the original-source identity and finite sum interval transport, using exact integer/rational addition and outward products to reach CP030's six original finite scalar inequalities.
4. Independently obtain real Lean4.35 compiler and strict standard-only axiom feedback for CP029 Borwein and the original CP026–28 HardyZ/IVT bridge. Only after the source finite inequalities and this inherited chain are paid can a narrow original critical-line zeta zero be certified.

Even that narrow existence would NOT prove rank53/uniqueness, full original signed-Weil/spectral normalized equivalence, global signed Weil positivity or RH.

## 4. Controlled CI and trust boundary

Four new paths: this document, a complete exact rational source-replay generator, a tiny external-not-Lean JSON summary, and an isolated original-source Lean candidate. No shared lakefile.toml or workflow modification. The 37 inherited workflows were checked read-only: ordinary PR triggers are path-scoped, with no relevant broad cp011_zeta_v435/**, scripts/**, docs/** or data/** PR patterns; others are opt-in manual/label-only. No heavy CI launched. No original NF/IV proof artifacts or 692/968 accepted frontier changed.

**Next CP033:** launch a narrowly coordinated first actual Lean4.35 isolated source-split compiler after rechecking runner capacity. Then pay genuine source-level term membership inequalities. The direct full pinned CP025 replay and CP029 actual compiler receipts remain separate unresolved obligations.
