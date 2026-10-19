# MG10 — The common physical boundary jump has rank ONE

**October 19, 2026.** MG10 is an original signed-odd **positive-action high-frequency source-tail certificate**, conditional on the original Fourier/form-domain identifications; it is not the strong Galerkin residual or full W-ODD-NEG/even/Weil/CC27/RH certificate. Stacked on MG09 #258 (passing original exact-rational Actions 39337083491).

## Why MG09's remaining endpoint contribution is not a generic 25D problem

Every one of the original 25 selected physically supported SI10 odd trial generators is odd on exactly the same \([-B,B]\) support, \(B=11/10\). With the actual odd sinh pole \(s(x)=\sinh(x/2)\), the 25 source endpoint traces \(b_j=f_j(B)\) satisfy \(f_j(-B)=-b_j\).

Thus the entire leading Fourier boundary jump for any source coefficients \(z\) is the **single source-coefficient linear functional**

\[
\widehat{f_z}_{\rm jump}(\xi)=-\frac{\cos(2\pi B\xi)}{\pi i\xi}\,b^\top z,
\qquad b=(f_0(B),\ldots,f_{24}(B)).
\]

This is rank ONE in source space, not 25 independent oscillatory boundary losses. The actual pole endpoint \(b_{24}=\sinh(B/2)>0\), so the kernel \(K_{\partial}=\{z:b^\top z=0\}\) is exactly 24-dimensional. A canonical physical basis is

\[
h_i(x)=f_i(x)-\frac{f_i(B)}{\sinh(B/2)}\,s(x),
\qquad i=0,\ldots,23.
\]

Every \(h_i\) is odd and vanishes at both endpoints, hence its leading boundary jump cancels **exactly**, with no numerical approximations and no discarded pole component. These 24 generators are linearly independent as coefficient vectors; physical independence is inherited from SM42's proved original physical Gram SPD.

This structural identity also formally extends to the full original 470-dimensional odd SI10 generator family: every generator is odd, supported on the same interval, and the pole trace is nonzero. Hence the leading endpoint jump is still rank at most one, with a 469-dimensional exact boundary-trace kernel. **MG10 certifies a numerical error matrix only for the selected original 25**; derivative majorants and complete 470 source/Schur residuals are not constructed.

## Entire original 25-source strong tail, now with the endpoint jump explicitly paid

SM41 rigorously proves the original positive multiplier \(a_o(\xi)=\max(\kappa,m(\xi))\le 17+\ln|\xi|\) on \(|\xi|\ge1\) conditional on the signed Fourier/domain premise. MG09 certifies the full source-vector peeled remainder action using true original SI10 source derivative majorants \(D_j\), with

\[
\left\|a_o\sum_{j=0}^{24}z_j E_j\right\|^2_{|\xi|>\Lambda}
\le C_E(\Lambda)\|z\|^2,\quad
C_E(\Lambda)=\frac{2\sum D_j^2}{6^4\Lambda^3}
\left[\frac{v^2}{3}+\frac{2v}{9}+\frac2{27}\right],
\quad v=17+k\frac{347}{500},\;\Lambda=2^k.
\]

The leading rank-one jump is **separately** integrated. Since \(a_o^2\le(17+\ln\xi)^2\), \(\cos^2\ge0\), and \(w(\xi)=(17+\ln\xi)^2/\xi^2\) is positive and strictly decreasing for \(\xi\ge\Lambda\ge2048\),

\[
\begin{split}
\|a_o\widehat{f_z}_{\rm jump}\|^2_{|\xi|>\Lambda}
&\le \frac{2}{\pi^2}(b^\top z)^2
\int_\Lambda^\infty w(\xi)\cos^2(2\pi B\xi)\,d\xi\\
&=\frac{(b^\top z)^2}{\pi^2}
\left(\int_\Lambda^\infty w(\xi)\,d\xi
+\int_\Lambda^\infty w(\xi)\cos(4\pi B\xi)\,d\xi\right).
\end{split}
\]

An exact integration by parts on the monotone \(w\) yields

