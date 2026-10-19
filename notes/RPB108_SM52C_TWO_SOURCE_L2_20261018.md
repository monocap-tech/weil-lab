# SM52C — Quantitative original signed-odd \(L^2\) coercivity on the verified 2D physical span

**October 18–19, 2026 · Added to SM53 draft PR #235 without changing canonical W-ODD-NEG.**

The original SI10 physically supported odd source pair \(g_2(x)=\mathbf1_{[-11/10,11/10]}(x)\sin(2\pi(1845/128)x)\), \(g_{17}(x)=\mathbf1_{[-11/10,11/10]}(x)\,x\cos(2\pi(1845/128)x)\) was rigorously tested in full signed-frequency detail under the inherited SI06/SM39/SM40/SM42/SM46 physical Fourier and form-domain identities. **SM52 focused CI [39205091881](https://github.com/monocap-tech/weil-lab/actions/runs/39205091881) passed**, including its compact exact rational true original 2×2 Loewner lower and the complete two-source Sylvester determinant test.

For real coefficient vector \(z\), the original signed odd form satisfies
\[
W_{\mathrm{odd}}(z_0g_2+z_1g_{17})\ge z^TLz,
\quad
L=\begin{pmatrix}
1070559452403/10^{12}&477/125000\\
477/125000&1437706842403/10^{12}
\end{pmatrix}.
\]
This matrix is the complete **outward-rounded true lower** exported by SM52, *not* a rounded midpoint of the true form; its exact rational rounding fee \(7597/10^{12}\) was already paid. The exact determinant equals \(1539136088063001900644409/10^{24}>0\). The full mixed signed and pole terms were present in SM52.

The independent 2×2 Gershgorin lower
\[
\ell=\min_i(L_{ii}-|L_{i,1-i}|)=\frac{1066743452403}{10^{12}}>0
\]
gives \(z^TLz\ge\ell\|z\|_2^2\).

**Crucial physical normalization.** The actual original source functions are zero outside \([-B,B]\), \(B=11/10\), and \(|\sin|,|\cos|\le1\), so their full physical Gram matrix \(H\) obeys
\[
H\succeq0,\qquad
\|H\|_{\mathrm{op}}\le\operatorname{tr}(H)
\le\int_{-B}^B 1\,dx+
\int_{-B}^Bx^2\,dx
=2B+\frac{2B^3}{3}=\frac{4631}{1500}.
\]
Therefore, for every real \(z\),
\[
\ell \|z\|_2^2\ge
\frac{\ell}{4631/1500}\|z_0g_2+z_1g_{17}\|_{L^2}^2,
\qquad
\frac{\ell}{4631/1500}
=\frac{3200230357209}{9262000000000}
> \frac{69}{200}.
\]

Hence the scoped original quantitative conclusion:
\[
\boxed{
W_{\mathrm{odd}}(h)\ge\frac{69}{200}\|h\|_{L^2}^2,
\qquad h\in\operatorname{span}_{\mathbb R}\{g_2,g_{17}\}.
}
\]

A standalone **exact-fraction replay script** takes the pinned complete signed two-source rational Loewner matrix from the passing SM52 original GitHub Actions artifact and checks every comparison without floating point. This is an immediate rigorous corollary of the inherited SM52 source theorem, **not** a fresh independent verification of its Fourier/domain identities. The physical source trace bound is intentionally conservative, so it cannot covertly depend on favorable approximate orthogonality.

The complete original 25 physical-source signed matrix, infinite orthogonal remainder/470-source Astar inverse and signed negative-index classification, odd O1/O2, even E1–E4, entire Weil form, CC27 and RH remain **OPEN**. SM53's genuine pole-input 3×3 test is separate and must pass on its own; success or failure there cannot be inferred from this 2D coercivity.
