# RPB108 NF12 — Rebuilt complete original native low16 at aperture 53/50

Date: 2026-10-08. Independent branch research/rpb108-phase-geometry-localization. Parent NF11 low8 prime-only result at branch head 87d74d2ff71c418516b4bf5e49c2fe77ec802738. Concurrent Coupled mathematical head CC39, read-only. The original whole-domain positivity anchor remains a=21/20; the NF10 genuine physical F112 complement at a=53/50 is >=17/100. This note is an **A-class finite native restriction certificate**, not a 112-retained sign, source-corrected Schur or whole-aperture positivity statement.

## Evaluated result: complete native signed low16 form is positive

For a=53/50, let E16 be the 16-dimensional span of normalized physical Legendre modes e_j(x)=sqrt((2j+1)/(2a))P_j(x/a) on [-a,a], j=0,...,15. The ORIGINAL complete native signed Weil form, with the full archimedean term, every active prime power {2,3,4,5,7,8} in both directions, and the Hermitian cross-paired signed poles, has been reconstructed as a 16x16 symmetric rational-interval matrix Q16.

Exact reflection gives eight even and eight odd modes, with ALL even/odd mixed entries zero. There are 72 distinct potentially nonzero same-parity symmetric entries (36 even+36 odd). Using exact-rational finite Gaussian/LDL elimination with all source-entry errors paid by an explicit operator-norm error, the result is

\[
 \boxed{Q_{53/50}(h)\ \ge\frac1{2\times10^{12}}\|h\|_{L^2}^2
 \quad\text{for every }h\in E_{16}.}
\tag{NF12.1}
\]

This is physically normalized finite native positivity. It is not positivity on the remaining 96 retained directions, the infinite complement, or their mixed block, and it makes no assertion about the full corrected Schur reaction.

## Exact native construction and independent comparison

The standalone [complete native low-mode producer](../scripts/certify_native_low4_nf12_106.py) retains the original native CC18 archimedean kernel/Euler–Maclaurin calculation with a target-specific order 130 exponential approximation, 100 Bernoulli pairs, 20 Euler gamma pairs, rational pole exponential moments, and full six-prime translated physical overlap polynomials. All four arithmetic channels are represented by exact rational intervals: archimedean, signed pole, prime, and complete sum. Directed grid 10^-58 is used internally; the constant bounding the target exponential truncation is 70, and the original regular-kernel error factor is conservatively bounded by 53/10. These bounds are applied to each original Legendre correlation polynomial with the original normalization and full signed poles. The source is a target-specific independent implementation, not relabeled CC18 matrix data.

At degree 0..3 the original complete Q has an exact-parity block structure. Representative full native entries:

| Native entry | Approximate value |
| --- | ---: |
| Q00 | +0.040152084275421 |
| Q02 | +0.086359478442110 |
| Q11 | +0.144011672856334 |
| Q13 | +0.226405494527280 |
| Q22 | +0.188900149093581 |
| Q33 | +0.362626980661478 |

The resulting two 2x2 determinants have strict exact rational lower values about 1.26775189e-4 (even) and 9.63070156e-4 (odd). The finite four-mode lower bound exceeds 5e-4. All 26 local rational low4 checks passed, including reconstruction/payment of complete arch/prime/pole pieces.

Independent Fourier-frequency sanity check uses the actual archimedean multiplier Re psi(1/4+i*pi*xi)-log pi, the Fourier transforms of normalized Legendre modes via spherical Bessel functions, and a frequency integral truncated at 2000. Differences from the exact native arch values are <=0.0015 on the six low4 parity entries; the differences have an omitted high-frequency tail, so the numerical integral is NOT used as the rigorous enclosure.

The prime piece of the exact full-form computation matches NF11's separately derived prime-only degree0/degree1/cross entries. Those crosscheck formulas were not simply copied into the new source evaluator.

## Exact 16-mode positive sign certificate and error payment

The separate [16-mode independent certificate](../scripts/certify_native_low16_nf12_106.py) reuses the proved low-mode source constructor at DEG=15, integrating all 72 complete same-parity native entries at a=53/50. The maximum individual original native interval width is

\[
 < 3.553\times10^{-19}.
\]

Round every interval midpoint to a rational grid of denominator 10^32. Its maximum distance to ANY true enclosed native matrix entry is strictly less than 1.777e-19; the complete symmetric 16x16 matrix error in operator norm is at most 16 times this bound, namely strictly less than 2.843e-18.

Now subtract the EXACT rational shift 6/10^13=6e-13 from the diagonal of the midpoint matrix and perform 16 steps of exact fraction LDL without any floating pivot decision. All 16 pivots are strictly positive. Therefore the midpoint matrix is >=6e-13 I, and the original actual Q16 is bounded below by

\[
6\times10^{-13}-2.843\times10^{-18}
>5\times10^{-13},
\]

which proves (NF12.1). This is a rigorous finite matrix sign, not a model or a derived RH condition.

The [machine-readable custody manifest](data/RPB108_NF12_FULL_NATIVE_LOW16_CERTIFICATE_106_20261008.json) records the exact maximum error and all 16 shifted pivot test status; the source script reproduces the complete exact interval records and their SHA hash. The separately saved [low4 component interval manifest](data/RPB108_NF12_FULL_NATIVE_LOW4_106_CERTIFICATE_20261008.json) records each arch/pole/prime/native entry as outward rational intervals on a 10^-25 grid; the [low4 independent validator](../scripts/validate_native_low4_nf12_106.py) replays all four native channels and validates their conservative determinants.

A 12-mode brute prime-only path in NF11 previously exceeded the local time window. The exact integrated-kernel method solves that *computational* bottleneck for low16 (the local complete integration and exact LDL took about a second). No complete 112 source has been run. High-degree source integrals can require higher truncation orders, sharper interval arithmetic and checkpointed source normalizations to prevent enclosure degradation.

## What remains open and new NF13 stopping rules

1. Rebuild original signed native entries through all 112 physical retained modes at a=53/50, retaining every cross term. The current 16-mode matrix is a strict *trial* submatrix; its positive determinant does NOT imply sign of a larger principal submatrix.
2. Rebuild complete target-specific original physical source and action Gram for both parity blocks. Even a certified positive native 112x112 matrix does NOT automatically imply whole-domain positivity: the NF10 infinite-complement lower c=17/100 has an adverse inverse-reaction allowance.
3. Compute and independently validate the corrected whole even56 and odd56 Schur signs. If the conservative Schur fails, classify it as a failed sufficient certificate; do NOT infer an actual negative Weil test.
4. To claim a new whole aperture, provide complete source-error payments, source Gram custody, a sound infinite complement, all 112 retained modes, and actual even/odd strict signs. Do not transfer CC18's 21/20 c=699/1000 or old interval pivots.

**NF13:** Increase complete native matrix batches via the exact moment integrator (e.g., 24 and 32 modes), assess actual interval widths and pivot stability, and prepare hash-bound 112 source checkpoints. After numerical feasibility is established, commit to the full 112 rather than repeating old-only phase or compactness investigations.

Standing: genuine F112 complement positivity at 1.06 (NF10) and complete native E16 positivity (NF12), separately; their union is NOT automatically a positive direct sum due to remaining modes and mixed coupling. Highest certified whole-domain positive aperture remains 1.05 (CC18). Coupled active CC39 and paused Global NF71 / Shadow PS3 unaffected. No RH/F4/non-stalling/full transport/Lean closure.
