# SM45 — Original physically supported local Fourier derivative: sharper complete source-window stiffness error

**Canonical W-ODD-NEG · stacked on SM44 draft PR #226, whose final-head focused CI passed.**

## Actual bottleneck and one mathematically precise correction

SM44 now produces the genuine ORIGINAL full 25×25 rational source-window positive stiffness proxy \(P_\mathcal W\), on exactly the original SM43A **16 selected source-centered physical frequency windows** (union measure \(1029/64\)), preserving all source cross and original zero-extended 16 sin, 8 \(x\cos\), and 1 genuine sinh odd pole. Its first exact-rational CI passed. But with maximum mesh \(1/8\), the **complete scalar Loewner error** was \(1314.453227809\,I_{25}\), comprising the original positive signed multiplier uncertainty \(45.610847484\,I_{25}\) and the **physical Fourier-cell integration error** \(1268.842380325\,I_{25}\). The original rational proxy diagonal scale was approximately 0.356–4.654; thus the mathematically valid source stiffness enclosure was useless for a positive inverse.

SM44 paid the worst-case global physical Fourier derivative \(L_j=2\pi\int |xg_j(x)|dx\) uniformly, including where the true supported Fourier transforms nearly vanish or vary slowly. SM45 corrects that overpricing **without changing the rational matrix proxy or the underlying operator**.

## Exact genuine original frequency-local derivative formulas

