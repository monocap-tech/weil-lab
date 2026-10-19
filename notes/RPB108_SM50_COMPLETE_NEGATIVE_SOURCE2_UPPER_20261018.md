# SM50 — Entire original odd signed-negative frequency upper on the rescued source e₂

**October 18–19, 2026 · canonical W-ODD-NEG active · stacks on SM49 draft #231.**

## Exact question

SM48 established that the 17-window SM47 positive **lower** reference was too small compared with a 15-band genuine negative **lower**, without proving actual original signed negativity. SM49 repaired that particular reference shortfall by adding 32 true signed-positive source-adaptive Jensen windows, but still compared lower bounds on *both sides*.

SM50 makes the essential logical advance: obtain a bound in the **correct direction on the negative side**, starting with the genuine original physically supported odd sine source \(g_2\), the source underlying SM48's nonpole reference deficit and SM49's adaptive selection. No full 25×25 signed PSD theorem is claimed merely by resolving this source.

## Full original negative-frequency operator, not a packet subset

Original SI10/SI07/SI06 certify 973 exhaustive unresolved dyadic leaves \(I=[a,b]\) in 107 original clusters on the positive half-frequency support, inside \([0,896]\). On each original leaf, its exact rational SI10 weight \(h_I+\kappa\) dominates the true original full signed seven-prime/digamma **negative** weight

\[
r(\xi)=(\kappa-m(\xi))_+\le h_I+\kappa
\quad\text{for EVERY real }\xi\in I.
\]

On every positive frequency outside the union, \(r(\xi)=0\), including **all** \(\xi\ge896\). Both signs are accounted for by the positive-half sine-Parseval factor \(2\). These are inherited original whole-real analytic sign certificates, not sampled pointwise cutoffs.

The true supported original source \(g_2(x)=\mathbf1_{[-B,B]}(x)\sin(2\pi c_2x)\) has \(B=11/10\), original selected rational center \(c_2=1845/128\). Its sine Fourier transform is

\[
T_2(\xi)
=\int_{-B}^B g_2(x)\sin(2\pi\xi x)dx
=B\bigl[\operatorname{sinc}(2B(c_2-\xi))
-\operatorname{sinc}(2B(c_2+\xi))\bigr].
\]

The exact source-window supremum lemma inherited from SM43 proves \(|T_2(\xi)|\le s_{2,I}\) at **every real point** of each original negative-cover cell, via \(|\operatorname{sinc}u|\le\min(1,1/(\pi|u|))\). Thus

\[
\boxed{
\langle g_2,K_{\mathrm{neg},o}g_2\rangle
=2\int_0^\infty(\kappa-m(\xi))_+|T_2(\xi)|^2\,d\xi
\le2\sum_{I\in\mathrm{SI10}_{973}} (b-a)(h_I+\kappa)s_{2,I}^2
=:U_{50,2}.}
\tag{SM50-N}
\]

The sum uses **all original 973 negative-cover leaves**, unlike SM48's 15-band lower. Every rational cap is exact and at the end rounded **up** for the exported scalar certificate. This is a valid, if possibly loose, full-spectrum original odd negative **upper** on one actual physical source.

## Original positive lower and true signed pole penalty

Recompute the actual **complete low-positive [0,4096]** one-sided full 25-source original SM47 positive matrix \(P_{17}\), physical original Gram \(H_q\), and the **32** SM49 additional true signed-positive whole-real Jensen cells \(P_{32}\). Retain both previous full-matrix Loewner errors \(\epsilon_{47},\epsilon_{49}\), **not** a source-specific error masquerading as a full operator bound:

\[
L^{\mathrm{full25}}_{+,2}
=\kappa(H_q)_{22}+(P_{17})_{22}+(P_{32})_{22}
-\epsilon_{47}-\epsilon_{49}.
\]

This is a certified lower for the original \(\langle g_2,A_o g_2\rangle\) because the original positive frequency tail outside 4096 remains **nonnegative**, not silently approximated.

Original SM42's true full 25×25 physical interval Gram \(H\) contains the actual \(\sinh(x/2)\) exceptional pole cross \(p_2=\langle g_2,s\rangle=H_{2,24}\). It supplies the true **upper** pole penalty \(\Pi_2=2\max(|p_{2,\rm lo}|,|p_{2,\rm hi}|)^2\), explicitly rounded **up**. Therefore the *actual* original signed odd form on the supported source satisfies

\[
\boxed{
\langle g_2,W_og_2\rangle
\ge L^{\mathrm{full25}}_{+,2}-U_{50,2}-\Pi_2.}
\tag{SM50-S}
\]

This is the correct direction of **all three terms** for a possible genuine signed-source positivity certificate. The separately tighter directional SM49 error is reported only as an independent optional improvement, not substituted into the full-25 original Loewner statement.

## Fail-closed acceptance and limitation

The focused validator must re-run SM49 actual source selection, SM47 positive source matrix, SI10 original entire 973 negative-cover leaf theorem, SM42 full original physical Gram with pole source, and the true SM43 whole-real physical Fourier source cap on **every** negative leaf. It must export all exact outward scalar values. **A statement that actual \(\langle g_2,W_og_2\rangle>0\) is permitted only if the exact certified signed lower is strictly positive.** If the negative upper is too loose, SM50 remains a valid source2 whole-negative-operator **upper** but **no signed-source positivity** is promoted; the next task becomes refining its physical Fourier-cell integration with true original midpoint/derivative estimates, not ignoring negative windows.

Even if SM50-S is strictly positive, this would certify only one actual physical source direction; it would not imply the full 25-source signed matrix PSD, its negative index, the orthogonal complement, complete 470-source Astar/Schur inverse, even E1–E4, Weil positivity, CC27 or RH. Those canonical obligations remain **OPEN**. Independent original Fourier/closed-domain mathematical audit is separate from GitHub Actions.
