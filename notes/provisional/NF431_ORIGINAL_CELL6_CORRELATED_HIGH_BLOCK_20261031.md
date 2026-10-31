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


## Post-CI original-source verification: NF431 PASS

**The original 256 NEW high modes a256..a511 are ACCEPTED** from focused [Actions #41251524378 SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/41251524378), exact script commit f4086e94f9bcb8d9d79c5072697436b270bfdd4c. The native job ran 2048-bit Arb/Acb over all original 246 generators, correct actual five signed post-seam primes/two neither, the exact NF404 dyadic center, 2048 shared physical endpoint image indices and removable odd pole. Every high-mode source/image-charged coefficient interval n256..511 is narrower than 1e-25, and the independent genuine NF416 original physical full z(0.9) I0/I1 interval overlap PASS. Original 256 low-mode balls n0..255 from NF428 remain unchanged. **512 of 1265 Chebyshev series coefficients now native source-certified, remaining 753 n512..n1264 OPEN.**

Source-native high256 JSON artifact #13060884765, ZIP SHA256 cf2c109c9b253a4d50c8bb2f35c10704ef2ada77de6f4b0c514c8115c529588e; inner original source interval JSON SHA256 10c93ca7f4b7779334fd686ef1fd348f79fe873068af3897c2a936487dbdcbf8.

Independent bounded original-source 32-coefficient pass n256..287 [Actions #41251733247 SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/41251733247), artifact #13061143926 ZIP SHA256 5d5986d02928afd34cc6aada380e302b6acc9373add6c04b969f6d7e5968c940, inner original JSON SHA256 c543a4c898ef1f167fe2b65d60b4f27f11bd35c130cd3bc14388740b1ab14f37. All 32 original native intervals independently **OVERLAP** corresponding indices in original high256 source JSON, with different high-vector truncation/padding lengths. This verifies high-mode absolute-index routing, without creating a new analytic tail bound.

## Original signed P511 partial polynomial: exact Fraction PASS (full z OPEN)

Original 256 low + 256 NEW high coefficient intervals, signed original NF428 1500 principal p moments and NF429 native 2999 raw dx moments were combined from four JSON SHA256-checked historical GitHub Actions artifacts. Focused [Actions #41251809577 SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/41251809577), original exact Fraction interval code `scripts/local_replay/nf431_original_cell6_P511_partial_contraction_exact.py`. Strict authentic J6=(log7-B,log8-B), B=11/10. The certified degree511 **partial** polynomial P511=sum_(n0..511)a_n T_n((x-.91)/.07) has the following rigorous outward intervals (displayed decimal MIDPOINTS only, full rational endpoints in artifact):

- `int_J6 p P511` approx **-2.8272867005838606282038858979779609463145e-22**, interval width approx 1.04071e-55.
- `int_J6 P511²` approx **3.5348473457388135980100367591935527607383e-22**, interval width approx 1.30276e-47.
- `4 int_J6 p P511 + 2 int_J6 P511²` approx **-4.2394521108578153167954700735247382637815e-22**, certified strictly negative upper, width approx 2.60552e-47.

Compared with the certified NF429 P255 partial signed approx -4.239452033456402e-22, the new 256-mode increment shifts the PARTIAL result by about **-7.74e-30**. This is an observed/computed finite-polynomial increment, **NOT** a bound on coefficients n512..n1264 or the true original full J6 scalar. A source-certified uniform tail bound for P511 has NOT been established.

Final original signed partial JSON artifact #13061626148 (ZIP SHA256 9d6eb44c150946cfefa25f307089eceaadc646c448f03d06b8e7ac3323a0edbd, inner original JSON SHA256 e04a0bc019128509afd0d6e0a37b8da9b6c397ac5260854d03f7862c3bb70418). Independent local exact Fraction source replay of same four SHA-pinned artifacts produced identical midpoint and strict interval width classification. All original output artifact JSON have GitHub retention until 2027-01-29. Their raw generated endpoints still require permanent repository archival. Permanent machine-readable source hashes/artifact digests/scoped receipts: `notes/data/provisional/NF431_original_cell6_native_high256_and_P511_custody_index.json`.

**NF431 accepted:** 256 new original-source-correlated a256..511 intervals (512/1265 cumulative), independent 32-mode overlapping replay, exact original signed partial P511 quadratic contraction. **Not accepted:** 753 remaining high coefficients; complete true J6 signed pz/z²; original seven other cells; global NF410/NF404 cap; original fourth J242 exterior upper; W-ODD-NEG, even/whole Weil, infinite operator domain/inverse; RH. **Next NF432:** exploit source-specific high-mode decay to rigorously bound remaining n512..1264 or compute source-correlated bounded blocks while retaining exact source and signed moment gates. No main merge.
