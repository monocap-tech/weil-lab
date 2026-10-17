# PS04 — Original edge/complement coupling is bounded but not compact in physical L²

**W-PHYSICAL-SHIFT**, scoped independent investigation; stacked after PS01–PS03. **Canonical obligation W-ODD-NEG remains OPEN.** No assertion of full signed Weil positivity, full Schur positivity, parity closure, global transfer or RH. This is a sharp qualitative diagnostic for the PS03 edge-elimination proposal, with exact-rational source checks.

## 1. The *actual* off-diagonal form, not a toy Schur matrix

Set \(B=11/10,\ R=2B,\ \ell=\log9,\ a=\ell-B,\ \delta=B-a\). Let
\[
E=[-B,-a]\cup[a,B],\quad F=(-a,a),\quad
H_E=L^2(E),\quad H_F=L^2(F).
\]
The **same** original signed CC27/SI10 form \(Q\) from PS01 applies on its original physical form domain. For supported domain vectors \(f\in H_E,\ h\in H_F\), define the real cross term
\[
\mathcal X(f,h)=Q(f+h)-Q(f)-Q(h)=2\operatorname{Re}b(f,h).
\]
All physical zero extensions are nonperiodic. The constant multiple of \(L^2\)-mass has no cross term because \(E\cap F\) has measure zero. Using PS01's complete digamma difference energy,
\[
\boxed{b_{\rm arch}(f,h)=
-\int_E\int_F k(|x-y|)f(x)\overline{h(y)}\,dy\,dx,
\quad k(u)=\frac{e^{-u/2}}{1-e^{-2u}}.}
\]
The integral can be interpreted by truncation and the Carleman bound below; for bounded step profiles it is absolutely convergent. Its sign is **negative for nonnegative profiles**.

The original seven prime-power term has bilinear bound
\[
|b_{\rm prime}(f,h)|\le 2\sum_{n\in\{2,3,4,5,7,8,9\}}w_n\,\|f\|_2\|h\|_2,\quad
w_n=\Lambda(n)/\sqrt n.
\]
This follows from the cosine Fourier multiplier, which has operator norm at most one; it is not a replacement of the true signed prime source. The actual signed poles obey
\[
|b_{\rm pole}(f,h)|\le
4\sqrt{a\delta}\,\cosh B\,\|f\|_2\|h\|_2.
\]
This comes from \(2|c\rangle\langle c|-2|s\rangle\langle s|\) with \(c=\cosh(x/2),s=\sinh(x/2)\) and the physical lengths \(|E|=2\delta,\ |F|=2a\).

## 2. An explicit bounded true physical cross operator

For \(u>0\),
\[
0<k(u)\le \frac1{2u}+1,
\]
because \(e^{2u}-1\ge2u\). Between each physical edge strip and the interior, \(|x-y|=r+t\) with \(r\in[0,\delta]\), \(t\in[0,2a]\).
The classical Hilbert/Carleman integral inequality
\[
\int_0^\infty\int_0^\infty\frac{|v(r)||w(t)|}{r+t}\,dr\,dt
\le\pi\|v\|_2\|w\|_2
\]
follows, for example, from Schur's positive weight \(r^{-1/2}\) and
\(\int_0^\infty \frac{t^{-1/2}}{r+t}\,dt=\pi r^{-1/2}\).
The bounded constant-kernel piece pays \(\sqrt{2a\delta}\). Sum both edge strips by Cauchy–Schwarz to obtain
\[
|b_{\rm arch}(f,h)|
\le\sqrt2\left(\frac\pi2+\sqrt{2a\delta}\right)\|f\|_2\|h\|_2.
\]
Therefore the **full original signed** off-diagonal form is bounded by
\[
\boxed{\begin{aligned}
|b(f,h)|&\le M\|f\|_2\|h\|_2,\\
M&\le \sqrt2\left(\frac\pi2+\sqrt{2a\delta}\right)
+2\sum_n w_n +4\sqrt{a\delta}\cosh B
<11.
\end{aligned}}
\]
The strict \(11\) is established by outward rational intervals without trusting floating-point tests. This establishes a bounded \(H_F\to H_E\) coupling operator **for independently form-admissible edge/interior vectors**, by continuous extension to the L² spaces. It does **not** establish that an arbitrary completed CC27/D-Riesz form-domain vector can be separated by the sharp edge projector without a further domain-invariance proof.

