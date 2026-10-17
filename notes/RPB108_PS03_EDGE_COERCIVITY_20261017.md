# PS03 — Uniform original signed Weil coercivity on an infinite-dimensional physical edge subspace

**Status:** W-PHYSICAL-SHIFT scoped analytic theorem; independent source-rational replay required. **Canonical active obligation:** W-ODD-NEG (unchanged, OPEN). Parents: PS01 full original signed physical difference-energy identity, PS02 exact log9 parity edge-strip geometry, RC313/315 original seven-prime translation/pole custody.

## 1. The new bound is genuinely infinite dimensional, not another witness

Fix the **original** physical interval \(I=[-B,B]\), \(B=11/10\), and its original signed Weil form
\[
Q(g)=\int_{\mathbb R}\left(\operatorname{Re}\psi(1/4+i\pi\xi)-\log\pi
-2\sum_{n\in N}\frac{\Lambda(n)}{\sqrt n}\cos(2\pi\xi\log n)\right)
|\widehat{Zg}(\xi)|^2d\xi
+2|\langle g,c\rangle|^2-2|\langle g,s\rangle|^2,
\]
with \(N=\{2,3,4,5,7,8,9\}\), \(c=\cosh(x/2)\), \(s=\sinh(x/2)\).

Let
\[
\ell=\log9,\quad a=\ell-B,\quad
\delta=B-a=2B-\ell,\quad
S=[-B,-a]\cup[a,B].
\]
Certified exact-rational log enclosures imply \(1<a<B\), \(0<\delta<1/350\), and \(2a>2>\log8\).

**PS03 theorem.** For every \(g\) in the original signed form domain with \(\operatorname{supp}(g)\subseteq S\),
\[
\boxed{\qquad Q(g)>\frac{3}{10}\|g\|_{L^2(I)}^2\quad(g\ne0).\qquad}
\]
This applies simultaneously to *all even, odd and mixed-parity edge-supported functions* and hence to an infinite-dimensional physical subspace. The result is a lower bound for the **same original signed Weil quadratic form**, not for a modified cap, a diagonal witness, or an auxiliary reference.

## 2. Exact original prime translation support gap

Let \(G=Zg\) and \(C_g(u)=\int_\mathbb R G(x)\overline{G(x+u)}dx\). On the two edge intervals, the within-edge overlap vanishes at shifts \(u\ge\delta\); between opposite edges, the overlap vanishes for \(0<u\le2a\). Therefore
\[
C_g(u)=0\quad\text{for every }\delta\le u\le 2a,
\quad D_g(u):=\|G-\tau_uG\|_2^2=2\|g\|_2^2.
\]
In particular, all six original primes \(n\in\{2,3,4,5,7,8\}\) have \(\ell_n=\log n\in(\delta,2a)\) and have **exactly zero** signed prime contribution. (This is stronger than PS02, which only canceled their Hankel reflection pieces.)

For \(n=9\), \(\tau_\ell\) maps the left edge interval onto the right edge interval. Cauchy–Schwarz and \(2ab\le a^2+b^2\) yield the uniform coupled sharp bound
\[
|C_g(\ell)|\le \|G\mathbf1_{[-B,-a]}\|_2
\|G\mathbf1_{[a,B]}\|_2\le\tfrac12\|g\|_2^2.
\]
With the *true* signed prime-power weight \(w_9=\Lambda(9)/\sqrt9=\log3/3\),
\[
-2\sum_{n\in N}w_n\operatorname{Re}C_g(\log n)
=-2w_9\operatorname{Re}C_g(\ell)
\ge -w_9\|g\|_2^2.
\]
No prime-frequency proxy, wraparound, or assumption of independent positive directions is used.

## 3. Certified full archimedean difference-energy recovery

By PS01's digamma identity,
\[
Q(g)=c_{\mathrm{arch}}\|g\|_2^2
+\int_0^\infty k(u)D_g(u)\,du
-2\sum_{n\in N}w_n\operatorname{Re}C_g(\log n)
+2|\langle g,c\rangle|^2-2|\langle g,s\rangle|^2,
\]
where
\[
c_{\mathrm{arch}}=\psi(1/4)-\log\pi
=-\gamma-\frac\pi2-3\log2-\log\pi,
\qquad k(u)=\frac{e^{-u/2}}{1-e^{-2u}}>0.
\]
In the entire gap \([\delta,2]\subseteq[\delta,2a]\) the exact difference energy is \(D_g(u)=2\|g\|^2\), independently of the detailed oscillation of \(g\).

