# MG35 — PSD-monotone original omitted-frequency source residual upper guard

October 20, 2026. Stacked on [MG34 PR #283](https://github.com/monocap-tech/weil-lab/pull/283). In the independently accepted original 24D original SI10/MG11 23+pole system, MG33/G34 established that adding [4,8] full source frequency coverage made both directly certified residual trace and the **conservative omitted-frequency upper** worse, even though the actual omitted frequency domain became smaller. This is because the sourcewise-Young lower Gram certificate, while rigorously below the true PSD source mass, is NOT itself guaranteed PSD.

## Rigorous PSD-safe remedy: nested omitted-frequency upper *reuse*

For fixed exact original rational B, write the true joint (pole-inclusive, seven-prime/digamma) residual Fourier row as

`r_B(xi)=t(xi)[I-a_o(xi)B+2e_p b^T B]`.

The true complete source residual covariance over a real frequency region D is

`X_B(D)=int_D r_B(xi)^T r_B(xi) dxi>=0`.

For *nested* measured sets C0 subset C1 subset C2, the omitted domains satisfy D2 subset D1 subset D0. Regardless of uncertain approximations to source mass,

```
  0 <= X_B(D2) <= X_B(D1) <= X_B(D0).
```

If MG32/33 independently established complete-original-frequency omitted-sector **Loewner UPPERS** U0, U1 and U2 for those exact same fixed B, every earlier Uj is still a valid upper for any later Dk subset Dj. One may choose any of these valid matrices as the later omitted-frequency upper. In particular, select the previously accepted Uj with smallest *exact rational TRACE*. This guarantees the **selected omitted upper TRACE** never increases as measured frequency sectors grow.

**Important mathematical precision:** the selected upper is a valid whole 24D Loewner upper BY THE PSD inclusion argument, NOT because smaller matrix trace implies Loewner order. Neither U_i<=U_j nor any improved Gershgorin margin is inferred. The accepted MG33 artifact stores exact bound TRACES but not its complete 24×24 residual covariance matrices; MG35 does NOT claim to independently recompute a new full matrix or certify source positivity from scalar trace.

On the same original MG30 scalar/nonscalar rational Bs and both k=12,16, recombine the MG33 source-specific direct JOINT upper for [0,4], [4,8], and exactly two genuine MG19 sites >8 with each legitimately inherited original omitted sector upper. Compare exact recombined trace to the verified MG32 baseline and MG33 published new-band/hybrid totals.

## Why not apply naive PSD clipping to MG33's indefinite mass lower?

Let H=[[1,1],[1,1]] PSD and L=[[0,1],[1,1]], with H-L=diag(1,0)>=0, so L is a rigorous but indefinite lower for H. Naively clipping L's diagonal to nonnegative diag(0,1) does **not** make a valid Loewner lower, since v=(1,-1) has v^T Hv=0 but v^T diag(0,1)v=1. Nor is the spectral positive-part L_+ generally an operator-monotone operation on noncommuting Hermitian matrices. MG35 never uses such a clipping substitution.

## Acceptance / mathematical limits

MG35 uses PINNED successful [MG33 Actions #39462301107](https://github.com/monocap-tech/weil-lab/actions/runs/39462301107) and [MG34 Actions #39467773045](https://github.com/monocap-tech/weil-lab/actions/runs/39467773045) and verifies each original marginal trace conservation identity **exactly with Fraction**, the same original B/cutoff, all three real-frequency sets, no new overlapping panels, and the exact valid PSD measure-inclusion proof for any reused upper.

The selected omitted-frequency TRACE guarantee is rigorous and nonincreasing. Yet each added directly measured band's positive upper TRACE still has to be paid, so the *combined whole residual upper TRACE* need not improve. The goal is to isolate this remaining actual calculation defect from spurious nonmonotonic source-mass credit.

A new source contraction requires an independent exact 24×24 residual Loewner matrix and strict source-metric positivity gate, which MG35's pinned scalar diagnostic artifacts do not contain. Absolutely no positive contraction, source-subspace invariance, full original 470D inverse, signed odd 51/56, independent original Fourier/form-domain verification, complete even/Weil/CC27/RH may be inferred.

**CI acceptance: PENDING.**
