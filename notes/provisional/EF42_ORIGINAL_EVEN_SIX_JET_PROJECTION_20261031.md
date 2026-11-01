# EF42 — Original first-cluster six protected even jets; quantitative Gram conditioning

**Date:** 2026-10-31. **Active obligation:** `W-EVEN-FORM` OPEN. Parent EF41 draft [PR #449](https://github.com/monocap-tech/weil-lab/pull/449), final focused [Actions #41269133991](https://github.com/monocap-tech/weil-lab/actions/runs/41269133991) SUCCESS, head `06ab039e3a04150033f4c9ea04c3e169f1b5edb9`.

## 1. Genuine original SI10 source rows and original physical operator

Original SI10 first protected frequency has center `c0=37/64`, with source-derived Taylor order **15** from the unchanged 107-cluster / 469-real-even-source inventory. On the physical interval `I=[-11/10,11/10]`, the six authentic real-even Fourier jets (up to harmless overall derivative signs) are

[
v_{2k}(x)=x^{2k}\cos(\omega x),\quad
v_{2k+1}(x)=x^{2k+1}\sin(\omega x),\quad
\omega=2\pi(37/64),\quad k=0,1,2.
]

All SIX rows are literal original protected SI10 functions. The genuine complete original signed first-source response remains

[
g_e=a_{\rm arch}(37/64)e+z+h_{\rm cut},
]

where `e=v0`, `z` is the complete original physical seven-prime-power source translation (`n=2,3,4,5,7,8,9`, actual signed original `w_n=(ln p)/sqrt n`, including n4,n8,n9) together with the true positive even pole gradient `2u cosh(x/2)`, and `h_cut` is the full original EF26/EF29 quarter-digamma physical half-integer cutoff series. The first arch term `a_arch(c0)e` is exactly in the protected source space; it is removed only under the valid protected/cofinite projection.

As EF39–EF41, define `H40=z+h40`, with `h40` the first **40** genuine signed physical Laplace cutoff modes; EF39 native originals retain its complete signed 40x40 arch Gram. The true original infinite remainder `h_tail` for `m>=40` is rigorously bounded by `||h_tail||<57/500+1/10000`.

## 2. Actual six-row physical Gram Schur, not a floating inverse

`scripts/validate_rpb108_ef42_original_even_six_jet_projection.py` replays the original first cluster order=15 and computes all six actual source pairings `b_i=<H40,v_i>` across the eight original positive-half physical cutoff cells. It uses native 10^340 directed rational fixed-point enclosures for exact antiderivatives of `x^n exp((a+i beta)x)`. Original arithmetic translations and positive pole are integrated without being dropped, and the 40 signed original arch modes are evaluated at bounded physical exponential endpoints `exp[-lambda_m(B±x)]`, avoiding exponentially growing substituted sources.

The exact physical `6x6` Gram `G_ij=<v_i,v_j>` is evaluated by the same original interval primitives for `x^(i+j)`, `x^(i+j) cos(2omega x)`, and `x^(i+j) sin(2omega x)`. An original-source Schur/Gram-Schmidt sequence calculates physical squared residuals `D_k`, with every pivot strictly positive and every subtraction interval-outward.

| Original source rows | Positive Gram pivot | Squared projection gain | Remaining signed finite response squared `D_k` |
|---|---:|---:|---:|
| 1 | 1.2363494115 | 0.41780698674 | 0.062320012550 |
| 2 | 0.28829890668 | 0.005257751141 | 0.057062261409 |
| 3 | 0.16703295695 | 0.001651701716 | 0.055410559694 |
| 4 | 0.027484393523 | 0.008649828192 | 0.046760731501 |
| **5** | **0.00068092005019** | 0.003878434504 | 0.042882296998 |
| **6** | **0.000010037139187** | 0.002349242492 | **0.040533054506** |

Native strict exact-rational pivot lower gates are `q4>1/1500` and `q5>1/100000`. The strict finite square upper gate is **`D6<41/1000`**. Each first-four-row squared residual replays the EF41 source result, with no assumption that the Gram of all 469 rows is well-conditioned.

**Critical quantitative conditioning finding:** The last pivot is now over five orders of magnitude smaller than the first. The six-row Gram is positive definite, but unscaled monomial-jet elimination is becoming a poor long-range strategy. This is not an obstruction to the underlying even Weil form; it is a warning about the certificate architecture and its error budget.

## 3. Complete infinite original cutoff and actual full cofinite upper

Because the six original even jets are contained in the unchanged protected `V469`, and the exact arch scalar row is protected, the full true cofinite projector `P_F` is a contraction of the six-row residual. The entire missing `m>=40` arch physical cutoff is paid using the original EF39 complete norm bound, not truncated:

[
\|P_Fg_e\|_{L^2(I)}
<\sqrt{41/1000}+57/500+1/10000
<203/1000+57/500+1/10000
<\boxed{8/25=0.32}.
]

The inherited original SI10 full signed even cofinite floor `q_even(f,f)>mu||f||²` with `mu=17/25000` gives

[
\boxed{\eta < (8/25)^2/(17/25000)=2560/17\approx150.58824}.
]

This improves EF41's `eta<25000/153≈163.39869` by about 7.8%. The strictly positive `eta>0` in EF34 retains its separate original arithmetic-jump/pseudolocality and form-core premises; the upper uses source-original physical Fourier/quarter-digamma identity and the inherited strong-domain attachment, both still open to independent analytic review.

## 4. Precise theorem standing and EF43

- Only **six** of the original 469 protected even source rows are projected; nine further genuine jets remain in the first original center, and **463 total** original protected even source rows remain unprojected. The original full 469D source Gram, true q-energy Riesz inverse and exceptional even Schur matrix are not computed.
- Even the improved upper `eta<2560/17` is vastly above the EF33 restricted first-source/kernel Schur margin `S2>1/500`. Therefore it does **not** determine the full first-source cofinite Schur sign or full even PSD.
- EF42 is an original arithmetic/interval-source certificate, not an independent complete form-domain, Fourier or RH proof. The paused original odd obstruction, whole Weil form and RH remain OPEN.

**EF43 next:** retype the monomial jet projection into a numerically/interval-stable **source-span-preserving orthogonal basis** rather than blindly adding further unscaled high-degree jets. The exact original protected span must be preserved, including genuine first-center Taylor cutoff identity, while the full signed original physical source response and entire infinite arch tail remain attached. Compare the conditional Gram pivots and fully certified residuals at identical source span to locate whether the present conditioning decay is intrinsic to the subspace or an artefact of the monomial representation. Only then extend toward the remaining nine same-cluster jets. No main merge.

Focused script `scripts/validate_rpb108_ef42_original_even_six_jet_projection.py`; workflow `.github/workflows/ef42-original-even-six-jet-source.yml`. Initial source native [Actions #41269337033](https://github.com/monocap-tech/weil-lab/actions/runs/41269337033) SUCCESS; stricter caps separately rerun at final-head CI.
