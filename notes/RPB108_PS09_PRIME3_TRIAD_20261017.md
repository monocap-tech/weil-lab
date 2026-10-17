# PS09 — Exact log(3)–log(9) three-channel resonance in the original signed IMS remainder

**W-PHYSICAL-SHIFT** independent scoped investigation; stacked on PS08. **Canonical W-ODD-NEG remains OPEN.** This is an exact *infinite-dimensional finite-channel* decomposition and a sharper essential-norm obstruction for the real original IMS remainder. It does **not** compute a finite-rank Galerkin matrix, a signed Schur PSD, a native CC27 D-Riesz bridge, whole odd/even Weil positivity or RH.

## 1. A non-apparent exact geometric resonance

Let \(B=11/10\), \(\ell_3=\log3\), \(\ell_9=\log9=2\log3\),
\[
\delta=2B-\ell_9,\quad a=\ell_9-B,\quad T=[0,\delta].
\]
Define three **actual intervals in the original physical support** by
\[
I_L=-B+T=[-B,-a],\qquad
I_M=-B+\ell_3+T=[\ell_3-B,B-\ell_3],\qquad
I_R=-B+\ell_9+T=[a,B].
\]
All have exactly equal width \(\delta>0\); they are mutually disjoint and contained in \([-B,B]\). Translation by \(\ell_3\) maps \(I_L\to I_M\to I_R\), while translation by \(\ell_9\) maps \(I_L\to I_R\). The identity \(\ell_9=2\ell_3\) is *exact*, not an approximate spectral coincidence.

For a physical function supported on their union, identify
\[
f\longleftrightarrow (f_L,f_M,f_R)\in L^2(T;\mathbb C^3),
\quad f_j(t)=f(-B+t+j\ell_3),\quad j=0,1,2.
\]
This is a unitary L² fiber-coordinate transformation. In particular the true original signed seven-prime translation form restricts on this triad to only the **\(n=3\) and \(n=9\) shifts**. For \(n\in\{2,4,5,7,8\}\), exact log enclosures give
\[
\operatorname{dist}(\log n,\{\log3,\log9\})>\delta,
\]
so none of those five shifts connects any two of the triad intervals. (The full operator still couples this triad to exterior intervals; this is an exact **compression**, not a reducing subspace.)

## 2. Exact original quadratic-IMS prime fiber matrix

Use PS07's original **quadratic** IMS masks
\[
\theta(x)=\frac\pi2\chi(x),\quad\alpha=\sin\theta,\quad\beta=\cos\theta,\quad
\eta(x,y)=2[1-\cos(\theta(x)-\theta(y))].
\]
The PS06 collar mask is even and linear on each edge transition. On the three translated intervals,
\[
\theta_M(t)=0,\qquad
\theta_L(t)+\theta_R(t)=\frac\pi2.
\]
Write \(z=\theta_L(t)\in[0,\pi/2]\), so \(\theta_R=\pi/2-z\). The *actual original signed prime portion of the IMS remainder*, \(R_{\rm prime}[f]=q_{\rm prime}[\alpha f]+q_{\rm prime}[\beta f]-q_{\rm prime}[f]\), satisfies the exact full-fiber identity
\[
\boxed{\quad
R_{\rm prime}[f]=\int_0^\delta \mathbf f(t)^*\,M(z(t))\,\mathbf f(t)\,dt ,
\quad
M(z)=\begin{pmatrix}
0&a(z)&c(z)\\
a(z)&0&b(z)\\
c(z)&b(z)&0
\end{pmatrix},}
\]
where **the true original von Mangoldt weights** are
\[
w_3=\frac{\log3}{\sqrt3},\quad w_9=\frac{\log3}{3},
\]
\[
a(z)=w_3(1-\cos z),\qquad
b(z)=w_3(1-\sin z),\qquad
c(z)=w_9(1-\sin2z).
\]
No other original prime powers contribute **within this 3-channel compression**; the original arch remainder and signed rank-one poles are retained separately, not discarded.

