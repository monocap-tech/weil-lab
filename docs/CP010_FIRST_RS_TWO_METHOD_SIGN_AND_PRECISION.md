# Weil-Lab — CP010
## Original first-Riemann–Siegel-zero dual-method proof pilot and one-exception full-spectral precision budget

**Independent CP### track**, stacked on CP009 PR #819 → CP008 #817 → CP007 #815 → CP006 #810 → CP005 #807 → CP004 #803 → CP003 #799 → CP002 #796 → CP001 #790. Do not modify the canonical original Phase IV IV### support-extension Lean proof program, Phase III NF### original numerical certification, or independent PI### arithmetic/trace interface.

**Classification:** original source-attached **Lean 4.35 proof candidates** and a new independently exact-rational spectral budgeting argument. The committed candidates have NOT been accepted by a new kernel/axiom audit. Python `mpmath` is **numeric screening only**, not a rigorous zero enclosure, not an original source theorem and not a proof of compatibility. Even two successful source-bound first-root proofs would not establish the full 1,748,002 zero list, spectral quadratures or original Weil arithmetic/zeros dictionary. No global Weil positivity/RH claim.

## 1. Compiler custody at kickoff

Actual GitHub Actions workflow statuses inspected:
- CP007 true upstream 52-source-row exact-rational preflight: `44856725172` **queued**.
- CP008 original source-nested first-52 high-precision candidate numerical preflight: `44857421560` **queued**.
- CP009 exact complete-RS policy arithmetic CI: `44858061714` **queued**.

The heavyweight CP008 separate v4.35 Lean source-kernel job is **manual-only**; no live compiled new `.olean` receipt was available. It is incorrect to call the CP008 first 52 refined zeros certified.

CP010 adds its own cheap PR-triggered numerical/rational CI and a separate MANUAL-only v4.35 kernel workflow, without adding another expensive automatic job to the original IV###/NF### backlog.

## 2. Actual upstream original source method and exact index dictionary

All sources are pinned to `smmercuri/zeta@c06b4e13d9c847e50a32c3d738271cbad62ae9f3`, Lean v4.35.0, **not** original Weil-Lab v4.34.0.

Original upstream has **52** Euler–Maclaurin certified source rows (first local Euler index 1 through 52) and **1,747,950** Riemann–Siegel source rows. Thus local RS row `1` is GLOBAL positive-zero ordinal index **53**, NOT 1. Its original upstream first RS batch is
```lean
theorem batch : BatchSpec 200 149500 1000 474603 1000 := by
  build_batch_rs 0 200
```
in `Zeta/Zeros/Certificates/RiemannSiegel/Batch0001.lean` (source Git blob `12848f56d0b62df858dcb89b708a858f4f7b28fb`). Its original input store `python/out/riemann_siegel/zeros/zeros_00001.txt` has source blob `1029bed8a315d1b39d7c45e55a6476acbbf8baf1`; the full ~7.3MB file is NOT copied into Weil-Lab. CP010's **manual** source-integrity workflow must actually fetch the raw source and verify the entire original Git blob before it can assert that a narrow/coarse candidate is contained in original RS row `1`.

Direct upstream sources:
- `Zeta/Zeros/BuildCertsRS.lean` (blob `2dbddd3716bfabbcd92390b6f25c554045179349`) genuinely reads local `python/out/riemann_siegel/zeros`, parses exactly `idx,left,right`, and invokes `build_batch_rs` with the original `Zeta.Certificate.NamedRS` certified Hardy-`Z` sign and analytic error machinery.
- `Zeta/Zeros/BuildCerts.lean` (blob `cab277b57726caa4aa8687e78a8efd084ba0cf8b`) similarly reads local `python/out/euler_maclaurin/zeros`, retaining four per-endpoint cutoff/Bernoulli parameters, and invokes original `build_batch`.
- The exact original Euler row `52` is `52, 146.530, 149.500, 92, 93, 20, 20`. For the first *new* Euler proof at ~150, CP010 **copies the genuine last upstream Euler per-endpoint parameters** `92,93,20,20`, without asserting their analytical adequacy after t=149.5. The genuine original Euler `build_batch` must determine whether these parameters are sufficient.

