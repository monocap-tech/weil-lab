# Weil-Lab — CP008
## Exact source-nested Euler first-52 refinement candidates and a genuine isolated Lean sign-certification gate

**Independent CP### stage:** CP008 stacked on CP007 PR #815 → CP006 #810 → CP005 #807 → CP004 #803 → CP003 #799 → CP002 #796 → CP001 #790. **Do not edit** the independent original Phase IV IV### support-extension chain, Phase III NF### numerical-custody chain or PI### trace interface. CP008 does not import external Zeta `.olean` into original Weil-Lab Lean v4.34.0.

**Custody status:** CP008 supplies **52 source-linked, five-decimal numerical candidate brackets** and a genuine direct original external `Zeta.Zeros.BuildCerts` Lean 4.35 **PROOF CANDIDATE**. Strict exact-rational source nesting/error estimates are independently checked; 75-digit mpmath Hardy Z endpoint signs are *nonrigorous screening only*. Until direct `lake build`, real `.olean`, pinned external full SHA and standard-only `#print axioms` receipt pass, NONE of the 52 new brackets is promoted to kernel-certified. The **old broad source intervals** remain the only previously reported upstream source proof objects. No RH/global signed Weil positivity or complete 3×3 arithmetic/spectral comparison is claimed.

## 1. Frozen provenance and real generator mechanics

Original external `smmercuri/zeta` **immutable source commit** `c06b4e13d9c847e50a32c3d738271cbad62ae9f3` / release tag `v1-1e6`.

1. Original `python/out/euler_maclaurin/zeros/zeros_00001.txt` is exact Git blob `6958515f7dd1be86ebe823ff6fd67ec110ec90f7`, 52 original seven-column records, first `1, 1.000, 17.846, 63, 67, 20, 20`, last `52, 146.530, 149.500, 92, 93, 20, 20`. It is identically preserved in CP007's `data/cp007_original_euler_maclaurin_first52.txt`.
2. Genuine upstream Lean `Zeta/Zeros/Certificates/EulerMaclaurin/Batch0001.lean` includes `theorem batch : BatchSpec 52 1000 1000 149500 1000 := by build_batch 0 52`. Direct source inspection of `Zeta/Zeros/BuildCerts.lean` reveals that `build_batch lo hi` reads **the actual project-local** `python/out/euler_maclaurin/zeros/manifest.json` and associated store rows, calls `Zeta.Certificate.Named` for rigorous Hardy-Z/analytic error checks and constructs a genuine `CertifiedZeroIntervals` bundle. The numeric endpoint denominators in Lean are exactly powers of 10 from the original row decimals, not float approximations. Thus a locally separate v4.35 source store can be the actual input of a genuine Lean sign proof. This is not a hypothetical arithmetic oracle.
3. Our own `cp008_zeta_v435/` is that **separate Lake project**, pinned to upstream `v1-1e6` Lean v4.35.0; it does not modify the upstream original store, original `Zeta.Main`, original `certifiedZeroCount`, nor any IV### v4.34 source or toolchain.
4. The two files `cp008_zeta_v435/python/out/euler_maclaurin/zeros/{manifest.json,zeros_00001.txt}` contain the 52 *proposed* source rows. Their original indices and four Euler cutoff/Bernoulli fields are copied exactly from the original upstream row. ONLY the pair of real endpoints is narrowed.

## 2. First 52 actual high-precision numerical refinement candidates

Numerically screen each positive zero `zeta(1/2+i gamma_n)=0` for indices `n=1..52` using `mpmath.zetazero(n)` at 75 decimal digits. Place `gamma_n` between consecutive exact five-decimal rationals `floor(100000*gamma_n)/100000` and `(floor(100000*gamma_n)+1)/100000`. Independently test Hardy `siegelz(left)*siegelz(right)<0`, **in high-precision floating computation only**. A 75-digit numerical screen returned opposite signs for 52/52 candidate intervals, with minimum absolute endpoint `|Z|` approximately `1.0038796·10^-7`. This is **not** a mathematically proved sign enclosure and must not be mistaken for the `Enclosure` kernel certificate.

The **exact-rational** result needs no `mpmath`: every one of the 52 new bracket candidates is STRICTLY contained in its independently SHA-checked ORIGINAL upstream widened interval with the SAME index and unchanged four original method-specific fields. All 52 new intervals are strictly ordered, disjoint and width exactly `1/100000`. In particular:

```
 Original I1 = [1, 17846/1000]           (halfwidth 8.423)
 New C1 = [1413472/100000,1413473/100000] (halfwidth 1/200000)
 Original I52 = [146530/1000,149500/1000]
 New C52 = [14742276/100000,14742277/100000]
```

These two endpoint replacements are candidate intervals, not a proof that the actual root lies inside them. The genuine independent kernel route is stated below.

## 3. A real external Zeta Lean theorem CANDIDATE for all 52, no invented library

`cp008_zeta_v435/CP008First52.lean` imports the **unchanged** upstream `Zeta.Zeros.BuildCerts` and proposes:

