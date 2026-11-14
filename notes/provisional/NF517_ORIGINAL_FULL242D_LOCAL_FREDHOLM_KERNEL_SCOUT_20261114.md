# NF517 — Genuine original J242 local Fredholm response and the first complete-projection physical scout

**2026-11-14 PT. Algebraic theorem plus 27 exact-Fraction finite physical controls: PASS. Three original-NF505-source-anchored conditional spectral-gap gates: EXACT RATIONAL PASS. Complete source-original 242D physical calculation: 550-decimal-digit HIGH-PRECISION NUMERICAL SCOUT ONLY, NOT SOURCE-CERTIFIED. Focused GitHub CI OPEN.** This branch stacks on NF516 draft PR #545, no main merge, no RH or Weil image/domain inference.

## Why NF516's rank-one shadow is not the missing original residual

NF516 computed the original arithmetic response minus one genuinely globally fitted selected 23-generator direction \(v\) on the real physical J8 cells \(H_{4094}\) and \(H_{4095}\). Its source-exact two-cell rank-one residual was approximately \(2.76935430766\times10^{-24}\). That is **not** the original full 242-dimensional globally fitted selected residual. NF517 restores all 242 original generator directions, using the authentic original exterior moment and Gram source instead of independently transported local selected moments.

Retain the genuine original NF407/NF406 source and NF494 H400/U400, the original fixed NF401 242-dimensional selected frame including the sinh pole, NF505 original central exterior \(O=[-549/500,549/500]\), unchanged NF404 \(\gamma^2\), and original two-collar source supported region. Put \(G_O=\int_OJJ^T>0\), \(b_O=\int_OJW\), \(a_O=G_O^{-1}b_O\), \(r_O=W-J^Ta_O\).

## New exact continuum identity, valid when trace leverage exceeds one

For an interior physical set \(D\subset O\), let \(r_D=r_O\mathbf 1_D\), \(T_D:L^2(D)\to\mathbb R^{242}\) be the selected moment operator \(T_D f=\int_DJf\), and define the exact **original selected reproducing-kernel compression**

\[
\boxed{\mathcal K_D=T_D^*G_O^{-1}T_D,\qquad
K_O(x,y)=J(x)^TG_O^{-1}J(y),\ x,y\in D.}
\]

Because the original analytic 242 selected generators remain independent on the surviving exterior \(O\setminus D\), their Gram \(G_{O\setminus D}=G_O-T_DT_D^T\) is positive definite. Consequently \(0\preceq\mathcal K_D\prec I\) in the operator sense; its 242 nonzero eigenvalues are strictly below one. The TRACE \(\tau_D=\mathrm{tr}(G_O^{-1}\int_D JJ^T)\) can be **larger than one** without violating this spectral fact.

Combining the exact NF506 support liberation identity with Woodbury,

\[
(I-\mathcal K_D)^{-1}=
I+T_D^*(G_O-T_DT_D^T)^{-1}T_D,
\]

gives the **exact original continuous refit gain**

\[
\boxed{
\mathcal R(O)-\mathcal R(O\setminus D)
=\langle r_D,(I-\mathcal K_D)^{-1}r_D\rangle_{L^2(D)}.
}
\]

Define \(\delta_D=1-\|\mathcal K_D\|_{\mathrm{op}}>0\). Then

\[
\boxed{
0\le\mathcal R(O)-\mathcal R(O\setminus D)
\le \frac{\|r_D\|_{L^2(D)}^2}{\delta_D}.
}
\]

Unlike NF508's crude sufficient trace gate requiring \(\tau_D<1\), this **exact kernel architecture continues to work at arbitrarily large trace leverage \(\tau_D\)** as long as the genuine restricted analytic complement has full rank. A second exact argument shows the kernel's nonzero spectrum is the spectrum of \(G_O^{-1/2}C_DG_O^{-1/2}\), so \(\delta_D\) can equivalently be source-certified via original selected complement generalized Gram positivity.

The committed script \(\texttt{scripts/local_replay/verify_nf517_exact_support_fredholm_woodbury.py}\) verifies the identity against full Schur source refits and the old NF506 liberation formula for **27 distinct exact rational odd-analytic finite-dimensional controls**, including cases with \(\tau_D>1\), with huge selected recentering; all pass.

## NEW original-source-specific full 242D high-precision scout — not a certificate

A separate **pure Python mpmath 550-decimal-digit** computation used the authentic original selected 242 raw generators, including sinh(x/2), and independently reconstructed full and exterior physical 242×242 analytic Grams using exact product-to-sum recurrence formulas. It reconstructed the historical *numerical* full-carrier Cholesky frame \(D=(L^T)^{-1}\), but **did not reproduce the historical exact 4096-bit dyadic frame SHA**. For the exterior global selected moment \(d_O\) and exterior frame Gram \(N_O\), it used the actual original NF505 SHA-pinned 4096-bit outward source boxes. It solved the complete 242D global exterior normal equations at 550-digit mpmath precision and reconstructed the globally fitted 242D physical response before evaluating two true local cells.

**Important independent numerical identities:** the reconstructed complete original selected projection power matched the NF505 source value \(7.4358343060326472094\times10^{-22}\) to more than 30 displayed digits; selected exterior Gram entries recomputed from the 242 raw physical generators differed from source-native entries by no more than about \(2\times10^{-253}\) on five representative entries (this is **numerical**, not an interval enclosure). The original H400/U400 physical W at local midpoint matched NF511/NF513 local source response values. Two independent local evaluation architectures were used: (i) directly squaring the complete globally fitted 242D physical residual with 24-point Gauss–Legendre on each positive cell; (ii) computing the **full 242D original projector kernel** \(K_O(x,y)\) via the exterior raw 242D Cholesky factor, and solving the small spatial Nyström matrix \(I-K\) for the full support-liberation gain. Orders 12, 18, and 24 per true mirrored cell agree closely. **No validated Gauss remainder, original 4096-bit interval Gram acceptance, or original full fitted 242D source interval error has been paid. Therefore none of the following values is promoted as SOURCE-CERTIFIED.**

