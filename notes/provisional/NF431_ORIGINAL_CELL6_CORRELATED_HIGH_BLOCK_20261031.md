# Weil-Lab NF431 — Original correlated true cell-6 Chebyshev high modes 256..511

**2026-10-31 PT.** Canonical W-ODD-NEG OPEN and RH OPEN. Stacked on NF430 draft PR #439, retaining NF407 original 242 selected+4 critical source, NF406 original true irrational log7/log8 support cell, NF404 original dyadic center, NF423 third-derivative coverage, NF424 same original exponential transfer with all 2048 common endpoint image indices, NF425/NF430 original Bernstein ellipse and NF429 signed integration machinery. No source substitution or merge.

## Previous cursor / current circle / next

**NF430 accepted:** Exact source envelope `sup_E2|z_2048|<1e330`, strict original true J6 uniform 1265-term (degree1264 Chebyshev *series*) residual <2e-45; only 256 original a0..a255 source-native interval balls available, with 1009 unknown a256..a1264. NF429 all raw dx Chebyshev moments and NF428 all signed principal p moments are already available for any final contraction.

**NF431 current:** Compute **actual** original source-correlated high modes `a_256,..,a_511` (256 NEW modes), with complete unchanged 246-generator physical source, all 32 critical sine components, original sinh pole and analytic removal of its m0 digamma/image singularity, all true prime shifts n2/3/4/5/7 and n8/n9 neither, actual x=9/10 physical I0/I1 independent NF416 pointwise overlap, and both 2048 left/right original endpoint-image families; 2048-bit native Arb/Acb outward enclosures with original image/source uniform charge <4e-45 per coefficient, every interval width <1e-25. We evaluate only coefficient indices [start,stop) instead of re-evaluating all lower modes: expanded source Chebyshev vectors are padded through stop+13, but expensive source/image coefficient accumulation visits only the required new indices. This is a computation of the **original fixed cell6 analytic branch** restricted to J6; no physical seam is crossed.

Reuses the successful source-native NF428 coefficient algorithm verbatim in its mathematical formulas. Major implementation change: all coefficient paths use absolute index n from start to stop-1 and store it as `res[n-start]`. Interior digamma/derivative, five prime shifted source polynomials, pole source and centering, signed endpoint logarithm, 2048 native shared endpoint image indices all use the same absolute index. A standalone check asserts exact contiguous indices 256..511, strict certified widths, all source pins, prime/pole/endpoint invariants, and separate true physical NF416 pointwise overlap.

**Acceptance if focused CI SUCCESS:** first original 256 low-mode intervals from NF428 and 256 NEW original high-mode intervals NF431 give 512/1265 independently source-certified coefficients, leaving **753** still uncomputed (n512..n1264). No full original P1264 or signed true J6 `int pz`, `int z²`, hence no NF410/NF404 accepted scalar. A partial P511 contraction could be performed using preexisting NF428 signed moments and NF429 raw dx moments, but it is not the original complete integral without remaining certified coefficients/tail.

**If CI FAILS:** leave all new coefficients provisional, retain original accepted n0..255 only; diagnose native high-index Bessel/Arb width or runtime before any numerical promotion.

## Provenance and audit

- Native script: `scripts/local_replay/nf431_original_cell6_correlated_cheb_high_block_native.py`
- Focused workflow: `.github/workflows/nf431-original-cell6-native-high-256to511.yml`
- Original source: `notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json`
- Original true physical seams: `notes/data/provisional/NF406_original_prime_support_partition_exact.json`
- Independent physical-x check: `notes/data/provisional/NF416_original_cell6_full_I0_and_z_point_native.json`
- Prior NF430 original series cutoff and NF424 source+image charge are inherited, not recalibrated from a surrogate.

**Standing before native CI:** implementation submitted, n256..511 pending. **Still OPEN:** complete true physical cell6 signed pz/z²; remaining original seven cells; NF410/NF404 whole signed scalar; original fourth J242 exterior upper, W-ODD-NEG, even/whole Weil, infinite operator domain/inverse and RH. No main merge.
