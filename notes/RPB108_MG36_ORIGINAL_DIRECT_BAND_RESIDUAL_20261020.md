# MG36 — Original [4,8] direct joint covariance, full 24D source matrices

October 20, 2026. Stacked on independently accepted [MG35 #284](https://github.com/monocap-tech/weil-lab/pull/284). The immediate original obligation remains W-ODD-NEG. In MG33, adding source-frequency [4,8] with 32 original physical interval cells increased the joint residual upper trace by about +5.03 for the scalar B, while its sourcewise-Young physical mass lower also made the omitted remainder upper ~+0.70 worse. MG35 repaired the nonmonotone omitted-mass *method* using valid old remainder Loewner-upper reuse, but the [4,8] measured *direct* residual upper remains large. MG36 addresses that latter cost **without modifying any original source identity**.

## New rigorous alternative to cellwise Young covariance upper

On each positive original frequency cell `[a,b]`, including the negative-frequency mirror, form the **true 24-channel residual Fourier row** before squaring:

```
r_B(xi) = t(xi)[I - a_o(xi) B + 2 e_p b_phys^T B].
```

The same accepted MG29 source value, derivative, third/fourth Taylor enclosures, original SI10 physical pole coefficient intervals and original signed seven-prime/digamma whole-cell multiplier give an affine center with bounded per-coordinate remainder:

```
r_j(xi) = v_j + d_j (xi-mid) + e_j(xi),
|e_j(xi)| <= rho_j
```

where `mid=(a+b)/2`, `half=(b-a)/2`. Importantly, all original Fourier source/multiplier/pole corrections enter v,d,rho *before* this estimation.

The previous MG32/MG33 24D upper used a rational Young parameter `tau>0`:

```
U_Young = (1+tau) P +2(b-a)(1+1/tau) diag(S*rho_j),
P=2(b-a)(v v^T + (b-a)^2 d d^T/12), S=sum rho_j.
```

This is a valid sourcewise-Young Loewner upper, but applies a global (1+tau) surcharge to the **whole affine covariance**.

MG36 derives an *independent* exact-rational PSD-dominating bound by preserving P without that surcharge and bounding **only the unknown covariance remainder**. Define `alpha_j=|v_j|+half |d_j|`, `A=sum_j alpha_j`, `S=sum_j rho_j`. Every entry of the unknown symmetric covariance correction satisfies

```
|Delta_ij| <= 2(b-a)[ alpha_i*rho_j
                      +rho_i*alpha_j
                      +rho_i*rho_j ].
```

The elementary inequality `2 |u_i u_j| <= u_i^2+u_j^2` implies `Delta <= diag(sum_j entry_error_ij)` in Loewner order. Therefore the following **complete 24x24 MATRIX**, not merely trace or diagonal, is a rigorous upper:

```
U_row = P + diag_j(2(b-a)[alpha_j*S+rho_j*A+rho_j*S]).
```

Both candidate matrices are upper Loewner bounds on the genuine original interval covariance. **Selecting the one with smaller exact rational trace retains a valid Loewner upper** for that cell, although it absolutely does *not* prove the matrices are Loewner-ordered by trace. Reuse MG32's accepted full-matrix outward `finalize` export, preserving a sourcewise nonnegative rounding fee.

## Whole-real original frequency and acceptance

Recompute the independently accepted MG32 `[0,4]` full source residual covariance, exact MG33 original 32-cell `[4,8]` source Taylor data, and evaluate the new matrix for every original [4,8] cell. The original MG33 *band* upper trace and MG32 *prefix* upper trace must replay exactly. In each original k=12/16 and same MG30 scalar/nonscalar rational B, compare:

1. MG32 complete [0,4] baseline with its rigorous *entire original-frequency* omitted Loewner upper.
2. MG35 original [0,8] PSD-safe guard, retaining the valid MG32 omitted-frequency upper matrix on the smaller omitted set.
3. MG36 new `[4,8]` **complete 24D original source residual upper matrix**, with per-cell smaller-trace rigorous covariance upper and same rigorously valid PSD-monotone inherited remainder matrix.

Recompute and **export every entry** of the full 24×24 new band upper, complete-original-frequency Rupper and Hlo−Rupper. Strict source contraction is promoted ONLY if an exact positive Gershgorin margin of the complete *matrix* difference is demonstrated. No smaller trace alone can prove it.

The accepted MG35 artifact stores trace-only diagnostics, so the MG36 calculation reconstructs matrices from the independently accepted original-source scripts/artifacts, rather than inventing them from scalar summaries.

Even a strict positive original 24D source residual would not prove source-subspace invariance, a full 470D strong inverse, the original signed odd 51/56 negative cap, even/Weil/CC27/RH or independent Fourier/form/domain identification.

**Actions acceptance: PENDING.**
