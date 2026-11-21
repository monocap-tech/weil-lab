# PI029 — Arbitrarily many first-prime Gamma cancellations on explicit smooth source tests

**Weil-Lab Potential Interface / ANALYTIC ONLY.** Parent \`research/pi028-three-prime-gamma-crossings\`; registry issue #792. This memo proves a real-analysis result conditional only on the already-source-identified PI027 physical Gamma and von Mangoldt formulas. No new PR, Lean module, Actions workflow/dispatch, NF/IV/CP edits, operator trace, spectral certification, RH or global Weil positivity.

## 1. Main theorem — no uniform finite first-prime crossing bound

Fix PI027's original source width \(d=\log(10/9)\) and \(\lambda_j=2j+1/2\). For **each integer \(N\ge2\)** set
\[
\boxed{\Delta_N=\frac d{N+1},\qquad \ell_N=\frac d{100N^2}.}
\]
Define the explicit standard nonnegative compact smooth bump
\[
b_N(x)=
\begin{cases}
\exp\left(-1/[(x/\ell_N)(1-x/\ell_N)]\right),&0<x<\ell_N,\\
0,&\mathrm{otherwise},
\end{cases}
\quad
\boxed{\rho_N(x)=\sum_{j=1}^N b_N(x-j\Delta_N).}
\]
Its \(N\) pairwise disjoint support intervals are strictly inside \((0,d)\): \(0<\Delta_N\), \(N\Delta_N+\ell_N<d\), \(\Delta_N>2\ell_N\). In particular the same explicit \(\rho_N\) works **simultaneously for every annihilator order \(m\ge1\)**.

For
\[
L_m=D\prod_{j=0}^{m-1}(D^2-\lambda_j^2),\quad
\eta_{m,N}=L_m b_N,\quad
\phi_{m,N}=L_m\rho_N,\quad
C_{m,N}(t)=\int\phi_{m,N}(x)\phi_{m,N}(x-t)\,dx,\quad
J_{m,N}=C_{m,N}(0)>0,
\]
take PI027's unchanged original autocorrelation test \(s_{\beta,m,a}=(\phi_{m,N}+\beta\phi_{m,N}(\cdot-a))/\sqrt2\), \(h_{\beta,m,a}(u)=\int s_{\beta,m,a}(x)\overline{s_{\beta,m,a}(x-u)}\,dx\), with \(|\beta|=1\).

Then the literal pole-minus-prime-plus-Gamma form retains
\[
\boxed{W(h_{\beta,m,a})=W(C_{m,N})+\Theta_{m,N}(a)\Re\beta,\quad
\Theta_{m,N}(a)=B_{m,N}(a)-P_{m,N}(a).}
\]
The poles vanish because \(S_{m,N}(0)=S_{m,N}(\pm1/2)=0\); \(B_{m,N}(a)>0\) for \(a>d\) by PI027's positive Gamma mode expansion, since \(\rho_N\ge0\), nonzero. The genuine prime coefficients are never altered.

**Theorem.** For every \(N\ge2\), and every \(m\ge1\), the function \(\Theta_{m,N}\) has at least \(2N-1\) **distinct** zeros within
\[
\boxed{a\in(\log3-d,\log3).}
\]
At every such zero, \(B_{m,N}=P_{m,N}>0\): the original \(n=3\) arithmetic channel is live, but the complete signed Weil value is independent of unit relative phase. There is **no universal finite upper bound** on first-prime cancellation counts over PI027's admissible nonnegative \(C_c^\infty((0,d))\) bump class. The theorem gives lower bounds, not exact root counts or nonzero derivatives.

## 2. Exact multiple-channel correlation algebra

Let \(Q_{m,N}(t)=\int\eta_{m,N}(x)\eta_{m,N}(x-t)\,dx\), with support in \([-\ell_N,\ell_N]\) and \(q_{m,N}=Q_{m,N}(0)=\|\eta_{m,N}\|_2^2>0\). Nonvanishing of \(\eta_{m,N}\) follows because a nonzero compactly supported smooth function cannot solve \(L_m b=0\) identically for a nonzero constant-coefficient differential operator (equivalently its entire bilateral Laplace transform cannot vanish off a finite root set).

Translations commute with \(L_m\). Expanding the \(N^2\) cross-correlations yields the source-exact identity
\[
\boxed{C_{m,N}(t)=\sum_{k=-(N-1)}^{N-1}(N-|k|)\,Q_{m,N}(t-k\Delta_N).}
\]
Since \(\Delta_N>2\ell_N\), the correlation channels are disjoint. Consequently
\[
J_{m,N}=Nq_{m,N},\qquad
C_{m,N}(k\Delta_N)=(N-k)q_{m,N}=\frac{N-k}{N}J_{m,N}
\quad (0\le k<N),
\]
\[
\boxed{C_{m,N}(\ell_N)=0,\quad
C_{m,N}(k\Delta_N-\ell_N)
=C_{m,N}(k\Delta_N+\ell_N)=0\quad(1\le k<N).}
\]
The zero endpoints are exact because every compact smooth \(Q\) vanishes on and outside \(|t|=\ell_N\); no assumption is made about the sign or unimodality of \(Q(t)\) between centers.

## 3. Genuine sole-n=3 window and stronger narrow-support Gamma bound

Write \(a=\log3-t\), \(0\le t\le d\). Across this **entire** window,
\[
a-d\ge\log(3/(10/9)^2)=\log(243/100)>\log2,\quad
a+d\le\log(10/3)<\log4,
\]
so the only integer \(n\ge2\) whose logarithm may meet the support of the shifted correlation is \(n=3\). Thus
\[
\boxed{P_{m,N}(\log3-t)=\kappa_3 C_{m,N}(t),\qquad
\kappa_3=\frac{\log3}{\sqrt3}>\frac13.}
\]
No other prime powers enter. Crucially, the actual support *measure* of \(\phi_{m,N}\) is bounded by \(N\ell_N\), considerably smaller than the ambient width \(d\). Using PI027's strictly positive mode formula and \(K(v)=e^{-v/2}/(1-e^{-2v})\) for \(v>0\), \(K\) strictly decreasing, one obtains
\[
\begin{aligned}
0<B_{m,N}(a)
&=\left|\iint\phi_{m,N}(x)\phi_{m,N}(y)K(a+x-y)\,dxdy\right|\\
&\le K(a-d)\left(\int|\phi_{m,N}(x)|dx\right)^2\\
&\le K(a-d)\,N\ell_N\,J_{m,N}\\
&<N\ell_N\,J_{m,N}
=\frac{d}{100N}J_{m,N}
<\frac{J_{m,N}}{900N}.
\end{aligned}
\]
The strict \(K(a-d)<K(\log2)=2\sqrt2/3<1\) holds uniformly on the stated window, and the last inequality uses \(d=\log(10/9)<1/9\). No smooth-integral quadrature appears in this bound.

At every center \(t=k\Delta_N\) (\(0\le k<N\)):
\[
\begin{aligned}
\frac{\Theta_{m,N}(\log3-k\Delta_N)}{J_{m,N}}
&<\frac1{900N}-\frac{N-k}{3N}
=\frac{1-300(N-k)}{900N}\\
&\le-\frac{299}{900N}<0.
\end{aligned}
\]
At \(t=\ell_N\) and \(t=k\Delta_N\pm\ell_N\), the prime sample vanishes **exactly**, so \(\Theta=B>0\).

## 4. Explicit 2N−1 disjoint crossing brackets and stability

Let \(A_k=\log3-k\Delta_N\). The strict alternating signs and continuity imply a zero in every one of
\[
\boxed{(\log3-\ell_N,\ \log3)}
\]
(the central peak), and, for each \(k=1,\ldots,N-1\), both
\[
\boxed{(A_k-\ell_N,\ A_k),\qquad(A_k,\ A_k+\ell_N).}
\]
Their interiors are pairwise disjoint by \(\Delta_N>2\ell_N\); all are contained strictly in \((\log3-d,\log3)\). There are \(1+2(N-1)=2N-1\) such brackets, of **exact width \(\ell_N=d/(100N^2)\)** each. The roots have \(B=P>0\), hence live arithmetic cancellation, \(W(D_a)=0\) for \(D_a=h_{1,m,a}-h_{-1,m,a}\), and \(W(h_{\beta,m,a})=W(C_{m,N})\) for all unit \(\beta\).

For each *fixed pair* \((N,m)\), every endpoint sign is strict. Because \(\Theta\) varies continuously with \(\rho\) in a suitably fixed-support smooth topology, all \(2N-1\) sign-changing brackets persist for sufficiently small admissible \(\rho\)-perturbations. The neighborhood size is not claimed uniform in \(N\) or \(m\).

**Derivative witnesses, not root transversality.** Since the amplitude drops at least \(299J_{m,N}/(900N)\) between each positive boundary and negative peak, the mean-value theorem yields at least one interior point in every bracket at which the oriented slope has magnitude greater than
\[
\boxed{\frac{299J_{m,N}}{900N\ell_N}
=\frac{299N}{9d}J_{m,N}.}
\]
The sign of the derivative is negative on the central and lower-a satellite brackets and positive on the upper-a satellite brackets. A steep derivative **somewhere in a bracket** does not imply \(\Theta'(a_*)\ne0\) **at its zero**. The root may be degenerate, and additional roots may lie in any bracket. Transversality and exact counts remain open.

## 5. Fixed IV physical window and complex spectral fingerprint

For \(a\le\log3\) and every \(N\), translate the *two* constituent physical bumps together by \(-1/2\). Their union then lies in the original full physical support window \((-11/10,11/10)\): the leftmost coordinate is \(>\!-1/2\) and the rightmost is \(<\log3+d-1/2<11/10\). Such a common physical translation does not change any correlation \(h\), so preserves the original signed Weil channels. These tests are **not** claimed to lie inside IV's narrower disconnected old-collar support class, nor to inherit its positivity certificates.

For \(\Xi_{m,N}(z)=\int\eta_{m,N}(x)e^{izx}dx\), the positive-sign Fourier transform of \(\phi\) is
\[
\Phi_{m,N}(z)=\Xi_{m,N}(z)\sum_{j=1}^N e^{ij\Delta_N z}.
\]
For the contact-free, pole-null difference \(D_a=h_{1,m,a}-h_{-1,m,a}\), the source-exact complex frequency expression is
\[
\boxed{\widehat D_a(z)=
2\cos(az)\,\Xi_{m,N}(z)\Xi_{m,N}(-z)
\left[N+2\sum_{k=1}^{N-1}(N-k)\cos(k\Delta_N z)\right].}
\]
At a nontrivial zero \(\rho_\zeta=\sigma+i\gamma\), one must evaluate at \(z_\zeta=\gamma-i(\sigma-1/2)\), NOT insert an RH-critical-line modulus-square. CP001's separately unproved *complete-zero* dictionary would require the full zero functional on every such \(D_{a_*}\) to equal \(W(D_{a_*})=0\) after all source/multiplicity/tail gates. The literal printed (not proved here) Masullo Ch12/Ch13 local-factor comparison inherited from PI027 would, **only if both claimed identities actually hold on a common canonical domain**, require
\[
Z_{12}(D_{a_*})=0,\qquad Z_{13,\mathrm{cap}}(D_{a_*})=2B_{m,N}(a_*)>0.
\]
These are conditional fingerprints; no actual spectral series has been computed or certified, and Chapter13's missing proof and factor-two real-place discrepancy remain unresolved.

## 6. Exact regression and PI030 handoff

The companion \`scripts/pi029_unbounded_prime_gamma_crossing_exact.py\` checks the rational geometry, isolated supports, exact channel centers, pure n=3 window and uniform sign margins for \(N=2,\ldots,128\) using Python \`Fraction\`. That finite regression checks the algebraic specializations; **the every-N, every-m theorem is the general proof in Sections 1–4**, not a finite loop result. It performs no smooth integration, derivative-root enclosure, zero enumeration, Lean compilation or Actions work.

**PI029 verdict:** the original signed Weil phase law permits an arbitrarily large number of live first-prime prime/Gamma cancellation crossings, even with the same original \(d=\log(10/9)\) and original von Mangoldt coefficients. No phase-blind graph or single cancellation root can encode this response. **PI030 analytic-only:** investigate simple-root genericity or validated derivative enclosures for selected fixed \(N,m\); retain full source and spectral normalizations and NF certification priority.