\[
\left|\int_\Lambda^\infty w(\xi)\cos(4\pi B\xi)\,d\xi\right|
\le \frac{2w(\Lambda)}{4\pi B}
=\frac{w(\Lambda)}{2\pi B}.
\]

Using \(\pi>3\), the exactly enclosed original jump satisfies

\[
\boxed{\|a_o\widehat{f_z}_{\rm jump}\|^2_{|\xi|>\Lambda}
\le \mu(\Lambda)(b^\top z)^2},
\]

where

\[
\mu(\Lambda)=\frac19
\left(\frac{v^2+2v+2}{\Lambda}
+\frac{v^2}{6B\Lambda^2}\right).
\]

The factor approaches one-half of the naive nonoscillatory cosine-squared cap, but **the underlying signed multiplier remains present through its rigorous pointwise majorant**; no false sinusoidal averaging of the multiplier is asserted.

For the exact source endpoint \(b\), full source-vector Young inequality gives \(Q_{\rm tail}\preceq(1+t)\mu\,bb^\top+(1+t^{-1})C_E I_{25}\). SM42 already provides **exact-rational outward intervals** for every actual endpoint sine/cos phase and the odd sinh pole. Write the true endpoint \(b=b_0+\delta\), with midpoint rational \(b_0\) and exact coordinate radius-square sum \(e^2\). Then for rational \(t>0,\eta>0\),

\[
\boxed{
Q_{\rm tail}\preceq
(1+t)(1+\eta)\mu\,b_0b_0^\top
+\left[(1+t)(1+\eta^{-1})\mu e^2+
(1+t^{-1})C_E\right]I_{25}.
}
\]

MG10 uses \(t=1/2\), \(\eta=1/64\). This is a **complete original 25-source Loewner high-frequency strong-action bound**, paying every mixed source through a rank-one full matrix plus a strictly positive rational diagonal fee. It is a valid whole-tail bound even for non-boundary-vanishing sources.

## Even faster complete high-frequency bound on the true boundary kernel

On the exact original physical basis \(h_i=f_i-(b_i/b_{24})s\), the leading jump cancels, leaving only the entire actual remainder \(E_i-(b_i/b_{24})E_{24}\). SM42's exact pole lower \(b_{24,\mathrm{lo}}>0\) and endpoint intervals give rational ratios \(a_i\ge|b_i/b_{24}|\). Hence set \(D'_i=D_i+a_iD_{24}\) and \(D'^2=\sum_{i=0}^{23}(D'_i)^2\). The **entire** high-frequency positive-operator strong action on the 24 boundary-vanishing physical directions satisfies

\[
Q_{\rm tail}|_{K_\partial}\preceq
\frac{2D'^2}{6^4\Lambda^3}
\left(\frac{v^2}{3}+\frac{2v}{9}+\frac2{27}\right)I_{24}
\]

in the explicitly described transformed coefficient basis. Unlike MG09's remainder-only estimate on arbitrary directions, **there is no unpaid jump term in this 24-dimensional space**.

No assertion that the transformed physical Gram is the identity, or that the original 470-source strong residual is small, is made. The boundary-coordinate transform can be poorly conditioned; any future original 470-dimensional certificate must account for its complete physical Gram and pole effects.

## Verification, scope and next gate

Replay original 107 rational SI10 cluster centers and select genuine 16 sine / eight xcos / one sinh pilot source; recompute all endpoint intervals using SM42's exact rational sine/cos Taylor interval and pole sinh enclosure. Confirm nonzero pole trace, exact rank-one/24-kernel dimension, 25-source complete jump and remainder Loewner upper at 11 dyadic cutoffs, and compare full-source scalar bound to previously passing SM41. The analytic high-tail assertions remain conditional on inherited signed original Fourier/form-domain lemmas.

**Next remaining acceptance** is no longer the generic boundary jump tail for the 25 selected sources. It is a certified **low-frequency original strong positive \(A_*\) action**, complete Galerkin residual and original negative cap in the boundary-adapted basis, then extension with actual rigorous high-degree bounds to all 470 sources, plus even/Weil transfer. Original odd/even/Weil/CC27/RH remain OPEN.
