# Weil-Lab — CP016
## Ordinal identity of the original first Riemann–Siegel zero, without indexed numeric source rows

**Track:** independent CP### cross-projection, stacked on CP015 PR #836 → CP014 #831 → CP013 #829 → CP012 #827 → CP011 #825 → CP010 #822 → CP009 #819 → CP008 #817 → CP007 #815 → CP006 #810 → CP005 #807 → CP004 #803 → CP003 #799 → CP002 #796 → CP001 #790. The original Phase IV IV### signed Weil support-extension compiler, NF### Phase III original numerical enclosure ledger, and PI### separate pole/prime/Gamma interface remain unchanged.

**Proof status: SOURCE MATHEMATICAL DERIVATION + UNCOMPILED LEAN 4.35 CANDIDATES**. Do NOT promote to an accepted new kernel theorem until the true upstream-original Lean `.olean`, standard-axiom checks and dependency compiles return completed PASS. No new global RH or global Weil positivity is claimed. The original external published source's bounded-height counting, zero simplicity and RH have a distinct proof lineage; the newly authored CP013/CP014/CP015/CP016 source theorems are NOT thereby kernel accepted.

## 1. Recovery and explicit CP015 open-height repair

The original CP015 PR #836 head `9ef7d25830d3c5191502fe1dbab7ef05c31589fa` and CP014 #831 / CP013 #829 source workflows remained QUEUED. CP015 intentionally does not automatically trigger heavy compilation because the NF###/IV### CI queue is congested.

CP016 rechecked the actual CP015 source statement `no_original_zero_exactly_at_149500_div1000`. **Concrete proof defect found:** to include a hypothetical zeta zero with ordinate exactly 149.5 in the original `zerosUnder g` finset, one needs (149.5<g), not merely (149.5\le g). The source candidate previously tried to supply `eulerCutLeGram` to this strict upper bound. CP016 commits `eulerCutLtGram`, correctly deducing the **strict** inequality:

```
  149.5 < 1000449.286 < 1000449.28682 <= original gramPoint g.
```

The last inequality uses original `certifiedGramBlockSeq.head_left_le_gramPoint`. This repairs a real Lean proof-signature mismatch in CP015; further compiler issues may remain. It does not change original mathematical facts or assert that the repaired source was kernel accepted.

## 2. An actual new mathematical result: the SOURCE-DEFINED first RS zero must be the 53rd positive-height zero

The source-original independent CP013/CP015 candidate constructs real finite sets
```
 E := (CP013Seam.first52Euler.bundle.zeros).toFinset
 R := (CP013Seam.allRS.bundle.zeros).toFinset
 S_g := {s : ζ(s)=0, 0<Im(s)<g}
```
from authentic published `CertifiedZeroIntervals.zeros`, `zeros_spec`, `zeros_length`, `zeros_nodup`, original `N(g)` and original finite-height simplicity.

If CP013+CP014+CP015 compile successfully, they give
```
  |E|=52; |R|=1747950; E∩R=∅; S_g=E∪R;
  ∀e∈E, Im(e)<149.5;
  ∀r∈R, Im(r)>149.5.
```

**The finite nonempty R has a least ordinate**: choose (\rho_{\min}\in R) such that (\Im\rho_{\min}\le\Im r) for every (r\in R). This is an instance of original Mathlib `Set.exists_min_image`, not a numerical zero-oracle.

For *any* positive-height zeta zero (w) below the ordinate of (\rho_{\min}), the complete source partition implies (w\in E\cup R). It cannot belong to R by minimality; therefore it belongs to E. Conversely all E roots are below 149.5 and (\rho_{\min}) is strictly above 149.5. Hence as an **exact set identity**
```
 { w∈S_g : Im(w)<Im(ρ_min) } = E.
```

Original finite-height `order_eq_one_upto` and `N_eq_sum` give `N(T)=card(zerosUnder T)` for (T\le g). Therefore

```
  N(Im(ρ_min)) = |E| = 52.
```

