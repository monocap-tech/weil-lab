# Terminology registry — GERM-74 additive research supplement

**Date:** 2026-09-28  
**Standing:** RESEARCH-LOCAL / UNRATIFIED  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

Read with [GERM-73](../notes/_recurrence73.md), its [GERM-72 correction](../notes/_recurrence72_correction.md), and [GERM-74](../notes/_recurrence74.md). Historical definitions and standing are unchanged.

## Residual lengths and internal-wrap width

Retain the residual lengths `alpha=beta+gamma`, `theta=2beta+gamma`, and `tau=7beta+4gamma`. Here beta and gamma are residual lengths, not the older prime coefficients.

Define
```math
\xi=5\gamma-\beta,\qquad
\omega=\gamma-19\xi.
```
GERM-74 certifies `19xi<gamma<20xi`, hence `0<omega<xi`.

Write `epsilon=beta+delta`, equivalently `e=3h-alpha+delta`. The new internal-wrap width is delta, with `0<delta<=gamma` in the exclusion theorem.

## Corrected third- and fourth-section species

The third-section inside-to-inside wrap is `I3=(E2+)^3 E2-`, with chronological second-section word `11-,11+,11+,11+`. Q3, P3, and D3 retain their corrected GERM-73 meanings. Their domains are re-audited in GERM-74; they are not continued solely from matching endpoint bits.

On the fourth beta-circle, use
```math
\mathcal E=P_3Q_3,\qquad
\mathcal J_0=D_3P_3Q_3,\qquad
\mathcal J_1=P_3I_3Q_3.
```
These are the two-step elliptic word, the old three-step word, and the new internal-wrap three-step word respectively. All are complete exterior-to-exterior returns with determinant one in the stated scope.

## Fifth-map source bit

The fifth section is `0<z<gamma`, physically `(h-beta,h-beta+gamma)`. Its rotation is `z -> z-xi mod gamma`. Define
```math
F_{i,n}=\mathcal E^{n-1}\mathcal J_i,\qquad
 i\in\{0,1\},\quad n\in\{4,5\}.
```
The source bit is `i=1` exactly for `z<delta`; `n=4` for `z<xi`, and `n=5` for `z>xi`. These are domains, not free choices of generators.

## Sixth section and typed domain contracts

The sixth section is `0<y<xi` in the fifth coordinate, physically `(h-beta,h-beta+xi)`. Its first return is `y -> y+omega mod xi`, taking 19 or 20 fifth steps.

A typed domain contract is the exact interval/overlap/wrap requirement under which a retained map is proved. GERM-74 checks the original-step lift of each third map, then checks the proved contract at every intermediate fourth-, fifth-, and sixth-step composition. This is a compositional source-domain certificate, not endpoint-only typing or an unrestricted renormalization theorem.

The sixth-return chart is `C6=[[1,1],[0,3]]`. Its factor 8000 applies per complete sixth return, not per original rotation step.
