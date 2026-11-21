# Weil-Lab — CP015
## Unconditional source-exhaustive Euler/RS zero-set partition at 149.5: no source row-identity axiom

**Independent CP### research stage**, stacked CP014 PR #831 → CP013 #829 → CP012 #827 → CP011 #825 → CP010 #822 → CP009 #819 → CP008 #817 → CP007 #815 → CP006 #810 → CP005 #807 → CP004 #803 → CP003 #799 → CP002 #796 → CP001 #790. The original Phase IV IV### signed Weil support-extension/Lean program, Phase III NF### original physical matrix numerical enclosure, and independent PI### pole/prime/Gamma interfaces are **unchanged**.

### Status and scope

CP015 commits a genuinely new **no-sorry original-Zeta Lean 4.35 SOURCE PROOF CANDIDATE** whose theorem statement has **no new missing hypothesis**:

```lean
theorem CP015SourceWitnesses.original_N_at_149500_div1000_eq_52 :
    riemannZeta.N ((149500 : ℝ) / 1000) = 52
```

It also proposes stronger source-defined lemmas showing the genuine Euler/RS witness subsets exhaust the entire original finite-height positive zero set and **there is no zeta zero at precisely 149.5**, at any real part. These are meaningful distinct consequences from a strict cut count because `N(T)` counts only ordinates *strictly* below `T`.

**Do NOT promote these CP015 SOURCE THEOREMS to accepted kernel facts** until the genuine external Lean v4.35 `CP013RSOnly.olean`, `CP013Seam.olean`, `CP014FiniteCut.olean`, `CP014ZetaCut.olean`, `CP015SourceWitnesses.olean` and actual no-sorry, standard-only `#print axioms` receipts exist. The code is not yet kernel accepted, and CP014 prerequisites have not been compiled. The theorem's lack of a formal premise does **not** imply a compiler pass. No narrow CP010 Hardy-Z root proof, ordinal 53 indexed proof, source-row decimal equality, complete cross-projection spectral matrix or RH/global Weil positivity follows.

At kickoff the original CP014 PR #831 workflow `44862100024` and original CP013 source verification `44862100005` were **queued**, along with inherited CP012; no later accepted receipts observed. In view of repository workflow multiplication, CP015 adds **two opt-in-only** workflows (explicit PR label or manual dispatch), and no jobs on normal pushes, PR creation, or PR synchronization.

## 1. Actual original source definitions: genuine zero roots already exist in the certificate API

Re-read the pinned original upstream `smmercuri/zeta@c06b4e13d9c847e50a32c3d738271cbad62ae9f3`. These are not invented specifications:

| Original upstream source | Immutable Git blob | Source theorem needed |
|---|---|---|
| `Zeta/Zeros/Interval.lean` | `152954545ca9997c2a2ddaead4d9161ffbbfe191` | `CertifiedZeroIntervals.zeros`, `zeros_spec`, `zeros_length`, `zeros_nodup`, `zeros_im`, `pairwise`, `height_le_of_getLast?` |
| `Zeta/Zeros/Certificates/Basic.lean` | `128e19e4bb056332b0fd71a8c107f4075cd8cd07` | Actual abstract `BatchSpec.bundle` has count, first-left, final-right; `height_le_of_getLast?_snd` |
| `Zeta/Zeros/CountCertificates.lean` | `a3e729d23802c3731432de9a3c7d46d18252ba10` | Actual concrete external source `certifiedZeroCount` |
| `Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean` | `c2b1da101a580cc91cfb0a43d72d5839fd97265c` | Original `N_gramPoint_eq`, finite-height simplicity, `le_N_of_zeros` |
| `Zeta/Gram/Certificates.lean` | `91fd460c42469ed889da985f3cd160df3f792105` | Original `gp1.fst=1000449.28682`, and the source `head_left_le_gramPoint` of certified Gram block sequence |
| `Zeta/Zeros/Certificates/EulerMaclaurin/Batch0001.lean` | `a4f28786abb75420cf950ae701f5c7befcda560d` | `BatchSpec 52 1000 1000 149500 1000` |
| `Zeta/Zeros/Certificates/RiemannSiegel/Batch0001.lean` | `12848f56d0b62df858dcb89b708a858f4f7b28fb` | `BatchSpec 200 149500 1000 474603 1000` |

