# MG13 — Original coupled low-frequency two-moment gate

October 19, 2026. Stacked on MG12 PR #261. Whole odd/even/Weil/CC27/RH and the original Fourier/domain premise audit remain OPEN.

MG12 passed an exact physical 23-source Gram certificate, but its whole-band scalar strong-action bound was enormously conservative. MG13 builds two rigorously enclosed original low-frequency matrices using true Fourier source values, not sampled FFTs.

Use the actual MG11 double-boundary supported odd physical functions h_i=f_i-a_i*s-c_i*f_23 (23 channels) and the original sinh pole s (one channel). For 24 disjoint rational real-frequency panels in three selected regions, SM43 bounds the actual original multiplier by l<=a_o(xi)<=u, including all seven prime terms and digamma. SM44 exact midpoint Fourier values and original derivative/curvature bounds enclose the full 24-vector T(xi) by v+e with ||e||^2<=E2.

The complete-source covariance identity gives -delta*I <= TT^t-vv^t <= delta*I, where delta=2*sqrt(||v||^2*E2)+E2. Every cell contributes two true original source Loewner sandwiches:

2*h*l*(vv^t-delta I) <= 2*integral_cell a_o TT^t <= 2*h*u*(vv^t+delta I),

2*h*l^2*(vv^t-delta I) <= 2*integral_cell a_o^2 TT^t <= 2*h*u^2*(vv^t+delta I).

The factor two covers both Fourier frequency signs for real odd sources. Both complete 24x24 source matrices retain every h_i cross and the original sinh pole channel. Final rational export pays a row-sum symmetric matrix error in Loewner order.

This is a selected-panel low-frequency moment certificate only, NOT the entire [0,Lambda] band. The second source moment is for A_o squared. The true Astar squared additionally contains original pole cross-response terms and is NOT certified by these panels. The original strong Galerkin residual, entire 470-source resolvent, odd/even/Weil/CC27 and RH remain open.

Decision: measure matrix error versus rank-one source response. If intervals are too loose, improve coupled affine source transforms rather than scaling the panel count indiscriminately. When useful, extend both moments across the entire low band with MG11 certified high tail and build the actual Astar strong residual.

## Accepted exact-rational method-gate result

The dedicated GitHub Actions run [39344407722](https://github.com/monocap-tech/weil-lab/actions/runs/39344407722) **PASSED** all original 24-channel moment and no-theorem-promotion checks.

On the 24 original coupled real-frequency panels, the complete certified first positive moment source matrix had lower-reference trace **−0.003790888628** and upper-reference trace **+0.006270752428**. The complete second (A_o-squared) moment source matrix had lower-reference trace **−0.000003827808** and upper-reference trace **+0.000006305924**.

Both lower-reference traces are negative, which is compatible with an actual positive-semidefinite source moment because the lower references are conservative. This is not an actual negative mode or signed odd positivity result.

**Decision: ACCEPT the construction of complete 24-channel first and second original Fourier source-moment sandwiches on the test regions; REDESIGN the per-cell approximation to improve spectral usefulness.** Existing pointwise midpoints and whole-matrix uniform covariance errors are too coarse to establish positive lower traces even on these 24 selected cells. Next method gate: integrate the certified AFFINE frequency variation in each source and use correlated whole-matrix error enclosures, while preserving the original multiplier, actual physical pole, and source cross terms. Only after such selected-panel tests improve should the whole [0,Lambda] low band and true Astar strong residual be attempted.

