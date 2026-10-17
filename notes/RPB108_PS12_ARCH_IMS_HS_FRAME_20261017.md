# PS12 — Thin-support Hilbert–Schmidt archimedean IMS bound and full signed graph-localization frame

**Lane:** W-PHYSICAL-SHIFT, scoped; stacked after PS11. **Canonical W-ODD-NEG remains OPEN.** This checkpoint supplies a rigorous **original archimedean** localization bound using the *actual measure of the two physical edge collars*, then combines it with PS10's sharp seven-prime IMS norm and PS11's correctly signed original pole bound. The resulting **entire original signed energy-normalized IMS remainder** has certified operator norm **strictly below 683/1000**. Consequently the quadratic IMS localization masks give a two-sided stable frame in the *positive shifted graph-energy norm* on the complete original physical form domain. This is NOT positivity of the unshifted Weil form, signed Schur closure, completed CC27 D-Riesz transfer or RH.

## 1. The exact original signed IMS object

On the actual physical support \(I=[-B,B]\), \(B=11/10\), let \(R=2B=11/5\), \(\ell=\log9\), \(\delta=R-\ell\), and let the PS06/PS07 edge-angle masks \(\alpha=\sin\theta,\ \beta=\cos\theta\) satisfy \(\alpha^2+\beta^2=1\), \(\theta=(\pi/2)\chi\), \(\chi=0\) off the two edge strips \(E=[-B,-a]\cup[a,B]\), \(a=\ell-B\). They obey
\[
A=\operatorname{Lip}(\theta)=\pi/\delta,\qquad
0<\delta<1/350,\quad 1/400<\delta,\quad A<1300.
\]
All masks preserve the actual physical logarithmic Weil form domain by PS07.

For \(f\) in that same domain, the **original complete signed seven-prime** IMS identity is
\[
Q[\alpha f]+Q[\beta f]-Q[f]
=\langle f,\mathcal R f\rangle
\]
where \(\mathcal R=\mathcal R_{\rm arch}+\mathcal R_{\rm prime}+\mathcal R_{\rm pole}\). The archimedean signed nonlocal defect is represented on \(L^2(I)\) by the self-adjoint integral operator
\[
K_{\rm arch}(x,y)=\frac12\,k(|x-y|)\,\eta(x,y)
\quad(x\ne y),\qquad
k(u)=\frac{e^{-u/2}}{1-e^{-2u}},
\]
\[
\eta(x,y)=2(1-\cos(\theta(x)-\theta(y))),\qquad
0\le\eta(x,y)\le\min(A^2|x-y|^2,\,2).
\]
The kernel is zero when **both** \(x,y\notin E\), since the angles are then zero. Its diagonal singularity is cancelled by \(\eta=O(|x-y|^2)\). PS07 showed it is Hilbert–Schmidt but used a coarse whole-space Schur bound \(<19\), without exploiting \(|E|=2\delta\).

## 2. A fully explicit original archimedean Hilbert–Schmidt bound

For **all** \(u>0\), the elementary exponential inequality \(e^{2u}\ge1+2u\) implies
\[
0<k(u)\le\frac1{2u}+1.
\]
The support property and the exact symmetric \(1/2\) kernel factor give, with \(R=11/5\),
\[
\begin{aligned}
\|\mathcal R_{\rm arch}\|_{\rm HS}^2
&=\frac14\iint_{I^2}k(|x-y|)^2\eta(x,y)^2\,dx\,dy\\
&\le |E|\int_0^R k(u)^2\min(A^2u^2,2)^2\,du\\
&=2\delta\int_0^R k(u)^2\min(A^2u^2,2)^2\,du.
\end{aligned}
\]
Split at \(u=1/A\). On the small part, use \(\min(A^2u^2,2)\le A^2u^2\); on the large part, use \(\le2\). Thus
\[
\begin{aligned}
\int_0^R k(u)^2\min(A^2u^2,2)^2du
&\le\int_0^{1/A} A^4\left(\frac{u^2}{4}+u^3+u^4\right)\,du\\
&\quad+\int_{1/A}^R\left(\frac1{u^2}+\frac4u+4\right)du\\
&<\frac{13A}{12}+\frac14+4\log(AR)+4R.
\end{aligned}
\]
Here \(\delta A=\pi\), \(AR<1300(11/5)=2860<4096=2^{12}\), and \(\delta<1/350\). Exact rational upper enclosures, using only \(\pi<22/7\) and \(\log2<7/10\), establish
\[
\begin{aligned}
\|\mathcal R_{\rm arch}\|_{\rm HS}^2
&<\frac{13\pi}{6}
+2\delta\left(\frac14+4\log(AR)+4R\right)\\
&<\frac{13}{6}\frac{22}{7}
+\frac2{350}\left(\frac14+48\frac7{10}
+\frac{44}{5}\right)
<\frac{64}{9}.
\end{aligned}
\]
Therefore the **entire original archimedean IMS remainder** satisfies the *strict operator-norm bound*
\[
\boxed{\|\mathcal R_{\rm arch}\|
\le\|\mathcal R_{\rm arch}\|_{\rm HS}<\frac83.}
\]
This improves PS07's certified arch bound \(18.6246\ldots\) by over a factor of six **without approximating the original digamma kernel**, and does not assume a finite-dimensional support subspace.

