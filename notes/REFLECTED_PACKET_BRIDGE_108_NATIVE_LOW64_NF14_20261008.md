# RPB108 NF14 — Original native E48/E64 strict finite positivity at aperture 53/50

Date 2026-10-08. Independent branch research/rpb108-phase-geometry-localization, following certified NF13 E24/E32 original native finite source intervals. Read-only latest recovered Coupled mathematical checkpoint CC41, head `4eb3278fc07caaf118166bb86b7093be3f28c095`. Paused Global NF71 and Pre-Contact Shadow PS3 unchanged. All historical a=21/20 CC18 certificates and a=53/50 NF10 F112 physical complement remain separately preserved.

**A — two new complete original native FINITE positivity results.** For the ORIGINAL unshifted Weil signed form on the physical-orthonormal Legendre subspaces E48 and E64 of L2([-a,a]), a=53/50,

\[
\boxed{Q_a(h)\ge9\times10^{-27}\|h\|_{L^2}^2\quad(h\in E_{48}),}
\tag{NF14.1}
\]
\[
\boxed{Q_a(h)\ge9\times10^{-31}\|h\|_{L^2}^2\quad(h\in E_{64}).}
\tag{NF14.2}
\]

These are COMPLETE original native SIGNED matrix calculations in their stated finite trial domains: the full archimedean endpoint/digamma contribution, ALL six active prime powers 2,3,4,5,7,8 with both shifts, and both original Hermitian signed pole terms. The even/odd mixed block vanishes EXACTLY by physical reflection. The source matrices split as 24+24 and 32+32 parity modes respectively.

**These do NOT certify** the entire retained E112 matrix, any corrected source/action Gram, the mixed/inverse coupling to NF10's infinite F112 complement, or entire original Weil positivity on aperture 53/50. The highest internally certified whole-domain original aperture remains CC18 a=21/20.

## 1. NF14 reconstruction: the actual precision bottleneck changed

The first full native E48 source using NF13-like exponent order 280/Bernoulli pairs 240 and the previous atanh logarithm precision (125 terms) reconstructed all 600 distinct same-parity signed entries, but its worst interval width was ~6.517730589275e-24, whereas the high-precision even minimum midpoint eigenvalue was ~2.431033691279e-26. Enlarging ONLY exponent/Bernoulli orders to 330/290 did not materially improve that entry width. An audit of its four separately enclosed native channels identified the **PRIME polynomial-evaluation interval** as the sole dominant source of uncertainty.

For NF14's passed E48 source, increase rational atanh log precision from 125 to 300 terms and directed-grid digits from 58 to 95. Keep the ORIGINAL native function itself unchanged and exponent/Bernoulli orders 280/240. Exact polynomial/correlation arithmetic now bounds:
- 600 independent symmetric nonzero same-parity entries;
- max full native entry width ~3.792184689718e-37 (now the ARCHIMEDEAN truncation dominates);
- complete symmetric matrix error <=9.101243255324e-36 after independently paid rational midpoint rounding at 10^-50;
- exact 24 even + 24 odd rational LDL pivots all strictly positive on midpoint matrix minus 10^-26 I.

Subtracting the whole interval error yields a real physical lower >9e-27, (NF14.1), with no numerical eigenvalue used to DECIDE sign.

The high-precision midpoint even eigenvalue (~2.4310e-26) is included only as an exploratory conditioning diagnostic; its sign is separately proved by exact shifted rational LDL.

## 2. NF14 E64 full native reconstruction

For E64 raise exponent order to 390, Bernoulli pairs to 340, log atanh terms to 380 and directed rational-grid digits to 140. The full native source contains:
- 1056 same-parity full signed interval entries (32x33/2 each parity);
- 4224 archimedean, signed pole, original prime, and total-form interval checks;
- worst original full native interval width ~4.044453455397e-55;
- complete symmetric rational midpoint error <=1.294225105727e-53, with midpoint rounding denominator 10^70;
- all 32 even and 32 odd exact-rational shifted LDL pivots pass after subtracting 10^-30 I.

