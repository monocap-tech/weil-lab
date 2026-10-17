# PS07 — Exact original signed IMS localization: compact arch correction and irreducible prime translations

**Lane:** W-PHYSICAL-SHIFT, scoped parallel investigation; stacked after PS06. **Canonical W-ODD-NEG remains OPEN**. This advances from PS06's graph-stable *additive* split to an exact **quadratic** partition-of-unity identity for the **same original seven-prime signed Weil form**. The remainder is an explicitly bounded physical operator with an analytically identified compact part, seven signed shift parts and original finite-rank pole parts. Its prime shift is not compact in raw physical L²; an energy-regularized sandwich is compact. No complete Schur PSD, whole even/odd positivity, CC27 D-Riesz domain transfer, or RH conclusion.

## 1. Actual original form, cutoff, and the quadratic partition

Set \(I=[-B,B]\), \(B=11/10\), \(\ell=\log9\), \(a=\ell-B\), \(\delta=2B-\ell\). Let \(\chi\) be the precise **real even Lipschitz edge cutoff of PS06**, zero for \(|x|\le a+\delta/4\), one for \(|x|\ge a+3\delta/4\) and linear on the transition collars. Define
\[
\vartheta(x)=\frac{\pi}{2}\chi(x),\quad
\alpha(x)=\sin\vartheta(x),\quad
\beta(x)=\cos\vartheta(x).
\]
Then
\[
\alpha^2+\beta^2=1,\quad
\alpha=0\text{ on the central core},\quad
\alpha=1\text{ on the outer edge strips},\quad
\beta=1\text{ on the core}.
\]
Both are globally Lipschitz and bounded between 0 and 1. Their Lipschitz bound is \(A=\pi/\delta<2048\). PS06's original-form energy multiplier argument extends to them. On the original physical logarithmic spectral form domain \(\mathcal D\), for \(G[f]=Q[f]+20\|f\|_2^2\),
\[
\boxed{G[\alpha f]<31G[f],\qquad G[\beta f]<31G[f]\quad(f\ne0).}
\]
Here \(Q\) is **unchanged**:
\[
Q[f]=c_{\rm arch}\|f\|^2 + J[f]
 -2\sum_{n\in N}w_n\operatorname{Re}C_f(\ell_n)
 +2|\langle f,c\rangle|^2-2|\langle f,s\rangle|^2,
\]
\[
J[f]=\int_0^\infty k(u)\|Zf-\tau_uZf\|_2^2du,\quad
k(u)=\frac{e^{-u/2}}{1-e^{-2u}},\quad
N=\{2,3,4,5,7,8,9\},\quad
w_n=\frac{\Lambda(n)}{\sqrt n},\quad\ell_n=\log n.
\]
The original pole vectors remain \(c(x)=\cosh(x/2)\), \(s(x)=\sinh(x/2)\). On the actual \(I\), \(\alpha f\) lies entirely in PS03's positive edge carrier; \(\beta f\) is an admissible **overlap-compatible** inner component, not an orthogonal complement.

## 2. Exact full signed IMS identity (all seven prime terms and both poles)

For \(x,y\in I\), let
\[
\eta(x,y)=(\alpha(x)-\alpha(y))^2+(\beta(x)-\beta(y))^2
=2[1-\cos(\vartheta(x)-\vartheta(y))].
\]
It satisfies \(0\le\eta\le2\) and \(\eta(x,y)\le A^2|x-y|^2\).

Define the quadratic partition remainder
\[
R[f]:=Q[\alpha f]+Q[\beta f]-Q[f].
\]
The constant \(c_{\rm arch}\|f\|^2\) cancels **exactly** because \(\alpha^2+\beta^2=1\); the original archimedean kernel and seven prime powers yield:
\[
\boxed{\begin{aligned}
R[f]={}&
\int_0^\infty k(u)\int_{\mathbb R}
\eta(x,x+u)\operatorname{Re}(Zf(x)\overline{Zf(x+u)})\,dx\,du\\
&+\sum_{n\in N}w_n\int_{\mathbb R}
\eta(x,x+\ell_n)\operatorname{Re}(Zf(x)\overline{Zf(x+\ell_n)})\,dx\\
&+2\Big(|\langle\alpha f,c\rangle|^2+|\langle\beta f,c\rangle|^2-|\langle f,c\rangle|^2\Big)\\
&-2\Big(|\langle\alpha f,s\rangle|^2+|\langle\beta f,s\rangle|^2-|\langle f,s\rangle|^2\Big).
\end{aligned}}
\]
This identity follows by expanding each **zero-extended actual original** difference energy and signed autocorrelation. The signs are not inferred from a positive auxiliary operator. \(\eta\) is nonnegative pointwise, but the integral involves \(f(x)\overline{f(y)}\), so **neither \(R\ge0\) nor \(R\le0\) is implied**.

Unlike PS06's additive partition, this is a quadratic IMS embedding: in general \(f\neq\alpha f+\beta f\). The scalar \(L^2\) term cancels because \(\alpha^2+\beta^2=1\); no fictitious orthogonal or additive identity is used.

## 3. Rigorous bounded/compact decomposition

