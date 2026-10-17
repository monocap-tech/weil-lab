# PS08 — Quantitative original signed graph-Galerkin approximation: a valid but noncompetitive rank certificate

**W-PHYSICAL-SHIFT, scoped.** Stacked after PS07; **canonical W-ODD-NEG remains OPEN**. This is an original signed, non-toy, **operator-norm finite-rank approximation theorem** for the entire seven-prime IMS remainder in its native *physical graph-energy normalization*. It is NOT a computed matrix, practical finite Schur certificate, accepted spectral sign, complete CC27 D-Riesz transfer, whole-even/odd positivity, or RH.

## 1. Objects fixed to the original physically supported signed form

Let \(I=[-B,B], B=11/10\), \(R=2B=11/5\). The original seven-prime SI10/CC27 form \(q\), its complete digamma arch difference energy \(J\), and its correctly signed poles are unchanged from PS01–PS07. Fix the **actual** PS07 quadratic IMS self-adjoint physical remainder \(\mathcal R\), defined by
\[
q[\alpha f]+q[\beta f]-q[f]=\langle f,\mathcal R f\rangle,
\quad
\alpha^2+\beta^2=1,
\]
where both masks are PS07's original PS06 physical collar cutoffs.

All seven true signed prime-power translation terms, the full arch kernel and both rank-one poles enter \(\mathcal R\). PS07's rational certificate proves
\[
\boxed{\|\mathcal R\|<37}
\]
(actual conservative sum \(<36.384805\)), despite the raw physical \(L^2\) operator being noncompact due to the true \(n=2\) translation.

Let \(G[f]=q[f]+20\|f\|_2^2\) and \(H\) its positive self-adjoint operator on the full original physical logarithmic form domain \(\mathcal D=\operatorname{Dom}G\). The **full** signed seven-prime/pole rational coefficient bound from PS06 satisfies \(C_*<179/10\), hence
\[
G[f]\ge J[f]+\gamma\|f\|_2^2,\quad
\gamma=20-C_*>21/10>\frac{100}{49},
\]
and
\[
T:=H^{-1/2}:L^2(I)\to L^2(I),\qquad\|T\|<7/10 .
\]
Define the **actual compact normalized remainder**
\[
K=T\mathcal R T.
\]
The goal of this checkpoint is a *fully explicit finite-rank operator-norm residual*, not just the qualitative compactness of PS07.

## 2. Rigorous Fourier tail on the entire original physical graph form

For any \(g\in\mathcal D\), the actual original arch kernel yields the full-frequency bound (PS05/PS07):
\[
J(\xi)\ge \log(|\xi|/2)-1/\pi-1/2
\quad (|\xi|\ge2).
\]
For a cutoff \(\Lambda\ge4\), set
\[
L_\Lambda=\log(\Lambda/2)-1/\pi-1/2>0.
\]
If \(g=Tv\), then \(G[g]=\|v\|^2\), so
\[
\boxed{\|\mathbf1_{|\xi|\ge\Lambda}\widehat{ZTv}\|_2
\le L_\Lambda^{-1/2}\|v\|_2.}
\]
This is the **true original full signed physical graph norm** and not a surrogate positive Fourier cone.

## 3. Explicit finite-rank spatial Galerkin projection and error

Divide \(I\) into \(N\) equal intervals of length \(h=R/N\). Let \(P_N\) be \(L^2(I)\)'s orthogonal projection onto cellwise constant functions. Rank exactly \(N\). Choose **even** \(N\) so reflection preserves the cell partition; the projection then respects both parity sectors.

For \(g=Tv\) with \(\|v\|=1\), Fourier split \(Zg=g_{\le\Lambda}+g_{>\Lambda}\). Standard one-cell Poincaré for averages gives
\[
\|(I-P_N)g_{\le\Lambda}\|_{L^2(I)}
\le h\|g'_{\le\Lambda}\|_{L^2(I)}
\le 2\pi\Lambda h\,\|g\|_2 .
\]
Together with the high Fourier tail and \(\|g\|<\tfrac7{10}\),
\[
\boxed{\|(I-P_N)T\|
\le L_\Lambda^{-1/2}+
\frac7{10}\frac{2\pi\Lambda R}{N}.}
\]
No matrix entries, floating quadrature, sample functions or truncations of the original form have been substituted.

