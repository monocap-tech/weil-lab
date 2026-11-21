# Weil-Lab — CP011
## Exact canonical zero-slot identity from the genuine upstream Turing count, and a source-first row containment gate

**Independent cross-projection CP### track**: CP011 stacked on CP010 PR #822 → CP009 #819 → CP008 #817 → CP007 #815 → CP006 #810 → CP005 #807 → CP004 #803 → CP003 #799 → CP002 #796 → CP001 #790. The active Phase IV IV### original signed Weil support-extension/Lean certification, Phase III NF### physical numerical enclosure, and PI### alternative arithmetic/Gamma interface work are **separate and unchanged**.

**Current proof status:** CP011 independently establishes the mathematical *deduction* that the external complete Turing count enforces a unique original positive-height zero in every original certified interval, with an exact no-sorry Lean **source proof CANDIDATE** under isolated upstream v4.35. A real actual external `.olean`/Lean axiom receipt for this new lemma was not available at creation, and original CP008 first-52 and CP010 root53 narrow interval candidates have no accepted new kernel proof. The original v4.35 `smmercuri/zeta@v1-1e6` formal finite height proof and its original source declarations remain a distinct external trust boundary. The actual first original RS row has NOT yet been read by the connector (the 7.34MB original source fetch exceeds the direct file-extraction limit), so CP011 explicitly arranges a small separate SHA-pinned source audit rather than inventing its endpoints. Never claim current arithmetic–spectral equivalence or RH/global Weil positivity.

## 1. Genuine source dictionary: the completeness theorem already enforces **per-slot uniqueness**

All external source observations below were re-fetched at exact immutable commit `c06b4e13d9c847e50a32c3d738271cbad62ae9f3`:

| Source file | Original Git blob | Actual exposed structure |
|---|---|---|
| `Zeta/Zeros/Interval.lean` | `152954545ca9997c2a2ddaead4d9161ffbbfe191` | `CertifiedZeroIntervals`, `intervals : List (NonemptyInterval ℝ)`, `has_zero : ∀ I ∈ intervals, ∃ t ∈ Ioo I.fst I.snd, ζ(1/2+it)=0`, `disj : intervals.IsChain (fun I J => I.snd ≤ J.fst)`, `zeros`, `zeros_length`, `zeros_nodup`, `zeros_spec`, `pairwise` |
| `Zeta/Zeros/Count.lean` | `b8c458cca723b20cdf71a5f8d662d9d8e952c983` | `CertifiedZeroCount` extends counted Gram and zero bundles, requiring matching Turing count and `below : Z.height ≤ gramPoint Z.minIdx` |
| `Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean` | `c2b1da101a580cc91cfb0a43d72d5839fd97265c` | Real `riemannZeta.N_gramPoint_eq Z : N(g)=Z.intervals.length`, `riemannZeta.le_N_of_zeros`, proofs excluding extra off-line zeros and proving simplicity |
| `Zeta/Zeros/Certificates.lean` | `54fce07cbc5bf0913ceccb108cbf73f1227857c0` | Actual `certifiedZeroIntervals_length : … = 1748002` |
| `Zeta/Zeros/CountCertificates.lean` | `a3e729d23802c3731432de9a3c7d46d18252ba10` | Concrete `certifiedZeroCount`, with original generated Turing `count` and `below` proofs |

The source's existing `Z.zeros_nodup` establishes that choosing ONE genuine zero `ρ_k` in the OPEN interior of each of the (n) disjoint original intervals `I_k` yields `n` distinct positive-height zeta zeros. The real count theorem says:

```
  N(g) = n,  n = 1,748,002.
```

The `N` count is with multiplicities and every positive-height zero contributes ≥1. Therefore if an additional zero `s` of any real part with `0<Im(s)<g` were missing from the `n` chosen zeros, the enlarged list `s :: Z.zeros` would be a nodup list of `n+1` zeros. The **existing source theorem** `riemannZeta.le_N_of_zeros` implies `n+1≤N(g)=n`, contradiction. Hence:

```
  ∀ 0<Im(s)<g, ζ(s)=0  =>  s ∈ Z.zeros.                 (CP011-C1)
```

