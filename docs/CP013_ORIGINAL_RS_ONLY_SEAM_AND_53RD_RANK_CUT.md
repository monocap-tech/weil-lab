# Weil-Lab — CP013
## Original source RS-only certified bundle reconstruction and exact 149.5 seam count; finite-rank alternative to indexed-row opacity

**Independent CP### cross-projection stage:** CP013 stacked on CP012 PR #827 → CP011 #825 → CP010 #822 → CP009 #819 → CP008 #817 → CP007 #815 → CP006 #810 → CP005 #807 → CP004 #803 → CP003 #799 → CP002 #796 → CP001 #790.

**Do not modify** original Phase IV IV### support-extension/Lean certification, original NF### numerical enclosure/custody, or independent PI### arithmetic/Gamma trace interface. CP013 does not import the original external Lean v4.35 theorem into the original Weil-Lab Lean v4.34 tree. No global signed Weil positivity or RH claim.

**Status at kickoff:** CP012 original source batch-opacity CI run `44860452343`, CP011 source-row CI `44859873767`, and CP010 dual-sign CI `44859054487` remained **queued**; none of the new CP008/CP010 refined zero-sign proofs or CP011/CP012 new kernel/source-index bridging theorems has been accepted in the current audit. This stage's imported original published Zeta source is a separate proof lineage. CP013 creates a source-derived, no-sorry **Lean proof candidate** for a NEW partition, with a manual-only real kernel build and a cheap, source-SHA-pinned verification workflow. Mathematical deductions downstream of the candidate are stated conditionally until their corresponding kernel receipts exist.

## 1. New actual source observation: the original generator already separates Euler from RS at 149.500

Directly retrieved and parsed frozen `smmercuri/zeta@c06b4e13d9c847e50a32c3d738271cbad62ae9f3`:

| Source | Original Git blob | Exact source fact |
|---|---|---|
| `Zeta/Zeros/Certificates/Groups/Level1/Group0001.lean` | `12263d2f09d5a69c489c29c63940829e2c7211dc` | Imports original Euler Batch0001 then RS Batch0001–0124; 124 RS batches ×200 intervals, plus 52 Euler intervals |
| `Zeta/Zeros/Certificates.lean` | `54fce07cbc5bf0913ceccb108cbf73f1227857c0` | Source-generated total 70 Level1 groups; Group1 length 24852, Groups2–69 add 25000 apiece, Group70 adds 23150 |
| `Zeta/Zeros/Certificates/EulerMaclaurin/Batch0001.lean` | `a4f28786abb75420cf950ae701f5c7befcda560d` | `BatchSpec 52 1000 1000 149500 1000 := by build_batch 0 52` |
| `Zeta/Zeros/Certificates/RiemannSiegel/Batch0001.lean` | `12848f56d0b62df858dcb89b708a858f4f7b28fb` | `BatchSpec 200 149500 1000 474603 1000 := by build_batch_rs 0 200` |
| `Zeta/Zeros/Certificates/Fold.lean` | `2596e253a8c8f94c47ce880500973775f2611d77` | Original `BatchSpec.append` has a kernel-proved disjoint seam preserving count and first/last endpoints |
| `Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean` | `c2b1da101a580cc91cfb0a43d72d5839fd97265c` | Original `riemannZeta.N_gramPoint_eq` count matching the complete 1,748,002 original source-certified slots |

The **exact integer source ledger**, checked independently, is:

```
  Euler original low source:               52
  RS from Group0001 (124 × 200):       24,800
  RS from groups0002..0069 (68 × 25000): 1,700,000
  RS from group0070:                   23,150
                                     ----------
  all original RS:                  1,747,950
  all original certified zeros:     1,748,002
```

The original Euler LAST interval ends at the exact rational (c=149500/1000=299/2=149.5). Original RS FIRST interval starts exactly at (c), and their *open interior* zero witnesses cannot be at the common boundary. This source-level support of a method seam does not expose any intermediate numeric RS row endpoints. It is entirely compatible with CP012's `BatchSpec` indexed-row nonidentifiability finding.

## 2. New separate original source RS-only Lean proof CANDIDATE

Committed `cp011_zeta_v435/CP013RSOnly.lean` with **193 source-linked proof stages**, unlike the original top-level combined Euler+RS list:

