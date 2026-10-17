# PS05 — The original edge-energy Schur correction is compact despite noncompact physical seam coupling

**W-PHYSICAL-SHIFT** scoped, stacked on PS01–PS04. **Canonical W-ODD-NEG remains OPEN.** This is an analytic compactness theorem and quantitative Fourier-tail bound for the same original signed Weil form on the *separately admissible edge domain*. No claim of a small finite-dimensional Schur residual, positivity of the middle Schur complement, form-domain invariance of sharp edge restriction, whole even/odd Weil positivity, or RH.

## 1. Reconcile PS03 and PS04 without discarding their obstruction

The original CC27/SI10 physically supported signed form from PS01 is
\[
Q(f)=c_{\rm arch}\|f\|_2^2+
\int_0^\infty k(u)\|Zf-\tau_u Zf\|_2^2\,du
-2\sum_{n\in\{2,3,4,5,7,8,9\}}w_n\operatorname{Re}C_f(\log n)
+2|\langle f,c\rangle|^2-2|\langle f,s\rangle|^2
\]
with \(B=11/10\), \(k(u)=e^{-u/2}/(1-e^{-2u})\), \(w_n=\Lambda(n)/\sqrt n\),
\(c_{\rm arch}=-\gamma-\pi/2-3\log2-\log\pi\),
\(c(x)=\cosh(x/2)\) and \(s(x)=\sinh(x/2)\).

Let \(\delta=2B-\log9\), \(a=\log9-B\), \(E=[-B,-a]\cup[a,B]\), \(F=(-a,a)\).
Define \(H_E=L^2(E)\), \(H_F=L^2(F)\).
Let \(\mathcal D_E=\{f\in\operatorname{Dom}Q:\operatorname{supp}f\subseteq E\}\).
The restriction \(q_E=Q|_{\mathcal D_E}\) is a closed, densely defined, symmetric semibounded form on \(H_E\): the full digamma difference form is closed, and the signed seven prime shifts and pole terms are bounded \(L^2\) perturbations; \(\mathcal D_E\) is closed in its form norm since support projection is closed in \(L^2\). Smooth interior edge functions are dense in \(H_E\).

PS03's source-rational original edge theorem provides
\[
q_E(f)\ge c_0\|f\|_2^2,\qquad c_0=3/10.
\]
Let \(A_E\) be the associated positive self-adjoint **original edge operator** (not a scalar replacement). In particular \(A_E\ge c_0I\) and \(A_E^{-1}\) is bounded.

PS04 establishes a bounded offdiagonal **original signed** \(L^2\) cross operator \(B_{EF}:H_F\to H_E\) representing
\[
Q(f+h)-Q(f)-Q(h)=2\operatorname{Re}\langle f,B_{EF}h\rangle
\]
on independently admissible supported vectors. It is **not compact** in \(L^2\), with essential norm at least \(\log2\). The current strict rational upper is \(\|B_{EF}\|<11\).

The question is therefore not whether \(B_{EF}\) is small in plain \(L^2\), but whether the *true positive edge inverse* regularizes its response.

## 2. Explicit original archimedean logarithmic Fourier growth

The archimedean difference term is
\[
\int_{\mathbb R}J(\xi)|\widehat{Zf}(\xi)|^2d\xi,\quad
J(\xi)=2\int_0^\infty k(u)(1-\cos(2\pi\xi u))\,du\ge0 .
\]
For \(0<u\le\tfrac12\), the exact elementary inequality
\[
k(u)\ge\frac1{2u}-\frac14
\]
follows from \(1-e^{-2u}\le2u\) and \(e^{-u/2}\ge1-u/2\).
For \(|\xi|\ge2\), set \(A=1/|\xi|\) and \(t=2\pi|\xi|\). Drop the nonnegative portions outside \([A,1/2]\):
\[
\begin{aligned}
J(\xi)&\ge\int_A^{1/2}\left(\frac1u-\frac12\right)(1-\cos(tu))\,du\\
&\ge\log\frac{|\xi|}{2}-\frac1\pi-\frac12.
\end{aligned}
\]
The signed cosine integral is bounded by integration by parts:
\[
\left|\int_A^{1/2}\frac{\cos(tu)}u\,du\right|
\le\frac2{tA}=\frac1\pi.
\]
For the remaining negative piece, \(\frac12\int_A^{1/2}(1-\cos(tu))du\le\frac12\).
No asymptotic substitution for the original digamma is used.

The edge negative odd pole has the exact support bound from PS03,
\[
-2|\langle f,s\rangle|^2\ge-4\delta\sinh^2(B/2)\|f\|_2^2.
\]
The prime terms obey \(-2\sum_n w_n\operatorname{Re}C_f(\log n)\ge-2\sum_n w_n\|f\|_2^2\), and the positive even pole is retained and safely dropped for this lower bound.

Hence for every \(f\in\mathcal D_E\),
\[
\int_{\mathbb R}J(\xi)|\widehat{Zf}(\xi)|^2d\xi
\le q_E(f)+C_E\|f\|_2^2,
\quad
C_E=-c_{\rm arch}+2\sum_nw_n+4\delta\sinh^2(B/2).
\]
The PS05 rational replay proves the conservative strict bound \(C_E<13\) on the **original seven weights** (including \(\Lambda(4)=\Lambda(8)=\log2,\Lambda(9)=\log3\)), original pole, original normalizations.

