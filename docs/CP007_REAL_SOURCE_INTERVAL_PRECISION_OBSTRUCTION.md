# Weil-Lab — CP007
## First *actual* source-backed zero interval precision obstruction and complete-store analysis plan

**Independent CP### program only**, stacked on CP006 PR #810, CP005 #807, CP004 #803, CP003 #799, CP002 #796 and CP001 #790. The Phase IV IV024 PR #811, Phase III NF### numerical-custody PRs, and PI006 PR #812 remain independent. No changes to their branches.

**Certification boundary:** This is the first CP### stage that ingests actual immutable upstream positive-zero bracket DATA, rather than synthetic controls or merely declarations of a zero-count theorem. It evaluates the adequacy of the current CP006 *conservative interval error certificate*, **not the actual distance** between the true finite spectral matrix and a numerical approximation. It is NOT a newly Lean-accepted theorem, complete original signed Weil 3×3 matrix, arithmetic–spectral compatibility verdict, RH or global Weil positivity.

## 1. What was actually found in primary upstream code and files

The upstream `smmercuri/zeta` release `v1-1e6` resolves to source commit **`c06b4e13d9c847e50a32c3d738271cbad62ae9f3`**.

The genuine, newly inspected upstream source data are:
- `python/out/euler_maclaurin/zeros/manifest.json`, immutable Git blob `72a4a851de388383a885709fda35c8ec3c9c06e0`: **52** original Euler–Maclaurin positive-zero interval rows; `widen: true`, `bisection_depth: 0`, `epsilon: 0.125`, height 149.500.
- `python/out/euler_maclaurin/zeros/zeros_00001.txt`, Git blob **`6958515f7dd1be86ebe823ff6fd67ec110ec90f7`**. We copied ONLY this tiny 1,855-byte source file byte-for-byte under `data/cp007_original_euler_maclaurin_first52.txt` (it has the **same actual Git blob SHA** in Weil-Lab). Source credited to upstream Apache-2.0 project; original data was not recalculated.
- Its genuine generated Lean `Zeta/Zeros/Certificates/EulerMaclaurin/Batch0001.lean`, Git blob `a4f28786abb75420cf950ae701f5c7befcda560d`, states `theorem batch : BatchSpec 52 1000 1000 149500 1000 := by build_batch 0 52`. This is the exact first source batch that the upstream interval-generation pipeline connects to actual kernel-checkable sign-change proofs (kernel receipt still not locally reproduced).
- `python/out/riemann_siegel/zeros/manifest.json`, Git blob `9cb5d0ca577927109dabc0024cff39e2b3df51d9`: **1,747,950** more rows across seven original `zeros_00001.txt` to `zeros_00007.txt` shards, totaling **52 + 1,747,950 = 1,748,002**, matching the upstream genuine Turing-certified `certifiedZeroIntervals_length` source theorem. Their seven exact original Git blob SHA identities and expected per-file last endpoints are committed in `scripts/cp007_upstream_store_source_manifest.json`, without copying ~53 MB of raw data into Weil-Lab.
- `python/src/data_gen/gen_zero_certificates.py` directly specifies that it reads these stores and emits `BatchSpec` modules using exact source-row endpoints and `build_batch`. This gives a **concrete source-to-batch provenance route**, but external source inspection alone is not a local Lean kernel axiom audit or independent verification of every numerical zero.

## 2. A concrete, **falsifiable failure** of the unrefined CP006 error certificate

The FIRST genuine upstream row is:
```
1, 1.000, 17.846, 63, 67, 20, 20
```
Thus its original source enclosure `I1=[1,17846/1000]` has exact half-width `δ1=8423/1000=8.423`. The entire first-source batch comprises 52 **wide, tiled** intervals ending at 149.500. These are authentic upstream *certificate source inputs*, not newly invented counterexamples.

For CP006's dyadic band `2^0<=gamma<2^1` determined from the ORIGINAL LEFT ENDPOINT `1`, the original exact-rational derivative-bound weights give
`
 E_loc^CP006(only I1, r=1/1000) = 93183649/640000000 ≈ 0.1455994515625,
 E_loc^CP006(only I1, r=1/500)  = 185617651/960000000 ≈ 0.1933517197917.
`
Both values exceed **the ENTIRE planned normalized error tolerance (1/500=0.002)**, even with every other zero bracket hypothetically point-exact.

Summing the actual first 52 source rows in the same CP006 exact-rational dyadic formula gives approximately
`
 E_loc^CP006(first 52 source intervals, r=1/1000)
    = 3285711/2560000 = 1.283480859375,
 E_loc^CP006(first 52 source intervals, r=1/500)
    = 2181663/1280000 = 1.70442421875.
`
An independent local exact-Fraction recheck verified the original 1,855-byte source Git blob and BOTH complete 52-row fractions above. The new reproducible checker also calculates these results with `fractions.Fraction`, verifies the immutable Git SHA, every source index and all 52 seven-column records, and uses the prior source-bounded CP006 function rather than an independent unaudited reimplementation.

