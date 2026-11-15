# NF520 — The complete original J242 Fredholm spectral gap: three named physical panels SOURCE-EXACT

**November 14, 2026 PT. LOCAL SOURCE-EXACT PASS on ALL THREE complete 242-dimensional original Fredholm gaps, with an independent exact Fraction receipt/custody audit PASS. Dedicated GitHub CI still OPEN, no merge to main.** This increment follows NF519 draft PR #548 and preserves the original NF407/NF406 response, NF505 original 4096-bit physical source and original historical 242 selected generators. It does **not** certify the original globally fitted local squared residual \(e_H\), any unconditional NF404 physical NO-GO, Weil multiplier image/domain, W-ODD-NEG, even/odd Weil sign, or RH.

## What NF520 closes

NF517 proved the exact support-refit Fredholm identity for the complete original selected-space source response:

\[
\mathcal R(O)-\mathcal R(O\setminus H)
=\langle r_H,(I-\mathcal K_H)^{-1}r_H\rangle,\quad
\mathcal K_H(x,y)=J(x)^TG_O^{-1}J(y).
\]

The source-accurate 550-digit NF517 numerical scout suggested actual kernel gaps approximately \(0.42855\), \(0.00334\), \(0.00006889\) for original \(H_{4094}\), \(H_{4095}\), and their union, but **did not prove any gap**.

NF519 showed the original kernel gap is frame-independent. For a proposed strict lower \(g\), with \(G_O=\int_OJJ^\top\), \(C_H=\int_HJJ^\top\), and \(G_{O\setminus H}=G_O-C_H\),

\[
\boxed{\delta_H>g\quad\Longleftrightarrow\quad
G_{O\setminus H}-gG_O\succ0,}
\]

where \(\delta_H=1-\|\mathcal K_H\|_\mathrm{op}\). This is a basis-invariant generalized positive-definiteness test and does not require recovering the historical 4096-bit dyadic selected frame \(D\).

**NF520 NOW RIGOROUSLY CERTIFIES ALL THREE such source-specific positive matrices:**

\[
\boxed{\delta_{4094}>\frac25=0.4,\quad
\delta_{4095}>\frac1{1000}=0.001,\quad
\delta_{4094\cup4095}>\frac1{20000}=0.00005.}
\]

The inequalities concern the **actual original 242-dimensional selected subspace**, including the genuine sinh(x/2) pole and all 241 archived original sin/cos-polynomial generators. No rank reduction, synthetic source, or extrapolation from the 23D NF514 witness is involved.

## Exact physical geometry and source Grams

Pin the immutable original NF505 81MB raw native source SHA256:

\`ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec\`.

Original NF407 source SHA256 \`0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce\`; original NF406 seam SHA256 \`c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675\`.

Set

\[
O=[-B_O,B_O],\quad B_O=\frac{549}{500},\qquad
h=\frac{B_O}{4096},
\quad b_0=B_O,\quad b_1=B_O-h,\quad b_2=B_O-2h.
\]

For the **actual original physical** \(j_i(x)\) in the source-certified NF505 order, form three entire **242×242 original raw physical Gram matrices**

\[
G_k=\int_{-b_k}^{b_k}J(x)J(x)^\top dx,\qquad k=0,1,2.
\]

On the original named reflected panels the kernel gap inequalities reduce to positive definiteness of the following *raw physical* symmetric matrices, not to the historical D-frame:

\[
\boxed{
\begin{aligned}
M_{4094}&=\frac35G_0-G_1+G_2,\\
M_{4095}&=G_1-\frac1{1000}G_0,\\
M_{\cup}&=G_2-\frac1{20000}G_0.
\end{aligned}
}
\]

These follow from the original true physical cell removal \(H_{4094}\) (an interior two-lobe patch), \(H_{4095}\) (the outermost two lobes) and their union. A single original n=9-active branch is not extended into the next inward seam-crossing \(H_{4093}\).

## Rigorously outward source-native Gram oracle

The exact-interval generator \`scripts/local_replay/nf520_original_raw_gram_exact.py\` reads the **actual source SHA-pinned NF505 selected basis node list**. No floating point is used to construct the source physical Gram.

It uses the exact rational physical nodes, a rigorous 350-term Machin arctan enclosure of \(\pi=16\arctan(1/5)-4\arctan(1/239)\), and reduces every argument \(2\pi fb\) *by exact rational multiples of \(2\pi\)* to a phase of magnitude at most \(\pi\), even for the highest original selected \(f=113013/128\). It computes every \(\sin,\cos\) value with integer-directed Taylor recursion to 160 terms, paying phase, rounding and analytic tails using fixed denominator \(10^{420}\). The exponential source of the authentic sinh pole uses 300-term outward Taylor values, exact hyperbolic endpoints and exact complex-recurrence moments through source order 13.

All source trigonometric product-to-sum moments are integrated analytically to total monomial degree 26. The authentic selected \(\sinh(x/2)\) pole and its 241 full cross terms use the direct complex-exponential moment recurrence; no surrogate pole or numerical spatial quadrature enters the source matrix.

Every interval operation is outward rounded using integer floors/ceilings at denominator \(10^{420}\). The maximum actual raw Gram-entry interval width on any of the three endpoints is approximately \(10^{-403}\); the logged exact widths are in the source SHA custody record. Independent high-precision direct numerical integration of selected full-carrier raw generator pairs and pole crosses agrees, but **is not used for certification**.

## Untrusted numerical preconditioners; exact integer acceptance

For each of the three symmetric source interval matrices \(M\), a 300-decimal-digit mpmath Cholesky and inverse triangular factor merely propose a rational triangular \(T\), with every entry quantized to an exact integer divided by \(10^{200}\). That **numerical Cholesky does not certify positivity** and is never used in an acceptance comparison.

Let \(M_*\) be the midpoint integer matrix of the fully outward-enclosed original source \(M\), with fixed scale \(S=10^{420}\). All original Gram uncertainty is retained as \(|M_{ij}-(M_*)_{ij}/S|\le\epsilon/S\). For each proposed exact integer \(T_*\), scale \(Q=10^{200}\), the final verifier uses *two independent exact 242×242 integer matrix multiplications* to compute

\[
Z=\frac{T_*^\top M_* T_*}{S Q^2}.
\]

The **entire source interval perturbation**, including all 242 rows and every preconditioner coefficient, is paid by

\[
\|\Delta Z\|_\infty\le
\frac{\|T_*^\top\|_\infty\,(242\,\epsilon)\,\|T_*\|_\infty}{SQ^2}.
\]

The rigorous integer inequality

\[
\boxed{\|Z-I\|_\infty+\|\Delta Z\|_\infty<1}
\]

makes the exact source matrix \(T^\top M T\succ0\) by Gershgorin. Since this positive matrix is nonsingular, \(T\) itself is necessarily invertible, and hence \(M\succ0\). This is a complete proof independent of the mpmath candidate's own numerical accuracy or displayed eigenvalues.

**All three source-true matrices passed:**

| Original physical panel | Strict certified gap | Exact Gershgorin center row deficit (display) | Rigorous source-interval perturbation (display) |
| --- | ---: | ---: | ---: |
| \(H_{4094}\) | \(>2/5\) | \(0.00157897926828145\) | \(4.33805\times10^{-102}\) |
| \(H_{4095}\) | \(>1/1000\) | \(0.000130238995461803\) | \(1.04626\times10^{-102}\) |
| \(H_{4094}\cup H_{4095}\) | \(>1/20000\) | \(0.000447779387050551\) | \(1.61028\times10^{-102}\) |

Each sum is *strictly* below \(0.002\), well under the required 1. Displayed decimals are not the acceptance inputs; exact integers and rational fractions prove the inequalities. Unlike the aborted naïve direct raw interval LDL method (which became indeterminate at pivot 75 because it discarded matrix correlations), these source-preserving congruence tests remain decision-quality for **all 242 original directions**.

## Independent audit and custody

A separate local exact Fraction auditor checks the actual original NF505 SHA, historic D-frame identity **without needing its serialized coefficients**, true 3-endpoint geometry, SHA of each complete source Gram file, SHA of each untrusted exact integer candidate, positive exact Gershgorin margins, original \(R_{\rm lo}\) and unchanged NF404 \(\gamma^2\). It separately re-verifies the NF517 conditional implication with *now certified* spectral gaps and **still unverified** local energy inputs. The independent auditor does not re-integrate 242×242 source Gram entries a second time.

Actual locally verified digest custody:

- Complete 3-endpoint original Gram custody JSON SHA256 \`80e19a74955e4a994aaac9fc08fbb32f344ddb48845eba758fb9def891a2b5b4\`.
- \(H_{4094}\) exact-integer gap receipt SHA256 \`6d42ab98423e6cf79f49d530cc15ea5af32d32806ea8c0415dbfe4c04862b47a\`.
- \(H_{4095}\) receipt SHA256 \`80b9baa0027459a6ca2b3016c366596ea694dfc8cd6d8a9c2ea97ea4e8988688\`.
- Union receipt SHA256 \`223c35b7c54041500f3e2a7ee37d8b32b361c42f239f7387b674c5a073806299\`.
- Independent Fraction audit SHA256 \`b1ab7e1aabed0aed880ff49ce20871517d5d0da3c1359be63dca901d6c7d1000\`.
- Complete 16-file source proof ZIP SHA256 \`68d85bcdbee50627414a6423d41c6f063950125f87ce3c8472d51a279e5c2932\`.

The source verification package contains all exact source scripts, all three complete 242×242 Gram interval arrays, the three proposed integer preconditioners, all original exact acceptance receipts, independent audit, and README. The big NF505 original 81MB input is not duplicated; its SHA and original successful GitHub Actions artifact remain pinned. Generated Gram/seed files are pickled deterministic local outputs and should not be unpickled from untrusted sources.

**This is source-EXACT local PASS, not dedicated GitHub CI acceptance.** No CI run completion or main merge is asserted.

## Consequence for NF517 and the remaining open problem

NF517's three original conditional support NO-GO gates were:

\[
\begin{array}{c|cc}
H&\text{required genuine upper }e_H&\text{required }\delta_H\\\hline
H_{4094}&10^{-27}&2/5\\
H_{4095}&10^{-27}&1/1000\\
H_{4094}\cup H_{4095}&3\times10^{-27}&1/20000
\end{array}
\]

**NF520 has now source-certified ALL THREE spectral inputs.** The only missing inputs for these particular exact rational Fredholm gates are the source-rigorous local globally fitted squared residuals \(e_{4094}, e_{4095},e_{\cup}\). NF517's strong 550-digit scouts \(6.9447\times10^{-28}\), \(6.1341\times10^{-28}\), \(1.3079\times10^{-27}\) are still **UNVERIFIED numerical candidates**, and cannot supply those actual energy inputs.

The original NF518 complete historical D-frame Galerkin coefficient posterior \(<2\times10^{-84}\) and NF519 conditional raw beta physical transfer fee \(<4\times10^{-30}\) remain available but have NOT been converted into a genuine certified physical source residual evaluation.

**NF520 DOES NOT settle a named NF404 physical patch, the source multiplier image/graph domain, W-ODD-NEG, full even/odd Weil positivity, or RH.**

### NF521 next

Stop recomputing gap matrices or scouting new physical cells. The three original 242D Fredholm gaps are settled within the rigorous source-local scope. Recover the authentic original globally fitted **physical raw 242-vector** (NF518/NF519), with a verified weighted coefficient fee, or develop a source-certified frame-independent direct residual evaluator. On the same seam-free \(H_{4094},H_{4095}\), rigorously square the original complete W-minus-full-J242 fitted function and enclose \(e_{4094}\le10^{-27}\), \(e_{4095}\le10^{-27}\), \(e_\cup\le3\times10^{-27}\). Only after those separate source interval tests pass may the **fixed original NF404 named physical support NO-GO** be promoted via the now-certified gaps. Such a physical finite-selected result would still not prove the full Weil image/domain condition or RH.
