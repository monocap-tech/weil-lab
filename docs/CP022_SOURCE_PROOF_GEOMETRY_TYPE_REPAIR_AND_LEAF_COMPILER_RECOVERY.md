# Weil-Lab — CP022
## Concrete original-v4.35 leaf geometry type repair, stronger frozen Mathlib API custody, and ordered two-stage kernel diagnostics

**Scope:** independent CP### cross-projection proof/custody, stacked on CP021 PR #843 (then CP020 #842, CP019 #840, CP018 #839, etc.). No change to original Weil signed-support **IV###**, numerical matrix acceptance **NF###**, or independent **PI###**. No RH or global Weil positivity claim.

### 1. Live original compiler evidence, NOT a completion claim

At inspection, GitHub head for CP021 PR #843 was `bd9eb61b98d37465c2d27ac2f738f5f248805cd5`. Its CP013 and CP014 inherited source Actions runs `44878586071` and `44878586072` were **QUEUED**; no accepted CP021 standalone leaf `.olean` or genuine `#print axioms` logs were available.

Current container test: `command -v lean` and `command -v lake` return no compiler, and `curl github.com` fails DNS resolution. There is **no genuine local Lean4.35 kernel**. This CP022 cycle thus performs source/primary-API proof audit and repairs *provable source errors*, then prepares forensic actual-kernel jobs for explicit future dispatch. It must not call static source inspection a compiler result or assume queued CP013/CP014 passed.

### 2. Found a concrete Lean proof TYPE defect, not a mathematical gap

In original both `CP021BorweinLeaf.source_circle_geometry` and inherited `CP020BorweinCircle.source_circle_geometry`, the authors had used:

```lean
simp [norm_mul, abs_of_nonneg ht.1]
```

But `ht : t ∈ Set.Icc a b` and `a=149.5`, so `ht.1 : a ≤ t`, whereas `abs_of_nonneg` requires **`0 ≤ t`**. The inequality is mathematically true; the original argument simply supplied a proof of the **wrong type**.

CP022 explicitly derives the missing bridge from the exact rational lower endpoint:

```lean
have ht_nonneg : (0 : ℝ) ≤ t := by
  have ha_nonneg : (0 : ℝ) ≤ a := by norm_num [a]
  exact ha_nonneg.trans ht.1
```

and then uses:

```lean
simp [norm_mul, abs_of_nonneg ht_nonneg]
```

This is a source-level **type-correct repair of the explicit hypothesis**, but still requires true Lean elaboration/compilation to establish the complete original theorem. There are potentially other new proof errors. The duplicate inherited CP020 source proof was repaired simultaneously so the future original integration does not reintroduce the same invalid `abs_of_nonneg` argument.

CP022 also replaces a fragile

```lean
rwa [hdist] at this
```

in the same norm triangle proof with

```lean
simpa only [hdist] using this
```

to explicitly deliver the derived inequality to the goal rather than rewriting only a local hypothesis. This is proof hygiene; not evidence that the remaining source theorem compiles.

### 3. Expanded authentic original Mathlib declaration custody from five to seven source blobs

Reopened two original Mathlib v4.35.0 files not previously included in the CP021 preflight SHA contract:

| Original source | Immutable Git blob | Directly observed declarations |
|---|---|---|
| `Mathlib/Analysis/Complex/Norm.lean` | `0e2b6317a777c4d168a9098fb17ad33323efd4c3` | true `Complex.abs_re_le_norm` used by the circle geometry |
| `Mathlib/Analysis/SpecialFunctions/Pow/Real.lean` | `97c12aed7085a7fc77727567d87e508064b49a18` | true `Complex.norm_cpow_eq_rpow_re_of_pos`, `Real.rpow_neg`, `Real.rpow_le_rpow_of_exponent_le` used by the original complex-power estimate |

The previous FIVE immutable primary sources remain unchanged:
- frozen original Zeta `Zeta/EulerMaclaurin/Continuation.lean`, `1bb01e946fa7e344497eaf7694fbecff0a714d09`;
- frozen original Zeta `Zeta/EulerMaclaurin/ErrorBound.lean`, `01184af0dbfd1369e14725e02e990b016bedfe6f`;
- `Mathlib/RingTheory/Polynomial/Pochhammer.lean`, `f3503627af3430a48c087b85b03095e84dfb2824`;
- `Mathlib/NumberTheory/Bernoulli.lean`, `45d389886738789e80185fd2a6da4185727ab502`;
- `Mathlib/Analysis/Calculus/IteratedDeriv/Lemmas.lean`, `d9348833bece1297dd8ffe57e6b976fcc268af38`.

