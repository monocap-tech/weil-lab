# MG46 — Original complete omitted-frequency source covariance with retained G/S cross moments

October 21, 2026. Stacked on independently verified [MG45 PR #294](https://github.com/monocap-tech/weil-lab/pull/294), original Actions #39544081287. MG45 showed strict original Fourier source residual cancellation improvement in all 12 measured [0,4] rational rays, yet its complete-real-frequency upper remained worse than MG44 in every case. MG32's extremely conservative complete **omitted** frequency Young bound is the relevant bottleneck.

## New complete-original missing-frequency matrix, not an invented scalar-tail reduction

Let \(\mathcal C=[-4,4]\) and \(\mathcal D=\mathbb R\setminus\mathcal C\). The same original physical SI10 25 generator catalog, MG11 23 boundary-adapted plus TRUE sinh-pole 24D source basis, and SM43 signed archimedean/seven-prime/digamma multiplier \(a_o(\xi)\) occur on ALL source frequencies. MG32's actual original 32-cell adapted Taylor source integration on \(\mathcal C\) provides exact rational Loewner \(H_{C,\mathrm{lo}}\preceq H_C\preceq H_{C,\mathrm{up}}\). The actual complete physical Gram satisfies \(H_{\mathrm{lo}}\preceq H\preceq H_{\mathrm{up}}\). Thus, without double charging the measured mass,

\[
H_{\mathcal D,\mathrm{lo}}=H_{\mathrm{lo}}-H_{C,\mathrm{up}}
\preceq H_{\mathcal D}
\preceq H_{\mathrm{up}}-H_{C,\mathrm{lo}}
=H_{\mathcal D,\mathrm{up}}.
\]

The unpoled original positive multiplier satisfies \(a_o(\xi)\ge \kappa>0\) on the complete omitted frequency set. The existing accepted MG24/SM41 cutoff-\(k\) polynomial and tail controls prove

\[
\begin{aligned}
0&\preceq G_{\mathcal D}=\int_\mathcal D a_o(\xi)\,t(\xi)t(\xi)^\mathsf T\,d\xi,\\
\kappa H_{\mathcal D,\mathrm{lo}}&\preceq G_{\mathcal D}\preceq
M_k H_{\mathcal D,\mathrm{up}}+\tau_{1,k}I=:U_G,\\
S_{\mathcal D}&=\int_\mathcal D a_o(\xi)^2t(\xi)t(\xi)^\mathsf T\,d\xi
\preceq M_k^2 H_{\mathcal D,\mathrm{up}}+\tau_{2,k}I=:U_S,\\
M_k&=17+(347/500)k.
\end{aligned}
\]

Both \(L_G=0\) and \(L_G=\kappa H_{\mathcal D,\mathrm{lo}}\) are independently justified lower bounds. Their validity does not require \(H_{\mathcal D,\mathrm{lo}}\) to be PSD. For either, let \(G_c=(L_G+U_G)/2\) and \(E=(U_G-L_G)/2\succeq0\).

For any **genuine original nonscalar** 24×24 rational response \(B\), retain the rank-one pole correction before squaring. With the accepted physical pole coefficient interval \(b\in[b_0\pm e_b]\), define
\[
C_0=I+2e_p b_0^\mathsf T B.
\]
The true original omitted-frequency residual is
\[
r_\mathcal D(\xi)=t(\xi)[C_0-a_o(\xi)B]+2t_p(\xi)(\delta b^\mathsf T B).
\]
If \(b\) had zero uncertainty, the exact omitted-frequency covariance would be
\[
C_0^\mathsf T H_\mathcal D C_0
-C_0^\mathsf T G_\mathcal D B-B^\mathsf T G_\mathcal D C_0
+B^\mathsf T S_\mathcal D B.
\]
The **two original first/second moment cross terms now remain explicitly coupled**; MG32 previously paid them via independent, nested Young inequalities for the \((t C_0)\) and \((a_o t B)\) pieces.

By the original MG40 block-PSD lemma, \(-E\preceq\Delta G=G_\mathcal D-G_c\preceq E\) implies for every rational \(\eta>0\)
\[
-C_0^\mathsf T\Delta G B-B^\mathsf T\Delta G C_0
\preceq \eta C_0^\mathsf T E C_0+\eta^{-1}B^\mathsf T E B.
\]
Thus the full **genuine-original Loewner** upper before pole coefficient error is
\[
U_{\mathrm{base}}=
 C_0^\mathsf T H_{\mathcal D,\mathrm{up}}C_0
-C_0^\mathsf T G_c B-B^\mathsf T G_c C_0
+B^\mathsf T U_S B
+\eta C_0^\mathsf T E C_0+\eta^{-1}B^\mathsf T E B.
\]

### Genuine rank-one pole uncertainty, no omitted covariance unaccounted for

Let \(d_j=\sum_i(e_b)_i|B_{ij}|\), \(D=\sum_jd_j\). For the true residual uncertainty \(\delta r=2t_p\delta b^\mathsf T B\), two independently valid PSD upper matrices are
\[
W_{\mathrm{iso}}=4(H_{\mathcal D,\mathrm{up}})_{pp}\Big(\sum_jd_j^2\Big)I,\qquad
W_{\mathrm{diag}}=4(H_{\mathcal D,\mathrm{up}})_{pp}\operatorname{diag}(D\,d_j).
\]
The second bound follows from weighted Cauchy–Schwarz:
\((\sum_j d_j|z_j|)^2\le D\sum_jd_j z_j^2\). Neither matrix is asserted to Loewner-dominate the other. For every \(\gamma>0\), the true original **omitted-frequency** residual covariance obeys
\[
Q_{\mathcal D}\preceq U_{\mathrm{new},\mathcal D}
=(1+\gamma)U_{\mathrm{base}}+(1+\gamma^{-1})W.
\]

This creates a new complete **24×24 matrix** Loewner residual upper for the omitted physical spectrum, not merely a pointwise ray estimate and not an artificial fee reduction.

## Acceptance grid and independent full-source gate

MG46 tests four original fixed accepted best nonscalar \(B\) source responses from MG43 (original mesh 16/32 × cutoff 12/16), two original first-moment lower brackets, rational \(\eta,\gamma\in\{1/16,1/4,1,4\}\), and two true PSD pole error matrices: **64 valid Loewner upper candidates per original source case, 256 total**. Each is separately combined with the SAME actual original MG32 \([0,4]\) complete 24D residual covariance upper; thus all original frequencies are covered, and no band or physical mass is double counted.

The independently accepted MG32 old complete original omitted-frequency source upper remains available as a valid fallback. The grid selection criterion is the signed exact Gershgorin sufficient lower margin of the full source \(H_{\mathrm{lo}}-[U_{C}+U_{\mathcal D}]\), NOT trace-as-Loewner. The final selected full matrix is independently classified using 24 strictly positive EXACT rational LDL Schur pivots, an exact rational nonzero negative Rayleigh vector, or inconclusive. Failure of any conservative source lower certificate does NOT mean the actual original operator or physical residual is negative. Export all exact full matrices, candidate rational margins/traces, signed source Rayleigh/LDL evidence, and 12 accepted MG45 ray comparisons.

A separate verification executable independently reconstitutes all **256** source candidate matrices and all original measured/unmeasured physical matrices from pinned accepted MG24 #39378465438, MG29 #39440914565, MG32 #39459624082, MG43 #39522608989, MG44 #39542236311 and MG45 #39544081287 artifacts. It checks exact output matrix equality and every rational sign. Independent original Actions acceptance required.

MG46 does **not** establish the original source-subspace invariance, 470D strong inverse, signed odd 51/56 negative cap, independent Fourier/form/domain, complete even/Weil/CC27/RH or RH.

**CI PENDING.**