**Logic of the negative result:** CP006's localization error estimate is a NONNEGATIVE UPPER BOUND obtained by summing per-interval derivative terms. A single published raw row contributes more than the desired allowance. Consequently the **present error certificate cannot close when applied directly to the raw upstream widened brackets**. This does NOT prove the true approximation error is large; it does NOT falsify the full zeta explicit formula, CP-C1's mathematical compatibility conjecture, or RH.

## 3. Exact *refinement threshold* for the first source interval

Let `E_tail(r)` denote CP005's previously derived unconditional-count/T=10^6 high-zero tail upper bound and retain `E_quad<=1/50000` as a strictly **unverified planned allowance**. If ALL OTHER intervals had ZERO localization error (an optimistic counterfactual), the first interval's allowed half-width would have to satisfy
`
 δ1 < [1/500 - E_tail(r) - 1/50000] / L_r,
 L_r = E_loc^CP006(r; single band j=0 and sum δ=1).
`
Exact fractions imply
`
 r=1/1000: δ1 < 0.005027 (original δ1=8.423),
 r=1/500:  δ1 < 0.008031 (original δ1=8.423).
`
So the first interval needs **more than a factor 1,675** or **more than a factor 1,048**, respectively, narrower half-width under our existing CP006 estimator, even before allocating any budget to the remaining 1,748,001 intervals.

These are **method-specific sufficient-certificate requirements**. Replacing the overconservative dyadic derivative estimate with a sharper interval technique might reduce the amount of refinement required; the numbers are not intrinsic invariants of the Weil form.

## 4. New exact-data verification and complete-store audit

**Cheap fully reproducible actual-data preflight** (runs automatically):
- `scripts/cp007_original_first52_precision_obstruction.py` evaluates the literal 52-row preserved original source blob; asserts the first-row and first-52 strict failures, tests a synthetic narrow-row negative control, and records the conditional optimistic refinement threshold for both radii.
- `scripts/cp007_full_original_store_band_audit.py --self-test` confirms pinned metadata and first-source-row failure, without pretending it has read all 1.748m zeros.
- `.github/workflows/cp007-first-real-zero-store-obstruction.yml` compiles the scripts and runs their actual-data tests, avoiding an expensive original Lean build or new unrelated workflow fan-out.

**Manual full-source audit prepared (NOT executed in CP007):**
- The same `cp007_full_original_store_band_audit.py --upstream-source-root DIR` accepts exactly the two upstream original manifests, ALL eight external data shards and original Euler batch source, checks every immutable Git blob SHA, validates exact row counts, source indices, boundary order and no overlap, and computes **the complete original 1,748,002-zero dyadic budget** with exact fractions. It emits a short explicit report with `SOURCE_DATA_ERROR_BUDGET_EXCEEDED` or `SOURCE_DATA_BUDGET_BELOW_THRESHOLD`. These are **mathematical data-budget assessments only**, never positive spectral/Lean certifications.
- `.github/workflows/cp007-full-original-store-manual-audit.yml` is deliberately **workflow_dispatch only** because repository CI remains queued across IV###, NF### and CP###. The workflow fetches pinned exact external source URLs (~53 MB of data), hashes every original blob and emits a report. We do not add additional heavy automatic backpressure to canonical Phase IV.
- The full data SHA manifest is traceable to exact original upstream release contents and captures both distinct zero-generation methods. Neither default source manifest reports `bisection_depth>0`: the broad published tiling is part of the original computational proof design, not evidence of a missing theorem.

**Important**: even a SHA-perfect 1,748,002-row upstream store plus generated `BatchSpec` source is not a Weil-Lab kernel-accepted theorem without actual compiled upstream trust receipts, verified per-row batch correspondence, and complete original signed Weil arithmetic–zero pairing dictionary.

## 5. Research implications and next CP008

CP007 eliminates a false shortcut: **the existing published broad intervals cannot simply be plugged into the CP006 spectral comparison and declared precise enough**.

The two actual remedies have materially different verification costs:
1. **Refine** the actual zero brackets with fresh, source-linked narrow rational intervals, and prove each refined root lies inside its original kernel-certified interval, with an independently accepted sign-change or equivalent interval-root proof. Re-run the adaptive weighted bound on ALL 1.748m after refinement. The early rows must be treated first.
2. **Improve the estimator** using direct interval-enclosed signed cosine moments or finer frequency subdivisions, without silently selecting a midpoint unsupported by the original bracket. Cancellation/oscillation estimates must be rigorously justified across every supplied interval and cannot be inferred from a point value or signed row average.

**Next CP008:** identify and certify a deterministic refinement for the first 52 source-batch intervals (pilot first zero), link it to the upstream `EulerMaclaurin.Batch0001` proof without importing incompatible `.olean` into Weil-Lab v4.34, and find a scalable precision/complexity budget for the remaining RS rows. Only after that can a full original Pole–Prime–Gamma versus complete finite-cosine-moment comparison become a defensible test. No global Weil positivity or RH claim.

**Primary source:** https://github.com/smmercuri/zeta/tree/v1-1e6/python/out ; https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Zeros/Certificates/EulerMaclaurin/Batch0001.lean ; https://github.com/smmercuri/zeta/blob/v1-1e6/python/src/data_gen/gen_zero_certificates.py ; CP006 PR #810; IV024 PR #811. Source data is credited to Salvatore Mercuri and collaborators under Apache-2.0.