- Start from imported ORIGINAL `RiemannSiegel.Batch0001.batch`, then append ORIGINAL `Batch0002` through `Batch0124`, preserving exact 149.500 first-left and each original 200-row cumulative last-right.
- Append ORIGINAL source group theorem `Groups.Level1.Group0002.group` through `Group0070.group`, 69 additional disjoint source groups. **Only existing upstream kernel-certified batch/group theorem statements are used**; no root location or sign calculation is invented or independently assumed.
- Export NEW source candidate

```lean
theorem CP013RSOnly.all_original_RS_only :
    BatchSpec 1747950 149500 1000 1000449286 1000
```

with a final original source boundary (1000449.286). The original toolchain is unchanged **Lean v4.35.0**; this statement is **not kernel-accepted in CP013 until actual .olean/axiom receipts are produced**.

Second new module `cp011_zeta_v435/CP013Seam.lean` explicitly reassembles

```lean
theorem CP013Seam.first52Euler :
    BatchSpec 52 1000 1000 149500 1000

theorem CP013Seam.allRS :
    BatchSpec 1747950 149500 1000 1000449286 1000

theorem CP013Seam.allOriginalSplit :
    BatchSpec 1748002 1000 1000 1000449286 1000 :=
  BatchSpec.append first52Euler allRS rfl rfl rfl
```

The reassembly uses the ACTUAL original `BatchSpec.append`, whose `Separated` seam is kernel-proved from the published endpoint bounds. This is a different **certified-bundle construction** from the generator's original abstract existential witness; it does not claim definitional equality of the two `Classical.choose` witnesses or exact numerical values for every internal row. That is a deliberate preservation of CP012's source/Lean distinction.

## 3. Important mathematical deduction: the source split implies EXACTLY 52 zeros before 149.5

Let `g` be the original Turing-certified Gram point above the original terminal height 1000449.286. Assume CP013's newly compiled source split succeeds. The genuine ORIGINAL external source provides:

1. **52 distinct actual critical-line zeros with ordinates strictly below `c=149.5`**, witnessed by the Euler certified batch of length 52. Every bracket has open interior and last right endpoint exactly `c`.
2. **1,747,950 distinct actual critical-line zeros with ordinates strictly above `c=149.5` and below `g`**, witnessed by the separate RS-only certified bundle. Its very first lower endpoint is `c`, and its ordered interval chain guarantees every later interval begins at or above `c`.
3. **The ORIGINAL externally certified total multiplicity count is (N(g)=1,748,002)**. This counts EVERY possible positive-height zeta zero, not just critical-line zeros.

The two sets of witnessed roots are disjoint because their imaginary parts lie on different sides of `c`. Their total count equals `N(g)`. Every genuine positive-height zero contributes at least one to that multiplicity count. Hence **there is no unaccounted-for zero in (0<\gamma<g)**, and no zero at exactly `c`. Therefore:

```
  N(149.5) = 52,   counting multiplicities.
```

This is a **valid mathematical deduction from the source-certified count and the proposed disjoint certified source split**, not a direct checked result of the currently committed `CP013Seam.lean`: its actual kernel proof of `N(149.5)=52` has **not** yet been authored/compiled as a separate theorem. The condition “CP013 separate RS-only batch compiler PASS” MUST remain explicit in reporting.

Crucially, obtaining a LOW-HEIGHT COUNT from the externally certified complete source set **does not require knowing the literal first RS row's right decimal endpoint**, and does not require identifying `(certifiedZeroCount.intervals.get ⟨52,…⟩)` with an original source text row.

## 4. What remains to establish the first RS zero is global ordinal 53

A low-side cut count (N(149.5)=52) alone establishes only that **at least 52** roots precede a new zero above 149.5. It does NOT prove that an arbitrary new certified zero in the narrow candidate [150.05352,150.05353] is next; there might be another root between 149.5 and that new zero.

A possible logically sufficient count-cut route, avoiding CP012's indexed-row endpoint bridge, is the pair of independently kernel-certified local counts:

```
  N(149.5) = 52,                  [proposed derivation from CP013 split]
  N(150.05353) = 53,              [STILL OPEN: rigorous local rank upper bound]
  ∃ γ ∈ (150.05352,150.05353),
      ζ(1/2+iγ) = 0.               [CP010 Euler sign/analytic proof OPEN]
```

