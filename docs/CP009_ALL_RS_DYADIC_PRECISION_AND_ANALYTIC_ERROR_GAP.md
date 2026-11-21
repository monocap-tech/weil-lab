# Weil-Lab — CP009
## Exact all-RS-root precision policy, original analytic Riemann–Siegel error-floor obstruction, and fail-closed source/Lean receipt gates

**Canonical independent CP### stage:** stacked CP009 on CP008 PR #817 → CP007 #815 → CP006 #810 → CP005 #807 → CP004 #803 → CP003 #799 → CP002 #796 → CP001 #790. The original Phase IV IV### support-extension program and the Phase III NF### numerical compiler program continue unchanged; PI### trace tests remain a distinct alternative construction.

**Proof status:** CP009 gives an exact mathematical **sufficient** uniform/dyadic precision schedule and independently source-audits the original Riemann–Siegel analytic error term. A new source-nested refined RS *list* has **not** been produced, no external Zeta v4.35 `.olean` for CP008's proposed 52 brackets is accepted, and the original v4.34 mixed signed Weil arithmetic/spectral identity is not established. In particular, an error tolerance is NOT a numerical enclosure or a proof about a zero location. No global Weil positivity or RH.

## 1. Actual CP008 and upstream original Lean source status

At CP009 kickoff, CP008 numerical preflight workflow 44857421560 was **QUEUED/PENDING**, not PASS. The original CP008 isolated `CP008First52.refinedCandidateBatch : BatchSpec 52 1413472 100000 14742277 100000` is a real Lean SOURCE CANDIDATE using original `Zeta.Zeros.BuildCerts`; its expensive v4.35 proof workflow is manual-only and has not supplied a kernel/axiom receipt. Thus CP009's improved RS precision allowances always say **conditional on certification of the first 52 exact CP008 intervals**.

CP009 separately reopened and verified the original **Riemann–Siegel**, not Euler–Maclaurin, source:
- `smmercuri/zeta@c06b4e13d9c847e50a32c3d738271cbad62ae9f3`;
- `Zeta/Zeros/BuildCertsRS.lean` (Git blob SHA `2dbddd3716bfabbcd92390b6f25c554045179349`): `build_batch_rs lo hi` reads `python/out/riemann_siegel/zeros`, preserving the original 3-column `idx,left,right` source row and checking `ZIntervalRS.Certified` (either `Certificate₀` or the full `Certificate`) by actual `Zeta.Certificate.NamedRS` ball arithmetic;
- `Zeta/Zeros/Certificates/RiemannSiegel/Batch0001.lean` (SHA `12848f56d0b62df858dcb89b708a858f4f7b28fb`): source theorem `theorem batch : BatchSpec 200 149500 1000 474603 1000 := by build_batch_rs 0 200`, pinpointing the first **200** original RS root rows. This first RS batch is **after** the original first 52 Euler roots; RS row `1` corresponds to global zero index `53`, not to `1`;
- `Zeta/Certificate/NamedRS.lean` (SHA `11275b8d9b0b5d9f198ae7286e51e8dc26695fc4`): the rigorous Riemann–Siegel analytic error majorant actually used by the unchanged upstream Hardy-`Z` sign/error tactic.

This exact method-specific source custody matters: a plausible mpmath root is not a proof that the **RS** approximation's certified analytic error at that height is small enough to resolve its proposed bracket.

## 2. New exact rational complete remaining-roster precision schedule

Fix the original CP001 frozen tests `h=1/2000`, `r∈{1/1000,1/500}`, centers `(-1099/1000,1099/1000,1/5)`, the unchanged CP006 `Φ,Φ'` derivative bounds and their normalized three-row operator error formula. The complete original external Turing-verified positive zero count is **1,748,002**, split into first **52** Euler–Maclaurin tests and the remaining **1,747,950** genuine Riemann–Siegel tests (source-count equalities; individual refined root certificates still OPEN).

**New sufficient uniform policy.** Suppose every one of the 1,747,950 RS positive-root intervals is independently certified and has half-width at most