**7/7 source file SHA+genuine theorem-signature checks** follow from actual direct GitHub source retrieval. Again, this is **source provenance**, not new local original Lean kernel acceptance.

### 4. Independent fail-closed preflight now actively blocks reintroduction of the bad source proof

`scripts/cp021_independent_leaf_v435_source_kernel_gate.py` now:
- Checks *seven* actual pinned original Zeta/Mathlib source blobs and exposed exact source declarations, not five;
- Requires the explicit `0≤t` chain and correct `abs_of_nonneg ht_nonneg` in `CP021BorweinLeaf.lean`;
- Rejects use of `abs_of_nonneg ht.1`, since its argument has the wrong type in this source context;
- Requires `simpa only [hdist] using this`, the explicit norm triangle conclusion;
- Continues to reject local `CP013–CP020` imports in either original source leaf and checks the exact **13** theorem names, `#print axioms` targets, no new `sorry`/axiom/constant declarations.

The matching **source-only opt-in workflow** `.github/workflows/cp021-original-independent-leaf-source-only-opt-in.yml` now downloads the two additional Mathlib files and demands the **7/7** real source gate. It remains strictly label/manual, without ordinary PR/branch build fan-out.

The genuine kernel workflow `.github/workflows/cp021-original-independent-leaf-v435-lean-kernel-opt-in.yml` was revised to capture the FIRST actual compiler failure separately:

1. `lake build CP021GermLeaf` (true original external v4.35, original Zeta+Mathlib only), log `cp022-first-actual-upstream-germ-leaf-build.log`.
2. If that passes, `lake build CP021BorweinLeaf`, log `cp022-second-actual-upstream-borwein-leaf-build.log`.
3. If both pass, re-elaborate both sources to capture the **13** actual original standard-only `#print axioms` receipts and require both compiled `.olean` files through the fail-closed audit.

The workflow does NOT compile any new source from CP013–CP020, and no additional ordinary push/PR runner jobs are triggered. At CP022 PR creation this job is **NOT dispatched**; queued original NF/IV work retains priority.

### 5. Mathematical content and remaining obligations

The original exact rational Borwein envelope is unchanged:

[
\frac{656}{53}\frac{7}{6\cdot14!}
\frac{\prod_{j=0}^{12}(151+j)}{256^{13}}
=\frac{181596617021805363}{633825300114114700748351602688}
\approx2.865089433777896\cdot10^{-13}
<3\cdot10^{-13}.
]

CP021's two independent mathematical source candidates remain:
- **10** original complex Borwein all-circle theorems (`CP021BorweinLeaf`);
- **3** exact original complex zeta/EM derivative germ identity theorems (`CP021GermLeaf`).

A real acceptance of both, plus the separately original holomorphic/Cauchy derivative transfer, could help bound the derivatives of `riemannZeta - zetaApproximant`. It **cannot by itself** establish the full Hardy-`Z` derivative anchor, uniform curvature, numerical first RS zero identity, or full original Weil–spectral 3×3 comparison.

Remaining independent proof obligations:
- Genuine original v4.35 compiler logs and kernel-accepted `.olean` receipts for both isolated leaves (still absent).
- Actual proof of the source Euler–Maclaurin holomorphic Cauchy integration (CP019 has source candidates, not kernel acceptance).
- Validated interval arithmetic for finite original (A_{6,256}), its complex first and second derivatives, and the correlated original theta/digamma phase, not just the remainder.
- Actual Hardy-(Z) derivative anchor (Z'(149.5)\ge12/5), true uniform (|Z''(t)|\le4) over ([149.5,150.05353]), genuine CP010 narrowed root sign certificate, and CP016 original intrinsic ordinal 53 attachment.
- The original signed Weil Pole−Prime+Arch (3\times3) equality against the **complete** spectral/zero-side form; RH/global Weil positivity remain **open**.

**Next — CP023:** Recover real first-leaf compiler error logs from the label/manual opt-in original v4.35 kernel workflow as queue permits. Repair actual type errors individually and never promote an uncompiled source candidate to kernel acceptance. Continue source-compatible finite approximant/phase interval enclosure development only after proof custody is credible.

**Result level:** one **verified source-type error found and corrected in two locations**; two Mathlib proof API sources newly SHA-pinned; independent opt-in compilation reordered for useful partial diagnostics; real kernel acceptance still pending.