Use the following *elementary global-on-subinterval* kernel lower bounds:
\[
k(u)\ge\frac{1}{2u}-\frac14\quad(0<u\le1/2),
\qquad k(u)>\frac25\quad(1/2\le u\le3/2),
\qquad k(u)>\frac13\quad(3/2\le u\le2).
\]
The first follows \(1-e^{-2u}\le2u\), \(e^{-u/2}\ge1-u/2\). The second follows \(1-e^{-2u}<1\), \(e^{-3/4}>2/5\), itself elementary by bounding \(e^{3/4}<5/2\); the third follows \(e^{-1}>1/3\) (since \(e<3\)).

Consequently, with \(\delta<1/350\),
\[
2\int_\delta^2 k(u)\,du
>\log\frac{1/2}{\delta}
-\frac{1/2-\delta}{2}+\frac45+\frac13
>\log175-\frac14+\frac45+\frac13.
\]
This rigorous lower bound includes the entire continuum \(\delta\le u\le2\), not a finite frequency subset; the remaining nonnegative difference energy is safely discarded.

The original even pole is nonnegative. For the actual negative odd pole, \(|s(x)|\le\sinh(B/2)\) on \(S\), \(|S|=2\delta\), giving
\[
-2|\langle g,s\rangle|^2
\ge-4\delta\sinh^2(B/2)\|g\|_2^2.
\]

Combine without discarding **any negative original contribution**:
\[
\boxed{
Q(g)\ge \mathfrak c\,\|g\|_2^2,\qquad
\mathfrak c=
c_{\rm arch}
+\log175-\tfrac14+\tfrac45+\tfrac13
-\frac{\log3}{3}
-4\delta\sinh^2(B/2)> \frac3{10}.
}
\]
The strict rational test uses outward enclosures of Euler \(\gamma\), Machin \(\pi\), \(\log(2),\log(3),\log(5),\log(7)\), and \(\sinh(B/2)\), without floating-point acceptance. Note \(\log175=\log7+2\log5\) for sharp rational atanh convergence.

## 4. Correct mathematical meaning

PS02 showed the difference \(Q_{\rm even}-Q_{\rm odd}\) is indefinite under the half-interval identification. PS03 shows the **two individual original signed forms are both uniformly positive on the same infinite-dimensional edge strip**. There is no contradiction: two positive operators need not be ordered.

The edge-strip theorem is not a result about the full original form, the whole complement of the edge strip, or the Schur coupling between the edge space and its complement. In particular, positivity on the edge subspace alone does **not** allow deleting it from the remaining 890-source or 301/317-source problem. The exact cross block, admissible closed-domain projection and residual Schur loss are open.

This is a potentially useful new physical boundary reference. The next mathematical discriminator is whether a verified high-elimination cross estimate converts edge coercivity into an improved *full-carrier* Schur margin, not merely a new positive infinite-dimensional subspace.

A dense compactly supported smooth core in the open edge strips satisfies the formulas directly. For other members of the completed signed form domain supported in \(S\), extend by form-continuity using the bounded prime/pole terms and nonnegative closed digamma difference-energy form; the inherited original-form/CC27 transfer must still be checked in its \(D\)-Riesz model.

## 5. Verification and governance

Run
\`python3 scripts/validate_rpb108_ps03_edge_coercivity.py\`.
This validator must (i) pin old RC313/315 original-operator evidence, (ii) verify the seven actual shifts and the exact gap, (iii) derive a rational strict \(3/10\) margin using only lower/upper enclosures, (iv) confirm canonical \`W-ODD-NEG\` unchanged, and (v) never call this RH, whole Weil positivity or complete parity positivity.

**Standing:** source-verified analytic original-form edge coercivity, after focused final-head CI; not independent mathematical review or Lean formalization.
