# SM47 — Whole original low-frequency 25-source Jensen lower via SM12 positive bands

**October 18, 2026.** Independent one-sided original-source lower certificate, stacked on SM46 draft PR #228. Canonical `W-ODD-NEG` (odd O1/O2), even E1–E4, original signed Weil, CC27, and RH remain **OPEN**.

## Bottleneck and change of method

SM46 passed full 625-entry original-source affine Fourier window construction at final-head focused Actions run **39188523031**. The true original source-window matrix error at mesh 1/8 was `76.978784539`: of this `45.610847484` comes from original true seven-prime/digamma scalar interpolation, `31.367937056` from source Fourier integration. It certifies a two-sided approximation only on the 16 source-centered windows of measure `1029/64` and is too loose for original `Astar` inversion.

**SM47 changes the target.** Instead of paying a two-sided approximation error across all `[0,4096]` source-frequency cells, derive a **one-sided Loewner lower bound** across the entire original low band using (i) the existing SM42 Parseval floor, and (ii) exact original SM12 strictly sign-positive intervals and Jensen's inequality. Omitted positive-frequency excess is **nonnegative**, not an unchecked remainder. This does **not** identify the full low operator or turn a finite-source bound into complete original odd positivity.

## Mathematical statement

Take the original SI10 zero-extended physical supported odd 25 source functions (g_i): sixteen (sin(2\pi c_i x)), eight (xcos(2\pi c_i x)), and the genuine (sinh(x/2)) pole, all on ([-11/10,11/10]). Write

[
 T_i(\xi)=\int_{-B}^B g_i(x)sin(2\pi\xi x)\,dx,qquad
 H_{ij}=\int_{-B}^B g_i(x)g_j(x)\,dx
      =2\int_0^\infty T_i(\xi)T_j(\xi)\,d\xi.
]

Let (m(\xi)) be the actual original seven-prime signed multiplier plus digamma term, (a_o(\xi)=max{\kappa,m(\xi)}) and (\kappa=10^{-3}). Define the actual original positive low source form

[
 A_{\mathrm{low},25}=2\int_{0}^{4096} a_o(\xi)T(\xi)T(\xi)^T\,d\xi.
]

The SM42/SM41 original source tail was certified as
[
2\int_{4096}^\infty T(\xi)T(\xi)^T\,d\xi
 \preceq \frac{2E}{4096}I_{25},\qquad E=\frac{202}{25}.
]
Hence (A_{\mathrm{low},25}\succeq\kappa(H-2E/4096\,I)).

SM12 already certified **17 mutually disjoint real signed-positive intervals** (I_j=[c_j-r,c_j+r]), (r=1/100), (0<I_j<4096), where the actual original (m(\xi)>\kappa+\Delta) everywhere, (\Delta=2). This is a whole-real interval result with the original seven prime terms, not sampled endpoint optimism. Write
[
u_j=\frac{1}{2r}\int_{I_j}T(\xi)\,d\xi,qquad\gamma=4r\Delta=\frac{2}{25}.
]
Jensen gives the **complete low source-bound**
[
\boxed{
A_{\mathrm{low},25}\succeq
 \kappa\left(H-\frac{2E}{4096}I\right)
 +\gamma\sum_{j=1}^{17}u_ju_j^T.}
\tag{SM47-A}
]
This includes every source cross and the actual pole, without double-counting the floor or adding SM46's overlapping selected windows.

## Fully rational matrix and all-source mean error

The frequency average removes the linear Fourier derivative **exactly**. For each true interval ([c-r,c+r]), the original physical Fourier antiderivative intervals of SM42/SM44 and actual SI06/SM46 second/third derivatives yield
[
 |u_{ij}-v_{ij}|\le e_{ij}
 :=r_{ij}^{(0)}+\frac{K_{ij}r^2}{6},\quad
 K_{ij}=\min\Big\{K_{i,\mathrm{global}},
 |T_i''(c_j)|_{\mathrm{upper}}+r M_{3,i}\Big\}.
]
No numerical sampling, hidden source averaging assumption, or general (k>1) physical polynomial-source extension is used. (T_s'') for the pole uses the certified spatial bound. Let (P=\gamma\sum v_jv_j^T), with all 625 rational entries formed exactly. Using (V_j^2=\sum_i v_{ij}^2), (R_j^2=\sum_i e_{ij}^2), exact outward integer-square-root ceilings prove
[
\left\|\gamma\sum u_ju_j^T-P\right\|\le
 \epsilon_P:=\gamma\sum_{j=1}^{17}
 [2\sqrt{V_j^2R_j^2}+R_j^2].
]
The `sqrt_upper` values are true rational upper enclosures. Independently, take the SM42 **original** full 25×25 interval physical Gram (H), rational midpoint matrix (H_q), and (epsilon_H) equal to the maximum exact absolute row sum of the entrywise interval/rounding errors. Then (H\succeq H_q-\epsilon_H I).

Therefore
[
\boxed{
A_{\mathrm{low},25}\succeq
 \kappa H_q+P-
 \left[\epsilon_P+
 \kappa\left(\epsilon_H+\frac{2E}{4096}\right)\right]I_{25}.}
\tag{SM47-B}
]

The exact unrounded Jensen positive reference and the displayed (P) are PSD by construction. **The final lower matrix including a negative scalar error is not automatically PSD**. Do not infer positivity, invertibility, a spectral index, or negative-frequency absorption from the source-gain test alone.

## Acceptance and failure conditions

The new validator must:

1. Re-run SM12's **actual original whole-real signed seven-prime positive 17-window** check and verify bands are disjoint and inside `[0,4096]`.
2. Construct every original supported SI10 physical source transform at each of the 17 original rational positive centers, including sine, xcos and real sinh pole; bound the source *frequency mean*, not a sampled quadrature.
3. Form the full rational 25×25 Jensen (P) with **all** source cross terms and an outward complete-operator (epsilon_P). Fail closed unless (epsilon_P<1/10) and at least one actual physical source-coordinate diagonal gain exceeds its own entire (\epsilon_P).
4. Reuse the exact SM42 original physical Gram intervals and the existing original whole-low high-frequency tail, paying all errors by exact rational row-sum Loewner domination.
5. Explicitly retain entire 470 genuine original higher polynomial source columns, original `Astar` pole-conditioned inverse/strong residual, complete signed odd O1/O2, even E1–E4, signed Weil, CC27 and RH as **open**. Independent original physical Fourier/closed-domain proof audit remains open.

This is **not** a claim that the original operator has only one negative direction, nor a replacement for complete-operator parity-resolved spectral certification. In particular, neither SM47-A nor SM47-B certifies the effective exceptional pole compensation or the complete orthogonal remainder.

## Verification/custody

New focused Python validator: `scripts/validate_rpb108_sm47_original_full_low_jensen.py`. GitHub Actions workflow: `.github/workflows/rpb108-sm47-full-low-jensen.yml`. The artifact exports the rational 25×25 lower and positive-source matrices and exact errors. **Until the focused PR-head Actions pass, all new numeric acceptance values remain unverified and should not be promoted.**

**Next gate SM48:** confront the resulting **complete original** 25×25 lower matrix with the original negative-cap source directions, and determine whether the Jensen positive subspace and original pole-conditioned inverse can be certified with a residual relative to the original physical Gram. Extend to all 470 original sources only with verified original (k>1) physical transforms and complete Schur residual. A 17-window gain by itself does not close W-ODD-NEG.