Let \(\Lambda\ge 2^2\) (here \(\Lambda\) denotes a frequency cutoff, *not* von Mangoldt's function). Put
\[
L(\Lambda)=\log(\Lambda/2)-\frac1\pi-\frac12.
\]
Whenever \(L(\Lambda)>0\), the **true complete high-frequency Fourier tail** obeys
\[
\boxed{\int_{|\xi|\ge\Lambda}|\widehat{Zf}(\xi)|^2d\xi
\le \frac{q_E(f)+C_E\|f\|_2^2}{L(\Lambda)}
\le\frac{1+C_E/c_0}{L(\Lambda)}q_E(f).}
\]
At \(\Lambda=2^{80}\), the certificate checks *entirely by outward rational inequalities*
\[
L(2^{80})=79\log2-\frac1\pi-\frac12>53,\quad
\frac{1+C_E/c_0}{L(2^{80})}<\frac45.
\]
This large cutoff is a conservative analytic diagnostic—not a competitive 890-source numerical Schur estimate. The right-hand ratio decreases to zero as \(\Lambda\to\infty\).

## 3. Actual compact edge inverse and energy-dual Schur operator

For fixed finite \(\Lambda\), the operator
\[
K_\Lambda=1_E\mathcal F^{-1}1_{[-\Lambda,\Lambda]}\mathcal F1_E:H_E\to H_E
\]
is positive, satisfies \(0\le K_\Lambda\le I\), and is Hilbert–Schmidt on finite-measure \(E\); its kernel is the bounded sinc function
\[
K_\Lambda(x,y)=\frac{\sin(2\pi\Lambda(x-y))}{\pi(x-y)},\quad K_\Lambda(x,x)=2\Lambda.
\]
For \(f\in\mathcal D_E\),
\[
\|(I-K_\Lambda)f\|_2^2\le
\langle f,(I-K_\Lambda)f\rangle
=\int_{|\xi|>\Lambda}|\widehat{Zf}(\xi)|^2d\xi.
\]
The preceding edge-energy tail estimate shows \(K_\Lambda\) approximates the **energy-unit-ball embedding** into \(L^2(E)\) uniformly as \(\Lambda\to\infty\). Since each \(K_\Lambda\) is compact, the embedding
\[
(\mathcal D_E,q_E^{1/2})\hookrightarrow H_E
\]
is compact. Therefore the original restricted edge operator \(A_E\) has **compact resolvent** and \(A_E^{-1/2}\) is compact as an operator on \(H_E\).

Consequently, although \(B_{EF}\) itself is not compact,
\[
\boxed{
A_E^{-1/2}B_{EF}:H_F\to H_E\quad\text{is compact},
}
\]
and the **actual true-edge energy-dual Schur subtraction**
\[
\boxed{
S_{\rm edge}:=B_{EF}^*A_E^{-1}B_{EF}
=(A_E^{-1/2}B_{EF})^*(A_E^{-1/2}B_{EF})
}
\]
is positive compact on \(H_F\).

No false inference that \(\|S_{\rm edge}\|\) is small is made. The crude norm control \(\|S_{\rm edge}\|\le\|B_{EF}\|^2/c_0<121/(3/10)\) is not a positive-Schur certificate. Compactness yields **finite-rank approximability**, not an actionable small residual without quantitative singular-value enclosures in the correct energy norm.

## 4. Domain and acceptance limitations

This compactness result concerns the supported original edge form and the bounded physical cross operator of PS04. It is *not* a claim that sharp multiplication by \(1_E\) preserves the entire original signed form domain. Therefore an arbitrary original-form vector may **not** yet be decomposable into two independently form-admissible vectors \(f_E+f_F\).

On the restricted direct-sum form domain \(\mathcal D_E\oplus\mathcal D_F\), the correct signed Schur complement—when the interior form is realized consistently—is \(q_F-S_{\rm edge}\), which remains wholly unproved positive. The true 890-source SI10/SM/EF or 301/317 RC D-Riesz carrier cannot be replaced merely because \(S_{\rm edge}\) is compact.

**PS06 obligations:** (i) certify the sharp-edge projector/domain split or introduce a smooth energy-stable partition; (ii) construct a *quantitative*, signed and physically supported finite-rank approximation for \(A_E^{-1/2}B_{EF}\); (iii) provide a verified norm/domain attachment to the canonical original CC27 D-Riesz form; (iv) close an actual Schur/PSD gate before any promotion.

## 5. Verification

\`python3 scripts/validate_rpb108_ps05_energy_dual_compactness.py\` must pin the original RC313/315 source identity, replay the original PS03 edge gap and original seven prime weights, verify the explicit high-frequency logarithmic lower and strict \(2^{80}\) tail coefficient by rational arithmetic, record that compactness is analytic and that no finite Schur PSD has been computed, and keep W-ODD-NEG and RH OPEN.

**Standing:** mathematical derivation plus exact rational constant/source gate, subject to focused CI, independent mathematical review and formal domain transfer. This is a genuine operator-level regularization statement relative to PS04, not a proof of RH.
