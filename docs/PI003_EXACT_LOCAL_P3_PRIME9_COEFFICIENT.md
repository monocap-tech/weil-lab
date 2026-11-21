# PI003 — Actual p=3, n=9 local trace coefficient versus original signed Weil prime term

**Research lane:** PI### Potential Interface, stacked on PI002 PR #798 / PI001 PR #793. The PI registry is issue #792. NF, IV, and CP branches are untouched.

**Status:** exact finite-place mathematical derivation from Masullo's displayed formula and IV011's original source, plus rational support preflight. NOT a Lean PASS, full trace equality, positivity, or RH/GRH.

## 1. Primary source custody

A. M. Masullo, The Music of the Primes (November 2026 manuscript):
https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf

- Theorem 12.5.1.1, equation (12.5.1.2), **printed p.519 / PDF page index 518**, displays the finite-place geometric summand
\[
G_v(\varphi)=\frac{\log q_v}{\mu_v(\mathcal O_v^\times)}
\int_{F_v^\times}^{\prime}
\frac{\varphi(g)|g|_v^{1/2}}{|1-g|_v}\,d\mu_v(g).
\]
The full geometric side includes this sum with a PLUS sign, and equals the two Mellin pole evaluations MINUS a spectral zero sum over a specified relative strip I.
- Immediately preceding equation (12.4.1.27) uses \(\varphi(g^{-1})\); the author states in the ensuing text that replacing inversion by \(\varphi(g)\) leaves the local sums unchanged. This audit uses **the final Theorem 12.5.1.1 orientation**.
- Definition A.3.2.2, **printed p.560 / PDF page index 559**, defines multiplicative Haar \(\mu_v\), with finite unit-shell volume \(|\mathrm{disc}(\mathcal O_v/\mathbb Z_p)|_p^{1/2}\). For \(\mathbb Q_3\), \(\mu_3(\mathbb Z_3^\times)=1\). Independently, the prefactor \(1/\mu_v(\mathcal O_v^\times)\) cancels any Haar unit-shell volume.
- A.3.3, **printed p.561 / PDF page index 560**, gives the norm splitting/product Haar dictionary used in PI002.
- Genuine original Weil-Lab source: IV011 PR #774, file WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean. Its definitions neutralIV011OriginalMixedPrime and neutralIV011OriginalMixed_arithmeticSplit retain both signed shifts and the full von Mangoldt coefficient. The IV011 Lean compilation is separately audited.

These are mathematical formulas in the primary documents; none constitutes independent validation of Masullo's nuclear-operator trace theorem.

## 2. Exact p-adic shell calculation

Fix \(F=\mathbb Q\), a prime p, and a smooth compact h with h(0)=0. Define the norm-only adelic test \(\varphi(g)=h(\log|g|_{\mathbb Q})\). Via the embedding of \(\mathbb Q_p^\times\) into the idele class group, its local restriction is constant on valuation shells
\[
\mathbb Q_p^\times=\coprod_{k\in\mathbb Z}p^k\mathbb Z_p^\times,\qquad |p^k u|_p=p^{-k}.
\]
Haar invariance gives \(\mu_p(p^k\mathbb Z_p^\times)=\mu_p(\mathbb Z_p^\times)\). On the three cases:

| Valuation | Ratio \(|g|_p^{1/2}/|1-g|_p\) | \(\varphi(g)\) |
|---|---|---|
| \(k=m>0\) | \(p^{-m/2}\) because \(|1-g|_p=1\) | \(h(-m\log p)\) |
| \(k=-m<0\) | \(p^{-m/2}\) because \(|1-g|_p=p^{m}\) | \(h(+m\log p)\) |
| \(k=0\) | potential singularity at g=1 | identically zero, as h(0)=0 |

Inserting these into the **actual theorem integral** and canceling the unit-shell volume yields the exact local identity
\[
\boxed{G_p(h\circ\log|\cdot|)=\log p\sum_{m\ge1}p^{-m/2}
\left[h(m\log p)+h(-m\log p)\right].}
\tag{PI003-local}
\]
Compact support of h makes the discrete shell sum finite. Since \(\Lambda(p^m)=\log p\), this matches the corresponding p-primary summand in IV011's literal
\[
P(s,t)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\left[h_{s,t}(\log n)+h_{s,t}(-\log n)\right],
\quad h_{s,t}(u)=\int_\mathbb R t(x)\overline{s(x-u)}\,dx.
\]
**This is a coefficient equality between the given source formulas, not the whole trace identity.**

