# RPB108 NF15 — Complete original signed native E80 positivity at aperture 53/50

Date: 2026-10-08. Independent branch research/rpb108-phase-geometry-localization. NF14 source head at start: 85d7cfc6c994562b733f68028a77754ccef52178; Coupled at start: c8cb8ec3e0cc2b8eae83afc328595ff84f2c1793 (CC43 work preserved). Earlier Global NF71 and Pre-Contact Shadow PS3 remain paused. This is a **finite retained native sign result**, not positivity on all 112 retained vectors, not corrected Schur sign, and not whole-domain a=53/50 positivity.

## New certified finite arithmetic result

Fix a=53/50. Let E80 be the span of the first 80 physical-orthonormal Legendre functions e_j(x)=sqrt((2j+1)/(2a)) P_j(x/a) on [-a,a]. The complete original unshifted Weil native quadratic form on this **finite** space (full archimedean term, every active von-Mangoldt prime power 2,3,4,5,7,8 in both shifts, and both Hermitian signed poles) satisfies

\[
\boxed{Q_{53/50}(h)>9\cdot10^{-34}\|h\|_{L^2}^2 \quad \forall h\in E_{80}\setminus\{0\}.}
\tag{NF15.1}
\]

All even/odd cross terms are exactly zero by original reflection symmetry. The 80x80 physical normalized native matrix contains 1640 distinct potentially nonzero same-parity entries: 820 even + 820 odd. For every entry the source stores independent outward enclosures for the archimedean, prime, signed-pole, and total native form. Thus there are 6560 original signed component interval checks.

No negative-source factor Gram, incomplete finite source dictionary, shifted positive physical level, or RH hypothesis substitutes for the original native terms.

## New exact reconstruction and precision

The full native E80 source was **actually generated locally** with:

- exact Fraction arithmetic and an exact precomputed Euler/kernel moment integrator;
- 490 exponential terms, 430 Bernoulli pairs, and 20 Euler gamma correction terms;
- 500-term rational atanh enclosures for the original prime logarithms;
- directed rational interval grid 10^-180, and 85-digit rational midpoint rounding;
- the original archimedean regular-kernel remainder bound and complete original prime and signed-pole error terms.

The maximum true native interval width was about 4.054308670225e-68. Taking the rational midpoint matrix M and paying all outward native entry errors and midpoint rounding gives an operator error bound

\[
\|Q_{E80}-M\|\le80\max_{ij}\max(|M_{ij}-\ell_{ij}|,|M_{ij}-u_{ij}|)
 <1.621724\times10^{-66}.
\tag{NF15.2}
\]

After shifting M by 10^-33 times the identity, **all 40 even and all 40 odd exact rational LDL pivots are strictly positive**. Therefore the true source form is bounded below by 10^-33 minus the full matrix error, which is strictly greater than 9x10^-34. No floating numerical eigenvalue is used for the finite sign decision.

Source data SHA256:

`9188d9b48525c1e1af41292e3bfe8d3004470e03b00520428d9d5b0cc76a8513`.

Compressed source archive SHA256 (deterministic gzip, mtime zero):

`f5ec122a209ad7b98a54286765ed55d726204e768f51b1cfbd781f0f4a8de09c`.

The full 80-mode source archive was generated in the local container and attached in the conversation. The repository contains [the reproducible target exact source generator](../scripts/certify_native_low80_nf15_106.py), [the independent exact rational parity/interval validator](../scripts/validate_native_low80_nf15_106.py) and [the compact custody manifest](data/RPB108_NF15_COMPLETE_NATIVE_LOW80_CERTIFICATE_106_20261008.json). The GitHub source emits canonical compact sorted JSON; it can be regenerated from the stated parameters. The repository itself is not claimed to contain the full raw ~multi-MB interval JSON, and no GitHub Actions/Lean replay is claimed.

## Independent source consistency against NF14 E64

The exact prior complete E64 source archive SHA256 was independently reverified as

`133d707391f5785b2237cee631246b4d08f30a222d88f8359b4a65035bdf4f07`.

Its original 32 even + 32 odd shifted rational LDL pivots were **actually replayed successfully** during NF15. The new E80 source and saved E64 source share the first 64 original Legendre modes. Every overlapping actual original signed interval in all four channels intersects:

\[
\boxed{4224/4224\text{ source component interval intersections pass.}}
\tag{NF15.3}
\]

This supports source truncation consistency and mathematical custody, not an independent derivation of the complete Weil explicit formula or a Lean certificate.

## Runtime and the next scalable architecture

The 80-mode source has a substantial exact-arithmetic setup cost. Its common moment integrator consumed most of the ~426-second local complete source run, rather than entry-by-entry assembly; the full 1640 entries were then successfully produced. This is a computational workload limit, not a sign obstruction. A faster next 96/112 producer should split the shared kernel-integrator precomputation from prime translations, cache exact kernel moment weights across batches, and checkpoint source rows without repeatedly rebuilding the common rational integral denominator. There is no reliable positivity extrapolation from E80 to E96 or E112.

The independent NF10 certified original physical F112 complement at this same aperture satisfies Q(h)>=17/100||h||² on F112. E80 and F112 are individually positive, but degrees 80..111 and the complete original mixed source/action coupling are unresolved. **The positive finite E80 result does not imply that the entire supported original Weil form at a=53/50 is positive.** Even a future native E112 positive trial matrix is insufficient without its corrected Schur reaction against F112.

## NF16 decision

Next:
1. A targeted **native E96/E112 generator** with shared exact moment-map caching and row checkpoints. Quantify high-degree interval errors before asserting any new finite sign. Stop on a failed certificate rather than labeling it a negative original vector.
2. In parallel rebuild target-specific **original positive-source/action Gram** for the complete E112, with every source-error payment and the original both signed poles. Test the corrected full even56/odd56 Schur using c=17/100, or derive and independently certify a sharper source-aligned complement bound if needed.
3. Keep CC43's independent global contact/pole-moment investigation separate; do not present this as a global RH-equivalent non-stalling result.

**Certified standing:** Whole-domain original positivity remains internally certified through a=21/20 (CC18). At a=53/50, original native E80 finite positivity and the original infinite F112 positive complement are separately established; the complete 112-native and original source Schur are still open. No RH/F4, full transport, new whole-aperture sign or Lean closure.