These three hypotheses, with the original multiplicity counting convention, force `γ` to be **the unique first zero above 149.5** and hence positive-zero ordinal **53**. The second count could alternatively be replaced by an exact bounded-height no-extra-zero theorem or source-index `IndexedSlotContains` receipt from CP012. A numerical mpmath zero guess, original full `N(g)`, first RS batch `BatchSpec 200...` outer endpoints, and source SHA are each insufficient individually.

This specifies a falsifiable competing bridge:
- **Row bridge**: original source bundle's `IndexedSlotContains` at global index 52, plus rigorously accepted refined root existence; OR
- **Rank bridge**: independently certified height cut counts (N(149.5)=52), (N(150.05353)=53) and refined zero existence.

Neither is silently assumed complete. The original full signed Weil Pole−Prime+Gamma 3×3 arithmetic/zero-side identity, oscillatory quadrature and refined full million-height zero roster remain independent OPEN tasks.

## 5. Verification machinery, exact source signatures and trust boundaries

Source `scripts/cp013_rs_only_batch_source_lineage.py`:
- `--self-test` independently checks exact all-RS count and deliberate missing/duplicate group negative controls.
- `--original-root UPSTREAM` verifies **exact Git blob SHA-1 of the two original generator source modules** shown above. It parses every original RS prefix count and last-right from original group0001 and every original group-end count and last-right from the top-level assembler. It verifies all **193 exact matching new Lean theorem signatures** and their immediate upstream proof dependencies, source-group imports, original first/last ordinates and exact seam. This is a **SOURCE THEOREM DEPENDENCY PREFLIGHT**, NOT an accepted Lean proof.
- Any blob drift, omitted/duplicated original group, incompatible count, source signature/proof dependency mismatch or fabricated endpoint returns `NOT_READY`. A successful result says `CP013_ORIGINAL_RS_ONLY_SIGNATURES_AND_149500_SEAM_SOURCE_PASS_NOT_KERNEL`.

Source `scripts/cp013_original_rs_only_lean_axiom_audit.py`:
- Requires actual `CP013RSOnly.olean` AND `CP013Seam.olean`, real external Zeta v4.35.0 and FOUR actual `#print axioms` receipts for the full RS-only theorem, reassembly theorem and 52/RS counts. Permits standard `propext, Classical.choice, Quot.sound` only.
- Its SUCCESS label strictly says **original source split certified**, with `N_at_seam_149500_div1000_kernel_proved=false`, `numerical_original_index53_row_binding_proved=false`, `CP008_CP010_refined_root_signs_proved=false`, `original_Weil_spectral_dictionary_proved=false`.

CI:
- `.github/workflows/cp013-original-RS-only-source-lineage.yml` is cheap automatic PR-triggered exact source signature/sequence audit (only ~55KB of new original source fetched; **no 53MB original data**).
- `.github/workflows/cp013-original-RS-only-v435-manual-kernel.yml` is **manual-only** real original Zeta 4.35 source theorem + axiom compiler. Protect the canonical IV###/NF### original compiler queues.

**Next — CP014:** recover original RS-only compiler and source receipts. Then make the disjoint split exact count (N(149.5)=52) into its OWN explicit real Lean 4.35 kernel theorem, not just a mathematical corollary; test original published zero count around 150.05353 for a rigorous upper count of 53. Do not promote CP010's Euler refined-root numeric candidate to a source-certified first RS zero until its original rigorous method-specific sign/analytic error proof AND an admissible rank/slot certificate both pass.

**Ledger:** Reconstructed original 1,747,950 RS source bundle: no-sorry source candidate committed; source-generated 193-stage signature proof checked against retrieved original source statements. RS-only Lean .olean, exact `N(149.5)=52` Lean proof, (N(150.05353)=53) Lean proof, narrow Euler root Lean sign, original 3×3 Weil–spectral equality, global Weil positivity/RH: **all OPEN**. The falsifiable compatibility conjecture remains the research objective, not any global claim.

Original source references: https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Zeros/Certificates/Groups/Level1/Group0001.lean ; https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Zeros/Certificates.lean ; https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Zeros/Certificates/Fold.lean .