| Original physical support D | 550-digit numerical \(e_D=\|r_O\|^2_D\) | Numerical full refit gain | Numerical true trace \(\tau_D\) | Numerical spectral gap \(1-\rho_D\) |
|---|---:|---:|---:|---:|
| \(H_{4094}\) | \(6.94468549743\times10^{-28}\) | \(1.49444029313\times10^{-27}\) | \(0.666913584218\) | \(0.428554922452\) |
| \(H_{4095}\) | \(6.13413743073\times10^{-28}\) | \(1.71044995354\times10^{-27}\) | \(1.656025648585\) | \(0.003339996518\) |
| \(H_{4094}\cup H_{4095}\) | \(1.30788229282\times10^{-27}\) | \(2.52634792930\times10^{-27}\) | \(2.322939232803\) | \(0.000068890324\) |

Two observations of methodological importance:
1. The **full 242-dimensional local fit is numerically ~\(2.1\times10^3\) times more effective** than NF516's globally fitted *rank-one* source response on the two-cell union: rank-one squared leftover ~\(2.769\times10^{-24}\) versus complete-242D numerical leftover ~\(1.308\times10^{-27}\). This shows quantitatively why global orthogonality cannot justify transferring the rank-one residual into the actual 242D Schur; it is **not a rigorous energy ratio** until the full projection is source-certified.
2. The actual trace \(\tau_{4095}\) numerically exceeds 1.6 and the two-cell trace exceeds 2.3. Hence NF508's \(\tau<1\) gain bound is *structurally inapplicable* to at least the second cell and their union, whereas the genuine operator gaps remain positive. NF514's certified lower leverage bounds are fully consistent with this scouting evidence.

The original source-certified NF505 lower exterior residual is \(R_{\rm lo}\approx1.5782989705548823\times10^{-22}\); unchanged \(\gamma^2\approx5.1296807867614294\times10^{-26}\). The **uncertified** full-kernel liberated gain for the two-cell union is only ~\(2.5263\times10^{-27}\). Thus the numerical experiment strongly favors **physical NO-GO** for these named additions, but **this decision is NOT certified**; a successful high-precision numerical experiment is not a proof of its own quadrature error and source matrix inversion conditioning.

## Three exact rational source-anchored *conditional* NO-GO gates

The separate committed \(\texttt{verify_nf517_original_conditional_spectral_gate_exact.py}\) SHA-pins the actual original NF505 81MB native source and proves with exact \(\texttt{Fraction}\) arithmetic that each of these **IF–THEN** gates suffices to show \(\mathcal R(O\setminus D)>\gamma^2\):

| Named original D | Required source-certified \(e_D\) upper | Required source-certified \(\delta_D\) lower | Conservatively permitted gain \(e_D/\delta_D\) |
| --- | ---: | ---: | ---: |
| \(H_{4094}\) | \(\le10^{-27}\) | \(\ge2/5\) | \(\le2.5\times10^{-27}\) |
| \(H_{4095}\) | \(\le10^{-27}\) | \(\ge1/1000\) | \(\le10^{-24}\) |
| Two-cell union | \(\le3\times10^{-27}\) | \(\ge1/20000\) | \(\le6\times10^{-23}\) |

All three exact implication checks PASS against the unchanged original NF404 gamma and source-certified NF505 \(R_{\rm lo}\). All six required **actual** original local interval bounds are **still unverified**. They have been deliberately chosen looser than the 550-digit source-candidate values to leave room for rigorous interval error payment. The strongest two-cell gate would leave source lower residual \(R_{\rm lo}-6\times10^{-23}>9.78\times10^{-23}\gg\gamma^2\), once validated.

## Standing and NF518 acceptance target

- **Exact continuum source geometry/Fredholm support identity:** ESTABLISHED (mathematical proof; 27 independent exact rational controls PASS).
- **Original NF505 SHA source anchor and three spectral/e upper conditional gates:** exact \(\texttt{Fraction}\) PASS.
- **Original full 242D physical H4094/H4095 globally fitted local source/correlation scout:** NUMERICAL ONLY; independent sample Gram/projection and order convergence PASS as numerical consistency checks.
- **True source 4096-bit Arb interval globally fitted local \(e_D\), true \(\delta_D\), rigorous quadrature/analytic remainder:** OPEN.
- **Unconditional physical H4094/H4095 NF404 no-go:** OPEN, despite strong numerical indications.
- **Weil multiplier image/source domain, W-ODD-NEG, full original even/odd signed form, RH:** OPEN.

**Next NF518:** Do not expand to new physical cells or select new finite witness directions. Reconstruct the exact historical 4096-bit NF401 dyadic D-frame SHA and original full exterior selected source inverse with rigor; source-enclose the **complete** locally contracted \(r_O(x)\), then certify \(e_{4094}\le10^{-27}\), \(e_{4095}\le10^{-27}\), and \(e_\mathrm{union}\le3\times10^{-27}\). Independently certify the original \(\mathcal K_D\) spectral gap, especially \(\delta_\mathrm{union}\ge1/20000\), using original source interval Gram or verified local kernel polynomial/quadrature envelopes. Accept an unconditional named physical NF404 support NO-GO **only when both independent source bounds and the exact conditional gate pass**, then keep Weil-domain/RH status OPEN. If exact dyadic source transport remains an information/condition limit, precisely record the failing source error fee and stop, rather than promoting the mpmath scout.
