# NF508 — Original 242D exterior residual: selected leverage and aggregate local-patch exclusion

**2026-11-14 PT. Original-source-artifact exact-rational LOCAL PASS; independent focused GitHub acceptance OPEN.** Stacked on NF507 PR #536, no main merge. This is a new *aggregate* source-specific support-geometry no-go, not a localized source profile or any Weil/RH theorem.

## Fixed original source and geometric question

Retain genuine original NF407/NF406 source, NF401 selected 242D analytic basis including sinh pole, NF404 fixed dyadic centering and exact \(\gamma^2\), NF505 full source-original physical Schur, and historical complete NF494 H400/U400 physical J8 response. Set \(I=[-11/10,11/10]\), old physical support \(S_0=\{549/500<|x|<11/10\}\), old exterior \(O=[-549/500,549/500]\). Let \(J(x)\in\mathbb R^{242}\), \(G=\int_O JJ^T>0\), \(a=G^{-1}\int_O JW\), and \(r=W-J^Ta\). The **original actual complete physical residual** obeys the source-outward NF505 interval

\[
R_{\rm lo}=1.5782989705548823\ldots\times10^{-22}
\le \mathcal R(O)=\int_O r^2 \le
R_{\rm hi}=1.6059616072170955\ldots\times10^{-22},
\]

while the unchanged NF404 sufficient gate requires the new physical support-saturated residual to be \(<\gamma^2\), \(\gamma^2=5.1296807867614294\ldots\times10^{-26}\). These are exact rational source-artifact enclosures, not newly reintegrated interior values.

Partition the actual \(O\) into \(m=4096\) true symmetric mirror-pair physical cells
\[
H_j=[jh,(j+1)h]\cup[-(j+1)h,-jh],
\quad h=\frac{549}{500\cdot4096},\quad 0\le j<4096.
\]
Each pair has total length \(549/1024000\). Investigate support \(S_0\cup H_j\), which adds only one tiny interior mirrored pair to the two original terminal collars, **not** the nearly whole-carrier support of NF507's existential feasible construction.

## New local no-go lemma: original residual energy + selected leverage

For *any* measurable \(D\subset O\), put
\[
e_D=\int_D r^2,\quad C_D=\int_D JJ^T,\quad
\tau_D=\mathrm{tr}(G^{-1}C_D),\quad k_D=\int_D Jr.
\]
All quantities are genuine physical observables. The NF506 exact support-liberation identity is
\[
\mathcal R(O)-\mathcal R(O\setminus D)
=e_D+k_D^T(G-C_D)^{-1}k_D.
\]

The matrix Cauchy inequality \(k_Dk_D^T\preceq e_D C_D\) holds. Let \(U=G^{-1/2}C_DG^{-1/2}\succeq0\), so \(\lambda_{\max}(U)\le\mathrm{tr}(U)=\tau_D\). For \(\tau_D<1\), \(G-C_D>0\) and
\[
k_D^T(G-C_D)^{-1}k_D
\le e_D\,\mathrm{tr}((I-U)^{-1}U)
\le e_D\frac{\tau_D}{1-\tau_D}.
\]
Therefore the **exact, rigorous localized gain bound** is
\[
\boxed{
0\le \mathcal R(O)-\mathcal R(O\setminus D)
\le \frac{e_D}{1-\tau_D}\qquad(\tau_D<1).
}
\]
This directly handles the full 242-dimensional optimal **refit after adding support**, not merely an unreoptimized residual truncation. A candidate with \(\tau_D\le\theta<1\) and \(e_D<(1-\theta)(R_{\rm lo}-\gamma^2)\) necessarily leaves \(\mathcal R(O\setminus D)>\gamma^2\) and thus *fails* the unchanged fixed NF404 sufficient certificate.

## New original-source aggregate numerical certificate

Although no individual true-cell \(e_j\) or \(\tau_j\) has been integrated, their total budgets are **exact**:
\[
\sum_{j=0}^{4095}e_j=\mathcal R(O)\le R_{\rm hi},\qquad
\sum_{j=0}^{4095}\tau_j
=\mathrm{tr}\bigl(G^{-1}\int_O JJ^T\bigr)=242.
\]

