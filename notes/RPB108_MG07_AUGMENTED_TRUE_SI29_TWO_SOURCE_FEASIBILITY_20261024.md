# NF — Returned SM40 tests and first augmented original two-source numerical probe

Date: October 24, 2026. **W-ODD-NEG OPEN; PR #317 DRAFT.** No claimed RH or whole-odd certificate.

## Completed GitHub Actions

- Original exact SM40 sharpened-complement run 40071136137: SUCCESS, all 107 original clusters/3892 signed subcells/890 exact moment pivots, original b9 470 exceptional sources unchanged; the fully paid exact threshold is
  \[
  \theta_{\mathrm{SM40}}=1-\varepsilon_{\rm eff}/(1/1000)
  =0.9699135819561749\ldots .
  \]
  This supersedes the earlier coarse lower bound around 0.93356, conditional on original operator realization.
- MG07 original 470 reference/residual theorem run 40071136586: SUCCESS on exact algebra and toy models; full original 470 source matrices still NOT evaluated.
- SM40 original cap-ray discovery run 40071136256: SUCCESS as NUMERICAL ONLY.
- Critical path run 40071136207: FAILED on invalid research manifest check role. Thirty-four historical checks used descriptive statuses as roles. Repaired by converting their main role to the valid canonical verification classification and saving the original precise value in scope_role; no obligation was promoted. Added tests for rejecting invalid roles and preserving limited scope. CI rerun pending.

## First actual original-source augmented SI29 pilot

Fix one genuine rational original 470-source coefficient vector, supported only on the degree-zero original sine centered at 37/64 and the true sinh pole:
\[
 f(x)=1_{[-11/10,11/10]}(x)
      [12001\sin(2\pi(37/64)x)+16384\sinh(x/2)] .
\]
The SI29 augmented trial uses **the 14 TRUE continuous Jensen means / moments** (12 means and 2 first moments), not their SI25 Simpson quadrature proxies. Each new trial feature is pole-aligned by subtracting its true endpoint value divided by sinh(11/20), preserving the augmented span exactly.

The noncertifying pilot evaluates the actual seven-prime-power signed digamma multiplier numerically on FFT bins, pays the negative pole correction in positive Astar, and solves a sampled positive-form Galerkin problem. The SI29 trial features are severely nearly dependent; physical SVD cutoffs give resolved ranks 10–13 rather than an accurately represented full nominal rank-16 local trial. Consequently this is NOT the true complete 484D original Galerkin response.

Results (float64, NOT outward enclosed):

| Physical points / FFT pad | Truncated local rank | Sampled direct Kminus / Astar energy | Relative squared strong residual |
|:--|--:|--:|--:|
| 2048 / 4 | 10–11 | 0.99643 | 0.000587–0.000588 |
| 4096 / 4 | 10–11 | 0.99643 | 0.000590–0.000593 |
| 4096 / 8 | 10–11 | 0.99907 | 0.000464–0.000466 |

A rank-13 numerical cutoff yields comparable direct Kminus ratios; numerical relative residual around 0.000444–0.000560. These sampled direct ratios are ABOVE theta_SM40=0.96991358, while still BELOW 1: they may obstruct the *sufficient* MG07 scheme, but cannot prove an odd negative direction. The complete original SM40 cap dominates the exact direct Kminus, so a future RIGOROUS such ray would be a stopping witness for that one augmented trial/cap method. Numerical grids do NOT certify it.

The full MG07 strengthened SI06 residual cost c=Hinf/(kappastar*kappa) is about 3.7047e8. At theta_SM40 a necessary residual-only condition for any precise ray of this sufficient method is D/G < theta_SM40/c, approximately 2.618e-9. The numerical pilot is more than five orders of magnitude above that budget. Nor is any 470D G/N generalized spectrum known.

## Next strictly required work

1. **Certify a small-source method stopping witness with exact complete operator enclosures:** upper original Astar energy on the stated true rational f and lower original SM40 full 890-column/eta cap energy for the identical f. If Ccap(f) > theta_SM40 Astar(f), the source-only Galerkin trial V=ran(J470) fails the sufficient gate even with zero residual. This does NOT exclude an enriched trial or original odd positivity. The numerical margin against theta is about 0.026, suggesting a 1-percent rigorous enclosure might suffice.
2. For the enriched SI29 trial, first certify exact independent physical feature rank/conditioning and its complete original 484-by-470 action/strong residual data. Do NOT call SVD-truncated float output a full Galerkin obstruction.
3. If a chosen sufficient method is rigorously obstructed, change the method. Do not accumulate further tail bounds without a path to the original signed Loewner or native even/global RH obligations.

Reproducer: scripts/scout_rpb108_mg07_augmented_true_si29_two_source.py.
