# RPB108 NF23 — Complete original physical low-two source-square Gram

Date: 2026-10-09 UTC. Branch: `research/rpb108-phase-geometry-localization`.
Recovered parent: `1261995ecc9ce80351ab3cfbaf802929444fe92e` (NF22).
Coupled and paused branches are read-only dependencies and receive no writes.

**NF23 closes all missing arch–prime and arch–pole physical source cross terms on e0/e1 at a=53/50.** The complete original physical source includes the endpoint-log archimedean action, all six prime powers in both orientations and both signed Hermitian poles. Its low-two source-square Gram is diagonal by exact reflection, with strict bounds

\[
0.083661834381 < \|L_a e_0\|_2^2 < 0.083661834383,
\qquad
0.338141181532 < \|L_a e_1\|_2^2 < 0.338141181534.
\]

This is an original physical source-square certificate, not a native Q diagonal, a high inverse-response estimate, a compensated near-critical vector certificate or a whole-domain sign.

## Missing covariance now certified

All entries below are strict outward rational decimal enclosures. The word "twice" is part of the definition of each displayed cross term.

| Physical source quantity | Even e0 | Odd e1 |
| --- | --- | --- |
| Twice arch–prime | (10.024385266799, 10.024385266800) | (-2.767819391026, -2.767819391025) |
| Twice arch–pole | (-24.267433489082, -24.267433489081) | (0.741993999404, 0.741993999405) |
| Complete source square | (0.083661834381, 0.083661834383) | (0.338141181532, 0.338141181534) |
| Complete even–odd source pairing | 0 exactly | 0 exactly |

The complete squares add these covariances to NF22's rigorous arch squares and a fresh replay of NF21's exact combined prime-plus-pole source-square sectors. The large signed cancellation is retained before drawing any conclusion. The covariance enclosures have widths below 10^-15 before outward decimal display; the final square enclosures inherit the 10^-12 arch-square display intervals.

## Exact integration and complete error ledger

Write c=-gamma-log(2pi), L(x)=log(a²-x²), and use NF22's rational polynomials P and V. The arch approximants are

\[
A_{0,N}(x)=\frac{P(x)+c-L(x)/2}{\sqrt{2a}},
\qquad
A_{1,N}(x)=\sqrt{\frac{3}{2a^3}}
\left[V(x)+xP(x)+cx-\frac{xL(x)}2\right].
\]

All 12 oriented source-support boundaries are enclosed and strictly ordered with the two outer endpoints, producing the original 13 translation cells. On each cell the prime source is a constant or affine polynomial. The code checks separation and active support membership, and retains a per-cell rational covariance ledger.

Polynomial products are integrated by their exact antiderivatives. For partial logarithmic moments, substitute t=a+s*x with s=±1. The primitive of x^n log(a+s*x) is obtained by the finite binomial expansion of s^(n+1)(t-a)^n and

\[
\int t^k\log t\,dt
=\frac{t^{k+1}}{k+1}\left(\log t-\frac1{k+1}\right).
\]

At t=0 this primitive uses its exact continuous limit zero. There is no discarded endpoint strip. Logarithms and Euler gamma are enclosed by the existing rational atanh/Euler–Maclaurin constructions. Pi is enclosed through Machin's formula. Every interval operation rounds outward on NF21's 10^-44 rational grid.

For arch–pole covariance, cosh(x/2) and sinh(x/2) are approximated through degree 40. The common uniform error bound is

\[
R_{40}=\frac{2(a/2)^{41}}{41!},
\]

since exp(a/2)<2. Full-interval polynomial/log moments use NF22's exact odd-harmonic identities. The pole Taylor errors are paid by 128 R40 (even twice covariance) and 1024 R40 (odd), using ||A_j,N||<4 and conservative rational bounds on the pole coefficients and support length.

Finally let epsilon=4(106/125)^320/(1-106/125). NF22's physical arch-source errors are delta0=4a*epsilon and delta1=14a*epsilon. Fresh NF21 intervals explicitly verify ||prime e_j||<3 and ||pole e_j||<5. The exact twice-covariance error payments are therefore at most 6 delta_j and 10 delta_j, respectively. All analytic and Taylor errors are included in the published rational intervals.

## Reproduction and independent checks

- [Exact rational NF23 producer](../scripts/certify_native_complete_source_low2_nf23_106.py).
- [Machine-readable interval certificate, input hashes and 13-cell ledger](data/RPB108_NF23_COMPLETE_SOURCE_LOW2_CERTIFICATE_20261009.json).
- [Independent stable-endpoint numerical check](../scripts/diagnose_native_complete_source_stable_nf23_106.py), explicitly non-certifying.

The producer and both NF22 exact producers ran locally and passed. NF21 is replayed inside the NF23 producer. No Lean or GitHub Actions execution is claimed.

The independent numerical check integrates the complete squared source directly rather than adding sector squares. Endpoint cells use a fourth-power change of variables, and J(t) uses log1p/expm1 to avoid rounding e^(-t/2) to one. It gives 0.08366183438191532 even and 0.33814118153293554 odd, inside both displayed certificates. These numbers and reported quadrature errors remain diagnostics. NF22's older odd double-precision checkpoint (~0.3381411815357) differs by about 3e-12, well within its reported quadrature error; it is not an exact conflicting value.

## Next frontier: compensated near-critical source

The low-two construction gate is closed. The next computation should apply this same exact source/covariance machinery to an explicit rational NF18 near-critical retained vector, retain the measured H2 compensation, and integrate its compensated residual source before squaring. A directional P2/S2 bound is a useful probe, but cannot establish the full matrix inequality. For the whole gate, extend to all 58 genuine source columns per parity or directly construct the 56 compensated residual columns, with errors below their actual retained margins. CC59's sharper correlated response criterion remains a separate read-only interface; this certificate supplies genuine source data, not its final sign.

**Standing:** Full 58-column source Gram, compensated residual P2, whole-domain positivity at a=1.06, global F4, RH, transport and Lean closure remain open. The highest internally certified whole-domain aperture remains a=1.05. No branch beyond Phase Geometry is modified.
