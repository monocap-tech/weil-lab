# EF45 — Original first SI10 ten even jets: conditioning, marginal projection, and decision gate

**Date:** 2026-10-31 Pacific. **Canonical obligation:** `W-EVEN-FORM` OPEN, paused `W-ODD-NEG` OPEN, entire Weil positivity/RH OPEN. **Parent:** EF44 [draft PR #453](https://github.com/monocap-tech/weil-lab/pull/453), native final-head [Actions #41273173395](https://github.com/monocap-tech/weil-lab/actions/runs/41273173395) SUCCESS; parent SHA `355d2e355d944cba9f254de4a705fc980fd8d4d1`.

## 1. Exactly unchanged original source and arithmetic identity

The genuine original SI10 protected real-even first frequency cluster has center c0=37/64, original Taylor order 15, and is embedded in the unchanged 107-cluster, 469-real-even-protected-source SI10 space V469. EF45 adds precisely two **authentic** original even source rows to EF44's protected first eight:

\[
v_{8}(x)=x^8\cos(2\pi c_0 x),\qquad
v_{9}(x)=x^9\sin(2\pi c_0 x),\qquad
I=[-11/10,11/10].
\]

These are exact even Fourier Taylor jets of the original SI10 first frequency, up to inessential overall Taylor derivative signs. There are thus TEN source-valid rows in the first cluster, with five still unprojected in that cluster and **459 unprojected directions among all original 469 SI10 rows**.

Retain the true signed original first-source gradient after subtracting only its actual SI10-protected constant arch row. Its finite-mode physical part H40=z+h40 consists of EVERY original source translated prime-power response n=2,3,4,5,7,8,9 with true signed weights log(p)/sqrt(n), the actual even cosh pole 2u cosh(x/2), and the first 40 genuine physical quarter-digamma half-integer arch cutoff modes with EF39's complete signed 40x40 arch Gram. The remaining INFINITE m>=40 quarter-digamma cutoff is never discarded: inherited exact original bound \(\|h_{tail}\|<57/500+1/10000\).

## 2. Native 10x10 physical interval projection and exact rational retyping

Use the same original EF24/EF29 10^340 outward interval arithmetic, original eight positive-half arithmetic cutoff cells, and exact finite antiderivatives of x^n exp((a+i beta)x) to build the genuine physical Gram
\[
G_{ij}=\langle v_i,v_j\rangle_{L^2(I)},\qquad
b_i=\langle H40,v_i\rangle_{L^2(I)},\quad 0\le i,j<10.
\]
Evaluate all TRUE physical ten-row Schur pivots, signed marginal squared projection gains, and D8,D9,D10 without floating linear algebra. EF44 baseline D8≈0.031541398330, with seventh/eighth pivots ~9.9555424331e-8 and 7.0883034365e-10. The ninth/tenth actual pivots will be smaller; strict positivity must be established, never inferred from the numerical pattern.

Independently construct an exact lower-triangular rational C with strictly positive diagonal and all entries having denominators at most Q=10^42. C is chosen using a rounded Gram MIDPOINT solely as a basis-selection device. The vector span is identical to the ten authentic original source rows by exact invertibility, regardless of midpoint selection. Recompute the ACTUAL original physical transformed Gram \(K=C G C^T\) with full 10^340 outward intervals and certify \(\|K-I\|_\infty<10^{-7}\). Do not confuse physical source orthonormality of C v with small coefficients in the raw monomial representation; report max_i sum_j |C_ij|.

For true signed original pairings h=C b, use the symmetric Gram order \((1-\epsilon)I\preceq K\preceq(1+\epsilon)I\) to obtain independent, inverse-free certified bounds
\[
\|H40\|^2-\frac{\|h\|^2}{1-\epsilon}
\le \|H40-P_{V10}H40\|^2 \le
\|H40\|^2-\frac{\|h\|^2}{1+\epsilon}.
\]
Both independent bounds must enclose the original direct 10-row Schur result; an interval failure is a METHOD/CERTIFICATE STOP rather than evidence about signed Weil positivity.

## 3. Accept/stop and full original cofinite seam

This pass has three distinct certification gates:

1. New ninth/tenth actual original Gram pivots strictly positive and actual D10<D8 with outward intervals; otherwise local monomial/source method STOP with exact failing gate.
2. Exact rational C invertible and actual original transformed K near identity, with explicit coefficient row growth and **independent** projected-square enclosure; otherwise basis-conditioning METHOD STOP, not a theorem obstruction.
3. Whole infinite original arch tail paid and actual original cofinite first-source norm \(\|P_Fg_e\|\le\sqrt{D10}+\|h_{tail}\|\), and corresponding unseen first-source energy-dual \(\eta\le \|P_Fg_e\|^2/(17/25000)\). Only a strict source-certified bound with all tails included may improve EF44's previous \(\eta<85849/680\).

EF44 eight-row actual finite projected signed squared response was ≈0.031541398330<79/2500=0.0316, full source projected norm<293/1000 and eta<85849/680. An EF45 result should preserve the old certificate if the ten-jet conditioned method fails, not erase the accepted EF44 result.

Even a successful EF45 partial source projection does not compute the actual 469-source cofinite projector or q-energy Riesz inverse, and does not determine the sign of the **full** first-source Schur because EF33's genuine original restricted two-vector Schur positive lower bound is only S2>1/500. Original full W-EVEN-FORM PSD, the paused odd obstruction, full Weil/RH OPEN. Independent physical original Fourier/quarter-digamma identity and strong-domain/form-core verification OPEN. No main merge, no hidden proof promotion.

## 4. Custody

Source validator: `scripts/validate_rpb108_ef45_original_even_ten_jet_conditioning.py`. Dedicated CI: `.github/workflows/ef45-original-even-ten-jet-rational-conditioning.yml`. All source results must be linked to exact final-head successful CI and commit; draft PR and canonical obligation manifest update after verification.