## 3. An actually nonzero coefficient test, including orientation

Freeze nonnegative genuine smooth bumps in the original strict NF543 collars:
\[
s=b_{-1099/1000,1/2000},\qquad
t=b_{+1099/1000,1/2000},
\]
where \(b_{c,a}(x)=\exp(1-a^2/(a^2-(x-c)^2))\) for \(|x-c|<a\), and zero elsewhere. Physical supports are disjoint so \(h_{s,t}(0)=0\), and the resulting norm pullback meets the stated norm-one trace-test gate.

With center difference \(d=1099/500\) and combined bump radii \(1/1000\), rigorously enclosed real logarithms give
\[
0<1099/500-\log9<1/1000.
\]
Hence \(h_{s,t}(\log9)>0\) on a nonempty open overlap. All other signed prime-power shifts vanish for 2<=n<10, and log10>11/5 excludes n>=10 inside the original [-11/10,11/10] physical window.

For this ordered pair, \(h_{s,t}(-\log9)=0\). On Masullo's p=3 place, the **valuation shell k=-2** has \(|g|_3=9\), sees \(h(+\log9)\), and contributes exactly \((\log3)/3\,h_{s,t}(\log9)\). The k=+2 shell sees the negative shift and contributes zero. Thus:
\[
\boxed{
G_3(\varphi_{s,t})
=P_{\mathrm{IV011}}(s,t)
=\frac{\log3}{3}h_{s,t}(\log9)>0.
}
\tag{PI003-n9}
\]
The equality refers to the finite prime component of the ORIGINAL source and the displayed Masullo local geometric integral. There is **no extra factor two**, no unaccounted unit-volume constant, and no orientation reversal.

## 4. Full-form sign bookkeeping

Masullo's displayed claimed theorem has
\[
G_\infty(\varphi)+\sum_pG_p(\varphi)
=\mathrm{Pole}_{\mathrm{Masullo}}(\varphi)-\mathrm{Zero}_{I}(\varphi).
\]
Rearranging yields a NEGATIVE finite-prime contribution to the asserted zero sum:
\[
\mathrm{Zero}_{I}=\mathrm{Pole}_{\mathrm{Masullo}}-\sum_p G_p-G_\infty.
\]
The original signed Weil-Lab source is \(W_{\mathrm{IV011}}=\mathrm{Pole}_{\mathrm{IV011}}-P_{\mathrm{IV011}}+\mathrm{Arch}_{\mathrm{IV011}}\).

The prime terms therefore have compatible signs **after rearranging Masullo's geometric equation**. A full compatibility law is still unproved, requiring equality of the two pole conventions, \(\mathrm{Arch}_{\mathrm{IV011}}=-G_\infty\) with all Gamma, Fourier and contact terms, and a valid identification of Masullo's strip-limited zero side with the complete original zero divisor.

Crucially, Masullo's claimed trace formula has not been independently certified by checking its local coefficient.

## 5. Remaining obligations and PI004

The local p3/n9 equality is **not**:
- proof that Masullo's global trace formula is valid or that its zero multiplicities/tail equal the Weil divisor;
- resolution of the diagonal barrier \(h_{t,t}(0)=\|t\|_2^2>0\);
- an operator-domain isometry or the corresponding Alpöge arithmetic construction;
- any new Lean theorem or general support-extension positivity.

**PI004 next:** calculate the author's real-place principal-value trace distribution directly on norm-only tests and match it, with sign, to the exact original IV011 signed Gamma/digamma Fourier term. Audit the pole terms and possible contact/delta contribution at h(0). If the normalizations differ, retain the explicit discrepancy as a genuine obstruction; do not quietly redefine the original Weil source.

**Independent preflight:** scripts/pi003_local_p3_n9_coefficient_preflight.py; exact rational logarithm enclosures, shell-volume cancellation and signed-translation checks only.