Since the witness list is assembled **one chosen zero per original disjoint open interval**, and an interior point cannot simultaneously belong to two of these intervals, it follows:

```
  ∀ k,  ∀ s,t with Im(s),Im(t)∈(I_k.fst,I_k.snd)
         and ζ(s)=ζ(t)=0, we have s=t.                  (CP011-C2)
```

This is **a mathematical theorem deduced from the actual upstream certificate fields**, not an independent assumption that an arbitrarily narrow high-precision interval is already certified, and not a claim that the new CP011 Lean source was compiled.

### Consequence for the two-method projection

If a real independent refined Euler `J^E_k` and a real refined RS `J^R_k` are each **proved by the original Lean analytic sign-error tactics to contain a zero**, and both are **source verified as subsets of the same original** `I_k`, then their zeros must be the **same canonical original zero**. In fact, **one** such refined certified interval suffices to give a rigorous ordinate enclosure of the canonical zero, provided source containment `J_k⊂int(I_k)` is established. **No separate local uniqueness axiom and no extra RS-vs-Euler spectral equivalence claim are required.**

The source-index dictionary is: 52 published original low-height Euler rows first; original RS local row `1` corresponds to global positive-zero index `53`. This assumes original generated batch assembly order and count, which upstream's source `Zeta/Zeros/Certificates.lean` and original generator/manifest explicitly provide. The root `γ_{53}` numerical center near 150.05352042078488 is an independently computed numerical guide, NOT part of the proof.

## 2. Genuine source-linked Lean 4.35 proof candidate, using exact original declarations

CP011 creates a separate `cp011_zeta_v435/` Lake environment pinned to external `smmercuri/zeta@v1-1e6`, **Lean v4.35.0**, without upgrading original Weil-Lab v4.34.0. The original external upstream `Zeta.Main` is imported unchanged.

New `CP011CanonicalRoster.lean` has **no sorry and no new axioms**. It proposes four exact source mathematical theorems:

1. `every_positive_zero_is_original_witness (Z : CertifiedZeroCount)`: any positive zero below original Gram `g` belongs to `Z.zeros`, directly applying existing `le_N_of_zeros` to `s :: Z.zeros`, and original `N_gramPoint_eq Z`.
2. `unique_zero_in_original_slot`: any two zeros with ordinates strictly inside the same original interval are the identical complex zero, combining (1), the source's exact `zeros` witness mapping and its proven pairwise interval separation.
3. `refined_root_identifies_original_slot`: given any `k : Fin Z.intervals.length`, an externally **actually certified** refined zero inside original slot `k` equals the source-chosen zero in that slot, with an explicit source-index witness `t`.
4. `pinned_external_positive_root_is_member`: specialize (1) to the concrete 1,748,002-zero `certifiedZeroCount`.

Each is a REAL Lean theorem source candidate, **NOT** Lean accepted before actual compiler/audit receipts. They do NOT prove CP008 or CP010's proposed narrow brackets' Hardy-Z endpoint signs, and are intentionally not imported into the canonical Weil-Lab IV### v4.34 proof modules.

**Manual-only** `.github/workflows/cp011-original-v435-roster-uniqueness-manual-kernel.yml` pins the exact upstream full commit before the real `lake build CP011CanonicalRoster`, logs genuine `#print axioms` for all four declarations, and runs the fail-closed source/.olean/standard-axiom auditor `scripts/cp011_original_roster_lean_axiom_audit.py`. This extra computational build is NOT triggered automatically because existing IV###/NF### queues are still backlogged. Until a completed build returns, this is merely a proof candidate.

## 3. Exact original RS source ROW is a separate, falsifiable gate

CP010 had proposed two candidate source-specific intervals for **global positive zero #53**, the first `RiemannSiegel` store row:

```
 Coarse original RS method:     J_RS = [150.00, 150.10].
 Narrow independent Euler:      J_EM = [150.05352, 150.05353].
```

There are THREE DIFFERENT predicates:
```
 (A) J_EM ⊂ int(J_RS)                          [EXACT RATIONAL PASS]
 (B) J_RS ⊂ int(original source RS row I_53) [OPEN until whole source shard is actually read]
 (C) Both J_EM and J_RS contain proved zeros [OPEN until true kernel Hardy-Z sign receipts]
```