## 3. Full original seven-prime + pole + arch normalized remainder

PS10's *exact global* channel calculation gives
\[
\|\mathcal R_{\rm prime}\|=
\rho_7=\sqrt{\sum_{n\in\{2,3,4,5,7,8,9\}}
\left(\Lambda(n)/\sqrt n\right)^2}<\frac{71}{50}.
\]
PS11's two correctly signed original pole localization estimate, using the *same masks*, gives
\[
\|\mathcal R_{\rm pole}\|<\frac{549}{800}.
\]
Those three components add **as bounded operators** on the same original physical \(L^2(I)\). Thus the **complete signed** IMS error satisfies
\[
\boxed{
\|\mathcal R\|
<\frac83+\frac{71}{50}+\frac{549}{800}
=\frac{11455}{2400}<\frac{24}{5}.
}
\]
The right hand side is a valid upper bound; it is **not** a newly computed sharp operator norm or a sign bound.

PS11 proved the **complete original signed shifted graph operator**
\[
H=Q_{\rm op}+20I>7I
\]
in form order using the true positive even and negative odd pole signs. Therefore the *full* original signed energy-normalized IMS correction obeys
\[
\boxed{
\|H^{-1/2}\mathcal R H^{-1/2}\|
<\frac{11455}{16800}
<\frac{683}{1000}<\frac7{10}.
}
\]
This is **a bound on the entire original IMS error** (archimedean + all seven primes + both poles), not merely the prime-and-pole portion in PS11.

## 4. A whole-domain two-sided stable quadratic localization frame

Define the **positive graph form**
\[
G[f]=Q[f]+20\|f\|_2^2.
\]
Because \(\alpha^2+\beta^2=1\), the scalar mass cancels exactly and the signed original IMS identity also gives
\[
G[\alpha f]+G[\beta f]-G[f]=\langle f,\mathcal R f\rangle.
\]
With \(\kappa=683/1000\) and \(G[f]=\|H^{1/2}f\|_2^2\),
\[
|\langle f,\mathcal R f\rangle|
\le \|H^{-1/2}\mathcal RH^{-1/2}\|\,G[f]
<\kappa G[f].
\]
Hence **for every nonzero original physically form-admissible \(f\)**,
\[
\boxed{
\frac{317}{1000}\,G[f]
<
G[\alpha f]+G[\beta f]
<
\frac{1683}{1000}\,G[f].
}
\]
This gives a certified energy-stable **quadratic localization frame** on the *complete physical original signed form domain*. The frame is in \(G=Q+20\|\cdot\|^2\), not the unshifted \(Q\). It does **not** assert \(Q\ge0\). In particular the original signed interior form \(Q[\beta f]\), the CC27 D-Riesz transfer and a complementary signed Schur PSD remain unproved positive.

## 5. What PS12 establishes, and PS13

PS12 closes a specific quantitative obstruction: the *complete* original signed IMS localization error is now \(<0.683\) in its own graph energy metric. This is a whole-form-domain estimate and a strict improvement over PS07's \(<40\) raw \(L^2\) remainder. It makes the quadratic localization stable and furnishes a usable graph-energy tolerance for subsequent inverse-Gram/Schur calculations.

**PS13** must move beyond shifted graph stability: certify a signed **unshifted interior positivity** estimate on the actual \(\beta\)-localized range, or produce the full inverse-Gram signed Schur PSD with native CC27 D-Riesz domain transfer. Neither a graph-frame bound nor an exact finite-channel prime source independently proves Weil/RH.

**Replay:** \`python3 scripts/validate_rpb108_ps12_arch_ims_hs_frame.py\` reruns PS11→PS10→PS09→PS07→PS06→PS03→RC315 pinned original-source chain, checks the Hilbert–Schmidt support integral and strict *outward rational* bound \(<64/9\), sharp seven-prime norm, localized original pole estimate, strict global normalized signed bound \(<683/1000\) and no-promotion custody. Functional-analytic arguments remain subject to independent review.