The point (\rho_{\min}) is a genuine zeta zero, so **its intrinsic positive-zero ordinal rank is 53**. The *source-defined* first RS zero is unique as a complex zero: any two source choices minimizing the ordinate have the same imaginary part, and the original finite-height RH ensures they both have real part 1/2. An extra zero in the open gap `(149.5, Im(ρ_min))` is impossible.

**This is stronger than CP015's cut theorem.** It identifies the original first RS zero by ordinal rank **without** supplying the original private source row #1's right decimal endpoint, relying on fake equality of abstract `Classical.choose` bundle witnesses or assuming an otherwise unknown new local zero count near 150.05353.

**Crucial limitation:** this does **NOT** yet prove that the original rank-53 zero lies in the new numerical candidate `(150.05352,150.05353)`. The original first source row endpoint and CP010's proposed narrow Euler kernel sign proof remain open. The source-built canonical identity and a numerical ordinate enclosure are two different types of information.

## 3. New original-source Lean theorem candidate: exact ordinal #53 and empty preceding gap

New `cp011_zeta_v435/CP016FirstRSRank.lean`, isolated original Lean 4.35:
- `exists_least_original_RS_witness`: obtain a genuine finite minimum of R's imaginary ordinate through original Mathlib finite-set theorem.
- `original_roots_below_least_RS_are_exactly_Euler`: exact real zero roster prefix equality, exploiting source exhaustion and minimality.
- `N_at_original_least_RS_root_eq_52`: original multiplicity-correct count exactly 52 at the first RS source root's height.
- `original_53rd_positive_zeta_zero_exists`: concrete existence of the positive-zero ordinal 53, source-defined but WITHOUT a new narrow numeric bound.
- `original_first_RS_zero_has_no_preceding_zero`: no nontrivial zero in the open region (149.5<\Im s<\Im\rho_{\min}).
- `original_least_RS_root_unique`: uniqueness of the source-minimum positive complex zero, using original finite-height RH (only in the source-certified finite window).

These source declarations invoke the actual original upstream `Zeta` published facts and new CP013–CP015 source candidates. They contain no `sorry` and no new axioms; they still need a genuine compiler run.

## 4. A falsifiable NARROW-root compatibility bridge that avoids missing indexed source coordinates

New separate `cp011_zeta_v435/CP016MonotoneAttach.lean` provides a precise conditional dictionary.

Let (c=149.5), let (g) be original certified Gram point, and suppose (c<t<b<g) is an independently rigorously certified Euler/RS zero:
```
  ζ(1/2+i t)=0.
```

Original full source zero exhaustion implies `1/2+i t∈R` (it is too high to belong to E). Hence the *source-minimum* RS zero (\rho_{\min}) has `Im(ρ_min)≤t`.

Now if a genuine analytic/interval certificate proves
```lean
  StrictMonoOn Zeta.hardyZ (Icc 149.5 b)
```
on the ENTIRE compact interval, the original source theorem `hardyZ_eq_zero_iff_riemannZeta` and CP014's conditional monotone-root uniqueness force
```
  ρ_min = 1/2+i t.
```
Thus the new refined zero has genuine ordinal 53. This is a **precise compatibility theorem** with independently falsifiable premises, without requiring an indexed original source-row endpoint theorem.

**This is NOT yet a complete root attachment**: CP010's proposed narrow `[150.05352,150.05353]` Euler `build_batch` source candidate has not been kernel accepted, and source `StrictMonoOn hardyZ` is NOT established by the 17-point high-precision derivative sample from CP014. The true rigorous task is a uniform bound (Z'(x)>0) throughout `[149.5,150.05353]`, or an independent count upper bound (N(150.05353)=53). Neither is assumed. All nontrivial zeros in this finite range are already known by the original externally certified bounded-height RH to lie on the critical line.

CP016's existence of a source-defined first RS zero and CP016's **conditional** equality with a numerical refined root must NEVER be conflated.

## 5. Immutable source controls, exact model negative tests, and actual compiler custody

Re-fetched primary original mathematical sources at `smmercuri/zeta@c06b4e13d9c847e50a32c3d738271cbad62ae9f3`:

