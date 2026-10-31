# Weil-Lab NF430 — Sharpened original cell-6 ellipse bound and smaller series cutoff

**2026-10-31 PT.** Canonical W-ODD-NEG OPEN, RH OPEN. Stacked after accepted NF429 draft PR #438, without replacing historical NF425/427/428/429 scripts, source artifacts or modes.

## Previous / current / next

**Previous NF429:** the original true cell6 quadratic integral has a source-certified 2999 raw Chebyshev moment router and exact signed P255 partial polynomial contraction, but **not** the true original pz/z² value. NF428 certifies modes a0..a255; NF427's global original fixed-cell6 series cutoff was degree1499 (1500 modes), leaving 1244 missing.

**Current NF430:** sharpen the SAME rigorous NF425 Bernstein ellipse E2 bound using `pi < 22/7` instead of `pi < 4`. No new source, no new model, no sampling, no change to NF406 true cell J6=(log7−11/10, log8−11/10). This gives an explicitly smaller original finite 2048-image fixed-branch complex envelope `M<10^330` and **degree1264** Chebyshev series approximation, making only 1265 source-coefficient balls necessary to achieve the inherited <2e-45 original cell6 function residual. Savings: **235** coefficients, and **1009** still to be numerically certified. Numerical CI and receipt standing are recorded separately below.

## Exact improvement to the original E2 growth envelope

NF425's same original 242 selected plus four critical 4096-bit dyadic generators (including all 32 critical sine modes and odd pole) have exact source raw triangle less than `10^160`, generator polynomial order <=13, frequency f<883, coefficient uncertainty <10^-700. Their full genuine five post-seam signed prime branches n=2,3,4,5,7 and n8/n9 neither, endpoint log and dyadic centering remain exactly as before. Source-exact preflight replays the same NF407/NF406/NF423 ancestry and the same NF425 normal image-series and removable-pole interface.

In Chebyshev x=C+Ht, C=91/100, H=7/100, on E2 retain Re x≤399/400 and |Im x|≤21/400; hence Re(B−x)≥41/400>1/10. Each original frequency lambda0=±2*pi*i*f is surrounded by radius1/8 in lambda. This makes Re(1/4±lambda/2)≥3/16, preserves NF425's psi<64000, its image geometric factor <6, Cauchy derivative `13! 8^13<10^24`, shifted monomial factor `3^13<10^7`, and analytic cancellation of the true lambda=±1/2 m0 pole.

The improvement is entirely in the complex oscillatory exponential. Using the classical rigorous `pi<22/7`, and conservatively covering the five original prime shifts with |Re(x−log n)|<3B, its exponent obeys the exact rational inequality

```
(2*(22/7)*883 + 1/8)*(21/400) + 3B/8 < 293,
B=11/10.
```

Thus every source-frequency Cauchy disk complex exponential is <e^293<3^293, instead of NF425's <3^373. The unchanged coarse constants from original digamma, images, source `10^160`, degree-13 derivatives and prime translations are already overcharged by `10^190` in NF425. Exact integer arithmetic now checks

```
10^190 * 3^293 < 10^330.
```

This supplies the stronger original finite-model E2 bound `sup_E2 |z_2048|<10^330` for the **same fixed cell6 branch**, never for the physical operator across prime seams.

## Acceptance reduction and inherited source budget

Standard Chebyshev **series**, not interpolant, coefficient bound on E2:

```
|a_n| <= 2*10^330*2^(-n), n>=1,
sup |sum_(n>=1265) a_n T_n| <= 4*10^330 / 2^1265 < 10^-50.
```

The strict threshold is tight under this particular envelope: `4*10^330/2^1264 >= 10^-50` (a choice of the envelope, NOT an impossibility of further improved bounds). Inherited genuine original NF424 2048-image/source-ball uniform error on true J6 remains <10^-45, so the true original response admits a degree1264 series partial sum with **uniform residual <2*10^-45**. Previously all 1500 a0..a1499 were required under NF427's conservative envelope; now only **a0..a1264**. Already certified: a0..a255. Uncomputed: a256..a1264 = **1009**.

Already accepted NF428 signed p Chebyshev moments n0..1499 cover all necessary 1265 signed moments, and accepted NF429 raw dx Chebyshev moments n0..2998 cover all required n0..2528 square moments. The exact NF429 product-to-sum integration router therefore needs only a smaller coefficient vector once supplied; do not falsely invoke its current 1500-coefficient all-input guard or label a 256-coefficient partial as true z. Remaining 1009 coefficients require original 246-source correlated Arb balls and interval widths sufficiently tight for the final signed acceptance budget.

## Scope

The sharper source-envelope proof and exact rational computation are mathematical inequalities; native finite-source response coefficients n256..1264 are **not** computed here. Existing 256-mode signed partial polynomial contribution ~−4.23945e−22 remains a statement about P255 only; high modes can change it. The true cell6 integrals pz/z², other seven cells, NF410/NF404 complete scalar, fourth J242 exterior upper, original infinite domain/inverse, W-ODD-NEG, even/whole Weil and RH remain OPEN. No merge main, source swap, or change to original signed branch.

Verification script: `scripts/local_replay/nf430_original_cell6_sharper_ellipse_series_cutoff_exact.py`. Focused workflow: `.github/workflows/nf430-original-cell6-sharp-ellipse.yml`. Source hash and CI receipt must be retained before numerical promotion.

**Next:** source-correlated native coefficient blocks a256..a1264 or a stronger original-source high-mode tail that rigorously replaces some missing coefficients; then certify true cell6 pz/z² against original NF428/NF429 moment vectors. Permanent archive of already generated JSON remains due before Actions expiry.