For the original physically supported odd \(g\), take
\[
T_g(\xi)=\int_{-B}^Bg(x)\sin(2\pi\xi x)dx,\quad B=11/10.
\]
SM42 already certifies the rational-interval elementary physical Fourier integrals
\[
F_1(q)=\int_{-B}^Bx\sin(2\pi qx)dx,\quad
F_2(q)=\int_{-B}^Bx^2\cos(2\pi qx)dx.
\]
The exact *original* source-frequency derivatives at any rational midpoint \(\xi_I\) are
\[
\begin{aligned}
T'_{\sin(2\pi cx)}(\xi_I)
 &=\pi\big(F_1(c-\xi_I)+F_1(c+\xi_I)\big),\\
T'_{x\cos(2\pi cx)}(\xi_I)
 &=\pi\big(F_2(c+\xi_I)+F_2(\xi_I-c)\big),\\
T'_{\sinh(x/2)}(\xi_I)
 &=2\pi\,\operatorname{pole}_{x\cos}(\xi_I),
\end{aligned}
\]
where the last term is the exact physically supported \(\int x\sinh(x/2)\cos(2\pi\xi x)dx\) from SM42. Every trig, \(\pi\), and hyperbolic quantity is enclosed in **original SI06/SM42 exact rational intervals**, never by finite differences or an FFT. All 25 genuine source derivative values receive complete rigorous interval upper bounds \(D_{j,I}\ge|T'_j(\xi_I)|\).

For the same original entire real frequency domain, we independently pay the true **second derivative** physical-moment ceiling:
\[
|T_g''(\xi)|\le(2\pi_{\rm up})^2\int_{-B}^B x^2|g(x)|dx.
\]
Specifically, the 16 original sine directions and actual \(\sinh(x/2)\) pole use \(K_j=(2\pi_{\rm up})^2\,2B^3/3\), and the eight original \(x\cos\) directions use \(K_j=(2\pi_{\rm up})^2 B^4/2\). Nothing about an approximate frequency window or source “orthogonality” is assumed.

For every **actual real** \(\xi\) in the original rational cell \(I=[a,b]\), \(h=b-a\), midpoint \(\xi_I\), these yield the rigorous local Taylor bound
\[
\boxed{
|T_j(\xi)-v_{j,I}|
\le r_{j,I}+\min\left\{
L_jh/2,\ D_{j,I}h/2+K_jh^2/8
\right\}.
}
\]
Here \(v_{j,I}\in\mathbb Q\) is the **same exact SM44 rational Fourier midpoint** and \(r_{j,I}\) pays its rational sine/cosine interval uncertainty. The second bound has a mathematically unavoidable curvature term; an independent exact rational quadratic \(f(x)=dx+Kx^2/2\) saturates \(d h/2+Kh^2/8\) on the midpoint-to-edge interval.

Both the global source derivative and midpoint-local source derivative/curvature costs are **independently valid** on every real frequency; their **minimum** preserves validity and cannot increase any source cell error. For each original frequency cell, recalculate the original SM44 source-coupled
\[
E_I=\sum_j e_{j,I}^2,\quad S_I=\sum_j s_{j,I}^2,
\qquad \epsilon_{\rm Fourier,I}=2J_I(2\sqrt{E_IS_I}+E_I)
+2|J_I-\widetilde J_I|\sum_jv_{j,I}^2,
\]
with rigorously upward-rounded rational square roots. Every source offdiagonal remains included by full rank-one matrix Cauchy, not a componentwise positivity argument.

## Full 25×25 exact rational **same-matrix** regression

For **both** maximum widths \(h=1/4\) (65 original cells) and \(h=1/8\) (129 original cells), run the **SM44 global derivative mode** and **SM45 local certified derivative mode** against the SAME genuine original source frequencies/window union. Require:

1. Exact *equality of every one of the 625 rational proxy matrix entries* \(P_\mathcal W\) between SM44 and SM45 at the same mesh.
2. Exact equal original SM43A signed digamma/seven-prime positive multiplier Loewner error; no accepted physical source or multiplier modification.
3. Strictly smaller rational **physical Fourier-cell full-matrix Loewner error** and smaller combined true original positive SOURCE WINDOW source-stiffness Loewner error in SM45.
4. **At least 5% exact rational reduction** at mesh1/8; if this fails, do not promote an inconsequential improvement. Strict mesh1/4→1/8 error contraction.
5. Both chosen local and inherited global derivative alternatives remain valid with true original \(m=\kappa\) crossings and original full 25×25 physical source cross.

The resulting **exact source-window** inequality is
\[
\boxed{
-\epsilon_{45}I_{25}
\preceq A^{\rm original}_{o,\mathcal W}
-P_{\mathcal W}^{\rm SM44}
\preceq\epsilon_{45}I_{25}.
}
\]
The rational matrix itself is **identical** to SM44; only the mathematical outward error shrinks.

## Remaining genuine whole-operator acceptance

SM45 is **not** the original complete positive LOW form on \([0,4096]\) because its selected frequency union has measure \(1029/64\), strictly less than 4096. Nor does it establish the true original all-470 supported physical-source \(A_*\) pole-conditioned resolvent/strong residual or entire signed \(W_o=A_o-2|s\rangle\langle s|-K_{\neg,o}\). SM41's original positive HIGH log tail remains separate; SM40's full signed negative-frequency operator cap remains separate; SM42's exact physical 25-source Gram and pole remain separate. None of them alone supplies a complete original odd sign proof.

SM46 decision rule: inspect whether the new local physical Fourier derivative correction materially closes the source-window quadrature error. If scalar Cauchy overpricing still dominates, derive preconditioned/matrix-weighted frequency-cell error or higher-order true original source transform Taylor proxy; do **not** merely shrink the signed scalar multiplier envelope. Extend frequency coverage to all real \([0,4096]\), handle all true 470 original degree-\(k\) supported source Fourier transforms, certify actual complete original \(A_*\) inverse/strong residual and 470-dimensional \(51/56\) or corrected full Schur. Canonical odd O1/O2, even E1–E4, Weil positivity, native CC27 and RH remain **OPEN**. Independent original Fourier/closed-domain analytic audit remains required.

Replay \`python3 scripts/validate_rpb108_sm45_local_source_fourier_derivative.py\`; output JSON contains exact rational before/after full source-window Loewner fees and the **same** full 25×25 rational matrix. Mathematical source formulas are auditable independently from output and CI.


## Verified actual-original full 25-source CI and remaining acceptance

**First SM45 focused GitHub Actions run 39184177196 completed SUCCESS**, including exact TRUE original midpoint F1/F2/pole_xcos rational Fourier derivative bounds at every real original source-window cell, complete source second-derivative Taylor remainders, and strict identical **all 625 rational SM44 original source stiffness proxy matrix entries** on both frequency meshes. Original SM43A exact signed digamma-plus-all-seven-prime multiplier error is mathematically and numerically EXACTLY unchanged. The full 25×25 source cross and all true supported pole couplings remain priced.

| Mathematically certified original selected 25-source positive source-window Loewner error in raw source coordinates | Mesh1/4: 65 cells SM44 → SM45 | Mesh1/8: 129 cells SM44 → SM45 |
|---|---:|---:|
| Original SM43A original true signed multiplier interpolation fee | 179.349827 → **179.349827** | 45.610847 → **45.610847** |
| Full original physical source Fourier CELL integration fee | 4646.433685 → **806.427340** | 1268.842380 → **130.916378** |
| **Complete 25×25 source WINDOW matrix Loewner fee** | 4825.783512 → **985.777167** | 1314.453228 → **176.527225** |
| Original source-cell components strictly helped by local derivative | **1625 / 1625** | **3225 / 3225** |
| Sum of original source Fourier amplitude-cell error relative to former global derivative bound | 1 → **0.316167** | 1 → **0.168907** |
| Complete same rational source stiffness matrix | **exact entrywise identical** | **exact entrywise identical** |

At mesh1/8, the exact original source physical Fourier-cell fee decreases by **89.68%** and the overall true positive source-window stiffness error by **86.57%**. This is a rigorous consequence of the valid whole-real original local derivative bounds, not a refined sampled eigenvalue or loss of cross contributions. The 5% formal gate passed by a substantial margin.

**The bottleneck has shifted again:** remaining fine source-window physical Fourier-cell integration error **130.916** is only about **2.87×** the original signed multiplier error **45.611**, versus SM44's ≈27.82×. However the combined rigorous raw-source-coordinate Loewner fee **176.527** still dwarfs the unchanged rational matrix diagonal range **0.355686–4.653812**, so it cannot yield a positive coercive bound or original true Astar inverse. The remaining feasible mathematical improvement is a **matrix/source-conditioned error bound**, improved actual source Fourier variation through linearized (not midpoint-constant) true supported transforms, and tighter original seven-prime/digamma source-weight cell envelopes. Crucially, the larger untouched deficiency is still **the rest of the original positive LOW frequency 0–4096 outside the selected windows** plus the all-470 original source resolvent and its strong residual.

**SM46 proposed acceptance:** move from the scalar \(I_{25}\) source-Cauchy allowance to an exact/interval full 25×25 PSD matrix source variation error, possibly using exact SM42 true source Gram preconditioning; insist on strict original spectral-form lowering in verified physical norm and complete original true Fourier-cell coverage, rather than optimizing a selected numerical Ritz sign. The original W-ODD-NEG O1/O2, even E1–E4, full signed Weil, CC27 and RH remain OPEN. This first scoped SM45 CI passed; any subsequent note/manifest-only source revisions require a separate final-head CI check.