The actual original `CertifiedZeroIntervals.zeros` chooses a proven critical-line zero in **each open interval** of its certified bundle and maps `t` to `1/2+i t`. Its source theorems prove that the chosen list is `Nodup`, has the same length as `C.intervals`, and each chosen point is an actual `riemannZeta` zero with strictly positive ordinate beneath `C.height`.

This is the key: the original **abstract** `BatchSpec` *does not* export every numerical row's endpoints (CP012), but it **does** export enough structural facts to choose `n` genuine, distinct zeros and prove precise *side-of-seam inequalities*. Therefore there is no need to assert definitional equality between original combined `certifiedZeroCount` and CP013's separately reconstructed Euler and RS-only existential witnesses. They can be different lists that independently saturate the same true finite zero set.

## 2. Stronger source-invariant theorem: every original finite-height zero belongs to E or R

Let `g = gramPoint certifiedZeroCount.minIdx`; use CP013's newly source-built original-v4.35 bundles:

```
 E_bundle = CP013Seam.first52Euler.bundle
 R_bundle = CP013Seam.allRS.bundle
 E = E_bundle.zeros.toFinset
 R = R_bundle.zeros.toFinset
 S_g = {s:ℂ | 0<Im(s)<g, ζ(s)=0}.
```

All three zero sets are genuine mathematical objects. The CP015 proof candidate directly discharges the remaining CP014 source-root hypotheses as follows.

**Exact counts**: original `zeros_nodup` and `zeros_length` give
```
 |E| = 52,  |R|=1747950.
```

**Euler source side**: its last source interval ends at exactly `149500/1000`; the original `height_le_of_getLast?_snd` bounds every Euler witness strictly below that endpoint:
```
 ∀ z∈E, 0<Im z<149.5.
```

**RS source side**: its first source interval begins exactly at `149500/1000`. Original `CertifiedZeroIntervals.pairwise` proves each later interval starts no earlier than this FIRST interval. Each RS selected witness lies strictly inside its certified interval, therefore
```
 ∀ z∈R, 149.5<Im z.
```

This is derived from the PUBLIC first endpoint plus the genuine sorted-interval invariant; it is not a claim to know the original first RS row's RIGHT decimal endpoint. CP015 adds an explicit source lemma `lower_bound_of_first_endpoint` implementing this order argument with the same original `List.pairwise_iff_getElem` proof interface.

**Original finite-height inclusion**: the original RS-only published final right endpoint is exactly `1000449286/1000 = 1000449.286`, while genuine upstream Gram certificate `gp1.fst=1000449.28682`. Independent exact rational comparison:
```
  149.5 < 1000449.286 < 1000449.28682 ≤ g.
```
The final comparison `≤g` uses the genuine original `certifiedGramBlockSeq.head_left_le_gramPoint`; it is not an assumption. `zeros_spec` plus both source bundle `height_le` facts imply
```
 E∪R ⊆ S_g.
```

**Disjointness**: every E zero is below `c`, every R zero above `c`, hence `E∩R=∅`.

**Saturation**: original externally certified `N(g)=1748002` with all original zeros of height below `g` simple (an actual upstream theorem). The CP014 new formal target `original_full_source_finite_zero_card` rewrites this as `|S_g|=1748002`. Thus
```
 E∪R ⊆ S_g,   |E∪R| = 52+1747950=1748002=|S_g|
 ```
and so **as a mathematical consequence**,
```
 S_g = E∪R.
```

CP015 source theorem `original_complete_positive_roster_is_euler_union_rs` asserts precisely this equality with **no unproved premise**. It depends on actual CP013 and CP014 source theorem **candidates**. The source establishes WHAT to kernel-check, but is not itself a completed compiler receipt.

## 3. Two unconditional consequences, no source-row identity

A. All (zin S_g) are from E or R, and the two subsets strictly straddle `c=149.5`. Therefore there is **no zero exactly on the seam**, whatever the real part:

```
 ∀ z:ℂ, Im z =149.5 ⇒ ζ(z)≠0.
```

New source theorem `no_original_zero_exactly_at_149500_div1000` proves this from the zero-set union. In contrast, `N(149.5)=52` alone would *not* rule out roots AT 149.5 because the upstream `N(T)` counts `0<Im z<T` strictly.

B. Exactly the 52 E zeros lie below the seam, hence exact multiplicity count

```
 N(149.5) = 52.
```

New source theorem `original_N_at_149500_div1000_eq_52` supplies CP014's previous conditional `N_at_Euler_RS_seam_eq_52_of_source_witnesses` with actual proof-derived `E,R` and all six missing coverage, no-overlap and side-of-seam propositions.