Choose \(\theta=27/29\). The exact outward source comparison gives

\[
\Delta=R_{\rm lo}-\gamma^2>0,\qquad
e_*=(1-\theta)\Delta=\frac{2}{29}\Delta
\approx1.0881282775697973\times10^{-23}.
\]

If adding only \(H_j\) could attain \(\mathcal R(O\setminus H_j)<\gamma^2\), then necessarily **either** \(\tau_j\ge27/29\) **or** \(e_j\ge e_*\). The exact source bounds imply
\[
\#\{j:\tau_j\ge27/29\}\le
\left\lfloor\frac{242}{27/29}\right\rfloor=259,
\]
\[
\#\{j:e_j\ge e_*\}\le
\left\lfloor\frac{R_{\rm hi}}{e_*}\right\rfloor=14.
\]

Thus without knowing any identities of the exceptional cells,

\[
\boxed{
\text{At least }4096-259-14=\mathbf{3823}\text{ individual mirror-pair enlargements are strict physical NO-GOs.}
}
\]

**At most 273 individual pair locations remain unexcluded** by this particular aggregate test; not a claim that 273 are feasible. This is a real, new negative localization certificate for the *unchanged* source / projector / gamma, whereas NF507 was a positive physical existence certificate for near-whole-carrier support. There is no conflict.

## Multi-pair aggregate bound

For a uniformly sampled \(k\)-subset of the 4096 pairs, additive \(e_D,\tau_D\) have expectations at most \(k R_{\rm hi}/4096\) and exactly \(k\cdot242/4096\), respectively. Markov and the union bound imply the fraction of **all** \(k\)-pair enlargements certified to fail is at least

\[
\boxed{p_k\ge 1-
\frac{k}{4096}\left(
\frac{242}{\theta}+\frac{R_{\rm hi}}{(1-\theta)\Delta}
\right).}
\]

The exact rational source ledger certifies positive lower bounds through \(k=14\): approximately \(p_2>86.58\%\), \(p_4>73.17\%\), \(p_8>46.35\%\), and \(p_{14}>6.11\%\). At \(k=15\) this particular aggregate inequality becomes vacuous, which is a **method stop**, not evidence of feasibility.

## Verification and limitations

The new script `scripts/local_replay/verify_nf508_original_local_patch_leverage_exact.py` SHA-pins NF505 native source artifact #14004781980 and its independent NF505 exact-Fraction audit #14005655074 (workflow #43352403600), original NF407/NF406 source identities, selected dimension, and exact outward Schur/gamma rationals. All integer floors and multi-pair fractions are computed with Python Fraction; *no decimal rounding enters the acceptance decision*. The local run passed all quantitative identities and 126 nontrivial exact-rational finite-dimensional support-removal/recentering regression cells.

No individual source-native physical cell values \(e_j\), \(\tau_j\), \(k_j\) are yet computed, so the 3823 certified no-go locations remain unidentified and no cell is certified feasible. The 242² exterior physical Gram has not been independently reintegrated. Likewise no Weil multiplier/image or graph-domain realization, W-ODD-NEG, full original even/odd Weil positivity, or RH result is asserted. No new unrestricted-trigger GitHub workflow is added during the open CI fan-out/RC custody maintenance; **focused CI acceptance of NF508 remains OPEN**. No main merge.

**Next NF509:** Compute a *genuine original-source* first pass of \(\tau_j=\int_{H_j}J^TG^{-1}J\) and \(e_j=\int_{H_j}|W-J^Ta|^2\), using matched sources and outward intervals, at least for adaptive coarse cells. This identifies which of the at-most-273 numerical exceptions merit a full 242D support-augmentation Schur recomputation. Then test authentic Weil multiplier image/graph-domain eligibility before any promotion. Avoid blindly running 4096 uncoupled original integrations or pretending the aggregate count identifies cells.