## 3. A nonzero cross-coupling persists at arbitrarily small seam scale

For \(0<\epsilon<\delta\), use actual physical original-form vectors
\[
f_\epsilon=\epsilon^{-1/2}\mathbf1_{[a,a+\epsilon]},
\qquad
h_\epsilon=\epsilon^{-1/2}\mathbf1_{[a-\epsilon,a]}.
\]
Both have norm one, the first supported in \(E\), the second in \(F\). Their *combined* support has diameter \(2\epsilon<\log2\), so **all seven** original prime-power autocorrelation cross terms vanish, not just six. All original signed pole cross terms are bounded in absolute value by \(4\epsilon\cosh B\).

The nontrivial part is the archimedean seam:
\[
\mathcal X_{\rm arch}(f_\epsilon,h_\epsilon)
=-\frac2\epsilon\int_0^\epsilon\int_0^\epsilon k(r+t)\,dr\,dt.
\]
For \(0<u\le1/2\) there is the **two-sided elementary estimate**
\[
\frac1{2u}-\frac14\le k(u)\le\frac1{2u}+1.
\]
Also,
\[
\frac1\epsilon\int_0^\epsilon\int_0^\epsilon\frac1{r+t}\,dr\,dt
=2\log2.
\]
Hence
\[
-2\log2-2\epsilon-4\epsilon\cosh B
\le\mathcal X(f_\epsilon,h_\epsilon)
\le -2\log2+\frac\epsilon2+4\epsilon\cosh B.
\]
At the concrete exact geometric scale \(\epsilon=\delta/16\), the outward rational upper enclosure establishes
\[
\boxed{\mathcal X(f_\epsilon,h_\epsilon)<-\frac{137}{100}.}
\]
This is a full-original signed cross-energy result, not a PSD or negative-Rayleigh witness: \(Q(f_\epsilon),Q(h_\epsilon)\) individually may be large and positive.

**More strongly, letting \(\epsilon\downarrow0\):**
\[
\boxed{\lim_{\epsilon\downarrow0}\,b(f_\epsilon,h_\epsilon)=-\log2.}
\]
Both \(f_\epsilon\) and \(h_\epsilon\) converge weakly to zero in physical L², being unit vectors supported on shrinking intervals. The **bounded** physical off-diagonal operator \(B:H_F\to H_E\) representing \(b\) is therefore **not compact**. For any compact \(K:H_F\to H_E\),
\[
\|B-K\|_{\rm op}\ge\log2.
\]
Thus finite-rank subtraction cannot make the cross coupling small in the plain physical L² operator norm. The lower essential-norm bound is a rigorous mechanism-level obstruction to naïvely dropping the thin edge, not an obstruction to positive definiteness of the original form.

## 4. Consequences for the next frontier

PS03 gives \(Q|_{H_E}\ge0.3 I\). PS04 gives an L²-bounded but noncompact edge-to-middle cross block of norm at least \(\log2\). The PS03 scalar floor **alone** therefore cannot justify treating this block as a small residual; the form-domain diagonal edge energy is unbounded and may provide much stronger response suppression for near-seam functions.

The appropriate next action is not another smaller edge strip. **PS05 must retain the full positive edge operator and investigate an energy-dual/Riesz Schur norm of the seam Carleman interaction**, including the accurate arch diagonal, original signed seven-prime interactions and poles. In that stronger metric the behavior may differ; no smallness or positive Schur margin is asserted here.

This noncompact L² result does not contradict the SI10 finite-codimension result: SI10 and the RC model employ different projections and forms/dual norms, and PS04 has not transferred either of them.

## 5. Replay and custody

Run \`python3 scripts/validate_rpb108_ps04_edge_schur_coupling.py\`.
The exact-rational validator imports RC315's pinned original operator receipt; checks original logarithmic shifts, full seven weights, source gap, the \(\epsilon=\delta/16\) strict mixed-energy bound, the two-sided kernel bounds, and strict \(M<11\). It also enforces open governance and no automatic promotion.

**Standing:** analytic original-supported bounded-cross/noncompactness theorem and rational envelope, pending final-head Actions and independent review. No completed edge elimination, full odd/even Weil positivity, or RH.