The original first RS row's **actual right endpoint is not inferred** from the original first batch's endpoint 474.603; a batch only exposes the first of 200 left endpoints and the 200th right endpoint. The mandatory CP010 source-containment audit downloads its original entire SHA-pinned shard and inspects the first row. No numeric approximation is allowed to replace this actual source check.

## 3. Two distinct original Lean source proof candidates for the same numerically identified zero

Using independent 60–75-digit `mpmath.zetazero(53)` only for numerical *proposal*, the first RS positive-zero ordinate is approximately
```
 gamma_53 ≈ 150.05352042078488035143246723695937...
```
and high-precision, **nonrigorous** `mpmath.siegelz` gives:

| Approximation method | Proposed EXACT rational bracket | Numeric Z(left) | Numeric Z(right) |
|---|---|---:|---:|
| Riemann–Siegel | `[15000/100,15010/100]` = [150.00,150.10] | about −0.0910109233 | about +0.0719002367 |
| Euler–Maclaurin | `[15005352/100000,15005353/100000]` | about −0.000000681740868 | about +0.0000155197598 |

Both numerical signs are compatible with a root, but **neither is a rigorous sign certificate**, and original RS source containment must be separately checked.

The isolated separate `cp010_zeta_v435/CP010DualMethods.lean` invokes the unchanged upstream certified tactics:

```lean
theorem coarseRiemannSiegelCandidate :
    BatchSpec 1 15000 100 15010 100 := by
  build_batch_rs 0 1

theorem narrowEulerMaclaurinCandidate :
    BatchSpec 1 15005352 100000 15005353 100000 := by
  build_batch 0 1
```

Their two method-specific **candidate** stores/manifests are independently checked for exact decimals, original source parameter carryover and numerical nesting. Even if both compile, identifying the contained root with the *original global 53rd* certified zero requires importing or independently proving the exact index/uniqueness/bijection argument from the original `CertifiedZeroCount` and batch chain. Two overlapping certified intervals from different methods do **not** alone prove they contain the identical zero without a suitable uniqueness statement.

## 4. Original RS analytic approximation: true error bound versus numeric sign margin

The actual upstream `Zeta/Certificate/NamedRS.lean` (source Git blob `11275b8d9b0b5d9f198ae7286e51e8dc26695fc4`) has original full-correction analytic remainder bound

```
 E_RS(t)=25/(4*t^(5/4))+1/(32*t^(15/4)).
```

Rigorous **exact-rational** inequalities at the proposed RS coarse interval's left endpoint `t=150` are:

```
 E_RS(150) > (25/4)/(150*4) = 1/96,
 E_RS(150) < (25/4)/(150*3)+(1/32)/(150^3*27),
```

because `3 < 150^(1/4) < 4`. The upper bound remains true for all t≥150. This controls the analytic remainder, NOT the still-needed ball-arithmetic enclosure of the approximant itself. The observed nonrigorous coarse `|Z|` values are much larger than this analytic error bound, making it a plausible **true Lean RS sign proof candidate**.

For the narrow interval, numerical `|Z(150.05352)|≈6.8174×10^-7` and `|Z(150.05353)|≈1.5520×10^-5`, both far smaller than the full-correction RS analytic remainder bound `≈0.0119`. This makes a brute-force high-precision *RS* sign proof ineffective with its existing rigorous analytic truncation bound. Increasing `Enclosure` working precision alone cannot shrink a source remainder of that size. **It does not prove an impossibility theorem** about other algorithms or even every possible sign proof; the Euler–Maclaurin source method has a distinct analytic remainder.

This sharpens CP009's obstruction into a **single named test** rather than a hypothetical need for all 1.75m zeros.

## 5. New full-roster error-budget result: one exception need not obey the uniform per-root cap

CP009 established a strictly sufficient blanket RS interval half-width `δ0=2×10^-9` for all 1,747,950 RS roots, conditional on the CP008 first52 intervals and independently bounded `E_quad≤1/50000`. Its source-registered conservative original 3×3 cosine-moment error coefficient for band `2^7<=gamma<2^8` (where gamma_53 lies) is exactly:

```
 L_(1/1000)(7) = 11063/640000   ≈0.0172859375,
 L_(1/500)(7)  = 22037/960000   ≈0.02295520833.
```

Suppose all RS roots except #53 have certified `δ_k≤δ0` and first 52 original CP008 candidates are genuinely certified. For a single exception at #53, the same full 1,748,002-root normalized error estimate becomes:

```
 Total_r(δ_53)=
   E_tail(r)+E_quad_allowance+E_loc(first52,r)
   +N_RS*δ0*L_r(0)
   +(δ_53-δ0)*L_r(7).
```

This is an exact rational upper bound conditioned on the previously stated original full Weil dictionary and all independent proof gates. It gives:

| #53 candidate | Narrow-radius conditional full total | Wider-radius conditional full total |
|---|---:|---:|
| **Narrow Euler** `δ53=1/200000=0.000005` | **0.001978115 < 0.002** | **0.001901990 < 0.002** |
| **Coarse RS** `δ53=1/20=0.05` | **0.002842326 > 0.002** | **0.003049635 > 0.002** |

Thus a successfully kernel-certified narrow Euler bracket **can be an allowed exception** to the uniform 2e-9 per-root rule while preserving the complete conservative 0.002 comparison tolerance; the coarse RS bracket **cannot**, under the current estimator and unverified quadrature allowance.

The maximum possible single-exception half-width, under the optimistic assumption that all *other* RS roots meet δ0, is:

```
 radius 1/1000: δ_53 < ~0.001271072,
 radius 1/500:  δ_53 < ~0.004274657.
```

To satisfy **both** radii simultaneously, require the smaller threshold. This clarifies that a **1e−5-wide rigorous bracket** is already mathematically useful for the *global budget*, even though it is wider than the CP009 blanket requirement. These thresholds and totals are source/bump-dependent **certificate sufficiency criteria**, not intrinsic invariants of the original Weil form or RH.

**Important logic:** `Total_r(δ53)>0.002` for the coarse proposed interval means the **current upper-bound certificate does not close**, not that the actual spectral approximation error exceeds the threshold or that CP-C1 is false.

## 6. Implemented fail-closed verification and next CP011

Committed:
- `scripts/cp010_dual_method_root53_pilot.py`: genuine source-indexed exact rational method store/parameter check, original first52 SHA verification, one-exception full-roster error budget, original RS source full Git blob/row-1 containment **when the source file is actually downloaded**, and separately labeled numerical Hardy-`Z` screening.
- `cp010_zeta_v435/{lean-toolchain,lakefile.toml,CP010DualMethods.lean,python/out/{euler_maclaurin,riemann_siegel}/zeros/{manifest.json,zeros_00001.txt}}`: *two distinct authentic upstream method-tactic proof candidates*, not one new fabricated generic zero oracle.
- `scripts/cp010_dual_method_lean_axiom_audit.py`: refuses to claim any v4.35 Lean kernel PASS without actual compiled `.olean`, genuine double `#print axioms` logs restricted to standard axioms, pinned source/first original RS source Git blob, candidate store/manifests and SHA receipts.
- `.github/workflows/cp010-root53-dual-method-numerical.yml`: cheap PR-triggered mathematical and numerical-only screening, explicitly NONKERNEL.
- `.github/workflows/cp010-root53-original-v435-manual-kernel.yml`: intentionally **workflow_dispatch only** for authentic heavy external library v4.35 compiler; downloads the exact SHA-locked original 7.3MB RS source shard, verifies genuine source containment, runs actual `lake build CP010DualMethods` and strict source/olean/axiom audits. No Phase IV CI preemption.

Next CP011:
1. Recover actual original first RS source containment, CP008 52 new refined Euler and CP010 dual-tactic compiler outcomes before promoting new statements to Lean PASS.
2. If Euler at 150.05352 with original `92/93, M20` fails, inspect the specific analytic error/cutoff and alter only the isolated candidate with a separate new receipt; preserve original 52-source custody.
3. If narrow Euler succeeds, formalize the link to the first original RS source interval and Turing-count uniqueness, and use a one-exception budget to prioritize similarly difficult low-height RS rows.
4. Only after 1.748m complete source-certified root roster and genuine source-bound original pole/prime/archimedean mixed Weil 3×3 dictionary/quadratures can CP004's actual spectral falsifier run. No equivalence presumed.

Primary upstream sources: https://github.com/smmercuri/zeta/tree/v1-1e6/Zeta/Zeros ; https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Certificate/NamedRS.lean ; https://github.com/smmercuri/zeta/blob/v1-1e6/Zeta/Zeros/Certificates/RiemannSiegel/Batch0001.lean .