| Source | Git blob | Used fact |
|---|---|---|
| `Zeta/Zeros/Interval.lean` | `152954545ca9997c2a2ddaead4d9161ffbbfe191` | Genuine `CertifiedZeroIntervals.zeros_nodup`, `zeros_spec` |
| `Zeta/Zeros/CountCertificates.lean` | `a3e729d23802c3731432de9a3c7d46d18252ba10` | Original full source complete count |
| `Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean` | `c2b1da101a580cc91cfb0a43d72d5839fd97265c` | Original `N_gramPoint_eq`, `order_eq_one_upto`, finite-height RH |
| `Zeta/Zeros/HardyZ.lean` | `9975442b0c14011c35f4624197d0bf26169c7665` | Original `Zeta.hardyZ`, zero↔Hardy Z bridge |
| Original Mathlib 4.35 `Mathlib/Data/Set/Finite/Lemmas.lean` | `de41c17e1d3056674b274a6b3e695a9e20c87a25` | Original genuine `Set.exists_min_image` |

New `scripts/cp016_original_first_RS_ordinal_source_gate.py` verifies all five pinned upstream blobs, checks authentic theorem signatures, the CP015 strict-cut repair, six new rank theorems and conditional rank attachment source. `--self-test` verifies an **exact rational finite-roster** model where the first RS is rank 53, and a negative control where a separately suggested narrow numeric root can be rank 54 without a missing local rank theorem. A source-only success is labeled `CP016_PINNED_SOURCE_AND_ORDINAL_MODEL_PASS_NOT_LEAN`.

New `scripts/cp016_original_firstRS_rank_lean_axiom_audit.py` is **FAIL-CLOSED**: actual original Zeta v4.35 compiled CP013/CP014/CP015 dependencies and BOTH CP016 `.olean` files, true source `#print axioms` for all **eight** new declarations, no `sorryAx`, only original standard axioms `propext, Classical.choice, Quot.sound`. A resulting genuine pass would certify source-defined ordinal 53 and the conditional monotone attachment theorem, **not** the narrow numerical enclosure or actual Hardy Z monotonicity.

Two opt-in only workflows:
- `.github/workflows/cp016-source-rank53-opt-in-preflight.yml`: run by explicit PR label `cp016-source-preflight` (or eligible manual dispatch), original SHA/source/Fraction check, not Lean.
- `.github/workflows/cp016-original-firstRS-rank53-lean-kernel-opt-in.yml`: explicit PR label `cp016-lean-kernel` (or eligible manual dispatch), original full Lean 4.35 source dependencies + genuine .olean and axioms. No PR-created/PR-updated/push job fanout; protect independent IV###/NF### backlog.

**At PR creation no new source preflight or Lean kernel pass is presumed. No label has been applied and no expensive workflow dispatched.** The source proof is valuable as an explicit falsifiable compiler task, not as a fabricated accepted proof.

## 6. New preservation law and the next true obligation

**Source-intrinsic:** the genuine 53rd positive-height zeta zero (\rho_{53}), defined as the least positive zero above the first 52 and below the real certified cutoff, is independent of Euler vs RS approximant methods, numeric source batch boundaries, private existential witness choices, or coordinate resolution. Its ordinal count is mathematically forced by the original fully saturated finite zero roster.

**Source presentation dependent:** whether a particular generated batch's first row has right endpoint `150.1` or some other rational, and whether an independently refined numerical root lies within that specific original row.

**Analytic/certificate dependent:** an accepted refined Hardy Z root bracket near `150.05352042` and a uniform local strict monotonicity certificate. These are sufficient to identify the numerical candidate with the intrinsic source rank-53 zero, but they are not established by the original root count or a nonrigorous derivative sample.

**Next CP017**: recover actual CP016 compiler output or repair the first concrete Lean type error. Pursue genuinely certified local monotonicity or a direct original finite-height rank count upper bound, plus true CP010 first root narrow Hardy Z sign/error certificates, and only then attach numerical zero #53. Do not flood CI while IV###/NF### queued work is outstanding. Original signed Weil `Pole−Prime+Arch` 3×3 zero-side normalization, full RS refined roster and oscillatory/quadrature terms remain independently OPEN.

**NO GLOBAL WEIL POSITIVITY OR RH CLAIM.**