The arch portion of \(R\) is a symmetric Hilbert–Schmidt operator \(\mathcal R_{\rm arch}\) with integral kernel
\[
K_{\rm arch}(x,y)=\frac12 k(|x-y|)\eta(x,y)
\quad(x\ne y),\qquad K_{\rm arch}(x,x)=0.
\]
Near the diagonal \(k(u)\sim(2u)^{-1}\), while \(\eta(x,y)=O(|x-y|^2)\). Therefore \(K_{\rm arch}=O(|x-y|)\), is bounded on \(I^2\), and defines a compact Hilbert–Schmidt operator on \(L^2(I)\).

Its operator norm is explicitly bounded by Schur's integral test. Set
\[
H_A=\int_0^\infty k(u)\min(A^2u^2,2)\,du.
\]
For \(0<u\le1\), \(k(u)\le1/(2u)+1\); for \(u\ge1\), \(k(u)<2e^{-u/2}\). Splitting at \(u=1/A\) and \(u=1\),
\[
H_A<\log A+11<11+11\log2<19.
\]
Thus \(\|\mathcal R_{\rm arch}\|\le H_A<19\).

The **seven true signed prime-power** components are bounded weighted translation operators; since \(\eta\le2\),
\[
\|\mathcal R_{\rm prime}\|\le 2\sum_{n\in N}w_n<8.
\]
The actual rank-one poles yield a finite-rank remainder of rank at most six:
\[
\|\mathcal R_{\rm pole}\|\le 8\sinh B<12.
\]
Consequently the true complete signed IMS remainder has a bounded self-adjoint extension \(\mathcal R:L^2(I)\to L^2(I)\):
\[
\boxed{\|\mathcal R\|<40,\qquad |R[f]|\le40\|f\|_2^2.}
\]
This proves the **entire-original-domain localization inequality**
\[
\boxed{
Q[f]=Q[\alpha f]+Q[\beta f]-\langle f,\mathcal R f\rangle
\ge Q[\beta f]+\frac3{10}\|\alpha f\|^2-40\|f\|^2
}
\]
using PS03 on the actual edge-supported \(\alpha f\). The bound is currently far too coarse to prove global positivity; it is a mathematically valid starting gate, not a completed Schur estimate.

## 4. Exact noncompactness of the prime correction in raw L²

Let \(V=[B-\delta/8,B]\) be a tiny interval wholly in the outer mask \(\alpha=1,\beta=0\). Set \(U=V-\log2\), which is wholly in the central mask \(\alpha=0,\beta=1\). The exact original log bounds ensure that no shift \(\log n\) for \(n\in\{3,4,5,7,8,9\}\) maps any part of \(V\) into \(U\).

On \(U\times V\), the IMS factor satisfies \(\eta=2\), and the actual **only** surviving prime term is \(n=2\), with weight
\[
w_2=\frac{\log2}{\sqrt2}.
\]
Consequently, if \(P_U,P_V\) are the physical support projections,
\[
\boxed{
P_U\,\mathcal R\,P_V
=w_2 T_{\log2}+K,\quad K\text{ compact},
}
\]
where \(T_{\log2}:L^2(V)\to L^2(U)\) is the unitary partial translation, the arch part is Hilbert–Schmidt and poles are finite rank. Thus
\[
\boxed{\|\mathcal R\|_{\rm essential}\ge
\frac{\log2}{\sqrt2}>0.49.}
\]
The complete original quadratic IMS remainder is **not compact in physical L²**, even though its archimedean portion is. This identifies an explicit obstructing prime translation, rather than assigning the earlier PS04 seam obstruction to a vague kernel loss.

## 5. Full-graph compactness repairs *this* norm, not the PSD gate

The original digamma arch spectral multiplier \(J(\xi)\) satisfies PS05's rigorous lower
\[
J(\xi)\ge\log(|\xi|/2)-1/\pi-1/2,\quad |\xi|\ge2.
\]
PS06 gives \(G[f]\ge J[f]+2\|f\|^2\). Hence the full original physical graph-form energy unit ball is Fourier-tight, and finite-frequency sinc cutoffs are compact on \(L^2(I)\). Therefore the embedding \((\mathcal D,G^{1/2})\hookrightarrow L^2(I)\) is compact. If \(H\) represents the positive form \(G\), then \(H^{-1/2}\) is compact and
\[
\boxed{H^{-1/2}\mathcal R H^{-1/2}\quad\text{is compact}.}
\]
It may still have large positive or negative eigenvalues; the present theorem does **not** quantify a small Schur subtraction or certify PSD.

**Next PS08:** explicitly approximate this whole *signed* graph-conjugated IMS error (including the noncompact physical prime shifts) by a finite-rank rational/Fourier certificate and test whether its bad spectral directions can be absorbed by the known PS03 edge positivity and the remaining middle original form. A controlled CC27 D-Riesz domain transfer and full accepted Schur PSD remain mandatory.

## 6. Verification and standing

Run \`python3 scripts/validate_rpb108_ps07_ims_localization.py\`. The exact-rational validator pins RC313/315 original source identity via the PS03 and PS06 parents, certifies the physical collar masks, full original seven von Mangoldt weights, strict \(\|\mathcal R\|<40\), \((\log2)/\sqrt2>0.49\), the isolated true log2 translation geometry, full logarithmic graph growth, and canonical W-ODD-NEG custody. It is a **constant/geometry test for an analytic operator theorem**, not a full numeric eigenvalue/Schur certificate or independent peer review.
