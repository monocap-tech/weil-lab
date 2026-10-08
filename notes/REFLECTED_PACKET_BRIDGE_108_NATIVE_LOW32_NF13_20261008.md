# RPB108 NF13 — Complete original native low24 and low32 positivity at a=53/50

Date: 2026-10-08. Independent branch research/rpb108-phase-geometry-localization, advancing NF12 native E16 positivity. Live Coupled branch read-only: latest observed `f800c8d1d1e6f98dff83278b03a0f24db719f202` (boundary-contact pole-moment work). Global NF71 and Shadow PS3 paused. All CC18 a=21/20 source custody is unchanged.

**A: evaluated complete ORIGINAL signed Weil native finite-matrix result.** At a=53/50, the complete native quadratic form is strictly positive on E24 and E32, the spans of the first 24 and 32 normalized physical Legendre modes. This is NOT positivity on all E112 or the complete infinite supported domain; the full original source/action Gram and corrected even56/odd56 Schur tests remain to be constructed.

## 1. New strict finite-mode certificates

Each new interval matrix retains exactly the original unshifted Weil archimedean multiplier, all six active prime powers {2,3,4,5,7,8} in BOTH physical translation directions (including 4 and 8 with von Mangoldt weight log2), and both Hermitian signed pole terms. Physical parity splits E24 into two 12-dimensional blocks and E32 into two 16-dimensional blocks, with all even–odd crosses exactly zero.

The validated complete finite-space lower bounds are:

\[
\boxed{
Q_{53/50}(h)\ge9\times10^{-19}\|h\|_{L^2(-a,a)}^2
\quad(h\in E_{24}),}
\tag{NF13.1}
\]
\[
\boxed{
Q_{53/50}(h)\ge10^{-22}\|h\|_{L^2(-a,a)}^2
\quad(h\in E_{32}).}
\tag{NF13.2}
\]

The displayed margins are conservative rational consequences of independently paid whole-matrix interval errors and exact-rational shifted LDL pivots. No floating-point eigenvalue was used to certify these signs.

| Exact component | E24 | E32 |
| --- | ---: | ---: |
| Distinct full same-parity signed entries | 156 | 272 |
| Exponential / Bernoulli truncation orders | 190 / 160 | 190 / 160 |
| Largest signed native interval width | 3.070202e-31 | 3.518990e-25 |
| Full symmetric error bound (entries + rational center) | 3.684258e-30 | 5.630384e-24 |
| Rational diagonal shift removed before LDL | 1e-18 | 2e-22 |
| Verified exact positive pivots | 12 even + 12 odd | 16 even + 16 odd |
| Actual strict finite-mode lower (rounded) | >9e-19 | >1e-22 |

For every same-parity interval [l_ij,u_ij], the certificate chooses a rational midpoint approximation m_ij on grid 10^-36, paying `epsilon = max_{ij}max(|m_ij-l_ij|,|m_ij-u_ij|)`. Because the full error matrix has at most N entries per row, its operator norm is <=N epsilon. For each of the two parity blocks, exact rational Gaussian/LDL elimination proves `M_N-shift*I>0`; thus `Q_N>=(shift-N epsilon)I`. The corrected lower bound is 9.999999999963158e-19 for N=24 and 1.9436961643204275e-22 for N=32 (decimal displays of rigorous exact fractions). The conservative lower bounds (NF13.1)–(NF13.2) follow strictly.

## 2. NF12 truncation orders were too weak; increasing them resolved the error

The first reconstruction reused NF12's exponent order 130 and 100 Bernoulli pairs. Those runs reconstructed the signed 24x24/32x32 native matrices rapidly, but produced worst interval widths ~3.8143e-13 (E24) and ~4.37185e-7 (E32). The numerical midpoint eigenvalues were positive (smallest about 3.09e-18 at E24 and 5.15e-22 at E32), BUT the errors exceeded those gaps. No rigorous sign could be inferred from those initial reconstructions.

Increasing the exact native kernel Taylor controls to exponent order 190 and Bernoulli pairs 160, with the same rational directed integrator and original native formula, reduced the worst widths by approximately eighteen orders of magnitude in both cases. The original normalized Legendre/correlation arithmetic and all signed pole and prime terms were retained. The new matrix source uses the inherited CC18-type exponential and regular-kernel bounds with target-safe exponential factor 70, regular-kernel factor 53/10, and an exact Euler–Maclaurin gamma enclosure; none relies on RH.

The producer is [`certify_native_low32_nf13_106.py`](../scripts/certify_native_low32_nf13_106.py), a faithful target-specific expansion of the NF12 signed source, with selectable audited orders and dimension 24/32. The separate [`validate_native_low32_nf13_106.py`](../scripts/validate_native_low32_nf13_106.py) performs rigorous original-component interval checks and independently recomputes exact rational parity-block LDL after a conservative shift.

## 3. Alternative truncation-order recomputation

As a nontrivial reproducibility test, E32 was reconstructed *again* with exponent order 210 and Bernoulli pairs 180. All 272 signed matrix entries carry four component enclosures (arch, prime, poles, full). Intersecting the earlier 190/160 and new 210/180 intervals gives

\[
\boxed{1088/1088\text{ nonempty exact rational intersections; zero conflicts.}}
\]

The alternative order reduces the E32 maximum source interval width further to ~3.273503e-31. This tests truncation consistency, not independence of the underlying original Weil identities or implementations. The exact order-210 source SHA256 and both primary source SHA256 values are recorded in [NF13 custody manifest](data/RPB108_NF13_COMPLETE_NATIVE_LOW32_106_CERTIFICATE_20261008.json). The full 24/32 interval archives were generated locally and are reproducible using the published producer with the stated command-line order parameters. The compact manifest does not embed all ~400KB of full interval records; its archived digests must be checked against regenerated files.

Historical a=21/20 positivity, the NF10 a=53/50 positive physical F112 complement c=17/100, and NF12 a=53/50 E16 finite positivity are preserved. NF13 strengthens only the FINITE native retained positive subspace from 16 to 32.

## 4. The actual remaining whole-aperture problem

The first 112 native degrees are NOT proved positive as a whole. Even if a future complete E112 native restriction is positive, its mixed coupling with the NF10 positive F112 complement can make the entire form indefinite unless the true corrected Schur lower closes. The original complete source/action columns, residual Grams, and true inverse/on-source geometry must be paid. The CC18 a=21/20 source Gram and physical complement c=699/1000 cannot be relabeled or reused at 53/50.

**NF14 objective:** Move to 48 or 64 fully signed native retained modes using precision chosen relative to the smallest high-precision midpoint eigenvalue, independent error payment, and exact rational parity pivots. Rebuild complete source/action columns in checkpointed batches rather than assuming positive native finite trials imply positivity of the full form. A failed conservative shifted LDL at larger dimension is *inconclusive* unless an actual enclosed negative vector is furnished.

**Standing:** On a=53/50, E32 finite trial and F112 infinite physical complement are positive separately. E112 and its corrected mixed Schur remain unresolved; there is no certified whole-domain a=53/50 sign. Highest internally certified whole-domain original aperture remains a=21/20. No RH/F4, non-stalling, full transport, or Lean closure.

## 5. Exact custody

This investigation locally executed exact Fraction native integration for E24 and E32 at 190/160, and for E32 at 210/180; exact rational LDL and the 1088 exact component intersection assertions passed. The existing GitHub producer/validator implement these choices, but no claim is made that a GitHub Actions runner independently executed this new commit. The finite signed original Weil calculation is not a new global RH result.
