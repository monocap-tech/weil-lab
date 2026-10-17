# PS10 — Complete original seven-prime IMS channel graph; exact thirteen-to-five fiber reduction

**Lane:** W-PHYSICAL-SHIFT (scoped parallel investigation), stacked on PS01–PS09. **Canonical W-ODD-NEG remains OPEN**. This checkpoint obtains a **global exact** decomposition of the **entire original seven-prime part of the PS07 quadratic IMS localization remainder**, not merely the PS09 triad compression. It gives an exact sharp **full prime-IMS operator norm**, a 13-channel physical fiber with only five active channels, and a stronger essential-norm bound for the complete signed IMS remainder. It does **not** reduce the full signed Weil form or its archimedean operator to finite dimensions, does **not** compute an energy-inverse matrix or sign of a Schur complement, and makes no RH claim.

## 1. Geometry: 13 disjoint entire-source channels, not just a triad

Work on the **original physical interval** \(I=[-B,B]\), \(B=11/10\), with \(N_0=\{2,3,4,5,7,8\}\), \(\ell=\log9=2\log3\), \(\delta=2B-\ell>0\), and the original PS06/07 angle \(\theta=(\pi/2)\chi\). Write \(\theta_L(t)=\theta(-B+t)=z(t)\) and \(\theta_R(t)=\theta(-B+\ell+t)=\pi/2-z(t)\), \(0\le t\le\delta\). All other points below have angle zero.

Define the 13 **distinct exact offsets**
\[
\mathcal O=
\{0,\log9\}
\cup\{\log n:n\in N_0\}
\cup\{\log(9/n):n\in N_0\setminus\{3\}\}.
\]
These represent physical intervals
\[
I_o=[-B+o,-B+o+\delta]\quad(o\in\mathcal O).
\]
Because \(\log3=\log(9/3)\) **exactly**, the two candidate \(n=3\) interior channels are identical; no other offsets coincide. Exact-rational logarithm enclosures verify the **minimum distinct offset gap exceeds \(1/10\)**, while \(\delta<1/350\). Thus all 13 intervals are disjoint and lie in \(I\); all 11 interior channels are strictly inside the zero-angle core of \(\chi\).

The only nonzero prime-IMS edges in the *whole original physical interval* are:
- left hub \(L=I_0\) to \(I_{\log n}\), for every \(n\in N_0\);
- right hub \(R=I_{\log9}\) to \(I_{\log(9/n)}\), for every \(n\in N_0\);
- the single original \(n=9\) link \(L\leftrightarrow R\).

Both \(n=3\) links meet at **the same** central interval \(I_{\log3}\), producing the PS09 triad. The other five spokes on either side are distinct. All prime-IMS edges keep the original weights \(w_n=\Lambda(n)/\sqrt n\) and physical zero extension.

**Why this is globally complete for the prime-IMS defect:** If \(\eta(x,y)=2[1-\cos(\theta(x)-\theta(y))]\neq0\) and \(|x-y|=\log n\), at least one endpoint belongs to an edge-active subset of \(I_0\) or \(I_{\log9}\). Since every \(\log n\ge\log2>\delta\), positive shifts cannot connect points within one edge. For \(n\le8\), they cannot connect the opposite edges, because \(\log8<2a\) where \(a=\ell-B\). Thus the other endpoint belongs to precisely one of the enumerated translated interior intervals. For \(n=9\), the entire admissible translation is \(I_0\leftrightarrow I_{\log9}\). Consequently the global prime-IMS operator vanishes on the **orthogonal complement** of the union of these 13 intervals, and cannot couple that complement to these intervals. This is stronger than a mere finite-row compression but does not include the archimedean or pole parts.

## 2. Exact \(13\times13\) fiber, reduced to \(5\times5\) by a fixed isometry

The map
\[
U:\bigoplus_{o\in\mathcal O}L^2(I_o)\longrightarrow
L^2([0,\delta];\mathbb C^{13}),
\quad (Uf)_o(t)=f(-B+o+t)
\]
is unitary. Under \(U\), the **entire** original prime contribution to the IMS remainder, not the original prime form itself, is *multiplication* by a real symmetric 13-by-13 weighted adjacency \(M(t)\), zero on all other \(L^2(I)\) directions. Put
\[
p(t)=1-\cos z(t),\quad q(t)=1-\sin z(t),\quad
c(t)=w_9[1-\sin2z(t)].
\]
The nonzero entries (symmetric counterparts understood) are
\[
M_{L,\log n}=w_np,\qquad
M_{R,\log(9/n)}=w_nq\quad(n\in N_0),\qquad
M_{L,R}=c.
\]
For \(n=3\), the two entries touch the same shared vertex. The diagonal and all unlisted entries are **exactly zero**. These coefficients follow from PS07's actual original signed \(\eta/2\), with no periodic wrapping or missing signed sources.