Predicate (A) is not (B), and (B) is not (C).

CP011 adds `scripts/cp011_first_rs_source_slot_identity.py`. With **real original source** input, it demands:
- Exact entire original 7.34MB first RS shard `python/out/riemann_siegel/zeros/zeros_00001.txt`, immutable Git blob `1029bed8a315d1b39d7c45e55a6476acbbf8baf1`.
- Exact original `Zeta/Zeros/Certificates/RiemannSiegel/Batch0001.lean`, Git blob `12848f56d0b62df858dcb89b708a858f4f7b28fb`, which actually states `BatchSpec 200 149500 1000 474603 1000 := by build_batch_rs 0 200`. This batch exposes the first interval's LEFT endpoint and the 200th RIGHT endpoint; it does **not** expose the original first row's right endpoint, which the auditor reads from the actual SHA-verified store, not from the batch bound.
- The authentic 52-row Euler source Git blob, exact count 52 + 1,747,950 = 1,748,002, source local-index 1→global-index 53 and both exact candidate stores.
- Exact *strict* containment `I_53.fst<150.00<150.05352<150.05353<150.10<I_53.snd`; this is a falsifiable check, not asserted true before real source read.

If ANY original source hash, batch declaration, count, source index or strict containment fails, the auditor returns **NOT_READY**, not a selectively widened guessed source interval. A success reports only `EXACT_SOURCE_SLOT_CONTAINMENT_ONLY_NOT_LEAN`, and emits the actual original source endpoints for independent reproducibility.

The **small PR-triggered** source-validation workflow `.github/workflows/cp011-root53-real-source-gate.yml` downloads the two pinned original ~7.3 MB + 1.3 KB files, executes exact SHA and rational source checks, and retains a receipt. This is *not* an expensive Lean compile. At initial commit no workflow result is presumed.

## 4. What is intrinsic, what depends on coordinates, and what CP011 does NOT prove

**Intrinsic:** the identity of each genuine zeta zero as a complex number; multiplicity; no extra positive zeros below the source-certified Gram point; exact equality of a new rigorously enclosed zero with its original source slot's sole zero. These consequences survive any new genuinely certified interval refinement strictly inside the same source slot.

**Dependent on source presentation:** the integer `53` as a particular list slot in the specific count-ordered Euler+RS decomposition, the width and endpoints of the original broad source intervals, and whether a new proposed narrow interval sits strictly inside that source slot. Reindexing batches or switching the published Gram cutoff changes the representational dictionary, not the underlying zero.

**Dependent on frozen Schwartz bump/numerical technique:** the CP005–CP010 `1/500` normalized spectral tolerance, the dyadic `Φ` decay constant, the `2×10^-9` blanket RS root half-width, the `5×10^-6` exception at #53, and the strict quadrature allowance. These are certificate sufficiency conditions, NOT invariants of the original signed Weil form.

**Still OPEN:**
- Actual external v4.35 kernel/axiom build for new CP011 source uniqueness and CP008/CP010 existence candidates;
- Actual SHA-verified original root53 source-row and true first RS candidate containment (now a concrete CI job);
- All 1,747,950 independently certified refined Riemann–Siegel intervals;
- Formal complete finite transformed cosine moments and `Φ` quadrature;
- The complete **original source** signed Weil (Pole - Prime + Arch) 3×3 matrix and source-faithful explicit-formula/zero-side normalization;
- Global signed Weil positivity and RH: expressly NOT asserted.

**Next CP012:** recover live source containment/Lean outcomes; if any CP011 source proof fails to compile, repair its precise type/error while preserving the mathematical theorem; if CP008/CP010 local certified brackets pass, attach the source-unique zero identity to the actual new ordinate and prioritize high-impact root refinements under CP009's exact dyadic budget. Continue IV### and NF### entirely independently, without unverified kernel claims.

Primary source: https://github.com/smmercuri/zeta/tree/v1-1e6/Zeta/Zeros ; exact source implementation https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Zeros/Interval.lean ; https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Zeros/RiemannHypothesisUpTo/Basic.lean ; CP010 draft https://github.com/monocap-tech/weil-lab/pull/822.
