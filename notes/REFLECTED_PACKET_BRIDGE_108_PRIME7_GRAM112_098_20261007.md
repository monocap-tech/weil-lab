# RPB108: whole-domain positivity at aperture 49/50

2026-10-07 UTC. Continuation of the aperture lane from the published repaired 112-vector native/source construction `3b8cd0e3b958cecdc62dd16322e266bfdab07ad9`. Concurrent global/F4 work and historical certificates are preserved.

The full eleven-panel matched 112-source residual Gram and the actual source-error corrected Schur test pass at aperture 49/50. Whole-domain actual positivity is certified through **0.98**, with the conservative published bounds

\[
 Q(h)\ge 10^{-30}\,\|h\|_{\mathrm{mass}}^2,
 \qquad Q(h)\ge 8\times10^{-33}E_{\log}(h).
\]

## Complete Gram and independent audits

The physical retained and projected-away degrees are 0 through 111. Both fresh complete Gram constructions start with separate absent checkpoints and retain all eleven prime-7 geometry panels. The integration degree is **826**, determined from the complete repaired source polynomials of maximum degree 413; no high-degree Bernoulli or smooth-source tail is dropped. All endpoint-log, smooth, mixed and projection terms remain present.

The complete outputs and checkpoints repeat byte for byte. Checkpoints contain all three 112-by-112 contractions CS, smooth and cross: **37632 saved interval entries**. The largest residual entry width is about **9.279911e-80** on the 300-digit outward grid. Endpoint-log construction uses 160 Machin terms; independent reconstruction uses 320 terms and a finer 400-digit grid.

Independent exact rational endpoint projections validate all **12544 native/source pairings**, including both enclosure widths and the actual per-column source allowance. All 12544 displaced pairing controls are rejected. Independent closed binomial Legendre coefficients and endpoint-log squared Hankel moments reconstruct all **12544 residual entries** from saved contractions. Every finer enclosure lies inside its saved Gram enclosure; all displaced residual controls are rejected.

## Actual correction and corrected sign

The previously published complete source allowance remains eta = 1.643684784137795e-35 < 1.65e-35. The full Gram trace gives surrogate residual map norm M about **6.736334312143365**, and the actual operator correction

\[
 \delta=\eta(2M+\eta)\approx2.214482041947078\times10^{-34}.
\]

The independently proved **112-vector** complement is c = 247/250, strictly below its unrounded bound about 0.9886124780930549. No previous 96-vector Gram or conditional sign is transferred. The actual corrected matrix

\[
 Q_{112}-(250/247)(R_{112}+\delta I)-10^{-28}I
\]

passes all **112 outward pivots at 160 digits**, and the complete sign certificate repeats byte for byte. A separate audit widens the inputs to 80 digits and rechecks all 112 corrected pivots. Negative diagonal and oversized conversion controls are rejected.

An integer lift bound L = 7 gives

\[
 \mu=\frac{10^{-28}c}{10^{-28}+c(1+7^2)},
 \qquad \kappa=\frac{\mu}{10(\mu+24)}.
\]

The exact conversion determinant is mu squared, strictly positive. Mu is just below 2e-30 and kappa is about 8.333333333333334e-33, supporting the rounded published bounds above. The fresh Gårding-24 audit uses prime loss below 6, pole loss below 12 and the published multiplier bound m0 >= w/10 - 6 at aperture 49/50.

## Custody and reproduction

`notes/data/RPB108_PRIME7_GRAM112_098_CUSTODY_20261007.json` pins every new file, immutable archive part, unchanged local arithmetic dependency, the 112-vector preflight and prior native/source custody. Complete Gram and panel checkpoints are deterministic gzip archives transported as base64 parts; both compressed and decoded SHA256 hashes and Git blob hashes are checked before publication. The original complete Gram extraction retains its pre-sign flags; the separate Schur and whole-domain audit records supply the final positive sign.

Restore the published archives with `python scripts/restore_native_prime7_gram112_098_archives.py`; restore the previous native/source archives with their published restoration script. The complete Gram, pairing and residual auditors accept restored archive paths, and the corrected sign constructor reads the pinned native/source/Gram inputs. The whole-domain auditor accepts a freshly repeated Schur output path.

Global endpoint exclusion, F4, full transport and Lean formalization remain open. The next aperture target requires its own geometry, native/source/complement and complete coupling checks; no new target is certified here.