The conservative physical lower >9e-31 in (NF14.2) follows by paying the COMPLETE error. The high-precision numerical midpoint eigenvalue diagnostics, not used as sign proofs, were:
- smallest even eigenvalue ~3.852653539158e-30;
- smallest odd eigenvalue ~1.158088490372e-28.

This is an entire full native E64 finite form certificate, not an assertion that all of the first112 positive after mixed source correction.

## 3. Consistency and independence scope

Original NF13 signed interval archives on E32, with a separately chosen exponent/Bernoulli pair 210/180, were compared to the E64 signed sources for the entire common 32-mode principal restriction. All **1088/1088** exact component intervals intersect. Similarly NF14's independently computed E48 source at 280/240 intersects the E64 restriction in **2400/2400** exact signed component checks. Zero conflicting intervals; combined **3488/3488**.

E48 also has a more coarsely bounded alternate computation using 330/290 exponent/Bernoulli orders with the original 125-term log bounds. Its full 600x4 signed components intersect the refined E48 source in **2400/2400** exact rational comparisons. These checks establish internal consistency across truncation choices, nested native sizes and original component accounting. They do NOT form an independent derivation of the entire Weil explicit formula or a Lean proof.

New reproducible GitHub sources:
- [NF14 exact E48 native producer](../scripts/certify_native_low48_nf14_106.py)
- [NF14 exact E64 native producer](../scripts/certify_native_low64_nf14_106.py)
- [NF14 exact E48 full signed validator](../scripts/validate_native_low48_nf14_106.py)
- [NF14 exact E64 full signed validator](../scripts/validate_native_low64_nf14_106.py)
- [NF14 certificate and source SHA256 custody](data/RPB108_NF14_COMPLETE_NATIVE_LOW64_106_CERTIFICATE_20261008.json).

The full raw original source interval JSON archives were generated in the local calculation runtime. They are not silently substituted with previous archived CC18 or NF13 matrices. Their exact SHA256 and numerical tolerances appear in the compact manifest. The GitHub source scripts are new reproducibility artifacts; no GitHub Actions CI replay is claimed.

## 4. Main research decision: next aperture gate is E112 plus complete original source Schur

NF10 already proved original physical F112 complement positivity at a=53/50 with c>=17/100. NF14 now certifies E64 original native positivity. A positive E64 and a positive F112 do NOT cover the middle physical Legendre degrees64..111 or the indefinite mixed coupling. Even proving native E112 finite positivity would not close the whole domain without source-corrected Schur against F112.

**NF15 options, with meaningful stopping rules:**
1. Finish native E80 or E96 and assess exponentially shrinking numerical margins under adaptive log/kernel truncation. Avoid any assumption of lower bound monotonicity across nested finite spaces; first-principles exact interval LDL is required.
2. In parallel, restore complete target-specific positive-source/action columns and source Gram, paying every target-specific original source error and both Hermitian poles, rather than leaving the mixed Schur until after E112.
3. Audit whether the current conservative complement lower c=17/100 makes the corrected Schur gate plausible. If it cannot, improve source-aligned inverse estimates or the target-specific complement before expensive full source builds. Failure of a sufficient bound is NOT an actual original negative vector.

The earlier IP7 generic Fourier-tail cutoff bottleneck is no longer used; the operator-adapted Legendre native engine, exact kernel moments and compensated interval enclosures are now explicitly reproduced.

## 5. Verified standing

NF14 strengthens FINITE original signed Weil positivity on the new a=53/50 target through E64 (and E48). The ORIGINAL whole supported domain remains internally certified through a=21/20 only (CC18), even0/odd0. No RH/F4, all-cap non-stalling, full transport, corrected full source Schur or Lean closure is asserted. Coupled remains the sole integration frontier; independent Phase Geometry owns these computational aperture preflights.