The **explicitly defined** (though computationally enormous) finite-rank operator
\[
K_N:=P_N\,T\mathcal RT\,P_N=P_NKP_N
\]
is self-adjoint and has rank at most \(N\). The rigorous, full signed *operator norm* residual follows directly:
\[
\boxed{\begin{aligned}
\|K-K_N\|
&\le2\|\mathcal R\|\,\|T\|\,\|(I-P_N)T\|\\
&<2\cdot37\cdot\frac7{10}
\left[L_\Lambda^{-1/2}
+\frac7{10}\frac{2\pi\Lambda R}{N}\right].
\end{aligned}}
\]
This is not a computed spectral matrix: entries \(\langle e_i,T\mathcal RT e_j\rangle\) still require actual inverse-energy solves.

## 4. Exact rational checkpoint: quantitative yes, computationally NO

Set
\[
\Lambda=2^{8192},\qquad N=2^{8206},\quad N/\Lambda=2^{14}.
\]
The rational certificate establishes using \(\log2>69/100,\ \pi>3,\ \pi<22/7\):
\[
L_\Lambda=8191\log2-\frac1\pi-\frac12
>8191\frac{69}{100}-\frac56>75^2.
\]
It follows that
\[
\begin{aligned}
\|K-K_N\|
&<2\cdot37\cdot\frac7{10}
\left[\frac1{75}
+\frac7{10}\frac{2(22/7)(11/5)}{2^{14}}\right]\\
&=\frac{443149}{614400}
<\boxed{\frac34}.
\end{aligned}
\]
**This is a mathematically explicit operator-norm finite-rank bound for the actual original signed graph-normalized IMS remainder.** All signs and original physical support survive. It is also *wildly noncompetitive*: \(2^{8206}\) degrees of freedom and unknown inverse-energy matrix entries. It is not an actionable finite signed PSD certificate. The validator represents \(N\) by an integer/exponent, **never allocates the matrix**.

A quantitative **limitation of this particular coarse proof architecture** also follows. Even with \(N\to\infty\), the displayed *sufficient residual formula* cannot certify \(<3/4\) if \(\Lambda\le2^{6000}\), because \(\log2<7/10\) gives
\[
L_\Lambda<(6000-1)\frac7{10}<4700,
\quad
\left(\frac{2\cdot37(7/10)}{3/4}\right)^2>4700.
\]
This is **NOT** a lower bound on the actual rank, spectral approximation numbers or mathematical viability of better energy-aware methods. It merely proves the uniform logarithmic-tail plus scalar-norm method has an exponential computational bottleneck under these constants.

## 5. Rigorous spectral interpretation, not a sign conclusion

Both the original complete signed form and the even IMS collar masks are reflection invariant. Therefore \(K\) commutes with parity; so does \(P_N\). In each parity sector, \(K_N\) has rank at most \(N/2=2^{8205}\).

By the norm residual, every eigenvalue of the true **compact** self-adjoint normalized remainder outside \((-3/4,3/4)\) would need to be represented by a nonzero eigenvalue of the respective finite compressed block. However **no numerical eigenvalue, inertia, accepted residual Schur matrix or positive margin is calculated**. The abstract \(\|K-K_N\|<3/4\) alone does not prove the sign of \(q\).

The next frontier, **PS09**, must replace this enormous sufficient rank by a *native edge/interior energy-adapted basis*, calculate real original signed entries (including the true inverse-energy action and prime translations), and certify a residual small relative to an actual positive spectral gap. This is required before any assertion about W-ODD-NEG, W-EVEN-FORM, the original Weil statement or RH.

## 6. Replay and custody

Run \`python3 scripts/validate_rpb108_ps08_quantitative_galerkin.py\`. It replays the source-pinned original PS07, checks the 7 true weights, both signed poles, exact original graph constants, strict rational \(\|K-K_N\|<3/4\) and the \(\Lambda\le2^{6000}\) **method-bound** obstruction. It must **not** allocate \(2^{8206}\) basis vectors or claim the absent matrix was evaluated. Canonical W-ODD-NEG and RH status remain OPEN. Analytic proof pending independent functional-analytic review and CC27 domain transfer.