**The central CP012 limitation remains true:** no source-level count theorem reveals the original first RS internal RIGHT endpoint or gives a refined zero inside `[150.05352,150.05353]` a rigorously certified ordinal number 53. However, the true seam count can now be approached **without** any unsupported bridge from a source file SHA into a private indexed `Classical.choose` interval.

## 4. Verification design and source/Lean trust boundary

Committed source and audit files:

- `cp011_zeta_v435/CP015SourceWitnesses.lean`: true original `CertifiedZeroIntervals.zeros` constructed finite sets, exact original method-side inequalities, complete source cardinality union, no root at seam, and `N(149.5)=52`. No new axioms or `sorry` declarations; all are original-v4.35 **SOURCE CANDIDATES**.
- `scripts/cp015_unconditional_seam_source_preflight.py`: SHA1 Git-blob verifier for all seven actually inspected upstream source files; exact rational Gram margin and 52+1747950 source count, absence-of-seam-root abstract negative controls and source theorem signature checks. Returns only `CP015_SOURCE_WITNESS_COVER_AND_SEAM_SIGNATURES_PASS_NOT_KERNEL`.
- `scripts/cp015_exact_source_seam_lean_axiom_audit.py`: requires genuine compiled original CP013+CP014 dependency `.olean` files and CP015 `.olean`, all **NINE real** standard-only `#print axioms` lines, source SHA receipts, and no admitted axioms. Only then reports `CP015_ORIGINAL_ZETA_UNCONDITIONAL_N_1495_EQ_52_KERNEL_PASS`, expressly not ordinal 53 or spectral equality.
- `.github/workflows/cp015-source-witness-seam-manual-preflight.yml`: explicitly **OPT-IN ONLY** cheap seven-source authenticated preflight; trigger by adding PR label `cp015-source-preflight` or through `workflow_dispatch` after GitHub registers the workflow on the default branch. Ordinary PR commits do not enqueue jobs.
- `.github/workflows/cp015-original-1495-count-v435-manual-kernel.yml`: **OPT-IN ONLY** original Zeta v4.35 compiler and strict axiom audit; trigger with PR label `cp015-lean-kernel` or eligible `workflow_dispatch`. Normal PR updates do not run expensive compilation. No IV###/NF### source mutations.

**No new Lean kernel acceptance has been reported for CP015; neither opt-in workflow has been triggered.** The source proofs and external SHA checks are a new auditable compiler work item, not an executed kernel result. If a source-level type/lemma proof fails, the precise compiler errors must be repaired in a new reviewed commit before any result can be promoted.

## 5. Root-53 rank remains an independent mathematical gate

Even knowing the exact count (N(149.5)=52) and no zero at (149.5) does **not** identify the next zero's height. CP010's high-precision numerical root at `150.05352042078...` and proposed `[150.05352,150.05353]` remain **numerical candidates**, with no accepted source-derived Euler–Maclaurin sign/error proof.

To attach the first refined zero's ordinal index (53), still need **both**:
1. Genuine original Euler–Maclaurin (or alternative) kernel-certified existence inside the tiny proposed rational interval (CP010 external v4.35 still pending).
2. A rigorous local upper bound excluding another zero in (149.5<t<150.05353). Sufficient alternatives: prove (N(150.05353)=53); prove `StrictMonoOn Zeta.hardyZ (Icc 149.5 150.05353)` with an **actual uniform analytic derivative bound** and combine with original published finite RH below (g); or attach an actual indexed source containment theorem as in CP012. Finite floating-point derivative samples are not a uniform bound.

**Next CP016:** Inspect a genuine compiled CP015 proof result and repair any failing source tactic/type. If the unconditional seam theorem becomes kernel accepted, promote its exact `N(149.5)=52` and source no-seam-root results to permanent custody and move the local first-RS rank proof to the *narrow* analytic derivative problem. Focus on a rigorous sign/error method for CP010 first RS root before scaling more than a million zero refinements. The complete original signed Weil (Pole−Prime+Arch) 3×3 versus full spectral zeros equality and oscillatory quadrature are still independently OPEN.

**No global RH or Weil positivity claim.**

Original source references: https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Zeros/Interval.lean ; https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Zeros/Certificates/Basic.lean ; https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Zeros/CountCertificates.lean ; https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Gram/Certificates.lean .