```lean
namespace CP008First52
open Zeta.Certificates

theorem refinedCandidateBatch :
    BatchSpec 52 1413472 100000 14742277 100000 := by
  build_batch 0 52
end CP008First52

#print axioms CP008First52.refinedCandidateBatch
```

The original upstream tactic must establish rigorous source-specific 52 endpoint sign/error certificates, the ordered interval bundle and the exact first/last endpoints from the candidate store. If any one of the 52 five-decimal signs is too close for the original Euler approximation/cutoff, this **must FAIL**, and the next repair is a margin-aware, wider or higher-precision interval / source-bound original analytic cutoff—not treating mpmath signs as rigorous. All 52 old row indices/cutoff/ Bernoulli parameters remain intact. A successful compilation proves the new `BatchSpec` but still does **not** by itself replace the full 1,748,002-root original `certifiedZeroCount` or prove the original Weil mixed transform identity.

The heavyweight `.github/workflows/cp008-refined-first52-v435-manual-kernel.yml` is **manual-only**, to avoid additional automated backpressure on canonical IV### and NF###. It verifies external source commit `c06b4e13d9c847e50a32c3d738271cbad62ae9f3`, builds `CP008First52` under original Zeta v4.35, and runs `scripts/cp008_refined_first52_lean_audit.py` to require actual source/data and compiled olean SHA custody and ONLY standard axioms `propext, Classical.choice, Quot.sound`. The separate cheap pull-request CI checks exact rational source nesting and 52 nonrigorous numeric screens; **that cheap test can NEVER be counted as a Lean pass**.

## 4. Exact mathematical improvement on the CURRENT CP006 conservative error bound

All 52 candidate bracket halfwidths are exactly `1/200000`. Their strictly rational dyadic-band halfwidth sums are:

| Dyadic lower ordinate band | Number of rows | Sum of candidate halfwidths |
|---|---:|---:|
| [8,16) | 1 | 1/200000 |
| [16,32) | 3 | 3/200000 |
| [32,64) | 10 | 1/20000 |
| [64,128) | 28 | 7/50000 |
| [128,256) | 10 | 1/20000 |
| **Total** | **52** | **13/50000** |

Plugging these **candidate** widths (not actual certified root intervals) into CP006's unchanged **exact Fraction** nonnegative dyadic operator localization bound yields

```
 radius r=1/1000:
   E_loc^candidate(first52) = 143819/32000000000
                            = 0.00000449434375.

 radius r=1/500:
   E_loc^candidate(first52) = 286481/48000000000
                            = 0.000005968354166666....
```

Compare the old, SHA-verified genuinely upstream broad-interval CP007 bound of `1.283480859375` (narrow) and `1.70442421875` (wide). This is a **strict improvement in a conditional worst-case error bound when the new brackets are certified**. It does not say the true spectral values are closer by that amount or that the external Lean actually accepted the proposed signs.

With the CP005 conservatively bounded high-zero tail at `T_0=10^6` and a **still unverified** normalized quadrature allocation `E_quad<=1/50000`, the amount left for the other **1,747,950** positive zero brackets is

```
  r=1/1000:
     E_remaining = 1/500 - E_tail - 1/50000 - E_loc^candidate(first52)
                 = 126177353528816167/1531250000000000000000
                 ≈ 0.00008240153699841055.

  r=1/500:
     E_remaining = 1638817498429771003/9187500000000000000000
                 ≈ 0.00017837469370664174.
```

This is a **conditional error budget allocation**, not a claim that the remaining RS zero store meets it. In particular, ALL seven published original Riemann–Siegel zero shards still have their original broad source brackets, and their full source-data computation/refinement has not been kernel certified here.

## 5. Missing precise interface and falsifiers

The CP008 candidate could fail in four genuinely informative ways:

1. A new endpoint fails original Lean `Zeta.Certificate.Named` sign/error proof at the original `63..93` cutoff/Bernoulli parameters. This **invalidates the proposed refined interval certificate**, not the upstream broad original zero proof.
2. The local `build_batch` source directory is incorrectly resolved, the `BatchSpec` first/last rationals mismatch, the original external SHA changes or the v4.35 release toolchain doesn't import. This is a **source/custody failure**.
3. The genuine kernel theorem accepts 52 refined intervals but the original count-to-batch correspondence cannot be transported to the unchanged 1,747,950 Riemann–Siegel root intervals with actual separation/multiplicity proofs. This blocks claiming a COMPLETE refined million-height roster.
4. Even if the 52 refined intervals are certified, the remaining RS intervals exceed the available normalization error allowance, the independent `Phi` quadrature is not rigorously enclosed, or the complete Weil pole/prime/Gamma versus zeros mixed dictionary remains unattached. These are still independent CP-C1 tests.

**Next — CP009:** recover the actual heavy CP008 v4.35 Lean first-52 batch compiler/audit receipt without claiming a pass in advance. If it fails, refine the precise original source cutoff/precision or widen candidate brackets while preserving the <=1/500 spectral budget. Then formulate a source-linked RS batch refinement and REAL full height-band budget. Do not merge or disturb IV### or NF### certification. No global Weil positivity or RH.