```
 δ_RS <= 2/10^9 = 0.000000002.
```

Under the CP008 **candidate** first-52 width and the CP005 previously stated quadrature allowance `E_quad<=1/50000`, exact Fraction calculations yield

| Radius | Candidate first-52 localization | All 1,747,950 RS localization ≤ | Conservative high-zero tail | Quadrature allowance (OPEN) | Full conditional sum |
|---|---:|---:|---:|---:|---:|
| `1/1000` | `0.000004494344` | `0.000060429909` | `0.001893104119` | `0.000020000000` | **`0.001978028372 < 0.002`** |
| `1/500`  | `0.000005968354` | `0.000080249113` | `0.001795656952` | `0.000020000000` | **`0.001901874419 < 0.002`** |

Both strict margins are **independently exact-rational**. Even the full conservative *uniform* policy leaves positive headroom. This is a feasible mathematical **precision criterion**, not a claim that all roots can be certified at this width by the current RS evaluator. The actual maximally widened upstream RS source DOES NOT meet it.

**Height-adaptive relaxation.** Define, for dyadic band `2^j<=gamma<2^(j+1)`,

```
 A_i(j) = min(2, 16/(h_i² 2^(2j))),
 D_i(j) = h_i min(1,20/(h_i² 2^(2j))),
 L_r(j) = max_i sum_k (25/24)(h_i+h_k)
                [D_i(j)A_k(j)+A_i(j)D_k(j)+|c_i-c_k|A_i(j)A_k(j)] .
```

Every certified RS root has lower endpoint `≥149.5` and lies below the published actual Gram point `g<2^20`, hence belongs to one of the bands `j=7,...,19`. Set

```
 δ_allowed(j) =
   min(1/1000, (2/10^9)*min_{r in {1/1000,1/500}} [L_r(0)/L_r(j)]).
```

Every quantity above is a nonnegative **EXACT RATIONAL** (integer powers of two, frozen rational supports). By construction, for EVERY root and EACH radius,

```
 δ_k * L_r(j_k) <= (2/10^9) * L_r(0).
```

Summing at most 1,747,950 roots gives precisely the conservative RS budget above, **without estimating how many zeros live in each dyadic band or relying on cancellation**. Both radii are protected simultaneously.

Representative resulting half-width ceilings:

| Root's lower ordinate height band | Allowed half-width, approximately |
|---|---:|
| `[128,256)` through `[2048,4096)` | `2×10^-9` |
| `[4096,8192)` | `2.65×10^-9` |
| `[8192,16384)` | `1.36×10^-8` |
| `[16384,32768)` | `2.17×10^-7` |
| `[32768,65536)` | `3.47×10^-6` |
| `[65536,131072)` | `5.56×10^-5` |
| `[131072,262144)` | `8.90×10^-4` |
| `[262144,524288)` and above | `1×10^-3` hard cap |

The allowance increases with height because the *actual compact bump Fourier transform and its derivative decay*, not because the zeros at high heights are being assumed to lie on the critical line unconditionally. The externally accepted finite-height theorem and each per-root proof must still be present. It is a **support/bump dependent certificate policy**, not an intrinsic spectral invariant.

## 3. New ORIGINAL method-specific obstruction: Riemann–Siegel error bound is too coarse for naïve all-root narrowing

Exact source `Zeta/Certificate/NamedRS.lean` defines the full-correction analytic error

```
 E_RS(t) = (25/4)*t^(-5/4) + (1/32)*t^(-15/4).
```

Its linear-free fallback adds `(13/10)*t^(-3/4)`. The original source tactic requires the approximant's signed enclosure to overcome the corresponding analytic error at BOTH interval endpoints. Increasing the **ball-arithmetic working precision** cannot remove this **analytic truncation error**.

The following comparisons are **rigorous rational LOWER BOUNDS** on that analytic majorant, not guesses or direct evaluations:

- Since `150^(1/4)<4`, `E_RS(150)> (25/4)/(150*4)=1/96 ≈0.0104167`.
- Since `(10^6)^(1/4)<32`, `E_RS(10^6)>25/(4*10^6*32)=25/128000000≈1.953125×10^-7`.

These are much larger than the blanket **2×10^-9 half-width** sought for low RS bands, and even at height one million the analytical majorant remains roughly two orders of magnitude larger than that width. **This does not prove that every narrow RS bracket is impossible using the current source tactic** (it depends on actual Hardy-`Z) values, derivatives, correction errors and proof conditions). It does establish a **specific analytic accuracy obstacle**: merely requesting more decimal digits or increasing Lean's ball precision may not furnish the needed sign certificate. Replacing or sharpening the analytic approximant remainder, shifting to source-certified Euler–Maclaurin evaluation where tractable, or developing direct certified oscillatory-moment enclosures are genuine alternatives, with separate costs.

**Do not conflate** `E_RS` (upstream Hardy-Z approximation error) with `E_tail` (our compact-bump spectral zeros above the Gram cutoff). These are different errors controlled by different arguments.

## 4. Executable CP009 exact arithmetic and complete source-verification interface

New `scripts/cp009_riemann_siegel_precision_policy.py`:

- `--self-test` independently verifies CP008's exact candidate first52 band weights, both strict complete 1.75-million-root conservative totals, all 13 source-supported dyadic precision caps, rational error-floor lower bounds, and negative controls for too-wide low-height brackets.
- `--source-rs-dir ROOT --candidate-rs-dir ROOT --report JSON` (optional only when real data are available): read all SEVEN original RS text shards from CP007's **exact pinned Git blob SHA manifest**, enforce an independently SHA256-pinned seven-shard proposed refined store with exactly **1,747,950** rows, exact original RS row index preservation, strictly disjoint intervals, every candidate nested within its original 3-column source bracket, correct source interval order, no 52-row Euler/RS index conflation, and each source-aware candidate half-width under `δ_allowed(j)`. Output exact dyadic actual localization, complete conditional budget and literal SHA receipts.
- **Fail closed** on missing source shards, source SHA drift, incomplete or fabricated roster, invalid candidate width, overlap, root-index mismatch, or total error >`1/500`. It explicitly prints `STRUCTURAL_PRECISION_POLICY_PASS_NOT_LEAN`, NEVER `LEAN_PASS`, `CERTIFIED_COMPATIBILITY`, or `RH`. Hashes/manifest strings alone are not real accepted per-root Hardy-Z sign certificates.

The **small automatic CI** tests the exact rational complete-roster arithmetic and original first-52 numerical source nesting; no 53-MB fetch, no new original IV### Lean compile, no complete ROOT claims. A second **manual-only** source-shard metadata recheck may be run when authentic refined RS files exist. No invented RS rows are committed.

## 5. Exact mathematical interface still missing

A clear source-aware refined root index dictionary must satisfy: for each external original RS interval `I_k`, new `J_k⊆I_k` with the same original 1-based RS index `k`, **a kernel-accepted new zero-sign theorem for `J_k`**, no cross-interval overlap, and the original complete `N(g)=1748002` source theorem. Only then can the original one-zero-per-slot completeness argument identify the new refined roots as the original complete list; source-level strict inclusion alone is insufficient.

Next, independently enclose `Φ(hγ)` and all five real cosine moments, and compare the REAL original signed `Pole-Prime+Arch` 3×3 matrix with the complete spectral cosine matrix plus the certified tail. This still requires the original mixed Weil↔zero-side normalization theorem; a matching numerical 3×3 is only evidence, and a rigorously failing matrix envelope falsifies the **claimed dictionary** rather than RH.

**Next — CP010:** recover CP008 first52 actual v4.35 compiler result when available; pilot at least one true RS (build_batch_rs) narrow bracket with an analytically valid sign/error budget; choose among higher-order RS correction, the independently certified Euler route and direct integral refinement before scaling to 1,747,950 roots. Preserve original Phase IV and NF compiler queues and their custody; no global RH/Weil positivity.
