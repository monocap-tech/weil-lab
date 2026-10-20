# MG16 — Exact weighted Fourier moments and genuinely source-correlated affine covariance

October 19, 2026. This stacks on verified MG15 #264, whose source-dependent rational first/second original Fourier moments have **lower-reference inertia (3+,21−,0)** on all seven Young parameters. Complete original W-ODD-NEG, even, Weil/CC27/RH and independent Fourier/form-domain hypotheses remain OPEN.

## Changed mathematical architecture

MG15 uses pointwise multiplier extrema l,u on each original real-frequency cell and integrates constant-weight affine source covariances. MG16 instead uses SM46's **actual certified original piecewise-affine positive multiplier reference** w_ref=max(kappa, interpolated signed digamma+seven-prime multiplier) or its valid constant-cell choice. It integrates J_n^(p)=int_cell (xi-mid)^n w_ref(xi)^p dxi exactly, for n=0,1,2 and BOTH p=1 (A_o) and p=2 (A_o-squared). The reference may cross its kappa floor; the exact rational integration splits at that crossing. Independent use of the existing SM46 J0,J1,J2 for p=1 checks the new integration.

As in MG11–MG15, the physical Fourier channels are the 23 actual double-boundary-vanishing original supported source combinations plus genuine original sinh pole, with all 24x24 mixed crosses. At every selected original MG15 cell, the SM44/46 original true source transform and endpoint coefficient enclosures give

  T(xi)=V(xi)+e(xi), V(xi)=v+d(xi-mid), |e_i(xi)|<=r_i.

The complete weighted affine reference is

  C_p=J0^(p) vv^T + J1^(p) (vd^T+dv^T) + J2^(p) dd^T.

Unlike scalar-weighted MG15, it retains a potentially **nonzero multiplier-source correlation** through J1. C_p is PSD as the exact integral of a positive weight times V V^T; quantization/export is paid separately.

Weighted Cauchy gives e e^T <= D_r=(sum_i r_i) diag(r_i), and whole-matrix Young yields, for any rational 0<tau<1,

  (1-tau)C_p-(tau^-1-1)J0^(p)D_r
  <= int_cell w_ref^p T T^T
  <= (1+tau)C_p+(1+tau^-1)J0^(p)D_r.

**Critical weight-error term:** the reference multiplier is NOT silently promoted to the original multiplier. SM43A provides a rational pointwise error |w_true-w_ref|<=eps. For p=1 set eta_1=eps, and for p=2 set eta_2=eps*(2 sup w_ref+eps). If |T_i|<=q_i=|v_i|+width*|d_i|/2+r_i, the true covariance obeys T T^T<=D_q=(sum q_i)diag(q_i). Therefore an independent whole-matrix full-frequency-sign error 2*width*eta_p*D_q is added in both directions. All original multiplier crossings, source mixed entries, and pole are paid.

The final rigorous selected-panel Loewner sandwich, including the positive and reflected negative real Fourier frequency signs, is

  2[(1-tau)C_p-(tau^-1-1)J0^(p)D_r-width*eta_p*D_q]
   <= M_p(cell)
   <=
  2[(1+tau)C_p+(1+tau^-1)J0^(p)D_r+width*eta_p*D_q].

Both first and second moments are complete 24×24 source matrices, but the second is **A_o-squared, not original pole-corrected Astar-squared**. MG16 tests all seven exact original MG15 tau parameters and a per-cell trace-optimized weighted family, with exact rational full-matrix inertia and outward symmetric row-sum export fees.

## Method gate

An independently rebuilt MG15 complete original 24×24 reference is the comparison baseline, with exact prior accepted inertia. The new weighted moments can be stronger or weaker: MG16 must not assume that source-multiplier correlation improves the bound. Acceptance requires measured reference inertia and negative margins, not positive trace alone. All 24 cells cover only 3 selected small intervals and NOT the entire original [0,Lambda] band.

If the lower-reference inertia remains 21 negative, the next methodological target is a *correlated remainder-source Gram and joint spectral preconditioner*, not endlessly optimizing scalar/diagonal Young parameters. To certify true original 23D strong Galerkin residual or all 470-source Astar inverse, the entire low band, high logarithmic tail, pole-corrected Astar² cross response and independent form/domain audit are still required.

Reproduce:

  OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 python scripts/validate_rpb108_mg16_weighted_affine_source_moments.py


## Verified result — fundamental flat-multiplier pilot obstruction

The original MG16 arithmetic passed GitHub Actions [39351668605](https://github.com/monocap-tech/weil-lab/actions/runs/39351668605) and its independent 24D rational inertia replay. A subsequent diagnostic rerun [39352050679](https://github.com/monocap-tech/weil-lab/actions/runs/39352050679) ALSO PASSED and revealed the exact cause of non-improvement:

- All **24 of the 24 selected genuine source-frequency cells** use SM43A's original_constant_cell reference.
- On ALL 24 cells, the reference weight is **exactly kappa**, and the certified pointwise reference/true-multiplier error is **zero**. Therefore the true original positive multiplier itself is identically kappa on each of these frequency cells.
- **Zero** cells have a nonflat certified weight reference; **zero** cells have a nonzero multiplier-reference error.
- The MG16 true source first-moment and A_o² second-moment lower and upper TRACE results are IDENTICAL to MG15, with same exact reference inertias (3 positive, 21 negative, 0 zero).
- A final fail-closed amendment verifies the **full 24x24 LOWER and UPPER rational matrices** agree entry-by-entry with independently recomputed MG15 on both moments, not just the traces or inertias.

**Formal methodological inference:** when w_true=w_ref=kappa on an entire panel, its exact J1=0 and J0=kappa*h, J2=kappa*h³/12; all weighted first/second affine moment schemes reduce identically to the existing constant-weight source-affine scheme, provided source-error schemes and tau values agree. Therefore **reoptimizing multiplier-weighted source moments cannot improve the fixed original 24-cell lower reference**, no matter how accurate the moment integration is. This is a local **method no-go conditioned on the fixed selected panels**, not a no-go for the original full Fourier band or the actual signed operator.

**MG16 disposition:** ACCEPT exact analytic weighted first/second moment infrastructure; REJECT the *existing 24 selected cells* as a discriminating test of multiplier-source correlation. The next method should select original frequency cells with **certified nonconstant a_o(xi)** (including actual seven-prime/digamma variation and any kappa crossing), carry all original physical source cross terms, and compare spectral inertia with the unchanged source-affine baseline. This is more fundamental than further tightening an error budget where the original weight is identically constant.

Full low-frequency integration, the actual pole-corrected Astar² and original 470-source Galerkin residual, complete signed odd/even Weil and RH remain OPEN.