Let \(N_5=\{2,4,5,7,8\}\) and set
\[
W_5^2=\sum_{n\in N_5}w_n^2,\qquad
u_L=W_5^{-1}\sum_{n\in N_5}w_n e_{\log n},\quad
u_R=W_5^{-1}\sum_{n\in N_5}w_n e_{\log(9/n)}.
\]
The 5-dimensional space spanned by \((e_L,e_R,e_{\log3},u_L,u_R)\) is **invariant for every fiber**, with \(8\) orthogonal **common null modes**, and the exact effective matrix
\[
\boxed{
M_{\rm eff}(z)=
\begin{pmatrix}
0&c&w_3p&W_5p&0\\
c&0&w_3q&0&W_5q\\
w_3p&w_3q&0&0&0\\
W_5p&0&0&0&0\\
0&W_5q&0&0&0
\end{pmatrix}.
}
\]
Thus **13 physical translation channels reduce exactly to five active fiber modes**. This is a constant-size matrix-valued function over an **infinite-dimensional** \(L^2([0,\delta])\) fiber: it is **not** a rank-five approximation in physical \(L^2\).

## 3. A sharp exact operator norm for the entire original prime IMS defect

Let \(M_L\) and \(M_R\) be the two fiber endpoint matrices, realized at \(z=\pi/2\) and \(z=0\) respectively. Each is a weighted star whose hub has exactly seven edges, namely the original \(n\in N_0\) six prime powers and the original \(n=9\) pole-free prime-power edge. Their operator norms are **equal**
\[
\rho_7=\sqrt{\sum_{n\in N_0}w_n^2+w_9^2}.
\]
For all \(0\le z\le\pi/2\), \(p,q\ge0\), and
\[
p+q=2-(\sin z+\cos z)\le1.
\]
Moreover
\[
1-\sin2z\le p+q
\]
because \(s+c-1=2sc/(s+c+1)\le2sc\) for \(s=\sin z,c=\cos z\). Therefore **every nonnegative entry** of \(M(z)\) is bounded by the corresponding entry of \(pM_L+qM_R\). For real symmetric entrywise-nonnegative matrices, such domination bounds the operator norm; convexity gives
\[
\|M(z)\|\le\|pM_L+qM_R\|
\le(p+q)\rho_7\le\rho_7.
\]
The outer-quarter plateaux \(t\in[0,\delta/4]\) and \(t\in[3\delta/4,\delta]\) realize \(M_L\) and \(M_R\) on sets of positive measure. **Therefore**
\[
\boxed{
\|\mathcal R_{\rm prime}\|_{\mathcal B(L^2(I))}
=\rho_7
=\sqrt{
\frac{(\log2)^2}{2}
+\frac{(\log3)^2}{3}
+\frac{(\log2)^2}{4}
+\frac{(\log5)^2}{5}
+\frac{(\log7)^2}{7}
+\frac{(\log2)^2}{8}
+\frac{(\log3)^2}{9}
}.
}
\]
The original \(n=8\) weight uses \(\sqrt8\), so \(w_8^2=(\log2)^2/8\). Outward exact-rational certificates establish
\[
\boxed{\frac{1419}{1000}<\rho_7<\frac{1420}{1000}}.
\]
This **sharp whole-prime IMS norm** substantially replaces PS07's coarse prime-error allowance \(2\sum_nw_n\approx7.075006\), but makes no comparable new bound on the arch and pole remainders.

## 4. Stronger full-original IMS essential-norm lower; correct interpretation

The original archimedean IMS remainder is Hilbert–Schmidt (PS07), and the two signed pole remainders are finite rank. Hence the complete original signed quadratic IMS defect \(\mathcal R\) is a **compact perturbation** of \(\mathcal R_{\rm prime}\). Since the plateau star eigenvalues \(\pm\rho_7\) each have infinite multiplicity as fiber multiplication values,
\[
\boxed{
\|\mathcal R\|_{\rm essential}
=\|\mathcal R_{\rm prime}\|_{\rm essential}
=\rho_7>1.419.
}
\]
In particular the **essential spectrum of \(\mathcal R\) contains both \(\pm\rho_7\)** (by invariance of essential spectrum under compact self-adjoint perturbations). This sharpens PS09's \(2\log3/3\approx0.732408\) lower.

Note carefully: this is essential spectrum of the **IMS remainder**, not of \(q\), not a negative Rayleigh direction for the original Weil form, and not an RH claim. The original full Weil quadratic form retains its unbounded archimedean energy, native prime shifts, and two poles.

## 5. What PS10 changes and what remains

The *complete* prime-IMS defect no longer requires any spatial uniform gridding: a fixed 5-by-5 fiber handles its entire prime-weighted physical interaction exactly. This eliminates PS08's \(2^{8206}\) uniform-grid expense **for this component only**. The full graph-energy-normalized defect \(H^{-1/2}\mathcal R H^{-1/2}\) still involves the arch and pole corrections and the nonlocal energy inverse \(H^{-1/2}\), which do **not** preserve the 13-channel subspace or the five effective modes automatically.

**PS11:** attach the **true energy inverse** and the compact arch/pole contributions to this exact source graph, certify quantitative residuals in a practically computable energy-adapted basis, and test an actual signed Schur/PSD margin on the original domain. A complete CC27 D-Riesz identification and independent review are separate mandatory gates.

## 6. Verification and limitations

\`python3 scripts/validate_rpb108_ps10_full_prime_graph.py\` replays the pinned RC313/315 original source through PS09's ancestors, verifies all 13 exact-rational channel offsets and >1/10 separations, checks the 13-edge adjacency and five-mode common-null reduction, all original weights and original pole custody, the sharp exact \(\rho_7\) margin, and governance W-ODD-NEG still OPEN. The continuous-fiber operator proof above is analytic and subject to independent mathematical review; successful rational CI is not a substitute for an independently validated full signed Schur or RH proof.