Because \(0\le z\le\pi/2\) gives \(\sin z+\cos z\ge1\), and \(0\le1-\sin2z\le1\), each row sum of the **nonnegative symmetric** matrix \(M(z)\) is bounded by \(w_3+w_9\). Hence for every profile \(\mathbf f\),
\[
\boxed{
|\langle \mathbf f,M\mathbf f\rangle|
\le(w_3+w_9)\|\mathbf f\|_{L^2(T;\mathbb C^3)}^2,
\qquad w_3+w_9<101/100.
}
\]
This is a rigorous *operator bound on the true three-channel prime compression*, independent of any spatial Fourier discretization.

## 3. Exact analytically diagonalized plateau and essential-norm improvement

On the nonempty physical collar plateau \(0\le t\le\delta/4\),
\[
z(t)=\pi/2,\quad
\theta_R=0,\quad
M(z)=M_0:=
\begin{pmatrix}
0&w_3&w_9\\
w_3&0&0\\
w_9&0&0
\end{pmatrix}.
\]
Its eigenvalues are **exactly**
\[
\boxed{
\operatorname{spec}M_0=
\left\{-\rho,0,+\rho\right\},
\qquad \rho=\sqrt{w_3^2+w_9^2}=\frac{2\log3}{3}.
}
\]
Exact outward rational logarithm checks establish
\[
\frac{732}{1000}<\rho<\frac{733}{1000}.
\]
Each eigenvalue has **infinite multiplicity** for the plateau multiplication operator, since the eigenvector can be multiplied by arbitrary \(L^2(0,\delta/4)\) functions.

The PS07 original full signed IMS remainder \(\mathcal R\) has the same compression to the triad **plus** the original archimedean Hilbert–Schmidt correction and the original finite-rank pole correction. Their compressions are compact. For any orthonormal sequence \(e_j\) in \(L^2(0,\delta/4)\), the plateau fiber eigenvectors \(v_\pm e_j\) converge weakly to zero and
\[
\langle v_\pm e_j,\mathcal R(v_\pm e_j)\rangle
\longrightarrow \pm\rho .
\]
Therefore
\[
\boxed{
\|\mathcal R\|_{\rm essential}\ge\frac{2\log3}{3}>0.732,
}
\]
strictly improving PS07's \((\log2)/\sqrt2>0.49\) physical essential-norm lower bound.

**Important:** This asserts essential *numerical-range* values for the true whole operator and essential-spectrum values for its 3-channel **compression**. The compressed eigenvalues need not be eigenvalues of the full uncompressed \(\mathcal R\). Neither \(-\rho\) nor \(+\rho\) is a negative or positive statement about the original full signed Weil quadratic form \(q\): \(\mathcal R\) is only the IMS correction.

## 4. Why this changes the next computational obligation

PS08's gigantic \(2^{8206}\) rank arises from approximating the **entire** physical IMS remainder by a uniform spatial grid and scalar logarithmic Fourier bound. PS09 identifies part of its noncompact prime structure that can instead be handled **exactly as a three-by-three matrix over a continuous physical fiber**:

- the triad needs **three source channels**, not a huge cell count, to represent the original \(3\)-\(9\) signed prime interactions;
- the variation in \(t\) is explicit via the elementary cut-off angle \(z(t)\);
- the entire arch/pole corrections, the other original five prime interactions **outside** the triad and the signed graph-energy inverse remain genuine separate obligations.

This is a useful geometry-adapted **channel compression**, **not** a finite-rank L² approximation. One must not assert that three dimensions now solve PS08's full finite-rank problem or that the other signed channels vanish globally.

**PS10:** build a complete exact prime-translation channel adjacency graph with overlap-aware finite physical interval cells, retain cross-triad channels, and couple it to arch/pole and energy-inverse residual certificates on the *same* original form domain. Progress requires a genuinely computable certified full signed Schur bound, not just another isolated channel diagonalization.

## 5. Verification and custody

\`python3 scripts/validate_rpb108_ps09_prime3_triad.py\` replays PS07's pinned RC313/315 original form receipt and original signed seven-prime weights, verifies \(\log9=2\log3\) as the exact number-theoretic source identity, interval containment and non-prime3/9 source separation, the cosine/sine IMS mask plateau, the exact symbolic \(3\times3\) eigenvalue formula and strict outward rational margins, and preserves W-ODD-NEG and RH as OPEN.

The rational validator certifies the source identities and inequalities; it is not an independent machine-formalized proof of the functional-analytic operator statements.
