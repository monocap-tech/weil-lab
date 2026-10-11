# RPB108 RC71 — rank-38 residual for the existing 22 source inputs

RC71 attaches the existing complete original 22-input source map to the actual rank-38 canonical projection. It evaluates all same-parity physical Legendre/source pairings through degree 37, including the archimedean, full paired-prime, and signed-pole terms. Mixed-parity pairings vanish exactly. This is a rectangular 38-by-22 attachment, not a new 38-input source covariance.

## Certified results

For the actual rank-38 projection and the existing 22 source inputs,

\[
\Gamma_{38}^{(22\text{ inputs})}\le (4323/512)M_{22}.
\]

The bound is approximately 8.443359375, compared with RC68's 471/32=14.71875. The certified upper bound improves by 1071/2512, approximately 42.6354%. This compares certified upper factors; it does not prove an equal reduction in actual leakage.

| Method and projection | Even upper | Odd upper | Uniform upper |
|---|---:|---:|---:|
| RC68 canonical trial subtraction, rank 22 | 471/32 | 5873/512 | 471/32 |
| RC71 physical subtraction, rank 22 | 4423/512 | 1371/256 | 4423/512 |
| RC71 physical subtraction, rank 38 | 4323/512 | 5191/1024 | 4323/512 |

Within the same physical-subtraction method, enlarging 22 to 38 features tightens the uniform upper factor by 100/4423, approximately 2.2609%. Most of the improvement over RC68 comes from the new subtraction estimate. Selected Young parameters are 2 for both rank-22 parity blocks, and 4 (even) and 2 (odd) for rank 38. The physical transfer-error enclosure is unchanged. Further head enlargement cannot be assumed to produce another comparable improvement.

## Exact physical subtraction into the actual head

Let i be the physical embedding from the canonical carrier and i* its Hilbert adjoint. The original source is Sigma_plus=i*F, where F=q+K_actual iR22. RC68 supplies the complete physical nominal source F_nom=q+K_nom V64, its covariance upper enclosure U, and the actual physical transfer Gram upper E_F.

For any physical polynomial p of degree at most 37, i*p belongs exactly to the actual 38-feature Riesz head. This follows from the physical target definition and the equality of the Chebyshev and Legendre polynomial spans. Therefore

\[
(I-\Pi_{38})\Sigma_+=(I-\Pi_{38})i^*(F-p).
\]

The embedding bound gives

\[
\|(I-\Pi_{38})\Sigma_+(v)\|_{\mathrm{can}}^2
\le\rho\|F(v)-p(v)\|_{\mathrm{phys}}^2,
\qquad\rho=252/257.
\]

This subtraction has no additional Riesz-trial error. The approximation error between F and F_nom remains fully paid using RC68's correlated physical transfer enclosure. The native target part q lies in both evaluated polynomial spaces and cancels from the actual projected source residual.

## Rectangular pairings and nominal residual

The validator computes enclosures for

\[
H_{nj}=\langle P_n,F_{\mathrm{nom},j}\rangle_{\mathrm{phys}},
\quad 0\le n<38,\quad0\le j<22.
\]

The pole contribution is 2(-1)^n times the exponential moment of P_n times that of the native trial column. All 14 paired-prime translations and 15 support segments are included. The source forms and their explicitly paid regular-kernel omission use the RC68 convention unchanged.

For each head count m in {22,38}, choose the exact rational physical polynomial coefficient matrix L_m=D_m^-1 H_mid,m. The covariance of the nominal residual is bounded by

\[
W_m\ge U-H^*L_m-L_m^*H+L_m^*D_mL_m.
\]

Each pairing-center halfwidth is paid through a diagonal row-sum Gram allowance. Outward matrix rounding is also paid. The validator independently checks W_m is PSD; no negative numerical variance is discarded.

The central nominal capture increment H_mid,22:38^* D_22:38^-1 H_mid,22:38 is exact PSD and is stored. It is a physical nominal quantity. It is not identified with the actual canonical projection gain, and separate interval allowances can prevent rounded residual upper matrices from having the same exact difference.

## Actual residual upper and input normalization

For each parity, explicit rational Young parameters give

\[
\Gamma_m\le\rho\big((1+t)W_m+(1+1/t)E_F\big).
\]

The finite parameter grid is {1/16,1/8,1/4,1/2,1,2,4,8,16}. Every candidate is compared with RC67's certified actual 22-input canonical Gram lower bound by exact PSD bisection. The selected candidate is checked again after final outward rounding.

All relative bounds use the actual canonical norm of the existing 22 source inputs. The new projection has 38 output-head features. Those two dimensions must not be conflated.

The same fixed source map also satisfies Gamma38 <= Gamma22 by the actual nested-projection identity of RC70. Thus the retained scalar upper is the smaller of RC68's 471/32 and RC71's directly evaluated rank-38 bound. This is an upper bound; its size does not establish actual source-budget failure.

## Independent replay

Generation uses all three archimedean log components and physical prime monomial primitives. Replay uses reflected two-log pairings, affine prime-source moments followed by an exact binomial change of coordinates, and closed exponential primitives for the test polynomials. Replay checks every saved pairing enclosure, independently completes the nominal residual square, checks exact physical Legendre orthogonality, and verifies final canonical comparisons after a Legendre congruence. It reproduces the certificate exactly.

## Evidence boundary

RC71 evaluates a rank-38 projected residual for the old 22-input map. It supplies no 38-input covariance, positive Weil head floor, complement floor, exact actual projection coefficients, or numerical actual canonical projection gain. It does not establish the inherited scalar source budget, source-budget failure at rank 38, whole-aperture positivity, RH, or F4.

RC69's necessary head-count lower bound and RC63's weak-floor ceiling remain unchanged. The result advances the larger-projection interface while retaining those constraints. All historical milestone files remain unchanged.
