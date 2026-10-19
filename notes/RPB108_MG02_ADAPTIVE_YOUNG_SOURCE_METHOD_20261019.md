# MG02 — Adaptive Young source-mean method gate (stacked on SM62)

**October 19, 2026 — method viability only — W-ODD-NEG, full odd/even, Weil, CC27 and RH OPEN.**

## Why this is a different method test

SM60 showed that the existing SM58 23-coordinate signed LOWER reference is negative definite. SM61's mixed-block Schur bounds are mathematically valid but cannot change that fact when their complement starts at the same negative-definite lower. SM62 therefore adds 338 previously unused genuine signed-positive original real-frequency windows to the entire 25-source lower, rather than only improving the mixed block.

MG02 independently tests whether **the way SM62 pays complete-source mean uncertainty** is throwing away most of the new positivity. It keeps exactly the same 338 disjoint original SM54 (96) / SM55 (242) windows, the same 49 previously credited windows, all 973 original signed-negative leaves, and the exceptional odd sinh pole. The only variable is the mathematical inequality used to enclose the uncertain full **25-component physical Fourier mean**.

## A rigorous alternative complete 25D Loewner bound

On a real-frequency cell, write its exact 25-vector Fourier mean as (u=v+e), where (v\in\mathbb Q^{25}) is the exact-rational physical midpoint proxy and (|e_i|\le r_i) from the original SM42/44/46 source and curvature enclosures. Set (R^2=\sum_i r_i^2), and let (\gamma=2|I|(m_{I,\mathrm{lo}}-\kappa)>0). Only the *excess over* (\kappa) is newly credited, to avoid double-counting the original SM58 physical-Parseval floor.

SM62's ordinary scalar-Cauchy certificate is
\[
\gamma uu^T \succeq
\gamma vv^T-\gamma\bigl(2\sqrt{\|v\|^2R^2}+R^2\bigr)I_{25}.
\]
This pays a linear-in-(R) scalar error in **all** 25 directions, even though most of the uncertainty is concentrated along the rank-one source vector.

For every rational (0<t<1), the identity
\[
(v+e)(v+e)^T-(1-t)vv^T+(t^{-1}-1)ee^T
=\frac{(tv+e)(tv+e)^T}{t}\succeq0
\]
and (ee^T\preceq\|e\|^2 I\preceq R^2I) give the independently valid **full-source, all-cross** enclosure:
\[
\boxed{\gamma uu^T\succeq
\gamma(1-t)vv^T-\gamma(t^{-1}-1)R^2I_{25}.}
\]
It trades a controlled fraction of the favorable rank-one gain for a potentially much smaller full-matrix diagonal fee. This formula is not a componentwise positivity assertion: it is an operator-order inequality on all 25 source coefficients.

MG02 tests (t\in\{1/256,1/128,1/64,1/32,1/16,1/8,1/4,1/2\}) and the original SM62 scalar alternative on each identical cell. It chooses the candidate maximizing the exact trace of its **23-coordinate complement LOWER**. Every candidate separately obeys the full 25D Loewner inequality; the adaptive selection is therefore valid on any mixed 25-vector. Maximizing trace is merely a diagnostic, **not** a claim of Loewner dominance, positive definiteness or spectral classification.

All irrational square-root upper bounds, rational weights, and full matrix export errors are rounded outward. At 96, 192, 288 and 338 windows, independently compute both complete 25D rational LOWER inertias and the complementary 23D LOWER inertias. Negative pivots of either LOWER are not genuine negative eigenvalues of the original form.

## Acceptance and decision rule

A successful focused run must (a) reproduce the exact SHA-256 hashes of all 625 entries of the **original passing SM58 signed LOWER and complete negative UPPER**; (b) confirm disjointness and positivity of all 338 original windows and the original 49 already-paid windows; (c) pay every actual 25D cross and source error in the Young or scalar bound; (d) choose at least one Young improvement in the exact raw 23D lower trace; (e) show nondecrease of the 23D lower trace within the independently paid rational export fees; and (f) report **both** 25D and 23D reference inertias without promoting them to actual operator signs.

- **Continue the adaptive bound** if the coupled 23D complement lower spectrum becomes materially closer to PSD, under independent exact replay and all original full-source premises.
- **Redesign again** if only trace improves while the lower complement remains strongly indefinite; consider signed-frequency integrals on the weak eigenvectors and matrix-weighted (not scalar) source errors.
- **Do not infer** even from a positive 25-source signed LOWER that the actual 470-source corrected exceptional Schur or infinite remainder is positive.

The independent Fourier formula, supported operator domain, 470-source source-completeness and even-sector/Weil/RH transfer remain separate open mathematical obligations.

Reproduction: `python scripts/validate_rpb108_mg02_young_source_enclosure.py`.
